# -*- coding: utf-8 -*-
import csv
import tempfile

from engine.outcome import OutcomeEngine
from engine.thesis_logger import EventStore
from tests._helpers import ROOT, valid_event


FIX = ROOT / "tests" / "fixtures"


def _csv_rows(name, cast=("close",)):
    with open(FIX / name, encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        for c in cast:
            if r.get(c) not in (None, ""):
                r[c] = float(r[c])
    return rows


def _cal():
    return [
        l.strip()
        for l in (FIX / "trading_calendar.txt").read_text(encoding="utf-8").splitlines()
        if l.strip() and not l.startswith("#")
    ]


def _event(**kw):
    return valid_event(created_at="2026-08-21T10:15:00-04:00", **kw)


def test_close_return_confirmed():
    with tempfile.TemporaryDirectory() as tmp:
        store = EventStore(tmp)
        ev = store.append_event(_event())
        rev = OutcomeEngine(store).evaluate(
            ev, _csv_rows("prices_soxx.csv"), trading_days=_cal(),
            now="2026-08-28T09:00:00-04:00",
        )
        assert rev is not None
        assert rev["result"] == "CONFIRMED"
        assert abs(rev["metric_value"] - (485.4 / 497.2 - 1.0)) < 1e-9


def test_close_return_rejected():
    with tempfile.TemporaryDirectory() as tmp:
        store = EventStore(tmp)
        ev = store.append_event(_event())
        prices = _csv_rows("prices_soxx.csv")
        for r in prices:
            if r["date"] == "2026-08-26":
                r["close"] = 505.0
        rev = OutcomeEngine(store).evaluate(
            ev, prices, trading_days=_cal(), now="2026-08-28T09:00:00-04:00"
        )
        assert rev["result"] == "REJECTED"


def test_pending_before_window_end():
    with tempfile.TemporaryDirectory() as tmp:
        store = EventStore(tmp)
        ev = store.append_event(_event())
        rev = OutcomeEngine(store).evaluate(
            ev, _csv_rows("prices_soxx.csv"), trading_days=_cal(),
            now="2026-08-24T09:00:00-04:00",
        )
        assert rev is None  # 窗口未结束：不写 revision


def test_expired_when_data_missing():
    with tempfile.TemporaryDirectory() as tmp:
        store = EventStore(tmp)
        ev = store.append_event(_event())
        prices = [r for r in _csv_rows("prices_soxx.csv") if r["date"] <= "2026-08-25"]
        rev = OutcomeEngine(store).evaluate(
            ev, prices, trading_days=_cal(), now="2026-08-28T09:00:00-04:00"
        )
        assert rev["result"] == "EXPIRED"
        assert rev["evaluation_status"] == "INSUFFICIENT_DATA"


def test_rv_expansion_confirmed():
    with tempfile.TemporaryDirectory() as tmp:
        store = EventStore(tmp)
        ev = store.append_event(
            _event(
                primary_target={
                    "metric": "5D_rv_expansion",
                    "direction": ">=",
                    "threshold": 1.25,
                    "horizon": "5D",
                    "evaluation_rule": "rv_ratio",
                }
            )
        )
        rev = OutcomeEngine(store).evaluate(
            ev, [], rv=_csv_rows("rv_soxx.csv", cast=("rv5d", "rv20d")),
            trading_days=_cal(), now="2026-08-28T09:00:00-04:00",
        )
        assert rev["result"] == "CONFIRMED"
        assert abs(rev["metric_value"] - 0.48 / 0.32) < 1e-9


def test_mdd_confirmed():
    with tempfile.TemporaryDirectory() as tmp:
        store = EventStore(tmp)
        ev = store.append_event(
            _event(
                primary_target={
                    "metric": "3D_mdd",
                    "direction": ">=",
                    "threshold": 0.03,
                    "horizon": "3D",
                    "evaluation_rule": "mdd_path",
                }
            )
        )
        rev = OutcomeEngine(store).evaluate(
            ev, _csv_rows("prices_soxx.csv"), path=_csv_rows("path_soxx.csv"),
            trading_days=_cal(), now="2026-08-28T09:00:00-04:00",
        )
        assert rev["result"] == "CONFIRMED"
        assert rev["metric_value"] > 0.03


def test_invalidate():
    with tempfile.TemporaryDirectory() as tmp:
        store = EventStore(tmp)
        ev = store.append_event(_event())
        rev = OutcomeEngine(store).invalidate(ev, "规则Bug：条件定义错误")
        assert rev["result"] == "INVALIDATED"
        assert rev["evaluation_status"] == "SUPERSEDED"
        model = store.read_model()
        assert model["events"][0]["outcome"] == "INVALIDATED"


def test_provisional_status():
    ev = _event()
    status = OutcomeEngine(None).provisional_status(
        ev, _csv_rows("prices_soxx.csv"), trading_days=_cal()
    )
    assert status["target_status"] == "TEMPORARILY_MET"
    assert status["value"] < 0
