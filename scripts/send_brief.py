#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""简报发送 CLI（多标的）：渲染 → 幂等检查 → 一次推送 → 一次写台账。

用法（仓库根目录执行）：
  python scripts/send_brief.py --session morning --date 2026-09-04 \
      --webhook-url "$DISCORD_BRIEF_WEBHOOK_URL"
  python scripts/send_brief.py --session morning --date 2026-09-04 --dry-run
  python scripts/send_brief.py --session morning --tickers QQQ,SPY --dry-run

标的名单：默认读取 config/brief_tickers.txt（每行一个，# 开头为注释）。
该文件是用户名单：程序只读，任何代码/脚本不得写入或覆盖。
幂等：与完整晨/晚报共用 data/history/_sent_log.json，键分离
（早报简报 / 晚报简报）；整批成功后统一记账，避免逐标的账本分裂。
"""

from __future__ import annotations

import argparse
import csv
import gzip
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

from report.brief import _parse_created, render_brief, render_digest_with_state  # noqa: E402

DISCORD_USER_AGENT = "Mozilla/5.0 (option-alert-brief/1.1)"
_LOG_KEY = {"morning": "早报简报", "evening": "晚报简报"}
_STATE_NAME = "brief_signal_state.json"


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


def _load_universe(data_root: Path, override: str | None) -> list:
    """标的名单：--tickers 覆盖 > config/brief_tickers.txt > 默认 QQQ。只读，绝不写该文件。"""
    if override:
        return [t.strip().upper() for t in override.split(",") if t.strip()]
    cfg = Path(data_root) / "config" / "brief_tickers.txt"
    out = []
    if cfg.exists():
        for line in cfg.read_text(encoding="utf-8").splitlines():
            line = line.split("#", 1)[0].strip()
            if line:
                out.append(line.upper())
    return out or ["QQQ"]


def _state_path(data_root: Path) -> Path:
    return Path(data_root) / "data" / "history" / _STATE_NAME


def _load_state(data_root: Path) -> dict:
    path = _state_path(data_root)
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _save_state(data_root: Path, state: dict) -> None:
    path = _state_path(data_root)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, ensure_ascii=False, indent=1), encoding="utf-8")


def _merge_state(state: dict, pending: list, resolved: list, day: str) -> None:
    """移除已结算条件，写入新待兑现条件（同日同档只保留最新）。"""
    sigs = state.setdefault("signals", {})
    for key in resolved:
        sigs.pop(key, None)
    for p in pending:
        p["created"] = day
        key = f"{p.get('ticker')}|{p.get('expiry')}|{p.get('kind')}"
        sigs[key] = p
    if len(sigs) > 12:  # 防御性上限：删最旧的
        for key in list(sigs)[: len(sigs) - 12]:
            sigs.pop(key, None)


def _load_chain_history(
    data_root: Path, ticker: str, day: str, interest: list, n_files: int = 5
) -> dict:
    """读取最近 n 个链快照（日期 <= day），按到期档汇总 CALL/PUT OI，
    并在最新快照上附带各档 top CALL/PUT 集中 strike（用于标注"集中位"具体价位）。

    口径：链文件日期 D 的 OI = 前一交易日终值（OCC 滞后），相邻文件差
    = 最近已入账交易日的净变化。只读，不写任何文件。
    """
    chain_dir = Path(data_root) / "data" / "chain_history" / ticker
    if not chain_dir.exists():
        return {}
    files = sorted(p.name for p in chain_dir.glob("*.csv.gz") if p.name[:10] <= day)
    files = files[-n_files:]
    hist: dict = {}
    tops: dict = {}
    newest = files[-1] if files else None
    for name in files:
        date = name[:10]
        per: dict = {}
        with gzip.open(chain_dir / name, "rt", encoding="utf-8", errors="replace") as f:
            for r in csv.DictReader(f):
                exp = str(r.get("expiration") or "").strip()
                if exp not in interest:
                    continue
                typ = (r.get("right") or "").strip().upper()
                try:
                    oi = float(r.get("openInterest") or 0)
                except (TypeError, ValueError):
                    continue
                per.setdefault(exp, {"C": 0.0, "P": 0.0})
                if typ == "CALL":
                    per[exp]["C"] += oi
                elif typ == "PUT":
                    per[exp]["P"] += oi
                if name == newest:
                    try:
                        strike = float(r.get("strike") or 0)
                    except (TypeError, ValueError):
                        strike = None
                    if strike is not None:
                        tops.setdefault(exp, {"CALL": [], "PUT": []})
                        if typ in ("CALL", "PUT"):
                            tops[exp][typ].append((strike, oi))
        for exp, v in per.items():
            hist.setdefault(exp, []).append({"date": date, "C": v["C"], "P": v["P"]})
    out: dict = {}
    for exp, seq in hist.items():
        # 保留更多档位，供渲染层按"距现价带内"筛选（深虚值 top OI 不能当近端结构位）
        tc = sorted(tops.get(exp, {}).get("CALL", []), key=lambda x: x[1], reverse=True)[:8]
        tp = sorted(tops.get(exp, {}).get("PUT", []), key=lambda x: x[1], reverse=True)[:8]
        out[exp] = {
            "seq": seq,
            "topC": [{"s": s, "oi": o} for s, o in tc],
            "topP": [{"s": s, "oi": o} for s, o in tp],
        }
    return out


def main() -> int:
    _utf8()
    ap = argparse.ArgumentParser(description="发送期权简报到 Discord（多标的）")
    ap.add_argument("--session", required=True, choices=["morning", "evening"])
    ap.add_argument("--tickers", default=None, help="逗号分隔；默认读 config/brief_tickers.txt")
    ap.add_argument("--date", default=None, help="YYYY-MM-DD；默认取最新快照日期")
    ap.add_argument("--webhook-url", default=None)
    ap.add_argument("--data-root", default=None, help="仓库/数据根目录（默认脚本上级目录）")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--verify", action="store_true", help="只验证 webhook 有效性")
    ap.add_argument("--allow-stale", action="store_true", help="允许使用非目标日期快照（手动测试）")
    args = ap.parse_args()

    data_root = Path(args.data_root) if args.data_root else ROOT

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

    tickers = _load_universe(data_root, args.tickers)
    loaded = []
    skipped = []
    stale = []
    for t in tickers:
        try:
            snap = snaps.load(day, t, args.session)
        except FileNotFoundError:
            skipped.append(t)
            continue
        snap_day, _ts = _parse_created(snap.get("created_at"))
        if snap_day != day:
            if not args.allow_stale:
                stale.append(t)
                continue
            print(f"[新鲜度] {t} 快照日期 {snap_day} != 目标 {day}（--allow-stale 已放行）")
        loaded.append((t, snap))

    if not loaded:
        print(f"无 {day} {args.session} 快照（名单 {len(tickers)} 个），本次跳过")
        return 0
    if skipped:
        print(f"跳过无快照标的：{', '.join(skipped)}")
    if stale:
        print(f"跳过日期不符标的：{', '.join(stale)}")

    full_tickers = [t for t, _ in loaded]
    chain_map = {}
    for t, snap in loaded:
        interest = [
            str(e.get("expiration"))
            for e in ((snap.get("forward") or {}).get("expirations") or [])
        ]
        chain_map[t] = _load_chain_history(data_root, t, day, interest)
    state = _load_state(data_root)
    pending_all: list = []
    resolved_all: list = []
    text, pending_all, resolved_all = render_digest_with_state(
        loaded,
        session=args.session,
        date_str=day,
        full_tickers=full_tickers,
        chain_data=chain_map,
        prior_state=state,
    )
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
    _merge_state(state, pending_all, resolved_all, day)
    _save_state(data_root, state)
    print(f"已发送 {_LOG_KEY[args.session]}（{day}，{len(loaded)} 个标的）到 Discord")
    return 0


if __name__ == "__main__":
    sys.exit(main())
