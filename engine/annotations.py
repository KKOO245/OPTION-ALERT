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


def assert_no_direction_words(text: str) -> bool:
    return not any(w in text for w in FORBIDDEN_WORDS)


def options_annotation(pc_vol: Optional[float], pc_oi: Optional[float]) -> List[str]:
    lines = []
    if pc_vol is not None:
        if pc_vol >= 1:
            lines.append(f"Put/Call Volume: {pc_vol:.2f}×（Put 成交显著高于 Call）→ 方向 Unknown")
        else:
            lines.append(f"Put/Call Volume: {pc_vol:.2f}×（Call 成交高于 Put）→ 方向 Unknown")
    else:
        lines.append("Put/Call Volume: 数据不足 → 方向 Unknown")
    if pc_oi is not None:
        if pc_oi < 1:
            lines.append(f"Put/Call OI: {pc_oi:.2f}×（Put OI 低于 Call OI）→ 存量 Call-dominant")
        elif pc_oi > 1:
            lines.append(f"Put/Call OI: {pc_oi:.2f}×（Put OI 高于 Call OI）→ 存量 Put-dominant")
        else:
            lines.append(f"Put/Call OI: {pc_oi:.2f}×（两侧接近均衡）")
    else:
        lines.append("Put/Call OI: 数据不足")
    if pc_vol is not None and pc_oi is not None:
        divergent = (pc_vol >= 1) != (pc_oi >= 1)
        lines.append("两者结构不一致" if divergent else "两者结构一致")
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
    if delta >= 0:
        direction_word = "净增"
    else:
        direction_word = "净减"
    if magnitude == "LOW":
        ratio = m["r1"]
        return f"{direction_word}仓仅占量{ratio:.1f}%，以日内换手为主"
    if complete == "HIGH":
        volume_word = "放量且"
    else:
        volume_word = ""
    rel = m["r2"]
    if magnitude == "MEDIUM":
        return f"{volume_word}{direction_word}{m['r3']}张（{rel:+.1f}% vs前日OI），值得跟踪（方向未知）"
    return f"大额{direction_word}{m['r3']}张（{rel:+.1f}%），连续性待观察（方向未知）"


def event_card(
    contract: str,
    vol: Optional[float],
    oi_prev: Optional[float],
    oi_now: Optional[float],
    has_prev_vol: bool = True,
) -> List[str]:
    m = event_magnitude(vol, oi_prev, oi_now)
    complete = completeness(vol is not None, has_prev_vol, oi_prev is not None, oi_now is not None)
    delta_txt = f"ΔOI {m['delta_oi']:+d}张" if m["delta_oi"] is not None else "ΔOI N/A"
    oi_txt = f"OI {int(oi_prev)}→{int(oi_now)}" if (oi_prev is not None and oi_now is not None) else "OI N/A"
    r1_txt = f"ΔOI/Volume {m['r1']:.1f}%" if m["r1"] is not None else "ΔOI/Volume N/A"
    lines = [
        f"{contract} — Vol {int(vol) if vol is not None else 'N/A'} | {oi_txt} ({delta_txt}) | "
        f"{r1_txt} | Magnitude: {m['magnitude']} | 完整度: {complete}",
        f"   ⇒ {event_annotation(vol, oi_prev, oi_now, m['magnitude'], complete)}",
    ]
    return lines
