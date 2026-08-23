# -*- coding: utf-8 -*-
from engine import hash as hashing
from tests._helpers import valid_event


def test_canonical_json_deterministic():
    a = hashing.canonical_json({"b": 1, "a": [1, 2], "c": None})
    b = hashing.canonical_json({"c": None, "b": 1, "a": [1, 2]})
    assert a == b


def test_content_hash_excludes_hash_fields():
    e1 = valid_event()
    e2 = valid_event(event_hash="f" * 64, content_hash="e" * 64, prev_hash="d" * 64)
    assert hashing.content_hash(e1) == hashing.content_hash(e2)


def test_chain_verifies():
    events = []
    prev = ""
    for i in range(3):
        ev = valid_event(event_id=f"E{i}", created_at=f"2026-08-2{i}T10:15:00-04:00")
        ev["content_hash"] = hashing.content_hash(ev)
        ev["prev_hash"] = prev
        ev["event_hash"] = hashing.event_hash(ev, prev)
        events.append(ev)
        prev = ev["event_hash"]
    ok, errors = hashing.verify_chain(events)
    assert ok, errors


def test_chain_detects_tamper():
    events = []
    prev = ""
    for i in range(3):
        ev = valid_event(event_id=f"E{i}", created_at=f"2026-08-2{i}T10:15:00-04:00")
        ev["content_hash"] = hashing.content_hash(ev)
        ev["prev_hash"] = prev
        ev["event_hash"] = hashing.event_hash(ev, prev)
        events.append(ev)
        prev = ev["event_hash"]
    events[1]["spot"] = 999.0
    ok, errors = hashing.verify_chain(events)
    assert not ok
    assert any("content_hash" in e for e in errors)


def test_chain_detects_deletion():
    events = []
    prev = ""
    for i in range(3):
        ev = valid_event(event_id=f"E{i}", created_at=f"2026-08-2{i}T10:15:00-04:00")
        ev["content_hash"] = hashing.content_hash(ev)
        ev["prev_hash"] = prev
        ev["event_hash"] = hashing.event_hash(ev, prev)
        events.append(ev)
        prev = ev["event_hash"]
    del events[1]
    ok, errors = hashing.verify_chain(events)
    assert not ok
    assert any("event_hash" in e for e in errors)
