# -*- coding: utf-8 -*-
from engine.annotations import (
    assert_no_direction_words,
    completeness,
    event_annotation,
    event_card,
    event_magnitude,
    options_annotation,
)


def test_options_annotation_fact_only():
    lines = options_annotation(3.10, 0.70)
    assert len(lines) == 4
    assert "3.10×" in lines[0]
    assert "方向 Unknown" in lines[0]
    assert "Call-dominant" in lines[1]
    assert "两者结构不一致" in lines[2]
    assert "当日成交 vs 存量仓位" in lines[3]
    assert all(assert_no_direction_words(l) for l in lines)


def test_options_annotation_balanced_band():
    lines = options_annotation(1.05, 2.13)
    assert "Put 与 Call 成交量接近" in lines[0]
    assert "存量 Put 仓位高于 Call" in lines[1]
    # 成交均衡时不输出"两者结构不一致/一致"（无方向可比）
    assert len(lines) == 3
    assert "当日成交接近均衡，存量Put-dominant" in lines[2]
    assert "显著" not in "".join(lines)
    assert all(assert_no_direction_words(l) for l in lines)


def test_options_annotation_call_heavy_band():
    lines = options_annotation(0.62, 0.79)
    assert "Call 成交量高于 Put" in lines[0]
    assert "存量 Call 仓位高于 Put" in lines[1]
    assert "当日成交偏 Call，存量Call-dominant" in lines[3]


def test_magnitude_low_medium_high():
    low = event_magnitude(5000, 5000, 5030)  # r1=0.6%、r2=0.6%、r3=30 → 低
    assert low["magnitude"] == "LOW"
    med = event_magnitude(900, 2945, 3020)  # r1=8.3%、r2=2.5%、r3=75 → 中
    assert med["magnitude"] == "MEDIUM"
    high = event_magnitude(2000, 100, 700)  # r1=30%、r2=600%、r3=600 → 高
    assert high["magnitude"] == "HIGH"


def test_completeness():
    assert completeness(True, True, True, True) == "HIGH"
    assert completeness(True, False, True, True) == "LOW"
    assert completeness(True, True, False, True) == "LOW"


def test_event_annotation_no_direction_words():
    a = event_annotation(900, 2945, 3020, "MEDIUM", "HIGH")
    assert "值得跟踪（方向未知）" in a
    assert assert_no_direction_words(a)
    b = event_annotation(2121, 152, 189, "LOW", "HIGH")
    assert assert_no_direction_words(b)


def test_event_card_shape():
    lines = event_card("8/24 500P", 900, 2945, 3020)
    assert "Magnitude: MEDIUM" in lines[0]
    assert "ΔOI/Volume 8.3%" in lines[0]
    assert lines[1].startswith("   ⇒ ")


def test_event_card_filled_volume_and_price():
    """B 方案：CBOE 缺量时 yfinance 补量并标来源，同时显示最新价。"""
    lines = event_card(
        "8/28 505P", 18281, 162, 18399,
        has_prev_vol=False, last_price=0.01, vol_source="yfinance",
    )
    assert "Vol 18,281（Yahoo补）" in lines[0]
    assert "最新价 $0.01" in lines[0]
    assert "ΔOI/Volume 99.8%" in lines[0]


def test_delta_computed_without_volume():
    m = event_magnitude(None, 337, 7685)
    assert m["delta_oi"] == 7348
    assert m["r1"] is None
    assert m["magnitude"] == "HIGH"  # r2=2180%、r3=7348


def test_r1_none_when_volume_incomplete():
    # |ΔOI| 不可能超过当日成交量：OI +14003 但成交量仅 8 → 量数据不完整
    m = event_magnitude(8, 225, 14228)
    assert m["r1"] is None
    assert m["delta_oi"] == 14003
    # 量缺失不影响发现：由 r2（ΔOI/前日OI）与 r3（绝对张数）支撑 HIGH
    assert m["magnitude"] == "HIGH"
    lines = event_card("QQQ260930P00687000", 8, 225, 14228, has_prev_vol=False)
    assert "ΔOI/Volume N/A（量数据不完整）" in lines[0]
    # 正常情形不受影响
    ok = event_magnitude(2000, 100, 700)
    assert ok["r1"] == 30.0


def test_low_magnitude_without_volume_no_crash():
    a = event_annotation(None, 5000, 5016, "LOW", "LOW")  # r1=None → 低等级
    assert "量数据缺失" in a
    assert assert_no_direction_words(a)


def test_medium_high_without_prev_oi_no_crash():
    # r2=None（前日OI缺失）时 MEDIUM/HIGH 注解不能崩
    m_med = event_annotation(900, None, 3020, "MEDIUM", "HIGH")
    assert "前日OI缺失" in m_med
    assert assert_no_direction_words(m_med)
    m_high = event_annotation(2000, None, 700, "HIGH", "HIGH")
    assert "前日OI缺失" in m_high
    assert assert_no_direction_words(m_high)


def test_zero_net_change_annotation():
    a = event_annotation(1000, 5000, 5000, "LOW", "HIGH")  # ΔOI=0
    assert "净变动为0" in a
    assert assert_no_direction_words(a)
