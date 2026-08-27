# -*- coding: utf-8 -*-
"""全链覆盖审计（coverage_v1）测试。"""

from engine.coverage import classify_iv, coverage_audit


def _c(iv=0.3, oi=100, last=1.0, bid=0.9, ask=1.1, strike=100.0):
    return {
        "iv": iv, "open_interest": oi, "last": last,
        "bid": bid, "ask": ask, "strike": strike,
    }


def test_classify_iv_states():
    assert classify_iv(_c()) == "VALID"
    assert classify_iv(_c(iv=None)) == "INVALID"
    assert classify_iv(_c(iv=0.0)) == "INVALID"
    assert classify_iv(_c(oi=0)) == "INVALID"
    assert classify_iv(_c(last=0.0)) == "LOW_LIQUIDITY"
    assert classify_iv(_c(bid=None, ask=None)) == "LOW_LIQUIDITY"


def test_coverage_audit_counts_and_band():
    contracts = [
        _c(strike=95.0),    # VALID
        _c(strike=100.0),   # VALID
        _c(strike=105.0, iv=None),  # INVALID
        _c(strike=120.0, last=0.0),  # LOW_LIQUIDITY，带外（+20%）
        _c(strike=90.0, bid=None, ask=None),  # LOW_LIQUIDITY，带内（-10%）
    ]
    out = coverage_audit(contracts, spot=100.0, band_pct=15.0)
    assert out["total_contracts"] == 5
    assert out["iv_valid"] == {"VALID": 2, "LOW_LIQUIDITY": 2, "INVALID": 1}
    assert out["strike_coverage_pct"] == 80.0  # 4/5
    assert out["oi_coverage_pct"] == 80.0   # VALID+LOW 全额：400/500
    assert out["valid_only_oi_coverage_pct"] == 40.0  # 仅 VALID：200/500
    assert out["band_oi_coverage_pct"] == 75.0  # 带内未加权：300/400
    # 带内加权（VALID=1 / LOW=0.5）：(100+100+0+50)/400 = 62.5%
    assert out["effective_gex_coverage_pct"] == 62.5


def test_coverage_audit_empty():
    out = coverage_audit([], spot=100.0)
    assert out["total_contracts"] == 0
    assert out["effective_gex_coverage_pct"] is None
