# -*- coding: utf-8 -*-
import csv

from validation.base_rate import conditional_setup_rate, freeze_partition, unconditional_base_rate
from validation.confidence import label_for_n, wilson_ci
from validation.lift import lift_pp
from tests._helpers import ROOT


def test_wilson_ci():
    assert wilson_ci(0, 0) is None
    lo, hi = wilson_ci(5, 10)
    assert lo < 0.5 < hi
    lo, hi = wilson_ci(10, 10)
    assert lo > 0.6


def test_labels():
    assert label_for_n(5, 10, 30, 60) == "N/A"
    assert label_for_n(10, 10, 30, 60) == "PRELIMINARY"
    assert label_for_n(30, 10, 30, 60) == "DEVELOPING"
    assert label_for_n(60, 10, 30, 60) == "ESTABLISHED"


def test_unconditional_base_rate():
    with open(ROOT / "tests" / "fixtures" / "prices_soxx.csv", encoding="utf-8") as f:
        prices = list(csv.DictReader(f))
    for r in prices:
        r["close"] = float(r["close"])
    br = unconditional_base_rate(prices, "<=", -0.02, 3)
    assert br["n"] > 0
    assert 0 <= br["rate"] <= 1


def test_conditional_setup_rate_excludes_non_samples():
    eps = [
        {"representative_outcome": "CONFIRMED"},
        {"representative_outcome": "REJECTED"},
        {"representative_outcome": "EXPIRED"},
        {"representative_outcome": "PENDING"},
    ]
    r = conditional_setup_rate(eps)
    assert r["n"] == 2
    assert r["rate"] == 0.5
    assert r["excluded"] == 2
    assert r["excluded_kinds"]["EXPIRED"] == 1


def test_lift_pp():
    assert lift_pp(0.63, 0.51) == 12.0


def test_freeze_partition():
    eps = [
        {"start_ts": "2026-08-21T10:15:00-04:00"},
        {"start_ts": "2026-08-22T10:15:00-04:00"},
        {"start_ts": "2026-08-25T10:15:00-04:00"},
    ]
    pre, post = freeze_partition(eps, "2026-08-22")
    assert len(pre) == 1 and pre[0]["start_ts"].startswith("2026-08-21")
    assert len(post) == 2
