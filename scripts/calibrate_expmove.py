#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ExpMove Calibration（P1，研究层）：市场定价的波动范围历史上有多可靠。

口径：
  - 对每个交易日 t：取 dte ∈ {1..5} 的期限，expmove = expmove_pct/100（± 范围）；
  - 实际 |h 日移动| = |close[t+h]/close[t] − 1|，h = 该期限 dte（≤5 时）；
  - coverage_h = 样本中 |实际移动| ≤ expmove 的占比（衡量"定价范围是否够宽"）；
  - ratio = 实际移动 / expmove（>1 表示实际超出定价范围）。
只做研究层（thesis/expmove_calibration.jsonl），不进报告/评分。

用法：python scripts/calibrate_expmove.py [--tickers ...]
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parent.parent
HIST_DIR = REPO_ROOT / "data" / "expmove_history"
OUT = REPO_ROOT / "thesis" / "expmove_calibration.jsonl"
MAX_DTE = 5


def _tickers() -> list[str]:
    out = []
    for line in (REPO_ROOT / "config" / "tickers.txt").read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if s and not s.startswith("#"):
            out.append(s.upper())
    return out


def _load_closes(t: str) -> pd.DataFrame:
    df = pd.read_csv(REPO_ROOT / "data" / "closes" / f"{t}.csv")
    df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")
    return df[["date", "close"]].dropna().sort_values("date").reset_index(drop=True)


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:  # noqa: BLE001
        pass
    p = argparse.ArgumentParser(description="ExpMove 校准（研究层）")
    p.add_argument("--tickers", nargs="*", help="默认全部")
    args = p.parse_args()
    tickers = [t.upper() for t in args.tickers] if args.tickers else _tickers()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    records = []
    existing_keys: set = set()
    if OUT.exists():
        with open(OUT, encoding="utf-8") as fh:
            for line in fh:
                try:
                    r = json.loads(line)
                    existing_keys.add((r.get("ticker"), r.get("dte")))
                except Exception:  # noqa: BLE001
                    continue
    for t in tickers:
        f = HIST_DIR / f"{t}.csv"
        if not f.exists():
            print(f"[calib] {t}: 无 expmove_history，跳过", flush=True)
            continue
        hist = pd.read_csv(f)
        closes = _load_closes(t)
        close_map = dict(zip(closes["date"], closes["close"]))
        dates = closes["date"].tolist()
        idx = {d: i for i, d in enumerate(dates)}
        # 每个交易日 t：dte ∈ [1,5] 的期限 → h 日实际移动
        rows = []
        for r in hist.itertuples(index=False):
            d = str(r.date)
            dte = int(r.dte)
            if dte < 1 or dte > MAX_DTE:
                continue
            i = idx.get(d)
            j = i + dte if i is not None else None
            if j is None or j >= len(dates):
                continue
            c0, c1 = close_map.get(d), close_map.get(dates[j])
            if not c0 or not c1 or c0 <= 0:
                continue
            actual = abs(c1 / c0 - 1.0)
            rows.append((dte, float(r.expmove_pct) / 100.0, actual))
        if not rows:
            print(f"[calib] {t}: 无匹配样本", flush=True)
            continue
        df = pd.DataFrame(rows, columns=["dte", "expmove", "actual"])
        df["ratio"] = df["actual"] / df["expmove"]
        for dte in sorted(df["dte"].unique()):
            if (t, int(dte)) in existing_keys:
                continue  # 已校准过（幂等）
            sub = df[df["dte"] == dte]
            n = len(sub)
            coverage = (sub["actual"] <= sub["expmove"]).mean() * 100.0
            med_r = sub["ratio"].median()
            p75_r = sub["ratio"].quantile(0.75)
            p90_r = sub["ratio"].quantile(0.90)
            med_act = sub["actual"].median() * 100.0
            records.append(
                {
                    "schema_version": "expmove_calibration_v1",
                    "ticker": t,
                    "dte": int(dte),
                    "n": int(n),
                    "coverage_pct": round(coverage, 1),
                    "median_actual_pct": round(med_act, 3),
                    "median_ratio": round(med_r, 3),
                    "p75_ratio": round(p75_r, 3),
                    "p90_ratio": round(p90_r, 3),
                    "basis": "ThetaData EOD ATM straddle vs 实际 |h日移动|，h=dte",
                }
            )
        print(
            f"[calib] {t}: {len(df)} 样本，dte 1~5 coverage 中位 "
            f"{df.groupby('dte').apply(lambda g:(g['actual']<=g['expmove']).mean()*100).median():.1f}%",
            flush=True,
        )
    with open(OUT, "a", encoding="utf-8") as fh:
        for rec in records:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(f"[calib] 完成：{len(records)} 条记录 → {OUT}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
