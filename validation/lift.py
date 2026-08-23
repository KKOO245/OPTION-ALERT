# -*- coding: utf-8 -*-
"""Lift 计算与展示（百分点）。"""

from __future__ import annotations

from validation.confidence import format_rate


def lift_pp(conditional: float, base: float) -> float:
    return (conditional - base) * 100


def evidence_line(rate_data: dict, base_data: dict, label: str) -> str:
    """历史证据行：n / 独立Episode / Base Rate / Lift / CI / 数据状态。"""
    n = rate_data.get("n", 0)
    k = rate_data.get("confirmed", 0)
    cond_str = format_rate(k, n)
    base_str = (
        f"{base_data['rate']*100:.1f}%" if base_data.get("rate") is not None else "N/A"
    )
    if base_data.get("rate") is not None and n:
        lift = lift_pp(rate_data["rate"], base_data["rate"])
        lift_str = f"{lift:+.1f}pp"
    else:
        lift_str = "N/A"
    return (
        f"{label}: 条件率 {cond_str} | Base Rate {base_str} | Lift {lift_str} "
        f"| 数据状态: {rate_data.get('data_status', 'N/A')}"
    )
