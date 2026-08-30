# -*- coding: utf-8 -*-
"""历史回放引擎 v1（P3-1）：用回填数据批量构造 episode→outcome 样本。

分层（诚实边界，不编造）：
  A. IV 层（18 标的）：data/iv_history + data/closes
     - 条件：IV 滚动百分位（≤20 便宜 / ≥80 贵）、IV−RV spread、期限倒挂
     - 结果：未来 1/3/5D 收益、5D 已实现波动、5D 最大不利偏移（MAE）
  B. Gamma 层（仅 SPY/QQQ/IWM）：lambdaclass parquet（2008-2025，含 OI/IV/Greeks）
     - 条件：Gamma 符号、|现货/Flip−1|≤0.5%、Call/Put Wall 邻近≤1%
     - 结果：同上（closes 用 data/closes，IWM 缺则跳过）

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

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parent.parent
IV_HIST_DIR = REPO_ROOT / "data" / "iv_history"
CLOSES_DIR = REPO_ROOT / "data" / "closes"
LAMBDA_DIR = Path(r"D:\git\EXTERNAL DATA\IAMBDCLASS")

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
