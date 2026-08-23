# -*- coding: utf-8 -*-
"""Decision Gate：规则树（非矩阵查表）+ 资格审核 + reason_code + NOT_RENDERED。

v10.1c 纪律：
  - Gate 不创造 Alpha，只过滤已验证的 Setup（target-conditioned evidence）。
  - 未达资格 → NOT_RENDERED（WATCH 也是一种决策，未达资格不产生）。
  - Mechanism 不作为 Direction 硬条件（允许 Bearish + Mechanism Unknown）。
  - 输出分三层：Market Thesis / Volatility-Pricing Thesis / Tradeability。
"""

from __future__ import annotations

from typing import Any, Dict, Optional

REASON_CODES = (
    "INSUFFICIENT_EVIDENCE",
    "MISSING_CONFIRMATION",
    "PRICING_EXPENSIVE",
    "MECHANISM_UNCERTAIN",
    "LIQUIDITY",
    "SAMPLE_INSUFFICIENT",
    "TARGET_PENDING",
    "TRIGGER_INACTIVE",
    "DATA_INSUFFICIENT",
)


def qualification(
    n_episodes: int,
    n_regimes: int = 0,
    oos_lift_pp: Optional[float] = None,
    ci_lower: Optional[float] = None,
    oos_available: bool = False,
    polluted: bool = False,
    thresholds: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    t = thresholds or {}
    core_n = t.get("sample_gates", {}).get("core_n", 20)
    validated_n = t.get("sample_gates", {}).get("validated_n", 50)
    regime_min = t.get("sample_gates", {}).get("regime_min_count_for_oos", 2)
    lift_min = t.get("oos_lift_min_pp", 5)

    reasons = []
    if polluted:
        reasons.append("规则污染")
    if n_episodes < core_n:
        reasons.append(f"N={n_episodes} < {core_n}")
    if n_regimes < regime_min:
        reasons.append(f"regimes={n_regimes} < {regime_min}")
    if oos_lift_pp is None or oos_lift_pp < lift_min:
        reasons.append(f"OOS Lift {oos_lift_pp if oos_lift_pp is not None else 'N/A'} < +{lift_min}pp")
    if ci_lower is None or ci_lower <= 0:
        reasons.append(f"95% CI 下界 {ci_lower if ci_lower is not None else 'N/A'} 未 > 0")
    if not oos_available:
        reasons.append("OOS 不可计算（规则冻结后数据不足）")

    if n_episodes >= validated_n and not reasons:
        level = "VALIDATED"
    elif n_episodes >= core_n and not reasons:
        level = "CORE"
    elif n_episodes >= 10 and n_regimes >= regime_min and oos_available:
        level = "CANDIDATE"
    else:
        level = "EXPERIMENTAL"

    return {
        "level": level,
        "eligible": level in ("CORE", "VALIDATED"),
        "reasons": reasons,
        "n_episodes": n_episodes,
        "oos_lift_pp": oos_lift_pp,
        "ci_lower": ci_lower,
    }


def gate_pipeline(
    *,
    setup_trigger_met: bool,
    qual: Dict[str, Any],
    direction: Dict[str, Any],
    volatility: Dict[str, Any],
    pricing: Dict[str, Any],
    mechanism: Dict[str, Any],
    confirmation: Dict[str, Any],
    data_ok: bool = True,
) -> Dict[str, Any]:
    """规则树求值。confirmation = {satisfied, required}。"""
    layers = {
        "market_thesis": direction.get("synthesis", {}).get("state", "UNKNOWN"),
        "volatility_pricing": {
            "volatility": volatility.get("state", "UNKNOWN"),
            "pricing": pricing.get("classification", "UNKNOWN"),
        },
        "tradeability": {"yes": None, "reason": None},
    }

    def result(status, decision, reason, display):
        return {
            "gate_status": status,
            "decision": decision,
            "reason_code": reason,
            "layers": layers,
            "display": display,
        }

    # 1. 数据是否足够
    if not data_ok:
        layers["tradeability"] = {"yes": False, "reason": "DATA_INSUFFICIENT"}
        return result("NOT_RENDERED", "NOT_RENDERED", "DATA_INSUFFICIENT", "数据不足")
    # 2. 样本资格
    if not qual["eligible"]:
        layers["tradeability"] = {"yes": False, "reason": "SAMPLE_INSUFFICIENT"}
        return result(
            "NOT_RENDERED",
            "NOT_RENDERED",
            "SAMPLE_INSUFFICIENT",
            f"实验中，样本不足（N={qual['n_episodes']}）",
        )
    # 3. Setup 触发
    if not setup_trigger_met:
        layers["tradeability"] = {"yes": False, "reason": "TRIGGER_INACTIVE"}
        return result("ELIGIBLE", "WATCH", "TRIGGER_INACTIVE", "WATCH — Setup 未触发")
    # 4. 方向证据
    syn = direction.get("synthesis", {})
    if syn.get("state") == "UNKNOWN" or syn.get("evidence") in ("N/A", None):
        layers["tradeability"] = {"yes": False, "reason": "INSUFFICIENT_EVIDENCE"}
        return result("ELIGIBLE", "WATCH", "INSUFFICIENT_EVIDENCE", "WATCH — 方向证据不足")
    # 5. 定价可接受性（方向性交易视角）
    if pricing.get("classification") == "EXPENSIVE" and syn.get("state") in ("BULLISH", "BEARISH"):
        layers["tradeability"] = {"yes": False, "reason": "PRICING_EXPENSIVE"}
        return result("ELIGIBLE", "NO_TRADE", "PRICING_EXPENSIVE", "NO_TRADE — IV 偏贵（Pricing Proxy）")
    # 6. Confirmation 充分性
    required = confirmation.get("required", 0)
    satisfied = confirmation.get("satisfied", 0)
    if required and satisfied == 0:
        layers["tradeability"] = {"yes": False, "reason": "MISSING_CONFIRMATION"}
        return result("ELIGIBLE", "WATCH", "MISSING_CONFIRMATION", "WATCH — 缺 Confirmation")
    # 7. Mechanism：不作为硬条件，只标注
    mechanism_unconfirmed = mechanism.get("level") in ("LOW", None)
    # 8. 决策
    if syn.get("state") == "BULLISH":
        decision = "DIRECTIONAL_BULL"
    elif syn.get("state") == "BEARISH":
        decision = "DIRECTIONAL_BEAR"
    elif volatility.get("state") == "ELEVATED" and syn.get("state") == "NEUTRAL":
        decision = "VOLATILITY_SETUP"
    else:
        decision = "WATCH"
    layers["tradeability"] = {
        "yes": decision not in ("WATCH",),
        "reason": None,
        "mechanism_unconfirmed": mechanism_unconfirmed,
    }
    display = f"{decision}" + ("（mechanism unconfirmed）" if mechanism_unconfirmed else "")
    return result("ELIGIBLE", decision, None, display)
