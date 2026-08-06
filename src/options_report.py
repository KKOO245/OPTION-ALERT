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

4. 每天多伦多时间上午10:30和下午4:30各发一封邮件。因为GitHub Actions的定时
   任务只能设固定UTC时间，没法跟着夏令时自动变化，所以这里用了一个技巧：
   工作流会在覆盖两种夏令时/冬令时可能性的4个UTC时间点各触发一次，
   脚本自己检查"现在的多伦多本地时间是否接近10:30或16:30"，
   不是的话直接跳过、不发邮件、不消耗额外资源。这样全年都不用手动调整时间。

本脚本设计给完全不懂Python的人使用：正常情况下你不需要改这个文件，
只需要改 config/tickers.txt 来增删关注的股票。
"""

import os
import datetime
from zoneinfo import ZoneInfo
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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
TOLERANCE_MINUTES = 60  # 允许GitHub Actions触发延迟的容差(免费额度的定时任务
                         # 实际触发时间可能比设定时间晚20分钟到1小时以上，这是
                         # GitHub本身的已知限制，不是脚本的bug，所以给足够的余量)


# ---------- 判断现在是不是该发送的时段 ----------
def get_current_session():
    now = datetime.datetime.now(TORONTO_TZ)

    # 手动测试用：workflow_dispatch里勾选"强制发送"时，跳过时间检查
    if os.environ.get("FORCE_SEND", "false").lower() == "true":
        # 挑离现在最近的一个时段名称，只是用来给邮件标题用，不影响内容
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

    ratio = put_oi / call_oi if call_oi > 0 else float("nan")
    lines = [
        f"{ticker_symbol} 近一个月内到期期权：看涨总未平仓 {int(call_oi):,}，"
        f"看跌总未平仓 {int(put_oi):,}，Put/Call 未平仓比 = {ratio:.2f}。"
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


# ---------- 把DataFrame转成HTML表格 ----------
def df_to_html_table(df, cols_map):
    if df is None or len(df) == 0:
        return "<p style='color:#888'>（无数据）</p>"
    df2 = df[list(cols_map.keys())].rename(columns=cols_map)
    return df2.to_html(index=False, border=0, justify="center",
                        classes="option-table", float_format=lambda x: f"{x:,.2f}")


# ---------- 组装整封邮件的HTML ----------
def build_html_report(report_date, session_name, per_ticker_sections):
    style = """
    <style>
      body { font-family: -apple-system, Arial, sans-serif; color:#222; }
      h2 { color:#1a3e6f; border-bottom:2px solid #1a3e6f; padding-bottom:4px; }
      h3 { color:#333; margin-bottom:4px; }
      table.option-table { border-collapse: collapse; width:100%; margin-bottom:16px; font-size:13px;}
      table.option-table th { background:#1a3e6f; color:white; padding:6px 8px; }
      table.option-table td { padding:6px 8px; border-bottom:1px solid #ddd; text-align:center;}
      .analysis { background:#f4f7fb; padding:10px 14px; border-left:4px solid #1a3e6f;
                  white-space:pre-line; font-size:14px; margin-bottom:24px;}
    .price-banner { background:#1a3e6f; color:white; padding:10px 14px; border-radius:6px;
                    font-size:16px; margin-bottom:10px; }
    .price-banner .up { color:#8fffb0; }
    .price-banner .down { color:#ffb0b0; }
    </style>
    """
    html = f"<html><head>{style}</head><body>"
    html += f"<h2>期权市场{session_name} — {report_date}</h2>"
    html += "".join(per_ticker_sections)
    html += "<p style='font-size:11px;color:#999'>数据来源: Yahoo Finance (yfinance)，" \
            "数据可能有延迟，仅供参考，不构成投资建议。</p>"
    html += "</body></html>"
    return html


# ---------- 发送邮件 ----------
def send_email(subject, html_body):
    sender = os.environ["EMAIL_ADDRESS"]
    password = os.environ["EMAIL_APP_PASSWORD"]
    recipient = os.environ["RECIPIENT_EMAIL"]
    smtp_host = os.environ.get("SMTP_HOST", "smtp.gmail.com")
    smtp_port = int(os.environ.get("SMTP_PORT", "587"))

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipient
    msg.attach(MIMEText(html_body, "html", "utf-8"))

    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, recipient, msg.as_string())
    print(f"邮件已发送至 {recipient}")


# ---------- 主流程 ----------
def main():
    session_name, now = get_current_session()
    if session_name is None:
        print(f"当前多伦多时间 {now.strftime('%Y-%m-%d %H:%M %Z')} 不在预定发送时段(10:30/16:30)内，跳过本次运行。")
        return

    is_afternoon_session = (session_name == "午报")

    tickers = load_tickers()
    if not tickers:
        print("config/tickers.txt 里没有找到任何ticker，退出。")
        return

    report_date = now.strftime("%Y-%m-%d")
    sections = []

    for ticker_symbol in tickers:
        print(f"处理 {ticker_symbol} ...")
        price, prev_close = fetch_underlying_price(ticker_symbol)
        if price is not None:
            if prev_close:
                change_pct = (price - prev_close) / prev_close * 100
                arrow = "▲" if change_pct >= 0 else "▼"
                css_cls = "up" if change_pct >= 0 else "down"
                price_line = (f"{ticker_symbol} 现价: ${price:,.2f}　"
                               f"<span class='{css_cls}'>{arrow} {change_pct:+.2f}%</span>"
                               f"　(较前收盘 ${prev_close:,.2f})")
            else:
                price_line = f"{ticker_symbol} 现价: ${price:,.2f}"
        else:
            price_line = f"{ticker_symbol} 现价: 暂未获取到(可能是数据源临时问题)"
        price_banner_html = f"<div class='price-banner'>{price_line}</div>"

        df_all = fetch_option_chain(ticker_symbol)
        if df_all.empty:
            sections.append(f"<h2>{ticker_symbol}</h2>{price_banner_html}<p>未能获取到期权数据。</p>")
            continue

        nearest_exp, second_window = get_expiration_windows(df_all)
        if nearest_exp is None:
            sections.append(f"<h2>{ticker_symbol}</h2>{price_banner_html}<p>未找到有效的到期日。</p>")
            continue

        near_calls, near_puts = top5_for_expirations(df_all, [nearest_exp])
        month_calls, month_puts = top5_for_expirations(df_all, second_window)
        oi_surge = detect_oi_surge(ticker_symbol, df_all)
        analysis_text = build_analysis_text(ticker_symbol, df_all, oi_surge)

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

        section = f"<h2>{ticker_symbol}</h2>{price_banner_html}"
        section += f"<h3>📌 {ticker_symbol} — 最近到期日 {nearest_exp} Top{TOP_N} 看涨(按未平仓量)</h3>"
        section += df_to_html_table(near_calls, cols_map)
        section += f"<h3>📌 {ticker_symbol} — 最近到期日 {nearest_exp} Top{TOP_N} 看跌(按未平仓量)</h3>"
        section += df_to_html_table(near_puts, cols_map)

        if second_window:
            window_label = f"{second_window[0]} 至 {second_window[-1]}" if len(second_window) > 1 else second_window[0]
        else:
            window_label = "(无更多到期日数据)"
        section += f"<h3>📅 {ticker_symbol} — {window_label} 合并 Top{TOP_N} 看涨(按未平仓量)</h3>"
        section += df_to_html_table(month_calls, cols_map_with_exp)
        section += f"<h3>📅 {ticker_symbol} — {window_label} 合并 Top{TOP_N} 看跌(按未平仓量)</h3>"
        section += df_to_html_table(month_puts, cols_map_with_exp)

        section += f"<h3>🔺 {ticker_symbol} — 一个月内到期期权 未平仓量增幅Top{TOP_N}(今天 vs 上次)</h3>"
        section += df_to_html_table(oi_surge, surge_cols_map)

        section += f"<div class='analysis'>{analysis_text}</div>"
        sections.append(section)

        # 只在"午报"时段保存快照，避免同一天两次运行互相冲掉对比基准
        if is_afternoon_session:
            save_snapshot(ticker_symbol, df_all)

    html = build_html_report(report_date, session_name, sections)
    tickers_str = ", ".join(tickers)
    send_email(f"期权{session_name} {report_date} — {tickers_str}", html)


if __name__ == "__main__":
    main()
