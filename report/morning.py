# -*- coding: utf-8 -*-
"""晨报渲染（P0.3 规格 v1）：对比区 + 每标的展开块 + 注解 + Setup/Gate 状态。"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from engine.annotations import event_card, options_annotation
from engine.gate import gate_pipeline
from report.format import fmt, ticker_heading


def _trading_gap(a_date: str, b_date: str) -> int:
    """两个日期之间的工作日数（不含两端），与 Episode 聚类口径一致。"""
    from datetime import date, timedelta

    try:
        a = date.fromisoformat(a_date[:10])
        b = date.fromisoformat(b_date[:10])
    except (TypeError, ValueError):
        return 0
    if b <= a:
        return 0
    n = 0
    d = a
    while True:
        d += timedelta(days=1)
        if d >= b:
            break
        if d.weekday() < 5:
            n += 1
    return n


def _distance(spot: float, level: Optional[float]) -> Optional[float]:
    if spot is None or level is None:
        return None
    return (spot / level - 1.0) * 100.0


def _options_block(snapshot: Dict[str, Any]) -> List[str]:
    m = snapshot.get("momentum") or {}
    rank = m.get("iv_rank")
    if rank is None:
        rank_txt = "— (历史不足)"
    else:
        rank_txt = f"{rank * 100:.0f}%" if rank <= 1 else f"{rank:.0f}%"
    expmove = m.get("expected_move_pct")
    expmove_txt = f"±{fmt(expmove, 1)}%" if expmove is not None else "N/A"
    skew = m.get("skew")
    skew_txt = f"{fmt(skew, 1)}pp" if skew is not None else "N/A"
    line = (
        f"Options: P/C量 {fmt(m.get('pc_ratio'), 2)} | OI比 {fmt(m.get('pc_oi_ratio'), 2)} | "
        f"ATM IV {fmt_pct_safe(m.get('atm_iv'))} | Skew {skew_txt} | "
        f"Term {fmt(m.get('term_ratio'), 2)} | ExpMove {expmove_txt} | Rank {rank_txt}"
    )
    lines = [line]
    for a in options_annotation(m.get("pc_ratio"), m.get("pc_oi_ratio")):
        lines.append("   ⇒ " + a)
    return lines


def fmt_pct_safe(v: Any) -> str:
    if v is None:
        return "N/A"
    return f"{v * 100:.1f}%"


def _structure_block(snapshot: Dict[str, Any], gex: Optional[float] = None, gex_change: Optional[float] = None) -> List[str]:
    loc = snapshot.get("location") or {}
    spot = snapshot.get("spot")
    lines = ["🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）"]
    gamma = (snapshot.get("regime") or {}).get("gamma", "UNKNOWN")
    gex_txt = f"GEX(存量) {fmt(gex, 0)}" if gex is not None else "GEX(存量) N/A"
    chg_txt = f"GEX Change vs 上次快照 {fmt(gex_change, 0)}" if gex_change is not None else "GEX Change N/A"
    flip_txt = " / ".join(f"≈{f:.2f}" for f in (loc.get("flip_levels") or [])) or "N/A"
    lines.append(f"Gamma: {gamma} | {gex_txt} | {chg_txt} | Flip: {flip_txt}")
    lines.append("   ⇒ 全链负Gamma，波动易被放大（模型层）" if gamma == "NEGATIVE" else "")
    flips = loc.get("flip_levels") or []
    if len(flips) >= 2:
        zone_txt = f"{flips[0]:.0f}–{flips[1]:.0f}"
    elif len(flips) == 1:
        zone_txt = f"≈{flips[0]:.0f}"
    else:
        zone_txt = "N/A"
    lines.append(f"结构观察区: {zone_txt}（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）")
    cw, pw = loc.get("call_wall"), loc.get("put_wall")
    if cw or pw:
        parts = []
        if pw:
            parts.append(f"距 Put Wall {fmt(pw, 0)}: {_dist_str(_distance(spot, pw))}")
        if cw:
            parts.append(f"距 Call Wall {fmt(cw, 0)}: {_dist_str(_distance(spot, cw))}")
        lines.append(" | ".join(parts))
    return [l for l in lines if l]


def _dist_str(v: Optional[float]) -> str:
    return "N/A" if v is None else f"{v:+.1f}%"


def _structure_interpretation(snapshot: Dict[str, Any]) -> List[str]:
    loc = snapshot.get("location") or {}
    spot = snapshot.get("spot")
    mp = (snapshot.get("context") or {}).get("max_pain")
    cw, pw = loc.get("call_wall"), loc.get("put_wall")
    lines = ["🧭 结构解读（全部依赖上方假设）"]
    downs = [f"{fmt(pw, 0)}（Put Wall）"] if pw else []
    ups = []
    if mp:
        ups.append(f"{fmt(mp, 0)}（MaxPain，仅结算参考）")
    if cw:
        ups.append(f"{fmt(cw, 0)}（Call Wall）")
    if downs:
        lines.append(f"• 支撑/压力参考：下方 {' / '.join(downs)}；上方 {' / '.join(ups) if ups else 'N/A'}。")
    flips = loc.get("flip_levels") or []
    if flips:
        lines.append(f"• Gamma 区域：切换参考 {flips[0]:.0f}（Top-3 近似，需全链重定价验证）。")
    lines.append(
        "• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；"
        "实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。"
    )
    lines.append("• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。")
    return lines


def _setup_block(setup_status: Optional[Dict[str, Any]]) -> List[str]:
    if not setup_status:
        return ["Setup: 今日无 Setup 触发（机械检查全部 Setup）"]
    core = setup_status.get("core", {})
    conf = setup_status.get("confirmation", {})
    lines = [
        f"Setup {setup_status.get('setup_id')} {setup_status.get('version', '')} — Core Conditions",
        f"Price Regime {core.get('trend', '?')} | Location {core.get('location', '?')} | Gamma Regime {core.get('gamma', '?')}",
        f"Confirmation: ✓ {conf.get('satisfied', 0)} ｜ ✗ {conf.get('rejected', 0)} ｜ ? {conf.get('unknown', 0)}"
        + (f"（? {', '.join(conf.get('unknown_fields', []))}）" if conf.get("unknown_fields") else ""),
    ]
    q = setup_status.get("qualification")
    if q:
        lift = q.get("oos_lift_pp")
        lift_txt = f"{fmt(lift, 1)}pp" if lift is not None else "N/A"
        lines.append(f"验证状态: N={q.get('n_episodes', 'N/A')} ｜ OOS Lift {lift_txt} ｜ CI 下界 {fmt(q.get('ci_lower'), 2)}")
    pt = setup_status.get("primary_target")
    if pt:
        lines.append(f"Target: {pt.get('metric')} {pt.get('direction')} {pt.get('threshold')} — PENDING（evaluation date 待窗口结束）")
    st = setup_status.get("status")
    if st:
        lines.append(f"Status: {st}")
    return lines


def _activity_block(events: Optional[List[Dict[str, Any]]], stale_note: Optional[str] = None) -> List[str]:
    lines = ["🔺 Activity（事实层，方向 Unknown）"]
    if stale_note:
        lines.append(f"- ⚠️ {stale_note}")
    if events is None:
        lines.append("- Activity 数据缺失（analytics 未提供），不猜测")
        return lines
    if not events:
        lines.append("- 无中高变动事件（全部低等级）")
        return lines
    for ev in events:
        exp = ev.get("expiration") or "?"
        exp_txt = exp[5:] if isinstance(exp, str) and len(exp) >= 10 else str(exp)
        side = "P" if ev.get("type") == "put" else "C"
        lines.extend(
            event_card(
                f"{exp_txt} {ev.get('strike', '?')}{side}",
                ev.get("volume"),
                ev.get("oi_prev"),
                ev.get("open_interest"),
                has_prev_vol=ev.get("volume_prev") is not None,
            )
        )
    return lines


def market_block(market: Optional[Dict[str, Any]]) -> List[str]:
    """市场背景块（整份报告只出现一次）。"""
    if not market:
        return []
    m = []
    if market.get("spy") is not None:
        m.append(f"SPY ${market['spy']:,.2f}")
    if market.get("vix") is not None:
        m.append(f"VIX {market['vix']:.2f}")
    fg = market.get("fg_score")
    fg_rating = market.get("fg_rating")
    if fg is not None:
        m.append(f"CNN 恐惧贪婪 {fg}{'（' + str(fg_rating) + '）' if fg_rating else ''}")
    return ["市场背景： " + " ｜ ".join(m), ""] if m else []


def calendar_block(calendar: Optional[List[str]]) -> List[str]:
    """宏观日历块（整份报告只出现一次）。"""
    if not calendar:
        return []
    return ["## 📅 本周重要美国宏观日历（仅【高】，美东时间）"] + list(calendar) + [""]


def ticker_morning(
    snapshot: Dict[str, Any],
    prev_snapshot: Optional[Dict[str, Any]] = None,
    activity: Optional[List[Dict[str, Any]]] = None,
    setup_status: Optional[Dict[str, Any]] = None,
    gex: Optional[float] = None,
    gex_change: Optional[float] = None,
) -> str:
    """单个标的的晨报区块（不含标题/市场/日历）。"""
    ticker = snapshot.get("ticker", "?")
    lines: List[str] = []
    stale_note = None
    if prev_snapshot:
        p = prev_snapshot.get("spot")
        c = snapshot.get("spot")
        chg = (c / p - 1.0) * 100 if (p and c) else None
        lines.append("📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）")
        lines.append(
            f"{ticker}  昨收 {fmt(p, 2)} → 今晨 {fmt(c, 2)}"
            + (f"（{chg:+.1f}%）" if chg is not None else "")
            + " | 较昨收变动（含盘初走势）"
        )
        gap = _trading_gap(prev_snapshot.get("created_at", "")[:10], snapshot.get("created_at", "")[:10])
        if gap >= 1:
            prev_date = prev_snapshot.get("created_at", "")[:10]
            stale_note = (
                f"OI 增仓/异动基于 {prev_date} 快照对比（标的停更 {gap} 个交易日），"
                "前几日数据可能失真，请谨慎解读"
            )
            lines.append(
                f"⚠️ 标的停更 {gap} 个交易日：以下对比基于 {prev_date} 晚报，"
                f"趋势与 OI 增仓指标需 {gap} 个交易日数据恢复"
            )
        lines.append("")
    lines.append(ticker_heading(ticker))
    lines += _options_block(snapshot)
    lines += _structure_block(snapshot, gex=gex, gex_change=gex_change)
    lines += _structure_interpretation(snapshot)
    lines += _activity_block(activity, stale_note=stale_note)
    lines += _setup_block(setup_status)
    lines.append("")
    lines.append(f"数据溯源：完整表见附录 / thesis / analytics/daily/{snapshot.get('created_at', '')[:10]}/{ticker}_morning.json")
    return "\n".join(lines)


def render_morning(
    snapshot: Dict[str, Any],
    prev_snapshot: Optional[Dict[str, Any]] = None,
    activity: Optional[List[Dict[str, Any]]] = None,
    setup_status: Optional[Dict[str, Any]] = None,
    gex: Optional[float] = None,
    gex_change: Optional[float] = None,
    reminders: Optional[List[str]] = None,
    calendar: Optional[List[str]] = None,
    market: Optional[Dict[str, Any]] = None,
) -> str:
    date = snapshot.get("created_at", "")[:10]
    lines = [f"# 期权晨报 {date}", ""]
    if market:
        lines += market_block(market)
    if calendar:
        lines += calendar_block(calendar)
    if reminders:
        lines += [r for r in reminders if r]
        lines.append("")
    lines.append(ticker_morning(snapshot, prev_snapshot, activity, setup_status, gex, gex_change))
    return "\n".join(lines)
