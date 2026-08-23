# -*- coding: utf-8 -*-
from engine.schema import (
    SchemaError,
    parse_horizon,
    validate_event,
    validate_revision,
    validate_snapshot,
)
from tests._helpers import valid_event


def test_valid_event_passes():
    assert validate_event(valid_event()) == []


def test_missing_field_fails():
    ev = valid_event()
    del ev["outcome"]
    assert any("outcome" in e for e in validate_event(ev))


def test_bad_decision_fails():
    ev = valid_event(decision="BUY_NOW")
    assert any("decision" in e for e in validate_event(ev))


def test_no_trade_requires_reason():
    ev = valid_event(decision="NO_TRADE", no_trade_reason=None)
    assert any("no_trade_reason" in e for e in validate_event(ev))


def test_primary_target_must_be_single():
    ev = valid_event(primary_target=[{"metric": "x"}, {"metric": "y"}])
    assert validate_event(ev)


def test_secondary_keys_restricted():
    ev = valid_event(secondary_attribution=["mfe", "magic"])
    assert any("secondary_attribution" in e for e in validate_event(ev))


def test_horizon_parse():
    assert parse_horizon("3D") == 3
    assert parse_horizon(5) == 5
    try:
        parse_horizon("X")
        raise AssertionError("应抛出 SchemaError")
    except SchemaError:
        pass


def test_snapshot_validation():
    assert validate_snapshot(
        {
            "schema_version": "snapshot_v1",
            "ticker": "SOXX",
            "created_at": "2026-08-21T10:15:00-04:00",
            "session": "morning",
            "source": "test",
            "spot": 497.2,
        }
    ) == []
    assert validate_snapshot(
        {
            "schema_version": "snapshot_v1",
            "ticker": "SOXX",
            "created_at": "2026-08-21T10:15:00-04:00",
            "session": "midnight",
            "source": "test",
            "spot": 497.2,
        }
    )


def test_revision_validation():
    good = {
        "revision_id": "REV_X_001",
        "event_id": "X",
        "result": "CONFIRMED",
        "ts": "2026-08-28T09:00:00-04:00",
        "evaluation_rule_version": "targets_v1",
        "snapshot_hash": "0" * 64,
        "data_timestamp": "2026-08-26",
        "evaluation_anchor_date": "2026-08-21",
        "evaluation_end_date": "2026-08-26",
        "evaluation_horizon_days": 3,
        "metric_value": -0.023,
        "reason": None,
    }
    assert validate_revision(good) == []
    bad = dict(good, result="MAYBE")
    assert validate_revision(bad)
    assert validate_revision(dict(good, result="INVALIDATED", reason=None))


def test_optional_evidence_ledger():
    ev = valid_event(evidence={"supporting": ["neg gamma"], "contradicting": [], "unknown": ["dealer_position"]})
    assert validate_event(ev) == []
    bad = valid_event(evidence={"supporting": "not-a-list"})
    assert any("evidence" in e for e in validate_event(bad))
