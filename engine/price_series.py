# -*- coding: utf-8 -*-
"""从 analytics 历史行生成收盘价序列（供 Outcome 评价使用）。

口径：每个交易日取该日最后一条 session 的价格（晚报优先、早报兜底）；
这等价于"当天可获得的最新价格"，用于 close_to_close 类 Primary Target 评价。
"""

from __future__ import annotations

from typing import Any, Dict, List


def closes_from_analytics(rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    per_day: Dict[str, tuple] = {}
    for r in rows:
        day = r.get("date")
        price = r.get("price")
        if not day or price is None:
            continue
        rank = 1 if r.get("session") == "evening" else 0
        cur = per_day.get(day)
        if cur is None or rank >= cur[0]:
            per_day[day] = (rank, price)
    return [
        {"date": day, "close": float(v[1])}
        for day, v in sorted(per_day.items())
    ]
