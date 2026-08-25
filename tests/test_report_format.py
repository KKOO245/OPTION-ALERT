# -*- coding: utf-8 -*-
from report.format import code_block, table, ticker_heading
from report.evening import render_evening, ticker_evening
from report.morning import (
    _forward_block,
    _trading_gap,
    calendar_block,
    market_block,
    render_morning,
    ticker_morning,
)
from tests._helpers import load_fixture


def test_ticker_heading_standalone():
    h = ticker_heading("SOXX")
    assert h == "\n## SOXX\n"


def test_table_closed_and_title_outside():
    t = table([{"a": 1, "b": "x"}], {"a": "A", "b": "B"}, "标题")
    assert t.startswith("**标题**\n```")
    assert t.endswith("```")
    assert t.count("```") == 2


def test_code_block():
    assert code_block("x") == "```\nx\n```"


def test_render_morning_template():
    snap = load_fixture("snapshot_morning_soxx.json")
    text = render_morning(snap)
    assert "## SOXX" in text
    assert "Options:" in text
    assert "数据溯源" in text
    assert "Setup: 今日无 Setup 触发" in text


def test_render_evening_template():
    snap = load_fixture("snapshot_evening_soxx.json")
    text = render_evening(snap)
    assert "Thesis Scorecard" in text
    assert "PENDING" in text
    assert "数据溯源" in text


def test_render_morning_market_and_calendar():
    snap = load_fixture("snapshot_morning_soxx.json")
    market = {"spy": 765.72, "vix": 15.13, "fg_score": 45, "fg_rating": "中性"}
    cal = ["- 周一 08-24 08:30　【高】CPI 通胀　预测 0.2% ｜ 实际 待公布 ｜ 前值 0.3%"]
    text = render_morning(snap, market=market, calendar=cal)
    # 快照自带 vol_environment → 渲染新格式市场环境块（头部与快照一致）
    assert "📊 市场环境" in text
    assert "SPY $765.72" in text and "VIX 22.40" in text and "Vol Regime: ELEVATED" in text
    assert "CNN 恐惧贪婪 45（中性）" in text
    assert "宏观日历" in text and "CPI 通胀" in text


def test_render_morning_market_legacy_when_snapshot_lacks_vol_env():
    snap = load_fixture("snapshot_morning_soxx.json")
    del snap["context"]["vol_environment"]
    market = {"spy": 765.72, "vix": 15.13}
    text = render_morning(snap, market=market)
    assert "市场背景" in text and "VIX 15.13" in text


def test_market_block_with_vol_environment():
    snap = load_fixture("snapshot_morning_soxx.json")
    ve_env = snap["context"]["vol_environment"]
    market = {"spy": 764.19, "qqq": 701.4, "fg_score": 56, "fg_rating": "greed", "vol_environment": ve_env}
    lines = market_block(market)
    joined = "\n".join(lines)
    assert "📊 市场环境" in joined
    assert "SPY $764.19" in joined and "QQQ $701.40" in joined
    assert "VIX 22.40 ↑2.8%（5D +6.1%）" in joined
    assert "Vol Regime: ELEVATED" in joined
    assert "SPX 期权隐含的近 30 日预期波动率" in joined
    assert "CNN 恐惧贪婪 56（greed）" in joined


def test_market_block_legacy_fallback():
    market = {"spy": 765.72, "vix": 15.13}
    joined = "\n".join(market_block(market))
    assert "市场背景" in joined and "SPY $765.72" in joined and "VIX 15.13" in joined


def test_ticker_morning_vix_spread_and_env_tag_when_triggered():
    snap = load_fixture("snapshot_morning_soxx.json")
    setup_status = {
        "triggered": True,
        "setup_id": "A",
        "version": "v1",
        "core": {"trend": "DOWN", "location": "below_flip", "gamma": "NEGATIVE（模型层）"},
        "confirmation": {"satisfied": 1, "rejected": 0, "unknown": 1, "unknown_fields": ["price_break"]},
        "qualification": {"n_episodes": 5, "oos_lift_pp": None, "ci_lower": None, "level": "EXPERIMENTAL"},
        "primary_target": {"metric": "3D_close_return", "direction": "<=", "threshold": -0.02},
        "status": "WATCH",
    }
    text = ticker_morning(snap, setup_status=setup_status)
    assert "IV–VIX Spread" in text
    assert "仅作相对波动率 Proxy" in text
    assert "环境: Vol ELEVATED（仅环境标签，不参与计票）" in text


def test_ticker_morning_high_low():
    snap = load_fixture("snapshot_morning_soxx.json")
    prev = load_fixture("snapshot_evening_soxx.json")
    text = ticker_morning(snap, prev_snapshot=prev)
    assert "今日高 501.80" in text and "低 496.40" in text


def test_evening_scorecard_high_low():
    snap = load_fixture("snapshot_evening_soxx.json")
    morning = load_fixture("snapshot_morning_soxx.json")
    text = ticker_evening(snap, morning=morning)
    assert "今日高 503.50" in text and "低 495.10" in text


def test_ticker_morning_no_vix_lines_without_setup():
    snap = load_fixture("snapshot_morning_soxx.json")
    text = ticker_morning(snap)
    assert "IV–VIX Spread" not in text
    assert "环境: Vol" not in text


def _fwd_exp(exp, dte, c_d, p_d, act, **kw):
    base = {
        "expiration": exp,
        "dte": dte,
        "call_oi": 42800,
        "put_oi": 31600,
        "call_oi_prev": 37400,
        "put_oi_prev": 30800,
        "call_delta_oi": c_d,
        "put_delta_oi": p_d,
        "call_volume": 9000,
        "put_volume": 3000,
        "has_prev": True,
        "new_listing": False,
        "atm_strike": 515,
        "atm_call_price": 5.84,
        "atm_put_price": 14.12,
        "atm_iv": 0.388,
        "activity": act,
        "delta_exposure": None,
        "top_delta_oi": [],
        "significant": [],
    }
    base.update(kw)
    return base


def test_forward_block_l1_quiet():
    snap = {"forward": {"expirations": [
        _fwd_exp("2026-08-28", 4, 2100, 300, "LOW"),
        _fwd_exp("2026-09-04", 11, 3100, 2100, "MEDIUM"),
        _fwd_exp("2026-09-11", 18, -500, 1800, "MEDIUM"),
        _fwd_exp("2026-09-18", 25, 5400, 800, "LOW"),
    ]}}
    text = "\n".join(_forward_block(snap))
    assert "📆 Forward Expiration Structure" in text
    assert "08-28  C +2.1k / P +0.3k ｜ Activity LOW ｜ 4D" in text
    assert "Activity MEDIUM △" in text
    assert "09-18 Forward Structure" not in text
    assert "Significant Forward Positioning" not in text


def test_forward_block_l2_l3():
    top = [
        {"strike": 575, "type": "call", "delta_oi": 7348, "last_price": 0.87,
         "notional": 7348 * 0.87 * 100, "distance_pct": 11.5, "volume": 5840, "magnitude": "HIGH"},
        {"strike": 670, "type": "call", "delta_oi": 4120, "last_price": 0.49,
         "notional": 4120 * 0.49 * 100, "distance_pct": 29.9, "volume": 900, "magnitude": "HIGH"},
        {"strike": 500, "type": "put", "delta_oi": 2850, "last_price": 8.10,
         "notional": 2850 * 8.10 * 100, "distance_pct": -3.0, "volume": 2500, "magnitude": "HIGH"},
    ]
    sig = [
        {"strike": 575, "type": "call", "delta_oi": 7348, "last_price": 0.87,
         "notional": None, "distance_pct": 11.5, "volume": 5840, "magnitude": "HIGH", "r1": 125.8},
        {"strike": 500, "type": "put", "delta_oi": 2850, "last_price": 8.10,
         "notional": None, "distance_pct": -3.0, "volume": 2500, "magnitude": "HIGH", "r1": 114.0},
    ]
    snap = {"forward": {"expirations": [
        _fwd_exp("2026-09-18", 25, 5400, 800, "HIGH",
                 delta_exposure=1210000, top_delta_oi=top, significant=sig),
    ]}}
    text = "\n".join(_forward_block(snap))
    assert "09-18 Forward Structure" in text
    assert "OI:       C 42.8k / P 31.6k" in text
    assert "ΔOI:      C +5.4k / P +0.8k" in text
    assert "ATM:      C 5.84 / P 14.12" in text
    assert "ATM IV:   38.8%" in text
    assert "ΔOI Δ Exposure*: 1.2M shares" in text
    assert "C 575 ｜ +7,348 ｜ $0.87 ｜ 名义 $639.3k* ｜ +11.5%" in text
    assert "结构参考" in text and "形成 OI 变化集中区" in text
    assert "⚠️ Significant Forward Positioning" in text
    assert "ΔOI/Volume 126%" in text
    assert "不进入 Direction Edge / Gate" in text
    assert "买开/卖开方向不可观测" in text


def test_forward_block_new_strike_annotation():
    snap = {"forward": {"expirations": [
        _fwd_exp("2026-09-18", 25, 1000, 500, "HIGH",
                 call_new_oi=500, put_new_oi=300),
    ]}}
    text = "\n".join(_forward_block(snap))
    assert "（新行权价 C 0.5k / P 0.3k）" in text
    assert "ΔOI:      C +1.0k / P +0.5k（含新行权价 C 0.5k / P 0.3k）" in text


def test_ticker_morning_includes_forward_block():
    snap = load_fixture("snapshot_morning_soxx.json")
    snap["forward"] = {"expirations": [
        _fwd_exp("2026-09-18", 25, 5400, 800, "HIGH"),
    ]}
    text = ticker_morning(snap)
    assert "📆 Forward Expiration Structure" in text
    assert "09-18 Forward Structure" in text


def test_render_morning_stale_prev_snapshot():
    snap = load_fixture("snapshot_morning_soxx.json")
    prev = load_fixture("snapshot_evening_soxx.json")
    prev["created_at"] = "2026-08-11T16:30:00-04:00"  # 10 天前
    text = render_morning(snap, prev_snapshot=prev)
    assert "停更" in text and "个交易日" in text


def test_render_morning_stale_one_trading_day():
    snap = load_fixture("snapshot_morning_soxx.json")  # 2026-08-21
    prev = load_fixture("snapshot_evening_soxx.json")
    prev["created_at"] = "2026-08-19T16:30:00-04:00"  # 缺 8/20 → 停更 1 个交易日
    text = render_morning(snap, prev_snapshot=prev)
    assert "停更 1 个交易日" in text


def test_trading_gap_boundaries():
    assert _trading_gap("2026-08-24", "2026-08-27") == 2  # Mon→Thu：只计 Tue/Wed
    assert _trading_gap("2026-08-21", "2026-08-24") == 0  # Fri→Mon：周末不计
    assert _trading_gap("2026-08-19", "2026-08-21") == 1  # Wed→Fri：只计 Thu
    assert _trading_gap("bad-date", "2026-08-21") == 0   # 非法日期防御


def test_ticker_blocks_exclude_global_sections():
    morning = load_fixture("snapshot_morning_soxx.json")
    evening = load_fixture("snapshot_evening_soxx.json")
    m_text = ticker_morning(morning)
    e_text = ticker_evening(evening)
    assert "## SOXX" in m_text and "期权晨报" not in m_text and "市场背景" not in m_text
    assert "Thesis Scorecard" in e_text and "## SOXX" in e_text
    assert "期权晚报" not in e_text and "市场背景" not in e_text


def test_market_and_calendar_blocks():
    mb = market_block({"spy": 765.72, "vix": 15.13, "fg_score": 45, "fg_rating": "中性"})
    assert mb and "CNN 恐惧贪婪 45（中性）" in mb[0]
    cb = calendar_block(["- 测试日历行"])
    assert cb and "宏观日历" in cb[0] and "测试日历行" in cb[1]
    assert market_block(None) == []
    assert calendar_block(None) == []
