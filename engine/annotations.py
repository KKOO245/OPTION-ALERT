# -*- coding: utf-8 -*-
"""注解引擎（P0.3 规格 v1 + v10.1c）。

规则：
  - Options 注解三段式纯事实，方向一律 Unknown。
  - 事件卡：Vol | OI 前→现（ΔOI 张）| ΔOI/Volume % | Magnitude | 完整度 + 注解。
  - Magnitude 复合计分：r1=ΔOI/Volume、r2=ΔOI/前日OI、r3=|ΔOI| 张数。
  - 完整度：今量+昨量+昨OI+今OI 全有=HIGH；缺昨值=LOW；其余=MEDIUM。
  - 禁用词：买/卖（方向断言）、开仓/平仓（确认流）、看多/看空、偏空/偏多、避险买盘。
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

FORBIDDEN_WORDS = ("买", "卖", "开仓", "平仓", "看多", "看空", "偏空", "偏多", "避险买盘")
MAGNITUDE_DEFAULTS = {
    "r1_pct": {"low": 5, "high": 20},
    "r2_pct": {"low": 5, "high": 20},
    "oi_abs": {"low": 50, "high": 500},
}


def _pc_side(v: float) -> str:
    """P/C 方向分档（与注解口径一致）：>1.20 put / <0.80 call / 其余 balanced。"""
    if v > 1.20:
        return "put"
    if v < 0.80:
        return "call"
    return "balanced"


def assert_no_direction_words(text: str) -> bool:
    return not any(w in text for w in FORBIDDEN_WORDS)


def options_annotation(pc_vol: Optional[float], pc_oi: Optional[float]) -> List[str]:
    lines = []
    if pc_vol is not None:
        if pc_vol > 1.20:
            lines.append(f"Put/Call Volume: {pc_vol:.2f}×（Put 成交量高于 Call）→ 方向 Unknown")
        elif pc_vol < 0.80:
            lines.append(f"Put/Call Volume: {pc_vol:.2f}×（Call 成交量高于 Put）→ 方向 Unknown")
        else:
            lines.append(f"Put/Call Volume: {pc_vol:.2f}×（Put 与 Call 成交量接近）→ 方向 Unknown")
    else:
        lines.append("Put/Call Volume: 数据不足 → 方向 Unknown")
    if pc_oi is not None:
        if pc_oi > 1.20:
            lines.append(f"Put/Call OI: {pc_oi:.2f}×（存量 Put 仓位高于 Call）→ 存量 Put-dominant")
        elif pc_oi < 0.80:
            lines.append(f"Put/Call OI: {pc_oi:.2f}×（存量 Call 仓位高于 Put）→ 存量 Call-dominant")
        else:
            lines.append(f"Put/Call OI: {pc_oi:.2f}×（两侧接近均衡）")
    else:
        lines.append("Put/Call OI: 数据不足")
    if pc_vol is not None and pc_oi is not None:
        sv, so = _pc_side(pc_vol), _pc_side(pc_oi)
        if sv != "balanced" and so != "balanced":
            lines.append("两者结构不一致" if sv != so else "两者结构一致")
        vol_txt = {"put": "偏 Put", "call": "偏 Call", "balanced": "接近均衡"}[sv]
        oi_txt = {"put": "Put-dominant", "call": "Call-dominant", "balanced": "接近均衡"}[so]
        lines.append(f"当日成交 vs 存量仓位：当日成交{vol_txt}，存量{oi_txt}")
    return lines


def completeness(has_vol: bool, has_prev_vol: bool, has_prev_oi: bool, has_oi: bool) -> str:
    if has_vol and has_prev_vol and has_prev_oi and has_oi:
        return "HIGH"
    if not has_prev_vol or not has_prev_oi:
        return "LOW"
    return "MEDIUM"


def event_magnitude(
    vol: Optional[float],
    oi_prev: Optional[float],
    oi_now: Optional[float],
    thresholds: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    t = thresholds or MAGNITUDE_DEFAULTS
    r1_lo = t.get("r1_pct", {}).get("low", 5)
    r1_hi = t.get("r1_pct", {}).get("high", 20)
    r2_lo = t.get("r2_pct", {}).get("low", 5)
    r2_hi = t.get("r2_pct", {}).get("high", 20)
    oi_lo = t.get("oi_abs", {}).get("low", 50)
    oi_hi = t.get("oi_abs", {}).get("high", 500)
    if oi_now is None:
        return {"r1": None, "r2": None, "r3": None, "score": 0, "magnitude": "LOW", "delta_oi": None}
    delta = float(oi_now) - float(oi_prev or 0)
    ad = abs(delta)
    r1 = (ad / vol * 100.0) if vol else None
    r2 = (ad / float(oi_prev) * 100.0) if oi_prev else None
    score = 0
    score += 1 if r1 is not None and r1 >= r1_lo else 0
    score += 1 if r1 is not None and r1 >= r1_hi else 0
    score += 1 if r2 is not None and r2 >= r2_lo else 0
    score += 1 if r2 is not None and r2 >= r2_hi else 0
    score += 1 if ad >= oi_lo else 0
    score += 1 if ad >= oi_hi else 0
    magnitude = "LOW" if score <= 1 else ("MEDIUM" if score <= 3 else "HIGH")
    return {
        "r1": round(r1, 2) if r1 is not None else None,
        "r2": round(r2, 2) if r2 is not None else None,
        "r3": int(ad),
        "score": score,
        "magnitude": magnitude,
        "delta_oi": int(delta),
    }


def event_annotation(
    vol: Optional[float],
    oi_prev: Optional[float],
    oi_now: Optional[float],
    magnitude: str,
    complete: str,
) -> str:
    m = event_magnitude(vol, oi_prev, oi_now)
    delta = m["delta_oi"]
    if delta is None:
        return "数据不足，无法判定净变动"
    if delta == 0:
        return "净变动为0，以日内换手为主"
    if delta >= 0:
        direction_word = "净增"
    else:
        direction_word = "净减"
    if magnitude == "LOW":
        ratio = m["r1"]
        if ratio is None:
            return f"{direction_word}{m['r3']}张（量数据缺失），以日内换手为主"
        return f"{direction_word}仓仅占量{ratio:.1f}%，以日内换手为主"
    if complete == "HIGH":
        volume_word = "放量且"
    else:
        volume_word = ""
    rel = m["r2"]
    rel_txt = f"（{rel:+.1f}% vs前日OI）" if rel is not None else "（前日OI缺失）"
    if magnitude == "MEDIUM":
        return f"{volume_word}{direction_word}{m['r3']}张{rel_txt}，值得跟踪（方向未知）"
    return f"大额{direction_word}{m['r3']}张{rel_txt}，连续性待观察（方向未知）"


def event_card(
    contract: str,
    vol: Optional[float],
    oi_prev: Optional[float],
    oi_now: Optional[float],
    has_prev_vol: bool = True,
    last_price: Optional[float] = None,
    vol_source: Optional[str] = None,
) -> List[str]:
    m = event_magnitude(vol, oi_prev, oi_now)
    complete = completeness(vol is not None, has_prev_vol, oi_prev is not None, oi_now is not None)
    delta_txt = f"ΔOI {m['delta_oi']:+d}张" if m["delta_oi"] is not None else "ΔOI N/A"
    oi_txt = f"OI {int(oi_prev)}→{int(oi_now)}" if (oi_prev is not None and oi_now is not None) else "OI N/A"
    r1_txt = f"ΔOI/Volume {m['r1']:.1f}%" if m["r1"] is not None else "ΔOI/Volume N/A"
    vol_txt = f"Vol {int(vol):,}" if vol is not None else "Vol N/A"
    if vol_source == "yfinance" and vol is not None:
        vol_txt += "（Yahoo补）"
    price_txt = f" | 最新价 ${float(last_price):.2f}" if last_price is not None else ""
    lines = [
        f"{contract} — {vol_txt}{price_txt} | {oi_txt} ({delta_txt}) | "
        f"{r1_txt} | Magnitude: {m['magnitude']} | 完整度: {complete}",
        f"   ⇒ {event_annotation(vol, oi_prev, oi_now, m['magnitude'], complete)}",
    ]
    return lines
