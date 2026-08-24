# -*- coding: utf-8 -*-
"""晚报渲染（P0.3 规格 v1）：Thesis Scorecard + 关键位状态 + Target 状态 + 每标的。"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from report.format import fmt
from report.morning import (
    _activity_block,
    _options_block,
    _setup_block,
    _structure_block,
    _structure_interpretation,
    _trading_gap,
    calendar_block,
    market_block,
    ticker_heading,
)


def _scorecard(morning: Optional[Dict[str, Any]], evening: Dict[str, Any], key_level_status: Optional[str]) -> List[str]:
    ticker = evening.get("ticker", "?")
    lines = ["📋 Thesis Scorecard（今晨条件 vs 收盘实况，只打事实勾）"]
    if morning is None:
        lines.append(f"{ticker}: 晨报缺失（当日未生成），只报收盘事实")
    else:
        gap = _trading_gap(morning.get("created_at", "")[:10], evening.get("created_at", "")[:10])
        if gap >= 1:
            lines.append(f"{ticker}: ⚠️ 晨报为 {gap} 个交易日前（标的可能停更），仅作收盘事实对照")
        m_spot = morning.get("spot")
        e_spot = evening.get("spot")
        if m_spot and e_spot:
            chg = (e_spot / m_spot - 1.0) * 100
            lines.append(f"{ticker}: 今晨 {fmt(m_spot, 2)} → 收盘 {fmt(e_spot, 2)}（{chg:+.1f}%）")
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
) -> str:
    """单个标的的晚报区块（Scorecard + 明细，不含标题/市场/日历/提醒）。"""
    ticker = snapshot.get("ticker", "?")
    lines: List[str] = []
    lines += _scorecard(morning, snapshot, key_level_status)
    lines.append(ticker_heading(ticker))
    lines += _options_block(snapshot)
    lines += _structure_block(snapshot, gex=gex, gex_change=gex_change)
    lines += _structure_interpretation(snapshot)
    lines += _activity_block(activity)
    lines += _setup_block(setup_status)
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
) -> str:
    date = snapshot.get("created_at", "")[:10]
    lines = [f"# 期权晚报 {date}", ""]
    if market:
        lines += market_block(market)
    if calendar:
        lines += calendar_block(calendar)
    if reminders:
        lines += [r for r in reminders if r]
        lines.append("")
    lines.append(ticker_evening(snapshot, morning, activity, setup_status, gex, gex_change, key_level_status))
    return "\n".join(lines)
