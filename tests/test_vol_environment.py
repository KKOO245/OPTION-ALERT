# -*- coding: utf-8 -*-
"""VIX / Volatility Environment v1.1：规则冻结、缺失处理、时间口径、transition、shock。"""

import json
import tempfile
from pathlib import Path

from src import vol_environment as ve


def _rules():
    return ve._load_rules("config")


def test_classify_bucket_boundaries():
    rules = _rules()
    assert ve.classify_regime(14.99, rules) == "LOW"
    assert ve.classify_regime(15.0, rules) == "NORMAL"
    assert ve.classify_regime(19.99, rules) == "NORMAL"
    assert ve.classify_regime(20.0, rules) == "ELEVATED"
    assert ve.classify_regime(24.99, rules) == "ELEVATED"
    assert ve.classify_regime(25.0, rules) == "STRESS"


def test_classify_missing_required_input():
    rules = _rules()
    assert ve.classify_regime(None, rules) == "INSUFFICIENT_DATA"
    assert ve.classify_regime("bad", rules) == "INSUFFICIENT_DATA"


def test_missing_vix_is_insufficient_not_guessed():
    env = ve.compute_vol_environment(None, "2026-08-24T10:15:00-04:00", "morning", config_root="config")
    assert env["regime"]["label"] == "INSUFFICIENT_DATA"
    assert env["vix"]["value"] is None
    assert env["regime"]["evidence_completeness"] == "partial"


def test_optional_missing_keeps_label_partial():
    env = ve.compute_vol_environment(15.67, "2026-08-24T10:15:00-04:00", "morning", config_root="config")
    assert env["regime"]["label"] == "NORMAL"
    assert env["regime"]["evidence_completeness"] == "partial"
    assert env["vix"]["prior_close"] is None
    assert env["vix"]["change_1d_pct"] is None


def test_series_changes_and_transition_stable():
    series = [("2026-08-18", 14.0), ("2026-08-19", 14.5), ("2026-08-20", 15.0), ("2026-08-21", 15.48)]
    env = ve.compute_vol_environment(
        15.67, "2026-08-24T10:15:00-04:00", "morning",
        vix_series=series, prev_regime_label="NORMAL", config_root="config",
    )
    assert env["vix"]["prior_close"] == 15.48
    assert round(env["vix"]["change_1d_pct"], 2) == 1.23
    assert env["vix"]["change_5d_pct"] is None  # 前收盘不足 5 个
    assert env["regime"]["transition"] == {"from": "NORMAL", "to": "NORMAL", "changed": False}


def test_transition_changed():
    series = [("2026-08-21", 19.0)]
    env = ve.compute_vol_environment(
        20.3, "2026-08-24T10:15:00-04:00", "morning",
        vix_series=series, prev_regime_label="NORMAL", config_root="config",
    )
    assert env["regime"]["label"] == "ELEVATED"
    assert env["regime"]["transition"]["changed"] is True
    assert env["regime"]["transition"]["from"] == "NORMAL"


def test_today_close_not_counted_as_prior():
    """快照日当天即使出现在序列里，也不能当作前收盘。"""
    series = [("2026-08-21", 15.48), ("2026-08-24", 15.5)]
    env = ve.compute_vol_environment(
        15.67, "2026-08-24T16:30:00-04:00", "evening",
        vix_series=series, config_root="config",
    )
    assert env["vix"]["prior_close"] == 15.48


def test_basis_by_session():
    m = ve.compute_vol_environment(15.0, "2026-08-24T10:15:00-04:00", "morning", config_root="config")
    e = ve.compute_vol_environment(15.0, "2026-08-24T16:30:00-04:00", "evening", config_root="config")
    assert m["vix"]["basis"] == "intraday"
    assert e["vix"]["basis"] == "close"


def test_basis_honest_intraday_even_if_session_evening():
    """FORCE 手动运行盘中按「晚报」生成时，数据仍是盘中值，不许谎报 close。"""
    env = ve.compute_vol_environment(15.0, "2026-08-24T13:30:00-04:00", "evening", config_root="config")
    assert env["vix"]["basis"] == "intraday"


def test_shock_levels():
    def shock(pct):
        prior = 15.0 / (1.0 + pct / 100.0)
        series = [("2026-08-21", prior)]
        return ve.compute_vol_environment(
            15.0, "2026-08-24T10:15:00-04:00", "morning",
            vix_series=series, config_root="config",
        )["shock"]

    assert shock(5.0)["level"] == "NONE"
    assert shock(12.0)["level"] == "ELEVATED"
    assert shock(25.0)["level"] == "EXTREME"


def test_percentile_20d():
    series = [(f"2026-07-{d:02d}", 15.0) for d in range(1, 25)]
    env = ve.compute_vol_environment(
        16.0, "2026-08-24T10:15:00-04:00", "morning",
        vix_series=series, config_root="config",
    )
    assert env["regime"]["inputs"]["vix_percentile_20d"] == 100.0
    assert env["regime"]["evidence_completeness"] == "partial"  # 期限结构 v1 恒 null


def test_load_prev_regime_label():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp) / "analytics" / "daily"
        d21 = root / "2026-08-21"
        d21.mkdir(parents=True)
        (d21 / "SOXX_evening.json").write_text(json.dumps({
            "context": {"vol_environment": {"regime": {"label": "ELEVATED"}}}
        }), encoding="utf-8")
        assert ve.load_prev_regime_label(tmp, "2026-08-24", "morning") == "ELEVATED"
        assert ve.load_prev_regime_label(tmp, "2026-08-24", "evening") == "ELEVATED"

        d24 = root / "2026-08-24"
        d24.mkdir(parents=True)
        (d24 / "SOXX_morning.json").write_text(json.dumps({
            "context": {"vol_environment": {"regime": {"label": "NORMAL"}}}
        }), encoding="utf-8")
        assert ve.load_prev_regime_label(tmp, "2026-08-24", "evening") == "NORMAL"
        assert ve.load_prev_regime_label(tmp, "2026-08-24", "morning") == "ELEVATED"


def test_load_rules_accepts_repo_root_config_root():
    """回归：options_report 传仓库根目录（BASE_DIR）也能找到 regimes.yaml（8/25 线上事故）。"""
    rules = ve._load_rules(ve.BASE_DIR)
    assert rules["vol_regime"]["version"] == "vol_regime_v1"
    assert ve.classify_regime(15.85, rules) == "NORMAL"
