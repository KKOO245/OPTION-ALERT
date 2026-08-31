# -*- coding: utf-8 -*-
import sys
import os

import pandas as pd
from vollib.black_scholes.greeks import analytical as vollib_greeks

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import metrics as m


def _contracts():
    """构造一个简单的合成链：spot=100，近月 5 个行权价，看涨看跌各 5 份"""
    cs = []
    for k in (90, 95, 100, 105, 110):
        for typ, flag in (("call", 1), ("put", -1)):
            delta = flag * 0.5
            cs.append({
                "contract_symbol": f"T{typ}{k}",
                "expiration": "2026-08-28",
                "dte": 10,
                "type": typ,
                "strike": k,
                "last": 3.0, "bid": 2.9, "ask": 3.1, "mid": 3.0,
                "volume": 200 if typ == "call" else 100,
                "open_interest": 1000 if typ == "call" else 500,
                "iv": 0.30, "delta": delta, "gamma": 0.05,
                "theta": -0.02, "vega": 0.1, "rho": 0.01,
                "premium": 3.0 * 200, "vol_oi_ratio": 0.2,
                "moneyness": None,
            })
    # 一张 OI 堆在 95 行权价的看跌（用来验证 Max Pain）
    cs.append({
        "contract_symbol": "Tput95b",
        "expiration": "2026-08-28", "dte": 10, "type": "put", "strike": 95,
        "last": 1.0, "bid": 0.9, "ask": 1.1, "mid": 1.0,
        "volume": 0, "open_interest": 5000, "iv": 0.30, "delta": -0.5,
        "gamma": 0.05, "theta": -0.02, "vega": 0.1, "rho": 0.01,
        "premium": 0.0, "vol_oi_ratio": 0.0, "moneyness": None,
    })
    return cs


def test_ratios():
    cs = _contracts()
    df = m._frame(cs)
    pv, oi = m._ratios(df)
    assert abs(pv - 100 / 200) < 1e-9
    # 看涨 OI 1000×5 = 5000；看跌 OI 500×5 + 额外 5000 = 7500
    assert abs(oi - 7500 / 5000) < 1e-9


def test_max_pain_shifts_to_heavy_put_strike():
    cs = _contracts()
    df = m._frame(cs)
    out = m.max_pain(df, ["2026-08-28"])
    # 大量 OI 堆在 95 的看跌，最大痛点应落在 95
    assert out["2026-08-28"] == 95


def test_atm_metrics():
    cs = _contracts()
    df = m._frame(cs)
    iv, expected, k = m.atm_metrics(df, 100)
    assert k == 100
    assert iv is not None and abs(iv - 0.30) < 1e-6
    assert expected is not None and abs(expected - 6.0) < 1e-6  # 跨式 = 3+3


def test_skew_25():
    cs = _contracts()
    df = m._frame(cs)
    # 让看跌 delta 落在 -0.25，IV 0.35；看涨 delta 0.25，IV 0.25
    df.loc[df["type"] == "put", "delta"] = -0.25
    df.loc[df["type"] == "put", "iv"] = 0.35
    df.loc[df["type"] == "call", "delta"] = 0.25
    df.loc[df["type"] == "call", "iv"] = 0.25
    skew = m.iv_skew_25(df)
    assert skew is not None and abs(skew - 10.0) < 1e-6


def test_skew_25_interpolation():
    """skew_v2：|Δ|=0.25 线性插值（不再宽带平均）。"""
    import pandas as pd

    df = pd.DataFrame(
        [
            {"strike": 90.0, "type": "call", "delta": 0.20, "iv": 0.30, "dte": 10, "expiration": "2026-09-11"},
            {"strike": 95.0, "type": "call", "delta": 0.30, "iv": 0.50, "dte": 10, "expiration": "2026-09-11"},
            {"strike": 105.0, "type": "put", "delta": -0.30, "iv": 0.60, "dte": 10, "expiration": "2026-09-11"},
            {"strike": 110.0, "type": "put", "delta": -0.20, "iv": 0.40, "dte": 10, "expiration": "2026-09-11"},
        ]
    )
    skew = m.iv_skew_25(df)
    # call 25Δ = 0.30+(0.50-0.30)*(0.05/0.10) = 0.40；put 25Δ = 0.40+(0.60-0.40)*(0.05/0.10) = 0.50
    assert skew is not None and abs(skew - 10.0) < 1e-6


def test_unusual_activity_filters():
    cs = _contracts()
    df = m._frame(cs)
    # 提高成交量阈值，全部被过滤
    assert m.unusual_activity(df, min_volume=100000) == []
    rows = m.unusual_activity(df, min_volume=100, vol_oi_min=0.1)
    assert len(rows) > 0


def test_unusual_prev_lookup():
    cs = _contracts()
    df = m._frame(cs)
    prev = {"Tcall100": (500, 80)}  # 之前 OI 500、量 80
    rows = m.unusual_activity(df, min_volume=100, vol_oi_min=0.1, prev_lookup=prev)
    row = next(r for r in rows if r["contract_symbol"] == "Tcall100")
    assert row["oi_prev"] == 500
    assert row["volume_prev"] == 80
    assert row["oi_change"] == 500          # 今日 OI 1000 - 500
    assert row["oi_change_pct"] == 100.0    # +100%
    assert row["volume_ratio"] == 2.5       # 200 / 80


def test_top_oi_rows():
    cs = _contracts()
    df = m._frame(cs)
    calls, puts = m.top_oi_rows(df, ["2026-08-28"])
    assert calls and puts
    assert all(r["type"] == "Call" for r in calls)
    assert all(r["type"] == "Put" for r in puts)
    # 所有 call OI 都是 1000，按行权价稳定排序；最高行权价在最后，这里只验证数量与字段
    assert len(calls) == 5 and len(puts) == 5
    assert calls[0]["open_interest"] == 1000
    assert "strike" in calls[0] and "iv" in calls[0]


def test_oi_surge():
    cs = _contracts()
    prev = pd.DataFrame({
        "contractSymbol": ["Tcall100", "Tput95b"],
        "openInterest": [500, 5000],
    })
    df = m._frame(cs)
    surge = m.oi_surge(df, prev)
    assert surge is not None
    assert not surge.empty
    # 没有历史快照的合约增量 = 完整 OI(1000)，应排最前
    assert surge.iloc[0]["oi_change"] == 1000
    # Tput90 历史 OI 0 → 今日 500，增量 500（在 Top5 内）
    row = surge[surge["contract_symbol"] == "Tput90"]
    assert len(row) == 1 and row.iloc[0]["oi_change"] == 500


def test_iv_rank_requires_history():
    assert m.iv_rank(0.3, [0.2] * 19) is None
    hist = [0.2] * 19 + [0.3]
    assert abs(m.iv_rank(0.3, hist) - 100.0) < 1e-9


def _bs_delta(flag, S, K, t, sigma):
    return vollib_greeks.delta(flag, S, K, t, m.RISK_FREE_RATE, sigma)


def test_vanna_charm_vs_numeric():
    S, K, t, sigma = 100.0, 102.0, 0.2, 0.30
    v, c = m.vanna_charm(S, [K], t, [sigma])
    # Vanna = dDelta/dsigma（中心差分）
    h = 0.001
    v_num = (_bs_delta("c", S, K, t, sigma + h) - _bs_delta("c", S, K, t, sigma - h)) / (2 * h)
    assert abs(v[0] - v_num) < 1e-3
    # Charm = dDelta/dt（中心差分，t 以年为单位）
    h2 = 0.002
    c_num = (_bs_delta("c", S, K, t + h2, sigma) - _bs_delta("c", S, K, t - h2, sigma)) / (2 * h2)
    assert abs(c[0] - c_num) < 1e-2


def test_gamma_structure():
    cs = _contracts()
    df = m._frame(cs)
    st = m.gamma_structure(df, 100.0)
    assert st is not None
    assert st["call_wall"] is not None and st["put_wall"] is not None
    assert st["net_gex"] is not None
    assert len(st["top_gamma"]) <= 3
    assert st["net_vanna"] is not None and st["net_charm"] is not None
    # 看跌 OI 明显多于看涨（5000 vs 1000 的堆积），净 GEX 应为负（put 权重更大）
    assert st["net_gex"] < 0


def test_flow_and_new_exposure():
    cs = _contracts()
    df = m._frame(cs)
    # 只有 Tcall100 有历史 OI 500（今日 1000 → 开仓）；其余无历史
    prev_lookup = {"Tcall100": (500, 80), "Tput95b": (5000, 10)}
    rows = m.unusual_activity(df, min_volume=100, vol_oi_min=0.1, prev_lookup=prev_lookup)
    t100 = next(r for r in rows if r["contract_symbol"] == "Tcall100")
    assert t100["flow"] == "开仓"
    # Tput95b 有历史但 volume=0 → 流向为 —
    # 无历史的放量合约 → 新
    new_gex, new_delta = m._new_position_exposure(df, prev_lookup, 100.0)
    assert new_delta > 0   # Tcall100 新增 500 张 call → 正 delta
    assert new_gex > 0     # 新增 call gamma（正口径）


if __name__ == "__main__":
    for fn in (test_ratios, test_max_pain_shifts_to_heavy_put_strike, test_atm_metrics,
               test_skew_25, test_unusual_activity_filters, test_unusual_prev_lookup,
               test_top_oi_rows, test_oi_surge, test_iv_rank_requires_history,
               test_vanna_charm_vs_numeric, test_gamma_structure,
               test_flow_and_new_exposure):
        fn()
        print(f"PASS {fn.__name__}")
