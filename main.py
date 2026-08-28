#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""OPTION-ALERT P0.1 事件引擎 CLI。

用法示例：
  python main.py store-snapshot snapshot.json
  python main.py detect                          # 处理最近一次快照
  python main.py detect --date 2026-08-21 --all  # 处理某天全部快照
  python main.py evaluate --prices p.csv --rv r.csv --calendar cal.txt --as-of 2026-08-28
  python main.py invalidate SOXX_20260821_A_001 --reason "规则Bug，作废"
  python main.py episodes --calendar cal.txt
  python main.py validate --prices p.csv --calendar cal.txt
  python main.py report --session morning
  python main.py audit

默认数据根目录为仓库根目录；生产环境用 --data-root 指向本地数据目录
（如 D:\\option-alert\\data），并设置 OPTION_ALERT_DATA_ROOT 环境变量。
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
import time
import urllib.error
import urllib.request
from datetime import date, datetime
from pathlib import Path

from engine.edges import direction_components, mechanism_confidence, pricing_proxy, volatility_components
from engine.episode import EpisodeClusterer
from engine.gate import gate_pipeline, qualification
from engine.outcome import OutcomeEngine
from engine.price_series import closes_from_analytics
from engine.regime_map import regime_map
from engine.setup_detector import SetupDetector
from engine.snapshot_builder import build_snapshot, load_analytics_rows
from engine.snapshot import SnapshotStore
from engine.thesis_logger import EventStore
from engine import yaml_mini
from report.evening import render_evening
from report.evening import ticker_evening
from report.morning import calendar_block, market_block, render_morning, ticker_morning
from src.reminders import evening_reminder_lines
from validation.base_rate import conditional_setup_rate, freeze_partition, unconditional_base_rate
from validation.confidence import format_rate
from validation.data_sufficiency import label_for_episodes
from validation.lift import lift_pp

DISCORD_USER_AGENT = "Mozilla/5.0 (option-alert-report/3.0)"


def _ensure_utf8() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass


def _load_csv(path: str, numeric: tuple = ()) -> list:
    rows = []
    with open(path, encoding="utf-8-sig", newline="") as f:
        for raw in csv.DictReader(f):
            row = {k.strip(): v.strip() for k, v in raw.items()}
            for col in numeric:
                if col in row and row[col] != "":
                    row[col] = float(row[col])
                elif col in row:
                    row[col] = None
            rows.append(row)
    return rows


def _load_calendar(path: str) -> list:
    days = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            days.append(line[:10])
    return sorted(days)


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="OPTION-ALERT P0.1 事件引擎")
    p.add_argument("--data-root", default=None, help="数据根目录（默认 env 或仓库根）")
    p.add_argument("--config-root", default="config", help="配置目录")
    sub = p.add_subparsers(dest="command", required=True)

    sp = sub.add_parser("store-snapshot", help="校验并存储快照")
    sp.add_argument("file")

    sp = sub.add_parser("build-snapshot", help="由 analytics 历史行回溯生成快照（回填模式）")
    sp.add_argument("--ticker", required=True)
    sp.add_argument("--session", choices=["morning", "evening", "早报", "晚报"], default="morning")
    sp.add_argument("--date", help="YYYY-MM-DD；缺省用该时段最近一行")
    sp.add_argument("--created-at", help="ISO 时间戳；缺省由日期+时段合成")
    sp.add_argument("--source", default="analytics-backfill")
    sp.add_argument("--analytics-dir", help="旧 analytics CSV 目录；缺省自动探测")

    sp = sub.add_parser("detect", help="机械检测并记录事件")
    sp.add_argument("--date", help="YYYY-MM-DD；缺省用最近快照")
    sp.add_argument("--all", action="store_true", help="处理该日全部标的")

    sp = sub.add_parser("evaluate", help="回填 Outcome（确定性引擎）")
    sp.add_argument("--prices")
    sp.add_argument("--rv")
    sp.add_argument("--path")
    sp.add_argument("--calendar")
    sp.add_argument("--as-of", help="ISO 时间戳；缺省用今天")
    sp.add_argument("--event-id")
    sp.add_argument("--ticker", help="只评价该标的；缺省按事件自动分组")

    sp = sub.add_parser("invalidate", help="作废事件（规则Bug/数据污染）")
    sp.add_argument("event_id")
    sp.add_argument("--reason", required=True)
    sp.add_argument("--as-of")

    sp = sub.add_parser("episodes", help="重算 Episode 聚类并写盘")
    sp.add_argument("--calendar")

    sp = sub.add_parser("validate", help="验证摘要（Base Rate/Lift/CI/数据状态）")
    sp.add_argument("--prices")
    sp.add_argument("--calendar")

    sp = sub.add_parser("report", help="渲染晨报/晚报")
    sp.add_argument("--session", choices=["morning", "evening"], default="morning")
    sp.add_argument("--date", help="YYYY-MM-DD；缺省用最新快照")
    sp.add_argument("--ticker", help="缺省用最新快照")
    sp.add_argument("--out")

    sp = sub.add_parser("render-morning", help="按 P0.3 规格渲染晨报")
    sp.add_argument("--date")
    sp.add_argument("--ticker", required=True)
    sp.add_argument("--out")

    sp = sub.add_parser("render-evening", help="按 P0.3 规格渲染晚报")
    sp.add_argument("--date")
    sp.add_argument("--ticker", required=True)
    sp.add_argument("--out")

    sp = sub.add_parser("gate-summary", help="各 Setup 资格/决策摘要")

    sp = sub.add_parser("regime-map", help="全链重定价（模型隐含 GEX 过零点）")
    sp.add_argument("--contracts", required=True, help="合约 JSON 列表文件")
    sp.add_argument("--spot", type=float, required=True)
    sp.add_argument("--as-of", help="YYYY-MM-DD，用于 dte 计算")

    sp = sub.add_parser("send-report", help="渲染新格式报告并发送 Discord")
    sp.add_argument("--session", choices=["morning", "evening"], required=True)
    sp.add_argument("--ticker", required=True)
    sp.add_argument("--date")
    sp.add_argument("--webhook-url", default="")
    sp.add_argument("--dry-run", action="store_true", help="只打印不发送")
    sp.add_argument("--verify", action="store_true", help="只验证 webhook 有效性并打印目标频道")

    sp = sub.add_parser("send-report-all", help="合并所有 ticker 为一份报告发送（市场/日历只出现一次）")
    sp.add_argument("--session", choices=["morning", "evening"], required=True)
    sp.add_argument("--date")
    sp.add_argument("--webhook-url", default="")
    sp.add_argument("--dry-run", action="store_true")
    sp.add_argument("--verify", action="store_true")

    sp = sub.add_parser("audit", help="哈希链完整性 + 每日触发审计")
    return p


def _data_root(args) -> Path:
    import os

    return Path(args.data_root or os.environ.get("OPTION_ALERT_DATA_ROOT") or Path(__file__).resolve().parent)


def cmd_store_snapshot(args) -> int:
    snap = json.loads(Path(args.file).read_text(encoding="utf-8"))
    stored = SnapshotStore(_data_root(args)).store(snap)
    print(f"快照已存储: {stored['ticker']} {stored['session']} "
          f"{stored['created_at'][:10]} hash={stored['snapshot_hash'][:12]}...")
    return 0


def cmd_build_snapshot(args) -> int:
    data_root = _data_root(args)
    repo_root = Path(__file__).resolve().parent
    if args.analytics_dir:
        paths = [Path(args.analytics_dir) / f"{args.ticker.upper()}.csv"]
    else:
        # 兼容：新 analytics/ 与旧 data/analytics/ 与仓库默认位置
        paths = [
            data_root / "analytics" / f"{args.ticker.upper()}.csv",
            data_root / "data" / "analytics" / f"{args.ticker.upper()}.csv",
            repo_root / "data" / "analytics" / f"{args.ticker.upper()}.csv",
        ]
    rows = next((load_analytics_rows(str(p)) for p in paths if p.exists()), [])
    if not rows:
        print(f"没有可用 analytics 历史: {args.ticker.upper()}")
        return 1
    sess = {"早报": "morning", "晚报": "evening"}.get(args.session, args.session)
    if args.date:
        day_rows = [r for r in rows if r.get("date") == args.date and r.get("session") == sess]
    else:
        day_rows = [r for r in rows if r.get("session") == sess]
    if not day_rows:
        print(f"找不到 {args.ticker.upper()} {args.date or ''} {sess} 的记录")
        return 1
    row = day_rows[-1]
    date = row["date"]
    created_at = args.created_at or (
        f"{date}T10:15:00-04:00" if sess == "morning" else f"{date}T16:30:00-04:00"
    )
    thresholds = yaml_mini.load(Path(args.config_root) / "thresholds.yaml")
    snap = build_snapshot(
        args.ticker.upper(), sess, row, row.get("price"), created_at,
        analytics_rows=rows, thresholds=thresholds, source=args.source,
    )
    stored = SnapshotStore(_data_root(args)).store(snap)
    missing = sum(1 for v in stored["data_sufficiency"].values() if v in ("INSUFFICIENT_DATA", "N/A"))
    print(
        f"快照已存储: {stored['ticker']} {stored['session']} {stored['created_at']} "
        f"hash={stored['snapshot_hash'][:12]}... 待积累/缺失字段={missing}"
    )
    return 0


def cmd_detect(args) -> int:
    store = EventStore(_data_root(args))
    snaps = SnapshotStore(_data_root(args))
    if args.date:
        snap_list = snaps.load_day(args.date)
    elif args.all:
        snap_list = []
        for day in snaps.list_days():
            snap_list.extend(snaps.load_day(day))
    else:
        latest = snaps.load_latest()
        snap_list = [latest] if latest else []
    if not snap_list:
        print("没有可用快照")
        return 1

    detector = SetupDetector(args.config_root)
    existing = store.read_model(verify=False)["events"]
    seen = {(e["snapshot_hash"], e["setup_id"]) for e in existing}
    new_events = 0
    for snap in snap_list:
        events, audits = detector.detect(snap)
        for a in audits:
            store.audit(a)
        for ev in events:
            key = (ev["snapshot_hash"], ev["setup_id"])
            if key in seen:
                print(f"跳过（已存在）: {ev['ticker']} {ev['setup_id']} @ {ev['created_at'][:16]}")
                continue
            stored = store.append_event(ev)
            seen.add(key)
            new_events += 1
            print(f"事件已记录: {stored['event_id']} (setup={stored['setup_id']}, "
                  f"hash={stored['event_hash'][:12]}...)")
    print(f"新增事件 {new_events} 条，审计 {len(snap_list)} 份快照")
    return 0


def _analytics_rows(data_root: Path, ticker: str) -> list:
    for p in (
        data_root / "analytics" / f"{ticker}.csv",
        data_root / "data" / "analytics" / f"{ticker}.csv",
    ):
        if p.exists():
            return load_analytics_rows(str(p))
    return []


def cmd_evaluate(args) -> int:
    data_root = _data_root(args)
    store = EventStore(data_root)
    model = store.read_model()
    if model["errors"]:
        print("警告：事件库存在完整性错误，先运行 audit：")
        for e in model["errors"]:
            print("  -", e)
        return 1
    events = model["events"]
    if args.event_id:
        events = [e for e in events if e["event_id"] == args.event_id]
    if args.ticker:
        events = [e for e in events if e["ticker"] == args.ticker]
    open_events = [e for e in events if e.get("lifecycle") != "CLOSED"]
    if not open_events:
        print("没有待评价的 OPEN 事件")
        return 0
    rv = _load_csv(args.rv, ("rv5d", "rv20d")) if args.rv else None
    path = _load_csv(args.path, ("close",)) if args.path else None
    cal = _load_calendar(args.calendar) if args.calendar else None
    prices_by_ticker = {}
    if args.prices:
        prices_all = _load_csv(args.prices, ("close",))
        for t in {e["ticker"] for e in open_events}:
            prices_by_ticker[t] = prices_all
    else:
        # 自动从 analytics 历史生成该标的的收盘价序列（晚报优先）
        for t in {e["ticker"] for e in open_events}:
            prices_by_ticker[t] = closes_from_analytics(_analytics_rows(data_root, t))
    engine = OutcomeEngine(store)
    n = 0
    for ev in open_events:
        prices = prices_by_ticker.get(ev["ticker"], [])
        if not prices:
            print(f"{ev['event_id']}: 无可用价格序列（analytics 为空），保持 PENDING")
            continue
        rev = engine.evaluate(ev, prices, rv=rv, path=path, trading_days=cal, now=args.as_of)
        if rev is None:
            print(f"{ev['event_id']}: 窗口未结束/数据不足，保持 PENDING")
            continue
        n += 1
        print(f"{ev['event_id']}: -> {rev['result']} "
              f"(metric_value={rev.get('metric_value')}, reason={rev.get('reason')})")
    print(f"写入 revision {n} 条")
    return 0


def cmd_invalidate(args) -> int:
    store = EventStore(_data_root(args))
    model = store.read_model()
    match = [e for e in model["events"] if e["event_id"] == args.event_id]
    if not match:
        print(f"事件不存在: {args.event_id}")
        return 1
    rev = OutcomeEngine(store).invalidate(match[0], args.reason, as_of=args.as_of)
    if rev is None:
        print("已存在同锚点 revision，跳过")
    else:
        print(f"已作废: {args.event_id} -> {rev['revision_id']}")
    return 0


def cmd_episodes(args) -> int:
    store = EventStore(_data_root(args))
    model = store.read_model()
    cal = _load_calendar(args.calendar) if args.calendar else None
    eps = EpisodeClusterer(store).cluster(model["events"], trading_days=cal)
    store.write_episodes(eps)
    print(f"Episode 聚类完成: {len(eps)} 条（rule=episode_v1）")
    for ep in eps:
        print(f"  {ep['episode_id']}: {ep['setup_id']}/{ep['ticker']} "
              f"events={ep['n_events']} outcome={ep['representative_outcome']}")
    return 0


def cmd_validate(args) -> int:
    store = EventStore(_data_root(args))
    model = store.read_model()
    thresholds = yaml_mini.load(Path(args.config_root) / "thresholds.yaml")
    setups = yaml_mini.load(Path(args.config_root) / "setups.yaml")["setups"]
    cal = _load_calendar(args.calendar) if args.calendar else None
    eps = EpisodeClusterer(store).cluster(model["events"], trading_days=cal)
    prices = _load_csv(args.prices, ("close",)) if args.prices else None
    setups_cfg = yaml_mini.load(Path(args.config_root) / "setups.yaml")
    freeze_date = setups_cfg.get("rule_freeze_date", "2026-08-22")

    for s in setups:
        sid = s["setup_id"]
        s_eps = [e for e in eps if e["setup_id"] == sid]
        pre, post = freeze_partition(s_eps, freeze_date)
        cr = conditional_setup_rate(post)
        label = label_for_episodes(len(post), thresholds)
        pt = s["primary_target"]
        base = {"rate": None, "n": 0}
        if pt["metric"] == "3D_close_return" and prices:
            base = unconditional_base_rate(
                prices, pt["direction"], pt["threshold"], int(pt["horizon"][:-1])
            )
        lift = None
        if cr["rate"] is not None and base.get("rate") is not None:
            lift = lift_pp(cr["rate"], base["rate"])
        print(f"Setup {sid}: episodes={len(s_eps)} 数据状态={label}")
        if cr["rate"] is None:
            print(f"  条件率: N/A（无已评价独立Episode，排除 {cr['excluded']} 个非样本）")
        else:
            print(f"  条件率: {format_rate(cr['confirmed'], cr['n'])}")
        print(f"  冻结划分: 冻结后 OOS Episode={len(post)} | 冻结前(仅假设)={len(pre)}")
        invalids = sum(1 for e in s_eps if e.get("representative_outcome") == "INVALIDATED")
        if s_eps and invalids / len(s_eps) > thresholds.get("invalidated_ratio_alert", 0.30):
            print(f"  [数据质量告警] INVALIDATED 占比 {invalids/len(s_eps):.0%} "
                  f"> {thresholds.get('invalidated_ratio_alert', 0.30):.0%}，请审查数据质量")
        print(f"  Base Rate: {base['rate']*100:.1f}% (n={base['n']})"
              if base["rate"] is not None else "  Base Rate: N/A")
        print(f"  Lift: {lift:+.1f}pp" if lift is not None else "  Lift: N/A")
    return 0


def cmd_report(args) -> int:
    store = EventStore(_data_root(args))
    model = store.read_model()
    snaps = SnapshotStore(_data_root(args))
    snap = None
    if args.date and args.ticker:
        try:
            snap = snaps.load(args.date, args.ticker.upper(), args.session)
        except FileNotFoundError:
            snap = None
    if snap is None:
        snap = snaps.load_latest()
    if snap is None:
        print("没有可用快照，请先运行 store-snapshot / build-snapshot / pipeline_snapshot")
        return 1
    if args.session == "morning":
        text = render_morning(snap, market=_market_context("morning"), calendar=_calendar_lines())
    else:
        text = render_evening(snap, market=_market_context("evening"), calendar=_calendar_lines())
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        print(f"报告已写入: {args.out}")
    else:
        print(text)
    return 0


def _activity_from_analytics(data_root: Path, ticker: str, session: str) -> list:
    rows = _analytics_rows(data_root, ticker)
    sess = "evening" if session == "evening" else "morning"  # load_analytics_rows 已归一化
    row = next((r for r in reversed(rows) if r.get("session") == sess), None)
    if row is None:
        return None
    surge = (row or {}).get("top_surge") or []
    out = []
    for s in surge:
        out.append({
            "expiration": s.get("expiration"),
            "strike": s.get("strike"),
            "type": s.get("type"),
            "volume": s.get("volume"),
            "volume_prev": s.get("volume_prev"),
            "oi_prev": s.get("oi_prev"),
            "open_interest": s.get("oi") or s.get("open_interest"),
            "last_price": s.get("last_price"),
            "volume_source": s.get("volume_source"),
        })
    return out


def _market_context(session: str | None = None) -> dict:
    out = {"spy": None, "qqq": None, "vix": None, "fg_score": None, "fg_rating": None, "vol_environment": None}
    try:
        from src import data_fetcher as fetcher

        if session == "evening":
            # 晚报市场背景 SPY 用常规时段收盘价，避免盘后价（与 ticker 口径一致）
            ohlc = fetcher.fetch_ohlc_yfinance("SPY")
            spy = ohlc[3] if (ohlc and ohlc[3] is not None) else None
            if spy is None:
                spy, _ = fetcher.fetch_spot("SPY")
        else:
            spy, _ = fetcher.fetch_spot("SPY")
        out["spy"] = spy
    except Exception:
        pass
    try:
        from src import data_fetcher as fetcher

        qqq, _ = fetcher.fetch_spot_yfinance("QQQ")
        out["qqq"] = qqq
    except Exception:
        pass
    try:
        from src import data_fetcher as fetcher

        vix, _ = fetcher.fetch_spot_yfinance("^VIX")
        out["vix"] = vix
    except Exception:
        pass
    try:
        from src.fear_greed import fetch_fear_greed

        fg = fetch_fear_greed()
        if fg:
            out["fg_score"] = fg.get("score")
            out["fg_rating"] = fg.get("rating")
    except Exception:
        pass
    return out


def _calendar_lines():
    try:
        from datetime import datetime
        from zoneinfo import ZoneInfo

        from src.calendars import build_macro_lines

        return build_macro_lines(datetime.now(ZoneInfo("America/New_York")))
    except Exception:
        return None


def _macro_event_dates():
    """本周剩余【高】美国事件的结构化日期（供事件差分；失败返回 None，差分自动沉默）。"""
    try:
        from datetime import datetime
        from zoneinfo import ZoneInfo

        from src.calendars import macro_event_dates

        return macro_event_dates(datetime.now(ZoneInfo("America/New_York")))
    except Exception:
        return None


def _load_tickers() -> list:
    path = Path(__file__).resolve().parent / "config" / "tickers.txt"
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            out.append(line.upper())
    return out


def _load_snapshot_or_latest(snaps: SnapshotStore, date_str: str, ticker: str, session: str):
    try:
        return snaps.load(date_str, ticker, session), date_str
    except FileNotFoundError:
        for d in reversed(snaps.list_days()):
            try:
                return snaps.load(d, ticker, session), d
            except FileNotFoundError:
                continue
        return None, None


def _prev_evening_snapshot(snaps: SnapshotStore, date_str: str, ticker: str):
    for d in reversed([x for x in snaps.list_days() if x < date_str]):
        try:
            return snaps.load(d, ticker, "evening")
        except FileNotFoundError:
            continue
    return None


def _setup_status(snapshot: dict, store: EventStore, config_root: Path, thresholds: dict) -> dict:
    detector = SetupDetector(str(config_root))
    events, _ = detector.detect(snapshot)
    model = store.read_model(verify=False)
    eps = EpisodeClusterer(store).cluster(model["events"])
    if not events:
        return {"triggered": False, "display": "今日无 Setup 触发（机械检查全部 Setup）"}
    ev = events[0]
    sid = ev["setup_id"]
    s_eps = [e for e in eps if e["setup_id"] == sid]
    n = sum(1 for e in s_eps if e.get("representative_outcome") in ("CONFIRMED", "REJECTED"))
    qual = qualification(n_episodes=n, n_regimes=0, oos_lift_pp=None, ci_lower=None,
                         oos_available=False, thresholds=thresholds)
    conf = ev.get("confirmation_status", [])
    satisfied = sum(1 for c in conf if c.get("met") is True)
    rejected_c = sum(1 for c in conf if c.get("met") is False)
    unknown = sum(1 for c in conf if c.get("met") is None)
    unknown_fields = [c.get("name") for c in conf if c.get("met") is None]
    direction = direction_components(snapshot)
    vol = volatility_components(snapshot)
    pricing = pricing_proxy(snapshot.get("momentum", {}).get("atm_iv"))
    mech = mechanism_confidence(snapshot)
    gate = gate_pipeline(
        setup_trigger_met=True,
        qual=qual,
        direction=direction,
        volatility=vol,
        pricing=pricing,
        mechanism=mech,
        confirmation={"satisfied": satisfied, "required": len(conf)},
        data_ok=True,
    )
    regime = snapshot.get("regime") or {}
    location = snapshot.get("location") or {}
    pt = ev.get("primary_target") or {}
    return {
        "triggered": True,
        "setup_id": sid,
        "version": ev.get("setup_version", "v1"),
        "core": {
            "trend": f"{regime.get('trend', '?')}",
            "location": location.get("price_location") or "?",
            "gamma": f"{regime.get('gamma', '?')}（模型层）",
        },
        "confirmation": {
            "satisfied": satisfied,
            "rejected": rejected_c,
            "unknown": unknown,
            "unknown_fields": unknown_fields,
        },
        "qualification": {
            "n_episodes": qual["n_episodes"],
            "oos_lift_pp": qual.get("oos_lift_pp"),
            "ci_lower": qual.get("ci_lower"),
            "level": qual["level"],
        },
        "primary_target": pt,
        "status": gate["display"],
    }


def _render_status_arg(setup_status: dict) -> dict:
    if not setup_status.get("triggered"):
        return None
    return setup_status


def cmd_render_morning(args) -> int:
    data_root = _data_root(args)
    snaps = SnapshotStore(data_root)
    store = EventStore(data_root)
    ticker = args.ticker.upper()
    date_str = args.date or (snaps.load_latest() or {}).get("created_at", "")[:10]
    snap = snaps.load(date_str, ticker, "morning")
    prev = _prev_evening_snapshot(snaps, date_str, ticker)
    thresholds = yaml_mini.load(Path(args.config_root) / "thresholds.yaml")
    status = _setup_status(snap, store, Path(args.config_root), thresholds)
    text = render_morning(
        snap,
        prev_snapshot=prev,
        activity=_activity_from_analytics(data_root, ticker, "morning"),
        setup_status=_render_status_arg(status),
        market=_market_context("morning"),
        calendar=_calendar_lines(),
        event_dates=_macro_event_dates(),
    )
    _write_report(args.out, text)
    return 0


def cmd_render_evening(args) -> int:
    data_root = _data_root(args)
    snaps = SnapshotStore(data_root)
    store = EventStore(data_root)
    ticker = args.ticker.upper()
    date_str = args.date or (snaps.load_latest() or {}).get("created_at", "")[:10]
    snap = snaps.load(date_str, ticker, "evening")
    morning = None
    try:
        morning = snaps.load(date_str, ticker, "morning")
    except FileNotFoundError:
        morning = None
    thresholds = yaml_mini.load(Path(args.config_root) / "thresholds.yaml")
    status = _setup_status(snap, store, Path(args.config_root), thresholds)
    text = render_evening(
        snap,
        morning=morning,
        activity=_activity_from_analytics(data_root, ticker, "evening"),
        setup_status=_render_status_arg(status),
        reminders=evening_reminder_lines(datetime.fromisoformat(f"{date_str}T17:00:00-04:00")) if date_str else [],
        market=_market_context("evening"),
        calendar=_calendar_lines(),
        event_dates=_macro_event_dates(),
    )
    _write_report(args.out, text)
    return 0


def _write_report(out: str | None, text: str) -> None:
    if out:
        p = Path(out)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
        print(f"报告已写入: {out}")
    else:
        print(text)


def cmd_gate_summary(args) -> int:
    data_root = _data_root(args)
    snaps = SnapshotStore(data_root)
    store = EventStore(data_root)
    thresholds = yaml_mini.load(Path(args.config_root) / "thresholds.yaml")
    print("== Gate 摘要（按最新快照） ==")
    for day in reversed(snaps.list_days()):
        for snap in snaps.load_day(day):
            status = _setup_status(snap, store, Path(args.config_root), thresholds)
            if status.get("triggered"):
                q = status.get("qualification", {})
                print(
                    f"{snap['created_at'][:10]} {snap['ticker']} {snap['session']} | Setup {status['setup_id']} | "
                    f"资格 {q.get('level')} (N={q.get('n_episodes')}) | {status['status']}"
                )
        break
    return 0


def cmd_regime_map(args) -> int:
    contracts = json.loads(Path(args.contracts).read_text(encoding="utf-8"))
    as_of = date.fromisoformat(args.as_of) if args.as_of else None
    result = regime_map(contracts, args.spot, as_of=as_of)
    if result is None:
        print("无法计算（无有效合约或 spot 无效）")
        return 1
    print(
        f"模型隐含 GEX 过零点: {result['flip_levels'] or '无（单边）'} | "
        f"当前区: {result['spot_zone']} | 用合约 {result['n_contracts_used']} 个，跳过 {result['n_contracts_skipped']}"
    )
    print(f"模式: {result['vol_surface_mode']} | 假设: {'; '.join(result['assumptions'])}")
    return 0


def _chunk_text(text: str, limit: int = 1900) -> list:
    """按行切分；单行超限时硬切，保证每条 ≤ limit。"""
    chunks = []
    current = []
    size = 0
    for line in text.split("\n"):
        if len(line) > limit:
            if current:
                chunks.append("\n".join(current))
                current, size = [], 0
            for i in range(0, len(line), limit):
                chunks.append(line[i:i + limit])
            continue
        if size + len(line) + 1 > limit and current:
            chunks.append("\n".join(current))
            current, size = [], 0
        current.append(line)
        size += len(line) + 1
    if current:
        chunks.append("\n".join(current))
    return chunks


def _post_webhook(webhook: str, body: dict) -> None:
    """发送单条消息到 Discord webhook：429/5xx 重试一次。"""
    payload = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(
        webhook,
        data=payload,
        headers={"Content-Type": "application/json", "User-Agent": DISCORD_USER_AGENT},
    )
    for attempt in (1, 2):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                if resp.status >= 300:
                    raise RuntimeError(f"Discord webhook HTTP {resp.status}")
            return
        except urllib.error.HTTPError as e:
            if attempt == 1 and e.code in (429, 500, 502, 503, 504):
                time.sleep(1.5)
                continue
            raise


def _discord_send(webhook: str, text: str) -> None:
    """发送到 Discord webhook：切分 + 重试（纯文本，无彩色卡片）。"""
    webhook = (webhook or "").strip()
    if not webhook:
        raise RuntimeError("webhook URL 为空")
    if not text or not text.strip():
        raise RuntimeError("消息内容为空，拒绝发送")
    try:
        webhook_id = webhook.rstrip("/").rsplit("/", 2)[-2]
    except IndexError:
        webhook_id = "?"
    print(f"webhook id: {webhook_id}")
    for chunk in _chunk_text(text):
        _post_webhook(webhook, {"content": chunk})


def cmd_send_report(args) -> int:
    data_root = _data_root(args)
    snaps = SnapshotStore(data_root)
    store = EventStore(data_root)
    thresholds = yaml_mini.load(Path(args.config_root) / "thresholds.yaml")
    ticker = args.ticker.upper()
    date_str = args.date or (snaps.load_latest() or {}).get("created_at", "")[:10]

    if args.verify:
        webhook = (args.webhook_url or "").strip()
        if not webhook:
            print("webhook URL 为空（secret 未设置？）")
            return 1
        try:
            req = urllib.request.Request(webhook, headers={"User-Agent": DISCORD_USER_AGENT})
            with urllib.request.urlopen(req, timeout=30) as resp:
                info = json.loads(resp.read().decode("utf-8"))
            print(
                f"webhook 有效: id={info.get('id')} name={info.get('name')!r} "
                f"channel_id={info.get('channel_id')}"
            )
            return 0
        except Exception as e:
            print(f"webhook 验证失败: {type(e).__name__}: {e}")
            return 1

    event_dates = _macro_event_dates()
    if args.session == "morning":
        snap, used_date = _load_snapshot_or_latest(snaps, date_str, ticker, "morning")
        if snap is None:
            print(f"无 morning 快照，跳过（当日晨报未生成）")
            return 0
        date_str = used_date
        prev = _prev_evening_snapshot(snaps, date_str, ticker)
        status = _setup_status(snap, store, Path(args.config_root), thresholds)
        text = render_morning(
            snap,
            prev_snapshot=prev,
            activity=_activity_from_analytics(data_root, ticker, "morning"),
            setup_status=_render_status_arg(status),
            market=_market_context("morning"),
            calendar=_calendar_lines(),
            event_dates=event_dates,
        )
    else:
        snap, used_date = _load_snapshot_or_latest(snaps, date_str, ticker, "evening")
        if snap is None:
            print(f"无 evening 快照，跳过（当日晚报未生成）")
            return 0
        date_str = used_date
        morning = None
        try:
            morning = snaps.load(date_str, ticker, "morning")
        except FileNotFoundError:
            morning = None
        status = _setup_status(snap, store, Path(args.config_root), thresholds)
        text = render_evening(
            snap,
            morning=morning,
            activity=_activity_from_analytics(data_root, ticker, "evening"),
            setup_status=_render_status_arg(status),
            reminders=evening_reminder_lines(datetime.fromisoformat(f"{date_str}T17:00:00-04:00")) if date_str else [],
            market=_market_context("evening"),
            calendar=_calendar_lines(),
            event_dates=event_dates,
        )

    if args.dry_run:
        print(text)
        return 0
    if not args.webhook_url:
        print("未提供 --webhook-url，本次只打印不发送")
        print(text)
        return 1
    _discord_send(args.webhook_url, text)
    print(f"已发送 {args.session} {ticker} {date_str} 到 Discord")
    return 0


def cmd_send_report_all(args) -> int:
    data_root = _data_root(args)
    snaps = SnapshotStore(data_root)
    store = EventStore(data_root)
    thresholds = yaml_mini.load(Path(args.config_root) / "thresholds.yaml")
    tickers = _load_tickers()
    date_str = args.date or (snaps.load_latest() or {}).get("created_at", "")[:10]

    if args.verify:
        webhook = (args.webhook_url or "").strip()
        if not webhook:
            print("webhook URL 为空（secret 未设置？）")
            return 1
        try:
            req = urllib.request.Request(webhook, headers={"User-Agent": DISCORD_USER_AGENT})
            with urllib.request.urlopen(req, timeout=30) as resp:
                info = json.loads(resp.read().decode("utf-8"))
            print(
                f"webhook 有效: id={info.get('id')} name={info.get('name')!r} "
                f"channel_id={info.get('channel_id')}"
            )
            return 0
        except Exception as e:
            print(f"webhook 验证失败: {type(e).__name__}: {e}")
            return 1

    session_zh = "晨报" if args.session == "morning" else "晚报"
    market = _market_context(args.session)
    cal = _calendar_lines()
    event_dates = _macro_event_dates()
    body = []
    ticker_hl = {}
    used_dates = []
    render_failed = 0
    market_ve = None
    for t in tickers:
        snap, used_date = _load_snapshot_or_latest(snaps, date_str, t, args.session)
        if snap is None:
            print(f"无 {args.session} 快照，跳过 {t}")
            continue
        if market_ve is None:
            snap_ve = (snap.get("context") or {}).get("vol_environment")
            if isinstance(snap_ve, dict):
                market_ve = snap_ve
        used_dates.append(used_date)
        try:
            status = _setup_status(snap, store, Path(args.config_root), thresholds)
            activity = _activity_from_analytics(data_root, t, args.session)
            if args.session == "morning":
                prev = _prev_evening_snapshot(snaps, used_date, t)
                text = ticker_morning(
                    snap,
                    prev_snapshot=prev,
                    activity=activity,
                    setup_status=_render_status_arg(status),
                    event_dates=event_dates,
                )
            else:
                morning = None
                try:
                    morning = snaps.load(used_date, t, "morning")
                except FileNotFoundError:
                    morning = None
                text = ticker_evening(
                    snap,
                    morning=morning,
                    activity=activity,
                    setup_status=_render_status_arg(status),
                    event_dates=event_dates,
                )
            prev_ref = prev if args.session == "morning" else (morning if args.session == "evening" else None)
            from report.highlight import build_highlights

            ticker_hl[t] = build_highlights(snap, activity=activity, prev=prev_ref, event_dates=event_dates)
        except Exception as e:
            render_failed += 1
            text = f"⚠️ {t} 区块渲染失败（已跳过）：{type(e).__name__}: {e}"
            print(text)
        body.append(text)

    if not body:
        print(f"无 {args.session} 快照，本次跳过（正常情况，例如周末/标的未抓取）")
        return 0
    if market_ve:
        market = {**market, "vol_environment": market_ve}
    final_date = max(used_dates)
    if date_str and final_date != date_str and not any(d == date_str for d in used_dates):
        # 整个时段都没有目标日期快照（全部回退到旧日期）：
        # 手动 FORCE 测试时不要把旧日期报告混进当天推送，直接跳过并说明原因。
        import os

        force = os.environ.get("FORCE", "").lower() == "true"
        if force:
            print(
                f"[FORCE] {date_str} 无任何 {args.session} 快照（最近为 {final_date}），"
                "为避免把旧日期报告混入本次推送，跳过发送"
            )
            return 0
    lines = [f"# 📊 期权{session_zh} {final_date}", ""]
    mixed = len(set(used_dates)) > 1
    if date_str and (final_date != date_str or mixed):
        if final_date != date_str:
            lines.append(
                f"⚠️ 数据时点说明：{date_str} 该时段快照未生成，本报告使用最近快照（{final_date}），"
                "内容为补发/回退数据"
            )
        elif mixed:
            lines.append(
                f"⚠️ 数据时点说明：部分标的缺少 {date_str} 快照，本报告混用最近可用快照"
                f"（最早 {min(used_dates)}，最新 {final_date}），请以各标的区块数据为准"
            )
        lines.append("")
    lines += market_block(market)
    lines += calendar_block(cal)
    from report.highlight import aggregate_highlights, highlights_section

    agg_items, truncated = aggregate_highlights(ticker_hl)
    hl_note = None
    no_hl = [t for t in tickers if not ticker_hl.get(t)]
    notes = []
    if truncated:
        notes.append("…（其余重点已截断，详见各标的区块）")
    if no_hl and agg_items:
        notes.append(f"其余 {len(no_hl)} 个标的今日无重点项（机械检查 highlight_v1）")
    if notes:
        hl_note = "\n".join(notes)
    lines += highlights_section(agg_items, note=hl_note)
    if args.session == "evening" and final_date:
        reminders = evening_reminder_lines(datetime.fromisoformat(f"{final_date}T17:00:00-04:00"))
        if reminders:
            lines += reminders + [""]
    lines += body
    full = "\n".join(lines)
    if args.dry_run:
        print(full)
        return 0
    if not args.webhook_url:
        print("未提供 --webhook-url")
        return 1
    _discord_send(args.webhook_url, full)
    print(f"已发送合并{session_zh}（{len(body)} 个标的）到 Discord")
    return 1 if render_failed else 0


def cmd_audit(args) -> int:
    store = EventStore(_data_root(args))
    ok, errors = store.verify()
    print("== 完整性 ==")
    if ok:
        print("哈希链 OK（内容哈希 + prev_hash 链）")
    else:
        for e in errors:
            print("  [ERROR]", e)

    print("== 每日触发审计 ==")
    snaps = SnapshotStore(_data_root(args))
    audits = store.load_audits()
    audit_keys = {(a["date"], a["ticker"], a["session"], a["setup_id"]) for a in audits if a.get("checked")}
    setups = yaml_mini.load(Path(args.config_root) / "setups.yaml")["setups"]
    setup_ids = [s["setup_id"] for s in setups]
    missing = 0
    for day in snaps.list_days():
        for snap in snaps.load_day(day):
            for sid in setup_ids:
                if (day, snap["ticker"], snap["session"], sid) not in audit_keys:
                    missing += 1
                    print(f"  缺失检查: {day} {snap['ticker']} {snap['session']} setup={sid}")
    if missing == 0:
        print("所有 (日期, 标的, 时段, Setup) 均已机械检查")
    else:
        print(f"缺失 {missing} 项检查")
    return 0 if ok and missing == 0 else 1


def main() -> int:
    _ensure_utf8()
    args = build_parser().parse_args()
    return {
        "store-snapshot": cmd_store_snapshot,
        "build-snapshot": cmd_build_snapshot,
        "detect": cmd_detect,
        "evaluate": cmd_evaluate,
        "invalidate": cmd_invalidate,
        "episodes": cmd_episodes,
        "validate": cmd_validate,
        "report": cmd_report,
        "render-morning": cmd_render_morning,
        "render-evening": cmd_render_evening,
        "gate-summary": cmd_gate_summary,
        "regime-map": cmd_regime_map,
        "send-report": cmd_send_report,
        "send-report-all": cmd_send_report_all,
        "audit": cmd_audit,
    }[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
