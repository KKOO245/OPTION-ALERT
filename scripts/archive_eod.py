#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""OPTION-ALERT 定期归档脚本（两周一次，周六 10:30 由 Windows 计划任务触发）

职责（全部自动）：
  1) 拉取上次归档以来的 ThetaData EOD 全链 → 写入 SQLite 研究档案
     + 保存原始分块（供 IV 转换读取，同一存储）
  2) 刷新 yfinance 全历史价格 + 重算 data/iv_history（复用 backfill_history）
  3) git 提交推送（先 pull --rebase 防冲突）
  4) 备份：SQLite 拷贝到备份目录 + 摘要文件（保留最近 8 份）
  5) 弹窗汇报结果（计划任务跑完可见）

用法：
  python scripts/archive_eod.py              # 正常归档
  python scripts/archive_eod.py --backup-only # 只做备份（数据无新增时）

路径（可用环境变量覆盖）：
  OPTION_ALERT_DB_DIR    默认 D:\\git\\EXTERNAL DATA\\OPTION-ALERT-DB
  OPTION_ALERT_BACKUP_DIR 默认 D:\\git\\EXTERNAL DATA\\OPTION-ALERT-BACKUP
  THETADATA_RAW_DIR       默认 D:\\git\\EXTERNAL DATA\\OPTION-ALERT-RAW（回填脚本同款逻辑）
"""

from __future__ import annotations

import argparse
import datetime
import os
import shutil
import sqlite3
import subprocess
import sys
import time
from pathlib import Path

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from backfill_history import (  # noqa: E402
    RAW_DIR,
    _make_client,
    _to_trading_date,
    RateLimiter,
)

DB_DIR = Path(os.environ.get("OPTION_ALERT_DB_DIR") or r"D:\git\EXTERNAL DATA\OPTION-ALERT-DB")
DB_PATH = DB_DIR / "options_eod.db"
BACKUP_DIR = Path(
    os.environ.get("OPTION_ALERT_BACKUP_DIR") or r"D:\git\EXTERNAL DATA\OPTION-ALERT-BACKUP"
)
TICKERS_FILE = REPO_ROOT / "config" / "tickers.txt"
PYTHON = sys.executable
KEEP_BACKUPS = 8


def _log(msg: str) -> None:
    print(f"[archive] {msg}", flush=True)


def _tickers() -> list[str]:
    out = []
    for line in TICKERS_FILE.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if s and not s.startswith("#"):
            out.append(s.upper())
    return out


def _connect() -> sqlite3.Connection:
    DB_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS option_eod (
          date TEXT, root TEXT, expiration TEXT, strike REAL, right TEXT,
          close REAL, bid REAL, ask REAL, volume INTEGER, count INTEGER,
          open REAL, high REAL, low REAL,
          PRIMARY KEY (date, root, expiration, strike, right)
        );
        CREATE TABLE IF NOT EXISTS stock_eod (
          date TEXT, root TEXT, close REAL, open REAL, high REAL, low REAL,
          volume INTEGER, PRIMARY KEY (date, root)
        );
        CREATE TABLE IF NOT EXISTS option_oi (
          date TEXT, root TEXT, expiration TEXT, strike REAL, right TEXT,
          open_interest REAL,
          PRIMARY KEY (date, root, expiration, strike, right)
        );
        CREATE TABLE IF NOT EXISTS meta (key TEXT PRIMARY KEY, value TEXT);
        """
    )
    return conn


def _last_archive_date(conn: sqlite3.Connection) -> datetime.date:
    row = conn.execute("SELECT value FROM meta WHERE key='last_archive_date'").fetchone()
    if row:
        try:
            return datetime.date.fromisoformat(row[0])
        except ValueError:
            pass
    return datetime.date(2023, 6, 1)


def _save_raw_chunk(df: pd.DataFrame, t: str, start: datetime.date, end: datetime.date) -> None:
    """保存原始分块，供 backfill convert 读取（与历史分块同一命名规则）。"""
    tdir = RAW_DIR / t
    tdir.mkdir(parents=True, exist_ok=True)
    stem = f"{start:%Y%m%d}_{end:%Y%m%d}"
    try:
        import pyarrow  # noqa: F401

        df.to_parquet(tdir / f"{stem}.parquet", index=False)
    except ImportError:
        df.to_csv(tdir / f"{stem}.csv.gz", index=False, compression="gzip")


def _process_ticker(client, limiter: RateLimiter, t: str,
                    start: datetime.date, end: datetime.date,
                    conn: sqlite3.Connection) -> tuple[int, int]:
    """处理单个标的：期权+股票 EOD → 原始分块 + SQLite。异常向上抛，由调用方隔离。"""
    opt_n = stk_n = 0
    tdir = RAW_DIR / t
    tdir.mkdir(parents=True, exist_ok=True)
    # ---- 期权 EOD（全链）----
    limiter.wait()
    df = client.option_history_eod(
        symbol=t, start_date=start, end_date=end, expiration="*"
    )
    if df is None or df.empty:
        _log(f"{t} {start}~{end} 无期权数据")
    else:
        _save_raw_chunk(df, t, start, end)
        d = df.copy()
        d = d[d["strike"].notna() & (d["strike"] > 0)]
        if not d.empty:
            if "created" in d.columns:
                d["date"] = _to_trading_date(d["created"]).dt.strftime("%Y-%m-%d")
            elif "date" in d.columns:
                d["date"] = pd.to_datetime(d["date"]).dt.strftime("%Y-%m-%d")
            d["expiration"] = pd.to_datetime(d["expiration"]).dt.strftime("%Y-%m-%d")
            d["root"] = d.get("root", d.get("symbol", t))
            d["right"] = d["right"].astype(str).str.upper().str[0]
            rows = [
                (
                    r.date, r.root, r.expiration, float(r.strike), r.right,
                    _f(r.close), _f(r.bid), _f(r.ask), _i(r.volume),
                    _i(getattr(r, "count", None)),
                    _f(r.open), _f(r.high), _f(r.low),
                )
                for r in d.itertuples(index=False)
                if r.right in ("C", "P")
            ]
            conn.executemany(
                "INSERT OR IGNORE INTO option_eod VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
                rows,
            )
            opt_n += len(rows)
            _log(f"{t} 期权 {len(rows)} 行（增量写入）")
    # ---- 股票 EOD（现货）----
    limiter.wait()
    se = client.stock_history_eod(symbol=t, start_date=start, end_date=end)
    if se is not None and not se.empty:
        sd = se.copy()
        sd["date"] = _to_trading_date(
            sd["created"] if "created" in sd.columns else sd["date"]
        ).dt.strftime("%Y-%m-%d")
        srows = [
            (r.date, t, _f(r.close), _f(r.open), _f(r.high), _f(r.low), _i(r.volume))
            for r in sd.itertuples(index=False)
        ]
        conn.executemany(
            "INSERT OR IGNORE INTO stock_eod VALUES (?,?,?,?,?,?,?)", srows
        )
        stk_n += len(srows)
        _merge_stock_eod_file(t, sd)
    return opt_n, stk_n


def _fetch_and_store(client, limiter: RateLimiter, tickers: list[str],
                     start: datetime.date, end: datetime.date) -> tuple[int, int, int, list[str]]:
    """返回 (期权行数, 股票行数, OI 行数, 失败列表)。单个标的异常不影响其他标的。"""
    conn = _connect()
    opt_n, stk_n, oi_n = 0, 0, 0
    fails: list[str] = []
    for t in tickers:
        try:
            n1, n2 = _process_ticker(client, limiter, t, start, end, conn)
            opt_n += n1
            stk_n += n2
            oi_n += _fetch_oi(client, limiter, t, start, end, conn)
        except Exception as e:  # noqa: BLE001
            _log(f"{t} 处理异常，跳过（下次归档可补）: {e}")
            fails.append(f"{t}-异常")
    conn.commit()
    conn.close()
    return opt_n, stk_n, oi_n, fails


def _fetch_oi(client, limiter: RateLimiter, t: str,
              start: datetime.date, end: datetime.date, conn: sqlite3.Connection) -> int:
    """OI 历史（v1 最佳努力）：expiration='*' 是否可用需实测；失败静默跳过不中断归档。"""
    method = getattr(client, "option_history_open_interest", None)
    if method is None:
        return 0
    # 实测结论：免费档 PERMISSION_DENIED（需 Value 订阅）→ 记录一次后不再尝试
    row = conn.execute("SELECT value FROM meta WHERE key='oi_unavailable'").fetchone()
    if row:
        return 0
    limiter.wait()
    try:
        df = method(symbol=t, expiration="*", start_date=start, end_date=end)
    except Exception as e:  # noqa: BLE001
        msg = str(e).lower()
        if any(k in msg for k in ("permission", "subscription", "value subscription")):
            conn.execute("INSERT OR REPLACE INTO meta(key,value) VALUES('oi_unavailable','1')")
            _log(f"{t} OI 接口免费档不可用（已记录，后续归档不再尝试）: {e}")
        else:
            _log(f"{t} OI 拉取失败（实测项，跳过）: {e}")
        return 0
    if df is None or df.empty:
        return 0
    d = df.copy()
    if "created" in d.columns:
        d["date"] = _to_trading_date(d["created"]).dt.strftime("%Y-%m-%d")
    elif "date" in d.columns:
        d["date"] = pd.to_datetime(d["date"]).dt.strftime("%Y-%m-%d")
    d["expiration"] = pd.to_datetime(d["expiration"]).dt.strftime("%Y-%m-%d")
    d["root"] = d.get("root", d.get("symbol", t))
    d["right"] = d["right"].astype(str).str.upper().str[0]
    oi_col = "open_interest" if "open_interest" in d.columns else ("oi" if "oi" in d.columns else None)
    if oi_col is None or "strike" not in d.columns:
        _log(f"{t} OI 返回列不完整，跳过（列: {list(d.columns)}）")
        return 0
    rows = [
        (r.date, r.root, r.expiration, float(r.strike), r.right, _f(getattr(r, oi_col)))
        for r in d.itertuples(index=False)
        if r.right in ("C", "P") and r.strike == r.strike
    ]
    conn.executemany(
        "INSERT OR IGNORE INTO option_oi VALUES (?,?,?,?,?,?)", rows
    )
    _log(f"{t} OI {len(rows)} 行（实测项）")
    return len(rows)


def _merge_stock_eod_file(t: str, new_df: pd.DataFrame) -> None:
    """把新股票 EOD 并入 data/raw 下的 stock_eod.csv.gz（convert 的现货来源）。"""
    tdir = RAW_DIR / t
    tdir.mkdir(parents=True, exist_ok=True)
    f = tdir / "stock_eod.csv.gz"
    frames = []
    if f.exists() and f.stat().st_size > 0:
        try:
            frames.append(pd.read_csv(f, compression="gzip"))
        except Exception:  # noqa: BLE001
            pass
    frames.append(new_df)
    if frames:
        merged = pd.concat(frames, ignore_index=True).drop_duplicates()
        merged.to_csv(f, index=False, compression="gzip")


def _f(v):
    try:
        x = float(v)
        return x if x == x else None
    except (TypeError, ValueError):
        return None


def _i(v):
    try:
        return int(float(v))
    except (TypeError, ValueError):
        return 0


def _run_backfill(steps: list[str]) -> None:
    for step in steps:
        _log(f"运行 backfill --{step} ...")
        subprocess.run(
            [PYTHON, str(REPO_ROOT / "scripts" / "backfill_history.py"), f"--{step}"],
            cwd=REPO_ROOT,
            check=False,
        )


def _git_commit_push() -> str:
    today = datetime.date.today().isoformat()
    def _git(*args: str) -> subprocess.CompletedProcess:
        return subprocess.run(["git", *args], cwd=REPO_ROOT, capture_output=True, text=True)
    _git("add", "data/iv_history", "data/closes")
    if _git("diff", "--cached", "--quiet").returncode == 0:
        return "无数据变化，跳过推送"
    if _git("commit", "-m", f"更新历史数据 {today}").returncode != 0:
        return "git commit 失败"
    pull = _git("pull", "--rebase")
    if pull.returncode != 0:
        return f"git pull --rebase 失败: {pull.stderr.strip()[:200]}"
    push = _git("push")
    if push.returncode != 0:
        return f"git push 失败: {push.stderr.strip()[:200]}"
    return "已推送"


def _backup(summary: str) -> str:
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    ts = time.strftime("%Y%m%d")
    if not DB_PATH.exists():
        return "无数据库，跳过备份"
    dest = BACKUP_DIR / f"options_eod_{ts}.db"
    shutil.copy2(DB_PATH, dest)
    (BACKUP_DIR / f"summary_{ts}.txt").write_text(summary, encoding="utf-8")
    backups = sorted(BACKUP_DIR.glob("options_eod_*.db"))
    for old in backups[:-KEEP_BACKUPS]:
        old.unlink(missing_ok=True)
    return f"已备份到 {dest}（保留最近 {KEEP_BACKUPS} 份）"


def _popup(title: str, msg: str) -> None:
    """弹窗由独立子进程显示：归档脚本立即退出，计划任务不会被阻塞。
    （阻塞弹窗会导致任务一直"运行中"，下次归档无法触发。）"""
    try:
        code = (
            "import ctypes,sys;"
            "ctypes.windll.user32.MessageBoxW(0, sys.argv[1], sys.argv[2], 0x40)"
        )
        subprocess.Popen(
            [sys.executable, "-c", code, msg, title],
            creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
        )
    except Exception:  # noqa: BLE001
        pass


def main() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:  # noqa: BLE001
        pass
    p = argparse.ArgumentParser(description="OPTION-ALERT 定期归档")
    p.add_argument("--backup-only", action="store_true", help="只做备份")
    p.add_argument("--no-push", action="store_true", help="不推送 git（仅本地更新）")
    args = p.parse_args()

    tickers = _tickers()
    today = datetime.date.today()
    end = today - datetime.timedelta(days=1)  # EOD 有 1 天延迟
    conn = _connect()
    last = _last_archive_date(conn)
    conn.close()
    start = max(last + datetime.timedelta(days=1), end - datetime.timedelta(days=45))
    _log(f"标的({len(tickers)}) | 归档窗口 {start} ~ {end}（上次归档 {last}）")

    summary_parts: list[str] = []
    if not args.backup_only:
        client = _make_client()
        limiter = RateLimiter(20)
        opt_n, stk_n, oi_n, fails = _fetch_and_store(client, limiter, tickers, start, end)
        summary_parts.append(f"期权新增 {opt_n} 行 | 股票新增 {stk_n} 行 | OI 新增 {oi_n} 行")
        if fails:
            summary_parts.append(f"失败: {', '.join(fails)}")
        _run_backfill(["prices"])
        subprocess.run(
            [PYTHON, str(REPO_ROOT / "scripts" / "backfill_history.py"), "--convert", "--force"],
            cwd=REPO_ROOT,
            check=False,
        )
        if not args.no_push:
            summary_parts.append(_git_commit_push())
    # 更新进度：成功→end；部分失败→回退 7 天（下次重补重叠窗口）；完全失败/无数据→不动
    if not args.backup_only and (opt_n + stk_n) > 0:
        new_last = end if not fails else end - datetime.timedelta(days=7)
    else:
        new_last = last
    conn = _connect()
    conn.execute(
        "INSERT OR REPLACE INTO meta(key,value) VALUES('last_archive_date',?)",
        (new_last.isoformat(),),
    )
    conn.commit()
    conn.close()

    summary = " | ".join(summary_parts) if summary_parts else "（无新增）"
    bk = _backup(f"归档 {end} | {summary}\n标的: {', '.join(tickers)}\n")
    final = f"归档完成（数据截至 {end}）\n{summary}\n{bk}"
    _log(final)
    _popup("OPTION-ALERT 数据归档", final)


if __name__ == "__main__":
    main()
