# -*- coding: utf-8 -*-
"""
SOXX(及其他自定义ticker)期权日报生成脚本 — v2
------------------------------------------------
本版本逻辑：

1. 找出"最近到期日"(比如今天是最近一个周五到期，就是这个日期)，
   列出这一天到期的期权里，未平仓量最高的5个看涨 + 5个看跌(含行权价、最新价)

2. 找出"离今天大约一个月"的到期日(比如今天+30天前后最接近的那个到期日，
   通常是月度到期日)，同样列出未平仓量最高的5个看涨 + 5个看跌

3. 在"一个月以内到期"的所有合约里，对比今天和前一个交易日的未平仓量，
   列出增加最多的5个合约(疑似有资金新建仓位)

4. 每天多伦多时间上午10:30和下午4:30各发一次Discord消息。GitHub Actions对
   "间隔短于1小时"的定时任务经常会静默丢弃大部分触发(不报错，就是不执行)，
   所以工作流改成了"整点触发、间隔1小时"这种GitHub认为可靠的频率，在每个
   目标时间前后安排几次独立的整点尝试作为备份。脚本自己判断"现在的多伦多
   本地时间是否接近10:30或16:30"，命中就发，没命中就跳过；同一天同一个
   时段只会真正发送一次(靠 data/history/_sent_log.json 记录，防止多次整点
   尝试都命中同一个时段时重复发送)。

本脚本设计给完全不懂Python的人使用：正常情况下你不需要改这个文件，
只需要改 config/tickers.txt 来增删关注的股票。
"""

import os
import json
import datetime
from zoneinfo import ZoneInfo
import requests

import pandas as pd
import yfinance as yf

# ---------- 基本配置 ----------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TICKERS_FILE = os.path.join(BASE_DIR, "config", "tickers.txt")
HISTORY_DIR = os.path.join(BASE_DIR, "data", "history")

FETCH_WINDOW_DAYS = 40   # 抓取数据的窗口(留一点buffer，确保能覆盖到月度到期日)
ANOMALY_WINDOW_DAYS = 35  # "一个月以内"窗口(留一点buffer，确保能覆盖到月度到期日，
                           # 比如今天到下个月同一天有时是31-35天，避免把它排除在外)
TOP_N = 5

TORONTO_TZ = ZoneInfo("America/Toronto")
# 每天想发送的两个时间点(多伦多本地时间)
TARGET_SESSIONS = [
    ("早报", 10, 30),
    ("午报", 16, 30),
]
TOLERANCE_MINUTES = 75  # 实测发现GitHub免费额度的定时任务，早上时段的延迟
                         # 可能超过60分钟，所以把容差进一步放宽，配合每小时
                         # 连续触发，确保目标时间前后有更充足的缓冲。


# ---------- 判断现在是不是该发送的时段 ----------
def get_current_session():
    now = datetime.datetime.now(TORONTO_TZ)

    # 手动测试用：workflow_dispatch里勾选"强制发送"时，跳过时间检查
    if os.environ.get("FORCE_SEND", "false").lower() == "true":
        # 挑离现在最近的一个时段名称，只是用来给消息标题用，不影响内容
        closest = min(
            TARGET_SESSIONS,
            key=lambda s: abs((now.replace(hour=s[1], minute=s[2], second=0, microsecond=0) - now).total_seconds())
        )
        print(f"[FORCE_SEND] 手动测试模式，忽略时间检查，强制按「{closest[0]}」发送。")
        return closest[0], now

    for name, hh, mm in TARGET_SESSIONS:
        target = now.replace(hour=hh, minute=mm, second=0, microsecond=0)
        diff_minutes = abs((now - target).total_seconds()) / 60
        if diff_minutes <= TOLERANCE_MINUTES:
            return name, now
    return None, now


# ---------- 防止15分钟检查一次导致同一时段重复发送 ----------
def _sent_log_path():
    return os.path.join(HISTORY_DIR, "_sent_log.json")


def already_sent_today(session_name, today_str):
    path = _sent_log_path()
    if not os.path.exists(path):
        return False
    try:
        with open(path, "r", encoding="utf-8") as f:
            log = json.load(f)
    except Exception:
        return False
    return log.get("date") == today_str and session_name in log.get("sessions", [])


def mark_sent(session_name, today_str):
    os.makedirs(HISTORY_DIR, exist_ok=True)
    path = _sent_log_path()
    log = {"date": today_str, "sessions": []}
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                existing = json.load(f)
            if existing.get("date") == today_str:
                log = existing
        except Exception:
            pass
    if session_name not in log["sessions"]:
        log["sessions"].append(session_name)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(log, f, ensure_ascii=False)


# ---------- 读取ticker列表 ----------
def load_tickers():
    tickers = []
    with open(TICKERS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            tickers.append(line.upper())
    return tickers


# ---------- 抓取标的现价 ----------
def fetch_underlying_price(ticker_symbol):
    """返回 (现价, 前收盘价)，都拿不到时返回 (None, None)"""
    tk = yf.Ticker(ticker_symbol)
    price, prev_close = None, None

    # 方法1：fast_info(比较快，通常够用)
    try:
        fi = tk.fast_info
        price = fi.get("last_price") if hasattr(fi, "get") else getattr(fi, "last_price", None)
        prev_close = fi.get("previous_close") if hasattr(fi, "get") else getattr(fi, "previous_close", None)
    except Exception as e:
        print(f"[警告] fast_info获取{ticker_symbol}现价失败: {e}")

    # 方法2：如果方法1没拿到，退而用history兜底
    if price is None:
        try:
            hist = tk.history(period="5d")
            if not hist.empty:
                price = float(hist["Close"].iloc[-1])
                if len(hist) > 1:
                    prev_close = float(hist["Close"].iloc[-2])
        except Exception as e:
            print(f"[警告] history获取{ticker_symbol}现价失败: {e}")

    return price, prev_close


# ---------- 抓取期权链 ----------
def fetch_option_chain(ticker_symbol, max_days=FETCH_WINDOW_DAYS):
    tk = yf.Ticker(ticker_symbol)
    today = datetime.date.today()

    try:
        expirations = tk.options
    except Exception as e:
        print(f"[警告] 无法获取 {ticker_symbol} 的到期日列表: {e}")
        return pd.DataFrame()

    frames = []
    for exp_str in expirations:
        exp_date = datetime.datetime.strptime(exp_str, "%Y-%m-%d").date()
        days_out = (exp_date - today).days
        if days_out < 0 or days_out > max_days:
            continue
        try:
            chain = tk.option_chain(exp_str)
        except Exception as e:
            print(f"[警告] 跳过 {ticker_symbol} {exp_str}: {e}")
            continue

        calls = chain.calls.copy()
        calls["type"] = "Call"
        puts = chain.puts.copy()
        puts["type"] = "Put"

        both = pd.concat([calls, puts], ignore_index=True)
        both["expiration"] = exp_str
        both["days_to_exp"] = days_out
        both["ticker"] = ticker_symbol
        frames.append(both)

    if not frames:
        return pd.DataFrame()

    df = pd.concat(frames, ignore_index=True)
    keep_cols = ["ticker", "contractSymbol", "expiration", "days_to_exp", "type",
                 "strike", "lastPrice", "bid", "ask", "volume", "openInterest"]
    for c in keep_cols:
        if c not in df.columns:
            df[c] = None
    df = df[keep_cols]
    df["volume"] = df["volume"].fillna(0)
    df["openInterest"] = df["openInterest"].fillna(0)
    return df


# ---------- 挑出"最近到期日"和"次近到期日~一个月内"的窗口 ----------
def get_expiration_windows(df_all):
    """返回 (最近到期日, [第二窗口涵盖的所有到期日列表])
    第二窗口 = 除最近到期日以外、且在ANOMALY_WINDOW_DAYS天以内的所有到期日，
    比如最近到期日是8/7，第二窗口就是 8/14, 8/21, 8/28, 9/4 这些的集合。"""
    exps = sorted(df_all["expiration"].unique())
    if not exps:
        return None, []
    nearest_exp = exps[0]
    others = [e for e in exps if e != nearest_exp]
    second_window = [e for e in others
                      if (datetime.datetime.strptime(e, "%Y-%m-%d").date()
                          - datetime.date.today()).days <= ANOMALY_WINDOW_DAYS]
    return nearest_exp, second_window


# ---------- 某个到期日(或多个到期日合并)的Top5(按未平仓量) ----------
def top5_for_expirations(df_all, exp_dates, top_n=TOP_N):
    subset = df_all[df_all["expiration"].isin(exp_dates)]
    top_calls = subset[subset["type"] == "Call"].sort_values("openInterest", ascending=False).head(top_n)
    top_puts = subset[subset["type"] == "Put"].sort_values("openInterest", ascending=False).head(top_n)
    return top_calls, top_puts


# ---------- 历史快照存取(用于异动检测) ----------
def load_prev_snapshot(ticker_symbol):
    path = os.path.join(HISTORY_DIR, f"{ticker_symbol}.csv")
    if not os.path.exists(path):
        return None
    return pd.read_csv(path)


def save_snapshot(ticker_symbol, df_all):
    os.makedirs(HISTORY_DIR, exist_ok=True)
    path = os.path.join(HISTORY_DIR, f"{ticker_symbol}.csv")
    snap = df_all[["contractSymbol", "openInterest", "volume"]].copy()
    snap["snapshot_date"] = datetime.date.today().isoformat()
    snap.to_csv(path, index=False)


# ---------- 未平仓量异动(一个月窗口内, 今天 vs 昨天) ----------
def detect_oi_surge(ticker_symbol, df_all, top_n=TOP_N):
    prev = load_prev_snapshot(ticker_symbol)
    if prev is None:
        return None  # 第一次跑，还没有对比数据

    scope = df_all[df_all["days_to_exp"] <= ANOMALY_WINDOW_DAYS]
    merged = scope.merge(
        prev[["contractSymbol", "openInterest"]],
        on="contractSymbol", how="left", suffixes=("", "_prev")
    )
    merged["openInterest_prev"] = merged["openInterest_prev"].fillna(0)
    merged["oi_change"] = merged["openInterest"] - merged["openInterest_prev"]

    surge = merged[merged["oi_change"] > 0].sort_values("oi_change", ascending=False).head(top_n)
    return surge


# ---------- 简单规则型文字分析 ----------
def build_analysis_text(ticker_symbol, df_all, oi_surge):
    scope = df_all[df_all["days_to_exp"] <= ANOMALY_WINDOW_DAYS]
    call_oi = scope[scope["type"] == "Call"]["openInterest"].sum()
    put_oi = scope[scope["type"] == "Put"]["openInterest"].sum()

    if call_oi + put_oi == 0:
        return f"{ticker_symbol}: 近一个月内到期期权没有获取到有效的持仓数据。"

    ratio = put_oi / call_oi if call_oi > 0 else float("inf")
    lines = [
        f"{ticker_symbol} 近一个月内到期期权：看涨总未平仓 {int(call_oi):,}，"
        f"看跌总未平仓 {int(put_oi):,}，Put/Call 未平仓比 = "
        f"{'∞' if ratio == float('inf') else f'{ratio:.2f}'}。"
    ]
    if ratio > 1.2:
        lines.append("→ 未平仓量偏向看跌一方，市场对下行保护/投机需求较高。")
    elif ratio < 0.8:
        lines.append("→ 未平仓量偏向看涨一方，市场情绪偏乐观或有杠杆多头布局。")
    else:
        lines.append("→ 看涨看跌未平仓量大致平衡，没有明显方向性倾斜。")

    if oi_surge is not None and len(oi_surge) > 0:
        top1 = oi_surge.iloc[0]
        lines.append(
            f"→ 未平仓量增幅最大的合约是 {top1['type']} 行权价 {top1['strike']} "
            f"(到期日 {top1['expiration']})，较上一次快照增加 {int(top1['oi_change']):,} 张，"
            f"值得关注是否有新增布局。"
        )
    elif oi_surge is None:
        lines.append("→ 这是该ticker第一次运行，还没有前一次的数据可以对比，"
                      "下一次运行起会显示未平仓量的变化。")
    else:
        lines.append("→ 本次没有观察到明显的未平仓量增仓。")

    lines.append("（以上为基于未平仓量的量化观察，不构成投资建议。）")
    return "\n".join(lines)


# ---------- 把DataFrame转成Discord能显示的等宽文本表格 ----------
def format_table_text(df, cols_map):
    """用等宽字体(```代码块)拼一个简单表格，Discord能正常对齐显示"""
    if df is None or len(df) == 0:
        return "```\n(无数据)\n```"

    df2 = df[list(cols_map.keys())].rename(columns=cols_map)
    headers = list(df2.columns)

    def fmt_cell(val):
        if isinstance(val, float):
            return f"{val:,.2f}"
        if isinstance(val, int):
            return f"{val:,}"
        # numpy数值类型(比如int64/float64)也走这里统一处理
        if hasattr(val, "item"):
            v = val.item()
            if isinstance(v, float):
                return f"{v:,.2f}"
            return f"{v:,}"
        return str(val)

    rows = [[fmt_cell(v) for v in row] for row in df2.itertuples(index=False)]
    widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(cell))

    def pad_row(cells):
        return " | ".join(cell.ljust(widths[i]) for i, cell in enumerate(cells))

    lines = [pad_row(headers), "-+-".join("-" * w for w in widths)]
    lines += [pad_row(row) for row in rows]
    return "```\n" + "\n".join(lines) + "\n```"


# ---------- 拼装单个ticker的Discord消息内容(纯文本/Markdown) ----------
def build_ticker_message(ticker_symbol, price_line, nearest_exp, near_calls, near_puts,
                          window_label, month_calls, month_puts, oi_surge, analysis_text):
    cols_map = {
        "type": "类型", "strike": "行权价", "lastPrice": "最新价", "openInterest": "未平仓量"
    }
    cols_map_with_exp = {
        "type": "类型", "expiration": "到期日", "strike": "行权价",
        "lastPrice": "最新价", "openInterest": "未平仓量"
    }
    surge_cols_map = {
        "type": "类型", "expiration": "到期日", "strike": "行权价",
        "openInterest": "今日未平仓", "openInterest_prev": "上次未平仓", "oi_change": "变化量"
    }

    parts = [f"## {ticker_symbol}", price_line, ""]
    parts.append(f"📌 **最近到期日 {nearest_exp} Top{TOP_N} 看涨(按未平仓量)**")
    parts.append(format_table_text(near_calls, cols_map))
    parts.append(f"📌 **最近到期日 {nearest_exp} Top{TOP_N} 看跌(按未平仓量)**")
    parts.append(format_table_text(near_puts, cols_map))

    parts.append(f"📅 **{window_label} 合并 Top{TOP_N} 看涨(按未平仓量)**")
    parts.append(format_table_text(month_calls, cols_map_with_exp))
    parts.append(f"📅 **{window_label} 合并 Top{TOP_N} 看跌(按未平仓量)**")
    parts.append(format_table_text(month_puts, cols_map_with_exp))

    parts.append(f"🔺 **一个月内到期期权 未平仓量增幅Top{TOP_N}(今天 vs 上次)**")
    parts.append(format_table_text(oi_surge, surge_cols_map))

    parts.append(analysis_text)
    return "\n".join(parts)


# ---------- 把过长的消息切成多条(Discord单条消息上限约2000字符) ----------
def chunk_message(text, max_len=1900):
    if len(text) <= max_len:
        return [text]
    chunks = []
    current = ""
    for line in text.split("\n"):
        candidate = (current + "\n" + line) if current else line
        if len(candidate) > max_len:
            if current:
                chunks.append(current)
            current = line
        else:
            current = candidate
    if current:
        chunks.append(current)
    return chunks


# ---------- 发送到Discord(通过Webhook) ----------
def send_discord_message(content):
    webhook_url = os.environ["DISCORD_WEBHOOK_URL"]
    for chunk in chunk_message(content):
        resp = requests.post(webhook_url, json={"content": chunk}, timeout=30)
        if resp.status_code not in (200, 204):
            raise RuntimeError(f"Discord webhook发送失败: HTTP {resp.status_code} — {resp.text[:300]}")
    print("已发送到Discord")


# ---------- 主流程 ----------
def main():
    session_name, now = get_current_session()
    if session_name is None:
        print(f"当前多伦多时间 {now.strftime('%Y-%m-%d %H:%M %Z')} 不在预定发送时段(10:30/16:30)内，跳过本次运行。")
        return

    is_forced = os.environ.get("FORCE_SEND", "false").lower() == "true"
    today_str = now.date().isoformat()
    # 因为一天里有好几次整点尝试都可能落在同一个目标时段的容差范围内，
    # 这里确保同一天同一个时段只真正发送一次。
    # 手动测试(强制发送)不受这个限制，方便随时测试。
    if not is_forced and already_sent_today(session_name, today_str):
        print(f"「{session_name}」今天({today_str})已经发送过了，跳过本次重复触发。")
        return

    is_afternoon_session = (session_name == "午报")

    tickers = load_tickers()
    if not tickers:
        print("config/tickers.txt 里没有找到任何ticker，退出。")
        return

    report_date = now.strftime("%Y-%m-%d")
    any_data_ok = False  # 只要有一个ticker成功拿到期权数据，就算这次运行"有价值"
    ticker_messages = []  # 收集每个ticker的消息内容，最后统一判断是否要发送

    for ticker_symbol in tickers:
        try:
            print(f"处理 {ticker_symbol} ...")
            price, prev_close = fetch_underlying_price(ticker_symbol)
            if price is not None:
                if prev_close:
                    change_pct = (price - prev_close) / prev_close * 100
                    arrow = "▲" if change_pct >= 0 else "▼"
                    price_line = (f"**现价: ${price:,.2f}**　{arrow} {change_pct:+.2f}%　"
                                   f"(较前收盘 ${prev_close:,.2f})")
                else:
                    price_line = f"**现价: ${price:,.2f}**"
            else:
                price_line = "现价: 暂未获取到(可能是数据源临时问题)"

            df_all = fetch_option_chain(ticker_symbol)
            if df_all.empty:
                ticker_messages.append(f"## {ticker_symbol}\n{price_line}\n未能获取到期权数据。")
                continue

            nearest_exp, second_window = get_expiration_windows(df_all)
            if nearest_exp is None:
                ticker_messages.append(f"## {ticker_symbol}\n{price_line}\n未找到有效的到期日。")
                continue

            any_data_ok = True

            near_calls, near_puts = top5_for_expirations(df_all, [nearest_exp])
            month_calls, month_puts = top5_for_expirations(df_all, second_window)
            oi_surge = detect_oi_surge(ticker_symbol, df_all)
            analysis_text = build_analysis_text(ticker_symbol, df_all, oi_surge)

            if second_window:
                window_label = f"{second_window[0]} 至 {second_window[-1]}" if len(second_window) > 1 else second_window[0]
            else:
                window_label = "(无更多到期日数据)"

            msg = build_ticker_message(
                ticker_symbol, price_line, nearest_exp, near_calls, near_puts,
                window_label, month_calls, month_puts, oi_surge, analysis_text
            )
            ticker_messages.append(msg)

            # 只在"午报"时段保存快照，避免同一天两次运行互相冲掉对比基准
            if is_afternoon_session:
                save_snapshot(ticker_symbol, df_all)

        except Exception as e:
            # 单个ticker处理出错(比如数据格式异常)，不能让它连累其他ticker都发不出去，
            # 记录一段错误提示，继续处理下一个ticker。
            print(f"[错误] 处理 {ticker_symbol} 时出现异常，已跳过该ticker: {e}")
            ticker_messages.append(f"## {ticker_symbol}\n⚠️ 本次处理该ticker时出现异常，已跳过：{e}")

    if not any_data_ok:
        # 所有ticker都没能拿到有效的期权数据(大概率是数据源临时故障)，
        # 与其发一条全是"无数据"的空消息、还白白占用今天这个时段的唯一发送机会，
        # 不如直接跳过、不标记为已发送，留给下一次整点尝试重试。
        print(f"「{session_name}」本次所有ticker都未能获取到有效数据，跳过发送，"
              f"留给下一次整点尝试重试(不标记为已发送)。")
        return

    intro = f"# 📊 期权{session_name} — {report_date}"
    send_discord_message(intro)
    for msg in ticker_messages:
        send_discord_message(msg)
    send_discord_message("-# 数据来源: Yahoo Finance (yfinance)，数据可能有延迟，仅供参考，不构成投资建议。")

    if not is_forced:
        mark_sent(session_name, today_str)


if __name__ == "__main__":
    main()
