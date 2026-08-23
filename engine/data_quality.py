# -*- coding: utf-8 -*-
"""Data Quality 瓶颈维度（v10.1c）。

维度：market_data / options_structure / flow / dealer_mechanism，各 A/B/C。
瓶颈 = 最低等级维度；瓶颈过低 → 禁高置信。
"""

from __future__ import annotations

from typing import Any, Dict


GRADE_RANK = {"A": 0, "B": 1, "C": 2}


def grade_snapshot(snapshot: Dict[str, Any]) -> Dict[str, str]:
    """按快照字段完整度打分（机械规则，不猜数）。"""
    spot = snapshot.get("spot")
    price = snapshot.get("price")
    momentum = snapshot.get("momentum") or {}
    location = snapshot.get("location") or {}
    has_hist_price = price is not None or bool(momentum.get("price_momentum") is not None)

    if spot is not None and has_hist_price:
        market = "A"
    elif spot is not None:
        market = "B"
    else:
        market = "C"

    has_structure = any(
        location.get(k) is not None
        for k in ("call_wall", "put_wall", "flip_levels", "price_location")
    )
    has_iv = momentum.get("iv_level") is not None or momentum.get("iv_rank") is not None
    options = "A" if (has_structure and has_iv) else ("B" if (has_structure or has_iv) else "C")

    flow_fields = [momentum.get(k) for k in ("oi_flow", "volume_ratio")]
    present = sum(1 for v in flow_fields if v is not None)
    flow = "A" if present == 2 else ("B" if present == 1 else "C")

    mechanism = "C"  # 模型估算层，恒为 C

    return {
        "market_data": market,
        "options_structure": options,
        "flow": flow,
        "dealer_mechanism": mechanism,
    }


def bottleneck(grades: Dict[str, str]) -> str:
    """取最低等级（C 最差）。"""
    return max(grades.values(), key=lambda g: GRADE_RANK.get(g, 2))


def bottleneck_low(grades: Dict[str, str]) -> bool:
    """关键数据维度（market/options/flow）是否过低。

    dealer_mechanism 恒为 C（不可观测，设计如此），不参与"过低"判断——
    Mechanism 永不作为方向前提，因此不应让它拖垮整体判断。
    """
    return any(
        grades.get(k) == "C"
        for k in ("market_data", "options_structure", "flow")
    )
