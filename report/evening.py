# -*- coding: utf-8 -*-
"""晚报渲染（P0.3 规格 v1）：Thesis Scorecard + 关键位状态 + Target 状态 + 每标的。"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from report.format import fmt
from report.morning import (
    _activity_block,
    _data_quality_line,
    _day_range,
    _event_differential_lines,
    _forward_block,
    _options_block,
    _setup_block,
    _structure_block,
    _structure_interpretation,
    _trading_gap,
    _vix_spread_line,
    _vol_env,
    calendar_block,
    market_block,
    ticker_heading,
)


def _scorecard(morning: Optional[Dict[str, Any]], evening: Dict[str, Any], key_level_status: Optional[str]) -> List[str]:
    ticker = evening.get("ticker", "?")
    lines = ["📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）"]
    if morning is None:
        lines.append(f"{ticker}: 晨报缺失（当日未生成），只报收盘事实")
    else:
        gap = _trading_gap(morning.get("created_at", "")[:10], evening.get("created_at", "")[:10])
        if gap >= 1:
            lines.append(f"{ticker}: ⚠️ 晨报为 {gap} 个交易日前（标的可能停更），仅作收盘事实对照")
        m_spot = morning.get("spot")
        e_spot = evening.get("spot")
        # 今开 = 当日常规时段开盘价（晨报快照 context.day_open，缺则用晚报快照的，再缺回退晨报 spot）
        m_open = ((morning.get("context") or {}).get("day_open"))
        if m_open is None:
            m_open = ((evening.get("context") or {}).get("day_open"))
        m_ref = m_open if m_open is not None else m_spot
        ref_label = "今开" if m_open is not None else "今晨"
        if m_ref and e_spot:
            chg = (e_spot / m_ref - 1.0) * 100
            lines.append(
                f"{ticker}: {ref_label} {fmt(m_ref, 2)} → 收盘 {fmt(e_spot, 2)}（{chg:+.1f}%）"
                + (_day_range(evening) or "")
            )
    if key_level_status:
        lines.append(f"关键位状态: {key_level_status}——纯事实")
    lines.append("Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞")
    lines.append("")
    return lines


def ticker_evening(
    snapshot: Dict[str, Any],
    morning: Optional[Dict[str, Any]] = None,
    activity: Optional[List[Dict[str, Any]]] = None,
    setup_status: Optional[Dict[str, Any]] = None,
    gex: Optional[float] = None,
    gex_change: Optional[float] = None,
    key_level_status: Optional[str] = None,
    event_dates: Optional[List[Dict[str, Any]]] = None,
) -> str:
    """单个标的的晚报区块（Scorecard + 明细，不含标题/市场/日历/提醒）。"""
    ticker = snapshot.get("ticker", "?")
    lines: List[str] = [ticker_heading(ticker)]
    lines += _scorecard(morning, snapshot, key_level_status)
    lines += _options_block(snapshot)
    if setup_status:
        spread = _vix_spread_line(snapshot)
        if spread:
            lines.append(spread)
    lines += _structure_block(snapshot, gex=gex, gex_change=gex_change, prev_snapshot=morning)
    lines += _structure_interpretation(snapshot)
    lines += _activity_block(activity)
    lines += _forward_block(snapshot)
    lines += _event_differential_lines(snapshot, event_dates)
    dq_line = _data_quality_line(snapshot)
    if dq_line:
        lines.append(dq_line)
    lines += _setup_block(setup_status, _vol_env(snapshot))
    lines.append("")
    lines.append(f"数据溯源：完整表见附录 / thesis / analytics/daily/{snapshot.get('created_at', '')[:10]}/{ticker}_evening.json")
    return "\n".join(lines)


def render_evening(
    snapshot: Dict[str, Any],
    morning: Optional[Dict[str, Any]] = None,
    activity: Optional[List[Dict[str, Any]]] = None,
    setup_status: Optional[Dict[str, Any]] = None,
    gex: Optional[float] = None,
    gex_change: Optional[float] = None,
    key_level_status: Optional[str] = None,
    reminders: Optional[List[str]] = None,
    calendar: Optional[List[str]] = None,
    market: Optional[Dict[str, Any]] = None,
    event_dates: Optional[List[Dict[str, Any]]] = None,
) -> str:
    date = snapshot.get("created_at", "")[:10]
    lines = [f"# 期权晚报 {date}", ""]
    if market:
        snap_ve = (snapshot.get("context") or {}).get("vol_environment")
        if isinstance(snap_ve, dict):
            market = {**market, "vol_environment": snap_ve}
        lines += market_block(market)
    if calendar:
        lines += calendar_block(calendar)
    from report.highlight import build_highlights, highlights_section

    hl_items = build_highlights(snapshot, activity=activity, prev=morning, event_dates=event_dates)
    lines += highlights_section(hl_items)
    if reminders:
        lines += [r for r in reminders if r]
        lines.append("")
    lines.append(
        ticker_evening(
            snapshot, morning, activity, setup_status, gex, gex_change,
            key_level_status, event_dates,
        )
    )
    return "\n".join(lines)
