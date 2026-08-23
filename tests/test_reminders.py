# -*- coding: utf-8 -*-
import datetime

from src.reminders import evening_reminder_lines, is_first_business_day


def test_first_business_day():
    # 2026-08-01 周六、08-02 周日 → 08-03 周一才是第一个工作日
    assert is_first_business_day(datetime.date(2026, 8, 3)) is True
    assert is_first_business_day(datetime.date(2026, 8, 4)) is False
    assert is_first_business_day(datetime.date(2026, 9, 1)) is True  # 周二
    assert is_first_business_day(datetime.date(2026, 8, 2)) is False  # 周日


def test_friday_reminder():
    lines = evening_reminder_lines(datetime.datetime(2026, 8, 21, 17, 0))  # 周五
    assert any("每周本地备份提醒" in l for l in lines)
    assert "git pull" in lines[0]


def test_no_reminder_on_plain_thursday():
    lines = evening_reminder_lines(datetime.datetime(2026, 8, 20, 17, 0))  # 周四
    assert lines == []


def test_monthly_reminder_on_first_business_day():
    lines = evening_reminder_lines(datetime.datetime(2026, 9, 1, 17, 0))  # 周二
    assert any("月度归档提醒" in l for l in lines)


def test_both_reminders_on_friday_first_business_day():
    lines = evening_reminder_lines(datetime.datetime(2026, 5, 1, 17, 30))  # 周五且当月第一个工作日
    assert any("每周本地备份提醒" in l for l in lines)
    assert any("月度归档提醒" in l for l in lines)
