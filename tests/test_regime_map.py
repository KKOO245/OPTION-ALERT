# -*- coding: utf-8 -*-
from engine.regime_map import bs_gamma, regime_map


def _contracts(rows):
    return [
        {"type": t, "strike": k, "dte": d, "iv": v, "open_interest": o}
        for t, k, d, v, o in rows
    ]


def test_bs_gamma_atm_higher_than_otm():
    g_atm = bs_gamma(100.0, 100.0, 10 / 365, 0.3)
    g_otm = bs_gamma(100.0, 130.0, 10 / 365, 0.3)
    assert g_atm is not None and g_otm is not None
    assert g_atm > g_otm > 0


def test_put_heavy_chain_negative_zone():
    # 大量实值 Put（客户多头假设 → 做市商空头 → 负 Gamma）
    contracts = _contracts([
        ("put", 90.0, 30, 0.35, 50000),
        ("put", 95.0, 30, 0.35, 50000),
        ("call", 110.0, 30, 0.35, 1000),
        ("call", 120.0, 30, 0.35, 1000),
    ])
    r = regime_map(contracts, spot=100.0)
    assert r is not None
    assert r["spot_zone"] == "NEGATIVE"
    assert r["layer"] == "MODEL"
    assert r["vol_surface_mode"] == "STICKY_STRIKE"
    assert r["n_contracts_used"] == 4


def test_call_heavy_chain_positive_zone():
    contracts = _contracts([
        ("call", 100.0, 30, 0.3, 50000),
        ("call", 105.0, 30, 0.3, 50000),
        ("put", 80.0, 30, 0.3, 500),
    ])
    r = regime_map(contracts, spot=100.0)
    assert r["spot_zone"] == "POSITIVE"


def test_flip_detected():
    # 下方 Put 主导、上方 Call 主导 → 过零
    contracts = _contracts([
        ("put", 95.0, 30, 0.3, 50000),
        ("call", 105.0, 30, 0.3, 50000),
    ])
    r = regime_map(contracts, spot=100.0)
    assert r["flip_levels"], r["flip_levels"]
    assert all(95.0 < f < 105.0 for f in r["flip_levels"])


def test_missing_iv_skipped():
    contracts = [
        {"type": "call", "strike": 100.0, "dte": 10, "iv": None, "open_interest": 1000},
        {"type": "call", "strike": 105.0, "dte": 10, "iv": 0.3, "open_interest": 1000},
    ]
    r = regime_map(contracts, spot=100.0)
    assert r["n_contracts_used"] == 1
    assert r["n_contracts_skipped"] == 1
