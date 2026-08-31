# -*- coding: utf-8 -*-
"""二阶希腊字母（second_order_v1）测试。"""

import datetime

from engine.second_order import bs_charm, bs_vanna, second_order_aggregate


def _c(sym, exp, typ, strike, oi, iv, dte=None):
    return {
        "contract_symbol": sym, "expiration": exp, "type": typ,
        "strike": strike, "open_interest": oi, "iv": iv, "dte": dte,
    }


def test_bs_vanna_charm_finite_and_signed():
    v = bs_vanna(100.0, 100.0, 30 / 365.0, 0.3)
    ch = bs_charm(100.0, 100.0, 30 / 365.0, 0.3)
    assert v is not None and ch is not None
    # 只断言有限且有界（符号随 r/T/σ 参数变化，不写死）
    assert 0 < abs(v) < 1.0 and 0 < abs(ch) < 1.0


def test_bs_vanna_charm_standard_formula():
    """回归：必须与标准 Black-Scholes 公式（= src.metrics.vanna_charm 口径）一致。"""
    import math

    def pdf(x):
        return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)

    def std_vanna(S, K, T, sigma, r=0.05):
        d1 = (math.log(S / K) + (r + sigma * sigma / 2.0) * T) / (sigma * math.sqrt(T))
        d2 = d1 - sigma * math.sqrt(T)
        return -pdf(d1) * d2 / sigma

    def std_charm(S, K, T, sigma, r=0.05):
        d1 = (math.log(S / K) + (r + sigma * sigma / 2.0) * T) / (sigma * math.sqrt(T))
        return pdf(d1) * (
            (r + sigma * sigma / 2.0) / (2.0 * sigma * math.sqrt(T))
            - math.log(S / K) / (2.0 * sigma * T ** 1.5)
        )

    for S, K, T, sig in [(100, 100, 30 / 365, 0.3), (100, 110, 10 / 365, 0.35), (500, 480, 30 / 365, 0.5)]:
        assert abs(bs_vanna(S, K, T, sig) - std_vanna(S, K, T, sig)) < 1e-12
        assert abs(bs_charm(S, K, T, sig) - std_charm(S, K, T, sig)) < 1e-12
    # ATM（S=K, r>0）标准 vanna 为负、charm 为正（符号契约）
    assert bs_vanna(100.0, 100.0, 30 / 365.0, 0.3) < 0
    assert bs_charm(100.0, 100.0, 30 / 365.0, 0.3) > 0


def test_second_order_aggregate_gates():
    as_of = datetime.date(2026, 8, 24)
    contracts = [
        _c("C1", "2026-08-28", "call", 100.0, 1000, 0.30, dte=4),
        _c("P1", "2026-08-28", "put", 100.0, 1000, 0.30, dte=4),
    ]
    # vanna 门控：|IV 变动| 0.6pp ≥ 0.5 → True；charm 门控：最近 dte 4 ≤ 5 → True
    out = second_order_aggregate(contracts, 100.0, as_of=as_of, iv_move_pp=0.6)
    assert out["vanna_gate"] is True
    assert out["charm_gate"] is True
    assert out["min_dte"] == 4
    assert out["net_vanna"] is not None
    # IV 变动未知 → vanna 门控 null（诚实不判）
    out2 = second_order_aggregate(contracts, 100.0, as_of=as_of, iv_move_pp=None)
    assert out2["vanna_gate"] is None
