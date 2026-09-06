#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""简报发送 CLI：渲染 → 幂等检查 → Discord 推送 → 写发送台账。

用法（仓库根目录执行）：
  python scripts/send_brief.py --session morning --date 2026-09-04 \
      --webhook-url "$DISCORD_BRIEF_WEBHOOK_URL"
  python scripts/send_brief.py --session evening --date 2026-09-04 --dry-run

幂等：与完整晨/晚报共用 data/history/_sent_log.json，但键分离
（早报简报 / 晚报简报），互不锁死。
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from report.brief import _parse_created, render_brief  # noqa: E402

DISCORD_USER_AGENT = "Mozilla/5.0 (option-alert-brief/1.0)"
_LOG_KEY = {"morning": "早报简报", "evening": "晚报简报"}


def _utf8() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass


def _sent_log_path(data_root: Path) -> Path:
    return Path(data_root) / "data" / "history" / "_sent_log.json"


def _already_sent(data_root: Path, session: str, day: str) -> bool:
    path = _sent_log_path(data_root)
    if not path.exists():
        return False
    try:
        log = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return False
    return log.get("date") == day and _LOG_KEY[session] in log.get("sessions", [])


def _mark_sent(data_root: Path, session: str, day: str) -> None:
    path = _sent_log_path(data_root)
    path.parent.mkdir(parents=True, exist_ok=True)
    log = {"date": day, "sessions": []}
    if path.exists():
        try:
            existing = json.loads(path.read_text(encoding="utf-8"))
            if existing.get("date") == day:
                log = existing
        except Exception:
            pass
    key = _LOG_KEY[session]
    if key not in log["sessions"]:
        log["sessions"].append(key)
    path.write_text(json.dumps(log, ensure_ascii=False), encoding="utf-8")


def _chunk_text(text: str, limit: int = 1900) -> list:
    if len(text) <= limit:
        return [text]
    chunks = []
    cur = ""
    for line in text.splitlines(keepends=True):
        if len(cur) + len(line) > limit and cur:
            chunks.append(cur)
            cur = ""
        cur += line
    if cur:
        chunks.append(cur)
    return chunks


def _post(webhook: str, payload: dict) -> None:
    last_err: Exception | None = None
    for attempt in range(3):
        try:
            req = urllib.request.Request(
                webhook,
                data=json.dumps(payload).encode("utf-8"),
                headers={"Content-Type": "application/json", "User-Agent": DISCORD_USER_AGENT},
                method="POST",
            )
            with urllib.request.urlopen(req, timeout=30) as resp:
                if resp.status not in (200, 204):
                    raise RuntimeError(f"HTTP {resp.status}")
                return
        except urllib.error.HTTPError as e:
            last_err = e
            if e.code == 429:
                wait = float(e.headers.get("Retry-After", "5") or 5)
                time.sleep(min(wait, 30))
                continue
            if e.code >= 500:
                time.sleep(5 * (attempt + 1))
                continue
            raise
        except Exception as e:  # noqa: BLE001
            last_err = e
            time.sleep(3 * (attempt + 1))
    raise RuntimeError(f"webhook 推送失败（重试 3 次后）：{last_err}")


def _discord_send(webhook: str, text: str) -> None:
    if not text.strip():
        raise RuntimeError("消息内容为空，拒绝发送")
    chunks = _chunk_text(text)
    for i, chunk in enumerate(chunks):
        _post(webhook, {"content": chunk})
        if i < len(chunks) - 1:
            time.sleep(2.1)


def _verify(webhook: str) -> int:
    if not webhook:
        print("webhook URL 为空（secret 未设置？）")
        return 1
    try:
        req = urllib.request.Request(webhook, headers={"User-Agent": DISCORD_USER_AGENT})
        with urllib.request.urlopen(req, timeout=30) as resp:
            info = json.loads(resp.read().decode("utf-8"))
        print(
            f"webhook 有效: id={info.get('id')} name={info.get('name')!r} "
            f"channel_id={info.get('channel_id')}"
        )
        return 0
    except Exception as e:  # noqa: BLE001
        print(f"webhook 验证失败: {type(e).__name__}: {e}")
        return 1


def main() -> int:
    _utf8()
    ap = argparse.ArgumentParser(description="发送 QQQ 简报到 Discord")
    ap.add_argument("--session", required=True, choices=["morning", "evening"])
    ap.add_argument("--ticker", default="QQQ")
    ap.add_argument("--date", default=None, help="YYYY-MM-DD；默认取最新快照日期")
    ap.add_argument("--webhook-url", default=None)
    ap.add_argument("--data-root", default=None, help="仓库/数据根目录（默认脚本上级目录）")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--verify", action="store_true", help="只验证 webhook 有效性")
    ap.add_argument("--allow-stale", action="store_true", help="允许使用非目标日期快照（手动测试）")
    args = ap.parse_args()

    data_root = Path(args.data_root) if args.data_root else ROOT
    ticker = args.ticker.upper()

    if args.verify:
        return _verify(args.webhook_url or "")

    try:
        from engine.snapshot import SnapshotStore
    except Exception as e:  # noqa: BLE001
        print(f"SnapshotStore 导入失败：{e}")
        return 1
    snaps = SnapshotStore(data_root)

    if args.date:
        day = args.date
    else:
        latest = snaps.load_latest()
        if not latest:
            print("无任何快照")
            return 1
        day = _parse_created(latest.get("created_at"))[0]

    try:
        snap = snaps.load(day, ticker, args.session)
    except FileNotFoundError:
        print(f"无 {day} {args.session} 快照（{ticker}），跳过（正常情况，例如周末/标的未抓取）")
        return 0

    snap_day, _ts = _parse_created(snap.get("created_at"))
    if snap_day != day and not args.allow_stale:
        print(
            f"[新鲜度] 快照日期 {snap_day} != 目标 {day}；"
            "为避免把旧日期简报混入本次推送，跳过（可用 --allow-stale 手动测试）"
        )
        return 0

    text = render_brief(snap, session=args.session, ticker=ticker)
    if args.dry_run:
        print(text)
        return 0
    if not args.webhook_url:
        print("未提供 --webhook-url（本次只打印不发送）")
        print(text)
        return 1
    if _already_sent(data_root, args.session, day):
        print(f"[幂等] {day} {_LOG_KEY[args.session]} 已发送过（_sent_log），跳过本次发送")
        return 0
    _discord_send(args.webhook_url, text)
    _mark_sent(data_root, args.session, day)
    print(f"已发送 {ticker} {_LOG_KEY[args.session]}（{day}）到 Discord")
    return 0


if __name__ == "__main__":
    sys.exit(main())
