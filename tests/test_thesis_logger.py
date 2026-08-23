# -*- coding: utf-8 -*-
import json
import tempfile

from engine.thesis_logger import EventStore, IntegrityError
from engine.setup_detector import SetupDetector
from tests._helpers import load_fixture


def _two_events():
    det = SetupDetector("config")
    snap = load_fixture("snapshot_morning_soxx.json")
    events, _ = det.detect(snap)
    return events


def test_append_sequential_ids_and_chain():
    with tempfile.TemporaryDirectory() as tmp:
        store = EventStore(tmp)
        payloads = _two_events()
        e1 = store.append_event(payloads[0])
        e2 = store.append_event(payloads[1])
        assert e1["event_id"] == "SOXX_20260821_A_001"
        assert e2["event_id"] == "SOXX_20260821_B1_001"
        assert e2["prev_hash"] == e1["event_hash"]
        assert e1["event_id"] != e2["event_id"]
        ok, errors = store.verify()
        assert ok, errors


def test_read_model_merges_revision():
    with tempfile.TemporaryDirectory() as tmp:
        store = EventStore(tmp)
        e = store.append_event(_two_events()[0])
        rev = {
            "revision_id": "REV_001",
            "event_id": e["event_id"],
            "result": "CONFIRMED",
            "target_status": "CONFIRMED",
            "evaluation_status": "EVALUABLE",
            "evaluation_rule_version": "targets_v1",
            "snapshot_hash": e["snapshot_hash"],
            "data_timestamp": "2026-08-26",
            "ts": "2026-08-28T09:00:00-04:00",
            "evaluation_anchor_date": "2026-08-21",
            "evaluation_end_date": "2026-08-26",
            "evaluation_horizon_days": 3,
            "metric_value": -0.023,
            "reason": None,
        }
        assert store.append_revision(rev) is not None
        assert store.append_revision(rev) is None  # 幂等
        model = store.read_model()
        ev = model["events"][0]
        assert ev["outcome"] == "CONFIRMED"
        assert ev["lifecycle"] == "CLOSED"
        assert len(ev["outcome_revisions"]) == 1


def test_tamper_detected():
    with tempfile.TemporaryDirectory() as tmp:
        store = EventStore(tmp)
        store.append_event(_two_events()[0])
        path = store.events_path
        lines = path.read_text(encoding="utf-8").splitlines()
        parsed = json.loads(lines[0])
        parsed["spot"] = 999.0
        path.write_text(json.dumps(parsed, ensure_ascii=False) + "\n", encoding="utf-8")
        events, errors = store.load_events(verify=True)
        assert errors


def test_refuse_append_after_corruption():
    with tempfile.TemporaryDirectory() as tmp:
        store = EventStore(tmp)
        store.append_event(_two_events()[0])
        path = store.events_path
        path.write_text("{\"bad\": json\n", encoding="utf-8")
        try:
            store.append_event(_two_events()[1])
            raise AssertionError("应当拒绝写入")
        except IntegrityError:
            pass
