# -*- coding: utf-8 -*-
from engine.setup_detector import SetupDetector
from tests._helpers import ROOT, load_fixture


DET = SetupDetector(str(ROOT / "config"))


def test_morning_snapshot_triggers_a_b1_b2_not_c():
    snap = load_fixture("snapshot_morning_soxx.json")
    events, audits = DET.detect(snap)
    triggered = {e["setup_id"] for e in events}
    assert triggered == {"A", "B1", "B2"}
    assert "C" not in triggered
    checked = {a["setup_id"] for a in audits}
    assert checked == {"A", "B1", "B2", "C"}


def test_a_confirmation_statuses():
    snap = load_fixture("snapshot_morning_soxx.json")
    events, _ = DET.detect(snap)
    a = next(e for e in events if e["setup_id"] == "A")
    by_name = {c["name"]: c["met"] for c in a["confirmation_status"]}
    assert by_name["iv_surge"] is True
    assert by_name["skew_surge"] is True
    assert by_name["volume_confirmation"] is True
    assert by_name["put_buy_confirmation"] is None  # 数据缺失 → 不编造


def test_missing_core_field_not_triggered():
    snap = load_fixture("snapshot_morning_soxx.json")
    del snap["momentum"]  # B1/B2 依赖 momentum
    events, audits = DET.detect(snap)
    assert {"A"} == {e["setup_id"] for e in events}
    b1_audit = next(a for a in audits if a["setup_id"] == "B1")
    assert b1_audit["trigger_met"] is False
    assert "INSUFFICIENT_DATA" in b1_audit["trigger_reason"]


def test_b2_not_triggered_when_iv_normal():
    snap = load_fixture("snapshot_morning_soxx.json")
    snap["momentum"]["iv_level"] = "NORMAL"
    events, _ = DET.detect(snap)
    assert "B2" not in {e["setup_id"] for e in events}
