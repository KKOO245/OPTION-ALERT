# -*- coding: utf-8 -*-
from report.format import code_block, table, ticker_heading
from report.morning import render_morning
from report.evening import render_evening
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
