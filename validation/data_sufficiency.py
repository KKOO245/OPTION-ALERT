# -*- coding: utf-8 -*-
"""数据充分性标签统一计算。"""

from __future__ import annotations

from typing import Any, Dict

from validation.confidence import label_for_n


def label_for_episodes(n: int, thresholds: Dict[str, Any]) -> str:
    t = thresholds["data_sufficiency"]["setup_episodes"]
    return label_for_n(n, t["preliminary"], t["developing"], t["established"])


def label_for_rank(n: int, thresholds: Dict[str, Any]) -> str:
    t = thresholds["data_sufficiency"]["rank_obs"]
    return label_for_n(n, t["preliminary"], t["developing"], t["established"])


def setup_sufficiency_report(setup_ids, episodes_by_setup, thresholds) -> Dict[str, str]:
    out = {}
    for sid in setup_ids:
        eps = episodes_by_setup.get(sid, [])
        out[sid] = label_for_episodes(len(eps), thresholds)
    return out
