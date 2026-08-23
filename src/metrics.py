# -*- coding: utf-8 -*-
"""
指标层（v3）
------------
把原始期权链变成专业指标：
P/C 比率、Max Pain、ATM IV、IV Rank、期限结构、25Δ 偏度、
预期波动、OI 集中带、Greeks 敞口、异动评分、OI 增仓。
"""

import datetime
import math

import numpy as np
import pandas as pd
from scipy.stats import norm

from data_fetcher import RISK_FREE_RATE


def _frame(contracts):
    df = pd.DataFrame(contracts)
    for c in ("volume", "open_interest"):
        if c not in df.columns:
            df[c] = 0
        df[c] = df[c].fillna(0)
    return df


def _ratios(subset):
    if subset.empty:
        return None, None
    cv = subset.loc[subset["type"] == "call", "volume"].sum()
    pv = subset.loc[subset["type"] == "put", "volume"].sum()
    coi = subset.loc[subset["type"] == "call", "open_interest"].sum()
    poi = subset.loc[subset["type"] == "put", "open_interest"].sum()
    return (pv / cv if cv else None), (poi / coi if coi else None)


def _days(exp_str):
    exp = datetime.datetime.strptime(exp_str, "%Y-%m-%d").date()
    return (exp - datetime.date.today()).days


def _pick_far_expiry(exps, near_exp):
    """除最近到期日外，挑一个 dte 最接近 30 天的到期日（月度窗口）"""
    cands = [e for e in exps if e != near_exp]
    if not cands:
        return None
    best = min(cands, key=lambda e: abs(_days(e) - 30))
    return best if 10 <= _days(best) <= 60 else None


def _atm_strike(df, spot):
    if spot is None or df.empty:
        return None
    scope = df[df["dte"] >= 1] if (df["dte"] >= 1).any() else df
    return min(scope["strike"].unique(), key=lambda k: abs(k - spot))


def _atm_iv_for(df_subset, spot):
    k = _atm_strike(df_subset, spot)
    if k is None:
        return None
    ivs = df_subset[df_subset["strike"] == k]["iv"].dropna()
    ivs = ivs[(ivs > 0) & (ivs < 3)]
    return float(ivs.mean()) if len(ivs) else None


def atm_metrics(df, spot):
    """返回 (atm_iv, expected_move_pct, atm_strike)"""
    k = _atm_strike(df, spot)
    if k is None:
        return None, None, None
    sub = df[df["strike"] == k]
    ivs = sub["iv"].dropna()
    ivs = ivs[(ivs > 0) & (ivs < 3)]
    atm_iv = float(ivs.mean()) if len(ivs) else None
    expected = None
    call = sub[sub["type"] == "call"]
    put = sub[sub["type"] == "put"]
    if not call.empty and not put.empty and spot:
        cm, pm = call.iloc[0].get("mid"), put.iloc[0].get("mid")
        if cm is not None and pm is not None:
            expected = (cm + pm) / spot * 100.0
    return atm_iv, expected, k


def max_pain(df, expirations):
    """让期权卖方总赔付最小的行权价（到期结算视角）"""
    out = {}
    for exp in expirations:
        sub = df[(df["expiration"] == exp) & (df["open_interest"] > 0)]
        if sub.empty:
            out[exp] = None
            continue
        strikes = sorted(sub["strike"].unique())
        best_k, best_cost = None, None
        for s in strikes:  # s 为假设的结算价
            calls = sub[(sub["type"] == "call") & (sub["strike"] <= s)]
            puts = sub[(sub["type"] == "put") & (sub["strike"] >= s)]
            cost = ((s - calls["strike"]) * calls["open_interest"]).sum()
            cost += ((puts["strike"] - s) * puts["open_interest"]).sum()
            if best_cost is None or cost < best_cost:
                best_cost, best_k = cost, s
        out[exp] = best_k
    return out


def iv_skew_25(df):
    """25Δ 看跌 IV − 25Δ 看涨 IV（百分点）；负值=市场更怕大跌"""
    calls = df[(df["type"] == "call") & (df["delta"].notna())
               & (df["delta"] >= 0.20) & (df["delta"] <= 0.35)]
    puts = df[(df["type"] == "put") & (df["delta"].notna())
              & (df["delta"] <= -0.20) & (df["delta"] >= -0.35)]
    call_ivs = calls["iv"].dropna()
    call_ivs = call_ivs[(call_ivs > 0) & (call_ivs < 3)]
    put_ivs = puts["iv"].dropna()
    put_ivs = put_ivs[(put_ivs > 0) & (put_ivs < 3)]
    if call_ivs.empty or put_ivs.empty:
        return None
    return (float(put_ivs.mean()) - float(call_ivs.mean())) * 100.0


def oi_concentration(df, spot, band=0.05, top_n=3):
    """±5% 行权价内的 OI 堆叠（支撑/压力参考）"""
    if spot is None or df.empty:
        return []
    lo, hi = spot * (1 - band), spot * (1 + band)
    scope = df[(df["strike"] >= lo) & (df["strike"] <= hi) & (df["open_interest"] > 0)]
    if scope.empty:
        return []
    grouped = (scope.groupby(["strike", "type"])["open_interest"]
               .sum().reset_index()
               .sort_values("open_interest", ascending=False)
               .head(top_n))
    return [{"strike": float(r.strike), "type": r.type, "oi": int(r.open_interest)}
            for r in grouped.itertuples(index=False)]


def greeks_exposure(df, max_dte=None):
    """按未平仓量加权的净 delta / gamma 敞口（单位：股）"""
    scope = df if max_dte is None else df[df["dte"] <= max_dte]
    net_delta = net_gamma = 0.0
    for c in scope.itertuples(index=False):
        if c.open_interest:
            if c.delta is not None:
                net_delta += c.delta * c.open_interest * 100
            if c.gamma is not None:
                net_gamma += c.gamma * c.open_interest * 100
    return net_delta, net_gamma


def _prev_lookup(prev):
    """把上次快照转成 contract_symbol -> (oi_prev, volume_prev) 的查询表"""
    if prev is None or prev.empty:
        return {}
    out = {}
    for r in prev.itertuples(index=False):
        oi = getattr(r, "openInterest", None) or 0
        vol = getattr(r, "volume", None) or 0
        out[r.contractSymbol] = (oi, vol)
    return out


def flow_classify(vol, oi_change, has_prev):
    """按成交量 × OI 变化把合约资金流分为：开仓 / 平仓 / 换手 / 新（无历史）"""
    if not has_prev:
        return "新"
    if vol <= 0:
        return "—"
    if oi_change is None:
        return "—"
    if oi_change > 0:
        return "开仓"
    if oi_change < 0:
        return "平仓"
    return "换手"


def unusual_activity(df, min_volume=500, vol_oi_min=1.0, top_n=5, prev_lookup=None):
    """
    异动评分：vol/OI 比（新建仓强度）x 名义成交额（volume×mid）。
    只认有实质成交额的合约，避免一堆 1 美元的深度虚值单刷榜。
    同时附上"异动前后对比"：昨量/今量、OI 前值/现值，方便判断幅度。
    """
    prev_lookup = prev_lookup or {}
    cand = df[(df["volume"] >= min_volume)]
    rows = []
    for c in cand.itertuples(index=False):
        vol, oi = c.volume, c.open_interest
        if oi > 0:
            ratio = vol / oi
            if ratio < vol_oi_min:
                continue
        else:
            ratio = None
        premium = c.premium or 0
        if premium <= 0:
            continue
        strength = min(ratio, 20.0) if ratio else 5.0
        score = strength * math.log1p(premium)
        oi_prev, vol_prev = prev_lookup.get(c.contract_symbol, (None, None))
        has_prev = c.contract_symbol in prev_lookup
        vol_prev = vol_prev or 0
        oi_prev = oi_prev if oi_prev is not None else 0
        vol_ratio = round(vol / vol_prev, 1) if vol_prev else None
        oi_change = oi - oi_prev
        oi_change_pct = round(oi_change / oi_prev * 100, 1) if oi_prev else None
        rows.append({
            "contract_symbol": c.contract_symbol,
            "expiration": c.expiration,
            "dte": int(c.dte),
            "type": c.type,
            "strike": float(c.strike),
            "volume": int(vol),
            "open_interest": int(oi),
            "volume_prev": int(vol_prev),
            "volume_ratio": vol_ratio,
            "oi_prev": int(oi_prev),
            "oi_change": int(oi_change),
            "oi_change_pct": oi_change_pct,
            "flow": flow_classify(vol, oi_change, has_prev),
            "vol_oi_ratio": round(ratio, 2) if ratio else None,
            "premium": round(premium, 0),
            "iv": (round(float(c.iv), 4)
                   if c.iv is not None and not math.isnan(c.iv) and c.iv > 0 else None),
            "delta": round(float(c.delta), 3) if c.delta is not None and not math.isnan(c.delta) else None,
            "score": round(score, 1),
        })
    rows.sort(key=lambda r: -r["score"])
    return rows[:top_n]


def top_oi_rows(df, exp_dates, top_n=5):
    """指定到期日集合里，按未平仓量排序的看涨/看跌 Top N"""
    sub = df[df["expiration"].isin(exp_dates)]
    calls = sub[sub["type"] == "call"].sort_values("open_interest", ascending=False).head(top_n)
    puts = sub[sub["type"] == "put"].sort_values("open_interest", ascending=False).head(top_n)

    def to_rows(frame):
        return [{
            "type": "Call" if r.type == "call" else "Put",
            "expiration": r.expiration,
            "strike": float(r.strike),
            "last": float(r.last) if r.last is not None else None,
            "iv": round(float(r.iv), 4) if r.iv is not None and not math.isnan(r.iv) else None,
            "open_interest": int(r.open_interest),
        } for r in frame.itertuples(index=False)]

    return to_rows(calls), to_rows(puts)


def oi_surge(df, prev, window_days=35, top_n=5):
    """一个月窗口内，今天 vs 上次快照的未平仓量增幅 Top N（疑似新开仓）"""
    if prev is None or prev.empty:
        return None
    if "contractSymbol" not in prev.columns or "openInterest" not in prev.columns:
        return None
    scope = df[df["dte"] <= window_days]
    merged = scope.merge(
        prev[["contractSymbol", "openInterest"]],
        left_on="contract_symbol", right_on="contractSymbol",
        how="left", suffixes=("", "_prev"),
    )
    # 左右两侧列名不同（open_interest vs openInterest）时不会自动加后缀，统一归一化
    prev_col = "openInterest_prev" if "openInterest_prev" in merged.columns else "openInterest"
    merged["openInterest_prev"] = merged[prev_col].fillna(0)
    merged["oi_change"] = merged["open_interest"] - merged["openInterest_prev"]
    surge = merged[merged["oi_change"] > 0].sort_values("oi_change", ascending=False).head(top_n)
    return surge


def surge_rows(surge_df):
    if surge_df is None or surge_df.empty:
        return []
    rows = []
    for r in surge_df.itertuples(index=False):
        rows.append({
            "contract_symbol": r.contractSymbol,
            "expiration": r.expiration,
            "type": r.type,
            "strike": float(r.strike),
            "oi": int(r.open_interest),
            "oi_prev": int(r.openInterest_prev),
            "oi_change": int(r.oi_change),
        })
    return rows[:5]


def iv_rank(atm_iv, history):
    """当前 ATM IV 在历史序列中的百分位；历史不足 20 个观察值时返回 None"""
    if atm_iv is None or len(history) < 20:
        return None
    below = sum(1 for x in history if x <= atm_iv)
    return below / len(history) * 100.0


# ---------- 做市商定位：GEX / Gamma Flip / Walls / Vanna / Charm ----------
def _bs_d1d2(spot, strike, t, sigma):
    """Black-Scholes d1/d2（向量化）"""
    spot = float(spot)
    strike = np.asarray(strike, dtype=float)
    sigma = np.asarray(sigma, dtype=float)
    sq = sigma * np.sqrt(t)
    d1 = (np.log(spot / strike) + (RISK_FREE_RATE + sigma ** 2 / 2.0) * t) / sq
    return d1, d1 - sq


def vanna_charm(spot, strike, t, sigma):
    """Vanna（∂Δ/∂IV）与 Charm（∂Δ/∂τ）的 Black-Scholes 解析值，向量化；q=0"""
    strike = np.asarray(strike, dtype=float)
    t = np.asarray(t, dtype=float)
    sigma = np.asarray(sigma, dtype=float)
    d1, d2 = _bs_d1d2(spot, strike, t, sigma)
    phi = norm.pdf(d1)
    # Vanna = ∂Δ/∂σ = -φ(d1)·d2/σ（q=0 时 Δ=N(d1)，无折现因子）
    vanna = -phi * d2 / sigma
    # Charm = ∂Δ/∂τ = φ(d1)·[(r+σ²/2)/(2σ√τ) - ln(S/K)/(2σ·τ^1.5)]
    charm = phi * ((RISK_FREE_RATE + sigma ** 2 / 2.0) / (2.0 * sigma * np.sqrt(t))
                   - np.log(spot / strike) / (2.0 * sigma * t ** 1.5))
    return vanna, charm


def _find_flip(strikes, cum):
    """累计 GEX 由负转正（或正转负）的零交叉点，线性插值"""
    for i in range(len(cum) - 1):
        if cum[i] * cum[i + 1] < 0:
            frac = -cum[i] / (cum[i + 1] - cum[i])
            return float(strikes[i] + (strikes[i + 1] - strikes[i]) * frac)
    return None


def gamma_structure(df, spot, top_n=3):
    """
    按行权价聚合 Gamma 暴露（散户多头口径：Call 正、Put 负，×100×spot）。
    返回 Call/Put Wall、Gamma Flip（零交叉）、Top Gamma 行权价、Net GEX、
    Net Vanna / Net Charm、成交量集中行权价。
    """
    if df is None or df.empty or spot is None:
        return None
    g = df[(df["gamma"].notna()) & (df["open_interest"] > 0)].copy()
    if g.empty:
        return None
    g["dte"] = g["dte"].clip(lower=1)
    t = g["dte"] / 365.0
    sign = np.where(g["type"] == "call", 1.0, -1.0)
    g["gex"] = g["gamma"].values * g["open_interest"].values * 100.0 * spot * sign
    g["vanna"], g["charm"] = vanna_charm(
        spot, g["strike"].values, t.values, g["iv"].fillna(0.25).clip(lower=0.05).values
    )
    g["vanna_expo"] = g["vanna"] * g["open_interest"].values * 100.0 * sign
    g["charm_expo"] = g["charm"] * g["open_interest"].values * 100.0 * sign

    by_strike = g.groupby("strike")["gex"].sum().sort_index()
    cum = by_strike.cumsum()
    net_gex = float(cum.iloc[-1]) if len(cum) else None
    flip = _find_flip(by_strike.index.values, cum.values)

    call_oi = g[g["type"] == "call"].groupby("strike")["open_interest"].sum()
    put_oi = g[g["type"] == "put"].groupby("strike")["open_interest"].sum()
    call_wall = float(call_oi.idxmax()) if not call_oi.empty else None
    put_wall = float(put_oi.idxmax()) if not put_oi.empty else None

    top_gamma = []
    for k, v in by_strike.abs().sort_values(ascending=False).head(top_n).items():
        top_gamma.append({"strike": float(k), "gex": round(float(by_strike.loc[k]), 0)})

    call_vol = g[g["type"] == "call"].groupby("strike")["volume"].sum()
    put_vol = g[g["type"] == "put"].groupby("strike")["volume"].sum()

    return {
        "net_gex": round(net_gex, 0) if net_gex is not None else None,
        "gamma_flip": round(flip, 2) if flip is not None else None,
        "call_wall": call_wall,
        "put_wall": put_wall,
        "top_gamma": top_gamma,
        "net_vanna": round(float(g["vanna_expo"].sum()), 0),
        "net_charm": round(float(g["charm_expo"].sum()), 0),
        "call_vol_top": float(call_vol.idxmax()) if not call_vol.empty else None,
        "put_vol_top": float(put_vol.idxmax()) if not put_vol.empty else None,
    }


def _new_position_exposure(df, prev_lookup, spot):
    """今日（较上次快照）新增仓位对 Delta / GEX 的贡献。
    口径与主结构一致：Call 正、Put 负；OI 为前日结算口径，反映的是近两日资金流。"""
    if prev_lookup is None:
        prev_lookup = {}
    new_delta = 0.0
    new_gex = 0.0
    for c in df.itertuples(index=False):
        oi_prev, _ = prev_lookup.get(c.contract_symbol, (None, None))
        if oi_prev is None:
            change = c.open_interest or 0
        else:
            change = c.open_interest - oi_prev
        if change <= 0 or not c.open_interest:
            continue
        sign = 1.0 if c.type == "call" else -1.0
        if c.delta is not None:
            new_delta += c.delta * change * 100
        if c.gamma is not None:
            new_gex += c.gamma * change * 100 * spot * sign
    return round(new_gex, 0), round(new_delta, 0)


def compute_metrics(contracts, spot, prev=None,
                    fetch_window=40, anomaly_window=35,
                    min_volume=500, vol_oi_min=1.0, top_n=5):
    """主入口：输入合约列表 + 现价，输出全部指标 dict"""
    df = _frame(contracts)
    if df.empty:
        return {}
    df = df[df["dte"].between(0, fetch_window)]
    exps = sorted(df["expiration"].unique())
    near_exp = exps[0] if exps else None
    far_exp = _pick_far_expiry(exps, near_exp) if near_exp else None
    window_exps = exps[1:5]  # 未来 4 个期权日（紧邻最近到期日之后）

    near = df[df["expiration"] == near_exp] if near_exp else df.iloc[0:0]
    pcr_vol_near, pcr_oi_near = _ratios(near)
    pcr_vol_all, pcr_oi_all = _ratios(df)

    pains = max_pain(df, [e for e in (near_exp, far_exp) if e])
    # 预期波动/ATM IV 用最近到期日那一层，避免全链混算
    atm_iv, expected_move_pct, atm_k = atm_metrics(
        df[df["expiration"] == near_exp] if near_exp else df, spot
    )
    atm_iv_far = _atm_iv_for(df[df["expiration"] == far_exp], spot) if far_exp else None
    term_ratio = (atm_iv_far / atm_iv) if (atm_iv and atm_iv_far) else None
    skew = iv_skew_25(df[df["dte"] <= anomaly_window])
    conc = oi_concentration(df, spot)
    net_delta, net_gamma = greeks_exposure(df)
    net_delta_near, net_gamma_near = greeks_exposure(df, max_dte=10)
    unusual = unusual_activity(df, min_volume=min_volume, vol_oi_min=vol_oi_min,
                               top_n=top_n, prev_lookup=_prev_lookup(prev))
    nearest_calls, nearest_puts = top_oi_rows(df, [near_exp]) if near_exp else ([], [])
    window_calls, window_puts = top_oi_rows(df, window_exps)
    surge_df = oi_surge(df, prev, window_days=anomaly_window, top_n=top_n)
    surge = surge_rows(surge_df)
    structure = gamma_structure(df, spot)
    structure_near = gamma_structure(df[df["dte"] <= 7], spot)
    structure_monthly = (gamma_structure(df[df["expiration"] == far_exp], spot)
                         if far_exp else None)
    new_gex, new_delta = _new_position_exposure(df, _prev_lookup(prev), spot)

    return {
        "near_exp": near_exp,
        "far_exp": far_exp,
        "pcr_vol_near": pcr_vol_near,
        "pcr_oi_near": pcr_oi_near,
        "pcr_vol_all": pcr_vol_all,
        "pcr_oi_all": pcr_oi_all,
        "max_pain_near": pains.get(near_exp) if near_exp else None,
        "max_pain_monthly": pains.get(far_exp) if far_exp else None,
        "atm_iv_near": atm_iv,
        "atm_iv_monthly": atm_iv_far,
        "term_ratio": term_ratio,
        "iv_skew_25": skew,
        "expected_move_pct": expected_move_pct,
        "net_delta_oi": net_delta,
        "net_gamma_oi": net_gamma,
        "net_delta_near": net_delta_near,
        "net_gamma_near": net_gamma_near,
        "oi_concentration": conc,
        "top_unusual": unusual,
        "top_surge": surge,
        "has_surge_data": surge_df is not None,
        "n_contracts": int(len(df)),
        "nearest_top_calls": nearest_calls,
        "nearest_top_puts": nearest_puts,
        "window_top_calls": window_calls,
        "window_top_puts": window_puts,
        "window_label": (f"{window_exps[0]} 至 {window_exps[-1]}"
                         if len(window_exps) > 1 else (window_exps[0] if window_exps else None)),
        "structure": structure,
        "structure_near": structure_near,
        "structure_monthly": structure_monthly,
        "new_gex": new_gex,
        "new_delta": new_delta,
    }
