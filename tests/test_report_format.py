# -*- coding: utf-8 -*-
from report.format import code_block, table, ticker_heading
from report.evening import render_evening, ticker_evening
from report.morning import (
    _forward_block,
    _is_low_relevance,
    _relevant_top,
    _structure_interpretation,
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
    # 无 Setup 触发时诚实显示"无待验证 Target"（不再用占位 PENDING 文案）
    assert "Target" in text
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


def test_market_block_vol_regime_insufficient():
    ve_env = {
        "vix": {"value": 15.85, "change_1d_pct": -0.6, "change_5d_pct": -0.5},
        "regime": {"label": "INSUFFICIENT_DATA"},
    }
    market = {"spy": 765.19, "qqq": 709.24, "fg_score": 58, "fg_rating": "greed", "vol_environment": ve_env}
    text = "\n".join(market_block(market))
    assert "Vol Regime: INSUFFICIENT_DATA ⚠️" in text
    assert "Vol Regime unavailable: rule evaluation incomplete." in text


def test_structure_block_gamma_gex_semantics_and_flip_status():
    snap = load_fixture("snapshot_morning_soxx.json")
    text = ticker_morning(snap)
    assert "Gamma Regime: NEGATIVE（模型分类）" in text
    assert "不对 Gamma 强度做判断" in text
    assert "Flip: Candidates 502.00 / 530.00 ｜ Primary: N/A（CONDITIONAL）" in text
    assert "结构观察区: 502–530" in text
    assert "测量完整性" in text and "gex_sign_v1" in text
    assert "最近结构参考" in text


def test_structure_block_gex_from_p3():
    snap = load_fixture("snapshot_morning_soxx.json")
    snap["p3"] = {
        "schema_version": "p3_collect_v1",
        "gex": {"net_gex": -123456789.0, "abs_gex": 123456789.0,
                "n_used": 100, "n_skipped": 10, "spot_zone": "NEGATIVE"},
        "coverage": {"effective_gex_coverage_pct": 95.0},
    }
    text = ticker_morning(snap)
    assert "GEX(存量) -123,456,789" in text


def test_structure_block_gex_change_vs_prev_snapshot():
    snap = load_fixture("snapshot_morning_soxx.json")
    snap["p3"] = {"gex": {"net_gex": 1000.0}}
    prev = load_fixture("snapshot_morning_soxx.json")
    prev["p3"] = {"gex": {"net_gex": 800.0}}
    text = ticker_morning(snap, prev_snapshot=prev)
    assert "GEX Change vs 上次快照 200" in text


def test_options_line_expmove_matches_nearest_expiry():
    snap = load_fixture("snapshot_morning_soxx.json")
    snap["forward"] = {"expirations": [
        _fwd_exp("2026-08-28", 2, 1000, 500, "LOW", atm_iv=0.94,
                 atm_call_price=6.23, atm_put_price=5.93),
    ]}
    snap["forward"]["expirations"][0]["expmove_pct"] = round((6.23 + 5.93) / 497.2 * 100.0, 2)
    text = ticker_morning(snap)
    # Options 行 ExpMove 与 ExpMove 期限化行同源（最近期限 ±2.5%）
    assert "ExpMove ±2.5%（近端）" in text
    assert "ExpMove 期限化（expmove_v1）" in text
    assert "08-28（2D）±2.5%" in text

    snap2 = load_fixture("snapshot_morning_soxx.json")
    snap2["location"]["flip_levels"] = None
    snap2["location"]["flip_candidates"] = None
    snap2["location"]["flip_status"] = "NO_CROSS"
    text2 = ticker_morning(snap2)
    assert "结构观察区: NO_CROSS" in text2
    assert "Flip: NO_CROSS" in text2


def test_ticker_morning_expmove_tenor_line():
    snap = load_fixture("snapshot_morning_soxx.json")
    snap["forward"] = {"expirations": [
        _fwd_exp("2026-08-28", 2, 1000, 500, "LOW", atm_iv=0.94,
                 atm_call_price=6.23, atm_put_price=5.93),
        _fwd_exp("2026-09-04", 9, 2000, 1000, "LOW", atm_iv=0.54,
                 atm_call_price=7.45, atm_put_price=6.98),
    ]}
    # expmove_pct = (6.23+5.93)/497.2*100 ≈ 2.45；07.45+6.98)/497.2*100 ≈ 2.90
    snap["forward"]["expirations"][0]["expmove_pct"] = round((6.23 + 5.93) / 497.2 * 100.0, 2)
    snap["forward"]["expirations"][1]["expmove_pct"] = round((7.45 + 6.98) / 497.2 * 100.0, 2)
    text = ticker_morning(snap)
    assert "ExpMove 期限化（expmove_v1）" in text
    assert "08-28（2D）±2.5%" in text
    assert "09-04（9D）±2.9%" in text

    # 旧快照兜底：无 expmove_pct 字段时用 ATM C/P 与 spot 现算
    snap3 = load_fixture("snapshot_morning_soxx.json")
    snap3["forward"] = {"expirations": [
        _fwd_exp("2026-08-28", 2, 1000, 500, "LOW", atm_iv=0.94,
                 atm_call_price=6.23, atm_put_price=5.93),
    ]}
    text3 = ticker_morning(snap3)
    assert "08-28（2D）±2.5%" in text3


def test_ticker_morning_event_differential():
    snap = load_fixture("snapshot_morning_soxx.json")
    snap["forward"] = {"expirations": [
        _fwd_exp("2026-08-28", 2, 1000, 500, "LOW", atm_iv=0.94,
                 atm_call_price=6.23, atm_put_price=5.93),
        _fwd_exp("2026-09-04", 9, 2000, 1000, "LOW", atm_iv=0.54,
                 atm_call_price=7.45, atm_put_price=6.98),
    ]}
    event_dates = [
        {"date": "2026-08-28", "name": "美联储主席讲话", "time": "10:00"},
    ]
    text = ticker_morning(snap, event_dates=event_dates)
    assert "事件差分" in text
    assert "94.0%" in text and "54.0%" in text
    assert "美联储 IFDP 1376" in text
    assert "数据质量" in text


def test_render_highlights_at_report_top():
    snap = load_fixture("snapshot_morning_soxx.json")
    snap["forward"] = {"expirations": [
        _fwd_exp("2026-08-28", 2, 1000, 500, "LOW", atm_iv=0.94,
                 atm_call_price=6.23, atm_put_price=5.93),
        _fwd_exp("2026-09-04", 9, 2000, 1000, "LOW", atm_iv=0.54,
                 atm_call_price=7.45, atm_put_price=6.98),
    ]}
    event_dates = [{"date": "2026-08-28", "name": "美联储主席讲话", "time": "10:00"}]
    text = render_morning(snap, event_dates=event_dates, calendar=["- 周一 08-24　【高】测试事件"])
    # 重点速览位于宏观日历之后、ticker 区块之前
    assert "🔍 重点速览" in text and "🔴" in text
    assert text.index("宏观日历") < text.index("🔍 重点速览") < text.index("## SOXX")
    # ticker 区块内不再重复渲染重点速览
    ticker_part = text[text.index("## SOXX"):]
    assert "🔍 重点速览" not in ticker_part


def test_render_highlights_empty_state():
    snap = load_fixture("snapshot_morning_soxx.json")
    snap["momentum"]["price_momentum"] = 0.001  # 消除"单日价格波动"关注项，验证空态
    snap["location"]["flip_candidates"] = None
    snap["location"]["flip_levels"] = None
    snap["location"]["flip_status"] = "INSUFFICIENT_DATA"
    text = render_morning(snap)
    assert "今日无重点项" in text


def test_aggregate_highlights_ticker_prefix_and_order():
    from report.highlight import aggregate_highlights, highlights_section

    per = {
        "NVDA": [{"level": "INFO", "title": "Flip 状态", "detail": "CONDITIONAL", "reason": "r"}],
        "QQQ": [{"level": "CRITICAL", "title": "事件差分", "detail": "+30pp", "reason": "r2"}],
    }
    items, truncated = aggregate_highlights(per, max_items=10)
    assert not truncated
    assert items[0]["ticker"] == "QQQ" and items[0]["level"] == "CRITICAL"  # 关键级在前
    lines = "\n".join(highlights_section(items))
    assert "**QQQ ｜ 事件差分**" in lines
    assert "**NVDA ｜ Flip 状态**" in lines
    # 截断
    items2, truncated2 = aggregate_highlights(per, max_items=1)
    assert truncated2 and len(items2) == 1


def test_structure_block_primary_flip_and_coverage():
    snap = load_fixture("snapshot_morning_soxx.json")
    snap["location"]["flip_status"] = "PRIMARY"
    snap["location"]["flip_primary"] = 512.3
    snap["location"]["flip_reason"] = "full_chain_reprice_gate_pass"
    snap["location"]["flip_source"] = "full_chain"
    snap["p3"] = {
        "coverage": {
            "effective_gex_coverage_pct": 88.0,
            "iv_valid": {"VALID": 60, "LOW_LIQUIDITY": 5, "INVALID": 3},
        }
    }
    text = ticker_morning(snap)
    assert "Primary Flip: 512.30（PRIMARY，全链重定价 + 覆盖达标）" in text
    assert "Gamma 口径 全链重定价" in text
    assert "Effective GEX 覆盖: 88%（带内）" in text
    assert "IV 有效性: VALID 60 / LOW 5 / INVALID 3" in text
    # 全链口径下：结构观察区 / Gamma 区域不再出现 Top-3 近似文案
    assert "结构观察区: Primary Flip 512.30（全链重定价，覆盖 88%）" in text
    assert "Top-3 近似" not in text
    # 墙的距离标签改为明确方向
    assert "Put Wall 490（现价高于该位 1.5%）" in text
    assert "Call Wall 550（现价低于该位 9.6%）" in text
    assert "距现价 +" not in text


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


def test_activity_block_shows_filled_volume_and_price():
    events = [{
        "expiration": "2026-08-28",
        "strike": 505,
        "type": "put",
        "volume": 18281,
        "volume_prev": None,
        "oi_prev": 162,
        "open_interest": 18399,
        "last_price": 0.01,
        "volume_source": "yfinance",
    }]
    from report.morning import _activity_block

    text = "\n".join(_activity_block(events))
    assert "Vol 18,281（Yahoo补）" in text
    assert "最新价 $0.01" in text
    assert "OI 162→18399" in text


def test_evening_scorecard_high_low():
    snap = load_fixture("snapshot_evening_soxx.json")
    morning = load_fixture("snapshot_morning_soxx.json")
    text = ticker_evening(snap, morning=morning)
    assert "今日高 503.50" in text and "低 495.10" in text


def test_evening_scorecard_uses_day_open():
    snap = load_fixture("snapshot_evening_soxx.json")
    morning = load_fixture("snapshot_morning_soxx.json")
    morning["context"]["day_open"] = 500.0
    text = ticker_evening(snap, morning=morning)
    assert "今开 500.00 → 收盘" in text
    score_line = next(l for l in text.split("\n") if "→ 收盘" in l)
    assert "今开" in score_line and "今晨" not in score_line
    # 无 day_open 时回退"今晨"（晨报 spot）
    morning2 = load_fixture("snapshot_morning_soxx.json")
    text2 = ticker_evening(snap, morning=morning2)
    assert "今晨" in text2


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
    # 最近到期日（08-28，LOW）也强制完整展开；非最近 LOW 不展开
    assert "08-28 Forward Structure" in text
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
    assert "存量OI:      C 42.8k / P 31.6k" in text
    assert "今日变化ΔOI: C +5.4k / P +0.8k" in text
    assert "平值价格ATM:  C 5.84 / P 14.12" in text
    assert "隐含波动率 ATM IV:  38.8%" in text
    assert "ΔOI Δ Exposure*: 1.2M shares" in text
    assert "C 575 ｜ +7,348 ｜ $0.87 ｜ 名义 $639.3k* ｜ +11.5%" in text
    assert "结构参考" in text and "形成 OI 变化集中区" in text
    # v1 不渲染 L3（未验证的经验阈值堆叠，后台计算但不上报告）
    assert "Significant Forward Positioning" not in text
    assert "ΔOI/Volume 126%" not in text
    assert "买开/卖开方向不可观测" in text


def test_forward_block_medium_compact_top():
    top = [
        {"strike": 700, "type": "call", "delta_oi": 1800, "last_price": 3.2,
         "notional": None, "distance_pct": -0.9, "volume": 500, "magnitude": "HIGH"},
        {"strike": 690, "type": "put", "delta_oi": 900, "last_price": 3.0,
         "notional": None, "distance_pct": -2.3, "volume": 400, "magnitude": "HIGH"},
        {"strike": 710, "type": "call", "delta_oi": 700, "last_price": 2.5,
         "notional": None, "distance_pct": 0.5, "volume": 300, "magnitude": "MEDIUM"},
    ]
    snap = {"forward": {"expirations": [
        _fwd_exp("2026-08-28", 4, 800, 200, "LOW"),
        _fwd_exp("2026-09-04", 11, 3100, 2100, "MEDIUM", top_delta_oi=top),
    ]}}
    text = "\n".join(_forward_block(snap))
    # MEDIUM 非最近到期日：一行紧凑 Top ΔOI，且带日期标签（不再是无主孤儿行）
    assert "09-04（MEDIUM △）Top ΔOI: 700C +1,800 ｜ 690P +900" in text
    assert "09-04 Forward Structure" not in text
    # 最近到期日（08-28，LOW）强制完整展开
    assert "08-28 Forward Structure" in text


def test_forward_block_nearest_expands_even_if_low():
    """最近到期日无论 Activity 级别都渲染完整块；其余 LOW 不展开。"""
    snap = {"forward": {"expirations": [
        _fwd_exp("2026-08-28", 4, 2100, 300, "LOW"),
        _fwd_exp("2026-09-04", 11, 3100, 2100, "LOW"),
    ]}}
    text = "\n".join(_forward_block(snap))
    assert "08-28 Forward Structure" in text
    assert "09-04 Forward Structure" not in text


def test_structure_interpretation_shows_max_pain():
    """Max Pain 接线：快照 context.max_pain 进入结构解读（仅结算参考，不参与方向）。"""
    snap = load_fixture("snapshot_morning_soxx.json")
    snap["context"]["max_pain"] = 500.0
    joined = "\n".join(_structure_interpretation(snap))
    assert "500（MaxPain，仅结算参考）" in joined


def test_low_relevance_and_rule_no_good_data_kill():
    """彩票判据（AND）：名义<$50k 且 距现价>10% 才算彩票——绝不误杀近月好数据。"""
    near_cheap = {"strike": 3.0, "type": "call", "delta_oi": 5000, "last_price": 0.10,
                  "notional": 5000 * 0.10 * 100.0, "distance_pct": 2.0}
    far_cheap = {"strike": 100.0, "type": "put", "delta_oi": 9999, "last_price": 0.01,
                 "notional": 9999 * 0.01 * 100.0, "distance_pct": -30.0}
    far_big = {"strike": 100.0, "type": "put", "delta_oi": 100000, "last_price": 0.03,
               "notional": 100000 * 0.03 * 100.0, "distance_pct": -30.0}
    # 近月便宜（标的便宜，不是彩票）→ 保留
    assert _is_low_relevance(near_cheap) is False
    # 远端便宜（真彩票）→ 过滤
    assert _is_low_relevance(far_cheap) is True
    # 远端但大额累计（$30万）→ 保留（不误杀）
    assert _is_low_relevance(far_big) is False
    # _relevant_top 过滤行为一致
    top = [near_cheap, far_cheap, far_big]
    kept = _relevant_top(top)
    assert len(kept) == 2 and all(t is not far_cheap for t in kept)


def test_forward_block_new_strike_annotation():
    snap = {"forward": {"expirations": [
        _fwd_exp("2026-09-18", 25, 1000, 500, "HIGH",
                 call_new_oi=500, put_new_oi=300),
    ]}}
    text = "\n".join(_forward_block(snap))
    assert "（新行权价 C 0.5k / P 0.3k）" in text
    assert "今日变化ΔOI: C +1.0k / P +0.5k（含新行权价 C 0.5k / P 0.3k）" in text


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
