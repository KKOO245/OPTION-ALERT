# -*- coding: utf-8 -*-
"""flip_context_v1（P1 研究字段）测试。"""

import datetime
import json
import tempfile
from pathlib import Path

from src.flip_context import (
    build_flip_context,
    distance_percentile,
    load_flip_distance_history,
    recent_flips,
    stability_5d,
)


def test_distance_percentile_basic():
    hist = [0.001, 0.002, 0.005, 0.01, 0.02]
    # spot/flip → cur=0.002：小于等于 0.002 的有 2 个 → 40%
    spot, flip = 100.0, 100.0 / (1.0 + 0.002)
    assert abs(distance_percentile(spot, flip, hist) - 40.0) < 1e-9
    assert distance_percentile(None, flip, hist) is None
    assert distance_percentile(100.0, None, hist) is None
    assert distance_percentile(100.0, 101.0, []) is None


def test_stability_labels():
    params = {"lookback": 5, "min_obs": 3, "high_range_pct": 0.5, "medium_range_pct": 1.5}
    stable = stability_5d([("2026-08-28", 715.0), ("2026-08-27", 715.5), ("2026-08-26", 715.3)], params)
    assert stable["label"] == "HIGH"  # 区间 0.07% < 0.5%
    jumpy = stability_5d([("2026-08-28", 700.0), ("2026-08-27", 720.0), ("2026-08-26", 706.0)], params)
    assert jumpy["label"] == "LOW"  # 区间 ~2.9% > 1.5%
    insufficient = stability_5d([("2026-08-28", 715.0)], params)
    assert insufficient["label"] == "INSUFFICIENT_DATA"
    assert insufficient["range_pct"] is None


def test_build_flip_context_end_to_end():
    tmp = Path(tempfile.mkdtemp(prefix="fc_"))
    try:
        # 假 oi_history（SPY：5 个历史距离）
        oi_dir = tmp / "data" / "oi_history"
        oi_dir.mkdir(parents=True)
        (oi_dir / "SPY.csv").write_text(
            "date,spot,net_gex,flip,primary_flip\n"
            "2025-12-01,500.0,1.0,505.0,505.0\n"
            "2025-12-02,500.0,1.0,502.0,502.0\n"
            "2025-12-03,500.0,1.0,501.0,501.0\n"
            "2025-12-04,500.0,1.0,498.0,498.0\n"
            "2025-12-05,500.0,1.0,495.0,495.0\n",
            encoding="utf-8",
        )
        # 假 live 快照（3 天 flip_primary 稳定）
        snap_dir = tmp / "analytics" / "daily"
        for day, flip in [("2026-08-26", 715.3), ("2026-08-27", 715.5), ("2026-08-28", 715.0)]:
            d = snap_dir / day
            d.mkdir(parents=True)
            (d / "SPY_evening.json").write_text(
                json.dumps({"location": {"flip_primary": flip}}), encoding="utf-8"
            )
        ctx = build_flip_context("SPY", 715.0, 715.2, datetime.date(2026, 8, 31), tmp, str(snap_dir))
        assert ctx is not None
        assert ctx["flip_distance_pct_15y"] is not None
        assert ctx["stability_5d"]["label"] == "HIGH"
        assert ctx["stability_5d"]["n"] == 3
        # 非 SPY/QQQ → None
        assert build_flip_context("NVDA", 100.0, 101.0, datetime.date(2026, 8, 31), tmp, str(snap_dir)) is None
        # 历史距离正确加载（5 个点）
        assert len(load_flip_distance_history("SPY", tmp)) == 5
        # recent_flips 严格早于 as_of
        flips = recent_flips("SPY", datetime.date(2026, 8, 31), str(snap_dir), lookback=3)
        assert [d for d, _ in flips] == ["2026-08-26", "2026-08-27", "2026-08-28"]
    finally:
        import shutil

        shutil.rmtree(tmp, ignore_errors=True)
