# -*- coding: utf-8 -*-
from engine.edges import direction_components, mechanism_confidence, pricing_proxy, volatility_components
from tests._helpers import load_fixture


def test_direction_components_fixture():
    snap = load_fixture("snapshot_morning_soxx.json")
    d = direction_components(snap)
    assert d["trend"]["state"] == "DOWN"
    assert d["relative_strength"]["state"] == "WEAK"
    syn = d["synthesis"]
    assert syn["state"] == "BEARISH"
    assert syn["calibrated"] is False
    assert syn["agreement"] in ("STRONG", "PARTIAL", "WEAK")


def test_direction_unknown_when_no_data():
    d = direction_components({})
    assert d["synthesis"]["state"] == "UNKNOWN"
    assert d["synthesis"]["evidence"] == "N/A"


def test_volatility_components():
    snap = load_fixture("snapshot_morning_soxx.json")  # iv_level HIGH, iv_momentum 0.8
    v = volatility_components(snap)
    assert v["state"] == "ELEVATED"
    assert v["spread"]["evidence"] == "N/A"  # 快照无 RV，诚实标 N/A
    assert v["calibrated"] is False


def test_pricing_proxy_insufficient_history():
    p = pricing_proxy(0.40, [0.3, 0.31, 0.32])
    assert p["classification"] == "INSUFFICIENT_DATA"
    assert p["layer"] == "DERIVED"


def test_pricing_proxy_percentile():
    rv = [0.2 + i * 0.01 for i in range(30)]  # 0.20..0.49
    p = pricing_proxy(0.5, rv)  # 高于全部 → EXPENSIVE
    assert p["classification"] == "EXPENSIVE"
    assert p["percentile"] == 100.0
    assert p["percentile_basis"] == "RV_PROXY"  # 无历史 IV → 明确标代理口径


def test_pricing_proxy_spread_percentile_basis():
    rv = [0.2 + i * 0.01 for i in range(30)]
    iv_hist = [0.2 + i * 0.01 for i in range(30)]  # spread ≈ 0
    p = pricing_proxy(0.5, rv, iv_series=iv_hist)
    assert p["percentile_basis"] == "SPREAD_PERCENTILE"
    assert p["classification"] == "EXPENSIVE"  # 当前 spread 远超历史 spread


def test_mechanism_confidence():
    m = mechanism_confidence({})
    assert m["level"] == "LOW"
    assert "Scenario" in m["scenario_note"]
    assert m["layer"] == "MODEL"
