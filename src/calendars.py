# -*- coding: utf-8 -*-
"""
日历层（v3）
------------
每周二/周四早报附带：
1. 宏观日历：美国高重要性数据（美联储会议、CPI/PPI、非农、失业率等）
   来源：TradingView 经济日历公开接口（免费、无需 key，个人研究）
2. 财报日历：当周重要公司财报日期
   来源：Yahoo Finance（yfinance），监控名单见 config/earnings_watchlist.txt
"""

import datetime
import os
from zoneinfo import ZoneInfo

import requests

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EARNINGS_FILE = os.path.join(BASE_DIR, "config", "earnings_watchlist.txt")

ET = ZoneInfo("America/New_York")

TV_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Origin": "https://www.tradingview.com",
    "Referer": "https://www.tradingview.com/economic-calendar/",
}
TV_URL = "https://economic-calendar.tradingview.com/events"

# 常见重要宏观事件的中文名映射（没匹配到的保留英文原名）
MACRO_NAMES = {
    "fomc": "美联储议息会议",
    "fed funds rate": "美联储利率决议",
    "interest rate": "美联储利率决议",
    "nonfarm payrolls": "非农就业",
    "non-farm payrolls": "非农就业",
    "unemployment rate": "失业率",
    "cpi": "CPI 通胀",
    "core cpi": "核心 CPI",
    "ppi": "PPI 生产者物价",
    "core ppi": "核心 PPI",
    "gdp": "GDP",
    "pce": "PCE 物价",
    "retail sales": "零售销售",
    "housing starts": "新屋开工",
    "building permits": "建筑许可",
    "new home sales": "新屋销售",
    "existing home sales": "成屋销售",
    "consumer confidence": "消费者信心",
    "michigan": "密歇根消费者信心",
    "ism manufacturing": "ISM 制造业",
    "ism services": "ISM 非制造业",
    "durable goods": "耐用品订单",
    "initial jobless claims": "初请失业金",
    "jobless claims": "初请失业金",
    "jolts": "职位空缺(JOLTS)",
    "average hourly earnings": "平均时薪",
    "trade balance": "贸易帐",
    "industrial production": "工业生产",
    "capacity utilization": "产能利用率",
    "philadelphia fed": "费城联储制造业",
    "empire state": "纽约联储制造业",
    "treasury budget": "联邦财政预算",
    "current account": "经常帐",
    "consumer price index": "CPI 通胀",
    "producer price index": "PPI 生产者物价",
    "fed chair": "美联储主席讲话",
    "beige book": "美联储褐皮书",
    "gdp growth": "GDP 增速",
}

WEEKDAYS = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]


def _translate_macro(name):
    low = (name or "").lower()
    for key, zh in MACRO_NAMES.items():
        if key in low:
            return zh
    return name or "宏观数据"


def _week_range(now):
    """返回本周一 00:00 ~ 本周日 23:59（美东时间）"""
    start = now.date() - datetime.timedelta(days=now.weekday())
    end = start + datetime.timedelta(days=6)
    return start, end


def fetch_macro_calendar(week_start, week_end):
    """抓本周美国高重要性宏观事件，返回按时间排序的列表"""
    from_dt = datetime.datetime.combine(week_start, datetime.time.min, tzinfo=ET)
    to_dt = datetime.datetime.combine(week_end, datetime.time.max, tzinfo=ET)
    body = {
        "filter": [],
        "range": {
            "from": from_dt.isoformat(),
            "to": to_dt.isoformat(),
        },
        "columns": ["title", "country", "date", "importance",
                    "actual", "forecast", "previous"],
    }
    r = requests.post(TV_URL, headers=TV_HEADERS, json=body, timeout=40)
    r.raise_for_status()
    result = (r.json() or {}).get("result") or []

    events = []
    for e in result:
        if e.get("country") != "US" or e.get("importance") != 1:
            continue
        raw_date = e.get("date")
        if not raw_date:
            continue
        try:
            dt = datetime.datetime.fromisoformat(raw_date.replace("Z", "+00:00"))
            dt = dt.astimezone(ET)
        except ValueError:
            continue
        events.append({
            "date": dt.date(),
            "time": dt.strftime("%H:%M"),
            "name": _translate_macro(e.get("title") or ""),
        })
    events.sort(key=lambda x: (x["date"], x["time"]))
    return events


def load_earnings_watchlist():
    """读取 config/earnings_watchlist.txt：每行「代码,中文名」"""
    out = []
    if not os.path.exists(EARNINGS_FILE):
        return out
    with open(EARNINGS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = [p.strip() for p in line.split(",")]
            ticker = parts[0].upper()
            name = parts[1] if len(parts) > 1 else ticker
            if ticker:
                out.append((ticker, name))
    return out


def fetch_earnings_calendar(watchlist, week_start, week_end):
    """抓白名单里当周有财报的公司，返回按日期排序的列表"""
    import yfinance as yf

    out = []
    for ticker, name in watchlist:
        try:
            cal = yf.Ticker(ticker).calendar
            dates = cal.get("Earnings Date") if isinstance(cal, dict) else None
            if not dates:
                continue
            for d in dates:
                if isinstance(d, datetime.datetime):
                    d = d.date()
                if isinstance(d, datetime.date) and week_start <= d <= week_end:
                    out.append({"ticker": ticker, "name": name, "date": d})
        except Exception as e:
            print(f"[警告] 财报日历 {ticker} 获取失败: {e}")
    out.sort(key=lambda x: (x["date"], x["ticker"]))
    return out


def _fmt_event_date(d):
    return f"{WEEKDAYS[d.weekday()]} {d.month:02d}-{d.day:02d}"


def build_calendar_sections(now):
    """周二/周四早报用：返回 [宏观日历段, 财报日历段]"""
    week_start, week_end = _week_range(now)
    sections = []

    macro_lines = ["## 📅 本周宏观日历（美国重要数据，美东时间）"]
    try:
        macro = fetch_macro_calendar(week_start, week_end)
        if not macro:
            macro_lines.append("- 本周暂无明显高重要性数据公布")
        for e in macro:
            note = ""
            if e["date"] == now.date():
                if e["time"] <= now.strftime("%H:%M"):
                    note = "　✅ 今日已公布"
                else:
                    note = "　⏰ 今日"
            macro_lines.append(f"- {_fmt_event_date(e['date'])} {e['time']}　{e['name']}{note}")
    except Exception as e:
        print(f"[警告] 宏观日历获取失败: {e}")
        macro_lines.append("- 宏观日历源暂时不可用（稍后自动恢复）")
    sections.append("\n".join(macro_lines))

    earn_lines = ["## 🏢 当周重要公司财报（日期以公司公告为准）"]
    try:
        watchlist = load_earnings_watchlist()
        earnings = fetch_earnings_calendar(watchlist, week_start, week_end)
        if not earnings:
            earn_lines.append("- 本周白名单公司暂无财报")
        for e in earnings:
            note = "　📌 今天" if e["date"] == now.date() else ""
            earn_lines.append(f"- {_fmt_event_date(e['date'])}　{e['name']} ({e['ticker']}){note}")
    except Exception as e:
        print(f"[警告] 财报日历获取失败: {e}")
        earn_lines.append("- 财报日历源暂时不可用（稍后自动恢复）")
    sections.append("\n".join(earn_lines))

    return sections
