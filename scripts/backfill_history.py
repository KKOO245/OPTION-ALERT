#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""OPTION-ALERT 历史数据回填脚本（一次性任务）

数据源：
  1) ThetaData 官方 Python 库（直连服务器，无需本地终端）
     - 期权 EOD 链：2023-06-01 ~ 昨日，默认全量（所有行权价、所有到期日）
     - 股票 EOD：同窗口，用于对现货（spot）
     - （可选 --greeks）EOD Greeks 最佳努力尝试
  2) yfinance：18 标的全历史日线（不限窗口，供未来项目使用）

输出：
  data/raw/thetadata/{TICKER}/{YYYYMMDD}_{YYYYMMDD}.parquet
      原始期权 EOD 分块，文件名=起止日期（git 忽略）
      （无 pyarrow 时自动回退 .csv.gz；空块留 0 字节标记文件）
  data/raw/thetadata/{TICKER}/stock_eod.csv.gz    股票 EOD（git 忽略）
  data/raw/thetadata/{TICKER}/greeks/...          （可选）EOD Greeks（git 忽略）
  data/closes/{TICKER}.csv                        yfinance 全历史日线（进 git）
  data/iv_history/{TICKER}.csv                    每日 ATM IV 序列（进 git）

ATM IV 定义（对齐 src/metrics.py）：
  - near    = DTE>=1 的最近到期日
  - monthly = 除 near 外 DTE 最接近 30 且落在 [10,60] 的到期日
  - ATM 行权价 = 距离当日现货最近的行权价；ATM IV = 该行权价 Call/Put IV 均值
  - IV 优先用数据源自带 iv 字段；缺失时由 EOD 收盘价（无收盘价则用 (bid+ask)/2）
    按 Black-Scholes 反解，无风险利率沿用项目约定 RISK_FREE_RATE=0.05（参考级）

用法：
  python scripts/backfill_history.py --probe QQQ      # 连通性 + 字段自检
  python scripts/backfill_history.py --download        # 期权 EOD（全量）+ 股票 EOD
  python scripts/backfill_history.py --prices          # yfinance 全历史日线
  python scripts/backfill_history.py --convert         # 生成 data/iv_history/*.csv
  python scripts/backfill_history.py --all             # download + prices + convert
  python scripts/backfill_history.py --all --greeks    # 额外最佳努力拉 EOD Greeks
  python scripts/backfill_history.py --report          # 查看回填覆盖情况

说明：
  - 默认全量下载所有行权价与所有到期日；如只想小批量验证，可
    --strike-range 15 --max-dte 90 收窄。
  - 分块下载带断点续传：单块失败会自动对半拆分重试，不会因单月数据过大而整月丢失。
  - 防封号设计：默认 20 req/min（上限 30 的 2/3）+ 最小间隔 2.5s + 随机抖动；
    疑似限速自动退避 60s；连续失败 12 次自动熔断；下载期间有单实例锁，
    防止并发运行把额度打爆。
  - 凭证三选一（自动识别，绝不写进代码）：
      1) 环境变量 THETADATA_API_KEY
      2) creds.txt（第一行邮箱，第二行密码），放在运行目录
      3) 环境变量 THETADATA_EMAIL / THETADATA_PASSWORD
"""

from __future__ import annotations

import argparse
import math
import os
import random
import sys
import time
from collections import deque
from datetime import date, timedelta
from pathlib import Path

import pandas as pd
import numpy as np

try:
    np_erf = np.erf
except AttributeError:  # numpy < 2.0 兜底
    from math import erf as _math_erf

    np_erf = np.vectorize(_math_erf)

REPO_ROOT = Path(__file__).resolve().parent.parent
_RAW_ENV = os.environ.get("THETADATA_RAW_DIR")
if _RAW_ENV:
    RAW_DIR = Path(_RAW_ENV)
else:
    _RAW_NEW = Path(r"D:\git\EXTERNAL DATA\OPTION-ALERT-RAW")
    _RAW_LEGACY = REPO_ROOT / "data" / "raw" / "thetadata"
    RAW_DIR = _RAW_NEW if _RAW_NEW.exists() else _RAW_LEGACY
CLOSES_DIR = REPO_ROOT / "data" / "closes"
IV_HIST_DIR = REPO_ROOT / "data" / "iv_history"
TICKERS_FILE = REPO_ROOT / "config" / "tickers.txt"

DEFAULT_START = date(2023, 6, 1)  # ThetaData 免费档 EOD 起算日（官方订阅页）
RISK_FREE_RATE = 0.05  # 与 src/data_fetcher.py RISK_FREE_RATE 保持一致（参考级）
IV_SANITY = (0.001, 3.0)  # IV 合理性过滤，与项目 0<iv<3 一致
IV_USE_BAND = (0.02, 2.5)  # 输出 IV 合理性带：2%~250%（剔除 299%/0.2% 类伪值）
NEAR_MONTHLY_RATIO_CAP = 3.5  # near IV / monthly IV 超过该值视为 near 伪值（1DTE stale 报价）
MONTHLY_ABS_CAP = 2.0  # monthly IV >200% 视为不可靠
LOCK_FILE = RAW_DIR / ".backfill.lock"
_CONSECUTIVE_FAILURES = 0


class SeriesAborted(Exception):
    """单个标的/序列中止（跳过，不影响其他标的）。"""


def _log(msg: str) -> None:
    print(f"[backfill] {msg}", flush=True)


def _tickers(overrides: list[str] | None) -> list[str]:
    if overrides:
        return [t.strip().upper() for t in overrides if t.strip()]
    if not TICKERS_FILE.exists():
        raise SystemExit(f"找不到标的清单: {TICKERS_FILE}")
    out = []
    for line in TICKERS_FILE.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if s and not s.startswith("#"):
            out.append(s.upper())
    if not out:
        raise SystemExit("config/tickers.txt 里没有有效标的")
    return out


def _iter_months(start: date, end: date):
    """按自然月切分 [start, end]，返回 (YYYY-MM, 月首, 月末)。"""
    cur = start.replace(day=1)
    while cur <= end:
        if cur.month == 12:
            nxt = date(cur.year + 1, 1, 1)
        else:
            nxt = date(cur.year, cur.month + 1, 1)
        ms, me = cur, min(nxt - timedelta(days=1), end)
        yield cur.strftime("%Y-%m"), ms, me
        cur = nxt


def _make_client():
    try:
        from thetadata import ThetaClient
    except Exception as e:  # noqa: BLE001
        raise SystemExit(
            f"thetadata 导入失败: {e}\n"
            "请确认已 pip install thetadata（要求 Python 3.12+），并把上面的报错发回"
        )
    api_key = os.environ.get("THETADATA_API_KEY")
    if api_key:
        _log("使用 THETADATA_API_KEY 认证")
        return ThetaClient(api_key=api_key, dataframe_type="pandas")
    email = os.environ.get("THETADATA_EMAIL")
    password = os.environ.get("THETADATA_PASSWORD")
    if email and password:
        _log("使用环境变量邮箱/密码认证")
        return ThetaClient(email=email, password=password, dataframe_type="pandas")
    creds = Path("creds.txt")
    if creds.exists():
        lines = [
            x.strip()
            for x in creds.read_text(encoding="utf-8").splitlines()
            if x.strip()
        ]
        if len(lines) >= 2:
            _log(f"使用 creds.txt 认证（{lines[0]}）")
            return ThetaClient(email=lines[0], password=lines[1], dataframe_type="pandas")
    raise SystemExit(
        "未找到凭证：设置 THETADATA_API_KEY，或在运行目录放 creds.txt（第一行邮箱、第二行密码）"
    )


class RateLimiter:
    """防封号限速：滑动窗口 + 最小间隔双保险。

    免费档官方上限 30 req/min，这里默认只用到 20 req/min，
    且任意两次请求间隔 >= 2.5s（另加 0~0.5s 抖动），从根上避免突发。
    """

    def __init__(self, per_min: int = 20, min_interval: float = 2.5):
        self.per_min = max(1, per_min)
        self.min_interval = max(0.5, min_interval)
        self._stamps: deque[float] = deque()
        self._last = 0.0

    def wait(self) -> None:
        now = time.monotonic()
        while self._stamps and now - self._stamps[0] >= 60.0:
            self._stamps.popleft()
        need = 0.0
        if len(self._stamps) >= self.per_min:
            need = max(need, 60.0 - (now - self._stamps[0]) + 0.3)
        need = max(need, self.min_interval - (now - self._last), 0.0)
        if need > 0:
            need += random.uniform(0.0, 0.5)
            if need > 1.0:
                _log(f"限速中，等待 {need:.1f}s ...")
            time.sleep(need)
        now = time.monotonic()
        self._stamps.append(now)
        self._last = now


def _acquire_lock() -> None:
    """单实例锁：防止并发运行两个下载进程把额度打爆。"""
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    if LOCK_FILE.exists():
        age = time.time() - LOCK_FILE.stat().st_mtime
        if age < 3600:
            raise SystemExit(
                "检测到另一个回填进程正在运行（data/raw/thetadata/.backfill.lock）。"
                "若确认没有其他进程，请删除该文件后重试。"
            )
        LOCK_FILE.unlink(missing_ok=True)
    LOCK_FILE.write_text(str(os.getpid()), encoding="utf-8")
    _log("已获取单实例锁")


def _release_lock() -> None:
    try:
        LOCK_FILE.unlink(missing_ok=True)
    except Exception:  # noqa: BLE001
        pass


def _is_permission_error(e: Exception) -> bool:
    """凭证/权限/套餐类错误：不重试、不拆分，直接停该序列，避免无谓请求。"""
    t = str(e).lower()
    return any(
        k in t
        for k in (
            "403",
            "401",
            "forbidden",
            "permission",
            "unauthorized",
            "not authorized",
            "subscription",
            "plan",
        )
    )


def _is_no_data_error(e: Exception) -> bool:
    """权威"无数据"（如新股上市前）：不算失败，直接记空标记或二分定位边界。"""
    t = str(e).lower()
    return "no data found" in t or "no data" in t


# ---------------------------------------------------------------- 存储
def _chunk_paths(tdir: Path, ms: date, me: date):
    """分块文件名 = 起止日期，断点续传可精确判定覆盖。"""
    stem = f"{ms:%Y%m%d}_{me:%Y%m%d}"
    return tdir / f"{stem}.parquet", tdir / f"{stem}.csv.gz"


def _save_frame(df, parquet_path: Path, csv_path: Path) -> None:
    """保存分块数据：优先 parquet（小且快），无 pyarrow 时回退 csv.gz。
    空数据（权威无数据）留 0 字节标记文件，避免反复重试。"""
    parquet_path.parent.mkdir(parents=True, exist_ok=True)
    if df is None or len(df) == 0:
        csv_path.write_bytes(b"")
        return
    try:
        import pyarrow  # noqa: F401

        df.to_parquet(parquet_path, index=False)
        return
    except ImportError:
        pass
    except Exception as e:  # noqa: BLE001
        _log(f"parquet 保存失败（{e}），回退 csv.gz")
    df.to_csv(csv_path, index=False, compression="gzip")


def _chunk_covered(tdir: Path, ms: date, me: date) -> bool:
    p, c = _chunk_paths(tdir, ms, me)
    return p.exists() or c.exists()


def _iter_chunk_frames(tdir: Path):
    for f in sorted(tdir.glob("*.parquet")):
        if f.stat().st_size > 0:
            yield pd.read_parquet(f)
    for f in sorted(tdir.glob("*.csv.gz")):
        if f.name == "stock_eod.csv.gz" or f.stat().st_size == 0:
            continue
        yield pd.read_csv(f, compression="gzip")


# ---------------------------------------------------------------- 下载
def _download_range(
    client, limiter: RateLimiter, t: str, ms: date, me: date, call, tdir: Path, depth: int = 0
) -> bool:
    """下载 [ms, me] 一个分块；失败自动对半拆分重试（断点续传）。"""
    global _CONSECUTIVE_FAILURES
    if _chunk_covered(tdir, ms, me):
        _CONSECUTIVE_FAILURES = 0
        return True
    if depth > 12:
        _log(f"{t} {ms} ~ {me} 拆分过深仍失败，跳过（可后续手动补）")
        return False
    try:
        limiter.wait()
        df = call(ms, me)
    except Exception as e:  # noqa: BLE001
        _log(f"{t} {ms} ~ {me} 失败: {e}")
        if _is_no_data_error(e):
            # 权威无数据：不算失败；范围大则二分定位边界，小范围直接记空标记
            _CONSECUTIVE_FAILURES = 0
            span = (me - ms).days
            if span <= 5:
                p, c = _chunk_paths(tdir, ms, me)
                _save_frame(None, p, c)
                _log(f"{t} {ms} ~ {me} 无数据（记录空标记）")
                return True
            mid = ms + timedelta(days=span // 2)
            ok1 = _download_range(client, limiter, t, ms, mid, call, tdir, depth + 1)
            ok2 = _download_range(
                client, limiter, t, mid + timedelta(days=1), me, call, tdir, depth + 1
            )
            return ok1 and ok2
        _CONSECUTIVE_FAILURES += 1
        if _is_permission_error(e):
            raise SeriesAborted(f"{t} 凭证/权限/套餐类错误，停止该序列")
        if _CONSECUTIVE_FAILURES >= 12:
            raise SeriesAborted(f"{t} 连续失败过多，已跳过该序列（重跑会自动续传）")
        if "rate" in str(e).lower() or "429" in str(e).lower():
            _log("疑似限速，等待 60s 退避 ...")
            time.sleep(60)
        else:
            time.sleep(3)
        span = (me - ms).days
        if span <= 2:
            return False
        mid = ms + timedelta(days=span // 2)
        ok1 = _download_range(client, limiter, t, ms, mid, call, tdir, depth + 1)
        ok2 = _download_range(
            client, limiter, t, mid + timedelta(days=1), me, call, tdir, depth + 1
        )
        return ok1 and ok2
    # 请求成功：空且范围过大 -> 二分定位有效日期（不算失败，不计数）
    if df is None or len(df) == 0:
        if (me - ms).days > 5:
            mid = ms + timedelta(days=(me - ms).days // 2)
            ok1 = _download_range(client, limiter, t, ms, mid, call, tdir, depth + 1)
            ok2 = _download_range(
                client, limiter, t, mid + timedelta(days=1), me, call, tdir, depth + 1
            )
            return ok1 and ok2
        p, c = _chunk_paths(tdir, ms, me)
        _save_frame(df, p, c)
        _log(f"{t} {ms} ~ {me} 无数据（记录空标记）")
        _CONSECUTIVE_FAILURES = 0
        return True
    p, c = _chunk_paths(tdir, ms, me)
    _save_frame(df, p, c)
    _log(f"{t} {ms} ~ {me} {len(df)} 行")
    _CONSECUTIVE_FAILURES = 0
    return True


def cmd_download(
    client,
    tickers: list[str],
    start: date,
    end: date,
    strike_range: int | None,
    max_dte: int | None,
    rate: int,
    greeks: bool,
) -> None:
    global _CONSECUTIVE_FAILURES
    limiter = RateLimiter(rate)
    opt_kwargs: dict = {"expiration": "*"}
    if strike_range:
        opt_kwargs["strike_range"] = strike_range
    if max_dte:
        opt_kwargs["max_dte"] = max_dte
    ok, fail = 0, 0
    for t in tickers:
        _CONSECUTIVE_FAILURES = 0
        tdir = RAW_DIR / t
        tdir.mkdir(parents=True, exist_ok=True)
        # 股票 EOD（现货）
        stock_out = tdir / "stock_eod.csv.gz"
        if stock_out.exists() and stock_out.stat().st_size > 0:
            _log(f"{t} 股票 EOD 已存在，跳过")
        else:
            _log(f"{t} 拉取股票 EOD（API 单次限 365 天，自动分块）...")
            frames = []
            cur = start
            while cur <= end:
                chunk_end = min(cur + timedelta(days=330), end)
                limiter.wait()
                try:
                    df = client.stock_history_eod(
                        symbol=t, start_date=cur, end_date=chunk_end
                    )
                    if df is not None and not df.empty:
                        frames.append(df)
                        _log(f"{t} 股票 EOD {cur} ~ {chunk_end} {len(df)} 行")
                except Exception as e:  # noqa: BLE001
                    if _is_no_data_error(e):
                        _log(f"{t} 股票 EOD {cur} ~ {chunk_end} 无数据（正常）")
                    else:
                        _log(f"{t} 股票 EOD {cur} ~ {chunk_end} 失败: {e}")
                        fail += 1
                cur = chunk_end + timedelta(days=1)
            if frames:
                merged = pd.concat(frames, ignore_index=True).drop_duplicates()
                merged.to_csv(stock_out, index=False, compression="gzip")
                _log(f"{t} 股票 EOD 合并 {len(merged)} 行")
                ok += 1
        # 期权 EOD（默认全链：所有行权价、所有到期；按月分块，失败自动二分）
        def _opt_call(ms: date, me: date):
            return client.option_history_eod(
                symbol=t, start_date=ms, end_date=me, **opt_kwargs
            )

        try:
            for _ym, ms, me in _iter_months(start, end):
                if _download_range(client, limiter, t, ms, me, _opt_call, tdir):
                    ok += 1
                else:
                    fail += 1
        except SeriesAborted as e:
            _log(f"{t} 期权序列中止: {e}")
            fail += 1
        # 可选：EOD Greeks（最佳努力，接口/权限因库版本而异）
        if greeks:
            gdir = tdir / "greeks"
            gdir.mkdir(parents=True, exist_ok=True)
            method = getattr(client, "option_history_greeks_eod", None)
            if method is None:
                _log(f"{t} 当前 thetadata 库无 option_history_greeks_eod，--greeks 跳过")
            else:
                def _greeks_call(ms: date, me: date):
                    return method(
                        symbol=t, start_date=ms, end_date=me, **opt_kwargs
                    )

                try:
                    for _ym, ms, me in _iter_months(start, end):
                        if _download_range(client, limiter, t, ms, me, _greeks_call, gdir):
                            ok += 1
                        else:
                            fail += 1
                except SeriesAborted as e:
                    _log(f"{t} Greeks 序列中止: {e}")
                    fail += 1
    _log(f"下载完成：成功 {ok}，失败 {fail}")
    if fail:
        _log("存在失败项，可重跑同一命令续传（已成功的不重复下载）")


def cmd_prices(tickers: list[str]) -> None:
    """yfinance 全历史日线（不限窗口，供未来项目使用）。"""
    try:
        import yfinance as yf
    except ImportError:
        raise SystemExit("未安装 yfinance：请先 pip install yfinance")
    CLOSES_DIR.mkdir(parents=True, exist_ok=True)
    for t in tickers:
        out = CLOSES_DIR / f"{t}.csv"
        _log(f"{t} yfinance 全历史日线 ...")
        try:
            h = yf.Ticker(t).history(period="max", auto_adjust=False)
            if h.empty:
                _log(f"{t} 返回空")
                continue
            h = h.reset_index()
            if "Date" in h.columns:
                h["date"] = pd.to_datetime(h["Date"]).dt.date
            h = h.rename(
                columns={
                    "Open": "open",
                    "High": "high",
                    "Low": "low",
                    "Close": "close",
                    "Adj Close": "adj_close",
                    "Volume": "volume",
                }
            )
            h = h[["date", "open", "high", "low", "close", "adj_close", "volume"]]
            h.to_csv(out, index=False)
            _log(f"{t} -> {out}（{len(h)} 行）")
        except Exception as e:  # noqa: BLE001
            _log(f"{t} 失败: {e}")


# ---------------------------------------------------------------- 转换
def _norm_cols(df: pd.DataFrame) -> pd.DataFrame:
    """ThetaData EOD 字段别名归一化（防御不同版本库的列名差异）。"""
    aliases = {
        "date": ["date", "created", "quote_date", "trading_date"],
        "expiration": ["expiration", "exp"],
        "strike": ["strike", "strike_price"],
        "right": ["right", "option_type", "type"],
        "close": ["close", "last", "last_price"],
        "bid": ["bid"],
        "ask": ["ask"],
        "open_interest": ["open_interest", "oi", "openinterest"],
        "volume": ["volume"],
        "root": ["root", "symbol", "underlying"],
    }
    out = df.rename(columns={})
    for target, cands in aliases.items():
        for c in cands:
            if c in out.columns:
                out = out.rename(columns={c: target})
                break
    return out


def _bs_price(flag: str, spot: float, strike: float, t: float, sigma: float) -> float:
    """Black-Scholes 定价（q=0，与项目 Greeks 口径一致）。"""
    from math import erf, sqrt

    if t <= 0 or sigma <= 0:
        return math.nan
    d1 = (math.log(spot / strike) + (RISK_FREE_RATE + 0.5 * sigma ** 2) * t) / (
        sigma * sqrt(t)
    )
    d2 = d1 - sigma * sqrt(t)
    nd1 = 0.5 * (1.0 + erf(d1 / sqrt(2.0)))
    nd2 = 0.5 * (1.0 + erf(d2 / sqrt(2.0)))
    if flag == "C":
        return spot * nd1 - strike * math.exp(-RISK_FREE_RATE * t) * nd2
    return strike * math.exp(-RISK_FREE_RATE * t) * (1.0 - nd2) - spot * (1.0 - nd1)


def _to_trading_date(s: pd.Series) -> pd.Series:
    """把 EOD 报告时间戳（17:15 ET 生成）归一到美股交易日日期（无时区）。"""
    dt = pd.to_datetime(s, errors="coerce", utc=True, format="mixed")
    return (
        dt.dt.tz_convert("America/New_York")
        .dt.tz_localize(None)
        .dt.normalize()
    )


def _solve_iv(flag: str, spot: float, strike: float, t: float, price: float):
    """二分法反解 IV；失败返回 None。"""
    if price <= 0 or spot <= 0 or strike <= 0 or t <= 0:
        return None
    lo, hi = 1e-4, 5.0
    if price >= _bs_price(flag, spot, strike, t, hi):
        return None  # 价格超出可解范围（深度实值/数据异常）
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        p = _bs_price(flag, spot, strike, t, mid)
        if p < price:
            lo = mid
        else:
            hi = mid
    iv = 0.5 * (lo + hi)
    return iv if IV_SANITY[0] < iv < IV_SANITY[1] else None


def _solve_iv_vec(right, spot, strike, t, price) -> np.ndarray:
    """向量化二分反解 IV（Black-Scholes, q=0）；无法求解的行返回 NaN。
    6~7 百万行从逐行 Python（数十分钟）压到 numpy 秒级。"""
    right = np.asarray(right)
    spot = np.asarray(spot, dtype=float)
    strike = np.asarray(strike, dtype=float)
    t = np.asarray(t, dtype=float)
    price = np.asarray(price, dtype=float)
    is_call = np.asarray([str(r).upper().startswith("C") for r in right])

    def _bs_price(sig: np.ndarray) -> np.ndarray:
        sq = sig * np.sqrt(t)
        d1 = (np.log(spot / strike) + (RISK_FREE_RATE + 0.5 * sig ** 2) * t) / sq
        d2 = d1 - sq
        nd1 = 0.5 * (1.0 + np_erf(d1 / np.sqrt(2.0)))
        nd2 = 0.5 * (1.0 + np_erf(d2 / np.sqrt(2.0)))
        disc = np.exp(-RISK_FREE_RATE * t)
        call = spot * nd1 - strike * disc * nd2
        put = strike * disc * (1.0 - nd2) - spot * (1.0 - nd1)
        return np.where(is_call, call, put)

    valid = (price > 0) & (spot > 0) & (strike > 0) & (t > 0)
    lo = np.full_like(spot, 1e-4)
    hi = np.full_like(spot, 5.0)
    bad = ~valid | (price >= _bs_price(hi))  # 价格超出可解范围
    lo = np.where(bad, np.nan, lo)
    hi = np.where(bad, np.nan, hi)
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        p = _bs_price(mid)
        lo = np.where(p < price, mid, lo)
        hi = np.where(p < price, hi, mid)
    iv = 0.5 * (lo + hi)
    iv = np.where(bad, np.nan, iv)
    iv = np.where((iv > IV_SANITY[0]) & (iv < IV_SANITY[1]), iv, np.nan)
    return iv


def _load_raw_ticker(t: str) -> pd.DataFrame:
    tdir = RAW_DIR / t
    if not tdir.exists():
        raise SystemExit(f"{t} 无原始数据，请先运行 --download")
    frames = list(_iter_chunk_frames(tdir))
    if not frames:
        raise SystemExit(f"{t} 原始数据为空，请先运行 --download")
    df = pd.concat(frames, ignore_index=True)
    return df.drop_duplicates()


def _spot_series(t: str) -> pd.Series:
    """现货序列：ThetaData 股票 EOD（未复权原始价）优先，缺失日期才用 yfinance 补。"""
    spot = pd.Series(dtype=float)
    f = RAW_DIR / t / "stock_eod.csv.gz"
    if f.exists() and f.stat().st_size > 0:
        df = pd.read_csv(f, compression="gzip")
        dc = df.columns
        date_col = (
            "date"
            if "date" in dc
            else ("created" if "created" in dc else dc[0])
        )
        close_col = "close" if "close" in dc else ("last" if "last" in dc else dc[-1])
        s = pd.to_numeric(df[close_col], errors="coerce")
        s.index = _to_trading_date(df[date_col])
        spot = s.dropna().sort_index()
    yf_f = CLOSES_DIR / f"{t}.csv"
    if yf_f.exists():
        df = pd.read_csv(yf_f)
        if "date" in df.columns and "close" in df.columns:
            s = pd.to_numeric(df["close"], errors="coerce")
            s.index = pd.to_datetime(df["date"], errors="coerce").dt.normalize()
            s = s.dropna().sort_index()
            # 注意方向：ThetaData 原始价必须优先，yfinance 只补缺口
            # （yfinance 的 close 可能是复权价，拆股标的上不能覆盖原始价）
            spot = spot.combine_first(s) if not spot.empty else s
    return spot


def cmd_convert(tickers: list[str], start: date, end: date, force: bool) -> None:
    IV_HIST_DIR.mkdir(parents=True, exist_ok=True)
    for t in tickers:
        out = IV_HIST_DIR / f"{t}.csv"
        if out.exists() and not force:
            _log(f"{t} iv_history 已存在（--force 覆盖）")
            continue
        _log(f"{t} 转换中 ...")
        df = _norm_cols(_load_raw_ticker(t))
        required = {"date", "expiration", "strike", "right"}
        missing = required - set(df.columns)
        if missing:
            _log(
                f"{t} 缺字段 {sorted(missing)}（实际列: {list(df.columns)}）——"
                "请把 --probe 输出的列名发回来，脚本会更新字段映射"
            )
            continue
        df["date"] = _to_trading_date(df["date"])
        df["expiration"] = pd.to_datetime(df["expiration"], errors="coerce").dt.normalize()
        df = df[(df["date"] >= pd.Timestamp(start)) & (df["date"] <= pd.Timestamp(end))]
        df["strike"] = pd.to_numeric(df["strike"], errors="coerce")
        df["right"] = df["right"].astype(str).str.upper().str[0]
        df = df[df["right"].isin(["C", "P"])].copy()
        df["dte"] = (df["expiration"] - df["date"]).dt.days
        df = df[df["dte"] >= 1]
        df = df.drop_duplicates(subset=["date", "expiration", "strike", "right"])
        if df.empty:
            _log(f"{t} 窗口内无有效行")
            continue
        # IV：优先数据源自带 iv，缺失再反解
        if "iv" in df.columns:
            prov = pd.to_numeric(df["iv"], errors="coerce")
        else:
            prov = pd.Series([math.nan] * len(df), index=df.index)
        df["iv"] = prov.where(prov.between(IV_SANITY[0], IV_SANITY[1]))
        # 反解所需价格（质量门槛）：
        #   1) 优先"当天有成交"的收盘价（close>0 且 volume>0）
        #   2) 无成交才回退买卖中间价，且要求 bid/ask>0、价差不过宽
        if "close" not in df.columns:
            df["close"] = math.nan
        df["close"] = pd.to_numeric(df["close"], errors="coerce")
        if "volume" not in df.columns:
            df["volume"] = 1
        df["volume"] = pd.to_numeric(df["volume"], errors="coerce").fillna(0)
        traded = (df["close"] > 0) & (df["volume"] > 0)
        if "bid" in df.columns and "ask" in df.columns:
            bid = pd.to_numeric(df["bid"], errors="coerce")
            ask = pd.to_numeric(df["ask"], errors="coerce")
            mid = (bid + ask) / 2.0
            spread = ask - bid
            mid_ok = (bid > 0) & (ask > 0) & (spread <= 0.75 * mid) & (mid >= 0.02)
            df["mid"] = mid.where(mid_ok)
        else:
            df["mid"] = math.nan
        px = df["close"].where(traded)
        px = px.fillna(df["mid"])
        px = px.where(px > 0)
        df["px"] = px
        # 现货（反解 IV 需要当日现货）
        spot = _spot_series(t)
        df["spot"] = df["date"].map(spot)
        df = df.dropna(subset=["spot"])
        if df.empty:
            _log(f"{t} 无现货对齐数据")
            continue
        # 缺失 IV 的行用收盘价反解
        need = df["iv"].isna()
        if need.any():
            solveable = need & df["px"].notna()
            _log(f"{t} 反解 IV（{int(solveable.sum())} 行，向量化）...")
            sub = df[solveable]
            ivs = _solve_iv_vec(
                sub["right"].to_numpy(),
                sub["spot"].to_numpy(dtype=float),
                sub["strike"].to_numpy(dtype=float),
                (sub["dte"].clip(lower=1) / 365.0).to_numpy(dtype=float),
                sub["px"].to_numpy(dtype=float),
            )
            df.loc[solveable, "iv"] = ivs
        df = df[df["iv"].between(IV_USE_BAND[0], IV_USE_BAND[1])]
        # 每 (日期, 到期) 取 ATM 行权价，Call/Put IV 取均值
        if df.empty:
            _log(f"{t} 转换后无有效 ATM IV")
            continue
        g = df.groupby(["date", "expiration", "strike", "right"])["iv"].mean()
        wide = g.unstack("right").reset_index()
        wide.columns.name = None
        iv_cols = [c for c in ["C", "P"] if c in wide.columns]
        wide["iv_atm"] = wide[iv_cols].mean(axis=1, skipna=True)
        wide["spot"] = wide["date"].map(spot)
        wide["dte"] = (wide["expiration"] - wide["date"]).dt.days
        wide = wide[
            wide["iv_atm"].between(IV_USE_BAND[0], IV_USE_BAND[1])
        ].dropna(subset=["spot", "iv_atm"])
        if wide.empty:
            _log(f"{t} 转换后无有效 ATM IV")
            continue
        wide["abs_money"] = (wide["strike"] - wide["spot"]).abs()
        atm = wide.loc[wide.groupby(["date", "expiration"])["abs_money"].idxmin()].copy()
        # 每日 near / monthly（near 需通过 term-structure 合理性门，伪值自动回退下个到期）
        rows = []
        skipped_near = 0
        for d, sub in atm.groupby("date"):
            sub = sub.dropna(subset=["iv_atm"]).sort_values("dte")
            if sub.empty:
                continue
            far_cands = sub[
                (sub["dte"] >= 10)
                & (sub["dte"] <= 60)
            ]
            m_row = (
                far_cands.loc[(far_cands["dte"] - 30).abs().idxmin()]
                if not far_cands.empty
                else None
            )
            m_iv = (
                float(m_row["iv_atm"])
                if m_row is not None and float(m_row["iv_atm"]) <= MONTHLY_ABS_CAP
                else None
            )
            near = None
            for _, cand in sub.iterrows():
                c_iv = float(cand["iv_atm"])
                ok = c_iv <= 2.0 if m_iv is None else c_iv <= NEAR_MONTHLY_RATIO_CAP * m_iv
                if ok:
                    near = cand
                    break
            if near is None:
                skipped_near += 1
                continue
            same_exp = m_row is not None and m_row["expiration"] == near["expiration"]
            rows.append(
                {
                    "date": d.date().isoformat(),
                    "spot": round(float(near["spot"]), 4),
                    "near_exp": near["expiration"].date().isoformat(),
                    "near_dte": int(near["dte"]),
                    "atm_iv_near": round(float(near["iv_atm"]), 4),
                    "monthly_exp": (
                        m_row["expiration"].date().isoformat()
                        if m_row is not None and not same_exp
                        else None
                    ),
                    "monthly_dte": int(m_row["dte"]) if m_row is not None and not same_exp else None,
                    "atm_iv_monthly": round(m_iv, 4) if m_iv is not None and not same_exp else None,
                    "term_ratio": (
                        round(float(near["iv_atm"]) / m_iv, 4)
                        if m_iv is not None and not same_exp
                        else None
                    ),
                    "source": "thetadata_eod",
                }
            )
        if skipped_near:
            _log(f"{t} 有 {skipped_near} 天 near 未通过合理性门，已跳过（不污染序列）")
        res = pd.DataFrame(rows)
        if res.empty:
            _log(f"{t} 无有效 near/monthly ATM IV（数据可能过稀）")
            continue
        res.to_csv(out, index=False)
        iv = res["atm_iv_near"].dropna()
        _log(
            f"{t} -> {out}（{len(res)} 个交易日）| IV 均值 {iv.mean()*100:.1f}% | "
            f"中位 {iv.median()*100:.1f}% | P10 {iv.quantile(0.1)*100:.1f}% | "
            f"P90 {iv.quantile(0.9)*100:.1f}%"
        )
        if not iv.empty:
            top = res.nlargest(3, "atm_iv_near")[["date", "atm_iv_near"]]
            _log(
                t
                + " 最高 IV 日: "
                + " | ".join(
                    f"{r.date} {r.atm_iv_near*100:.1f}%" for r in top.itertuples()
                )
            )


def cmd_report(tickers: list[str]) -> None:
    print("\n=== IV 历史回填覆盖报告 ===")
    for t in tickers:
        f = IV_HIST_DIR / f"{t}.csv"
        if not f.exists():
            print(f"{t:6s}  未转换")
            continue
        df = pd.read_csv(f)
        if df.empty:
            print(f"{t:6s}  空")
            continue
        lo, hi = df["date"].min(), df["date"].max()
        iv = df["atm_iv_near"].dropna()
        print(
            f"{t:6s}  {lo} ~ {hi}  | {len(df)} 天  | "
            f"ATM IV 均值 {iv.mean()*100:.1f}%  | 范围 "
            f"{iv.min()*100:.1f}% ~ {iv.max()*100:.1f}%"
        )
    print()


def cmd_probe(client, symbol: str) -> None:
    _log(f"探测 {symbol}（最近 5 个交易日）...")
    end = date.today() - timedelta(days=1)
    start = end - timedelta(days=7)
    try:
        df = client.option_history_eod(
            symbol=symbol,
            start_date=start,
            end_date=end,
            expiration="*",
            strike_range=15,
            max_dte=90,
        )
        print("\n=== PROBE 结果 ===")
        print(f"行数: {0 if df is None else len(df)}")
        if df is not None and not df.empty:
            df = _norm_cols(df)
            print(f"列: {list(df.columns)}")
            if "date" in df.columns:
                print(f"日期范围: {df['date'].min()} ~ {df['date'].max()}")
            print(df.head(5).to_string())
        print("=== PROBE 结束 ===")
    except Exception as e:  # noqa: BLE001
        print(f"\n[探测失败] {e}\n请把这段报错发回，脚本会相应调整。")
        raise SystemExit(1)


def main() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:  # noqa: BLE001
        pass
    p = argparse.ArgumentParser(description="OPTION-ALERT 历史数据回填")
    p.add_argument("--probe", metavar="TICKER", help="连通性与字段自检")
    p.add_argument("--download", action="store_true", help="下载期权 EOD + 股票 EOD")
    p.add_argument("--prices", action="store_true", help="yfinance 全历史日线")
    p.add_argument("--convert", action="store_true", help="生成 data/iv_history")
    p.add_argument("--report", action="store_true", help="打印覆盖报告")
    p.add_argument("--all", action="store_true", help="download + prices + convert")
    p.add_argument("--greeks", action="store_true", help="最佳努力拉 EOD Greeks")
    p.add_argument("--tickers", nargs="*", help="覆盖标的清单（默认读 config/tickers.txt）")
    p.add_argument("--start", default=DEFAULT_START.isoformat(), help="起始日 YYYY-MM-DD")
    p.add_argument(
        "--end",
        default=(date.today() - timedelta(days=1)).isoformat(),
        help="结束日 YYYY-MM-DD",
    )
    p.add_argument(
        "--strike-range", type=int, default=None, help="现货上下各取几个行权价（默认全量）"
    )
    p.add_argument("--max-dte", type=int, default=None, help="只取 DTE<=n 的合约（默认全量）")
    p.add_argument("--rate", type=int, default=20, help="每分钟请求数上限（默认 20，上限 30）")
    p.add_argument("--force", action="store_true", help="转换时覆盖已有 iv_history")
    args = p.parse_args()

    start = date.fromisoformat(args.start)
    end = date.fromisoformat(args.end)
    tickers = _tickers(args.tickers)
    _log(f"标的({len(tickers)}): {', '.join(tickers)}")
    _log(f"窗口: {start} ~ {end}")

    if args.probe:
        cmd_probe(_make_client(), args.probe.upper())
        return
    if args.report:
        cmd_report(tickers)
        return
    if not (args.download or args.prices or args.convert or args.all):
        p.print_help()
        return
    if args.all:
        args.download = args.prices = args.convert = True
    if args.download:
        _acquire_lock()
        try:
            cmd_download(
                _make_client(),
                tickers,
                start,
                end,
                args.strike_range,
                args.max_dte,
                args.rate,
                args.greeks,
            )
        finally:
            _release_lock()
    if args.prices:
        cmd_prices(tickers)
    if args.convert:
        cmd_convert(tickers, start, end, args.force)
    if args.download or args.prices or args.convert:
        cmd_report(tickers)


if __name__ == "__main__":
    main()
