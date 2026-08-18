# -*- coding: utf-8 -*-
"""
指标层（v3）
------------
把原始期权链变成专业指标：
P/C 比率、Max Pain、ATM IV、IV Rank、期限结构、25Δ 偏度、
预期波动、OI 集中带、Greeks 敞口、异动评分、OI 增仓。
"""

import math

import pandas as pd


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
    import datetime

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


def unusual_activity(df, min_volume=500, vol_oi_min=1.0, top_n=5):
    """
    异动评分：vol/OI 比（新建仓强度）x 名义成交额（volume×mid）。
    只认有实质成交额的合约，避免一堆 1 美元的深度虚值单刷榜。
    """
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
        rows.append({
            "contract_symbol": c.contract_symbol,
            "expiration": c.expiration,
            "dte": int(c.dte),
            "type": c.type,
            "strike": float(c.strike),
            "volume": int(vol),
            "open_interest": int(oi),
            "vol_oi_ratio": round(ratio, 2) if ratio else None,
            "premium": round(premium, 0),
            "iv": (round(float(c.iv), 4)
                   if c.iv is not None and not math.isnan(c.iv) and c.iv > 0 else None),
            "delta": round(float(c.delta), 3) if c.delta is not None and not math.isnan(c.delta) else None,
            "score": round(score, 1),
        })
    rows.sort(key=lambda r: -r["score"])
    return rows[:top_n]


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
    """当前 ATM IV 在近 250 个交易日序列中的百分位；历史不足 20 个观察值时返回 None"""
    if atm_iv is None or len(history) < 20:
        return None
    below = sum(1 for x in history if x <= atm_iv)
    return below / len(history) * 100.0


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
    unusual = unusual_activity(df, min_volume=min_volume, vol_oi_min=vol_oi_min, top_n=top_n)
    surge_df = oi_surge(df, prev, window_days=anomaly_window, top_n=top_n)
    surge = surge_rows(surge_df)

    return {
        "ticker": df.iloc[0].get("ticker") if "ticker" in df.columns else None,
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
    }
