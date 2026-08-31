# -*- coding: utf-8 -*-
"""历史回放引擎 v1（P3-1）：用回填数据批量构造 episode→outcome 样本。

分层（诚实边界，不编造）：
  A. IV 层（18 标的）：data/iv_history + data/closes
     - 条件：IV 滚动百分位（≤20 便宜 / ≥80 贵）、IV−RV spread、期限倒挂
     - 结果：未来 1/3/5D 收益、5D 已实现波动、5D 最大不利偏移（MAE）
  B. Gamma 层（仅 SPY/QQQ/IWM）：lambdaclass parquet（2008-2025，含 OI/IV/Greeks）
     - 条件：Gamma 符号、|现货/Flip−1|≤0.5%、Call/Put Wall 邻近≤1%
     - 结果：同上（closes 用 data/closes，IWM 缺则跳过）
  C. OI 结构层（仅 SPY/QQQ/IWM）：与 live 同口径（metrics.gamma_structure +
     regime_map primary_rule）
     - 特征：Net GEX、Flip（raw + 符号解析 primary_flip）、Wall 质量分级（PRIMARY/WEAK/REMOTE）、
       P/C OI 比（全链 + 近端≤7D）、Net Vanna/Charm
     - 条件：同上；并导出逐日序列 data/oi_history/{TICKER}.csv

纪律：
  - 条件只用截至 T 的数据（滚动/扩张口径），结果只用 T 之后的数据 → 无未来信息泄漏
  - 输出 JSONL（thesis/replay_episodes_v1.jsonl），schema 对齐 episode 记录
"""

from __future__ import annotations

import datetime
import json
import math
from pathlib import Path
from typing import Any, Dict, List, Optional

import numpy as np
import pandas as pd

REPO_ROOT = Path(__file__).resolve().parent.parent
IV_HIST_DIR = REPO_ROOT / "data" / "iv_history"
CLOSES_DIR = REPO_ROOT / "data" / "closes"
LAMBDA_DIR = Path(r"D:\git\EXTERNAL DATA\IAMBDCLASS")
OI_HISTORY_DIR = REPO_ROOT / "data" / "oi_history"

SCHEMA = "replay_v1"
RV_LOOKBACK = 20
IV_PCT_WINDOW = None  # None = 扩张窗口（全部历史，无未来泄漏）
OUTCOME_HORIZONS = (1, 3, 5)


def _closes(ticker: str) -> List[Dict[str, Any]]:
    f = CLOSES_DIR / f"{ticker}.csv"
    if not f.exists():
        # 兜底：lambdaclass underlying parquet（如 IWM 不在 data/closes）
        uf = LAMBDA_DIR / f"{ticker}_underlying.parquet"
        if uf.exists():
            df = pd.read_parquet(uf, columns=["date", "close"])
        else:
            return []
    else:
        df = pd.read_csv(f)
    if not {"date", "close"}.issubset(df.columns):
        return []
    df = df.dropna(subset=["close"]).sort_values("date")
    return [
        {"date": pd.Timestamp(r.date).strftime("%Y-%m-%d"), "close": float(r.close)}
        for r in df.itertuples(index=False)
    ]


def _outcome(closes: List[Dict[str, Any]], idx: int) -> Optional[Dict[str, float]]:
    """未来结果：只用 T 之后的数据。返回 None 表示 T 之后数据不足（不构造样本）。"""
    c0 = closes[idx]["close"]
    if c0 <= 0:
        return None
    out: Dict[str, float] = {}
    n = len(closes)
    for h in OUTCOME_HORIZONS:
        j = idx + h
        if j >= n:
            return None
        out[f"ret_{h}d"] = round(closes[j]["close"] / c0 - 1.0, 6)
    # 5D 已实现波动：T+1..T+5 对数收益 std × √252
    if idx + 6 <= n:
        logrets = [
            math.log(closes[i]["close"] / closes[i - 1]["close"])
            for i in range(idx + 1, min(idx + 6, n))
            if closes[i - 1]["close"] > 0 and closes[i]["close"] > 0
        ]
        if len(logrets) >= 4:
            m = sum(logrets) / len(logrets)
            var = sum((x - m) ** 2 for x in logrets) / (len(logrets) - 1)
            out["rv_fwd_5d"] = round(math.sqrt(var) * math.sqrt(252), 6)
    # 5D 最大不利偏移（MAE）：峰值到谷值的最大回撤
    peak = c0
    mae = 0.0
    for i in range(idx + 1, min(idx + 6, n)):
        c = closes[i]["close"]
        peak = max(peak, c)
        if peak > 0:
            mae = min(mae, c / peak - 1.0)
    out["mae_5d"] = round(mae, 6)
    return out


def _iv_layer(ticker: str, start: Optional[str], end: Optional[str]) -> List[Dict[str, Any]]:
    f = IV_HIST_DIR / f"{ticker}.csv"
    if not f.exists():
        return []
    iv = pd.read_csv(f)
    if not {"date", "atm_iv_near"}.issubset(iv.columns):
        return []
    iv = iv.dropna(subset=["atm_iv_near"]).sort_values("date")
    closes = _closes(ticker)
    cdates = [c["date"] for c in closes]
    close_by_date = {c["date"]: c["close"] for c in closes}
    episodes: List[Dict[str, Any]] = []
    prior_ivs: List[float] = []
    for _, r in iv.iterrows():
        d = str(r["date"])
        if start and d < start:
            continue
        if end and d > end:
            continue
        if d not in close_by_date:
            continue
        idx = cdates.index(d)
        oc = _outcome(closes, idx)
        if oc is None:
            continue
        atm = float(r["atm_iv_near"])
        # 无未来泄漏：百分位只用截至 T 的历史
        prior_ivs.append(atm)
        iv_pct = sum(1 for x in prior_ivs if x <= atm) / len(prior_ivs) * 100.0
        # RV20：截至 T 的 20 日对数收益 std × √252
        logrets = []
        for i in range(max(1, idx - RV_LOOKBACK + 1), idx + 1):
            if closes[i - 1]["close"] > 0 and closes[i]["close"] > 0:
                logrets.append(math.log(closes[i]["close"] / closes[i - 1]["close"]))
        rv20 = None
        if len(logrets) >= 10:
            m = sum(logrets) / len(logrets)
            var = sum((x - m) ** 2 for x in logrets) / (len(logrets) - 1)
            rv20 = math.sqrt(var) * math.sqrt(252)
        conditions: List[str] = []
        if iv_pct <= 20:
            conditions.append("IV_CHEAP")
        if iv_pct >= 80:
            conditions.append("IV_EXPENSIVE")
        spread_pp = None
        if rv20 is not None and rv20 > 0:
            spread_pp = (atm - rv20) * 100.0
            if spread_pp >= 10.0:
                conditions.append("IV_PREMIUM_HIGH")
            if spread_pp <= -10.0:
                conditions.append("IV_PREMIUM_LOW")
        term = r.get("term_ratio")
        if term is not None and float(term) < 0.9:
            conditions.append("TERM_INVERTED")
        episodes.append(
            {
                "schema_version": SCHEMA,
                "ticker": ticker,
                "date": d,
                "layer": "iv",
                "conditions": conditions,
                "inputs": {
                    "atm_iv": round(atm, 4),
                    "rv20": round(rv20, 4) if rv20 is not None else None,
                    "spread_pp": round(spread_pp, 2) if spread_pp is not None else None,
                    "iv_pct": round(iv_pct, 1),
                    "term_ratio": round(float(term), 3) if term is not None else None,
                },
                "outcome": oc,
            }
        )
    return episodes


def _find_flip(strikes, cum):
    for i in range(len(strikes) - 1):
        if cum[i] * cum[i + 1] < 0:
            frac = -cum[i] / (cum[i + 1] - cum[i])
            return float(strikes[i] + (strikes[i + 1] - strikes[i]) * frac)
    return None


_LAMBDA_COLS = [
    "date", "expiration", "strike", "type",
    "open_interest", "gamma", "implied_volatility", "volume",
]


def _gamma_day_features(grp: pd.DataFrame, spot: float) -> Optional[Dict[str, Any]]:
    """lambdaclass 当日全链 → 与 live 同口径的 Gamma/Wall/P-C OI 特征。

    自包含实现：公式与 src/metrics.gamma_structure 逐项一致（GEX = γ×OI×100×S×sign；
    Vanna/Charm 用纯 math 实现 norm.pdf，与 scipy 双精度公式一致），Wall 质量参数
    从 config/thresholds.yaml 读取（与 metrics.WALL_QUALITY_V1 同源）。这样本地无
    scipy 也能跑，且与每日报告口径一致。
    """
    from src.data_fetcher import RISK_FREE_RATE

    d = pd.Timestamp(grp["date"].iloc[0])
    exp = pd.to_datetime(grp["expiration"])
    g = pd.DataFrame(
        {
            "strike": pd.to_numeric(grp["strike"], errors="coerce").values,
            "type": grp["type"].astype(str).str.lower().values,
            "gamma": pd.to_numeric(grp["gamma"], errors="coerce").values,
            "open_interest": pd.to_numeric(grp["open_interest"], errors="coerce").values,
            "dte": ((exp - d) / pd.Timedelta(days=1)).clip(lower=1).values,
            "iv": pd.to_numeric(grp["implied_volatility"], errors="coerce").values,
            "volume": pd.to_numeric(grp["volume"], errors="coerce").fillna(0).values,
        }
    )
    g = g[g["type"].isin(["call", "put"])].copy()
    g = g[g["gamma"].notna() & (g["open_interest"] > 0)]
    if g.empty:
        return None
    g["dte"] = g["dte"].clip(lower=1)
    t = g["dte"] / 365.0
    sign = np.where(g["type"] == "call", 1.0, -1.0)
    g["gex"] = g["gamma"].values * g["open_interest"].values * 100.0 * spot * sign
    iv = g["iv"].fillna(0.25).clip(lower=0.05)
    sqt = np.sqrt(t)
    d1 = (np.log(spot / g["strike"]) + (RISK_FREE_RATE + iv ** 2 / 2.0) * t) / (iv * sqt)
    d2 = d1 - iv * sqt
    phi = np.exp(-0.5 * d1 ** 2) / np.sqrt(2.0 * np.pi)
    g["vanna"] = -phi * d2 / iv
    g["charm"] = phi * (
        (RISK_FREE_RATE + iv ** 2 / 2.0) / (2.0 * iv * sqt)
        - np.log(spot / g["strike"]) / (2.0 * iv * t ** 1.5)
    )
    g["vanna_expo"] = g["vanna"] * g["open_interest"].values * 100.0 * sign
    g["charm_expo"] = g["charm"] * g["open_interest"].values * 100.0 * sign

    by_strike = g.groupby("strike")["gex"].sum().sort_index()
    cum = by_strike.cumsum()
    net_gex = float(cum.iloc[-1]) if len(cum) else None
    flip = _find_flip(by_strike.index.values, cum.values)
    # 符号解析最近穿越（与 live regime_map primary_rule 同口径）：
    #   正 GEX → 现价下方最近零交叉；负 GEX → 现价上方最近零交叉。
    # oi_history/回放的 NEAR_FLIP 必须用这个 primary_flip，才能与报告对齐。
    strikes_v = by_strike.index.values
    cum_v = cum.values
    crossings: List[float] = []
    for i in range(len(strikes_v) - 1):
        if cum_v[i] * cum_v[i + 1] < 0:
            frac = -cum_v[i] / (cum_v[i + 1] - cum_v[i])
            crossings.append(float(strikes_v[i] + (strikes_v[i + 1] - strikes_v[i]) * frac))
    primary_flip = None
    if crossings and net_gex is not None:
        if net_gex > 0:
            below = [f for f in crossings if f < spot]
            primary_flip = max(below) if below else None
        elif net_gex < 0:
            above = [f for f in crossings if f > spot]
            primary_flip = min(above) if above else None
    call_oi = g[g["type"] == "call"].groupby("strike")["open_interest"].sum()
    put_oi = g[g["type"] == "put"].groupby("strike")["open_interest"].sum()
    call_wall_raw = float(call_oi.idxmax()) if not call_oi.empty else None
    put_wall_raw = float(put_oi.idxmax()) if not put_oi.empty else None
    params = _wall_quality_params()
    call_q = _classify_wall_replay(call_oi, call_wall_raw, spot, params)
    put_q = _classify_wall_replay(put_oi, put_wall_raw, spot, params)
    call_wall = call_q["strike"] if call_q and call_q["classification"] != "REMOTE" else None
    put_wall = put_q["strike"] if put_q and put_q["classification"] != "REMOTE" else None

    call_oi_tot = float(call_oi.sum())
    put_oi_tot = float(put_oi.sum())
    pcr_all = put_oi_tot / call_oi_tot if call_oi_tot > 0 else None
    near = g[g["dte"] <= 7]
    call_n = float(near.loc[near["type"] == "call", "open_interest"].sum())
    put_n = float(near.loc[near["type"] == "put", "open_interest"].sum())
    pcr_near = put_n / call_n if call_n > 0 else None
    return {
        "spot": round(spot, 2),
        "net_gex": round(net_gex, 0) if net_gex is not None else None,
        "flip": round(flip, 2) if flip is not None else None,
        "primary_flip": round(primary_flip, 2) if primary_flip is not None else None,
        "call_wall": call_wall,
        "put_wall": put_wall,
        "call_wall_class": call_q["classification"] if call_q else None,
        "put_wall_class": put_q["classification"] if put_q else None,
        "pcr_oi_all": round(pcr_all, 3) if pcr_all is not None else None,
        "pcr_oi_near": round(pcr_near, 3) if pcr_near is not None else None,
        "net_vanna": round(float(g["vanna_expo"].sum()), 0),
        "net_charm": round(float(g["charm_expo"].sum()), 0),
    }


def _wall_quality_params() -> Dict[str, float]:
    """Wall 质量参数：优先 config/thresholds.yaml（与 metrics.WALL_QUALITY_V1 同源）。"""
    defaults = {"distance_cap_pct": 10.0, "dominance_min": 1.5, "strength_median_mult": 3.0}
    try:
        from engine.yaml_mini import load

        cfg = load(REPO_ROOT / "config" / "thresholds.yaml")
        wq = (cfg or {}).get("wall_quality_v1") or {}
        for k in defaults:
            v = wq.get(k)
            if v is not None:
                defaults[k] = float(v)
    except Exception:  # noqa: BLE001
        pass
    return defaults


def _classify_wall_replay(oi_series, wall_strike, spot, params):
    """镜像 src.metrics._classify_wall（Wall 质量分级 v1），保证回放与 live 判定一致。"""
    if oi_series is None or oi_series.empty or wall_strike is None or spot is None:
        return None
    wall_strike = float(wall_strike)
    wall_oi = float(oi_series.loc[wall_strike])
    if wall_oi <= 0:
        return None
    distance_pct = (wall_strike / spot - 1.0) * 100.0
    nz = oi_series[oi_series > 0]
    others = nz.drop(wall_strike) if wall_strike in nz.index else nz
    dominance = wall_oi / float(others.max()) if not others.empty else None
    median_nz = float(nz.median()) if not nz.empty else 0.0
    strength = "HIGH" if wall_oi >= params["strength_median_mult"] * median_nz else "LOW"
    dist_ok = abs(distance_pct) <= params["distance_cap_pct"]
    dom_ok = dominance is not None and dominance >= params["dominance_min"]
    if not dist_ok:
        classification = "REMOTE"
    elif dom_ok and strength == "HIGH":
        classification = "PRIMARY"
    else:
        classification = "WEAK"
    return {
        "strike": wall_strike,
        "oi": round(wall_oi, 0),
        "distance_pct": round(distance_pct, 2),
        "dominance": round(dominance, 2) if dominance is not None else None,
        "strength": strength,
        "classification": classification,
    }


def _oi_layer(ticker: str, start: Optional[str], end: Optional[str]) -> List[Dict[str, Any]]:
    """OI 结构层（SPY/QQQ/IWM）：逐日 GEX/Flip/质量 Wall/P-C OI/Vanna/Charm + 未来结果。"""
    pf = LAMBDA_DIR / f"{ticker}_options.parquet"
    if not pf.exists():
        return []
    df = pd.read_parquet(pf, columns=_LAMBDA_COLS)
    closes = _closes(ticker)
    if not closes:
        return []
    cdates = [c["date"] for c in closes]
    close_by_date = {c["date"]: c["close"] for c in closes}
    df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")
    episodes: List[Dict[str, Any]] = []
    for d, grp in df.groupby("date"):
        if start and d < start:
            continue
        if end and d > end:
            continue
        if d not in close_by_date:
            continue
        spot = close_by_date[d]
        idx = cdates.index(d)
        oc = _outcome(closes, idx)
        if oc is None:
            continue
        feats = _gamma_day_features(grp, spot)
        if feats is None:
            continue
        conditions: List[str] = []
        gamma_sign = "POSITIVE" if (feats["net_gex"] or 0) >= 0 else "NEGATIVE"
        conditions.append(f"GAMMA_{gamma_sign}")
        flip = feats["primary_flip"] or feats["flip"]
        if flip and spot > 0 and abs(spot / flip - 1.0) <= 0.005:
            conditions.append("NEAR_FLIP")
        # 只对通过质量分级的 Wall（PRIMARY/WEAK）判邻近，REMOTE 不算
        for w in (feats["call_wall"], feats["put_wall"]):
            if w and spot > 0 and abs(spot / w - 1.0) <= 0.01:
                conditions.append("NEAR_WALL")
        episodes.append(
            {
                "schema_version": SCHEMA,
                "ticker": ticker,
                "date": d,
                "layer": "oi",
                "conditions": conditions,
                "inputs": feats,
                "outcome": oc,
            }
        )
    return episodes


def write_oi_history(tickers: List[str], start: Optional[str] = None,
                     end: Optional[str] = None) -> Dict[str, int]:
    """导出逐日 OI 结构序列：data/oi_history/{TICKER}.csv（全量重建，确定性）。

    列：date, spot, net_gex, flip, primary_flip, call_wall, put_wall,
        call_wall_class, put_wall_class, pcr_oi_all, pcr_oi_near, net_vanna, net_charm
    """
    OI_HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    stats: Dict[str, int] = {}
    for t in tickers:
        pf = LAMBDA_DIR / f"{t}_options.parquet"
        if not pf.exists():
            continue
        df = pd.read_parquet(pf, columns=_LAMBDA_COLS)
        closes = _closes(t)
        if not closes:
            continue
        close_by_date = {c["date"]: c["close"] for c in closes}
        df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")
        rows: List[Dict[str, Any]] = []
        for d, grp in df.groupby("date"):
            if start and d < start:
                continue
            if end and d > end:
                continue
            if d not in close_by_date:
                continue
            feats = _gamma_day_features(grp, close_by_date[d])
            if feats is None:
                continue
            rows.append({"date": d, **feats})
        if rows:
            out = OI_HISTORY_DIR / f"{t}.csv"
            pd.DataFrame(rows).to_csv(out, index=False)
            stats[t] = len(rows)
    return stats


def _gamma_layer(ticker: str, start: Optional[str], end: Optional[str]) -> List[Dict[str, Any]]:
    pf = LAMBDA_DIR / f"{ticker}_options.parquet"
    if not pf.exists():
        return []
    cols = ["date", "strike", "type", "open_interest", "gamma"]
    df = pd.read_parquet(pf, columns=cols)
    right_col = "right" if "right" in df.columns else "type"
    closes = _closes(ticker)
    if not closes:
        return []
    cdates = [c["date"] for c in closes]
    close_by_date = {c["date"]: c["close"] for c in closes}
    df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")
    episodes: List[Dict[str, Any]] = []
    for d, grp in df.groupby("date"):
        if start and d < start:
            continue
        if end and d > end:
            continue
        if d not in close_by_date:
            continue
        spot = close_by_date[d]
        idx = cdates.index(d)
        oc = _outcome(closes, idx)
        if oc is None:
            continue
        g = grp.dropna(subset=["gamma", "open_interest"])
        g = g[g["open_interest"] > 0]
        if g.empty:
            continue
        is_call = g[right_col].astype(str).str.upper().str.startswith("C")
        sign = pd.Series([1.0 if c else -1.0 for c in is_call], index=g.index)
        g = g.assign(gex=g["gamma"].values * g["open_interest"].values * 100.0 * spot * sign.values)
        by_strike = g.groupby("strike")["gex"].sum().sort_index()
        cum = by_strike.cumsum()
        net_gex = float(cum.iloc[-1]) if len(cum) else None
        flip = _find_flip(by_strike.index.values, cum.values)
        call_oi = g[is_call].groupby("strike")["open_interest"].sum()
        put_oi = g[~is_call].groupby("strike")["open_interest"].sum()
        call_wall = float(call_oi.idxmax()) if not call_oi.empty else None
        put_wall = float(put_oi.idxmax()) if not put_oi.empty else None
        conditions: List[str] = []
        gamma_sign = "POSITIVE" if (net_gex or 0) >= 0 else "NEGATIVE"
        conditions.append(f"GAMMA_{gamma_sign}")
        if flip and spot > 0 and abs(spot / flip - 1.0) <= 0.005:
            conditions.append("NEAR_FLIP")
        for w in (call_wall, put_wall):
            if w and spot > 0 and abs(spot / w - 1.0) <= 0.01:
                conditions.append("NEAR_WALL")
        episodes.append(
            {
                "schema_version": SCHEMA,
                "ticker": ticker,
                "date": d,
                "layer": "gamma",
                "conditions": conditions,
                "inputs": {
                    "spot": round(spot, 2),
                    "net_gex": round(net_gex, 0) if net_gex is not None else None,
                    "flip": round(flip, 2) if flip is not None else None,
                    "call_wall": call_wall,
                    "put_wall": put_wall,
                },
                "outcome": oc,
            }
        )
    return episodes


def run_replay(tickers: List[str], start: Optional[str] = None, end: Optional[str] = None,
               layers: Optional[List[str]] = None,
               out: Optional[Path] = None) -> Dict[str, int]:
    layers = layers or ["iv", "gamma"]
    out = out or (REPO_ROOT / "thesis" / "replay_episodes_v1.jsonl")
    out.parent.mkdir(parents=True, exist_ok=True)
    # 幂等：跳过已存在的 (ticker, date, layer)，避免重复跑污染统计
    existing: set = set()
    if out.exists():
        with open(out, encoding="utf-8") as f:
            for line in f:
                try:
                    r = json.loads(line)
                    existing.add((r["ticker"], r["date"], r["layer"]))
                except Exception:  # noqa: BLE001
                    continue
    total = 0
    stats: Dict[str, int] = {}
    with open(out, "a", encoding="utf-8") as fh:
        for t in tickers:
            eps = []
            if "iv" in layers:
                eps += _iv_layer(t, start, end)
            if "gamma" in layers:
                eps += _gamma_layer(t, start, end)
            if "oi" in layers:
                eps += _oi_layer(t, start, end)
            new = 0
            for e in eps:
                key = (e["ticker"], e["date"], e["layer"])
                if key in existing:
                    continue
                fh.write(json.dumps(e, ensure_ascii=False) + "\n")
                existing.add(key)
                new += 1
            stats[t] = new
            total += new
    stats["_total"] = total
    stats["_out"] = str(out)
    return stats
