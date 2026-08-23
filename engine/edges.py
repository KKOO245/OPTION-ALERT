# -*- coding: utf-8 -*-
"""证据融合（Evidence Fusion）—— v10.1c。

纪律：
  - Direction 只含 Trend + RS + Price Structure；Confirmation 绝不进入 Direction。
  - 内部一律 raw_component + calibrated:false，不合成任何加权分数。
  - Volatility 六分量归三组（Level/Spread/Momentum），组间禁止加总。
  - Pricing Proxy 用历史百分位；历史不足 → INSUFFICIENT_DATA。
  - 快照里没有的字段（如 RV）一律 UNKNOWN，不猜数。
"""

from __future__ import annotations

import statistics
from typing import Any, Dict, List, Optional

EVIDENCE = ("LOW", "MEDIUM", "HIGH", "N/A")


def _evidence(present: bool, sufficient: bool = True) -> str:
    if not present:
        return "N/A"
    return "MEDIUM" if sufficient else "LOW"


def _rs_state(raw: Any) -> str:
    if raw is None:
        return "UNKNOWN"
    s = str(raw).upper()
    if s in ("WEAK", "STRONG", "NEUTRAL"):
        return s
    if s in ("UNDERPERFORM", "LAGGARD"):
        return "WEAK"
    if s in ("OUTPERFORM", "LEADER"):
        return "STRONG"
    return "NEUTRAL"


def _location_state(loc: Any) -> str:
    if loc is None:
        return "UNKNOWN"
    if loc == "near_put_concentration":
        return "AT_TRIGGER"
    if loc == "near_call_concentration":
        return "AT_TRIGGER"
    if loc == "below_flip":
        return "BELOW_TRIGGER"
    if loc == "above_flip":
        return "ABOVE_TRIGGER"
    if loc == "between":
        return "BETWEEN"
    return "UNKNOWN"


def direction_components(snapshot: Dict[str, Any]) -> Dict[str, Any]:
    momentum = snapshot.get("momentum") or {}
    regime = snapshot.get("regime") or {}
    location = snapshot.get("location") or {}
    context = snapshot.get("context") or {}

    trend_raw = momentum.get("price_momentum")
    trend_state = regime.get("trend")
    if trend_state not in ("UP", "DOWN", "RANGE"):
        trend_state = "UNKNOWN"

    rs_raw = context.get("sector_relative")
    rs_state = _rs_state(rs_raw)

    loc_raw = location.get("price_location")
    loc_state = _location_state(loc_raw)

    trend = {
        "raw_component": trend_raw,
        "state": trend_state,
        "evidence": _evidence(trend_state != "UNKNOWN" and trend_raw is not None),
        "layer": "DERIVED",
    }
    rs = {
        "raw_component": rs_raw,
        "state": rs_state,
        "evidence": _evidence(rs_state != "UNKNOWN"),
        "layer": "DERIVED",
    }
    ps = {
        "raw_component": loc_raw,
        "state": loc_state,
        "evidence": _evidence(loc_state != "UNKNOWN"),
        "layer": "MODEL",
    }
    synthesis = _synthesize_direction([trend, rs, ps])
    return {"trend": trend, "relative_strength": rs, "price_structure": ps, "synthesis": synthesis}


def _synthesize_direction(components: List[Dict[str, Any]]) -> Dict[str, Any]:
    bearish = bullish = neutral = 0
    known = 0
    for c in components:
        st = c["state"]
        if st in ("DOWN", "WEAK", "BELOW_TRIGGER"):
            bearish += 1
            known += 1
        elif st in ("UP", "STRONG", "ABOVE_TRIGGER"):
            bullish += 1
            known += 1
        elif st in ("RANGE", "NEUTRAL", "BETWEEN", "AT_TRIGGER"):
            neutral += 1
            known += 1
    if known == 0:
        state, agreement, evidence = "UNKNOWN", "N/A", "N/A"
    else:
        if bearish > bullish:
            state = "BEARISH"
        elif bullish > bearish:
            state = "BULLISH"
        else:
            state = "NEUTRAL"
        non_neutral = bearish + bullish
        if non_neutral == 0:
            agreement = "N/A"
        elif non_neutral == known or (bearish == 0) != (bullish == 0):
            agreement = "STRONG" if non_neutral == known and (bearish == 0 or bullish == 0) else "PARTIAL"
        else:
            agreement = "WEAK"
        if agreement == "STRONG" and known == len(components):
            evidence = "MEDIUM"
        elif known >= 2:
            evidence = "LOW"
        else:
            evidence = "N/A"
    return {"state": state, "evidence": evidence, "agreement": agreement, "calibrated": False}


def volatility_components(snapshot: Dict[str, Any]) -> Dict[str, Any]:
    momentum = snapshot.get("momentum") or {}
    iv_level = momentum.get("iv_level")
    iv_momentum = momentum.get("iv_momentum") or momentum.get("iv_momentum_1d")
    term = momentum.get("term_structure_momentum")
    rv_level = None  # 快照当前不含 RV（P1 数据层补充），诚实标 UNKNOWN
    iv_rv_spread = None

    level = {
        "iv_level": iv_level,
        "rv_level": rv_level,
        "evidence": _evidence(iv_level is not None),
    }
    spread = {
        "iv_rv_spread": iv_rv_spread,
        "evidence": "N/A",
        "note": "快照未含 RV，待 P1 数据层补充",
    }
    momentum_group = {
        "iv_momentum": iv_momentum,
        "rv_momentum": None,
        "term_structure": term,
        "evidence": _evidence(iv_momentum is not None or term is not None),
    }
    if iv_level == "HIGH" or (isinstance(iv_momentum, (int, float)) and iv_momentum >= 1.0):
        state = "ELEVATED"
    elif iv_level == "LOW" or (isinstance(iv_momentum, (int, float)) and iv_momentum <= -1.0):
        state = "DEPRESSED"
    elif iv_level in ("NORMAL", "HIGH", "LOW") or iv_momentum is not None:
        state = "NORMAL"
    else:
        state = "UNKNOWN"
    return {
        "level": level,
        "spread": spread,
        "momentum": momentum_group,
        "state": state,
        "evidence": _evidence(state != "UNKNOWN"),
        "calibrated": False,
    }


def pricing_proxy(
    iv: Optional[float],
    rv_series: Optional[List[float]] = None,
    iv_series: Optional[List[float]] = None,
    percentile_lo: float = 20.0,
    percentile_hi: float = 80.0,
) -> Dict[str, Any]:
    """Pricing Proxy：IV − 同期限 RV spread 的历史百分位分类。

    历史 <20 期 → INSUFFICIENT_DATA（不硬给 Fair）。
    - 提供 iv_series 时：计算 (iv_i − rv_i) 的 spread 序列，取当前 spread 的经验百分位。
    - 仅提供 rv_series 时：退化为 "IV 在历史 RV 分布中的百分位" 代理（percentile_basis=RV_PROXY），
      并如实标注，不得声称是 spread 百分位。
    """
    if iv is None or not rv_series:
        return {
            "value_pp": None,
            "n_history": len(rv_series or []),
            "percentile": None,
            "percentile_basis": None,
            "classification": "INSUFFICIENT_DATA",
            "horizon_matched": False,
            "layer": "DERIVED",
            "calibrated": False,
        }
    vals = [float(v) for v in rv_series if v is not None]
    if len(vals) < 20:
        return {
            "value_pp": None,
            "n_history": len(vals),
            "percentile": None,
            "percentile_basis": None,
            "classification": "INSUFFICIENT_DATA",
            "horizon_matched": True,
            "layer": "DERIVED",
            "calibrated": False,
        }
    iv = float(iv)
    mean_rv = statistics.mean(vals)
    spread_pp = (iv - mean_rv) * 100.0
    iv_vals = [float(x) for x in (iv_series or []) if x is not None]
    if len(iv_vals) >= 20:
        spreads = [i - r for i, r in zip(iv_vals, vals) if r is not None]
        spreads = [s for s in spreads if s is not None]
        if len(spreads) >= 20:
            percentile = sum(1 for s in spreads if s <= spread_pp) / len(spreads) * 100.0
            basis = "SPREAD_PERCENTILE"
        else:
            percentile = sum(1 for v in vals if v <= iv) / len(vals) * 100.0
            basis = "RV_PROXY"
    else:
        percentile = sum(1 for v in vals if v <= iv) / len(vals) * 100.0
        basis = "RV_PROXY"
    if percentile >= percentile_hi:
        classification = "EXPENSIVE"
    elif percentile <= percentile_lo:
        classification = "CHEAP"
    else:
        classification = "FAIR"
    return {
        "value_pp": round(spread_pp, 2),
        "n_history": len(vals),
        "percentile": round(percentile, 1),
        "percentile_basis": basis,
        "classification": classification,
        "horizon_matched": True,
        "layer": "DERIVED",
        "calibrated": False,
    }


def mechanism_confidence(snapshot: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "level": "LOW",
        "scenario_note": (
            "Scenario A（客户买开/做市商卖开）与 Scenario B（客户卖开/做市商买开）"
            "方向相反；实际对冲流量不可观测"
        ),
        "layer": "MODEL",
        "calibrated": False,
    }
