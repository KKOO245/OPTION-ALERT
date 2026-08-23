# -*- coding: utf-8 -*-
"""Episode 聚类（验证层的独立样本单位）。

规则（版本化，预提交）：
  - episode_v1：同一 (setup_id, ticker) 的连续触发，间隔 ≤ max_gap_trading_days 交易日 → 一簇
  - representative_event = first（第一个事件）
  - outcome_anchor = episode_start（以簇起点为评价锚点）
  - episode_id 由 rule_version + first_event_id 确定性生成；改规则 = 新版本重算，旧记录不改。
"""

from __future__ import annotations

from datetime import date, datetime, timedelta
from typing import Any, Dict, List, Optional


def _iso_day(s: str) -> date:
    return date.fromisoformat(s[:10])


def _trading_gap(a: date, b: date, trading_days: Optional[List[str]]) -> int:
    """a→b 之间的交易日数（不含两端）。有日历时精确，否则按工作日近似。"""
    if trading_days:
        days = sorted(d[:10] for d in trading_days)
        try:
            ia = days.index(a.isoformat())
            ib = days.index(b.isoformat())
        except ValueError:
            return _weekday_gap(a, b)
        return max(0, ib - ia - 1)
    return _weekday_gap(a, b)


def _weekday_gap(a: date, b: date) -> int:
    n = 0
    d = a + timedelta(days=1)
    while d < b:
        if d.weekday() < 5:
            n += 1
        d += timedelta(days=1)
    return n


class EpisodeClusterer:
    def __init__(self, store, max_gap_trading_days: int = 1, rule_version: str = "episode_v1"):
        self.store = store
        self.max_gap = max_gap_trading_days
        self.rule_version = rule_version

    def cluster(
        self, events: List[Dict[str, Any]], trading_days: Optional[List[str]] = None
    ) -> List[Dict[str, Any]]:
        by_key: Dict[tuple, List[Dict[str, Any]]] = {}
        for ev in events:
            by_key.setdefault((ev["setup_id"], ev["ticker"]), []).append(ev)

        episodes: List[Dict[str, Any]] = []
        for (setup_id, ticker), evs in sorted(by_key.items()):
            evs = sorted(evs, key=lambda e: (e["created_at"], e["event_id"]))
            cluster: List[Dict[str, Any]] = []
            for ev in evs:
                if cluster:
                    gap = _trading_gap(
                        _iso_day(cluster[-1]["created_at"]),
                        _iso_day(ev["created_at"]),
                        trading_days,
                    )
                    if gap > self.max_gap:
                        episodes.append(self._make_episode(cluster))
                        cluster = []
                cluster.append(ev)
            if cluster:
                episodes.append(self._make_episode(cluster))

        episodes.sort(key=lambda e: (e["setup_id"], e["ticker"], e["start_ts"]))
        return episodes

    def _make_episode(self, cluster: List[Dict[str, Any]]) -> Dict[str, Any]:
        first = cluster[0]
        last = cluster[-1]
        rep_outcome = first.get("outcome", "PENDING")
        return {
            "episode_id": f"EP-{self.rule_version}-{first['event_id']}",
            "rule_version": self.rule_version,
            "setup_id": first["setup_id"],
            "ticker": first["ticker"],
            "start_event_id": first["event_id"],
            "end_event_id": last["event_id"],
            "event_ids": [e["event_id"] for e in cluster],
            "representative_event_id": first["event_id"],
            "outcome_anchor": "episode_start",
            "start_ts": first["created_at"],
            "end_ts": last["created_at"],
            "n_events": len(cluster),
            "representative_outcome": rep_outcome,
            "representative_target_status": first.get("target_status", "NOT_EVALUATED"),
            "member_outcomes": _outcome_counts(cluster),
        }


def _outcome_counts(cluster: List[Dict[str, Any]]) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for ev in cluster:
        k = ev.get("outcome", "PENDING")
        counts[k] = counts.get(k, 0) + 1
    return counts
