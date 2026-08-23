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
    assert len(lines) == 3
    assert "3.10×" in lines[0]
    assert "方向 Unknown" in lines[0]
    assert "Call-dominant" in lines[1]
    assert "两者结构不一致" in lines[2]
    assert all(assert_no_direction_words(l) for l in lines)


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


def test_delta_computed_without_volume():
    m = event_magnitude(None, 337, 7685)
    assert m["delta_oi"] == 7348
    assert m["r1"] is None
    assert m["magnitude"] == "HIGH"  # r2=2180%、r3=7348


def test_low_magnitude_without_volume_no_crash():
    a = event_annotation(None, 5000, 5016, "LOW", "LOW")  # r1=None → 低等级
    assert "量数据缺失" in a
    assert assert_no_direction_words(a)
