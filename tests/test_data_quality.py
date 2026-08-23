# -*- coding: utf-8 -*-
from engine.data_quality import bottleneck, bottleneck_low, grade_snapshot


def test_full_snapshot_grades():
    snap = {
        "spot": 100.0,
        "price": 99.5,
        "momentum": {"oi_flow": "put_building", "volume_ratio": 1.2, "iv_level": "HIGH"},
        "location": {"price_location": "below_flip", "call_wall": 110.0},
    }
    g = grade_snapshot(snap)
    assert g["market_data"] == "A"
    assert g["options_structure"] == "A"
    assert g["flow"] == "A"
    assert g["dealer_mechanism"] == "C"
    assert bottleneck(g) == "C"
    assert bottleneck_low(g) is False  # dealer 恒 C 属设计，不拖累判断


def test_bottleneck_low_when_critical_dimension_c():
    g = {"market_data": "A", "options_structure": "B", "flow": "C", "dealer_mechanism": "C"}
    assert bottleneck_low(g) is True


def test_missing_spot_is_c():
    g = grade_snapshot({})
    assert g["market_data"] == "C"
