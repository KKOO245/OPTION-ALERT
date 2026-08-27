# -*- coding: utf-8 -*-
"""P3 采集层（p3_collect_v1）测试。"""

import math

from engine.p3_collect import collect_p3, daily_closes, realized_vol


def test_realized_vol_window_and_missing():
    prices = [100.0 + i for i in range(30)]
    rv = realized_vol(prices, 5, min_obs=5)
    assert rv is not None and rv >= 0
    assert realized_vol([100.0, 100.1], 5, min_obs=5) is None  # 观测不足


def test_daily_closes_evening_priority():
    rows = [
        {"date": "2026-08-25", "session": "morning", "price": 210.0},
        {"date": "2026-08-25", "session": "evening", "price": 211.0},
        {"date": "2026-08-26", "session": "morning", "price": 212.0},
    ]
    closes = daily_closes(rows)
    assert closes == [211.0, 212.0]  # 08-25 用晚报价，08-26 无晚报用早报价


def test_event_overlap_per_expiry():
    exps = [
        {"expiration": "2026-08-28", "dte": 2},
        {"expiration": "2026-09-04", "dte": 9},
    ]
    events = [
        {"date": "2026-08-28", "name": "美联储主席讲话", "time": "10:00"},
    ]
    p3 = collect_p3(
        regime_result=None, coverage=None, second_order=None,
        atm_iv_near=0.9, price_rows=None,
        forward_expirations=exps, event_dates=events,
        as_of=__import__("datetime").datetime(2026, 8, 26, 9, 0),
        spot=210.0, call_wall=None, put_wall=None, oi_strikes=None,
    )
    ov = p3["event_overlap"]
    assert ov[0]["covers_event"] is True
    assert ov[1]["covers_event"] is False
    assert p3["iv_rv"]["rv_5d"] is None  # 无价格历史 → 不编造

    # 快照时刻晚于事件（已公布）→ 不再算覆盖
    p3b = collect_p3(
        regime_result=None, coverage=None, second_order=None,
        atm_iv_near=0.9, price_rows=None,
        forward_expirations=exps, event_dates=events,
        as_of=__import__("datetime").datetime(2026, 8, 28, 11, 0),
        spot=210.0, call_wall=None, put_wall=None, oi_strikes=None,
    )
    assert p3b["event_overlap"] is None


def test_confluence_families():
    p3 = collect_p3(
        regime_result={"flip_levels": [208.0, 212.0], "net_gex_at_spot": 100.0},
        coverage=None, second_order=None,
        atm_iv_near=0.9, price_rows=None,
        forward_expirations=None, event_dates=None,
        spot=210.0, call_wall=209.5, put_wall=None,
        oi_strikes=[{"strike": 210.0, "type": "call", "oi": 100}],
    )
    assert p3["confluence"]["families_in_band"] == 2  # gamma(flip/墙) + oi
    assert p3["gex"]["net_gex"] == 100.0
