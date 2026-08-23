# -*- coding: utf-8 -*-
"""测试辅助：构造合法事件 / 加载 fixture。"""

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

FIXTURES = pathlib.Path(__file__).resolve().parent / "fixtures"


def load_fixture(name: str):
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


def valid_event(**overrides):
    base = {
        "event_id": "SOXX_20260821_A_001",
        "schema_version": "event_v1",
        "data_version": "test",
        "setup_id": "A",
        "setup_version": "v1",
        "trigger_rule_version": "A_v1",
        "confirmation_rule_version": "A_conf_v1",
        "target_version": "targets_v1",
        "regime_version": "regimes_v1",
        "rule_freeze_date": "2026-08-22",
        "created_at": "2026-08-21T10:15:00-04:00",
        "snapshot_hash": "0" * 64,
        "ticker": "SOXX",
        "spot": 497.2,
        "regime": {"version": "regimes_v1", "trend": "DOWN", "gamma": "NEGATIVE"},
        "location": {"price_location": "below_flip"},
        "momentum": {"iv_momentum": 0.8},
        "confirmation": {},
        "context": {},
        "primary_target": {
            "metric": "3D_close_return",
            "direction": "<=",
            "threshold": -0.02,
            "horizon": "3D",
            "evaluation_rule": "close_to_close",
        },
        "secondary_attribution": ["mfe", "mdd", "rv", "path"],
        "direction_signal": {"label": "NEUTRAL", "evidence": "LOW"},
        "vol_edge": {"label": "UNKNOWN", "evidence": "LOW"},
        "pricing_proxy": {"label": "UNKNOWN", "value": None},
        "mechanism_confidence": {"level": "LOW", "note": "测试"},
        "data_quality": {"market_data": "A", "options_structure": "B"},
        "data_sufficiency": {},
        "setup_trigger_met": True,
        "confirmation_status": [
            {"name": "iv_surge", "met": True, "rule_version": "A_conf_v1", "note": ""}
        ],
        "target_status": "NOT_EVALUATED",
        "decision": "WATCH",
        "no_trade_reason": None,
        "lifecycle": "OPEN",
        "outcome": "PENDING",
        "evaluation_status": "EVALUABLE",
        "episode_id": None,
        "content_hash": "0" * 64,
        "prev_hash": "",
        "event_hash": "0" * 64,
    }
    base.update(overrides)
    return base
