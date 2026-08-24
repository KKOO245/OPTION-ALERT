# -*- coding: utf-8 -*-
import datetime

from src import calendars


def _fake_fetch(*a, **k):
    return [
        {"date": datetime.date(2026, 8, 24), "time": "10:30", "name": "CPI 通胀",
         "importance": 1, "forecast": "0.2%", "actual": None, "previous": "0.3%"},
        {"date": datetime.date(2026, 8, 25), "time": "14:00", "name": "美联储利率决议",
         "importance": 1, "forecast": None, "actual": None, "previous": None},
        {"date": datetime.date(2026, 8, 21), "time": "20:00", "name": "上周旧事件",
         "importance": 1, "forecast": None, "actual": None, "previous": None},
    ]


def test_build_macro_lines_rest_of_week():
    original = calendars.fetch_macro_calendar
    calendars.fetch_macro_calendar = _fake_fetch
    try:
        lines = calendars.build_macro_lines(datetime.datetime(2026, 8, 24, 9, 0))
    finally:
        calendars.fetch_macro_calendar = original
    assert any("CPI 通胀" in l and "预测 0.2%" in l and "实际 待公布" in l and "前值 0.3%" in l for l in lines)
    assert any("美联储利率决议" in l for l in lines)
    assert not any("上周旧事件" in l for l in lines)  # 早于今天的事件不显示
    assert any("⏰ 今日" in l for l in lines)


def test_build_macro_lines_empty():
    original = calendars.fetch_macro_calendar
    calendars.fetch_macro_calendar = lambda *a, **k: []
    try:
        lines = calendars.build_macro_lines(datetime.datetime(2026, 8, 24, 9, 0))
    finally:
        calendars.fetch_macro_calendar = original
    assert lines and "暂无" in lines[0]
