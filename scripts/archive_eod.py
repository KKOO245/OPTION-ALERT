#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""OPTION-ALERT 定期归档脚本（两周一次，周六 10:30 由 Windows 计划任务触发）

职责（全部自动）：
  1) 拉取上次归档以来的 ThetaData EOD 全链 → 写入 SQLite 研究档案
     + 保存原始分块（供 IV 转换读取，同一存储）
  2) 归档前自查 data/closes：不通过就先按缺口补齐，再复检（结果进摘要与弹窗）
  3) 重算 data/iv_history（复用 backfill_history --convert；现货缺口读 data/closes）
  4) 把每日合约快照（data/chain_history）并入 SQLite（chain_oi_daily 表）
  5) git 提交推送（先 pull --rebase --autostash 防冲突/脏工作区）
  6) 备份：SQLite 拷贝到备份目录 + 摘要文件（保留最近 8 份）
     + 简报链存档目录（OPTION_ALERT_CHAIN_ARCHIVE）增量镜像到备份目录（只增不删）
  7) 弹窗汇报结果（计划任务跑完可见）

用法：
  python scripts/archive_eod.py              # 正常归档
  python scripts/archive_eod.py --backup-only # 只做备份（数据无新增时）
  python scripts/archive_eod.py --refresh-prices  # 额外重建 data/closes 全历史（一般不用）

路径（可用环境变量覆盖）：
  OPTION_ALERT_DB_DIR    默认 D:\\git\\EXTERNAL DATA\\OPTION-ALERT-DB
  OPTION_ALERT_BACKUP_DIR 默认 D:\\git\\EXTERNAL DATA\\OPTION-ALERT-BACKUP
  OPTION_ALERT_CHAIN_ARCHIVE        默认 D:\\git\\EXTERNAL DATA\\OPTION-ALERT-CHAIN-ARCHIVE
  OPTION_ALERT_CHAIN_ARCHIVE_BACKUP 默认 <OPTION_ALERT_BACKUP_DIR>\\chain_archive_mirror
  THETADATA_RAW_DIR       默认 D:\\git\\EXTERNAL DATA\\OPTION-ALERT-RAW（回填脚本同款逻辑）
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
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
CHAIN_ARCHIVE_SRC = Path(
    os.environ.get("OPTION_ALERT_CHAIN_ARCHIVE")
    or r"D:\git\EXTERNAL DATA\OPTION-ALERT-CHAIN-ARCHIVE"
)
CHAIN_ARCHIVE_BACKUP = Path(
    os.environ.get("OPTION_ALERT_CHAIN_ARCHIVE_BACKUP")
    or str(BACKUP_DIR / "chain_archive_mirror")
)


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
        CREATE TABLE IF NOT EXISTS chain_oi_daily (
          date TEXT, root TEXT, contract_symbol TEXT,
          open_interest REAL, volume REAL,
          PRIMARY KEY (date, contract_symbol)
        );
        CREATE TABLE IF NOT EXISTS chain_full_daily (
          date TEXT, root TEXT, contract_symbol TEXT,
          strike REAL, expiration TEXT, right TEXT,
          open_interest REAL, volume REAL,
          bid REAL, ask REAL, last REAL, mid REAL,
          iv REAL, delta REAL, gamma REAL, theta REAL, vega REAL, rho REAL, dte REAL,
          PRIMARY KEY (date, contract_symbol)
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


def _run_script(script: str) -> subprocess.CompletedProcess:
    # 必须显式 utf-8：子脚本输出中文，Windows 默认用 GBK 解码会让读取线程抛
    # UnicodeDecodeError，stdout 直接丢掉（摘要只剩 rc=0，看到也没用）。
    return subprocess.run(
        [PYTHON, str(REPO_ROOT / "scripts" / script)],
        cwd=REPO_ROOT, capture_output=True, text=True,
        encoding="utf-8", errors="replace",
    )


def _brief_line(text: str, markers: tuple[str, ...], fallback: str) -> str:
    """取子脚本输出里最适合进摘要的一行：优先汇总行（按 markers 前缀匹配），
    否则退回最后一行非空输出。"""
    lines = [l.strip() for l in (text or "").splitlines() if l.strip()]
    for line in lines:
        if any(line.startswith(m) for m in markers):
            return line
    return lines[-1] if lines else fallback


def _closes_selfcheck() -> tuple[bool, str]:
    """跑 data/closes 健康检查。返回 (是否通过, 汇总行摘要)。"""
    r = _run_script("check_closes_health.py")
    brief = _brief_line(r.stdout, ("[closes-check] 通过", "[closes-check] 未通过"),
                        f"rc={r.returncode}")
    return r.returncode == 0, brief


def _closes_precheck_repair() -> str:
    """归档前：closes 自查 → 不通过就按缺口补齐 → 复检。返回写进摘要的一行。

    修复用与每日 workflow 同一个脚本（缺口驱动、格子级、幂等）；
    无缺口时该脚本自身走快路径，不发请求、不写文件。
    """
    ok_before, brief = _closes_selfcheck()
    if ok_before:
        _log(f"closes 自查通过：{brief}")
        return "closes 自查：通过"
    _log(f"closes 自查未通过：{brief}")
    rep = _run_script("update_closes_daily.py")
    rep_brief = _brief_line(rep.stdout, ("[closes] 完成",), f"rc={rep.returncode}")
    _log(f"closes 缺口补齐：{rep_brief}")
    ok_after, brief_after = _closes_selfcheck()
    _log(f"closes 复检：{'通过' if ok_after else '仍未通过'}（{brief_after}）")
    return (
        f"closes 自查未通过（{brief}）→ 已补（{rep_brief}）→ "
        f"复检{'通过' if ok_after else '仍未通过：' + brief_after}"
    )


def _git_commit_push() -> str:
    today = datetime.date.today().isoformat()
    def _git(*args: str) -> subprocess.CompletedProcess:
        return subprocess.run(
            ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True,
            encoding="utf-8", errors="replace",
        )
    # data/closes 也提交：归档前只做格子级缺口自愈（不是整表重写），补好的数据要进仓库
    _git("add", "data/iv_history", "data/oi_history", "data/closes")
    if _git("diff", "--cached", "--quiet").returncode == 0:
        return "无数据变化，跳过推送"
    if _git("commit", "-m", f"更新历史数据 {today}").returncode != 0:
        return "git commit 失败"
    pull = _git("pull", "--rebase", "--autostash")
    if pull.returncode != 0:
        return f"git pull --rebase --autostash 失败: {pull.stderr.strip()[:200]}"
    push = _git("push")
    if push.returncode != 0:
        return f"git push 失败: {push.stderr.strip()[:200]}"
    return "已推送"


def _git_pull() -> str:
    """归档前先同步远端，确保 data/chain_history 是最新的。"""
    pull = subprocess.run(
        ["git", "pull", "--rebase", "--autostash"], cwd=REPO_ROOT,
        capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    if pull.returncode != 0:
        return f"git pull --rebase --autostash 失败（继续，可能漏最新快照）: {pull.stderr.strip()[:200]}"
    return "已同步远端"


def _ingest_chain_history(conn: sqlite3.Connection, hist_dir: Path | None = None) -> tuple[int, int]:
    """把每日合约快照（data/chain_history）并入 SQLite，作为 OI 历史后台。

    与 git 文件语义一致：同一日期同一合约以最后一次写入为准（INSERT OR REPLACE）。
    全字段文件（含 strike/expiration/iv/greeks）→ 同时并入 chain_full_daily；
    旧版 4 字段文件 → 只并入 chain_oi_daily。
    """
    hist_dir = hist_dir or (REPO_ROOT / "data" / "chain_history")
    if not hist_dir.is_dir():
        return 0
    total = 0
    full_total = 0
    for f in sorted(hist_dir.glob("*/*.csv.gz")):
        try:
            df = pd.read_csv(f, compression="gzip")
        except Exception as e:  # noqa: BLE001
            _log(f"chain_history 读取失败 {f}: {e}")
            continue
        if df.empty:
            continue
        ticker = f.parent.name.upper()
        if "snapshot_date" in df.columns:
            dates = df["snapshot_date"].astype(str).tolist()
        else:
            dates = [f.stem] * len(df)
        rows = [
            (d, ticker, str(r.contractSymbol), _f(r.openInterest), _f(r.volume))
            for r, d in zip(df.itertuples(index=False), dates)
        ]
        conn.executemany(
            "INSERT OR REPLACE INTO chain_oi_daily VALUES (?,?,?,?,?)", rows
        )
        total += len(rows)
        # 全字段：新格式文件才有 strike/expiration/iv 等列
        if {"strike", "expiration", "right", "iv"}.issubset(df.columns):
            full_rows = []
            for r, d in zip(df.itertuples(index=False), dates):
                full_rows.append(
                    (
                        d, ticker, str(r.contractSymbol),
                        _f(getattr(r, "strike", None)),
                        str(getattr(r, "expiration", "") or ""),
                        str(getattr(r, "right", "") or ""),
                        _f(getattr(r, "openInterest", None)),
                        _f(getattr(r, "volume", None)),
                        _f(getattr(r, "bid", None)),
                        _f(getattr(r, "ask", None)),
                        _f(getattr(r, "last", None)),
                        _f(getattr(r, "mid", None)),
                        _f(getattr(r, "iv", None)),
                        _f(getattr(r, "delta", None)),
                        _f(getattr(r, "gamma", None)),
                        _f(getattr(r, "theta", None)),
                        _f(getattr(r, "vega", None)),
                        _f(getattr(r, "rho", None)),
                        _f(getattr(r, "dte", None)),
                    )
                )
            conn.executemany(
                "INSERT OR REPLACE INTO chain_full_daily "
                "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                full_rows,
            )
            full_total += len(full_rows)
    if total:
        conn.commit()
    return total, full_total


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


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _mirror_chain_archive() -> str:
    """把简报"链存档"目录增量镜像到备份目录：只增不删、不覆盖已一致的文件。

    - 源：`OPTION_ALERT_CHAIN_ARCHIVE`（默认 D:\\git\\EXTERNAL DATA\\OPTION-ALERT-CHAIN-ARCHIVE）
    - 目标：`OPTION_ALERT_CHAIN_ARCHIVE_BACKUP`（默认 <BACKUP_DIR>\\chain_archive_mirror）
    - 判定"是否需要复制"用文件大小（存档文件一经写入不再变化，且同一分钟不重复写），
      新复制的文件再用 sha256 与源比对一次，对不上就计入 bad、下轮重试。
    - 只读源、只写目标；**从不删除**目标里的任何文件。
    - ⚠️ 目标与源在同一块盘时，只能防"误删 / 软件损坏"，防不住硬盘故障；
      要异地冗余，请把 OPTION_ALERT_CHAIN_ARCHIVE_BACKUP 指到另一块盘。
    """
    src, dst = CHAIN_ARCHIVE_SRC, CHAIN_ARCHIVE_BACKUP
    if not src.exists():
        return f"链存档镜像：源不存在（{src}），跳过"
    n_new = n_fix = n_same = n_bad = 0
    bytes_new = 0
    for root, _dirs, names in os.walk(src):
        rel = Path(root).relative_to(src)
        for name in names:
            s = Path(root) / name
            d = dst / rel / name
            try:
                if d.exists() and d.stat().st_size == s.stat().st_size:
                    n_same += 1
                    continue
                existed = d.exists()
                d.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(s, d)
                if d.stat().st_size != s.stat().st_size or _sha256(s) != _sha256(d):
                    n_bad += 1
                    continue
                if existed:
                    n_fix += 1
                else:
                    n_new += 1
                    bytes_new += d.stat().st_size
            except OSError:
                n_bad += 1
    msg = (f"链存档镜像：新增 {n_new} 份（{bytes_new / 1048576:.1f} MB）"
           f"｜补齐 {n_fix} 份｜已一致 {n_same} 份")
    if n_bad:
        msg += f"｜⚠️ 校验未过 {n_bad} 份（下轮重试）"
    return msg + f" → {dst}"


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
    p.add_argument("--refresh-prices", action="store_true",
                   help="额外用 yfinance 重建 data/closes 全历史（默认不做：closes 归每日 workflow）")
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
        _log(_git_pull())
        summary_parts.append(_closes_precheck_repair())
        client = _make_client()
        limiter = RateLimiter(20)
        opt_n, stk_n, oi_n, fails = _fetch_and_store(client, limiter, tickers, start, end)
        conn2 = _connect()
        oi_snap, full_snap = _ingest_chain_history(conn2)
        conn2.close()
        summary_parts.append(
            f"期权新增 {opt_n} 行 | 股票新增 {stk_n} 行 | OI 新增 {oi_n} 行 | "
            f"快照OI并入 {oi_snap} 行 | 全字段链并入 {full_snap} 行"
        )
        if fails:
            summary_parts.append(f"失败: {', '.join(fails)}")
        if args.refresh_prices:
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
    cm = _mirror_chain_archive()
    final = f"归档完成（数据截至 {end}）\n{summary}\n{bk}\n{cm}"
    _log(final)
    _popup("OPTION-ALERT 数据归档", final)


if __name__ == "__main__":
    main()
