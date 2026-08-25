# -*- coding: utf-8 -*-
"""
期权日报主入口（v3）
-------------------
调度：多伦多时间 10:15（早报）/ 16:30（晚报），周一至周五。
GitHub Actions 每小时触发一次，脚本自行判断是否命中目标时段；
命中才抓数据、算指标、生成报告并推送 Discord；否则几十秒内跳过。

数据：CBOE 官方延迟期权链（主源）+ yfinance（兜底），
指标：P/C、Max Pain、ATM IV、IV Rank、偏度、期限结构、预期波动、
      OI 集中带、Greeks 敞口、异动评分、OI 增仓。
日历：周二/周四早报附带本周宏观日历 + 当周重要公司财报。
分析：规则版（永远可用）+ 可选 AI 深度分析（OPENAI_API_KEY，失败自动退回规则版）。

正常情况下你不需要改这个文件，只需要改 config/tickers.txt。
"""

import datetime
import json
import os
import sys
from zoneinfo import ZoneInfo

import data_fetcher as fetcher
import metrics as metrics_mod
import storage
from analysis import appendix_line, build_report, build_ticker_section
from calendars import build_calendar_sections
from discord_sender import send_discord_message
from fear_greed import fetch_fear_greed, format_fear_greed
from llm_analyst import generate_deep_analysis
from reminders import evening_reminder_lines

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)
TICKERS_FILE = os.path.join(BASE_DIR, "config", "tickers.txt")

FETCH_WINDOW_DAYS = 40    # 抓取期权链的窗口（覆盖到月度到期日）
ANOMALY_WINDOW_DAYS = 35  # "一个月以内"异动扫描窗口
TOP_N = 5
MIN_VOLUME = 500          # 异动候选的最低成交量
VOL_OI_MIN = 1.0          # 异动候选的最低量/OI 比

TORONTO_TZ = ZoneInfo("America/Toronto")
TARGET_SESSIONS = [
    ("早报", 10, 15),
    ("晚报", 16, 30),
]
TOLERANCE_MINUTES = 75

DISCLAIMER = ("-# 数据来源: CBOE 延迟数据 / Yahoo Finance，可能有延迟；"
              "本报告由规则计算 + AI 辅助生成，仅供研究参考，不构成投资建议。")


# ---------- 时段判断 ----------
def get_current_session():
    now = datetime.datetime.now(TORONTO_TZ)
    if os.environ.get("FORCE_SEND", "false").lower() == "true":
        force_session = os.environ.get("FORCE_SESSION")
        if force_session and any(s[0] == force_session for s in TARGET_SESSIONS):
            print(f"[FORCE_SEND] 手动测试模式，强制按「{force_session}」生成。")
            return force_session, now
        closest = min(
            TARGET_SESSIONS,
            key=lambda s: abs(
                (now.replace(hour=s[1], minute=s[2], second=0, microsecond=0) - now).total_seconds()
            )
        )
        print(f"[FORCE_SEND] 手动测试模式，忽略时间检查，按「{closest[0]}」生成。")
        return closest[0], now
    for name, hh, mm in TARGET_SESSIONS:
        target = now.replace(hour=hh, minute=mm, second=0, microsecond=0)
        if abs((now - target).total_seconds()) / 60 <= TOLERANCE_MINUTES:
            return name, now
    return None, now


# ---------- 防止同一时段重复发送 ----------
def _sent_log_path():
    return os.path.join(storage.HISTORY_DIR, "_sent_log.json")


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
    os.makedirs(storage.HISTORY_DIR, exist_ok=True)
    log = {"date": today_str, "sessions": []}
    if os.path.exists(_sent_log_path()):
        try:
            with open(_sent_log_path(), "r", encoding="utf-8") as f:
                existing = json.load(f)
            if existing.get("date") == today_str:
                log = existing
        except Exception:
            pass
    if session_name not in log["sessions"]:
        log["sessions"].append(session_name)
    with open(_sent_log_path(), "w", encoding="utf-8") as f:
        json.dump(log, f, ensure_ascii=False)


# ---------- ticker 列表 ----------
def load_tickers():
    tickers = []
    with open(TICKERS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            tickers.append(line.upper())
    if len(tickers) > 20:
        print(f"[警告] ticker 数量 {len(tickers)} 超过 20 个上限：仓库体积与抓取频率会显著上升，请精简 config/tickers.txt")
    return tickers


# ---------- 市场背景（SPY + VIX） ----------
def market_context(include_fear_greed=False):
    spy = None
    vix = None
    try:
        spy, _ = fetcher.fetch_spot("SPY")
    except Exception:
        pass
    try:
        vix, _ = fetcher.fetch_spot_yfinance("^VIX")
    except Exception:
        pass
    parts = []
    if spy is not None:
        parts.append(f"SPY ${spy:,.2f}")
    if vix is not None:
        parts.append(f"VIX {vix:.2f}")
    if include_fear_greed:
        fg = fetch_fear_greed()
        fg_text = format_fear_greed(fg)
        if fg_text:
            parts.append(fg_text)
    return "市场背景： " + " ｜ ".join(parts) if parts else None


# ---------- LLM 输入（紧凑指标，不给原始链） ----------
def _r(v, n=4):
    if v is None:
        return None
    try:
        return round(float(v), n)
    except (TypeError, ValueError):
        return None


def _compact(ticker, m, price, prev_close, rank, source):
    chg = None
    if price and prev_close:
        chg = (price - prev_close) / prev_close * 100
    return {
        "ticker": ticker,
        "price": _r(price, 2),
        "change_pct": _r(chg, 2),
        "source": source,
        "pcr_vol_near": _r(m.get("pcr_vol_near")),
        "pcr_oi_near": _r(m.get("pcr_oi_near")),
        "pcr_vol_all": _r(m.get("pcr_vol_all")),
        "pcr_oi_all": _r(m.get("pcr_oi_all")),
        "max_pain_near": _r(m.get("max_pain_near"), 2),
        "max_pain_monthly": _r(m.get("max_pain_monthly"), 2),
        "atm_iv_near": _r(m.get("atm_iv_near")),
        "atm_iv_monthly": _r(m.get("atm_iv_monthly")),
        "term_ratio": _r(m.get("term_ratio")),
        "iv_skew_25_pp": _r(m.get("iv_skew_25")),
        "expected_move_pct": _r(m.get("expected_move_pct")),
        "net_delta_oi_shares": _r(m.get("net_delta_oi"), 0),
        "net_gamma_oi_shares": _r(m.get("net_gamma_oi"), 0),
        "iv_rank_pct": _r(rank, 1),
        "oi_concentration": m.get("oi_concentration"),
        "top_unusual": m.get("top_unusual"),
        "top_surge": m.get("top_surge"),
        "structure": {k: (m.get("structure") or {}).get(k) for k in (
            "net_gex", "gamma_flip", "call_wall", "put_wall",
            "top_gamma", "net_vanna", "net_charm",
        )},
        "structure_near_flip": (m.get("structure_near") or {}).get("gamma_flip"),
        "structure_monthly_flip": (m.get("structure_monthly") or {}).get("gamma_flip"),
        "new_gex": m.get("new_gex"),
        "new_delta": m.get("new_delta"),
    }


def build_llm_payload(date_str, session, market_line, summaries, calendar_sections=None):
    payload = {
        "date": date_str,
        "session": session,
        "market_context": market_line,
        "tickers": summaries,
    }
    if calendar_sections:
        payload["calendar"] = calendar_sections
    return json.dumps(payload, ensure_ascii=False, default=str)


# ---------- 主流程 ----------
def main():
    session_name, now = get_current_session()
    if session_name is None:
        print(f"当前多伦多时间 {now.strftime('%Y-%m-%d %H:%M %Z')} 不在预定时段(10:15/16:30)内，跳过本次运行。")
        return

    is_forced = os.environ.get("FORCE_SEND", "false").lower() == "true"
    today_str = now.date().isoformat()
    if not is_forced and already_sent_today(session_name, today_str):
        print(f"「{session_name}」今天({today_str})已发送过，跳过重复触发。")
        return

    is_afternoon = (session_name == "晚报")
    tickers = load_tickers()
    if not tickers:
        print("config/tickers.txt 里没有找到任何 ticker，退出。")
        return

    report_date = now.strftime("%Y-%m-%d")
    any_data_ok = False
    ticker_sections = []
    appendix = []
    summaries = []

    # VIX / Volatility Environment v1.1：市场层环境，所有 ticker 共用同一份
    vol_environment = None
    try:
        from src.vol_environment import build_vol_environment_for_run

        vol_environment = build_vol_environment_for_run(
            now, session_name, BASE_DIR, os.path.join(BASE_DIR, "config")
        )
    except Exception as e:
        print(f"[警告] vol_environment 构建失败（快照环境标签将缺失）: {e}")

    for ticker in tickers:
        try:
            print(f"处理 {ticker} ...")
            price, prev_close = fetcher.fetch_spot(ticker)
            contracts, chain_spot, source = fetcher.fetch_chain(ticker, max_days=FETCH_WINDOW_DAYS)
            spot = price or chain_spot
            prev = storage.load_prev_snapshot(ticker)
            m = metrics_mod.compute_metrics(
                contracts, spot, prev=prev,
                fetch_window=FETCH_WINDOW_DAYS,
                anomaly_window=ANOMALY_WINDOW_DAYS,
                min_volume=MIN_VOLUME, vol_oi_min=VOL_OI_MIN, top_n=TOP_N,
            )
            m["price"] = price
            m["prev_close"] = prev_close
            day_high, day_low = fetcher.fetch_day_range_yfinance(ticker)
            m["day_high"] = day_high
            m["day_low"] = day_low
            try:
                # 方案 A：把当天真实快照写入引擎（供 detect/事件库使用）
                from engine.snapshot_builder import build_snapshot, load_analytics_rows
                from engine.snapshot import SnapshotStore

                hist_rows = load_analytics_rows(
                    os.path.join(storage.ANALYTICS_DIR, f"{ticker}.csv")
                )
                forward = None
                try:
                    from src.forward_structure import build_forward_structure

                    forward = build_forward_structure(
                        contracts, prev, spot,
                        as_of_date=now.date(),
                        config_root=os.path.join(BASE_DIR, "config"),
                    )
                except Exception as e:
                    print(f"[警告] forward structure 构建失败（快照将缺失该层）: {e}")
                snap = build_snapshot(
                    ticker, session_name, m, spot,
                    now.isoformat(timespec="seconds"),
                    analytics_rows=hist_rows, source=source,
                    vol_environment=vol_environment,
                    forward_structure=forward,
                )
                SnapshotStore(BASE_DIR).store(snap)
            except Exception as e:
                print(f"[警告] {ticker} 快照入库失败（不影响报告发送）: {e}")
            history = storage.load_iv_history(ticker)
            rank = metrics_mod.iv_rank(m.get("atm_iv_near"), history)
            morning_iv = None
            if is_afternoon:
                morning_iv = storage.load_session_value(ticker, "早报", "atm_iv_near")

            storage.append_analytics(ticker, session_name, source, m)
            if is_afternoon:
                storage.save_snapshot(ticker, contracts)

            section = build_ticker_section(
                ticker, price, prev_close, m, rank,
                session_name, morning_iv=morning_iv, show_surge=True,
            )
            ticker_sections.append(section)
            appendix.append(appendix_line(ticker, m, rank))
            summaries.append(_compact(ticker, m, price, prev_close, rank, source))
            any_data_ok = True
        except Exception as e:
            print(f"[错误] 处理 {ticker} 时异常，已跳过该 ticker: {e}")
            ticker_sections.append(f"## {ticker}\n⚠️ 本次处理该 ticker 时异常，已跳过：{e}")

    if not any_data_ok:
        print(f"「{session_name}」本次所有 ticker 都未能获取到有效数据，跳过发送，留给下一次重试。")
        return

    market_line = market_context(include_fear_greed=(session_name == "早报"))
    calendar_sections = None
    if session_name == "早报" and now.weekday() in (1, 3):  # 周二/周四
        calendar_sections = build_calendar_sections(now)

    payload = build_llm_payload(report_date, session_name, market_line, summaries,
                                calendar_sections)
    deep_analysis = None
    if os.environ.get("LLM_ENABLED", "true").lower() == "true":
        deep_analysis = generate_deep_analysis(payload)

    report = build_report(
        report_date, session_name, ticker_sections,
        deep_analysis, market_line, appendix, DISCLAIMER,
        calendar_sections=calendar_sections,
    )
    if session_name == "晚报":
        reminder_lines = evening_reminder_lines(now)
        if reminder_lines:
            report = report + "\n\n---\n\n" + "\n\n".join(reminder_lines)

    dry_run = os.environ.get("REPORT_DRY_RUN", "false").lower() == "true"
    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL", "")
    if webhook_url:
        send_discord_message(webhook_url, report, dry_run=dry_run)
    else:
        print("[提示] 未配置 DISCORD_WEBHOOK_URL，本次只打印报告，不发送。")
        send_discord_message("", report, dry_run=True)

    if not is_forced:
        mark_sent(session_name, today_str)


if __name__ == "__main__":
    main()
