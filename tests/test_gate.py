# -*- coding: utf-8 -*-
from engine.gate import gate_pipeline, qualification


def test_qualification_boundaries():
    q1 = qualification(n_episodes=19, n_regimes=2, oos_lift_pp=6, ci_lower=1, oos_available=True)
    assert q1["level"] == "CANDIDATE" and q1["eligible"] is False

    q2 = qualification(n_episodes=20, n_regimes=2, oos_lift_pp=6, ci_lower=1, oos_available=True)
    assert q2["level"] == "CORE" and q2["eligible"] is True

    q3 = qualification(n_episodes=20, n_regimes=2, oos_lift_pp=3, ci_lower=1, oos_available=True)
    assert q3["eligible"] is False
    assert any("OOS Lift" in r for r in q3["reasons"])


def _base(**kw):
    defaults = {
        "setup_trigger_met": True,
        "qual": qualification(n_episodes=20, n_regimes=2, oos_lift_pp=6, ci_lower=1, oos_available=True),
        "direction": {"synthesis": {"state": "BEARISH", "evidence": "MEDIUM", "agreement": "STRONG"}},
        "volatility": {"state": "NORMAL"},
        "pricing": {"classification": "FAIR"},
        "mechanism": {"level": "LOW"},
        "confirmation": {"satisfied": 1, "required": 4},
        "data_ok": True,
    }
    defaults.update(kw)
    return defaults


def test_not_eligible_not_rendered():
    r = gate_pipeline(**_base(qual=qualification(n_episodes=5)))
    assert r["decision"] == "NOT_RENDERED"
    assert r["reason_code"] == "SAMPLE_INSUFFICIENT"
    assert "样本不足" in r["display"]


def test_trigger_inactive_watch():
    r = gate_pipeline(**_base(setup_trigger_met=False))
    assert r["decision"] == "WATCH"
    assert r["reason_code"] == "TRIGGER_INACTIVE"


def test_expensive_pricing_no_trade():
    r = gate_pipeline(**_base(pricing={"classification": "EXPENSIVE"}))
    assert r["decision"] == "NO_TRADE"
    assert r["reason_code"] == "PRICING_EXPENSIVE"
    assert r["layers"]["tradeability"]["yes"] is False


def test_bearish_allowed_with_mechanism_unknown():
    r = gate_pipeline(**_base())
    assert r["decision"] == "DIRECTIONAL_BEAR"
    assert r["layers"]["tradeability"]["mechanism_unconfirmed"] is True
    assert "mechanism unconfirmed" in r["display"]


def test_insufficient_evidence_watch():
    r = gate_pipeline(**_base(direction={"synthesis": {"state": "UNKNOWN", "evidence": "N/A"}}))
    assert r["decision"] == "WATCH"
    assert r["reason_code"] == "INSUFFICIENT_EVIDENCE"
