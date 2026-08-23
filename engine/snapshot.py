# -*- coding: utf-8 -*-
"""快照存储：校验、自动标注缺失字段、计算 snapshot_hash、落盘。

目录（data_root 下）：
  state/latest_snapshot.json        最近一次快照
  analytics/daily/YYYY-MM-DD/TICKER_{session}.json  每日快照历史
"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

from engine.hash import snapshot_hash
from engine.schema import assert_valid_snapshot


GROUPS: Dict[str, List[str]] = {
    "regime": ["version", "trend", "gamma", "iv_level", "age", "transition"],
    "location": ["price_location", "flip_levels", "call_wall", "put_wall", "concentration"],
    "momentum": [
        "iv_momentum",
        "iv_level",
        "iv_rank",
        "skew_momentum",
        "term_structure_momentum",
        "pc_ratio",
        "oi_flow",
        "price_momentum",
        "volume_ratio",
    ],
    "confirmation": ["iv_surge", "skew_surge", "volume_surge", "put_buy_flow", "price_break"],
    "price_extreme": ["price_extreme"],
    "protection_divergence": ["protection_divergence"],
    "context": ["spy_return", "qqq_return", "sector_relative", "vix", "notes"],
    "data_quality": ["market_data", "options_structure", "flow", "dealer_mechanism"],
}


class SnapshotStore:
    def __init__(self, data_root: str | Path):
        self.root = Path(data_root)
        self.analytics = self.root / "analytics" / "daily"
        self.state = self.root / "state"

    def _autotag(self, snapshot: Dict[str, Any]) -> Dict[str, str]:
        """对缺失字段打 INSUFFICIENT_DATA 标签；保留已有标签。"""
        tags = dict(snapshot.get("data_sufficiency") or {})
        for group, fields in GROUPS.items():
            # 顶层组键不存在（而非显式 null）才算整组缺失
            if group not in snapshot:
                for f in fields:
                    tags[f"{group}.{f}"] = "INSUFFICIENT_DATA"
                continue
            src = snapshot[group]
            if not isinstance(src, dict):
                continue
            for f in fields:
                if f not in src:
                    tags[f"{group}.{f}"] = "INSUFFICIENT_DATA"
        return tags

    def store(self, snapshot: Dict[str, Any]) -> Dict[str, Any]:
        assert_valid_snapshot(snapshot)
        data = dict(snapshot)
        data["data_sufficiency"] = self._autotag(data)
        data["snapshot_hash"] = snapshot_hash(data)

        ts = datetime.fromisoformat(data["created_at"])
        day = ts.date().isoformat()
        path = self.analytics / day / f"{data['ticker']}_{data['session']}.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        _write_json(path, data)

        self.state.mkdir(parents=True, exist_ok=True)
        _write_json(self.state / "latest_snapshot.json", data)
        return data

    def load_latest(self) -> Dict[str, Any]:
        path = self.state / "latest_snapshot.json"
        return _read_json(path) if path.exists() else None

    def load(self, day: str, ticker: str, session: str) -> Dict[str, Any]:
        return _read_json(self.analytics / day / f"{ticker}_{session}.json")

    def list_days(self) -> List[str]:
        if not self.analytics.exists():
            return []
        return sorted(p.name for p in self.analytics.iterdir() if p.is_dir())

    def load_day(self, day: str) -> List[Dict[str, Any]]:
        d = self.analytics / day
        if not d.exists():
            return []
        return [_read_json(p) for p in sorted(d.glob("*.json"))]

    def load_all(self) -> List[Dict[str, Any]]:
        out = []
        for day in self.list_days():
            out.extend(self.load_day(day))
        return out


def _write_json(path: Path, data: Any) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(path)


def _read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))
