# -*- coding: utf-8 -*-
import datetime
import sys
from types import ModuleType

from src import calendars


def _fake_fetch(*a, **k):
    return [
        {"date": datetime.date(2026, 8, 24), "time": "10:30", "name": "CPI 通胀",
         "importance": 1, "forecast": "0.2%", "actual": None, "previous": "0.3%"},
        {"date": datetime.date(2026, 8, 25), "time": "14:00", "name": "美联储利率决议",
         "importance": 1, "forecast": None, "actual": None, "previous": None},
        {"date": datetime.date(2026, 8, 21), "time": "20:00", "name": "上周旧事件",
         "importance": 1, "forecast": None, "actual": None, "previous": None},
        {"date": datetime.date(2026, 8, 26), "time": "09:00", "name": "中等重要性事件",
         "importance": 0, "forecast": None, "actual": None, "previous": None},
        {"date": datetime.date(2026, 8, 27), "time": "08:30", "name": "字符串高重要性事件",
         "importance": "1", "forecast": None, "actual": None, "previous": None},
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
    assert not any("中等重要性事件" in l for l in lines)  # importance=0 不显示
    assert any("字符串高重要性事件" in l for l in lines)  # 字符串 "1" 也按【高】处理
    assert any("⏰ 今日" in l for l in lines)


def test_build_macro_lines_empty():
    original = calendars.fetch_macro_calendar
    calendars.fetch_macro_calendar = lambda *a, **k: []
    try:
        lines = calendars.build_macro_lines(datetime.datetime(2026, 8, 24, 9, 0))
    finally:
        calendars.fetch_macro_calendar = original
    assert lines and "暂无" in lines[0]


def test_us_country_variants():
    assert calendars._is_us({"country": "US"})
    assert calendars._is_us({"country": "USA"})
    assert calendars._is_us({"country": "United States"})
    assert calendars._is_us({"country": "DE"}) is False
    assert calendars._is_us({}) is False


def test_norm_importance_variants():
    assert calendars._norm_importance(1) == 1
    assert calendars._norm_importance("1") == 1
    assert calendars._norm_importance("1.0") == 0  # 无法解析时按非高处理
    assert calendars._norm_importance(0) == 0
    assert calendars._norm_importance(-1) == -1
    assert calendars._norm_importance(None) == 0
    assert calendars._norm_importance("High") == 1
    assert calendars._norm_importance("Medium") == 0
    assert calendars._norm_importance("Low") == -1


def test_fetch_macro_calendar_uses_get_with_params():
    """接口必须是 GET + minImportance/from/to/currencies=USD（TradingView 日历页真实请求格式）。"""
    captured = {}

    class FakeResp:
        def raise_for_status(self):
            return None

        def json(self):
            return {
                "result": [
                    {
                        "title": "Core PCE Price Index",
                        "country": "US",
                        "date": "2026-08-26T12:30:00.000Z",
                        "importance": 1,
                        "actual": None,
                        "forecast": "0.2%",
                        "previous": "0.1%",
                    }
                ]
            }

    def fake_get(url, headers=None, params=None, timeout=None):
        captured["url"] = url
        captured["headers"] = headers
        captured["params"] = params
        return FakeResp()

    fake_requests = ModuleType("requests")
    fake_requests.get = fake_get
    original = sys.modules.get("requests")
    sys.modules["requests"] = fake_requests
    try:
        events = calendars.fetch_macro_calendar(
            datetime.date(2026, 8, 24), datetime.date(2026, 8, 30), high_only=False
        )
    finally:
        if original is None:
            sys.modules.pop("requests", None)
        else:
            sys.modules["requests"] = original

    assert captured["url"] == calendars.TV_URL
    assert captured["params"]["minImportance"] == "0"
    assert captured["params"]["currencies"] == "USD"
    assert captured["params"]["from"].endswith(".000Z")
    assert captured["params"]["to"].endswith(".000Z")
    assert len(events) == 1
    assert "PCE 物价" in events[0]["name"]
    assert events[0]["importance"] == 1
