# -*- coding: utf-8 -*-
"""Forward Expiration Structure v1（冻结 2026-08-24）。

独立观察层：回答"OI 变化集中在哪个未来时间窗口 × 行权价区域"。
纪律：
  - 不预测价格、不判断买卖方向（买卖方不可观测），不进入 Direction Edge / Gate；
  - ΔOI 对比"最近一次保存的期权链快照"（storage.save_snapshot）；
  - 上次没有的合约/到期日 → ΔOI = N/A（新上架），不算 0；
  - Forward Activity = max(C 侧, P 侧) 的 event_magnitude 等级（复用 r1/r2/绝对ΔOI 阈值）；
  - L2 仅 Activity=HIGH 展开；L3 需 HIGH + 距现价≤±5% + OI 集中 Top3 + ΔOI/Volume 高。
"""

from __future__ import annotations

import datetime
import os
from pathlib import Path
from typing import Any, Dict, List, Optional

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_CONFIG_ROOT = os.path.join(BASE_DIR, "config")

_DEFAULTS = {
    "n_expirations": 4,
    "min_dte": 1,
    "top_delta_oi_n": 3,
    "l3_max_distance_pct": 5.0,
}


def _num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def _load_cfg(config_root: Optional[str]) -> Dict[str, Any]:
    from engine import yaml_mini

    root = Path(config_root) if config_root else Path(DEFAULT_CONFIG_ROOT)
    return yaml_mini.load(root / "thresholds.yaml")


def _contract_rows(contracts: Optional[List[Dict[str, Any]]]) -> List[Dict[str, Any]]:
    rows = []
    for c in contracts or []:
        try:
            typ = str(c.get("type") or "").lower()
            if typ not in ("call", "put"):
                continue
            rows.append({
                "symbol": c.get("contract_symbol"),
                "expiration": str(c.get("expiration") or "")[:10],
                "type": typ,
                "strike": float(c.get("strike")),
                "last": _num(c.get("last")),
                "volume": float(c.get("volume") or 0),
                "oi": float(c.get("open_interest") or 0),
                "iv": _num(c.get("iv")),
                "delta": _num(c.get("delta")),
            })
        except (TypeError, ValueError):
            continue
    return rows


def _iter_prev_rows(prev) -> List[Any]:
    """兼容 pandas DataFrame 或 list[dict]（测试零依赖用 list）。"""
    if prev is None:
        return []
    if hasattr(prev, "iterrows"):
        return [r for _, r in prev.iterrows()]
    return list(prev)


def _prev_oi_map(prev) -> Dict[str, float]:
    out: Dict[str, float] = {}
    for r in _iter_prev_rows(prev):
        if not hasattr(r, "get"):
            continue
        sym = r.get("contractSymbol") or r.get("contract_symbol")
        if not sym:
            continue
        try:
            out[str(sym)] = float(r.get("openInterest") or r.get("open_interest") or 0)
        except (TypeError, ValueError):
            continue
    return out


def build_forward_structure(
    contracts: Optional[List[Dict[str, Any]]],
    prev,
    spot: Optional[float],
    as_of_date: Optional[datetime.date] = None,
    config_root: Optional[str] = None,
) -> Dict[str, Any]:
    cfg = _load_cfg(config_root)
    fs = cfg.get("forward_structure") or _DEFAULTS
    n_exp = int(fs.get("n_expirations", 4))
    min_dte = int(fs.get("min_dte", 1))
    top_n = int(fs.get("top_delta_oi_n", 3))
    l3_dist = float(fs.get("l3_max_distance_pct", 5.0))
    act_t = cfg.get("activity_magnitude") or {}

    from engine.annotations import event_magnitude

    today = as_of_date or datetime.date.today()
    prev_oi = _prev_oi_map(prev)

    rows = _contract_rows(contracts)
    by_exp: Dict[str, List[Dict[str, Any]]] = {}
    for r in rows:
        by_exp.setdefault(r["expiration"], []).append(r)

    expirations: List[Dict[str, Any]] = []
    for exp, crs in by_exp.items():
        try:
            dte = (datetime.date.fromisoformat(exp) - today).days
        except ValueError:
            continue
        if dte < min_dte:
            continue
        calls = [c for c in crs if c["type"] == "call"]
        puts = [c for c in crs if c["type"] == "put"]
        if not calls and not puts:
            continue

        call_oi = sum(c["oi"] for c in calls)
        put_oi = sum(c["oi"] for c in puts)
        call_vol = sum(c["volume"] for c in calls)
        put_vol = sum(c["volume"] for c in puts)
        has_prev = any(c["symbol"] in prev_oi for c in crs)

        # 同合约口径：ΔOI 只统计"上次也存在的合约"（matched 现 − matched 前），
        # 同一结算日内新上架行权价的全部 OI 单独记 call_new_oi / put_new_oi，不混入 ΔOI。
        matched_calls = [c for c in calls if c["symbol"] in prev_oi]
        matched_puts = [c for c in puts if c["symbol"] in prev_oi]
        call_oi_prev = sum(prev_oi[c["symbol"]] for c in matched_calls)
        put_oi_prev = sum(prev_oi[c["symbol"]] for c in matched_puts)
        call_oi_matched = sum(c["oi"] for c in matched_calls)
        put_oi_matched = sum(c["oi"] for c in matched_puts)
        call_d = (call_oi_matched - call_oi_prev) if has_prev else None
        put_d = (put_oi_matched - put_oi_prev) if has_prev else None
        call_new_oi = sum(c["oi"] for c in calls if c["symbol"] not in prev_oi) if has_prev else 0.0
        put_new_oi = sum(c["oi"] for c in puts if c["symbol"] not in prev_oi) if has_prev else 0.0

        # ATM：行权价离现价最近
        atm_strike = None
        atm_call_price = atm_put_price = atm_iv = None
        if spot is not None:
            atm_strike = min(crs, key=lambda c: abs(c["strike"] - float(spot)))["strike"]
            atm_call = next((c for c in calls if abs(c["strike"] - atm_strike) < 1e-6), None)
            atm_put = next((c for c in puts if abs(c["strike"] - atm_strike) < 1e-6), None)
            atm_call_price = atm_call["last"] if atm_call else None
            atm_put_price = atm_put["last"] if atm_put else None
            ivs = [c["iv"] for c in (atm_call, atm_put) if c and c["iv"] is not None]
            atm_iv = round(sum(ivs) / len(ivs), 4) if ivs else None

        # Top ΔOI（单一行权价明细，按 |ΔOI| 降序）
        top: List[Dict[str, Any]] = []
        for c in crs:
            if c["symbol"] not in prev_oi:
                continue  # 无前值/新上架 → 不参与变化计算
            d = c["oi"] - prev_oi[c["symbol"]]
            if abs(d) < 1:
                continue
            dist = (c["strike"] / float(spot) - 1.0) * 100.0 if spot else None
            mag = event_magnitude(c["volume"], prev_oi[c["symbol"]], c["oi"], act_t)
            top.append({
                "strike": c["strike"],
                "type": c["type"],
                "delta_oi": int(d),
                "last_price": c["last"],
                "notional": (d * c["last"] * 100.0) if c["last"] is not None else None,
                "distance_pct": round(dist, 1) if dist is not None else None,
                "volume": c["volume"],
                "magnitude": mag["magnitude"],
                "r1": mag.get("r1"),
                "contract_symbol": c["symbol"],
            })
        top.sort(key=lambda t: -abs(t["delta_oi"]))
        top = top[:top_n]

        # ΔOI Δ Exposure = Σ ΔOI × delta × 100（模型估算）
        delta_exposure = None
        if has_prev:
            total = 0.0
            for c in crs:
                if c["symbol"] in prev_oi and c["delta"] is not None:
                    total += (c["oi"] - prev_oi[c["symbol"]]) * c["delta"] * 100.0
            delta_exposure = round(total, 0)

        # Forward Activity：max(C 侧, P 侧) 的 event_magnitude；无前值 → LOW
        activity = "LOW"
        if has_prev:
            mg_c = event_magnitude(call_vol, call_oi_prev, call_oi_matched, act_t)
            mg_p = event_magnitude(put_vol, put_oi_prev, put_oi_matched, act_t)
            activity = max(mg_c["magnitude"], mg_p["magnitude"], key=lambda x: ("LOW", "MEDIUM", "HIGH").index(x))

        # L3 显著条件：Activity HIGH + 合约级 r1(ΔOI/Volume) ≥ 高分档 + 距现价 ≤ ±15% + OI 集中 Top3
        significant: List[Dict[str, Any]] = []
        r1_hi = float((act_t.get("r1_pct") or {}).get("high", 20))
        if activity == "HIGH":
            conc = sorted(crs, key=lambda c: -c["oi"])[:3]
            conc_symbols = {c["symbol"] for c in conc}
            for t in top:
                if (
                    t["magnitude"] == "HIGH"
                    and t.get("r1") is not None
                    and t["r1"] >= r1_hi
                    and t["distance_pct"] is not None
                    and abs(t["distance_pct"]) <= l3_dist
                    and t["contract_symbol"] in conc_symbols
                ):
                    significant.append(t)

        expirations.append({
            "expiration": exp,
            "dte": int(dte),
            "call_oi": round(call_oi, 0),
            "put_oi": round(put_oi, 0),
            "call_oi_prev": round(call_oi_prev, 0),
            "put_oi_prev": round(put_oi_prev, 0),
            "call_delta_oi": round(call_d, 0) if call_d is not None else None,
            "put_delta_oi": round(put_d, 0) if put_d is not None else None,
            "call_new_oi": round(call_new_oi, 0),
            "put_new_oi": round(put_new_oi, 0),
            "call_volume": round(call_vol, 0),
            "put_volume": round(put_vol, 0),
            "has_prev": has_prev,
            "new_listing": not has_prev,
            "atm_strike": atm_strike,
            "atm_call_price": atm_call_price,
            "atm_put_price": atm_put_price,
            "atm_iv": atm_iv,
            "activity": activity,
            "delta_exposure": delta_exposure,
            "top_delta_oi": top,
            "significant": significant,
        })

    expirations.sort(key=lambda e: e["dte"])
    expirations = expirations[:n_exp]
    return {
        "schema_version": "forward_v1",
        "expirations": expirations,
    }
