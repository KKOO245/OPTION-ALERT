# -*- coding: utf-8 -*-
import tempfile

from engine.snapshot import SnapshotStore
from engine.snapshot_builder import (
    build_snapshot,
    gamma_sign,
    iv_percentile,
    iv_zscore,
    load_analytics_rows,
    normalize_session,
    price_extreme_of,
    price_location_of,
    protection_divergence,
    trend_regime,
)
from tests._helpers import ROOT


FIX = ROOT / "tests" / "fixtures" / "analytics_soxx_synthetic.csv"


def _rows():
    return load_analytics_rows(str(FIX))


def test_session_normalize():
    assert normalize_session("早报") == "morning"
    assert normalize_session("晚报") == "evening"
    assert normalize_session("morning") == "morning"


def test_backfill_row_mode():
    rows = _rows()
    row = [r for r in rows if r["session"] == "morning"][-1]  # 2026-08-21 早报
    snap = build_snapshot(
        "SOXX", "早报", row, row["price"], "2026-08-21T10:15:00-04:00",
        analytics_rows=rows, source="analytics-backfill",
    )
    assert snap["session"] == "morning"
    assert snap["source"] == "analytics-backfill"
    assert snap["regime"]["gamma"] == "NEGATIVE"          # net_gamma_oi = -170000
    assert snap["regime"]["trend"] == "DOWN"              # 497.2 vs 505.0
    assert snap["regime"]["iv_level"] == "UNKNOWN"        # 历史不足 20 期
    assert snap["regime"]["age"] >= 1
    assert snap["momentum"]["iv_momentum"] is None
    assert snap["data_sufficiency"]["momentum.iv_momentum"] == "N/A"
    assert abs(snap["momentum"]["iv_momentum_1d"] - 4.0) < 1e-9  # 0.52 vs 0.48 (pp)
    assert snap["confirmation"]["iv_surge"] is True
    assert snap["location"]["call_wall"] is None
    assert snap["data_sufficiency"]["location.call_wall"] == "INSUFFICIENT_DATA"
    assert snap["location"]["price_location"] is None
    assert snap["data_sufficiency"]["location.price_location"] == "INSUFFICIENT_DATA"
    assert snap["confirmation"]["put_buy_flow"] is None
    assert snap["data_sufficiency"]["confirmation.put_buy_flow"] == "INSUFFICIENT_DATA"
    assert snap["price_extreme"] is None
    assert snap["data_sufficiency"]["price_extreme"] == "N/A"


def test_full_metrics_mode():
    rows = _rows()
    data = {
        "n_contracts": 1200,
        "prev_close": 505.0,
        "day_high": 501.8,
        "day_low": 496.4,
        "atm_iv_near": 0.52,
        "term_ratio": 0.82,
        "iv_skew_25": 4.0,
        "pcr_vol_near": 1.9,
        "structure": {"net_gex": -5_000_000, "gamma_flip": 502.0, "call_wall": 550.0, "put_wall": 490.0},
        "top_surge": [
            {"type": "put", "oi_change": 3000},
            {"type": "put", "oi_change": 2000},
            {"type": "call", "oi_change": 1000},
        ],
    }
    snap = build_snapshot(
        "SOXX", "morning", data, 497.2, "2026-08-21T10:15:00-04:00",
        analytics_rows=rows, source="cboe",
        forward_structure={"expirations": [{"expiration": "2026-09-18", "dte": 25}]},
    )
    assert snap["location"]["call_wall"] == 550.0
    assert snap["location"]["put_wall"] == 490.0
    assert snap["location"]["flip_levels"] == [502.0]
    # 497.2 距 put_wall 490 约 1.5% < 2% → 集中区优先于 flip
    assert snap["location"]["price_location"] == "near_put_concentration"
    assert snap["momentum"]["oi_flow"] == "put_building"
    # prev 505 > flip 502 >= spot 497.2 → 向下穿越
    assert snap["confirmation"]["price_break"] is True
    assert snap["data_quality"]["options_structure"] == "A"
    assert snap["context"]["day_high"] == 501.8
    assert snap["context"]["day_low"] == 496.4
    assert snap["forward"]["expirations"][0]["expiration"] == "2026-09-18"


def test_flip_status_tri_state():
    rows = _rows()
    base = {
        "n_contracts": 1200,
        "prev_close": 505.0,
        "atm_iv_near": 0.52,
        "structure": {"gamma_flip": 502.0, "call_wall": 550.0, "put_wall": 490.0},
    }
    snap = build_snapshot(
        "SOXX", "morning", base, 497.2, "2026-08-21T10:15:00-04:00",
        analytics_rows=rows, source="cboe",
    )
    assert snap["location"]["flip_levels"] == [502.0]
    assert snap["location"]["flip_status"] is None

    base2 = dict(base)
    base2["structure"] = {"gamma_flip": None, "call_wall": 550.0, "put_wall": 490.0}
    snap2 = build_snapshot(
        "SOXX", "morning", base2, 497.2, "2026-08-21T10:15:00-04:00",
        analytics_rows=rows, source="cboe",
    )
    assert snap2["location"]["flip_levels"] is None
    assert snap2["location"]["flip_status"] == "NO_FLIP_IN_RANGE"
    assert snap2["data_sufficiency"]["location.flip_levels"] == "NO_FLIP_IN_RANGE"

    base3 = dict(base)
    del base3["structure"]
    snap3 = build_snapshot(
        "SOXX", "morning", base3, 497.2, "2026-08-21T10:15:00-04:00",
        analytics_rows=rows, source="cboe",
    )
    assert snap3["location"]["flip_status"] == "INSUFFICIENT_DATA"


def test_helpers():
    assert gamma_sign(-1.0) == "NEGATIVE"
    assert gamma_sign(1.0) == "POSITIVE"
    assert gamma_sign(0.0) == "MIXED"
    assert gamma_sign(None) is None
    assert trend_regime(-0.03) == "DOWN"
    assert trend_regime(0.03) == "UP"
    assert trend_regime(0.001) == "RANGE"
    assert trend_regime(None) == "UNKNOWN"
    # 集中区优先
    assert price_location_of(497.2, 502.0, 550.0, 490.0) == "near_put_concentration"
    assert price_location_of(520.0, 502.0, 550.0, 490.0) == "above_flip"
    assert price_location_of(520.0, None, 550.0, 490.0) == "between"
    assert price_location_of(None, 502.0, 550.0, 490.0) is None
    # 新高/新低需要 ≥20 期
    closes = [100.0 + i for i in range(20)]
    assert price_extreme_of(121.0, closes) == "NEW_HIGH"
    assert price_extreme_of(99.0, closes) == "NEW_LOW"
    assert price_extreme_of(121.0, closes[:10]) is None
    # 背离逻辑
    assert protection_divergence("NEW_HIGH", "put_building") is True
    assert protection_divergence("NEW_LOW", "call_building") is True
    assert protection_divergence("NEW_HIGH", "call_building") is False
    assert protection_divergence("NEW_HIGH", None) is None


def test_zscore_and_percentile_require_20_obs():
    hist = [float(40 + i) for i in range(20)]  # 40..59，避免浮点误差
    assert iv_zscore(45.0, hist) is not None
    assert iv_zscore(45.0, hist[:19]) is None
    assert iv_percentile(45.0, hist) == 30.0  # 40..45 共 6 个 ≤ 45
    assert iv_percentile(60.0, hist) == 100.0
    assert iv_percentile(45.0, hist[:19]) is None


def test_real_analytics_soft_check():
    """用仓库里真实 analytics 数据做软校验（只断言结构不变量，不断言数值）。"""
    real = ROOT / "data" / "analytics" / "SOXX.csv"
    if not real.exists():
        return
    rows = load_analytics_rows(str(real))
    assert rows
    morning = [r for r in rows if r["session"] == "morning"]
    if not morning:
        return
    row = morning[-1]
    snap = build_snapshot(
        "SOXX", "morning", row, row["price"], f"{row['date']}T10:15:00-04:00",
        analytics_rows=rows, source="analytics-backfill",
    )
    with tempfile.TemporaryDirectory() as tmp:
        stored = SnapshotStore(tmp).store(snap)
        assert len(stored["snapshot_hash"]) == 64
        # 诚实规则：凡是 None 的关键字段，必须有数据充分性标签
        for key, val in (
            ("momentum.iv_momentum", snap["momentum"]["iv_momentum"]),
            ("momentum.iv_rank", snap["momentum"]["iv_rank"]),
            ("location.call_wall", snap["location"]["call_wall"]),
        ):
            if val is None:
                assert key in snap["data_sufficiency"], key
