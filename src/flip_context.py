# -*- coding: utf-8 -*-
"""Flip 上下文（flip_context_v1，P1）：历史距离分位 + 近端稳定性。

只进 p3（研究层 JSON），不进报告/评分。诚实边界：
- 距离分位：|spot/primary_flip−1| 相对 oi_history 全样本（lambdaclass，SPY/QQQ 15y）的分位。
  live 的 primary_flip 是 spot 网格全链重定价，历史序列是行权价网格——层级口径略不同，
  一律标注 basis，不伪装成同一测量。
- 稳定性：最近 lookback 个交易日（live 快照）primary_flip 的区间跨度（%中位）。
  有效点 < min_obs → INSUFFICIENT_DATA（不编数）。
- 参数为候选（flip_stability_v1，登记在 thresholds.yaml），待历史校准，不冻结为真理。
"""

from __future__ import annotations

import datetime
import json
import os
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

SCHEMA = "flip_context_v1"
DEFAULT_STAB = {
    "lookback": 5,
    "min_obs": 3,
    "high_range_pct": 0.5,
    "medium_range_pct": 1.5,
}


def _num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def _stab_params(root) -> Dict[str, Any]:
    params = dict(DEFAULT_STAB)
    try:
        from engine.yaml_mini import load

        cfg = load(Path(root) / "config" / "thresholds.yaml")
        fs = (cfg or {}).get("flip_stability_v1") or {}
        for k in params:
            v = fs.get(k)
            if v is not None:
                params[k] = float(v) if k.endswith("_pct") or k in ("lookback", "min_obs") else v
    except Exception:  # noqa: BLE001
        pass
    return params


def load_flip_distance_history(ticker: str, root) -> List[float]:
    """oi_history 的 |spot/primary_flip−1| 全样本（lambdaclass 口径）。"""
    p = Path(root) / "data" / "oi_history" / f"{ticker}.csv"
    if not p.exists():
        return []
    import pandas as pd

    try:
        df = pd.read_csv(p)
    except Exception:  # noqa: BLE001
        return []
    if not {"spot", "primary_flip"}.issubset(df.columns):
        return []
    out: List[float] = []
    for r in df.itertuples(index=False):
        s = _num(r.spot)
        f = _num(r.primary_flip)
        if s and f and s > 0 and f > 0:
            out.append(abs(s / f - 1.0))
    return out


def distance_percentile(spot, flip, hist: List[float]) -> Optional[float]:
    if spot is None or flip is None or spot <= 0 or flip <= 0:
        return None
    cur = abs(spot / flip - 1.0)
    if not hist:
        return None
    return sum(1 for x in hist if x <= cur) / len(hist) * 100.0


def recent_flips(ticker: str, as_of_date, snapshots_dir: str,
                 lookback: int = 5, scan_days: int = 14) -> List[Tuple[str, float]]:
    """最近 lookback 个有效 primary_flip（live 快照，日期严格早于 as_of）。"""
    sdir = Path(snapshots_dir)
    out: List[Tuple[str, float]] = []
    d = as_of_date - datetime.timedelta(days=1)
    for _ in range(scan_days):
        day = d.isoformat()
        f = sdir / day / f"{ticker}_evening.json"
        if not f.exists():
            f = sdir / day / f"{ticker}_morning.json"
        if f.exists():
            try:
                snap = json.loads(f.read_text(encoding="utf-8"))
                fp = (snap.get("location") or {}).get("flip_primary")
                if fp is not None:
                    v = _num(fp)
                    if v is not None and v > 0:
                        out.append((day, v))
            except Exception:  # noqa: BLE001
                pass
        if len(out) >= lookback:
            break
        d -= datetime.timedelta(days=1)
    out.sort()
    return out


def stability_5d(flips: List[Tuple[str, float]], params: Dict[str, Any]) -> Dict[str, Any]:
    """5D 稳定性：区间跨度（%中位）→ HIGH/MEDIUM/LOW；点数不足 → INSUFFICIENT_DATA。"""
    min_obs = int(params.get("min_obs", 3))
    basis = "live snapshot flip_primary"
    if len(flips) < min_obs:
        return {"n": len(flips), "range_pct": None, "label": "INSUFFICIENT_DATA", "basis": basis}
    vals = [v for _, v in flips]
    med = sorted(vals)[len(vals) // 2]
    if med is None or med <= 0:
        return {"n": len(flips), "range_pct": None, "label": "INSUFFICIENT_DATA", "basis": basis}
    rng = (max(vals) - min(vals)) / med * 100.0
    if rng <= float(params.get("high_range_pct", 0.5)):
        label = "HIGH"
    elif rng <= float(params.get("medium_range_pct", 1.5)):
        label = "MEDIUM"
    else:
        label = "LOW"
    return {
        "n": len(flips),
        "range_pct": round(rng, 3),
        "label": label,
        "basis": basis,
        "dates": [d for d, _ in flips],
    }


def build_flip_context(ticker: str, spot, primary_flip, as_of_date,
                       root, snapshots_dir: str) -> Optional[Dict[str, Any]]:
    """组装 flip_context（仅 SPY/QQQ 有 15y oi_history；其余返回 None）。"""
    ticker = (ticker or "").upper()
    if ticker not in ("SPY", "QQQ"):
        return None
    params = _stab_params(root)
    hist = load_flip_distance_history(ticker, root)
    dp = distance_percentile(spot, primary_flip, hist)
    flips = recent_flips(
        ticker, as_of_date, snapshots_dir,
        lookback=int(params.get("lookback", 5)),
    )
    stab = stability_5d(flips, params)
    return {
        "schema_version": SCHEMA,
        "ticker": ticker,
        "as_of": str(as_of_date),
        "flip_distance_pct_15y": round(dp, 1) if dp is not None else None,
        "flip_distance_basis": (
            "|spot/primary_flip-1| vs lambdaclass oi_history 15y"
            "（live=spot网格全链重定价；历史=行权价网格，层级略不同）"
        ),
        "stability_5d": stab,
    }
