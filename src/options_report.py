# -*- coding: utf-8 -*-
"""
SOXX(及其他自定义ticker)期权日报生成脚本
------------------------------------------------
功能：
1. 读取 config/tickers.txt 里的股票代码
2. 抓取每个ticker未来 ~90 天内到期的所有期权(看涨+看跌)
3. 从中筛选未来 30 天内到期的合约，按未平仓量(Open Interest)排序，
   分别取看涨、看跌前5名
4. 与"昨天保存的快照"对比，找出未来90天内到期的合约中：
   - 未平仓量增加最多的（可能是新建仓位）
   - 成交量/未平仓量比值最高的（可能当天有大单介入）
5. 生成简单的规则型文字分析
6. 把结果拼成HTML邮件并发送

本脚本设计给完全不懂Python的人使用：正常情况下你不需要改这个文件，
只需要改 config/tickers.txt 来增删关注的股票。
"""

import os
import json
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pandas as pd
import yfinance as yf

# ---------- 基本配置 ----------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TICKERS_FILE = os.path.join(BASE_DIR, "config", "tickers.txt")
HISTORY_DIR = os.path.join(BASE_DIR, "data", "history")

NEAR_TERM_DAYS = 30   # "近期"报告窗口：未来30天到期
FAR_TERM_DAYS = 90    # "异动扫描"窗口：未来90天到期
TOP_N = 5             # 每类取前几名


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


# ---------- 抓取期权链 ----------
def fetch_option_chain(ticker_symbol, max_days):
    """抓取某个ticker在未来max_days天内到期的所有看涨/看跌合约，
    返回一个合并后的DataFrame，多一列 days_to_exp / type / expiration"""
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
    # 只保留有用的列，缺失的用0/空填上，避免后面报错
    keep_cols = ["ticker", "contractSymbol", "expiration", "days_to_exp", "type",
                 "strike", "lastPrice", "bid", "ask", "volume", "openInterest",
                 "impliedVolatility"]
    for c in keep_cols:
        if c not in df.columns:
            df[c] = None
    df = df[keep_cols]
    df["volume"] = df["volume"].fillna(0)
    df["openInterest"] = df["openInterest"].fillna(0)
    return df


# ---------- 近期 Top5 (按未平仓量) ----------
def get_top_by_oi(df_all, near_days=NEAR_TERM_DAYS, top_n=TOP_N):
    df_near = df_all[df_all["days_to_exp"] <= near_days]
    top_calls = (df_near[df_near["type"] == "Call"]
                 .sort_values("openInterest", ascending=False)
                 .head(top_n))
    top_puts = (df_near[df_near["type"] == "Put"]
                .sort_values("openInterest", ascending=False)
                .head(top_n))
    return df_near, top_calls, top_puts


# ---------- 历史快照存取(用于异动检测) ----------
def load_prev_snapshot(ticker_symbol):
    path = os.path.join(HISTORY_DIR, f"{ticker_symbol}.csv")
    if not os.path.exists(path):
        return None
    return pd.read_csv(path)


def save_snapshot(ticker_symbol, df_far):
    os.makedirs(HISTORY_DIR, exist_ok=True)
    path = os.path.join(HISTORY_DIR, f"{ticker_symbol}.csv")
    snap = df_far[["contractSymbol", "openInterest", "volume"]].copy()
    snap["snapshot_date"] = datetime.date.today().isoformat()
    snap.to_csv(path, index=False)


# ---------- 异动检测(未来90天窗口) ----------
def detect_unusual_activity(ticker_symbol, df_far, top_n=TOP_N):
    prev = load_prev_snapshot(ticker_symbol)
    if prev is None:
        return None, None  # 第一次跑，还没有对比数据

    merged = df_far.merge(
        prev[["contractSymbol", "openInterest", "volume"]],
        on="contractSymbol", how="left", suffixes=("", "_prev")
    )
    merged["openInterest_prev"] = merged["openInterest_prev"].fillna(0)
    merged["oi_change"] = merged["openInterest"] - merged["openInterest_prev"]
    merged["vol_oi_ratio"] = merged["volume"] / merged["openInterest"].replace(0, 1)

    # 未平仓量增加最多的合约(新建仓位信号)
    oi_surge = merged[merged["oi_change"] > 0].sort_values(
        "oi_change", ascending=False).head(top_n)

    # 成交量/未平仓比最高的合约(当天可能有大单介入)
    vol_spike = merged[merged["volume"] > 50].sort_values(
        "vol_oi_ratio", ascending=False).head(top_n)

    return oi_surge, vol_spike


# ---------- 简单规则型文字分析 ----------
def build_analysis_text(ticker_symbol, df_near, oi_surge, vol_spike):
    lines = []
    call_oi = df_near[df_near["type"] == "Call"]["openInterest"].sum()
    put_oi = df_near[df_near["type"] == "Put"]["openInterest"].sum()
    ratio = put_oi / call_oi if call_oi > 0 else float("nan")

    if call_oi + put_oi == 0:
        lines.append(f"{ticker_symbol}: 未来{NEAR_TERM_DAYS}天内没有获取到有效的期权持仓数据。")
        return "\n".join(lines)

    lines.append(
        f"{ticker_symbol} 未来{NEAR_TERM_DAYS}天到期期权：看涨总未平仓 {int(call_oi):,}，"
        f"看跌总未平仓 {int(put_oi):,}，Put/Call 未平仓比 = {ratio:.2f}。"
    )
    if ratio > 1.2:
        lines.append("→ 未平仓量偏向看跌一方，市场对下行保护/投机需求较高。")
    elif ratio < 0.8:
        lines.append("→ 未平仓量偏向看涨一方，市场情绪偏乐观或有杠杆多头布局。")
    else:
        lines.append("→ 看涨看跌未平仓量大致平衡，没有明显方向性倾斜。")

    if oi_surge is not None and len(oi_surge) > 0:
        top1 = oi_surge.iloc[0]
        lines.append(
            f"→ 未来{FAR_TERM_DAYS}天窗口内，未平仓量增幅最大的合约是 "
            f"{top1['type']} {top1['strike']} 到期日 {top1['expiration']}，"
            f"较前一交易日增加 {int(top1['oi_change']):,} 张，值得关注是否有新增布局。"
        )
    if vol_spike is not None and len(vol_spike) > 0:
        top1 = vol_spike.iloc[0]
        lines.append(
            f"→ 成交量相对未平仓量比值最高的合约是 "
            f"{top1['type']} {top1['strike']} 到期日 {top1['expiration']}"
            f"(成交量 {int(top1['volume']):,} / 未平仓 {int(top1['openInterest']):,})，"
            f"当天换手异常活跃，可能有资金短线介入。"
        )
    if (oi_surge is None) and (vol_spike is None):
        lines.append("→ 这是第一次运行，还没有前一天的数据可以对比，明天起会显示未平仓量与成交量的变化。")

    lines.append("（以上为基于未平仓量/成交量的量化观察，不构成投资建议。）")
    return "\n".join(lines)


# ---------- 把DataFrame转成HTML表格 ----------
def df_to_html_table(df, cols_map):
    """cols_map: {原始列名: 显示名}"""
    if df is None or len(df) == 0:
        return "<p style='color:#888'>（无数据）</p>"
    df2 = df[list(cols_map.keys())].rename(columns=cols_map)
    return df2.to_html(index=False, border=0, justify="center",
                        classes="option-table", float_format=lambda x: f"{x:,.2f}")


# ---------- 组装整封邮件的HTML ----------
def build_html_report(report_date, per_ticker_sections):
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
    </style>
    """
    html = f"<html><head>{style}</head><body>"
    html += f"<h2>期权市场日报 — {report_date}</h2>"
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
    tickers = load_tickers()
    if not tickers:
        print("config/tickers.txt 里没有找到任何ticker，退出。")
        return

    report_date = datetime.date.today().isoformat()
    sections = []

    for ticker_symbol in tickers:
        print(f"处理 {ticker_symbol} ...")
        df_all = fetch_option_chain(ticker_symbol, FAR_TERM_DAYS)
        if df_all.empty:
            sections.append(f"<h3>{ticker_symbol}</h3><p>未能获取到期权数据。</p>")
            continue

        df_near, top_calls, top_puts = get_top_by_oi(df_all)
        oi_surge, vol_spike = detect_unusual_activity(ticker_symbol, df_all)
        analysis_text = build_analysis_text(ticker_symbol, df_near, oi_surge, vol_spike)

        cols_map = {
            "expiration": "到期日", "strike": "行权价", "lastPrice": "最新价",
            "bid": "买价", "ask": "卖价", "volume": "成交量", "openInterest": "未平仓量",
            "impliedVolatility": "隐含波动率"
        }
        surge_cols_map = {
            "type": "类型", "expiration": "到期日", "strike": "行权价",
            "openInterest": "今日未平仓", "openInterest_prev": "昨日未平仓", "oi_change": "变化量"
        }
        spike_cols_map = {
            "type": "类型", "expiration": "到期日", "strike": "行权价",
            "volume": "成交量", "openInterest": "未平仓量", "vol_oi_ratio": "量/仓比"
        }

        section = f"<h3>📈 {ticker_symbol} — 未来{NEAR_TERM_DAYS}天到期 Top{TOP_N} 看涨(按未平仓量)</h3>"
        section += df_to_html_table(top_calls, cols_map)
        section += f"<h3>📉 {ticker_symbol} — 未来{NEAR_TERM_DAYS}天到期 Top{TOP_N} 看跌(按未平仓量)</h3>"
        section += df_to_html_table(top_puts, cols_map)

        if oi_surge is not None:
            section += f"<h3>🔺 {ticker_symbol} — 未来{FAR_TERM_DAYS}天窗口 未平仓量增幅最大</h3>"
            section += df_to_html_table(oi_surge, surge_cols_map)
        if vol_spike is not None:
            section += f"<h3>⚡ {ticker_symbol} — 未来{FAR_TERM_DAYS}天窗口 成交量/未平仓比最高(疑似大单介入)</h3>"
            section += df_to_html_table(vol_spike, spike_cols_map)

        section += f"<div class='analysis'>{analysis_text}</div>"
        sections.append(section)

        # 保存今天的快照，供明天对比
        save_snapshot(ticker_symbol, df_all)

    html = build_html_report(report_date, sections)
    tickers_str = ", ".join(tickers)
    send_email(f"期权日报 {report_date} — {tickers_str}", html)


if __name__ == "__main__":
    main()
