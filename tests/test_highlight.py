# -*- coding: utf-8 -*-
"""重点速览（highlight_v1）与事件差分（event_diff_v1）测试。"""

from report.highlight import build_highlights, event_differential
from tests._helpers import load_fixture


def _snap_with_forward():
    snap = load_fixture("snapshot_morning_soxx.json")
    snap["forward"] = {"expirations": [
        {
            "expiration": "2026-08-28", "dte": 2,
            "call_oi": 986135.0, "put_oi": 432532.0,
            "call_delta_oi": 285554.0, "put_delta_oi": 62714.0,
            "atm_call_price": 6.23, "atm_put_price": 5.93,
            "atm_iv": 0.94, "activity": "HIGH",
            "top_delta_oi": [
                {"strike": 230.0, "type": "call", "delta_oi": 116279,
                 "last_price": 0.98, "notional": 11395342.0,
                 "distance_pct": 9.4, "volume": 33533.0, "magnitude": "HIGH"},
            ],
        },
        {
            "expiration": "2026-09-04", "dte": 9,
            "call_oi": 171008.0, "put_oi": 191855.0,
            "call_delta_oi": 22207.0, "put_delta_oi": 10029.0,
            "atm_call_price": 7.45, "atm_put_price": 6.98,
            "atm_iv": 0.54, "activity": "HIGH",
            "top_delta_oi": [],
        },
    ]}
    return snap


def test_event_differential_detected():
    snap = _snap_with_forward()
    events = [{"date": "2026-08-28", "name": "美联储主席讲话", "time": "10:00"}]
    diff = event_differential(snap, events)
    assert diff is not None
    assert diff["expiration"] == "2026-08-28"
    assert diff["control_expiration"] == "2026-09-04"
    assert abs(diff["diff_pp"] - 40.0) < 0.1
    assert "美联储主席讲话" in diff["events"]


def test_event_differential_silent_when_no_event():
    snap = _snap_with_forward()
    assert event_differential(snap, None) is None
    assert event_differential(snap, []) is None
    # 事件日期不在任何期限覆盖范围内 → 沉默
    assert event_differential(snap, [{"date": "2026-09-18", "name": "x", "time": "10:00"}]) is None


def test_highlight_event_diff_critical():
    snap = _snap_with_forward()
    snap["momentum"]["price_momentum"] = 0.001
    events = [{"date": "2026-08-28", "name": "美联储主席讲话", "time": "10:00"}]
    items = build_highlights(snap, event_dates=events)
    assert items, "事件差分 40pp 应触发关键级"
    assert items[0]["level"] == "CRITICAL"
    assert items[0]["title"] == "事件差分"
    assert len(items) <= 3


def test_highlight_watch_near_strike_and_price_move():
    snap = _snap_with_forward()
    snap["forward"]["expirations"][0]["top_delta_oi"][0]["distance_pct"] = -3.0
    snap["momentum"]["price_momentum"] = -0.025
    items = build_highlights(snap, event_dates=None)
    titles = [i["title"] for i in items]
    assert "近现价集中开仓" in titles
    assert "单日价格波动" in titles


def test_highlight_empty_state():
    snap = load_fixture("snapshot_morning_soxx.json")
    snap["momentum"]["price_momentum"] = 0.001
    snap["location"]["flip_candidates"] = None
    snap["location"]["flip_levels"] = None
    items = build_highlights(snap, event_dates=None)
    assert items == []


def test_highlight_gamma_switch_requires_prev():
    snap = load_fixture("snapshot_morning_soxx.json")
    prev = load_fixture("snapshot_evening_soxx.json")
    # 无前值 → 不判切换
    assert not any(i["title"] == "Gamma Regime 切换" for i in build_highlights(snap, prev=None))
    prev["regime"]["gamma"] = "POSITIVE"
    snap["regime"]["gamma"] = "NEGATIVE"
    items = build_highlights(snap, prev=prev)
    assert any(i["title"] == "Gamma Regime 切换" and i["level"] == "CRITICAL" for i in items)
