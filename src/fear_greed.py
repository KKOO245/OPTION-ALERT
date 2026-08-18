# -*- coding: utf-8 -*-
"""
市场情绪：CNN 恐惧贪婪指数（Fear & Greed Index）
-----------------------------------------------
用户提到的"BBC Fear & Greed"页面实际是 CNN 的指数（很多新闻页内嵌它）。
数据源：CNN 官方公开接口 production.dataviz.cnn.io，免费、无需 key。
返回当天分值 + 昨收，晨报用；不需要实时，但接口给的就是当天实时值。
"""

import requests

URL = "https://production.dataviz.cnn.io/index/fearandgreed/graphdata"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0 Safari/537.36",
    "Referer": "https://www.cnn.com/markets/fear-and-greed",
    "Accept": "application/json, text/plain, */*",
}

RATING_ZH = {
    "extreme_fear": "极度恐惧",
    "fear": "恐惧",
    "neutral": "中性",
    "greed": "贪婪",
    "extreme_greed": "极度贪婪",
}


def fetch_fear_greed():
    """返回 {score, rating, previous_close, timestamp}，失败返回 None"""
    try:
        r = requests.get(URL, headers=HEADERS, timeout=30)
        r.raise_for_status()
        fg = (r.json() or {}).get("fear_and_greed") or {}
        score = fg.get("score")
        if score is None:
            return None
        return {
            "score": round(float(score), 1),
            "rating": fg.get("rating"),
            "previous_close": fg.get("previous_close"),
            "timestamp": fg.get("timestamp"),
        }
    except Exception as e:
        print(f"[警告] 恐惧贪婪指数获取失败: {type(e).__name__}: {e}")
        return None


def format_fear_greed(fg):
    if not fg:
        return None
    zh = RATING_ZH.get(fg.get("rating"), fg.get("rating") or "未知")
    prev = fg.get("previous_close")
    prev_txt = f"，昨收 {float(prev):.1f}" if prev is not None else ""
    return f"恐惧贪婪指数 {fg['score']}（{zh}{prev_txt}）"
