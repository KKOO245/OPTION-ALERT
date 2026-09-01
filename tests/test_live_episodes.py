# -*- coding: utf-8 -*-
"""live snapshot → episode 接线测试：映射正确、结果只用未来、幂等。"""

import json
import tempfile
from pathlib import Path

from scripts.build_live_episodes import build_day


def _snap(ticker="QQQ", spot=700.0):
    return {
        "created_at": "2026-08-20T16:30:00-04:00",
        "ticker": ticker,
        "spot": spot,
        "session": "evening",
        "momentum": {
            "atm_iv": 0.18, "iv_rank": 0.30, "term_ratio": 1.1,
            "pc_ratio": 1.2, "pc_oi_ratio": 0.8,
        },
        "p3": {
            "gex": {"net_gex": -5.0e7},
            "iv_rv": {"rv_20d": 0.12},
            "second_order": {"net_vanna": 1.0e6, "net_charm": -2.0e5},
        },
        "location": {
            "flip_primary": 705.0, "flip_levels": [705.0, 710.0],
            "call_wall": 720.0, "put_wall": 680.0,
            "call_wall_class": "PRIMARY", "put_wall_class": "WEAK",
        },
    }


def test_build_day_mapping_and_outcome():
    tmp = Path(tempfile.mkdtemp(prefix="live_"))
    try:
        (tmp / f"QQQ_evening.json").write_text(json.dumps(_snap()), encoding="utf-8")
        eps = build_day("QQQ", "2026-08-20", tmp)
        assert len(eps) == 2, len(eps)
        layers = {e["layer"] for e in eps}
        assert layers == {"iv", "oi"}
        for e in eps:
            assert e["schema_version"] == "replay_v1"
            assert e["outcome"].get("ret_1d") is not None  # 未来数据可用
            assert e["date"] == "2026-08-20"
        iv = next(e for e in eps if e["layer"] == "iv")
        assert iv["inputs"]["atm_iv"] == 0.18
        assert iv["inputs"]["iv_pct"] == 30.0
        assert abs(iv["inputs"]["spread_pp"] - 6.0) < 1e-6
        oi = next(e for e in eps if e["layer"] == "oi")
        assert oi["inputs"]["net_gex"] == -5.0e7
        assert oi["inputs"]["primary_flip"] == 705.0
        assert oi["inputs"]["pcr_oi_near"] == 0.8
        assert "GAMMA_NEGATIVE" in oi["conditions"]
        print("映射与 outcome 断言 OK")
    finally:
        import shutil

        shutil.rmtree(tmp, ignore_errors=True)


def test_build_day_future_insufficient_returns_empty():
    tmp = Path(tempfile.mkdtemp(prefix="live2_"))
    try:
        (tmp / "QQQ_evening.json").write_text(
            json.dumps({**_snap(), "created_at": "2026-08-28T16:30:00-04:00"}),
            encoding="utf-8",
        )
        # 2026-08-28 未来 5D 无数据（closes 止于 08-28）→ 不构造，防未来泄漏
        assert build_day("QQQ", "2026-08-28", tmp) == []
        print("未来数据不足 → 空，OK")
    finally:
        import shutil

        shutil.rmtree(tmp, ignore_errors=True)
