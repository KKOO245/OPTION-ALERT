# -*- coding: utf-8 -*-
"""置信区间与证据等级（Wilson 95%，禁止正态近似）。"""

from __future__ import annotations

import math


Z_TABLE = {0.90: 1.6449, 0.95: 1.959964, 0.99: 2.575829}


def wilson_ci(k: int, n: int, level: float = 0.95):
    """Wilson score interval。n=0 返回 None。"""
    if n <= 0:
        return None
    z = Z_TABLE.get(level, 1.959964)
    p = k / n
    denom = 1 + z * z / n
    center = (p + z * z / (2 * n)) / denom
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denom
    return (max(0.0, center - half), min(1.0, center + half))


def label_for_n(n: int, prelim: int, developing: int, established: int) -> str:
    """数据充分性标签（N/A / PRELIMINARY / DEVELOPING / ESTABLISHED）。"""
    if n < prelim:
        return "N/A"
    if n < developing:
        return "PRELIMINARY"
    if n < established:
        return "DEVELOPING"
    return "ESTABLISHED"


def format_rate(k: int, n: int, level: float = 0.95) -> str:
    if n <= 0:
        return "N/A (n=0)"
    ci = wilson_ci(k, n, level)
    pct = k / n * 100
    return f"{pct:.1f}% (n={n}, 95% CI: {ci[0]*100:.1f}%-{ci[1]*100:.1f}%)"
