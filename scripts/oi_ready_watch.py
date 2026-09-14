#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""OI 就绪通知：OCC 终值发布后，每天推一条 Discord。

主检测：本机（--runner local）；备胎：GitHub Actions（--runner actions）。
去重：data/history/oi_ready_<date>.json（sent=true 即跳过）。
窗口：多伦多时间 19:00–23:00（--force 可跳过检查，用于测试）。
检测：比较当日链与前一交易日链的哨兵合约 OI（当日成交量>=1000 且 OI 变化）。
"""

from __future__ import annotations

import argparse
import csv
import gzip
import json
import os
import sys
import urllib.request
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))


def load_chain_file(path: Path) -> dict:
    out = {}
    with gzip.open(path, "rt", encoding="utf-8", errors="replace") as f:
        for r in csv.DictReader(f):
            try:
                key = (str(r.get("expiration")), (r.get("right") or "").upper(), float(r.get("strike")))
                out[key] = (float(r.get("openInterest") or 0), float(r.get("volume") or 0))
            except (TypeError, ValueError):
                continue
    return out


def gov_rows(contracts) -> dict:
    out = {}
    for c in contracts or []:
        try:
            key = (str(c.get("expiration")), str(c.get("type") or "").upper(), float(c.get("strike")))
            out[key] = (float(c.get("open_interest") or 0), float(c.get("volume") or 0))
        except (TypeError, ValueError):
            continue
    return out


def sentinel_changed(prev: dict, cur: dict, min_vol: float = 1000.0) -> list:
    hits = []
    for k, (poi, _pv) in prev.items():
        if k not in cur or poi <= 0:
            continue
        oi, vol = cur[k]
        if vol >= min_vol and abs(oi - poi) > 1e-9:
            hits.append((k, poi, oi, vol))
    return hits


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--runner", default="local", choices=["local", "actions"])
    ap.add_argument("--data-root", default=str(ROOT))
    ap.add_argument("--tickers", default="QQQ,SPY")
    ap.add_argument("--webhook-url", default=os.environ.get("DISCORD_BRIEF_WEBHOOK_URL", ""))
    ap.add_argument("--window-start", default="19:00")
    ap.add_argument("--window-end", default="23:00")
    ap.add_argument("--date", default=None)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--no-fetch", action="store_true", help="不抓取，直接用仓库里的当日链文件（测试用）")
    args = ap.parse_args()

    now = datetime.now(ZoneInfo("America/Toronto"))
    day = args.date or now.date().isoformat()
    if not args.force:
        hm = now.strftime("%H:%M")
        if not (args.window_start <= hm <= args.window_end):
            print(f"[窗口外] {hm} 不在 {args.window_start}-{args.window_end}，退出")
            return 0

    root = Path(args.data_root)
    state_path = root / "data" / "history" / f"oi_ready_{day}.json"
    if state_path.exists():
        try:
            if json.loads(state_path.read_text(encoding="utf-8")).get("sent"):
                print(f"[已通知] {day} 已发送，跳过")
                return 0
        except Exception:
            pass

    hits_all = {}
    for t in [x.strip().upper() for x in args.tickers.split(",") if x.strip()]:
        chain_dir = root / "data" / "chain_history" / t
        if not chain_dir.exists():
            print(f"[跳过] {t} 无链目录")
            continue
        prevs = sorted(p.name for p in chain_dir.glob("*.csv.gz") if p.name[:10] < day)
        if not prevs:
            print(f"[跳过] {t} 无前一交易日链文件")
            continue
        prev = load_chain_file(chain_dir / prevs[-1])
        if args.no_fetch:
            cur_path = chain_dir / f"{day}.csv.gz"
            if not cur_path.exists():
                print(f"[跳过] {t} 无当日链文件 {cur_path.name}")
                continue
            cur = load_chain_file(cur_path)
        else:
            import data_fetcher as fetcher  # type: ignore

            contracts, _spot, _src = fetcher.fetch_chain(t, max_days=40)
            cur = gov_rows(contracts)
        hits = sentinel_changed(prev, cur)
        print(f"[检测] {t}: 变化 {len(hits)} 条")
        if hits:
            hits_all[t] = hits[:3]

    if not hits_all:
        print(f"[未发布] {day} 未检测到 OI 终值更新")
        return 0

    msg = f"✅ OCC OI 终值已发布：{day}（检测 {now.strftime('%H:%M')} ET，执行方：{args.runner}）"
    detail = "；".join(
        f"{t}: " + ", ".join(
            f"{k[0]} {k[1]} {k[2]:.0f}（OI {p:.0f}→{o:.0f}）" for k, p, o, _v in hs
        )
        for t, hs in hits_all.items()
    )
    if args.dry_run:
        print("[DRY-RUN]", msg)
        print(detail[:1500])
        return 0
    if not args.webhook_url:
        print("[错误] 缺少 DISCORD_BRIEF_WEBHOOK_URL")
        return 2
    payload = json.dumps({"content": msg + "\n" + detail[:1500]}).encode("utf-8")
    req = urllib.request.Request(
        args.webhook_url, data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        print("Discord HTTP", resp.status)
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(
        json.dumps({
            "date": day, "sent": True, "detected_at": now.isoformat(),
            "runner": args.runner, "hits": {t: len(h) for t, h in hits_all.items()},
        }, ensure_ascii=False, indent=1),
        encoding="utf-8",
    )
    print("[已发送]", msg)
    return 0


if __name__ == "__main__":
    sys.exit(main())
