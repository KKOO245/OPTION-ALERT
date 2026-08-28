# -*- coding: utf-8 -*-
"""重点速览（highlight_v1）+ 事件差分（event_diff_v1）。

纪律：
  - 规则全部预提交（config/thresholds.yaml → highlight / event_differential 段），
    不靠"觉得重要"；阈值均为经验默认，待数据校准。
  - 每标的最多 max_items 条；无满足项时返回空（报告显示"今日无重点项"）。
  - highlight 是"提醒注意"，不是方向信号；文案禁用方向断言词。
  - 事件差分是观察（覆盖事件的期限 ATM IV vs 相邻期限），单日截面不写因果。
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Dict, List, Optional

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LEVEL_EMOJI = {"CRITICAL": "🔴", "WATCH": "🟡", "INFO": "🔵"}
LEVEL_RANK = {"CRITICAL": 0, "WATCH": 1, "INFO": 2}

_HL_DEFAULTS = {
    "max_items": 3,
    "event_diff_critical_pp": 15.0,
    "event_diff_watch_pp": 10.0,
    "near_level_pct": 5.0,
    "day_move_pct": 2.0,
    "concentration_min_pct": 10.0,
}
_ED_DEFAULTS = {"min_diff_pp": 5.0}


def _load_cfg() -> Dict[str, Any]:
    from engine import yaml_mini

    path = Path(BASE_DIR) / "config" / "thresholds.yaml"
    try:
        cfg = yaml_mini.load(path)
    except Exception:
        cfg = {}
    if not isinstance(cfg, dict):
        return {}
    return cfg


def _hl(cfg: Dict[str, Any]) -> Dict[str, Any]:
    v = cfg.get("highlight")
    return {**_HL_DEFAULTS, **(v if isinstance(v, dict) else {})}


def _ed(cfg: Dict[str, Any]) -> Dict[str, Any]:
    v = cfg.get("event_differential")
    return {**_ED_DEFAULTS, **(v if isinstance(v, dict) else {})}


def event_differential(
    snapshot: Dict[str, Any],
    event_dates: Optional[List[Dict[str, Any]]],
) -> Optional[Dict[str, Any]]:
    """事件差分 v1：最近一个覆盖本周剩余【高】事件的期限，与相邻下一期限比 ATM IV。

    覆盖判定：事件日期 > 上一期限到期日 且 <= 本期限到期日。
    返回 None 表示无事件覆盖、数据不足或差值低于阈值（不提示，不编造）。
    """
    cfg = _load_cfg()
    min_diff = float(_ed(cfg).get("min_diff_pp", 5.0))
    fwd = snapshot.get("forward") or {}
    exps = fwd.get("expirations") or []
    if not event_dates or len(exps) < 2:
        return None
    event_days = sorted(
        {d["date"] for d in event_dates if isinstance(d, dict) and d.get("date")}
    )
    if not event_days:
        return None

    covered = None
    prev_exp = None
    for e in exps:
        exp = str(e.get("expiration") or "")
        hits = [d for d in event_days if (prev_exp is None or d > prev_exp) and d <= exp]
        if hits and e.get("atm_iv") is not None:
            covered = (e, hits)
            break
        prev_exp = exp
    if covered is None:
        return None
    e, hits = covered
    idx = exps.index(e)
    if idx + 1 >= len(exps):
        return None
    control = exps[idx + 1]
    if control.get("atm_iv") is None:
        return None
    diff_pp = (float(e["atm_iv"]) - float(control["atm_iv"])) * 100.0
    if diff_pp < min_diff:
        return None
    names = "、".join(
        d.get("name") or d.get("date") for d in event_dates if d.get("date") in hits
    )
    if len(hits) > 2:
        names = "、".join(names.split("、")[:2]) + " 等"
    return {
        "expiration": e["expiration"],
        "dte": e.get("dte"),
        "covered_iv_pct": round(float(e["atm_iv"]) * 100.0, 1),
        "control_expiration": control["expiration"],
        "control_dte": control.get("dte"),
        "control_iv_pct": round(float(control["atm_iv"]) * 100.0, 1),
        "diff_pp": round(diff_pp, 1),
        "events": names or "高重要性事件",
    }


def _num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def build_highlights(
    snapshot: Dict[str, Any],
    activity: Optional[List[Dict[str, Any]]] = None,
    prev: Optional[Dict[str, Any]] = None,
    event_dates: Optional[List[Dict[str, Any]]] = None,
) -> List[Dict[str, str]]:
    """按 highlight_v1 规则生成重点速览（≤ max_items 条，按级别排序）。"""
    cfg = _load_cfg()
    h = _hl(cfg)
    max_items = int(h.get("max_items", 3))
    diff = event_differential(snapshot, event_dates)

    items: List[Dict[str, str]] = []
    m = snapshot.get("momentum") or {}
    loc = snapshot.get("location") or {}
    fwd = snapshot.get("forward") or {}
    exps = fwd.get("expirations") or []

    # 🔴 关键级
    if diff is not None and diff["diff_pp"] >= float(h.get("event_diff_critical_pp", 15.0)):
        items.append({
            "level": "CRITICAL",
            "title": "事件差分",
            "detail": (
                f"{diff['expiration'][5:]}（{diff['dte']}D）ATM IV {diff['covered_iv_pct']:.1f}% "
                f"vs {diff['control_expiration'][5:]} {diff['control_iv_pct']:.1f}%"
                f"（差 {diff['diff_pp']:+.1f}pp），覆盖 {diff['events']}"
            ),
            "reason": "覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）",
        })
    if prev:
        pg = (prev.get("regime") or {}).get("gamma")
        g = (snapshot.get("regime") or {}).get("gamma")
        if (
            pg in ("POSITIVE", "NEGATIVE")
            and g in ("POSITIVE", "NEGATIVE")
            and pg != g
        ):
            items.append({
                "level": "CRITICAL",
                "title": "Gamma Regime 切换",
                "detail": f"{pg} → {g}（模型分类）",
                "reason": "Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）",
            })
    ve = (snapshot.get("context") or {}).get("vol_environment") or {}
    label = (ve.get("regime") or {}).get("label")
    prev_label = None
    if prev:
        pve = (prev.get("context") or {}).get("vol_environment") or {}
        prev_label = (pve.get("regime") or {}).get("label")
    sev_order = {"LOW": 0, "NORMAL": 1, "ELEVATED": 2, "STRESS": 3}
    if (
        prev_label in sev_order
        and label in sev_order
        and sev_order[label] > sev_order[prev_label]
    ):
        items.append({
            "level": "CRITICAL",
            "title": "Vol Regime 升档",
            "detail": f"{prev_label or '?'} → {label}（vol_regime_v1）",
            "reason": "波动环境升档仅作环境标签，不判方向、不参与 Gate",
        })

    # 🟡 关注级
    pm = _num(m.get("price_momentum"))
    if pm is not None and abs(pm) * 100.0 >= float(h.get("day_move_pct", 2.0)):
        items.append({
            "level": "WATCH",
            "title": "单日价格波动",
            "detail": f"{pm * 100.0:+.1f}%（vs 前收盘）",
            "reason": "价格变动超阈值；纯事实，不解释方向",
        })
    if diff is not None and diff["diff_pp"] >= float(h.get("event_diff_watch_pp", 10.0)):
        if not any(it["title"] == "事件差分" for it in items):
            items.append({
                "level": "WATCH",
                "title": "事件差分",
                "detail": (
                    f"{diff['expiration'][5:]} ATM IV {diff['covered_iv_pct']:.1f}% "
                    f"vs {diff['control_expiration'][5:]} {diff['control_iv_pct']:.1f}%"
                    f"（差 {diff['diff_pp']:+.1f}pp）"
                ),
                "reason": "覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）",
            })
    near_pct = float(h.get("near_level_pct", 5.0))
    for e in exps:
        for t in e.get("top_delta_oi") or []:
            if (
                t.get("magnitude") == "HIGH"
                and t.get("distance_pct") is not None
                and abs(float(t["distance_pct"])) <= near_pct
            ):
                items.append({
                    "level": "WATCH",
                    "title": "近现价集中开仓",
                    "detail": (
                        f"{e['expiration'][5:]} {int(t['strike'])}{t['type'][0].upper()} "
                        f"ΔOI {t['delta_oi']:+,}（距现价 {t['distance_pct']:+.1f}%）"
                    ),
                    "reason": "高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）",
                })
                break
        if any(it["title"] == "近现价集中开仓" for it in items):
            break

    # 🔵 信息级
    conc_min = float(h.get("concentration_min_pct", 10.0))
    for e in exps:
        total = float(e.get("call_oi") or 0) + float(e.get("put_oi") or 0)
        for t in e.get("top_delta_oi") or []:
            d = abs(float(t.get("delta_oi") or 0))
            if total > 0 and d / total * 100.0 >= conc_min:
                items.append({
                    "level": "INFO",
                    "title": "期限 OI 集中",
                    "detail": (
                        f"{e['expiration'][5:]} {int(t['strike'])}{t['type'][0].upper()} "
                        f"ΔOI {t['delta_oi']:+,} 占该期限总 OI {d / total * 100.0:.1f}%"
                    ),
                    "reason": "新增仓位相对该期限总量显著（结构观察，非资金方向）",
                })
                break
    flip_candidates = loc.get("flip_candidates") or loc.get("flip_levels") or []
    if flip_candidates and loc.get("flip_status") in ("CONDITIONAL", None):
        cands = " / ".join(f"{f:.1f}" for f in flip_candidates[:3])
        items.append({
            "level": "INFO",
            "title": "Flip 状态",
            "detail": f"CONDITIONAL（Candidates: {cands}）｜ Primary: N/A",
            "reason": "Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读",
        })

    # 按 title 去重（保留最高级），按级别排序，截断
    seen: Dict[str, Dict[str, str]] = {}
    for it in items:
        key = it["title"]
        if key not in seen or LEVEL_RANK[it["level"]] < LEVEL_RANK[seen[key]["level"]]:
            seen[key] = it
    out = sorted(seen.values(), key=lambda x: LEVEL_RANK[x["level"]])
    return out[:max_items]


def aggregate_highlights(
    per_ticker: Dict[str, List[Dict[str, str]]],
    max_items: int = 15,
) -> tuple:
    """把各 ticker 的重点合并成一份（按级别排序，带 ticker 前缀，超限截断）。

    返回 (items, truncated)；truncated=True 表示还有更多被截断。
    """
    out: List[Dict[str, str]] = []
    for ticker in sorted(per_ticker):
        for it in per_ticker.get(ticker) or []:
            out.append({**it, "ticker": ticker})
    out.sort(key=lambda x: LEVEL_RANK.get(x["level"], 9))
    truncated = len(out) > max_items
    return out[:max_items], truncated


def highlights_section(items: List[Dict[str, str]], note: Optional[str] = None) -> List[str]:
    """渲染「🔍 重点速览」段（报告顶部聚合版；ticker 前缀由 items 自带）。"""
    if not items:
        return ["🔍 重点速览: 今日无重点项（机械检查 highlight_v1）", ""]
    lines = ["🔍 重点速览"]
    for it in items:
        prefix = f"{it.get('ticker', '')} ｜ " if it.get("ticker") else ""
        lines.append(f"{LEVEL_EMOJI.get(it['level'], '🔵')} **{prefix}{it['title']}**: {it['detail']}")
        if it.get("reason"):
            lines.append(f"   ⇒ {it['reason']}")
    if note:
        lines.append(note)
    lines.append("")
    return lines
