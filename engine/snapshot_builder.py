# -*- coding: utf-8 -*-
"""真实数据 → snapshot_v1 适配层（P0.2 第一步）。

两种输入模式：
  1. 实时模式：data = compute_metrics() 的完整输出 dict（含 structure/GEX/Walls）。
  2. 回溯模式：data = analytics CSV 的一行（紧凑字段；结构类字段缺失 → INSUFFICIENT）。

纪律（写死）：
  - 任何字段算不出来就写 None / UNKNOWN，并在 data_sufficiency 标注原因；
    绝不编造数字、绝不拿"看起来合理"的值补位。
  - iv_momentum 用 z-score（相对历史 20 期 IV 分布），历史不足 → N/A；
    iv_momentum_1d 才是当日环比（百分点），供确认层使用。
  - put_buy_flow / volume_surge 在本层一律 INSUFFICIENT：聚合数据无法判定
    主动买卖方向，也没有总量基线（这是诚实标注，不是缺陷）。
"""

from __future__ import annotations

import csv
import json
import math
import os
import statistics
from typing import Any, Dict, List, Optional

SESSION_MAP = {"早报": "morning", "晚报": "evening", "morning": "morning", "evening": "evening"}
SESS_RANK = {"morning": 0, "evening": 1}


def normalize_session(session: str) -> str:
    s = SESSION_MAP.get(str(session or "").strip())
    return s if s else "morning"


def _num(v: Any) -> Optional[float]:
    if v is None:
        return None
    try:
        f = float(v)
        if math.isnan(f) or math.isinf(f):
            return None
        return f
    except (TypeError, ValueError):
        return None


def _get(data: Dict[str, Any], key: str) -> Any:
    return data.get(key) if isinstance(data, dict) else None


def _nested(data: Dict[str, Any], *path: str) -> Any:
    node = data
    for p in path:
        if not isinstance(node, dict):
            return None
        node = node.get(p)
    return node


def _surge_list(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    surge = _get(data, "top_surge")
    if isinstance(surge, str):
        try:
            surge = json.loads(surge)
        except json.JSONDecodeError:
            return []
    return surge if isinstance(surge, list) else []


def load_analytics_rows(path: str) -> List[Dict[str, Any]]:
    if not os.path.exists(path):
        return []
    rows: List[Dict[str, Any]] = []
    with open(path, encoding="utf-8-sig", newline="") as f:
        for raw in csv.DictReader(f):
            row: Dict[str, Any] = {}
            for k, v in raw.items():
                k = (k or "").strip()
                v = (v or "").strip()
                if k in ("oi_concentration", "top_unusual", "top_surge") and v:
                    try:
                        v = json.loads(v)
                    except json.JSONDecodeError:
                        v = None
                elif k in ("oi_concentration", "top_unusual", "top_surge"):
                    v = None
                row[k] = v
            row["session"] = normalize_session(row.get("session"))
            for col in (
                "price", "atm_iv_near", "atm_iv_monthly", "term_ratio", "iv_skew_25",
                "net_gamma_oi", "net_delta_oi", "pcr_vol_near", "pcr_vol_all",
                "expected_move_pct", "max_pain_near", "max_pain_monthly",
            ):
                row[col] = _num(row.get(col))
            rows.append(row)
    return sorted(rows, key=lambda r: (r.get("date", ""), SESS_RANK.get(r.get("session"), 0)))


def _history_before(rows: List[Dict[str, Any]], today: str, session: str) -> List[Dict[str, Any]]:
    key = (today, SESS_RANK.get(session, 0))
    return [r for r in rows if (r.get("date", ""), SESS_RANK.get(r.get("session"), 0)) < key]


def _label_for_obs(n: int, prelim: int, developing: int, established: int) -> str:
    if n < prelim:
        return "N/A"
    if n < developing:
        return "PRELIMINARY"
    if n < established:
        return "DEVELOPING"
    return "ESTABLISHED"


def gamma_sign(net: Optional[float]) -> Optional[str]:
    if net is None:
        return None
    if net > 0:
        return "POSITIVE"
    if net < 0:
        return "NEGATIVE"
    return "MIXED"


def trend_regime(pct: Optional[float]) -> str:
    if pct is None:
        return "UNKNOWN"
    if pct > 0.005:
        return "UP"
    if pct < -0.005:
        return "DOWN"
    return "RANGE"


def price_location_of(spot: Optional[float], flip: Optional[float], call_wall: Optional[float],
                      put_wall: Optional[float], band: float = 0.02) -> Optional[str]:
    if spot is None:
        return None
    if put_wall is not None and abs(spot / put_wall - 1.0) <= band:
        return "near_put_concentration"
    if call_wall is not None and abs(spot / call_wall - 1.0) <= band:
        return "near_call_concentration"
    if flip is not None:
        return "below_flip" if spot < flip else "above_flip"
    if call_wall is not None and put_wall is not None:
        return "between"
    return None


def price_extreme_of(spot: Optional[float], closes: List[float], min_obs: int = 20) -> Optional[str]:
    """spot 相对历史 N 期收盘的新高/新低；历史不足返回 None（不冒充）。"""
    vals = [c for c in closes if c is not None]
    if spot is None or len(vals) < min_obs:
        return None
    if spot >= max(vals):
        return "NEW_HIGH"
    if spot <= min(vals):
        return "NEW_LOW"
    return None


def protection_divergence(extreme: Optional[str], oi_flow: Optional[str]) -> Optional[bool]:
    """价格创新高/低，但期权保护需求方向相反。"""
    if extreme is None or oi_flow is None:
        return None
    if extreme == "NEW_HIGH" and oi_flow == "put_building":
        return True
    if extreme == "NEW_LOW" and oi_flow == "call_building":
        return True
    return False


def oi_flow_of(surge: List[Dict[str, Any]]) -> Optional[str]:
    """按 OI 增仓合计判断建仓方向（Estimated Flow，非确认）。"""
    if not surge:
        return None
    put_oi = sum(int(r.get("oi_change") or 0) for r in surge if r.get("type") == "put")
    call_oi = sum(int(r.get("oi_change") or 0) for r in surge if r.get("type") == "call")
    if put_oi > call_oi and put_oi > 0:
        return "put_building"
    if call_oi > put_oi and call_oi > 0:
        return "call_building"
    return "neutral"


def iv_zscore(atm: Optional[float], hist: List[float]) -> Optional[float]:
    vals = [h for h in hist if h is not None]
    if atm is None or len(vals) < 20:
        return None
    sd = statistics.stdev(vals) if len(vals) > 1 else 0.0
    if sd == 0:
        return None
    return (atm - statistics.mean(vals)) / sd


def iv_percentile(atm: Optional[float], hist: List[float]) -> Optional[float]:
    vals = [h for h in hist if h is not None]
    if atm is None or len(vals) < 20:
        return None
    below = sum(1 for h in vals if h <= atm)
    return below / len(vals) * 100.0


def _iv_level(z: Optional[float], rank: Optional[float]) -> str:
    if z is not None:
        if z >= 1.0:
            return "HIGH"
        if z <= -1.0:
            return "LOW"
        return "NORMAL"
    if rank is not None:
        if rank >= 80:
            return "HIGH"
        if rank <= 20:
            return "LOW"
        return "NORMAL"
    return "UNKNOWN"


def build_snapshot(
    ticker: str,
    session: str,
    data: Dict[str, Any],
    spot: Optional[float],
    created_at: str,
    analytics_rows: Optional[List[Dict[str, Any]]] = None,
    thresholds: Optional[Dict[str, Any]] = None,
    context: Optional[Dict[str, Any]] = None,
    source: Optional[str] = None,
) -> Dict[str, Any]:
    sess = normalize_session(session)
    today = created_at[:10]
    spot = _num(spot)
    su = thresholds.get("data_sufficiency", {}) if isinstance(thresholds, dict) else {}
    rank_t = su.get("rank_obs", {"preliminary": 20, "developing": 60, "established": 250})
    dyn_t = su.get("dynamic_trend_min_trading_days", 5)

    rows = sorted(analytics_rows or [], key=lambda r: (r.get("date", ""), SESS_RANK.get(r.get("session"), 0)))
    hist = _history_before(rows, today, sess)
    prev_row = hist[-1] if hist else None
    prev_same = None
    for r in reversed(hist):
        if r.get("session") == sess:
            prev_same = r
            break
    prev = prev_same or prev_row

    # ---- regime ----
    prev_close = _num(_get(data, "prev_close"))
    if prev_close is None and prev_row:
        prev_close = prev_row.get("price")
    pct = (spot / prev_close - 1.0) if (spot and prev_close) else None
    net_gamma = _nested(data, "structure", "net_gex")
    if net_gamma is None:
        net_gamma = _get(data, "net_gamma_oi")
    gamma = gamma_sign(_num(net_gamma))

    cur_atm = _get(data, "atm_iv_near")
    hist_iv = [r.get("atm_iv_near") for r in hist if r.get("atm_iv_near") is not None]
    z = iv_zscore(_num(cur_atm), hist_iv)
    rank = iv_percentile(_num(cur_atm), hist_iv)

    prev_atm = _num(_get(prev, "atm_iv_near")) if prev else None
    iv_1d = None
    if _num(cur_atm) is not None and prev_atm is not None:
        iv_1d = (_num(cur_atm) - prev_atm) * 100.0  # 百分点

    # regime age / transition（按 gamma 符号 + 趋势组合连续计数）
    age = 1
    transition = None
    if prev_row is not None:
        prev_gamma = gamma_sign(_num(prev_row.get("net_gamma_oi")))
        prev_trend = trend_regime(_prev_pct(prev_row, hist))
        if prev_gamma != gamma or prev_trend != trend_regime(pct):
            transition = "SWITCH" if prev_gamma != gamma else None
        else:
            for r in reversed(hist):
                rg = gamma_sign(_num(r.get("net_gamma_oi")))
                rt = trend_regime(_prev_pct(r, hist))
                if rg == gamma and rt == trend_regime(pct):
                    age += 1
                else:
                    break

    # ---- location ----
    flip = _nested(data, "structure", "gamma_flip")
    flip_levels = []
    for fp in (_nested(data, "structure", "gamma_flip"),
               _nested(data, "structure_near", "gamma_flip"),
               _nested(data, "structure_monthly", "gamma_flip")):
        f = _num(fp)
        if f is not None and f not in flip_levels:
            flip_levels.append(f)
    flip_levels.sort()
    call_wall = _num(_nested(data, "structure", "call_wall")) or _num(_get(data, "call_wall"))
    put_wall = _num(_nested(data, "structure", "put_wall")) or _num(_get(data, "put_wall"))
    price_loc = price_location_of(spot, flip_levels[0] if flip_levels else None, call_wall, put_wall)

    # ---- momentum ----
    cur_skew = _num(_get(data, "iv_skew_25"))
    prev_skew = _num(_get(prev, "iv_skew_25")) if prev else None
    skew_1d = (cur_skew - prev_skew) if (cur_skew is not None and prev_skew is not None) else None
    cur_term = _num(_get(data, "term_ratio"))
    prev_term = _num(_get(prev, "term_ratio")) if prev else None
    term_1d = (cur_term - prev_term) if (cur_term is not None and prev_term is not None) else None
    surge = _surge_list(data)
    flow = oi_flow_of(surge)
    pc = _num(_get(data, "pcr_vol_near"))
    if pc is None:
        pc = _num(_get(data, "pcr_vol_all"))

    # ---- price extreme / divergence ----
    hist_closes = [r.get("price") for r in hist if r.get("price") is not None]
    extreme = price_extreme_of(spot, hist_closes, min_obs=20)
    divergence = protection_divergence(extreme, flow)

    # ---- confirmation ----
    prev_spot = prev_row.get("price") if prev_row else None
    price_break = None
    if prev_spot and spot and flip_levels:
        f = flip_levels[0]
        price_break = (prev_spot < f <= spot) or (prev_spot > f >= spot)

    # ---- data quality ----
    has_structure = _nested(data, "structure") is not None
    market_grade = "A" if (spot is not None and (prev_close is not None or hist_closes)) else "C"
    structure_grade = "A" if has_structure else ("B" if cur_atm is not None else "C")
    flow_grade = "C"
    mech_grade = "C"
    grades = {
        "market_data": market_grade,
        "options_structure": structure_grade,
        "flow": flow_grade,
        "dealer_mechanism": mech_grade,
    }

    # ---- data sufficiency（显式标签；存储层还会自动补缺失字段） ----
    tags: Dict[str, str] = {}
    obs = len(hist)
    dyn_label = _label_for_obs(obs, dyn_t, 20, 60)
    rank_label = _label_for_obs(len(hist_iv), rank_t["preliminary"], rank_t["developing"], rank_t["established"])
    if z is None:
        tags["momentum.iv_momentum"] = rank_label
    if rank is None:
        tags["momentum.iv_rank"] = rank_label
    if iv_1d is None:
        tags["momentum.iv_momentum_1d"] = dyn_label
    if _get(data, "volume_ratio") is None:
        tags["momentum.volume_ratio"] = "INSUFFICIENT_DATA"
    if flow is None:
        tags["momentum.oi_flow"] = "INSUFFICIENT_DATA"
    if extreme is None and (spot is None or len(hist_closes) < 20):
        tags["price_extreme"] = "N/A"
    if call_wall is None:
        tags["location.call_wall"] = "INSUFFICIENT_DATA"
    if put_wall is None:
        tags["location.put_wall"] = "INSUFFICIENT_DATA"
    if not flip_levels:
        tags["location.flip_levels"] = "INSUFFICIENT_DATA"
    if price_loc is None:
        tags["location.price_location"] = "INSUFFICIENT_DATA"
    if _get(data, "volume_ratio") is None:
        tags["confirmation.volume_surge"] = "INSUFFICIENT_DATA"
    tags["confirmation.put_buy_flow"] = "INSUFFICIENT_DATA"

    src = source or _get(data, "source") or ("cboe" if has_structure else "analytics-backfill")

    return {
        "schema_version": "snapshot_v1",
        "data_version": "snapshot_v1",
        "created_at": created_at,
        "session": sess,
        "source": src,
        "ticker": ticker,
        "spot": spot,
        "regime": {
            "version": "regimes_v1",
            "trend": trend_regime(pct),
            "gamma": gamma or "UNKNOWN",
            "iv_level": _iv_level(z, rank),
            "age": age,
            "transition": transition,
        },
        "location": {
            "price_location": price_loc,
            "flip_levels": flip_levels or None,
            "call_wall": call_wall,
            "put_wall": put_wall,
            "concentration": _get(data, "oi_concentration"),
        },
        "momentum": {
            "iv_momentum": round(z, 3) if z is not None else None,
            "iv_momentum_1d": round(iv_1d, 3) if iv_1d is not None else None,
            "iv_level": _iv_level(z, rank),
            "iv_rank": round(rank, 1) if rank is not None else None,
            "skew_momentum": round(skew_1d, 3) if skew_1d is not None else None,
            "skew": _num(_get(data, "iv_skew_25")),
            "term_structure_momentum": round(term_1d, 4) if term_1d is not None else None,
            "pc_ratio": round(pc, 3) if pc is not None else None,
            "pc_oi_ratio": _num(_get(data, "pcr_oi_near")),
            "oi_flow": flow,
            "price_momentum": round(pct, 4) if pct is not None else None,
            "volume_ratio": _num(_get(data, "volume_ratio")),
            "atm_iv": _num(_get(data, "atm_iv_near")),
            "expected_move_pct": _num(_get(data, "expected_move_pct")),
            "term_ratio": _num(_get(data, "term_ratio")),
        },
        "confirmation": {
            "iv_surge": (iv_1d > 0) if iv_1d is not None else None,
            "skew_surge": (skew_1d > 0) if skew_1d is not None else None,
            "volume_surge": None,
            "put_buy_flow": None,
            "price_break": price_break,
        },
        "price_extreme": extreme,
        "protection_divergence": divergence,
        "context": {
            "spy_return": _num(_get(context, "spy_return")),
            "qqq_return": _num(_get(context, "qqq_return")),
            "sector_relative": _get(context, "sector_relative"),
            "vix": _num(_get(context, "vix")),
            "notes": _get(context, "notes"),
        },
        "data_quality": grades,
        "data_sufficiency": tags,
    }


def _prev_pct(row: Dict[str, Any], rows: List[Dict[str, Any]]) -> Optional[float]:
    """该行相对其前一行（同一会话优先）的价格百分比变化。"""
    idx = None
    for i, r in enumerate(rows):
        if r is row:
            idx = i
            break
    if idx is None or idx == 0:
        return None
    price = row.get("price")
    prev = rows[idx - 1].get("price")
    return (price / prev - 1.0) if (price and prev) else None
