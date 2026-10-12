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
import hashlib
import json
import os
import shutil
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from report.brief import _parse_created, render_brief, render_digest_with_state  # noqa: E402

DISCORD_USER_AGENT = "Mozilla/5.0 (option-alert-brief/1.1)"
_LOG_KEY = {"morning": "早报简报", "evening": "晚报简报"}
_STATE_NAME = "brief_signal_state.json"
_ARCHIVE_ENV = "OPTION_ALERT_CHAIN_ARCHIVE"
_ET = ZoneInfo("America/Toronto")


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
        key = (
            f"{p.get('ticker')}|{p.get('expiry')}|{p.get('kind')}"
            f"|v{p.get('rule_version', 1)}"
        )
        sigs[key] = p
    if len(sigs) > 12:  # 防御性上限：删最旧的
        for key in list(sigs)[: len(sigs) - 12]:
            sigs.pop(key, None)


def _load_chain_history(
    data_root: Path, ticker: str, day: str, interest: list, n_files: int = 5,
    spot: float | None = None,
) -> dict:
    """读取最近 n 个链快照（日期 <= day），按到期档汇总 CALL/PUT OI，
    并在最新快照上附带各档 top CALL/PUT 集中 strike（用于标注"集中位"具体价位）。

    口径：链文件日期 D 的 OI = 前一交易日终值（OCC 滞后），相邻文件差
    = 最近已入账交易日的净变化。只读，不写任何文件。
    """
    chain_dir = Path(data_root) / "data" / "chain_history" / ticker
    if not chain_dir.exists():
        return {}
    # 0DTE（当日到期）必须纳入读取范围：快照 forward 因 min_dte=1 排除了它
    interest = list(dict.fromkeys(list(interest) + [day]))
    files = sorted(p.name for p in chain_dir.glob("*.csv.gz") if p.name[:10] <= day)
    files = files[-n_files:]
    hist: dict = {}
    tops: dict = {}
    zero = {"C": 0.0, "P": 0.0, "rows": []}
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
                    if exp == day:
                        if typ == "CALL":
                            zero["C"] += oi
                        elif typ == "PUT":
                            zero["P"] += oi
                        try:
                            mid = float(r.get("mid") or 0)
                            iv = float(r.get("iv") or 0)
                            vol = float(r.get("volume") or 0)
                            delta = float(r.get("delta") or 0)
                            bid = float(r.get("bid") or 0)
                            ask = float(r.get("ask") or 0)
                        except (TypeError, ValueError):
                            mid, iv, vol, delta, bid, ask = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
                        if typ in ("CALL", "PUT") and strike is not None:
                            # 0DTE 抓全档（含深虚值尾部/零 OI 档）：用于尾部通道、成交量通道、双 MaxPain
                            zero["rows"].append({
                                "s": strike, "right": typ, "oi": oi, "mid": mid,
                                "iv": iv, "vol": vol, "delta": delta,
                                "bid": bid, "ask": ask,
                            })
        for exp, v in per.items():
            hist.setdefault(exp, []).append({"date": date, "C": v["C"], "P": v["P"]})
    out: dict = {}
    for exp, seq in hist.items():
        # 保留更多档位，供渲染层按"距现价带内"筛选（深虚值 top OI 不能当近端结构位）
        tc = sorted(tops.get(exp, {}).get("CALL", []), key=lambda x: x[1], reverse=True)[:30]
        tp = sorted(tops.get(exp, {}).get("PUT", []), key=lambda x: x[1], reverse=True)[:30]
        out[exp] = {
            "seq": seq,
            "topC": [{"s": s, "oi": o} for s, o in tc],
            "topP": [{"s": s, "oi": o} for s, o in tp],
        }
    if zero["rows"] or zero["C"] or zero["P"]:
        out["_0dte"] = zero
    return out


def _archive_root(data_root: Path, override: str | None = None) -> Path:
    """存档根目录：--archive-root > 环境变量 > 仓库同级目录。

    默认刻意放在**仓库之外**，避免存档被 git 提交、把仓库撑大；优先落到
    `<仓库>/../EXTERNAL DATA/OPTION-ALERT-CHAIN-ARCHIVE`（与 EOD 数据库、
    备份同处一份目录约定），该父目录不存在时退回 `<仓库>/../option-alert-chain-archive`。
    """
    if override:
        return Path(override)
    env = os.environ.get(_ARCHIVE_ENV)
    if env:
        return Path(env)
    ext = Path(data_root).resolve().parent / "EXTERNAL DATA" / "OPTION-ALERT-CHAIN-ARCHIVE"
    if ext.parent.exists():
        return ext
    return Path(data_root).resolve().parent / "option-alert-chain-archive"


def _verify_file(path: Path, kind: str) -> dict:
    """校验一份副本是否完整：'csv_gz' 需为能读完的 gzip CSV，'json' 需能解析。

    返回 {"ok", "rows", "sha256", ["error"]}；只读，不修改文件。
    """
    out: dict = {"ok": False, "rows": None, "sha256": ""}
    try:
        raw = Path(path).read_bytes()
        out["sha256"] = hashlib.sha256(raw).hexdigest()
        if kind == "json":
            json.loads(raw.decode("utf-8"))
            out["ok"] = True
        elif kind == "text":
            out["ok"] = len(raw) > 0
        else:
            rows = 0
            with gzip.open(Path(path), "rt", encoding="utf-8", errors="replace") as f:
                if "contractSymbol" not in f.readline():
                    out["error"] = "表头异常"
                    return out
                for _ in f:
                    rows += 1
            out["rows"] = rows
            out["ok"] = rows > 0
    except Exception as e:  # noqa: BLE001
        out["error"] = type(e).__name__
    return out


def _copy_verified(src: Path, dst: Path, kind: str) -> dict:
    """复制并校验；不一致时重试一次（应对并发写入造成的半截文件）。

    校验口径：副本能完整读出，且与源文件 sha256 一致。
    """
    dst.parent.mkdir(parents=True, exist_ok=True)
    last: dict = {"ok": False, "rows": None, "sha256": "", "attempts": 0}
    for attempt in (1, 2):
        last["attempts"] = attempt
        try:
            shutil.copy2(src, dst)
        except Exception as e:  # noqa: BLE001
            last = {"ok": False, "rows": None, "sha256": "",
                    "attempts": attempt, "error": type(e).__name__}
            time.sleep(0.5)
            continue
        s = _verify_file(src, kind)
        d = _verify_file(dst, kind)
        if d["ok"] and s["ok"] and d["sha256"] == s["sha256"]:
            return {**d, "attempts": attempt}
        last = {**d, "attempts": attempt, "error": d.get("error") or "与源文件不一致"}
        time.sleep(0.5)
    return last


def _write_verified(path: Path, payload, kind: str) -> dict:
    """写入并校验：已存在且校验通过的副本不动；校验失败的重写。"""
    p = Path(path)
    if p.exists():
        cur = _verify_file(p, kind)
        if cur["ok"]:
            return {**cur, "source": "reused"}
        tag = "repaired"
    else:
        tag = "written"
    p.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(payload, (bytes, bytearray)):
        p.write_bytes(payload)
    else:
        p.write_text(str(payload), encoding="utf-8")
    return {**_verify_file(p, kind), "source": tag}


def _snapshot_stamp(data_root: Path, tickers: list, day: str, session: str) -> tuple:
    """存档目录的时刻标签：优先用快照 `created_at`（= 数据抓取时刻），否则用 ET 本机时间。

    不用裸 `datetime.now()`：那在 GitHub Actions 上是 UTC、在本机是 ET，会造成两套命名。
    """
    found = []
    for t in [str(x).upper() for x in tickers]:
        p = Path(data_root) / "analytics" / "daily" / day / f"{t}_{session}.json"
        if not p.exists():
            continue
        try:
            created = _parse_created(
                json.loads(p.read_text(encoding="utf-8")).get("created_at")
            )[1]
            hhmm = created.split(" ")[-1].replace(":", "")
            if len(hhmm) == 4 and hhmm.isdigit():
                found.append(hhmm)
        except Exception:  # noqa: BLE001
            continue
    if found:
        counts: dict = {}
        for x in found:
            counts[x] = counts.get(x, 0) + 1
        best = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[0][0]
        return best, "snapshot.created_at"
    return datetime.now(_ET).strftime("%H%M"), "local_clock(ET)"


def _archive_run_artifacts(
    data_root: Path, tickers: list, day: str, session: str, root: Path,
    extras: dict | None = None,
) -> dict:
    """把本次运行"看到的那份"数据留一份副本（永不覆盖，除非已有副本校验失败）。

    目录布局（与点位提醒的存档对齐）：
      `<root>/<日期>/<HHMM>/chains/<标的>.csv.gz`      ← 链文件副本
      `<root>/<日期>/<HHMM>/<标的>_<session>.json`     ← 快照副本
      `<root>/<日期>/<HHMM>/brief_<session>.md`        ← 简报正文（推送原文）
      `<root>/<日期>/<HHMM>/state_before.json`         ← 本次读到的信号状态
      `<root>/<日期>/<HHMM>/state_after.json`          ← 本次写回后的信号状态
      `<root>/<日期>/<HHMM>/_manifest.json`            ← 逐文件 ok/rows/source/sha256

    动机（2026-10-11 实测）：链文件与快照都会被当晚那次运行覆盖
    （`src/storage.py` 注释原话："同一日期再次写入以最后一次为准"），
    事后回看/回测因此拿到收盘口径的数据——实测实盘点位只有 80% 可复现。

    副本完整性：每份副本写入/复制后逐份校验（csv.gz 需能完整读完且与源 sha256
    一致，JSON 需能解析），不一致时重试一次——针对 `src/storage.py` 用 `to_csv`
    原地写、并发时可能读到半截文件的风险。

    不做清理：本地磁盘 1TB，用户 2026-10-11 明确"文件 size 完全不是问题"。
    单次约 1.2 MB（20 标的），按每天 2 次估算约 0.6 GB/年。

    本函数只读源文件、只写存档目录；同一分钟内重复运行复用已有副本
    （仅当已有副本校验失败时才重写它）。
    """
    extras = extras or {}
    stamp, stamp_src = _snapshot_stamp(data_root, tickers, day, session)
    dest = Path(root) / day / stamp
    chain_dest = dest / "chains"
    chain_info: dict = {}
    snap_info: dict = {}
    for t in [str(x).upper() for x in tickers]:
        src = Path(data_root) / "data" / "chain_history" / t / f"{day}.csv.gz"
        if src.exists():
            dst = chain_dest / f"{t}.csv.gz"
            cur = _verify_file(dst, "csv_gz") if dst.exists() else None
            if cur and cur["ok"]:
                chain_info[t] = {**cur, "source": "reused"}
            else:
                tag = "repaired" if cur else "copied"
                chain_info[t] = {**_copy_verified(src, dst, "csv_gz"), "source": tag}
        src_snap = Path(data_root) / "analytics" / "daily" / day / f"{t}_{session}.json"
        if src_snap.exists():
            dst_snap = dest / src_snap.name
            cur_s = _verify_file(dst_snap, "json") if dst_snap.exists() else None
            if cur_s and cur_s["ok"]:
                snap_info[t] = {**cur_s, "source": "reused"}
            else:
                tag = "repaired" if cur_s else "copied"
                snap_info[t] = {**_copy_verified(src_snap, dst_snap, "json"), "source": tag}
    # 派生件：简报正文 + 信号状态前后快照（回看时无需再跑一遍渲染）
    derived: dict = {}
    if extras.get("brief_text"):
        derived["brief_text"] = _write_verified(
            dest / f"brief_{session}.md", extras["brief_text"], "text")
    if extras.get("state_before") is not None:
        derived["state_before"] = _write_verified(
            dest / "state_before.json",
            json.dumps(extras["state_before"], ensure_ascii=False, indent=2), "json")
    if extras.get("state_after") is not None:
        derived["state_after"] = _write_verified(
            dest / "state_after.json",
            json.dumps(extras["state_after"], ensure_ascii=False, indent=2), "json")
    n_chain = sum(1 for v in chain_info.values() if v.get("ok"))
    n_snap = sum(1 for v in snap_info.values() if v.get("ok"))
    bad = sorted([f"chains/{k}" for k, v in chain_info.items() if not v.get("ok")]
                 + [k for k, v in snap_info.items() if not v.get("ok")]
                 + [k for k, v in derived.items() if not v.get("ok")])
    manifest = dest / "_manifest.json"
    if chain_info or snap_info or derived:
        # manifest 是累计记录（同分钟多次运行会合并），数据文件本身不覆盖
        prev: dict = {}
        if manifest.exists():
            try:
                prev = json.loads(manifest.read_text(encoding="utf-8"))
            except Exception:  # noqa: BLE001
                prev = {}
        chains_all = {**(prev.get("chains") or {}), **chain_info}
        snaps_all = {**(prev.get("snapshots") or {}), **snap_info}
        derived_all = {**(prev.get("derived") or {}), **derived}
        unverified = sorted([f"chains/{k}" for k, v in chains_all.items() if not v.get("ok")]
                            + [k for k, v in snaps_all.items() if not v.get("ok")]
                            + [k for k, v in derived_all.items() if not v.get("ok")])
        manifest.write_text(json.dumps({
            "date": day,
            "stamp": prev.get("stamp") or stamp,
            "stamp_source": prev.get("stamp_source") or stamp_src,
            "session": session,
            "runs": int(prev.get("runs") or 0) + 1,
            "chains": chains_all,
            "snapshots": snaps_all,
            "derived": derived_all,
            "unverified": unverified,
            "note": "运行时刻的链/快照/正文/状态副本（逐文件记录行数与 sha256）；"
                    "副本永不覆盖（仅校验失败的会被重写），manifest 为累计记录。"
                    "回看请读本目录，不要读仓库现值。",
        }, ensure_ascii=False, indent=2), encoding="utf-8")
    return {"dir": str(dest), "chain": n_chain, "snapshots": n_snap,
            "derived": sum(1 for v in derived.values() if v.get("ok")),
            "unverified": bad, "stamp": stamp, "stamp_source": stamp_src}


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
    ap.add_argument("--archive-root", default=None,
                    help="链/快照存档根目录（默认：仓库同级的 option-alert-chain-archive）")
    ap.add_argument("--no-archive", action="store_true", help="本次不存档（手动测试用）")
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
        chain_map[t] = _load_chain_history(
            data_root, t, day, interest, spot=(snap.get("spot") or None)
        )
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
    state_before = json.loads(json.dumps(state, ensure_ascii=False))  # 存档用：合并前的状态
    _discord_send(args.webhook_url, text)
    _mark_sent(data_root, args.session, day)
    _merge_state(state, pending_all, resolved_all, day)
    _save_state(data_root, state)
    if not args.no_archive:
        # 存档"本次推送的那一份"（正文+链+快照+状态前后；逐份校验）；失败不阻塞
        try:
            info = _archive_run_artifacts(
                data_root, full_tickers, day, args.session,
                _archive_root(data_root, args.archive_root),
                extras={"brief_text": text, "state_before": state_before, "state_after": state},
            )
            print(f"[存档] {info['dir']}｜链 {info['chain']}，快照 {info['snapshots']}，"
                  f"派生件 {info['derived']}｜时刻标签 {info['stamp']}（{info['stamp_source']}）")
            if info.get("unverified"):
                print(f"[警告] {len(info['unverified'])} 份副本未通过完整性校验："
                      f"{', '.join(info['unverified'][:5])}")
        except Exception as e:  # noqa: BLE001
            print(f"[警告] 存档失败（不影响本次发送）：{type(e).__name__}: {e}")
    # 审计日志：记录每次结算/新挂起，便于后续统计命中率（供 git 一起提交）
    if resolved_all or pending_all:
        log_path = data_root / "data" / "history" / "brief_signal_log.jsonl"
        log_path.parent.mkdir(parents=True, exist_ok=True)
        with log_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps({
                "date": day, "session": args.session,
                "resolved": resolved_all,
                "pending": [
                    f"{p.get('ticker')}|{p.get('expiry')}|{p.get('kind')}"
                    f"|v{p.get('rule_version', 1)}" for p in pending_all
                ],
            }, ensure_ascii=False) + "\n")
    print(f"已发送 {_LOG_KEY[args.session]}（{day}，{len(loaded)} 个标的）到 Discord")
    return 0


if __name__ == "__main__":
    sys.exit(main())
