# -*- coding: utf-8 -*-
from engine.price_series import closes_from_analytics
from engine.snapshot_builder import load_analytics_rows
from tests._helpers import ROOT


def test_picks_evening_price_per_day():
    rows = [
        {"date": "2026-08-19", "session": "morning", "price": 522.99},
        {"date": "2026-08-19", "session": "evening", "price": 520.43},
        {"date": "2026-08-20", "session": "morning", "price": 510.0},
        {"date": "2026-08-20", "session": "evening", "price": None},
    ]
    out = closes_from_analytics(rows)
    assert out == [
        {"date": "2026-08-19", "close": 520.43},
        {"date": "2026-08-20", "close": 510.0},  # 晚报缺失 → 早报兜底
    ]


def test_synthetic_fixture_series():
    rows = load_analytics_rows(str(ROOT / "tests" / "fixtures" / "analytics_soxx_synthetic.csv"))
    out = closes_from_analytics(rows)
    assert len(out) == 5  # 5 个交易日
    assert out[0]["date"] == "2026-08-17"
    assert out[-1] == {"date": "2026-08-21", "close": 494.0}  # 晚报价优先
