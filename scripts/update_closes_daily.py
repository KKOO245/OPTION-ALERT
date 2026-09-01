#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""每日收盘价更新（workflow 后台自动维护）：把 yfinance 已收盘日线追加进 data/closes。

口径与回填一致：yf.Ticker.history(auto_adjust=False) —— Close 已拆股调整、未含股息
（与 data/closes 现有 close 列同一口径），adj_close 全调整。
只追加严格早于今天的日期（防盘中/未收盘污染）；断点续传 + 去重。
失败只警告不中断（closes 是辅助数据）。

作用：live episodes 与 IV-RV（pricing_proxy）都依赖 data/closes，双周刷新会滞后，
改为每个报告时段自动补，保证数据时效。

用法：python scripts/update_closes_daily.py [--tickers ...]
"""

from __future__ import annotations

import argparse
import datetime
import sys
from pathlib import Path

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parent.parent
CLOSES_DIR = REPO_ROOT / "data" / "closes"


def _tickers() -> list[str]:
    out = []
    for line in (REPO_ROOT / "config" / "tickers.txt").read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if s and not s.startswith("#"):
            out.append(s.upper())
    return out


def update_ticker(t: str) -> int:
    path = CLOSES_DIR / f"{t}.csv"
    if not path.exists():
        return 0
    try:
        df = pd.read_csv(path)
    except Exception as e:  # noqa: BLE001
        print(f"[closes] {t} 读取失败: {e}", flush=True)
        return 0
    if "date" not in df.columns or "close" not in df.columns:
        return 0
    df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")
    last = df["date"].max()
    end = (datetime.date.today() - datetime.timedelta(days=1)).isoformat()
    if last >= end:
        return 0
    try:
        import yfinance as yf

        h = yf.Ticker(t).history(period="5d", auto_adjust=False)
    except Exception as e:  # noqa: BLE001
        print(f"[closes] {t} yfinance 拉取失败: {e}", flush=True)
        return 0
    if h is None or h.empty:
        return 0
    h = h.reset_index()
    if "Date" in h.columns:
        h["date"] = pd.to_datetime(h["Date"]).dt.strftime("%Y-%m-%d")
    h = h.rename(columns={
        "Open": "open", "High": "high", "Low": "low", "Close": "close",
        "Adj Close": "adj_close", "Volume": "volume",
    })
    need = {"date", "open", "high", "low", "close", "adj_close", "volume"}
    if not need.issubset(h.columns):
        print(f"[closes] {t} 列缺失: {list(h.columns)}", flush=True)
        return 0
    h = h[["date", "open", "high", "low", "close", "adj_close", "volume"]]
    h = h[(h["date"] > last) & (h["date"] <= end)]
    if h.empty:
        return 0
    merged = pd.concat([df, h], ignore_index=True).drop_duplicates(subset=["date"]).sort_values("date")
    merged.to_csv(path, index=False)
    print(f"[closes] {t}: 追加 {len(h)} 天 → {path}", flush=True)
    return len(h)


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:  # noqa: BLE001
        pass
    p = argparse.ArgumentParser(description="每日收盘价更新（workflow 后台）")
    p.add_argument("--tickers", nargs="*", help="默认全部报告标的")
    args = p.parse_args()
    tickers = [t.upper() for t in args.tickers] if args.tickers else _tickers()
    total = sum(update_ticker(t) for t in tickers)
    print(f"[closes] 完成：共追加 {total} 行", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
