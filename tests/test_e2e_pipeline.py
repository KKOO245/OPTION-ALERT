# -*- coding: utf-8 -*-
"""端到端：快照 → 检测 → 事件 → Outcome → Episode → 验证 → 报告。"""

import csv
import tempfile

from engine.episode import EpisodeClusterer
from engine.outcome import OutcomeEngine
from engine.setup_detector import SetupDetector
from engine.snapshot import SnapshotStore
from engine.thesis_logger import EventStore
from report.evening import render_evening
from report.morning import render_morning
from validation.base_rate import conditional_setup_rate
from tests._helpers import ROOT, load_fixture


def _rows(name):
    with open(ROOT / "tests" / "fixtures" / name, encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        for k, v in r.items():
            if k != "date" and v not in ("", None):
                r[k] = float(v)
    return rows


def _cal():
    return [
        l.strip()
        for l in (ROOT / "tests" / "fixtures" / "trading_calendar.txt")
        .read_text(encoding="utf-8").splitlines()
        if l.strip() and not l.startswith("#")
    ]


def test_full_pipeline():
    with tempfile.TemporaryDirectory() as tmp:
        snaps = SnapshotStore(tmp)
        morning = snaps.store(load_fixture("snapshot_morning_soxx.json"))
        evening = snaps.store(load_fixture("snapshot_evening_soxx.json"))

        det = SetupDetector(str(ROOT / "config"))
        store = EventStore(tmp)
        for snap in (morning, evening):
            events, audits = det.detect(snap)
            for a in audits:
                store.audit(a)
            for ev in events:
                store.append_event(ev)

        model = store.read_model()
        assert len(model["events"]) == 6  # 2 快照 x 3 Setup（A/B1/B2）
        assert all(e["setup_id"] in ("A", "B1", "B2") for e in model["events"])

        prices = _rows("prices_soxx.csv")
        rv = _rows("rv_soxx.csv")
        engine = OutcomeEngine(store)
        by_setup = {}
        for ev in model["events"]:
            rev = engine.evaluate(
                ev, prices, rv=rv, trading_days=_cal(),
                now="2026-08-28T09:00:00-04:00",
            )
            assert rev is not None
            by_setup.setdefault(ev["setup_id"], []).append(rev["result"])

        assert by_setup["A"] == ["CONFIRMED", "CONFIRMED"]
        assert by_setup["B1"] == ["CONFIRMED", "CONFIRMED"]
        assert by_setup["B2"] == ["REJECTED", "REJECTED"]

        # Episode 聚类：每个 setup 一天 2 个事件 → 1 个独立 episode
        clusterer = EpisodeClusterer(store)
        eps = clusterer.cluster(store.read_model()["events"], trading_days=_cal())
        assert len(eps) == 3
        assert all(ep["n_events"] == 2 for ep in eps)
        store.write_episodes(eps)
        model2 = store.read_model()
        assert all(e["episode_id"] for e in model2["events"])

        # 验证：A 的条件率 = 100%（n=1 独立 episode）
        a_eps = [e for e in eps if e["setup_id"] == "A"]
        assert conditional_setup_rate(a_eps)["rate"] == 1.0

        # 报告渲染
        morning_text = render_morning(morning, model2)
        evening_text = render_evening(evening, model2)
        assert "SOXX" in morning_text and "Setup A" in morning_text
        assert "Thesis Scorecard" in evening_text

        # 完整性
        ok, errors = store.verify()
        assert ok, errors


def test_invalidated_excluded_from_condition_rate():
    with tempfile.TemporaryDirectory() as tmp:
        store = EventStore(tmp)
        det = SetupDetector(str(ROOT / "config"))
        snap = SnapshotStore(tmp).store(load_fixture("snapshot_morning_soxx.json"))
        events, audits = det.detect(snap)
        for a in audits:
            store.audit(a)
        for ev in events:
            store.append_event(ev)
        engine = OutcomeEngine(store)
        for ev in store.read_model()["events"]:
            engine.invalidate(ev, "数据污染测试")
        eps = EpisodeClusterer(store).cluster(store.read_model()["events"])
        rate = conditional_setup_rate(eps)
        assert rate["n"] == 0
        assert rate["excluded"] == len(eps)
