# -*- coding: utf-8 -*-
"""全链重定价 Regime Map：模型隐含 GEX 过零点（Model-implied GEX zero-crossing）。

v10.1c 纪律：
  - 结果属于 MODEL 层（依赖 Scenario A/B + sticky-strike IV + BS 欧式近似），
    验证前不进入方向决策；报告展示必须写"≈ 且 Scenario 依赖"。
  - 纯标准库实现 Black-Scholes gamma（与 vollib 公式同源），零运行时依赖。
  - IV 缺失的合约不参与重定价（诚实排除并计数），不猜数。
"""

from __future__ import annotations

import math
from datetime import date
from typing import Any, Dict, List, Optional

RISK_FREE_RATE = 0.05
VOL_SURFACE_MODE = "STICKY_STRIKE"


def _d1(S: float, K: float, T: float, sigma: float, r: float) -> Optional[float]:
    if S <= 0 or K <= 0 or sigma <= 0 or T <= 0:
        return None
    return (math.log(S / K) + (r + sigma * sigma / 2.0) * T) / (sigma * math.sqrt(T))


def bs_gamma(S: float, K: float, T: float, sigma: float, r: float = RISK_FREE_RATE) -> Optional[float]:
    """Black-Scholes gamma（欧式，q=0）。"""
    d1 = _d1(S, K, T, sigma, r)
    if d1 is None:
        return None
    return math.exp(-0.5 * d1 * d1) / (S * sigma * math.sqrt(2.0 * math.pi * T))


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


def _normalize_contracts(contracts: List[Dict[str, Any]], as_of: Optional[date]) -> tuple:
    rows = []
    skipped = 0
    for c in contracts:
        typ = str(c.get("type", "")).lower()
        if typ not in ("call", "put"):
            skipped += 1
            continue
        strike = c.get("strike")
        iv = c.get("iv")
        oi = c.get("open_interest", c.get("oi"))
        dte = _dte(c, as_of)
        if strike is None or iv is None or oi is None:
            skipped += 1
            continue
        try:
            sigma = float(iv)
            oi = float(oi)
            strike = float(strike)
        except (TypeError, ValueError):
            skipped += 1
            continue
        if sigma <= 0 or oi <= 0 or strike <= 0:
            skipped += 1
            continue
        rows.append({
            "type": typ,
            "strike": strike,
            "oi": oi,
            "sigma": sigma,
            "t": dte / 365.0 if dte else None,
        })
    return rows, skipped


def _zero_crossings(net_by_spot: List[Dict[str, Any]]) -> List[float]:
    """零跨规则（paper 1）：精确零点只有左右邻点异号才算 Flip；同号/连续零不算。
    避免"净 GEX 恒为 0（NEUTRAL）"时把每个网格点都报成 Flip。"""
    flips = []
    n = len(net_by_spot)
    for i in range(n - 1):
        a, b = net_by_spot[i], net_by_spot[i + 1]
        na, nb = a["net_gex"], b["net_gex"]
        if na == 0:
            if i > 0:
                prev = net_by_spot[i - 1]["net_gex"]
                if prev * nb < 0:  # 左右异号 → 真翻转
                    flips.append(a["spot"])
            continue
        if na * nb < 0:
            frac = -na / (nb - na)
            flips.append(round(a["spot"] + (b["spot"] - a["spot"]) * frac, 4))
    return sorted({round(f, 4) for f in flips})


def regime_map(
    contracts: List[Dict[str, Any]],
    spot: Optional[float],
    grid_low: float = 0.85,
    grid_high: float = 1.15,
    step: float = 0.0025,
    as_of: Optional[date] = None,
) -> Optional[Dict[str, Any]]:
    if spot is None or spot <= 0:
        return None
    rows, skipped = _normalize_contracts(contracts, as_of)
    if not rows:
        return None

    spots = []
    s = spot * grid_low
    while s <= spot * grid_high + 1e-9:
        spots.append(round(s, 4))
        s += spot * step

    net_by_spot = []
    for S in spots:
        net = 0.0
        for c in rows:
            g = bs_gamma(S, c["strike"], c["t"], c["sigma"])
            if g is None:
                continue
            sign = 1.0 if c["type"] == "call" else -1.0
            net += sign * g * c["oi"] * 100.0 * S
        net_by_spot.append({"spot": S, "net_gex": round(net, 2)})

    flips = _zero_crossings(net_by_spot)
    current = next((p for p in net_by_spot if p["spot"] == round(spot, 4)), None)
    zone = "ZERO"
    current_net = None
    if current is not None:
        current_net = current["net_gex"]
        zone = "NEGATIVE" if current["net_gex"] < 0 else ("POSITIVE" if current["net_gex"] > 0 else "ZERO")

    # Primary Flip = 当前 regime 的边界（符号解析最近，paper 2 口径）：
    #   net GEX > 0 → 向下找最近的零穿越（spot 下方）；net GEX < 0 → 向上找最近的零穿越（spot 上方）
    primary_flip = None
    if flips and current_net is not None:
        if current_net > 0:
            below = [f for f in flips if f < spot]
            primary_flip = max(below) if below else None
        elif current_net < 0:
            above = [f for f in flips if f > spot]
            primary_flip = min(above) if above else None

    negative = [p["spot"] for p in net_by_spot if p["net_gex"] < 0]
    negative_zone = {"low": negative[0], "high": negative[-1]} if negative else None

    return {
        "schema_version": "regime_map_v1",
        "layer": "MODEL",
        "vol_surface_mode": VOL_SURFACE_MODE,
        "assumptions": [
            "Black-Scholes 欧式近似",
            "sticky-strike IV（重定价时 IV 固定）",
            "Scenario 依赖：OI 视为客户仓位；方向不可观测",
            "q=0（无股息近似；高股息个股 gamma 略偏，已知近似）",
        ],
        "spot": spot,
        "grid": {"low": spot * grid_low, "high": spot * grid_high, "step": spot * step, "n_points": len(spots)},
        "n_contracts_used": len(rows),
        "n_contracts_skipped": skipped,
        "flip_levels": flips,
        "primary_flip": primary_flip,
        "primary_rule": "sign_resolved_nearest_v1",
        "net_gex_at_spot": round(current_net, 2) if current_net is not None else None,
        "spot_zone": zone,
        "negative_zone": negative_zone,
        "net_gex_by_spot": net_by_spot,
    }
