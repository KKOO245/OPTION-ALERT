#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""data/closes 健康检查（workflow 断言步骤用，也可手动跑）。

要解决的问题：update_closes_daily 曾经静默地把空收盘价写进 data/closes，
而现有看门狗只检查"报告是否发出"，所以数据侧坏了 4 周无人知晓。

检查三项（对 config/tickers.txt 的每个标的）：
  1) 文件存在；
  2) 末尾 --tail 行（默认 10）里 close 为空的数量为 0；
  3) 最新日期距今不超过 --max-age-days（默认 6，容忍长周末/节假日导致的停更）。

异常时：打印明细 + GitHub 注解 ::warning:: + 退出码 1；
若环境变量 DISCORD_WEBHOOK_URL 存在，额外发一条 Discord 告警（发失败不影响退出码）。

用法：
  python scripts/check_closes_health.py
  python scripts/check_closes_health.py --closes-dir data/closes --tickers NVDA QQQ --tail 5
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import sys
import urllib.request
from pathlib import Path

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CLOSES_DIR = REPO_ROOT / "data" / "closes"
TICKERS_FILE = REPO_ROOT / "config" / "tickers.txt"
ET_TZ = "America/New_York"


def _tickers(explicit: list[str] | None = None) -> list[str]:
    if explicit:
        return [t.upper() for t in explicit]
    out: list[str] = []
    for line in TICKERS_FILE.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if s and not s.startswith("#"):
            out.append(s.upper())
    return out


def check(closes_dir: Path, tickers: list[str], tail: int, max_age_days: int):
    """返回 (ok 列表, bad 列表)；bad 元素为 (ticker, 原因)。"""
    today = pd.Timestamp.now(tz=ET_TZ).date()
    ok: list[tuple[str, str, int]] = []
    bad: list[tuple[str, str]] = []
    for t in tickers:
        path = closes_dir / f"{t}.csv"
        if not path.exists():
            bad.append((t, "文件不存在"))
            continue
        try:
            df = pd.read_csv(path, dtype={"date": str})
        except Exception as e:  # noqa: BLE001
            bad.append((t, f"读取失败: {e}"))
            continue
        if not {"date", "close"}.issubset(df.columns):
            bad.append((t, f"缺列（现有列: {list(df.columns)}）"))
            continue
        if df.empty:
            bad.append((t, "文件为空"))
            continue
        n_null = int(df.tail(tail)["close"].isna().sum())
        last = str(df["date"].max())[:10]
        try:
            age = (today - datetime.date.fromisoformat(last)).days
        except ValueError:
            bad.append((t, f"日期无法解析: {last}"))
            continue
        if n_null:
            bad.append((t, f"末尾 {tail} 行有 {n_null} 个空 close（最新 {last}）"))
        elif age > max_age_days:
            bad.append((t, f"最新数据 {last}，距今 {age} 天 > {max_age_days} 天"))
        else:
            ok.append((t, last, age))
    return ok, bad


def _alert(body: str) -> None:
    url = os.environ.get("DISCORD_WEBHOOK_URL")
    if not url:
        print("[closes-check] 未配置 DISCORD_WEBHOOK_URL，跳过告警", flush=True)
        return
    stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    msg = (
        f"⚠️ data/closes 健康检查未通过（{stamp}）\n{body}\n"
        "→ 检查「每日期权报告 / 每日简报」里的 update_closes_daily 步骤日志。"
    )
    try:
        data = json.dumps({"content": msg}).encode("utf-8")
        req = urllib.request.Request(
            url, data=data, headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            print(f"[closes-check] 告警已发送: HTTP {resp.status}", flush=True)
    except Exception as e:  # noqa: BLE001
        print(f"[closes-check] 告警发送失败（不影响退出码）: {e}", flush=True)


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:  # noqa: BLE001
        pass
    p = argparse.ArgumentParser(description="data/closes 健康检查")
    p.add_argument("--closes-dir", default=str(DEFAULT_CLOSES_DIR),
                   help="默认 data/closes（可用来自测失败路径）")
    p.add_argument("--tickers", nargs="*", help="默认取 config/tickers.txt")
    p.add_argument("--tail", type=int, default=10, help="检查末尾多少行（默认 10）")
    p.add_argument("--max-age-days", type=int, default=6,
                   help="最新数据允许的最大天数（默认 6）")
    args = p.parse_args()

    tickers = _tickers(args.tickers)
    ok, bad = check(Path(args.closes_dir), tickers, args.tail, args.max_age_days)
    for t, last, age in ok:
        print(f"[closes-check] OK  {t:6} 最新 {last}（{age} 天前）")
    if not bad:
        print(f"[closes-check] 通过：{len(ok)} 个标的，末尾 {args.tail} 行无空 close，"
              f"最新数据均不超过 {args.max_age_days} 天")
        return 0

    body = "\n".join(f"  - {t}: {why}" for t, why in bad)
    print(f"[closes-check] 未通过：{len(bad)} / {len(ok) + len(bad)} 个标的异常")
    print(body, flush=True)
    print("::warning::data/closes 健康检查未通过（详见上方明细）", flush=True)
    _alert(body)
    return 1


if __name__ == "__main__":
    sys.exit(main())
