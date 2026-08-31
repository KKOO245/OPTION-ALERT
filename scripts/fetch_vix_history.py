#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""VIX 历史日线入库（yfinance ^VIX，免费无 key，GitHub Actions 后台自动维护）。

输出：data/vix_history/VIX.csv（date, close）
- 首次运行拉 1990-01-01 → 昨日；之后断点续传（只拉新日期）。
- 用途：市场波动率环境定档、episode/analog 的 VIX Regime 分层。
- 失败只警告不中断（VIX 是辅助数据，不影响报告生成）。

用法：python scripts/fetch_vix_history.py
"""

from __future__ import annotations

import datetime
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
OUT = REPO_ROOT / "data" / "vix_history" / "VIX.csv"
START = datetime.date(1990, 1, 1)


def _log(msg: str) -> None:
    print(f"[vix] {msg}", flush=True)


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:  # noqa: BLE001
        pass
    OUT.parent.mkdir(parents=True, exist_ok=True)

    # 断点续传：读取已有文件最后日期
    start = START
    existing: list[tuple[str, str]] = []
    if OUT.exists() and OUT.stat().st_size > 0:
        try:
            with open(OUT, encoding="utf-8") as f:
                f.readline()  # header
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) >= 2:
                        existing.append((parts[0], parts[1]))
            if existing:
                start = datetime.date.fromisoformat(existing[-1][0]) + datetime.timedelta(days=1)
        except Exception as e:  # noqa: BLE001
            _log(f"读取已有 VIX.csv 失败，全量重拉: {e}")
            existing = []
            start = START

    end = datetime.date.today() - datetime.timedelta(days=1)  # 只用已收盘日期，避免盘中/未来泄漏
    if start > end:
        _log(f"已是最新（截至 {existing[-1][0]}），无需更新")
        return 0

    try:
        import pandas as pd  # noqa: F401
        import yfinance as yf

        df = yf.download(
            "^VIX",
            start=start.isoformat(),
            end=(end + datetime.timedelta(days=1)).isoformat(),
            interval="1d",
            auto_adjust=False,
            progress=False,
        )
    except Exception as e:  # noqa: BLE001
        _log(f"yfinance 拉取失败（保持原数据）: {e}")
        return 0

    if df is None or df.empty:
        _log(f"{start}~{end} 无新数据")
        return 0

    # 兼容单层列 / MultiIndex（yfinance 不同版本返回结构不同）
    close_series = None
    if "Close" in df.columns:
        close_series = df["Close"]
    elif hasattr(df.columns, "get_level_values") and "Close" in df.columns.get_level_values(0):
        c = df["Close"]
        close_series = c.iloc[:, 0] if hasattr(c, "iloc") and c.ndim > 1 else c
    if close_series is None:
        _log("返回列中没有 Close，跳过本次更新")
        return 0

    new_rows: list[tuple[str, str]] = []
    start_iso = start.isoformat()
    for ts, v in close_series.items():
        d = str(ts.date() if hasattr(ts, "date") else str(ts))[:10]
        if d < start_iso:
            continue  # 只接受起始日之后的日期，防止窗口外旧数据混入
        if d > end.isoformat():
            continue  # 排除今天盘中/未收盘
        try:
            fv = float(v)
        except (TypeError, ValueError):
            continue
        if fv != fv or fv <= 0:
            continue
        new_rows.append((d, f"{fv:.2f}"))
    new_rows.sort()

    seen = {d for d, _ in existing}
    merged = list(existing)
    added = 0
    for d, v in new_rows:
        if d not in seen:
            merged.append((d, v))
            seen.add(d)
            added += 1
    merged.sort()

    with open(OUT, "w", encoding="utf-8", newline="") as f:
        f.write("date,close\n")
        for d, v in merged:
            f.write(f"{d},{v}\n")
    span = f"{merged[0][0]} ~ {merged[-1][0]}" if merged else "空"
    _log(f"新增 {added} 天 → {OUT}（累计 {len(merged)} 天，{span}）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
