# -*- coding: utf-8 -*-
import tempfile

from engine.snapshot import SnapshotStore
from tests._helpers import load_fixture


def test_store_adds_hash_and_tags_missing():
    with tempfile.TemporaryDirectory() as tmp:
        store = SnapshotStore(tmp)
        snap = load_fixture("snapshot_morning_soxx.json")
        stored = store.store(snap)
        assert len(stored["snapshot_hash"]) == 64
        assert stored["data_sufficiency"] == {}
        # 删掉一个字段后应自动打 INSUFFICIENT_DATA
        snap2 = load_fixture("snapshot_morning_soxx.json")
        del snap2["momentum"]["iv_rank"]
        stored2 = store.store(snap2)
        assert stored2["data_sufficiency"]["momentum.iv_rank"] == "INSUFFICIENT_DATA"


def test_load_latest_and_load():
    with tempfile.TemporaryDirectory() as tmp:
        store = SnapshotStore(tmp)
        snap = load_fixture("snapshot_morning_soxx.json")
        store.store(snap)
        latest = store.load_latest()
        assert latest["ticker"] == "SOXX"
        assert latest["session"] == "morning"
        day = store.load("2026-08-21", "SOXX", "morning")
        assert day["spot"] == snap["spot"]
        assert store.list_days() == ["2026-08-21"]
