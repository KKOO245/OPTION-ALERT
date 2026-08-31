# -*- coding: utf-8 -*-
"""analog_v1（P2 研究层）测试：分层匹配、条件统计、OOS 判定、样本不足保护。"""

import random

from engine.analog import (
    DEFAULTS,
    _exceed_base_median,
    match_hierarchy,
    oos_validate,
    outcome_stats,
)


def _mk_rec(vol, gamma, flip, pcr, ret3, date="2024-01-01"):
    return {
        "ticker": "QQQ",
        "date": date,
        "iv_pct": {"LOW": 10.0, "MID": 50.0, "HIGH": 90.0}[vol],
        "net_gex": {"POSITIVE": 1.0, "NEGATIVE": -1.0, "ZERO": 0.0}[gamma],
        "flip_dist": {"LE0.5%": 0.002, "LE1%": 0.008, "GT2%": 0.03}[flip],
        "pcr_pct": {"BOTTOM": 5.0, "MID": 50.0, "TOP": 95.0}[pcr],
        "outcome": {"ret_3d": ret3},
    }


def test_match_hierarchy_stops_at_min_n():
    recs = [_mk_rec("LOW", "NEGATIVE", "LE1%", "BOTTOM", 0.01) for _ in range(25)]
    recs += [_mk_rec("LOW", "NEGATIVE", "LE1%", "MID", 0.01) for _ in range(25)]
    ok = match_hierarchy(
        recs, {"vol": "LOW", "gamma": "NEGATIVE", "flip_dist": "LE1%", "pcr": "BOTTOM"},
        DEFAULTS, min_n=20,
    )
    assert ok["matched"] is True and ok["n"] == 25
    scarce = match_hierarchy(
        recs, {"vol": "LOW", "gamma": "NEGATIVE", "flip_dist": "LE1%", "pcr": "TOP"},
        DEFAULTS, min_n=20,
    )
    assert scarce["matched"] is False
    assert scarce["n_at_stop"] == 0
    assert scarce["reached_layer"] == "pcr"


def test_outcome_stats_quantiles():
    recs = [{"outcome": {"ret_3d": v}} for v in [1.0, 2.0, 3.0, 4.0]]
    s = outcome_stats(recs, 3)
    assert s["median_abs_ret_3d"] == 2.5
    assert s["p75_abs_ret_3d"] == 3.25
    assert s["p90_abs_ret_3d"] == 3.7


def _synthetic_split(rng, n_pre, n_post):
    pre, post = [], []
    for i, (n, date) in enumerate(((n_pre, "2022-01-01"), (n_post, "2024-01-01"))):
        base = []
        for _ in range(n):
            vol = "LOW" if rng.random() < 0.5 else "MID"
            gamma = "NEGATIVE" if rng.random() < 0.5 else "POSITIVE"
            rec = _mk_rec(vol, gamma, "LE1%", "BOTTOM", abs(rng.gauss(0.010, 0.002)), date=date)
            base.append(rec)
        # 状态子集（LOW+NEGATIVE+LE1%+BOTTOM）波动更高
        state_sub = [r for r in base if r["iv_pct"] == 10.0 and r["net_gex"] < 0]
        for r in state_sub:
            r["outcome"]["ret_3d"] = abs(rng.gauss(0.020, 0.002))
        if i == 0:
            pre = base
        else:
            post = base
    return pre, post


def test_oos_validate_validated_and_insufficient():
    rng = random.Random(42)
    pre, post = _synthetic_split(rng, 120, 100)
    state = {"vol": "LOW", "gamma": "NEGATIVE", "flip_dist": "LE1%", "pcr": "BOTTOM"}
    rec = oos_validate(pre + post, state, "2023-01-01", 3, DEFAULTS)
    assert rec["status"] == "VALIDATED_HIGHER_VOL", rec["status"]
    assert rec["oos_median_ratio"] is not None and rec["oos_median_ratio"] > 1.0
    # 样本不足：要求匹配数 < min_n
    scarce = oos_validate(
        pre + post, {"vol": "HIGH", "gamma": "POSITIVE", "flip_dist": "LE0.5%"},
        "2023-01-01", 3, {**DEFAULTS, "min_n": 200},
    )
    assert scarce["status"] == "INSUFFICIENT"


def test_oos_validate_lower_vol():
    rng = random.Random(7)
    pre, post = [], []
    for i, (n, date) in enumerate(((120, "2022-01-01"), (100, "2024-01-01"))):
        base = [_mk_rec("HIGH" if rng.random() < 0.5 else "MID", "POSITIVE", "GT2%", "TOP",
                        abs(rng.gauss(0.010, 0.002)), date=date)
                for _ in range(n)]
        # 状态子集（vol HIGH 但 gamma POSITIVE 且 pcr TOP）：后续波动偏低
        state_sub = [r for r in base if r["iv_pct"] == 90.0]
        for r in state_sub:
            r["outcome"]["ret_3d"] = abs(rng.gauss(0.005, 0.001))
        if i == 0:
            pre = base
        else:
            post = base
    rec = oos_validate(
        pre + post,
        {"vol": "HIGH", "gamma": "POSITIVE", "flip_dist": "GT2%", "pcr": "TOP"},
        "2023-01-01", 3, DEFAULTS,
    )
    assert rec["status"] == "VALIDATED_LOWER_VOL", rec["status"]
    assert rec["oos_median_ratio"] is not None and rec["oos_median_ratio"] < 1.0


def test_exceed_base_median():
    recs = [
        {"outcome": {"ret_3d": 0.02}},
        {"outcome": {"ret_3d": 0.005}},
        {"outcome": {"ret_3d": 0.015}},
    ]
    k, n = _exceed_base_median(recs, 3, 0.01)
    assert (k, n) == (2, 3)
