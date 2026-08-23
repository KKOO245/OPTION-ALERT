# -*- coding: utf-8 -*-
"""晚报渲染（P0.1 简化版：Thesis Scorecard + 事件状态）。"""

from __future__ import annotations

from typing import Any, Dict, List


def render_evening(snapshot: Dict[str, Any], read_model: Dict[str, Any], evidence: List[str] = None) -> str:
    events = read_model.get("events", [])
    lines: List[str] = []
    lines.append(f"# 晚报 {snapshot['created_at'][:10]}（{snapshot['ticker']}）")
    lines.append("")
    lines.append("## Thesis Scorecard")
    lines.append("")
    lines.append("| event_id | Setup | Trigger | Target 状态 | Outcome | Episode |")
    lines.append("|---|---|---|---|---|---|")
    for ev in sorted(events, key=lambda e: e["created_at"]):
        lines.append(
            f"| {ev['event_id']} | {ev['setup_id']} | "
            f"{'MET' if ev.get('setup_trigger_met') else 'NOT MET'} | "
            f"{ev.get('target_status','?')} | {ev.get('outcome','?')} | "
            f"{ev.get('episode_id') or '-'} |"
        )
    lines.append("")
    lines.append("### 历史证据")
    if evidence:
        lines.extend(f"- {e}" for e in evidence)
    else:
        lines.append("- 尚无已评价 Episode；Base Rate / Lift / CI 均为 N/A（数据积累中）")
    lines.append("")
    lines.append("### 事件状态")
    for ev in sorted(events, key=lambda e: e["created_at"]):
        lc = ev.get("lifecycle", "OPEN")
        oc = ev.get("outcome", "PENDING")
        es = ev.get("evaluation_status", "EVALUABLE")
        lines.append(f"- `{lc} / {oc} / {es}` {ev['event_id']} "
                     f"(revisions={len(ev.get('outcome_revisions', []))})")
    lines.append("")
    lines.append("---")
    lines.append("*P0.1 事件引擎输出：Outcome 只以 revision 追加，不修改原始事件。*")
    return "\n".join(lines)
