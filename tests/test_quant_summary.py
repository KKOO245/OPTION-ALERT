# -*- coding: utf-8 -*-
"""quant_summary_v1 测试：可溯源、缺数据省略、组合升级、不输出方向。"""

import datetime
import json
import tempfile
from pathlib import Path

from src.quant_summary import (
    DEFAULTS,
    activity_quant,
    gex_quant_line,
    hist_quant_line,
    options_quant,
)


def _mk_snapshot(ticker="QQQ", momentum=None, p3=None, location=None, spot=700.0):
    return {
        "ticker": ticker,
        "spot": spot,
        "momentum": momentum or {},
        "p3": p3 or {"gex": {"net_gex": -5.0e7}},
        "location": location or {"spot_vs_primary_flip": {"distance_pct": -0.08, "side": "BELOW"}},
    }


def test_options_quant_full():
    m = {"iv_rank": 0.24, "term_ratio": 1.17, "skew": 1.2, "pc_ratio": 1.18, "pc_oi_ratio": 0.91}
    s = options_quant(m)
    assert s is not None and s.startswith("量化视角：")
    assert "IV 历史低位（Rank 24%，期权偏便宜）" in s
    assert "期限结构正常偏陡（Term 1.17）" in s  # 1.17 > term_steep 1.15
    assert "保护溢价薄（Skew 1.2pp）" in s
    assert "非方向信号" in s


def test_options_quant_divergence_watch():
    # 存量 Call 拥挤（OI≤0.85）+ 当日成交偏 Put（P/C量≥1.15）→ 重点观察
    m = {"iv_rank": 0.5, "term_ratio": 1.1, "skew": 3.0, "pc_ratio": 1.20, "pc_oi_ratio": 0.80}
    s = options_quant(m)
    assert "⚠️ 重点观察：存量 Call 重（OI比 0.80）+ 当日成交偏 Put（P/C量 1.20）" in s
    assert "买/卖方向不可观测" in s


def test_options_quant_missing_omits():
    # 缺 iv_rank/skew → 相应子句省略，不编造
    m = {"term_ratio": 1.1, "pc_ratio": 1.0, "pc_oi_ratio": 1.0}
    s = options_quant(m)
    assert "IV" not in s and "Skew" not in s
    assert "当日成交与存量接近均衡" in s
    # 全缺 → None
    assert options_quant({}) is None


def test_hist_quant_combination():
    import shutil
    import tempfile

    tmp_path = Path(tempfile.mkdtemp(prefix="qs_"))
    oi = tmp_path / "data" / "oi_history"
    oi.mkdir(parents=True)
    # 历史 net_gex 全为正大值，pcr_oi_near 全为 1.0 → 当前负 GEX=低分位、pcr=0.5 极低
    rows = "date,spot,net_gex,flip,primary_flip,pcr_oi_all,pcr_oi_near\n"
    for i in range(100):
        rows += f"2025-01-{i%28+1:02d},500.0,1000000000.0,505.0,505.0,1.0,1.0\n"
    (oi / "QQQ.csv").write_text(rows, encoding="utf-8")
    snap = _mk_snapshot(
        "QQQ",
        momentum={"pc_oi_ratio": 0.5},
        p3={"gex": {"net_gex": -50000000.0}},
    )
    s = hist_quant_line(snap, tmp_path)
    assert s is not None and "Gamma 异常偏负" in s and "极端 Call 重" in s
    assert "⚠️ 需重点观察" in s  # 持仓极端 + Gamma 异常侧
    assert "非方向信号" in s
    # 非 SPY/QQQ → None
    assert hist_quant_line(_mk_snapshot("NVDA"), tmp_path) is None
    shutil.rmtree(tmp_path, ignore_errors=True)


def test_gex_quant_change_and_watch():
    snap = _mk_snapshot(p3={"gex": {"net_gex": -5.0e7}})
    prev = _mk_snapshot(p3={"gex": {"net_gex": 1.0e8}})  # 正 → 负：转负
    s = gex_quant_line(snap, prev, Path("."))
    assert s is not None
    assert "负 Gamma" in s and "由正转负" in s
    assert "现价位于 Flip 下方 0.08%" in s
    # 负 Gamma + 加深 → 重点观察（prev 为正 → 转负触发结构切换观察）
    assert "⚠️ 重点观察" in s
    # GEX 缺失 → None
    assert gex_quant_line(_mk_snapshot(p3={"gex": {}}), prev, Path(".")) is None


def test_activity_quant_pattern():
    spot = 700.0
    events = [
        {"type": "put", "expiration": "2026-09-30", "strike": 687.0, "oi_prev": 225,
         "open_interest": 14228, "last_price": 5.31, "volume": 68},
        {"type": "put", "expiration": "2026-09-30", "strike": 681.0, "oi_prev": 159,
         "open_interest": 14159, "last_price": 4.76, "volume": 26},
        {"type": "put", "expiration": "2026-09-11", "strike": 500.0, "oi_prev": 140,
         "open_interest": 13203, "last_price": 0.03, "volume": 13083},
    ]
    s = activity_quant(events, spot)
    assert s is not None
    assert "合计 ΔOI" in s and "3 个事件" in s
    assert "尾部对冲特征" in s
    assert "方向未知" in s
    assert activity_quant([], spot) is None
    assert activity_quant(None, spot) is None
