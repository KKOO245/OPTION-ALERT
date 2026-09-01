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
THRESHOLDS_FILE = "thresholds.yaml"

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
    path = root / THRESHOLDS_FILE
    if not path.exists():
        # 兼容调用方传"仓库根目录"与传"config 目录"两种约定
        alt = root / "config" / THRESHOLDS_FILE
        if alt.exists():
            path = alt
    return yaml_mini.load(path)


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
            # ExpMove v2：优先 bid/ask mid（更稳），缺失回退 last
            atm_call_price = (atm_call.get("mid") if atm_call else None) or (atm_call.get("last") if atm_call else None)
            atm_put_price = (atm_put.get("mid") if atm_put else None) or (atm_put.get("last") if atm_put else None)
            ivs = [c["iv"] for c in (atm_call, atm_put) if c and c["iv"] is not None]
            atm_iv = round(sum(ivs) / len(ivs), 4) if ivs else None
        # ExpMove 期限化（expmove_v1）：ATM 跨式价 ÷ 现价 × 100，逐期限独立
        expmove_pct = None
        if spot is not None and atm_call_price is not None and atm_put_price is not None:
            expmove_pct = round((atm_call_price + atm_put_price) / float(spot) * 100.0, 2)

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
            notional = (d * c["last"] * 100.0) if c["last"] is not None else None
            # Top ΔOI 经济相关性：名义 < 阈值 或 距现价 > 远端阈值 → LOW（彩票/低信息价值）
            rel_low_k, rel_far_pct = 50.0, 10.0
            try:
                from engine.yaml_mini import load

                qs = (load(Path(DEFAULT_CONFIG_ROOT) / THRESHOLDS_FILE) or {}).get("quant_summary_v1") or {}
                rel_low_k = float(qs.get("notional_low_k", 50.0))
                rel_far_pct = float(qs.get("dist_far_pct", 10.0))
            except Exception:  # noqa: BLE001
                pass
            relevance = "OK"
            # 名义判据（修正版）：ΔOI×价格×100 的权利金总额 < 阈值 → 低相关性。
            # 纯名义与标的价格无关：低价股近月档不误伤；大额彩票累计不漏。
            # 彩票判据（AND，实证校准 2026-09-01）：权利金名义 <$50k 且 距现价 >10%。
            # 必须两者同时成立：近月档价格低是"标的便宜"不是彩票（不误伤低价股）；
            # 大额累计（如 10万张×$0.03=$30万）名义超阈值 → 不误杀。
            if (
                notional is not None and abs(notional) < rel_low_k * 1000.0
                and dist is not None and abs(dist) > rel_far_pct
            ):
                relevance = "LOW"
            top.append({
                "strike": c["strike"],
                "type": c["type"],
                "delta_oi": int(d),
                "last_price": c["last"],
                "notional": notional,
                "relevance": relevance,
                "distance_pct": round(dist, 1) if dist is not None else None,
                "volume": c["volume"],
                "magnitude": mag["magnitude"],
                "r1": mag.get("r1"),
                "contract_symbol": c["symbol"],
            })
        top.sort(key=lambda t: -abs(t["delta_oi"]))
        top = top[:top_n]

        # Possible Roll 候选（后台字段，不进报告/评分）：
        # 同类型、同一期限出现一正一负的大额 ΔOI → 配对为疑似 roll；
        # 行权价越接近置信越高；仅为观察假设，买开/卖开不可观测。
        roll_candidates: List[Dict[str, Any]] = []
        if has_prev:
            roll_min = float((cfg.get("highlight") or {}).get("roll_candidate_min_abs", 1000))
            by_type: Dict[str, List[Dict[str, Any]]] = {"call": [], "put": []}
            for c in crs:
                if c["symbol"] not in prev_oi:
                    continue
                d = c["oi"] - prev_oi[c["symbol"]]
                if abs(d) < roll_min:
                    continue
                by_type[c["type"]].append({"strike": c["strike"], "delta_oi": int(d)})
            for typ in ("call", "put"):
                pos = [x for x in by_type[typ] if x["delta_oi"] > 0]
                neg = [x for x in by_type[typ] if x["delta_oi"] < 0]
                if not pos or not neg:
                    continue
                best = None
                best_gap = None
                for p in pos:
                    for n in neg:
                        gap = abs(p["strike"] - abs(n["strike"]))
                        if best_gap is None or gap < best_gap:
                            best_gap = gap
                            best = {
                                "type": typ,
                                "from_strike": abs(n["strike"]),
                                "to_strike": p["strike"],
                                "from_delta_oi": n["delta_oi"],
                                "to_delta_oi": p["delta_oi"],
                            }
                if best is not None:
                    best["confidence"] = (
                        "MEDIUM" if best_gap <= max(1.0, 0.10 * best["to_strike"]) else "LOW"
                    )
                    roll_candidates.append(best)

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
                    and t.get("relevance") != "LOW"
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
            "expmove_pct": expmove_pct,
            "activity": activity,
            "delta_exposure": delta_exposure,
            "top_delta_oi": top,
            "roll_candidates": roll_candidates,
            "significant": significant,
        })

    expirations.sort(key=lambda e: e["dte"])
    expirations = expirations[:n_exp]
    return {
        "schema_version": "forward_v1",
        "expirations": expirations,
    }
