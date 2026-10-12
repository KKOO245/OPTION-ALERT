#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""每日收盘价更新（workflow 后台自动维护）：把 yfinance 已收盘日线并入 data/closes。

口径与回填一致：yf.Ticker.history(auto_adjust=False) —— Close 已拆股调整、未含股息
（与 data/closes 现有 close 列同一口径），adj_close 全调整。

两个职责（同一份文件）：
  1) 追加：只写严格早于"多伦多今天"的交易日（防拿到当日尚未定稿的 bar）；
  2) 修复：历史遗留的 close/adj_close 空值（缺口驱动，最多回溯 MAX_REPAIR_DAYS），
     同一日期用新值覆盖旧空行 —— 否则一个空行会永久挡住该日期的回填。

质量闸门：只接受 close 非空、>0、且落在该行 [low, high] 内的行；不合格一律跳过
（宁缺不写半行）。失败只警告不中断（closes 是辅助数据）。

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
ET_TZ = "America/New_York"
MAX_REPAIR_DAYS = 120  # 空值回溯上限（日历日），避免一次拉过长历史
PRICE_TOL = 0.02       # 质量闸门容差（元）


def _tickers() -> list[str]:
    out = []
    for line in (REPO_ROOT / "config" / "tickers.txt").read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if s and not s.startswith("#"):
            out.append(s.upper())
    return out


def _et_today() -> datetime.date:
    """多伦多"今天"。runner 是 UTC：直接用 date.today() 时，晚间运行"今天"已跳到次日，
    会把当日刚收盘、尚未定稿的 bar 当成"昨天的数据"写进来。"""
    return pd.Timestamp.now(tz=ET_TZ).date()


def _fetch_history(t: str, start: str):
    """按起点抓日线（auto_adjust=False）并归一化列名；失败/列不全返回 None。"""
    import yfinance as yf

    h = yf.Ticker(t).history(start=start, auto_adjust=False)
    if h is None or h.empty:
        return None
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
        return None
    return h[["date", "open", "high", "low", "close", "adj_close", "volume"]]


def update_ticker(t: str) -> tuple[int, int]:
    """更新单标的。返回 (新增行数, 修复空值行数)。"""
    path = CLOSES_DIR / f"{t}.csv"
    if not path.exists():
        return 0, 0
    try:
        df = pd.read_csv(path)
    except Exception as e:  # noqa: BLE001
        print(f"[closes] {t} 读取失败: {e}", flush=True)
        return 0, 0
    if "date" not in df.columns or "close" not in df.columns:
        return 0, 0
    df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")
    last = df["date"].max()
    end = (_et_today() - datetime.timedelta(days=1)).isoformat()
    # 待补日期：① 历史行 close/adj_close 为空 ② 比 last 更新的日期
    cutoff = (datetime.date.fromisoformat(end) - datetime.timedelta(days=MAX_REPAIR_DAYS)).isoformat()
    blank = df["close"].isna() | df["adj_close"].isna()
    holes = sorted(d for d in df.loc[blank, "date"] if d >= cutoff)
    if not holes and last >= end:
        return 0, 0  # 无缺口也无新日期：不发请求、不写文件
    try:
        h = _fetch_history(t, start=holes[0] if holes else last)
    except Exception as e:  # noqa: BLE001
        print(f"[closes] {t} yfinance 拉取失败: {e}", flush=True)
        return 0, 0
    if h is None:
        return 0, 0
    h = h[h["date"] <= end]
    h = h[h["close"].notna() & (h["close"] > 0)]
    h = h[(h["close"] >= h["low"] - PRICE_TOL) & (h["close"] <= h["high"] + PRICE_TOL)]
    if h.empty:
        return 0, 0
    h["adj_close"] = h["adj_close"].fillna(h["close"])
    hole_set = set(holes)
    patch_src = h[h["date"].isin(hole_set)]
    new_src = h[h["date"] > last]
    if patch_src.empty and new_src.empty:
        return 0, 0
    # 修复：只填该行空着的 close/adj_close，档案原有 OHLCV 一律不动
    base = df.copy()
    if not patch_src.empty:
        fill_map = {r["date"]: (r["close"], r["adj_close"]) for _, r in patch_src.iterrows()}
        for i, d in zip(base.index, base["date"]):
            if d in fill_map:
                c, a = fill_map[d]
                base.at[i, "close"] = c
                base.at[i, "adj_close"] = a
    merged = pd.concat([base, new_src], ignore_index=True)
    merged = merged.sort_values("date").drop_duplicates(subset=["date"], keep="last")
    if merged["date"].nunique() < df["date"].nunique():  # 安全闸门：绝不丢日期
        print(f"[closes] {t} 合并后日期数减少，放弃写入（需人工检查）", flush=True)
        return 0, 0
    merged.to_csv(path, index=False)
    added = len(new_src)
    repaired = len(patch_src)
    print(f"[closes] {t}: 新增 {added} 天 / 修复空值 {repaired} 天 → {path}", flush=True)
    return added, repaired


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:  # noqa: BLE001
        pass
    p = argparse.ArgumentParser(description="每日收盘价更新（workflow 后台）")
    p.add_argument("--tickers", nargs="*", help="默认全部报告标的")
    args = p.parse_args()
    tickers = [t.upper() for t in args.tickers] if args.tickers else _tickers()
    stats = [update_ticker(t) for t in tickers]
    added = sum(a for a, _ in stats)
    repaired = sum(b for _, b in stats)
    print(f"[closes] 完成：新增 {added} 行 / 修复空值 {repaired} 行 / 标的 {len(tickers)} 个", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
