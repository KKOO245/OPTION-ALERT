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
IV_HIST_DIR = os.path.join(BASE_DIR, "data", "iv_history")
CLOSES_DIR = os.path.join(BASE_DIR, "data", "closes")

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
    """每个交易日取最后一次的 ATM IV 序列，用于 IV Rank。
    已接线：data/iv_history（历史回填，ThetaData EOD 口径）优先，
    data/analytics（每日指标，CBOE 实时口径）补充回填截止日之后的新日期。"""
    _dates, ivs = load_iv_series(ticker)
    return ivs if len(ivs) >= min_obs else []


def load_iv_series(ticker):
    """合并后的每日 ATM IV 序列：
    1) data/iv_history/{ticker}.csv —— ThetaData EOD 历史回填（2023-06 起），同日期优先
    2) data/analytics/{ticker}.csv —— 每日指标，补回填截止日之后的新日期
    返回 (dates, ivs) 两个按日期升序的列表；同一日期只保留一个值。
    """
    daily: dict = {}
    p = os.path.join(IV_HIST_DIR, f"{ticker}.csv")
    if os.path.exists(p) and os.path.getsize(p) > 0:
        try:
            df = pd.read_csv(p)
            if "date" in df.columns and "atm_iv_near" in df.columns:
                sub = df.dropna(subset=["atm_iv_near"])
                for _, r in sub.iterrows():
                    try:
                        daily[str(r["date"])] = float(r["atm_iv_near"])
                    except (TypeError, ValueError):
                        continue
        except Exception as e:
            print(f"[警告] 读取 {ticker} iv_history 失败: {e}")
    a = load_analytics(ticker)
    if not a.empty and "atm_iv_near" in a.columns:
        a = a.dropna(subset=["atm_iv_near"])
        if "date" in a.columns and "session" in a.columns:
            a = a.sort_values(["date", "session"])
            for d, grp in a.groupby("date"):
                ds = str(d)
                if ds not in daily:  # iv_history 优先，同源长历史
                    try:
                        wd = pd.to_datetime(ds).weekday()
                    except Exception:
                        wd = 0  # 解析失败不拦截（保守保留）
                    if wd >= 5:
                        continue  # 周末行（手工/测试跑出来的）不进 IV 历史
                    try:
                        daily[ds] = float(grp["atm_iv_near"].iloc[-1])
                    except (TypeError, ValueError):
                        continue
    items = sorted(daily.items())
    dates = [d for d, _ in items]
    ivs = [v for _, v in items]
    return dates, ivs


def load_rv_series(ticker, lookback=20):
    """从 data/closes 全历史计算每日已实现波动率（对数收益滚动 std × √252）。
    返回 {date: rv}；窗口内收益不足 lookback 的天数不返回（不猜测）。
    """
    import math

    path = os.path.join(CLOSES_DIR, f"{ticker}.csv")
    if not os.path.exists(path):
        return {}
    try:
        df = pd.read_csv(path)
    except Exception:
        return {}
    if not {"date", "close"}.issubset(df.columns):
        return {}
    df = df.dropna(subset=["close"]).sort_values("date")
    df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")
    # 对数收益（与回放引擎/学术口径一致）；简单收益在日频上差异为二阶小量，但口径统一更严谨
    close = pd.Series(df["close"], dtype=float)
    ret = (close / close.shift(1)).apply(math.log)
    rv = ret.rolling(lookback).std() * math.sqrt(252)
    out = {}
    for d, v in zip(df["date"], rv):
        if v is not None and v == v and v > 0:
            out[str(d)] = float(v)
    return out


def load_rv_iv_aligned(ticker, lookback=20):
    """合并 IV 历史与 RV 历史（按日期对齐），返回 (dates, ivs, rvs)。
    pricing_proxy 的 iv_series/rv_series 必须逐日对应，故只取两者都有的日期。
    """
    dates, ivs = load_iv_series(ticker)
    rv_map = load_rv_series(ticker, lookback)
    out_d, out_i, out_r = [], [], []
    for d, iv in zip(dates, ivs):
        rv = rv_map.get(d)
        if rv is not None:
            out_d.append(d)
            out_i.append(iv)
            out_r.append(rv)
    return out_d, out_i, out_r


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
