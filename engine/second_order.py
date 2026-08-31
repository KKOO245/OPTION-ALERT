# -*- coding: utf-8 -*-
"""二阶希腊字母（second_order_v1）：vanna / charm + 门控聚合。

口径（与 regime_map 一致：BS 欧式近似、q=0、r=0.05）：
  - 合约符号沿用 Model A（call +, put −）；
  - vanna 门控：|当日 IV 变动| ≥ 阈值（默认 0.5 vol pts），否则 net_vanna 显示 null（不解读）；
  - charm 门控：最近期限 DTE ≤ 阈值（默认 5），否则 net_charm 显示 null；
  - 结果属研究采集层（p3），不进报告/评分，待验证。
"""

from __future__ import annotations

import math
from datetime import date
from typing import Any, Dict, List, Optional

RISK_FREE_RATE = 0.05


def _d1(S: float, K: float, T: float, sigma: float, r: float) -> Optional[float]:
    if S <= 0 or K <= 0 or sigma <= 0 or T <= 0:
        return None
    return (math.log(S / K) + (r + sigma * sigma / 2.0) * T) / (sigma * math.sqrt(T))


def bs_vanna(S: float, K: float, T: float, sigma: float, r: float = RISK_FREE_RATE) -> Optional[float]:
    d1 = _d1(S, K, T, sigma, r)
    if d1 is None:
        return None
    d2 = d1 - sigma * math.sqrt(T)
    phi = math.exp(-0.5 * d1 * d1) / math.sqrt(2.0 * math.pi)
    # 标准 BS vanna = ∂Δ/∂σ = −φ(d1)·d2/σ（与 src.metrics.vanna_charm 同口径；
    # 旧实现漏了负号，导致 p3 层 net_vanna 与 metrics/oi_history 符号相反）
    return -phi * d2 / sigma


def bs_charm(S: float, K: float, T: float, sigma: float, r: float = RISK_FREE_RATE) -> Optional[float]:
    d1 = _d1(S, K, T, sigma, r)
    if d1 is None:
        return None
    phi = math.exp(-0.5 * d1 * d1) / math.sqrt(2.0 * math.pi)
    # 标准 BS charm = ∂Δ/∂τ = φ(d1)·[(r+σ²/2)/(2σ√τ) − ln(S/K)/(2σ·τ^1.5)]
    # （与 src.metrics.vanna_charm 同口径；旧实现用了非标准公式）
    return phi * (
        (r + sigma * sigma / 2.0) / (2.0 * sigma * math.sqrt(T))
        - math.log(S / K) / (2.0 * sigma * T ** 1.5)
    )


def _dte(contract: Dict[str, Any], as_of: Optional[date]) -> Optional[int]:
    dte = contract.get("dte")
    if dte is not None:
        try:
            return max(1, int(dte))
        except (TypeError, ValueError):
            return None
    exp = contract.get("expiration")
    if exp and as_of:
        try:
            return max(1, (date.fromisoformat(str(exp)[:10]) - as_of).days)
        except ValueError:
            return None
    return None


def second_order_aggregate(
    contracts: Optional[List[Dict[str, Any]]],
    spot: Optional[float],
    as_of: Optional[date] = None,
    iv_move_pp: Optional[float] = None,
    vanna_gate_vol_pp: float = 0.5,
    charm_gate_max_dte: int = 5,
) -> Dict[str, Any]:
    """对全链有效合约聚合 dealer-signed vanna/charm；返回门控状态。"""
    net_vanna = 0.0
    net_charm = 0.0
    n_used = 0
    min_dte = None
    for c in contracts or []:
        typ = str(c.get("type", "")).lower()
        if typ not in ("call", "put"):
            continue
        iv = c.get("iv")
        oi = c.get("open_interest", c.get("oi"))
        strike = c.get("strike")
        dte = _dte(c, as_of)
        try:
            sigma, oi, strike = float(iv), float(oi), float(strike)
            t = float(dte) / 365.0
        except (TypeError, ValueError):
            continue
        if sigma <= 0 or oi <= 0 or strike <= 0 or t <= 0 or spot is None or spot <= 0:
            continue
        v = bs_vanna(float(spot), strike, t, sigma)
        ch = bs_charm(float(spot), strike, t, sigma)
        if v is None or ch is None:
            continue
        sign = 1.0 if typ == "call" else -1.0
        net_vanna += sign * v * oi * 100.0
        net_charm += sign * ch * oi * 100.0
        n_used += 1
        if min_dte is None or dte < min_dte:
            min_dte = dte

    vanna_gate = None
    if iv_move_pp is not None:
        vanna_gate = abs(iv_move_pp) >= vanna_gate_vol_pp
    charm_gate = (min_dte is not None and min_dte <= charm_gate_max_dte) if min_dte is not None else None
    return {
        "schema_version": "second_order_v1",
        "net_vanna": round(net_vanna, 0) if n_used else None,
        "net_charm": round(net_charm, 0) if n_used else None,
        "n_used": n_used,
        "min_dte": min_dte,
        "vanna_gate": vanna_gate,
        "charm_gate": charm_gate,
    }
