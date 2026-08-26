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

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EARNINGS_FILE = os.path.join(BASE_DIR, "config", "earnings_watchlist.txt")

try:
    ET = ZoneInfo("America/New_York")
except Exception:
    # 极少数环境缺少 tzdata（如部分精简 Python）；生产（GitHub runner）正常使用美东时间
    ET = datetime.timezone.utc

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
    "import prices": "进口价格",
    "export prices": "出口价格",
    "industrial production": "工业生产",
    "pending home sales": "成屋待完成销售",
    "adp employment": "ADP 就业",
    "api crude oil": "API 原油库存",
    "redbook": "红皮书零售",
    "capacity utilization": "产能利用率",
    "housing starts": "新屋开工",
    "building permits": "建筑许可",
}

WEEKDAYS = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]


def _translate_macro(name):
    low = (name or "").lower()
    # 长的关键词优先匹配（如 core cpi 先于 cpi）
    for key, zh in sorted(MACRO_NAMES.items(), key=lambda kv: -len(kv[0])):
        pos = low.find(key)
        if pos >= 0:
            tail = (name or "")[pos + len(key):].strip()
            return zh + (" " + tail if tail else "")
    return name or "宏观数据"


def _week_range(now):
    """返回本周一 00:00 ~ 本周日 23:59（美东时间）"""
    start = now.date() - datetime.timedelta(days=now.weekday())
    end = start + datetime.timedelta(days=6)
    return start, end


def _norm_importance(v):
    """TradingView importance：-1 低 / 0 中 / 1 高。

    兼容 int、数字字符串，以及接口可能返回的 'High'/'Medium'/'Low' 字符串。
    """
    if isinstance(v, str):
        low = v.strip().lower()
        if low in ("high",):
            return 1
        if low in ("medium",):
            return 0
        if low in ("low",):
            return -1
    try:
        return int(v)
    except (TypeError, ValueError):
        return 0


def _is_us(e):
    """兼容接口可能返回的国别写法（US / USA / United States）。"""
    return str(e.get("country") or "").strip().upper() in ("US", "USA", "UNITED STATES")


def fetch_macro_calendar(week_start, week_end, high_only=False):
    """抓本周美国宏观事件（含预测值、实际值、前值），按时间排序。

    TradingView 经济日历页面实际使用的接口是 GET：
      https://economic-calendar.tradingview.com/events?minImportance=1&from=...&to=...&currencies=USD
    （该请求格式由 urlscan 对 tradingview.com/widget/economic-calendar 的抓包确认）

    minImportance：-1 低 / 0 中 / 1 高。
    high_only=True 时只保留 importance == 1（【高】），此时接口按 minImportance=1 只取【高】；
    high_only=False 时按 minImportance=0 取【中】+【高】，由调用方自行过滤。
    """
    import requests

    from_dt = datetime.datetime.combine(week_start, datetime.time.min, tzinfo=ET).astimezone(datetime.timezone.utc)
    to_dt = datetime.datetime.combine(week_end, datetime.time.max, tzinfo=ET).astimezone(datetime.timezone.utc)
    params = {
        "minImportance": "1" if high_only else "0",
        "from": from_dt.strftime("%Y-%m-%dT%H:%M:%S.000Z"),
        "to": to_dt.strftime("%Y-%m-%dT%H:%M:%S.000Z"),
        "currencies": "USD",
    }
    r = requests.get(TV_URL, headers=TV_HEADERS, params=params, timeout=40)
    r.raise_for_status()
    data = r.json()
    if isinstance(data, dict):
        result = data.get("result") or []
    elif isinstance(data, list):
        result = data
    else:
        result = []

    if not result:
        print(
            f"[日历-raw] 接口返回空（GET minImportance={params['minImportance']}，"
            f"范围 {week_start}~{week_end}，currencies=USD）"
        )
    else:
        sample = result[:3]
        print(f"[日历-raw] 返回 {len(result)} 条；字段 keys={sorted(sample[0].keys())}")
        print(
            "[日历-raw] 样本 importance/country/date: "
            + "; ".join(
                f"{e.get('importance')!r}/{e.get('country')!r}/{str(e.get('date'))[:22]}"
                for e in sample
            )
        )

    events = []
    for e in result:
        imp = _norm_importance(e.get("importance"))
        if not _is_us(e) or imp < 0:
            continue
        if high_only and imp != 1:
            continue
        raw_date = e.get("date")
        if not raw_date:
            continue
        try:
            if isinstance(raw_date, (int, float)):
                # 兼容毫秒时间戳（如 1756051200000）
                dt = datetime.datetime.fromtimestamp(
                    raw_date / 1000.0, tz=datetime.timezone.utc
                )
            else:
                dt = datetime.datetime.fromisoformat(str(raw_date).replace("Z", "+00:00"))
            dt = dt.astimezone(ET)
        except ValueError:
            continue
        events.append({
            "date": dt.date(),
            "time": dt.strftime("%H:%M"),
            "name": _translate_macro(e.get("title") or ""),
            "importance": e.get("importance"),
            "actual": e.get("actual"),
            "forecast": e.get("forecast"),
            "previous": e.get("previous"),
        })
    events.sort(key=lambda x: (x["date"], x["time"]))
    if not events:
        print(
            f"[日历-raw] 未匹配到美国事件：接口返回 {len(result)} 条，"
            f"country 样本 {sorted({str(e.get('country')) for e in result})[:8]}，"
            f"importance 样本 {sorted({str(e.get('importance')) for e in result})[:8]}"
        )
    return events


def build_macro_lines(now):
    """每天晨/晚报用：返回 [今天, 本周日] 的【高】重要性美国宏观事件格式化行。"""
    week_start, week_end = _week_range(now)
    try:
        events = fetch_macro_calendar(week_start, week_end, high_only=False)
    except Exception as e:
        print(f"[警告] 宏观日历获取失败: {e}")
        return ["- 宏观日历源暂时不可用（稍后自动恢复）"]
    high = [e for e in events if _norm_importance(e.get("importance")) == 1]
    print(
        f"[日历] 本周美国事件 {len(events)} 个，其中【高】{len(high)} 个 "
        f"（范围 {week_start}~{week_end}，importance=-1低/0中/1高）"
    )
    today = now.date()
    lines = []
    for e in high:
        if e["date"] < today:
            continue
        note = ""
        if e["date"] == today:
            note = "　✅ 今日已公布" if e["time"] <= now.strftime("%H:%M") else "　⏰ 今日"
        vals = []
        if e.get("forecast") is not None:
            vals.append(f"预测 {e['forecast']}")
        vals.append(f"实际 {e['actual']}" if e.get("actual") is not None else "实际 待公布")
        if e.get("previous") is not None:
            vals.append(f"前值 {e['previous']}")
        lines.append(
            f"- {_fmt_event_date(e['date'])} {e['time']}　【高】{e['name']}　{' ｜ '.join(vals)}{note}"
        )
    if not lines:
        lines.append("- 本周剩余时间暂无【高】重要性美国数据公布")
    return lines


def macro_event_dates(now):
    """本周剩余【高】美国事件的结构化日期列表（供事件差分使用）。

    返回 [{"date": "YYYY-MM-DD", "name": str, "time": "HH:MM"}, ...]；
    抓取失败返回 []（事件差分层缺输入时自动沉默，不编造）。
    """
    week_start, week_end = _week_range(now)
    try:
        events = fetch_macro_calendar(week_start, week_end, high_only=True)
    except Exception as e:
        print(f"[警告] 宏观日历获取失败（事件差分）: {e}")
        return []
    today = now.date()
    out = []
    for e in events:
        if e["date"] < today:
            continue
        out.append({"date": e["date"].isoformat(), "name": e["name"], "time": e["time"]})
    out.sort(key=lambda x: (x["date"], x["time"]))
    return out


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
            macro_lines.append("- 本周暂无高/中重要性数据公布")
        for e in macro:
            note = ""
            if e["date"] == now.date():
                if e["time"] <= now.strftime("%H:%M"):
                    note = "　✅ 今日已公布"
                else:
                    note = "　⏰ 今日"
            imp_tag = "【高】" if _norm_importance(e.get("importance")) == 1 else "【中】"
            vals = []
            if e.get("forecast") is not None:
                vals.append(f"预测 {e['forecast']}")
            if e.get("actual") is not None:
                vals.append(f"实际 {e['actual']}")
            else:
                vals.append("实际 待公布")
            if e.get("previous") is not None:
                vals.append(f"前值 {e['previous']}")
            vals_txt = " ｜ ".join(vals)
            macro_lines.append(
                f"- {_fmt_event_date(e['date'])} {e['time']}　{imp_tag}{e['name']}　{vals_txt}{note}"
            )
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
