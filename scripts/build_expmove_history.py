#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从 ThetaData EOD 原始数据重建逐日 ExpMove 历史（P1，后台研究库）。

口径（与 live expmove_v1 同源）：
  - 每个交易日 × 每个期限：ATM 行权价 = |strike/现货收盘 − 1| 最小；
  - ATM 跨式 = 该行权价 call/put 的 mid（bid/ask 有效取 mid，否则用 close）；
  - expmove_pct = (call_mid + put_mid) / 现货收盘 × 100。

输出：data/expmove_history/{TICKER}.csv（date, expiration, dte, expmove_pct, atm_strike）
用途：ExpMove Calibration（市场定价的波动范围历史上有多可靠）。
只做研究层，不进报告/评分。

用法：
  python scripts/build_expmove_history.py --tickers QQQ          # 指定
  python scripts/build_expmove_history.py                        # 全部 18 个
"""

from __future__ import annotations

import argparse
import glob
import os
import sys
from pathlib import Path

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = Path(
    os.environ.get("THETADATA_RAW_DIR")
    or r"D:\git\EXTERNAL DATA\OPTION-ALERT-RAW\thetadata"
)
OUT_DIR = REPO_ROOT / "data" / "expmove_history"


def _tickers() -> list[str]:
    out = []
    for line in (REPO_ROOT / "config" / "tickers.txt").read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if s and not s.startswith("#"):
            out.append(s.upper())
    return out


def _mid(row) -> float:
    bid, ask, close = row.get("bid"), row.get("ask"), row.get("close")
    try:
        b, a = float(bid), float(ask)
        if b > 0 and a > 0 and a >= b:
            return (b + a) / 2.0
    except (TypeError, ValueError):
        pass
    try:
        c = float(close)
        if c > 0:
            return c
    except (TypeError, ValueError):
        pass
    return float("nan")


def build_ticker(t: str) -> int:
    tdir = RAW_DIR / t
    if not tdir.is_dir():
        print(f"[expmove] {t}: RAW 目录缺失，跳过", flush=True)
        return 0
    files = sorted(glob.glob(str(tdir / "*.parquet")))
    if not files:
        print(f"[expmove] {t}: 无 parquet 分块", flush=True)
        return 0
    frames = []
    for f in files:
        try:
            frames.append(pd.read_parquet(f))
        except Exception as e:  # noqa: BLE001
            print(f"[expmove] {t} 读取 {Path(f).name} 失败: {e}", flush=True)
    if not frames:
        return 0
    df = pd.concat(frames, ignore_index=True)
    need = {"date", "expiration", "strike", "right", "close"}
    has_date = "date" in df.columns
    has_created = "created" in df.columns
    if not has_date and not has_created:
        print(f"[expmove] {t}: 缺日期列（date/created），列={list(df.columns)}", flush=True)
        return 0
    missing = {"expiration", "strike", "right", "close"} - set(df.columns)
    if missing:
        print(f"[expmove] {t}: 列缺失 {missing}", flush=True)
        return 0
    if has_created:
        df["date"] = (
            pd.to_datetime(df["created"], errors="coerce")
            .dt.tz_localize(None)
            .dt.normalize()
        )
    else:
        df["date"] = pd.to_datetime(df["date"], errors="coerce").dt.normalize()
    df = df[df["right"].astype(str).str.upper().str[0].isin(["C", "P"])].copy()
    df["expiration"] = pd.to_datetime(df["expiration"], errors="coerce").dt.normalize()
    df = df.dropna(subset=["date", "expiration", "strike"])
    df = df[df["strike"] > 0]
    # 现货收盘（data/closes 全历史）
    cf = REPO_ROOT / "data" / "closes" / f"{t}.csv"
    if not cf.exists():
        print(f"[expmove] {t}: 无 data/closes，跳过", flush=True)
        return 0
    closes = pd.read_csv(cf)
    closes["date"] = pd.to_datetime(closes["date"]).dt.normalize()
    closes = closes[["date", "close"]].dropna().rename(columns={"close": "spot"})
    df = df.merge(closes, on="date", how="inner")
    df = df[df["spot"] > 0]
    df["dte"] = (df["expiration"] - df["date"]).dt.days
    df = df[df["dte"] >= 1]
    # ATM 行权价：每个 (date, expiration) 取 |strike/spot−1| 最小
    df["abs_money"] = (df["strike"] / df["spot"] - 1.0).abs()
    g = df.groupby(["date", "expiration"], as_index=False)["abs_money"].min()
    atm = df.merge(g, on=["date", "expiration", "abs_money"], how="inner")
    atm = atm.drop_duplicates(subset=["date", "expiration", "right"])
    atm["mid"] = atm.apply(_mid, axis=1)
    calls = atm[atm["right"].str.upper().str[0] == "C"].set_index(["date", "expiration"])["mid"]
    puts = atm[atm["right"].str.upper().str[0] == "P"].set_index(["date", "expiration"])["mid"]
    spot_map = atm.drop_duplicates(subset=["date", "expiration"])[
        ["date", "expiration", "spot", "strike", "dte"]
    ].set_index(["date", "expiration"])
    out = spot_map.join(calls.rename("cmid")).join(puts.rename("pmid")).dropna(subset=["cmid", "pmid"])
    out = out[(out["cmid"] > 0) & (out["pmid"] > 0)]
    out["expmove_pct"] = ((out["cmid"] + out["pmid"]) / out["spot"] * 100.0).round(4)
    out = out.reset_index()
    out = out[["date", "expiration", "dte", "strike", "expmove_pct"]].sort_values(
        ["date", "expiration"]
    )
    out["date"] = out["date"].dt.strftime("%Y-%m-%d")
    out["expiration"] = out["expiration"].dt.strftime("%Y-%m-%d")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out.to_csv(OUT_DIR / f"{t}.csv", index=False)
    print(
        f"[expmove] {t}: {len(out)} 条 (date×expiry) → {OUT_DIR / (t + '.csv')} | "
        f"范围 {out['date'].min()} ~ {out['date'].max()}",
        flush=True,
    )
    return len(out)


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:  # noqa: BLE001
        pass
    p = argparse.ArgumentParser(description="重建 ExpMove 历史（ThetaData EOD）")
    p.add_argument("--tickers", nargs="*", help="默认全部 18 个")
    args = p.parse_args()
    tickers = [t.upper() for t in args.tickers] if args.tickers else _tickers()
    total = 0
    for t in tickers:
        total += build_ticker(t)
    print(f"[expmove] 完成：{len(tickers)} 标的，共 {total} 条 (date×expiry) 记录", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
