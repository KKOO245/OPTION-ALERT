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
from reminders import evening_reminder_lines, morning_reminder_lines

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
# (会话名, 目标小时, 目标分钟, 单向容差分钟) —— 只准迟到、不许早到
TARGET_SESSIONS = [
    ("早报", 10, 15, 135),   # 10:15–12:30
    ("晚报", 16, 30, 180),   # 16:30–19:30（配合 23:00 UTC 槽兜底）
]
# 与工作流 timecheck 的单向窗口保持一致（早报 135 / 晚报 180 分钟），
# 否则 12:00/18:00/19:00 的兜底 cron 会通过工作流检查、却在这里被挡掉。

DISCLAIMER = ("-# 数据来源: CBOE 延迟数据 / Yahoo Finance，可能有延迟；"
              "本报告由规则计算 + AI 辅助生成，仅供研究参考，不构成投资建议。")


# ---------- 时段判断 ----------
def get_current_session():
    now = datetime.datetime.now(TORONTO_TZ)
    if os.environ.get("FORCE_SEND", "false").lower() == "true":
        force_session = os.environ.get("FORCE_SESSION")
        # 兼容工作流 session 输入的英文值（morning/evening）与本地中文值（早报/晚报）
        force_map = {"morning": "早报", "evening": "晚报"}
        fs = force_map.get(force_session, force_session)
        if fs and any(s[0] == fs for s in TARGET_SESSIONS):
            print(f"[FORCE_SEND] 手动测试模式，强制按「{fs}」生成。")
            return fs, now
        closest = min(
            TARGET_SESSIONS,
            key=lambda s: abs(
                (now.replace(hour=s[1], minute=s[2], second=0, microsecond=0) - now).total_seconds()
            )
        )
        print(f"[FORCE_SEND] 手动测试模式，忽略时间检查，按「{closest[0]}」生成。")
        return closest[0], now
    for name, hh, mm, tol in TARGET_SESSIONS:
        target = now.replace(hour=hh, minute=mm, second=0, microsecond=0)
        # 单向容差：只允许"晚于目标时刻"（delta >= 0），绝不提前生成
        delta_min = (now - target).total_seconds() / 60
        if 0 <= delta_min <= tol:
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


def _fill_activity_volumes(ticker, contracts, m, fetcher_mod):
    """B 方案：报告可见合约（top_surge/top_unusual）CBOE 缺量 → yfinance 补量并标来源。

    只补 volume 与最新价（last_price）；OI/IV/delta 不跨源，保持各自口径。
    补进来的量会同步更新 contracts，让 Forward 的 ΔOI/Volume 也能用上。
    """
    rows = list(m.get("top_surge") or []) + list(m.get("top_unusual") or [])
    missing = {r.get("contract_symbol") for r in rows if not (r.get("volume") or 0)}
    if not missing:
        return
    exps = sorted({
        r.get("expiration") for r in rows
        if r.get("contract_symbol") in missing and r.get("expiration")
    })
    vol_map = fetcher_mod.fetch_option_volumes_yfinance(ticker, exps)
    if not vol_map:
        return
    for r in rows:
        sym = r.get("contract_symbol")
        if sym not in missing or sym not in vol_map:
            continue
        e = vol_map[sym]
        if e.get("volume"):
            r["volume"] = e["volume"]
            r["volume_source"] = "yfinance"
        if not r.get("last_price") and e.get("last") is not None:
            r["last_price"] = e["last"]
    by_sym = {c.get("contract_symbol"): c for c in contracts or []}
    for sym in missing:
        c = by_sym.get(sym)
        e = vol_map.get(sym)
        if c is None or e is None:
            continue
        if e.get("volume"):
            c["volume"] = e["volume"]
            c["volume_source"] = "yfinance"
        if not c.get("last") and e.get("last") is not None:
            c["last"] = e["last"]


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
    try:
        from engine import yaml_mini

        thresholds = yaml_mini.load(os.path.join(BASE_DIR, "config", "thresholds.yaml"))
    except Exception as e:
        print(f"[警告] thresholds 加载失败（P1/P3 用默认值）: {e}")
        thresholds = {}
    event_dates = None
    try:
        from src.calendars import macro_event_dates

        event_dates = macro_event_dates(now)
    except Exception as e:
        print(f"[警告] 宏观日历获取失败（P3 事件覆盖将缺失）: {e}")

    for ticker in tickers:
        try:
            print(f"处理 {ticker} ...")
            price, prev_close = fetcher.fetch_spot(ticker)
            try:
                ohlc = fetcher.fetch_ohlc_yfinance(ticker)
            except Exception as e:
                print(f"[警告] {ticker} 当日 OHLC 获取失败（高/低/开/收 保持原逻辑）: {e}")
                ohlc = None
            contracts, chain_spot, source = fetcher.fetch_chain(ticker, max_days=FETCH_WINDOW_DAYS)
            # 每日全量合约快照永久存档（早/晚报都存，同日以最后一次为准）
            try:
                storage.append_chain_history(ticker, contracts, date=now.date().isoformat())
            except Exception as e:
                print(f"[警告] {ticker} 链快照存档失败（不影响报告）: {e}")
            # 晚报：收盘价用常规时段 Close（4:00pm ET），避免盘后 last_price 污染"昨收/收盘"
            if is_afternoon and ohlc is not None and ohlc[3] is not None:
                price = ohlc[3]
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
            if ohlc is not None:
                m["day_high"] = ohlc[0]
                m["day_low"] = ohlc[1]
                m["day_open"] = ohlc[2]
            try:
                _fill_activity_volumes(ticker, contracts, m, fetcher)
            except Exception as e:
                print(f"[警告] yfinance 补量失败（保持 N/A）: {e}")
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
                # P1：全链重定价 + 覆盖审计；P3：研究采集字段（只进 JSON，不进报告/评分）
                full_chain = None
                coverage = None
                p3 = None
                try:
                    from engine.coverage import coverage_audit
                    from engine.p3_collect import collect_p3
                    from engine.regime_map import regime_map
                    from engine.second_order import second_order_aggregate

                    full_chain = regime_map(contracts, spot, as_of=now.date())
                    qg = thresholds.get("quality_gate") or {}
                    coverage = coverage_audit(
                        contracts, spot,
                        band_pct=float(qg.get("flip_search_band_pct", 15.0)),
                    )
                    sess_rank = {"morning": 0, "evening": 1}.get(session_name, 0)
                    today_key = now.date().isoformat()
                    prev_atm = None
                    for r in reversed(hist_rows):
                        rk = (str(r.get("date", "")), {"morning": 0, "evening": 1}.get(r.get("session"), 0))
                        if rk < (today_key, sess_rank) and r.get("atm_iv_near") is not None:
                            prev_atm = r.get("atm_iv_near")
                            break
                    iv_move_pp = None
                    if m.get("atm_iv_near") is not None and prev_atm is not None:
                        iv_move_pp = (float(m["atm_iv_near"]) - float(prev_atm)) * 100.0
                    pc = thresholds.get("p3_collect") or {}
                    so = second_order_aggregate(
                        contracts, spot, as_of=now.date(),
                        iv_move_pp=iv_move_pp,
                        vanna_gate_vol_pp=float(pc.get("vanna_gate_vol_pp", 0.5)),
                        charm_gate_max_dte=int(pc.get("charm_gate_max_dte", 5)),
                    )
                    fwd_exps = ((forward or {}).get("expirations")) if forward else None
                    struct = m.get("structure") or {}
                    conc = m.get("oi_concentration")
                    p3 = collect_p3(
                        regime_result=full_chain,
                        coverage=coverage,
                        second_order=so,
                        atm_iv_near=m.get("atm_iv_near"),
                        price_rows=hist_rows,
                        forward_expirations=fwd_exps,
                        event_dates=event_dates,
                        as_of=now,
                        spot=spot,
                        call_wall=struct.get("call_wall"),
                        put_wall=struct.get("put_wall"),
                        oi_strikes=conc if isinstance(conc, list) else None,
                        rv_window=int(pc.get("ivrv_rv_window", 20)),
                        rv_min_obs=int(pc.get("ivrv_min_obs", 5)),
                        confluence_band_pct=float(pc.get("confluence_band_pct", 2.0)),
                    )
                except Exception as e:
                    print(f"[警告] {ticker} P1/P3 计算失败（快照保留旧结构层）: {e}")
                snap = build_snapshot(
                    ticker, session_name, m, spot,
                    now.isoformat(timespec="seconds"),
                    analytics_rows=hist_rows, source=source,
                    vol_environment=vol_environment,
                    forward_structure=forward,
                    full_chain=full_chain,
                    coverage=coverage,
                    p3=p3,
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
    else:
        reminder_lines = morning_reminder_lines(now)
    if reminder_lines:
        report = report + "\n\n---\n\n" + "\n\n".join(reminder_lines)

    dry_run = os.environ.get("REPORT_DRY_RUN", "false").lower() == "true"
    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL", "")
    if webhook_url:
        send_discord_message(webhook_url, report, dry_run=dry_run)
    else:
        print("[提示] 未配置 DISCORD_WEBHOOK_URL，本次只打印报告，不发送。")
        send_discord_message("", report, dry_run=True)

    # 幂等：只有真正发送（非 dry-run）才写发送记录；新渲染器路径由 send-report-all 在成功发送后写入
    if not is_forced and not dry_run:
        mark_sent(session_name, today_str)


if __name__ == "__main__":
    main()
