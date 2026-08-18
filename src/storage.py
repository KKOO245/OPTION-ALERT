# -*- coding: utf-8 -*-
"""
存储层（v3）
------------
1. data/history/{ticker}.csv   最近一次全量快照（覆盖式），用于 OI 日环比检测
2. data/analytics/{ticker}.csv 每日紧凑指标（追加式、长期保留），
   用于 IV Rank / IV 历史对比等；一年 6-8 个标的也只有几 MB
"""

import datetime
import json
import os

import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HISTORY_DIR = os.path.join(BASE_DIR, "data", "history")
ANALYTICS_DIR = os.path.join(BASE_DIR, "data", "analytics")

ANALYTICS_COLUMNS = [
    "date", "session", "source", "price",
    "pcr_vol_near", "pcr_oi_near", "pcr_vol_all", "pcr_oi_all",
    "max_pain_near", "max_pain_monthly",
    "atm_iv_near", "atm_iv_monthly", "term_ratio", "iv_skew_25",
    "expected_move_pct", "net_delta_oi", "net_gamma_oi",
    "oi_concentration", "top_unusual", "top_surge",
]


def _today():
    return datetime.date.today().isoformat()


# ---------- 最近快照（OI 日环比） ----------
def load_prev_snapshot(ticker):
    path = os.path.join(HISTORY_DIR, f"{ticker}.csv")
    if not os.path.exists(path):
        return None
    try:
        return pd.read_csv(path)
    except Exception as e:
        print(f"[警告] 读取 {ticker} 历史快照失败: {e}")
        return None


def save_snapshot(ticker, contracts):
    os.makedirs(HISTORY_DIR, exist_ok=True)
    path = os.path.join(HISTORY_DIR, f"{ticker}.csv")
    rows = [{
        "contractSymbol": c["contract_symbol"],
        "openInterest": c.get("open_interest") or 0,
        "volume": c.get("volume") or 0,
        "snapshot_date": _today(),
    } for c in contracts]
    pd.DataFrame(rows).to_csv(path, index=False)


# ---------- 每日紧凑指标（长期积累） ----------
def append_analytics(ticker, session, source, metrics):
    os.makedirs(ANALYTICS_DIR, exist_ok=True)
    path = os.path.join(ANALYTICS_DIR, f"{ticker}.csv")
    # 同一天同一个时段只追加一次，防止重试/重复测试产生重复行
    if os.path.exists(path) and os.path.getsize(path) > 0:
        try:
            existing = pd.read_csv(path)
            if ((existing["date"] == _today()) & (existing["session"] == session)).any():
                print(f"[跳过] {ticker} {_today()} {session} 指标已存在，不重复追加。")
                return
        except Exception:
            pass
    row = {k: metrics.get(k) for k in ANALYTICS_COLUMNS}
    row["date"] = _today()
    row["session"] = session
    row["source"] = source
    for k in ("oi_concentration", "top_unusual", "top_surge"):
        v = row.get(k)
        if isinstance(v, (list, dict)):
            row[k] = json.dumps(v, ensure_ascii=False)
    df = pd.DataFrame([row])[ANALYTICS_COLUMNS]
    if os.path.exists(path) and os.path.getsize(path) > 0:
        df.to_csv(path, mode="a", header=False, index=False)
    else:
        df.to_csv(path, index=False)


def load_analytics(ticker):
    path = os.path.join(ANALYTICS_DIR, f"{ticker}.csv")
    if not os.path.exists(path):
        return pd.DataFrame()
    try:
        return pd.read_csv(path)
    except Exception:
        return pd.DataFrame()


def load_iv_history(ticker, min_obs=20):
    """每个交易日取最后一次的 ATM IV 序列，用于 IV Rank"""
    df = load_analytics(ticker)
    if df.empty or "atm_iv_near" not in df.columns:
        return []
    df = df.dropna(subset=["atm_iv_near"])
    df = df.sort_values(["date", "session"])
    daily = df.groupby("date").last()["atm_iv_near"].tolist()
    return daily if len(daily) >= min_obs else []


def load_session_value(ticker, session, field, date=None):
    """取某一天某个时段的某个指标值（如今天早报的 ATM IV）"""
    df = load_analytics(ticker)
    if df.empty or field not in df.columns:
        return None
    d = date or _today()
    rows = df[(df["date"] == d) & (df["session"] == session)]
    if rows.empty:
        return None
    val = rows.iloc[-1][field]
    try:
        return float(val)
    except (TypeError, ValueError):
        return None
