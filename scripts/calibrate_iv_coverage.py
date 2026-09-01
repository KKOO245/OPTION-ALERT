#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""IV 三态分类实证校准（研究层，P 待办）：覆盖率是否与结构可靠性相关？

问题：coverage_v1 的 VALID/LOW/INVALID 分类 + 80% 门槛是否是"候选参数"还是
有实证依据？用 lambdaclass 15 年全链做首次检验：
  - 每日计算带内 OI 加权有效覆盖率（与 coverage_v1 同口径）；
  - 结构可靠性代理：primary_flip 的 1 日变动（|flip(t+1)−flip(t)|/spot(t)）——
    低覆盖率日若 flip 更不稳定，说明覆盖确实影响结构质量；
  - 输出：coverage 分布、低/高覆盖分桶下的 flip 稳定性、Spearman 相关。

只做研究层（thesis/iv_coverage_calibration.jsonl），不改变生产判定。

用法：python scripts/calibrate_iv_coverage.py [--tickers SPY QQQ]
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd

REPO_ROOT = Path(__file__).resolve().parent.parent
LAMBDA_DIR = Path(r"D:\git\EXTERNAL DATA\IAMBDCLASS")
OUT = REPO_ROOT / "thesis" / "iv_coverage_calibration.jsonl"
BAND_PCT = 15.0
WEIGHT = {"VALID": 1.0, "LOW_LIQUIDITY": 0.5, "INVALID": 0.0}


def _tickers() -> list[str]:
    out = []
    for line in (REPO_ROOT / "config" / "tickers.txt").read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if s and not s.startswith("#"):
            out.append(s.upper())
    return out


def _closes(t: str) -> pd.DataFrame:
    df = pd.read_csv(REPO_ROOT / "data" / "closes" / f"{t}.csv")
    df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")
    return df[["date", "close"]].dropna()


def _spearman(a: np.ndarray, b: np.ndarray) -> float:
    """Spearman 秩相关（无 scipy 依赖）。"""
    mask = ~(np.isnan(a) | np.isnan(b))
    a, b = a[mask], b[mask]
    if len(a) < 3:
        return float("nan")

    def _rank(x):
        order = x.argsort()
        ranks = np.empty_like(x, dtype=float)
        ranks[order] = np.arange(1, len(x) + 1)
        # 处理并列：取平均秩
        _, inv, cnt = np.unique(x, return_inverse=True, return_counts=True)
        for v, c in zip(np.unique(x), cnt):
            if c > 1:
                idx = np.where(x == v)[0]
                ranks[idx] = ranks[idx].mean()
        return ranks

    ra, rb = _rank(a), _rank(b)
    if ra.std() == 0 or rb.std() == 0:
        return float("nan")
    return float(np.corrcoef(ra, rb)[0, 1])


def calibrate(t: str) -> dict:
    pf = LAMBDA_DIR / f"{t}_options.parquet"
    if not pf.exists():
        return {"ticker": t, "status": "NO_DATA"}
    cols = ["date", "strike", "open_interest", "implied_volatility", "last", "bid", "ask"]
    df = pd.read_parquet(pf, columns=cols)
    df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")
    iv = pd.to_numeric(df["implied_volatility"], errors="coerce")
    oi = pd.to_numeric(df["open_interest"], errors="coerce")
    last = pd.to_numeric(df["last"], errors="coerce")
    bid = pd.to_numeric(df["bid"], errors="coerce")
    ask = pd.to_numeric(df["ask"], errors="coerce")
    invalid = iv.isna() | (iv <= 0) | oi.isna() | (oi <= 0)
    low = (~invalid) & ((last.isna() | (last <= 0)) | (bid.isna() | (bid <= 0)) | (ask.isna() | (ask <= 0)))
    w = np.where(invalid, 0.0, np.where(low, 0.5, 1.0))
    df = df.assign(_w=w, _oi=oi.fillna(0.0), _iv=iv)
    closes = _closes(t)
    close_map = dict(zip(closes["date"], closes["close"]))
    df["_spot"] = df["date"].map(close_map)
    df = df.dropna(subset=["_spot"])
    in_band = (df["strike"] / df["_spot"] - 1.0).abs() <= BAND_PCT / 100.0
    g = df[in_band].groupby("date")
    cov = (g.apply(lambda x: float((x["_oi"] * x["_w"]).sum()) / float(x["_oi"].sum()) * 100.0
                   if x["_oi"].sum() > 0 else np.nan, include_groups=False))
    cov = cov.rename("coverage").reset_index()
    # flip 稳定性（来自 oi_history primary_flip）
    oh = pd.read_csv(REPO_ROOT / "data" / "oi_history" / f"{t}.csv")
    oh = oh[["date", "spot", "primary_flip"]].dropna(subset=["primary_flip"]).sort_values("date")
    oh["flip_next"] = oh["primary_flip"].shift(-1)
    oh = oh.dropna(subset=["flip_next"])
    oh["flip_instab"] = (oh["flip_next"] - oh["primary_flip"]).abs() / oh["spot"] * 100.0
    m = cov.merge(oh[["date", "flip_instab"]], on="date", how="inner").dropna()
    if m.empty:
        return {"ticker": t, "status": "INSUFFICIENT", "n": 0}
    lo = m[m["coverage"] < 80.0]
    hi = m[m["coverage"] >= 80.0]
    spearman = _spearman(m["coverage"].to_numpy(dtype=float), m["flip_instab"].to_numpy(dtype=float))
    out = {
        "ticker": t,
        "status": "OK",
        "n": len(m),
        "coverage": {
            "mean": round(float(m["coverage"].mean()), 1),
            "p10": round(float(m["coverage"].quantile(0.10)), 1),
            "median": round(float(m["coverage"].median()), 1),
            "p90": round(float(m["coverage"].quantile(0.90)), 1),
            "below_80_pct": round(float((m["coverage"] < 80).mean() * 100), 1),
        },
        "flip_instab_pct": {
            "overall_median": round(float(m["flip_instab"].median()), 4),
            "low_cov_lt80_median": round(float(lo["flip_instab"].median()), 4) if len(lo) else None,
            "high_cov_ge80_median": round(float(hi["flip_instab"].median()), 4) if len(hi) else None,
            "n_low": int(len(lo)),
            "n_high": int(len(hi)),
        },
        "spearman_corr": round(float(spearman), 3) if spearman == spearman else None,
        "note": (
            "研究层：带内OI加权覆盖率 vs 次日Flip变动；spearman 为负=覆盖越高结构越稳。"
            "阈值为候选，本结果用于判断 80% 门槛是否有实证依据。"
        ),
    }
    return out


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:  # noqa: BLE001
        pass
    p = argparse.ArgumentParser(description="IV 三态分类实证校准（研究层）")
    p.add_argument("--tickers", nargs="*", help="默认全部（无 oi_history 的会自动跳过）")
    args = p.parse_args()
    tickers = [t.upper() for t in args.tickers] if args.tickers else _tickers()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    existing = set()
    if OUT.exists():
        with open(OUT, encoding="utf-8") as f:
            for line in f:
                try:
                    existing.add(json.loads(line).get("ticker"))
                except Exception:  # noqa: BLE001
                    continue
    with open(OUT, "a", encoding="utf-8") as f:
        for t in tickers:
            if t in existing:
                continue
            r = calibrate(t)
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
            if r["status"] == "OK":
                print(
                    f"[cov] {t}: n={r['n']} 覆盖中位={r['coverage']['median']}% "
                    f"<80%占比={r['coverage']['below_80_pct']}% | "
                    f"flip不稳 低覆盖={r['flip_instab_pct']['low_cov_lt80_median']}% vs "
                    f"高覆盖={r['flip_instab_pct']['high_cov_ge80_median']}% | "
                    f"spearman={r['spearman_corr']}",
                    flush=True,
                )
            else:
                print(f"[cov] {t}: {r['status']}", flush=True)
    print(f"[cov] 完成 → {OUT}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
