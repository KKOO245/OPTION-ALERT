# -*- coding: utf-8 -*-
from engine import yaml_mini
from engine.schema import METRICS, SECONDARY_KEYS, parse_horizon
from tests._helpers import ROOT


def test_frozen_setups_constraints():
    cfg = yaml_mini.load(ROOT / "config" / "setups.yaml")
    setups = cfg["setups"]
    assert len(setups) == 4
    assert {s["setup_id"] for s in setups} == {"A", "B1", "B2", "C"}
    for s in setups:
        assert isinstance(s["primary_target"], dict)  # 一 Setup 一 Primary Target
        pt = s["primary_target"]
        assert pt["metric"] in METRICS
        parse_horizon(pt["horizon"])
        assert 1 <= len(s["core"]) <= 3  # 最小充分集：1-3 条
        assert s["complexity_budget"]["max"] == 3
        assert set(s["secondary_attribution"]) <= SECONDARY_KEYS


def test_targets_yaml_has_metrics_for_all_setups():
    targets = yaml_mini.load(ROOT / "config" / "targets.yaml")
    metric_ids = {m["id"] for m in targets["metrics"]}
    setups = yaml_mini.load(ROOT / "config" / "setups.yaml")["setups"]
    for s in setups:
        assert s["primary_target"]["metric"] in metric_ids
