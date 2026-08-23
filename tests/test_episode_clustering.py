# -*- coding: utf-8 -*-
from engine.episode import EpisodeClusterer
from tests._helpers import valid_event


CAL = ["2026-08-17", "2026-08-18", "2026-08-19", "2026-08-20", "2026-08-21",
       "2026-08-24", "2026-08-25", "2026-08-26", "2026-08-27", "2026-08-28"]


def _ev(day, setup="A", seq=1):
    return valid_event(
        event_id=f"SOXX_{day.replace('-', '')}_{setup}_{seq:03d}",
        created_at=f"{day}T10:15:00-04:00",
        setup_id=setup,
    )


def test_adjacent_trading_days_merge():
    events = [_ev("2026-08-21"), _ev("2026-08-24")]  # 周五→周一：间隔 0 交易日
    eps = EpisodeClusterer(None).cluster(events, trading_days=CAL)
    assert len(eps) == 1
    assert eps[0]["n_events"] == 2
    assert eps[0]["representative_event_id"] == "SOXX_20260821_A_001"
    assert eps[0]["outcome_anchor"] == "episode_start"


def test_gap_two_trading_days_splits():
    events = [_ev("2026-08-21"), _ev("2026-08-26")]  # 间隔 2 交易日 → 拆
    eps = EpisodeClusterer(None).cluster(events, trading_days=CAL)
    assert len(eps) == 2


def test_chain_with_gap_one_merges():
    events = [_ev("2026-08-21"), _ev("2026-08-25")]  # 间隔 1 交易日 → 合并
    eps = EpisodeClusterer(None).cluster(events, trading_days=CAL)
    assert len(eps) == 1


def test_different_setups_separate():
    events = [_ev("2026-08-21", setup="A"), _ev("2026-08-21", setup="B1")]
    eps = EpisodeClusterer(None).cluster(events, trading_days=CAL)
    assert len(eps) == 2


def test_deterministic_ids():
    a = EpisodeClusterer(None).cluster([_ev("2026-08-21")], trading_days=CAL)
    b = EpisodeClusterer(None).cluster([_ev("2026-08-21")], trading_days=CAL)
    assert a[0]["episode_id"] == b[0]["episode_id"]
    assert a[0]["episode_id"].startswith("EP-episode_v1-")
