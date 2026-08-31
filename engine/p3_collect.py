# -*- coding: utf-8 -*-
"""P3 采集层（p3_collect_v1）：随 P1 一起入库的"待验证研究字段"。

纪律：
  - 只进 analytics JSON，不进报告/评分；公式全部版本化；
  - 数据不足一律 None，不编造；事件覆盖仅统计未来（>= 当日）事件；
  - IV/RV 的 RV 是滞后量（过去 N 日实现波动），IV 是前瞻量，二者不直接可比，仅作研究字段。
"""

from __future__ import annotations

import datetime
import math
from zoneinfo import ZoneInfo
from typing import Any, Dict, List, Optional


def _num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def realized_vol(closes: Optional[List[float]], window: int, min_obs: int = 5) -> Optional[float]:
    """最近 N 个交易日收盘价的年化实现波动（对数收益标准差 × √252）。
    需要 window+1 个收盘价（window 个收益）；不足返回 None。

    （修复）守卫必须用 window+1 而不是 min_obs+1：
    数据量在 [min_obs+1, window] 之间时，range(len-window, len) 起点为负，
    会触发 IndexError（或负索引环绕算出错误结果），从而拖垮整个 p3 采集。
    """
    vals = [c for c in closes or [] if c is not None and c > 0]
    if len(vals) < max(window + 1, min_obs + 1):
        return None
    rets = [math.log(vals[i] / vals[i - 1]) for i in range(len(vals) - window, len(vals))]
    if len(rets) < 2:
        return None
    mean = sum(rets) / len(rets)
    var = sum((r - mean) ** 2 for r in rets) / (len(rets) - 1)
    return math.sqrt(var) * math.sqrt(252.0)


def daily_closes(price_rows: Optional[List[Dict[str, Any]]]) -> List[float]:
    """按交易日去重（晚报优先），返回按日期升序的收盘价列表。
    修复"早晚各一行导致 RV 窗口错位"：5D RV 必须用 5 个交易日，不是 5 行。"""
    best: Dict[str, Dict[str, Any]] = {}
    for r in price_rows or []:
        d = str(r.get("date") or "")[:10]
        p = _num(r.get("price"))
        if not d or p is None or p <= 0:
            continue
        sess = "evening" if str(r.get("session") or "").lower() == "evening" else "morning"
        cur = best.get(d)
        if cur is None or sess == "evening" or sess == cur.get("session"):
            best[d] = {"session": sess, "price": p}
    return [best[d]["price"] for d in sorted(best)]


def _event_overlap(
    forward_expirations: Optional[List[Dict[str, Any]]],
    event_dates: Optional[List[Dict[str, Any]]],
    as_of=None,
) -> Optional[List[Dict[str, Any]]]:
    """逐期限：是否覆盖"快照时刻之后"的【高】事件（事件日期 > 上一期限到期日 且 <= 本期限到期日）。"""
    exps = forward_expirations or []
    if not exps:
        return None
    asof_dt = None
    if as_of is not None:
        try:
            asof_dt = as_of
            if asof_dt.tzinfo is not None:
                asof_dt = asof_dt.astimezone(ZoneInfo("America/Toronto")).replace(tzinfo=None)
            else:
                asof_dt = asof_dt.replace(tzinfo=None)
        except Exception:
            asof_dt = None
    upcoming = []
    for d in event_dates or []:
        if not isinstance(d, dict) or not d.get("date"):
            continue
        ds = str(d["date"])
        ts = str(d.get("time") or "00:00")[:5]
        try:
            ev_dt = datetime.datetime.fromisoformat(f"{ds}T{ts}:00")
        except ValueError:
            continue
        if asof_dt is not None and ev_dt <= asof_dt:
            continue  # 已公布/已过去的事件不计入覆盖
        upcoming.append(d)
    days = sorted({str(d.get("date")) for d in upcoming})
    if not days:
        return None
    out = []
    prev_exp = None
    for e in exps:
        exp = str(e.get("expiration") or "")
        hits = [d for d in days if (prev_exp is None or d > prev_exp) and d <= exp]
        names = [d.get("name") for d in upcoming if str(d.get("date")) in hits]
        out.append({
            "expiration": exp,
            "dte": e.get("dte"),
            "covers_event": bool(hits),
            "events": names[:3],
        })
        prev_exp = exp
    return out


def _confluence(
    spot: Optional[float],
    flip_levels: Optional[List[float]],
    call_wall: Optional[float],
    put_wall: Optional[float],
    oi_strikes: Optional[List[Dict[str, Any]]],
    band_pct: float = 2.0,
) -> Dict[str, Any]:
    """±band 价格带内聚合同族：gamma（flip/墙）与 oi（高 OI 档）计数。"""
    if spot is None:
        return {"families_in_band": 0, "levels": []}
    levels = []
    gamma_hit = False
    for f in flip_levels or []:
        if abs(f / spot - 1.0) * 100.0 <= band_pct:
            gamma_hit = True
            levels.append({"type": "gamma_flip", "price": round(f, 2)})
    for w, label in ((call_wall, "call_wall"), (put_wall, "put_wall")):
        if w is not None and abs(w / spot - 1.0) * 100.0 <= band_pct:
            gamma_hit = True
            levels.append({"type": label, "price": round(w, 2)})
    oi_hit = False
    for t in oi_strikes or []:
        k = _num(t.get("strike"))
        if k is not None and abs(k / spot - 1.0) * 100.0 <= band_pct:
            oi_hit = True
            levels.append({"type": "oi", "price": round(k, 2)})
    families = 0
    if gamma_hit:
        families += 1
    if oi_hit:
        families += 1
    return {"families_in_band": families, "levels": levels}


def collect_p3(
    *,
    regime_result: Optional[Dict[str, Any]],
    coverage: Optional[Dict[str, Any]],
    second_order: Optional[Dict[str, Any]],
    atm_iv_near: Optional[float],
    price_rows: Optional[List[Dict[str, Any]]],
    forward_expirations: Optional[List[Dict[str, Any]]],
    event_dates: Optional[List[Dict[str, Any]]],
    as_of=None,
    spot: Optional[float],
    call_wall: Optional[float],
    put_wall: Optional[float],
    oi_strikes: Optional[List[Dict[str, Any]]],
    rv_window: int = 20,
    rv_min_obs: int = 5,
    confluence_band_pct: float = 2.0,
) -> Dict[str, Any]:
    gex = None
    if isinstance(regime_result, dict):
        gex = {
            "net_gex": regime_result.get("net_gex_at_spot"),
            "abs_gex": (
                abs(regime_result["net_gex_at_spot"])
                if regime_result.get("net_gex_at_spot") is not None else None
            ),
            "n_used": regime_result.get("n_contracts_used"),
            "n_skipped": regime_result.get("n_contracts_skipped"),
            "spot_zone": regime_result.get("spot_zone"),
        }
    daily = daily_closes(price_rows)
    rv5 = realized_vol(daily, 5, min_obs=rv_min_obs)
    rv20 = realized_vol(daily, rv_window, min_obs=rv_min_obs)
    iv = _num(atm_iv_near)
    iv_rv = {
        "atm_iv_near": iv,
        "rv_5d": round(rv5, 4) if rv5 is not None else None,
        "rv_20d": round(rv20, 4) if rv20 is not None else None,
        "ratio_5d": round(iv / rv5, 3) if (iv is not None and rv5) else None,
        "ratio_20d": round(iv / rv20, 3) if (iv is not None and rv20) else None,
    }
    return {
        "schema_version": "p3_collect_v1",
        "gex": gex,
        "coverage": coverage,
        "second_order": second_order,
        "iv_rv": iv_rv,
        "event_overlap": _event_overlap(forward_expirations, event_dates, as_of),
        "confluence": _confluence(
            spot, (regime_result or {}).get("flip_levels") if isinstance(regime_result, dict) else None,
            call_wall, put_wall, oi_strikes, band_pct=confluence_band_pct,
        ),
    }
