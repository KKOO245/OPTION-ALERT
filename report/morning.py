# -*- coding: utf-8 -*-
"""晨报渲染（P0.1 简化版：消费快照 + 事件日志，只展示真实数据）。"""

from __future__ import annotations

from typing import Any, Dict, List


def _val(x: Any, suffix: str = "") -> str:
    if x is None:
        return "N/A"
    return f"{x}{suffix}"


def _confirmation_mark(met) -> str:
    if met is True:
        return "Y"
    if met is False:
        return "N"
    return "?"


def render_morning(snapshot: Dict[str, Any], read_model: Dict[str, Any], setups=None) -> str:
    events = read_model.get("events", [])
    lines: List[str] = []
    lines.append(f"# 晨报 {snapshot['created_at'][:10]}（{snapshot['ticker']}）")
    lines.append("")
    lines.append(
        f"> 数据纪律：本报告所有数字来自快照（{snapshot.get('source','?')} @ "
        f"{snapshot['created_at']}）；缺失字段一律标注 INSUFFICIENT_DATA，绝不编造。"
    )
    lines.append("")

    ctx = snapshot.get("context") or {}
    lines.append("## 市场背景")
    lines.append(
        f"- SPY: {_val(ctx.get('spy_return'), '%')} | QQQ: {_val(ctx.get('qqq_return'), '%')} "
        f"| 板块相对强度: {_val(ctx.get('sector_relative'))} | VIX: {_val(ctx.get('vix'))}"
    )
    lines.append("")

    lines.append(f"## {snapshot['ticker']}")
    regime = snapshot.get("regime") or {}
    location = snapshot.get("location") or {}
    lines.append("三行结论：")
    lines.append(f"- 价格状态: {_val(regime.get('trend'))} / spot={snapshot['spot']} / "
                 f"location={_val(location.get('price_location'))}")
    decision_events = [e for e in events if e.get("ticker") == snapshot["ticker"]]
    if decision_events:
        dec = decision_events[0]
        lines.append(f"- 决策: {dec['decision']}（P0.1 Gate 未实现，仅机械记录）")
        walls = []
        if location.get("put_wall"):
            walls.append(f"Put Wall={location['put_wall']}")
        if location.get("call_wall"):
            walls.append(f"Call Wall={location['call_wall']}")
        if location.get("flip_levels"):
            walls.append(f"Flip={location['flip_levels']}")
        lines.append(f"- 关键价位: {', '.join(walls) if walls else 'N/A（快照缺关键价位字段）'}")
    else:
        lines.append("- 决策: 今日无 Setup 触发（WATCH）")
        lines.append("- 关键价位: N/A")
    lines.append("")

    lines.append("### Setup 触发明细")
    if not decision_events:
        lines.append("- 无（今日机械检查所有 Setup，均未满足 Core 触发条件）")
    for ev in decision_events:
        lines.append(f"- Setup {ev['setup_id']}（{ev['setup_version']}, rule={ev['trigger_rule_version']}）")
        pt = ev["primary_target"]
        lines.append(f"  - Target: {pt['metric']} {pt['direction']} {pt['threshold']} @ {pt['horizon']} "
                     f"({pt['evaluation_rule']})")
        confs = ev.get("confirmation_status", [])
        ok = sum(1 for c in confs if c.get("met") is True)
        total = len(confs)
        lines.append(f"  - Confirmation: {ok}/{total} "
                     + " ".join(f"{c['name']}{_confirmation_mark(c.get('met'))}" for c in confs))
        su = ev.get("data_sufficiency") or {}
        missing = [k for k, v in su.items() if v == "INSUFFICIENT_DATA"]
        lines.append(f"  - 数据充分性: {len(missing)} 项缺失"
                     + (f"（{', '.join(missing[:5])}{'...' if len(missing) > 5 else ''}）" if missing else ""))
    lines.append("")
    lines.append("---")
    lines.append("*P0.1 事件引擎输出：完整原始记录见 thesis/events.jsonl（哈希链保护）。*")
    return "\n".join(lines)
