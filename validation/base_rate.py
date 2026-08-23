# -*- coding: utf-8 -*-
"""Base Rate 三级：无条件 → regime 调整 → 条件 Setup。

P0.1 只做可计算的部分；缺历史数据一律返回 N/A，绝不编数。
注意：无条件 Base Rate 用重叠窗口计算，仅作初步参考；
      正式版本按窗口结束日打分或按起始日聚类（见企划书验证层）。
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional


def unconditional_base_rate(
    prices: List[Dict[str, Any]], direction: str, threshold: float, horizon_days: int
) -> Dict[str, Any]:
    rows = sorted(prices, key=lambda r: r["date"][:10])
    if len(rows) <= horizon_days:
        return {"rate": None, "n": 0, "hits": 0, "note": "历史窗口不足"}
    hits = 0
    n = 0
    for i in range(len(rows) - horizon_days):
        a = float(rows[i]["close"])
        b = float(rows[i + horizon_days]["close"])
        if a == 0:
            continue
        ret = b / a - 1.0
        n += 1
        if _hit(direction, threshold, ret):
            hits += 1
    return {"rate": hits / n if n else None, "n": n, "hits": hits, "note": "重叠窗口" if n else ""}


def regime_adjusted_base_rate(
    history: List[Dict[str, Any]], direction: str, threshold: float, horizon_days: int,
    regime_state: str,
) -> Dict[str, Any]:
    """history 行需带 regime 字段（如 regime.gamma）。按起点 regime 过滤。"""
    rows = sorted(history, key=lambda r: r["date"][:10])
    hits = n = 0
    for i in range(len(rows) - horizon_days):
        if rows[i].get("regime") != regime_state:
            continue
        a = float(rows[i]["close"])
        b = float(rows[i + horizon_days]["close"])
        if a == 0:
            continue
        ret = b / a - 1.0
        n += 1
        if _hit(direction, threshold, ret):
            hits += 1
    return {"rate": hits / n if n else None, "n": n, "hits": hits}


def conditional_setup_rate(episodes: List[Dict[str, Any]]) -> Dict[str, Any]:
    """用独立 Episode 的代表事件 outcome（CONFIRMED/REJECTED）计算。
    EXPIRED / INVALIDATED / PENDING 不计入分母，单独列出。"""
    confirmed = rejected = excluded = 0
    excluded_kinds: Dict[str, int] = {}
    for ep in episodes:
        o = ep.get("representative_outcome", "PENDING")
        if o == "CONFIRMED":
            confirmed += 1
        elif o == "REJECTED":
            rejected += 1
        else:
            excluded += 1
            excluded_kinds[o] = excluded_kinds.get(o, 0) + 1
    n = confirmed + rejected
    return {
        "rate": confirmed / n if n else None,
        "n": n,
        "confirmed": confirmed,
        "rejected": rejected,
        "excluded": excluded,
        "excluded_kinds": excluded_kinds,
    }


def freeze_partition(episodes: List[Dict[str, Any]], freeze_date: str) -> tuple:
    """按规则冻结日期划分 Episode。

    冻结前积累的数据只用于生成假设；OOS 验证只用冻结后数据。
    返回 (pre_freeze, post_freeze)。
    """
    pre, post = [], []
    for ep in episodes:
        start = (ep.get("start_ts") or "")[:10]
        if start and start < freeze_date:
            pre.append(ep)
        else:
            post.append(ep)
    return pre, post


def _hit(direction: str, threshold: float, value: float) -> bool:
    if direction == ">=":
        return value >= threshold
    if direction == "<=":
        return value <= threshold
    if direction == ">":
        return value > threshold
    if direction == "<":
        return value < threshold
    return False
