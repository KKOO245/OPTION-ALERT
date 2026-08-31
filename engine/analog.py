# -*- coding: utf-8 -*-
"""Analog Engine（analog_v1，P2）：历史相似状态 → 条件结果分布 + OOS 验证。

纪律（与 validation/ 包一致）：
  - 只用截至 T 的特征匹配，结果只用 T 之后 → 无未来信息泄漏；
  - 分层匹配（Hierarchical）：逐层收窄，样本 < min_n 即停，不硬凑结论；
  - OOS：冻结日期切分，训练集定规则，样本外原样复跑；不显著 → NOT_VALIDATED；
  - 输出 thesis/analog_validation.jsonl（研究层），日报不展示；
  - 阈值（min_n / 提升 margin / 分位桶）为候选参数（analog_v1，thresholds.yaml），不冻结。

v1 特征（全部来自 episode，无未来泄漏）：
  - 波动率环境：iv_pct（该标的 IV 百分位，VIX 历史到位后升级为 VIX Regime）；
  - Gamma：net_gex 符号（Model A）；
  - Spot–Flip 距离：|spot/primary_flip − 1|；
  - P/C OI：pcr_oi_near 在该标的 oi_history 分布中的百分位。
结果：|1/3/5D 收益|、5D 实现波动、|5D MAE|。
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

from validation.base_rate import unconditional_base_rate  # noqa: F401 (口径参照)
from validation.confidence import label_for_n, wilson_ci
from validation.lift import lift_pp

SCHEMA = "analog_v1"
DEFAULTS = {
    "min_n": 20,
    "margin_ratio": 0.15,      # 条件中位 ≥ 基率中位 × (1+margin) 才算"偏高"
    "vol_low_pct": 25.0,
    "vol_high_pct": 75.0,
    "pcr_bottom_pct": 20.0,
    "pcr_top_pct": 80.0,
}


def _load_params(root) -> Dict[str, Any]:
    p = dict(DEFAULTS)
    try:
        from engine.yaml_mini import load

        cfg = load(Path(root) / "config" / "thresholds.yaml")
        av = (cfg or {}).get("analog_v1") or {}
        for k in p:
            if av.get(k) is not None:
                p[k] = float(av[k]) if k not in ("min_n",) else int(av[k])
    except Exception:  # noqa: BLE001
        pass
    return p


def load_episodes(path) -> List[Dict[str, Any]]:
    out = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            try:
                out.append(json.loads(line))
            except Exception:  # noqa: BLE001
                continue
    return out


def build_combined(episodes: List[Dict[str, Any]], root) -> List[Dict[str, Any]]:
    """oi 层 episode（15y）→ 全特征表（无未来泄漏）。

    - vol 分层用 episode 自带的扩张口径 iv_pct（lambdaclass ATM IV 百分位，截至 T）；
    - pcr 分位用扩张口径现算（按 ticker 按日期累计，只用截至 T 的 pcr_oi_near）。
    """
    recs: List[Dict[str, Any]] = []
    for ep in episodes:
        if ep.get("layer") != "oi":
            continue
        i1 = ep["inputs"]
        spot = i1.get("spot")
        flip = i1.get("primary_flip") or i1.get("flip")
        flip_dist = (
            abs(spot / flip - 1.0)
            if (spot and flip and spot > 0 and flip > 0) else None
        )
        recs.append(
            {
                "ticker": ep["ticker"],
                "date": ep["date"],
                "iv_pct": i1.get("iv_pct"),
                "atm_iv": i1.get("atm_iv"),
                "net_gex": i1.get("net_gex"),
                "flip_dist": flip_dist,
                "pcr_oi_near": i1.get("pcr_oi_near"),
                "outcome": ep.get("outcome") or {},
            }
        )
    # pcr 扩张百分位（按 ticker 按日期累计）
    import bisect

    by_t: Dict[str, List[Dict[str, Any]]] = {}
    for r in sorted(recs, key=lambda x: (x["ticker"], x["date"])):
        by_t.setdefault(r["ticker"], []).append(r)
    combined: List[Dict[str, Any]] = []
    for t in sorted(by_t):
        running: List[float] = []
        for r in by_t[t]:
            pcr = r["pcr_oi_near"]
            if pcr is not None:
                pos = bisect.bisect_right(running, pcr)
                running.insert(pos, pcr)
                r["pcr_pct"] = pos / len(running) * 100.0
            else:
                r["pcr_pct"] = None
            combined.append(r)
    return combined


def vol_bucket(iv_pct, p: Dict[str, Any]) -> Optional[str]:
    if iv_pct is None:
        return None
    if iv_pct < p["vol_low_pct"]:
        return "LOW"
    if iv_pct > p["vol_high_pct"]:
        return "HIGH"
    return "MID"


def gamma_sign(net_gex) -> Optional[str]:
    if net_gex is None:
        return None
    return "POSITIVE" if net_gex > 0 else ("NEGATIVE" if net_gex < 0 else "ZERO")


def flip_dist_bucket(flip_dist, p: Dict[str, Any]) -> Optional[str]:
    if flip_dist is None:
        return None
    if flip_dist <= 0.005:
        return "LE0.5%"
    if flip_dist <= 0.01:
        return "LE1%"
    if flip_dist <= 0.02:
        return "LE2%"
    return "GT2%"


def pcr_bucket(pcr_pct, p: Dict[str, Any]) -> Optional[str]:
    if pcr_pct is None:
        return None
    if pcr_pct <= p["pcr_bottom_pct"]:
        return "BOTTOM"
    if pcr_pct >= p["pcr_top_pct"]:
        return "TOP"
    return "MID"


def match_hierarchy(recs: List[Dict[str, Any]], state: Dict[str, Any],
                    p: Dict[str, Any], min_n: int) -> Dict[str, Any]:
    """分层匹配：vol → gamma → flip_dist → pcr。样本 < min_n 即停。"""
    layers = ["vol", "gamma", "flip_dist", "pcr"]
    cur = list(recs)
    reached = 0
    for layer in layers:
        want = state.get(layer)
        if want is None:
            continue
        nxt = []
        for r in cur:
            if layer == "vol" and vol_bucket(r.get("iv_pct"), p) == want:
                nxt.append(r)
            elif layer == "gamma" and gamma_sign(r.get("net_gex")) == want:
                nxt.append(r)
            elif layer == "flip_dist" and flip_dist_bucket(r.get("flip_dist"), p) == want:
                nxt.append(r)
            elif layer == "pcr" and pcr_bucket(r.get("pcr_pct"), p) == want:
                nxt.append(r)
        if len(nxt) < min_n:
            return {
                "matched": False,
                "reached_layer": layer,
                "n_at_stop": len(nxt),
                "n": len(cur),
                "reason": f"匹配到 {layer} 层后样本 {len(nxt)} < min_n {min_n}",
            }
        cur = nxt
        reached += 1
    return {"matched": True, "reached_layer": "all", "n": len(cur), "episodes": cur}


def outcome_stats(recs: List[Dict[str, Any]], horizon: int) -> Dict[str, Any]:
    vals = []
    rvs = []
    maes = []
    for r in recs:
        oc = r.get("outcome") or {}
        v = oc.get(f"ret_{horizon}d")
        if v is not None:
            vals.append(abs(float(v)))
        rv = oc.get("rv_fwd_5d")
        if rv is not None:
            rvs.append(float(rv))
        mae = oc.get("mae_5d")
        if mae is not None:
            maes.append(abs(float(mae)))

    def q(a: List[float], qq: float):
        if not a:
            return None
        s = sorted(a)
        k = (len(s) - 1) * qq
        lo = int(math.floor(k))
        hi = int(math.ceil(k))
        if lo == hi:
            return round(s[lo], 6)
        return round(s[lo] + (s[hi] - s[lo]) * (k - lo), 6)

    return {
        "n": len(vals),
        f"median_abs_ret_{horizon}d": q(vals, 0.5),
        f"p75_abs_ret_{horizon}d": q(vals, 0.75),
        f"p90_abs_ret_{horizon}d": q(vals, 0.90),
        "median_rv5": q(rvs, 0.5),
        "median_abs_mae5": q(maes, 0.5),
    }


def _base_stats(recs: List[Dict[str, Any]], horizon: int) -> Dict[str, Any]:
    return outcome_stats(recs, horizon)


def _match_summary(m: Dict[str, Any]) -> Dict[str, Any]:
    return {k: m[k] for k in ("matched", "reached_layer", "n", "n_at_stop", "reason") if k in m}


def _exceed_base_median(recs: List[Dict[str, Any]], horizon: int,
                        base_median: Optional[float]) -> Tuple[int, int]:
    if base_median is None:
        return 0, 0
    k = n = 0
    for r in recs:
        v = (r.get("outcome") or {}).get(f"ret_{horizon}d")
        if v is None:
            continue
        n += 1
        if abs(float(v)) >= base_median:
            k += 1
    return k, n


def oos_validate(combined: List[Dict[str, Any]], state: Dict[str, Any],
                 freeze_date: str, horizon: int, params: Dict[str, Any]) -> Dict[str, Any]:
    """冻结切分 → 训练集定规则 → 样本外原样复跑 → 证据 + 初步判定（候选阈值）。"""
    min_n = int(params["min_n"])
    margin = float(params["margin_ratio"])
    pre = [r for r in combined if r["date"] < freeze_date]
    post = [r for r in combined if r["date"] >= freeze_date]
    base_pre = _base_stats(pre, horizon)
    base_post = _base_stats(post, horizon)
    m_pre = match_hierarchy(pre, state, params, min_n)
    m_post = match_hierarchy(post, state, params, min_n)
    rec = {
        "schema_version": SCHEMA,
        "ticker": combined[0]["ticker"] if combined else None,
        "freeze_date": freeze_date,
        "state": state,
        "horizon": horizon,
        "n_pre": len(pre),
        "n_post": len(post),
        "base_pre": base_pre,
        "base_post": base_post,
    }
    if not m_pre["matched"] or not m_post["matched"]:
        rec["status"] = "INSUFFICIENT"
        rec["match_pre"] = _match_summary(m_pre)
        rec["match_post"] = _match_summary(m_post)
        return rec
    cond_pre = outcome_stats(m_pre["episodes"], horizon)
    cond_post = outcome_stats(m_post["episodes"], horizon)
    k_pre, n_pre_hit = _exceed_base_median(m_pre["episodes"], horizon, base_pre.get(f"median_abs_ret_{horizon}d"))
    k_post, n_post_hit = _exceed_base_median(m_post["episodes"], horizon, base_post.get(f"median_abs_ret_{horizon}d"))
    ci_pre = wilson_ci(k_pre, n_pre_hit)
    ci_post = wilson_ci(k_post, n_post_hit)
    # 初步判定（候选阈值，不冻结）：OOS 条件中位 ≥ 基率中位 × (1+margin)，且超基率中位占比 CI 不含 50%
    med_key = f"median_abs_ret_{horizon}d"
    oos_med = cond_post.get(med_key)
    oos_base = base_post.get(med_key)
    ratio = (oos_med / oos_base) if (oos_med and oos_base) else None
    ci_ok = ci_post is not None and (ci_post[0] > 0.5 or ci_post[1] < 0.5)
    if ratio is not None and ratio >= 1.0 + margin and ci_ok:
        status = "VALIDATED_HIGHER_VOL"
    elif ratio is not None and ratio <= 1.0 / (1.0 + margin) and ci_ok:
        status = "VALIDATED_LOWER_VOL"
    else:
        status = "NOT_VALIDATED"
    rec.update(
        {
            "status": status,
            "match_pre": {"matched": True, "n": m_pre["n"]},
            "match_post": {"matched": True, "n": m_post["n"]},
            "conditional_pre": cond_pre,
            "conditional_post": cond_post,
            "oos_median_ratio": round(ratio, 3) if ratio is not None else None,
            "exceed_base_median_pre": {"k": k_pre, "n": n_pre_hit,
                                       "ci": [round(x, 4) for x in ci_pre] if ci_pre else None},
            "exceed_base_median_post": {"k": k_post, "n": n_post_hit,
                                        "ci": [round(x, 4) for x in ci_post] if ci_post else None},
            "label": label_for_n(m_post["n"], 20, 60, 120),
            "note": (
                "研究层证据：条件结果分布 vs 基率；VALIDATED_HIGHER/LOWER_VOL 仅表示样本外复现"
                "'该状态后波动偏高/偏低'，不是方向信号，未进日报"
            ),
        }
    )
    return rec


def run_analog(episodes_path, root, tickers, freeze_date, horizons,
               out_path, states=None) -> Dict[str, int]:
    episodes = load_episodes(episodes_path)
    combined = build_combined(episodes, root)
    params = _load_params(root)
    min_n = int(params["min_n"])
    states = states or [
        {"vol": "LOW"},
        {"vol": "HIGH"},
        {"gamma": "NEGATIVE"},
        {"gamma": "POSITIVE"},
        {"flip_dist": "LE1%"},
        {"pcr": "BOTTOM"},
        {"pcr": "TOP"},
        {"vol": "HIGH", "gamma": "NEGATIVE"},
        {"vol": "LOW", "gamma": "POSITIVE"},
        {"gamma": "NEGATIVE", "flip_dist": "LE1%"},
        {"vol": "LOW", "gamma": "NEGATIVE", "flip_dist": "LE1%", "pcr": "BOTTOM"},
        {"vol": "LOW", "gamma": "NEGATIVE", "flip_dist": "LE1%"},
        {"gamma": "NEGATIVE", "flip_dist": "LE0.5%"},
        {"vol": "LOW", "gamma": "NEGATIVE"},
        {"flip_dist": "LE1%", "pcr": "BOTTOM"},
    ]
    # 幂等：跳过已有 (ticker, freeze, state, horizon)
    existing: set = set()
    if out_path.exists():
        with open(out_path, encoding="utf-8") as f:
            for line in f:
                try:
                    r = json.loads(line)
                    existing.add((r.get("ticker"), r.get("freeze_date"),
                                  json.dumps(r.get("state"), sort_keys=True), r.get("horizon")))
                except Exception:  # noqa: BLE001
                    continue
    written = 0
    with open(out_path, "a", encoding="utf-8") as f:
        for t in tickers:
            recs = [r for r in combined if r["ticker"] == t]
            if not recs:
                continue
            for st in states:
                for h in horizons:
                    key = (t, freeze_date, json.dumps(st, sort_keys=True), h)
                    if key in existing:
                        continue
                    rec = oos_validate(recs, st, freeze_date, h, params)
                    rec["ticker"] = t
                    f.write(json.dumps(rec, ensure_ascii=False) + "\n")
                    existing.add(key)
                    written += 1
    return {"written": written, "out": str(out_path)}
