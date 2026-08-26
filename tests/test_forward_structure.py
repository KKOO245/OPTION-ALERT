# -*- coding: utf-8 -*-
"""Forward Expiration Structure v1：聚合、Activity、Top ΔOI、L3、缺失处理。"""

import datetime

from src import forward_structure as fs


def _c(symbol, exp, typ, strike, oi, vol, last=None, iv=None, delta=None):
    return {
        "contract_symbol": symbol,
        "expiration": exp,
        "type": typ,
        "strike": strike,
        "open_interest": oi,
        "volume": vol,
        "last": last,
        "iv": iv,
        "delta": delta,
    }


def _prev(rows):
    return [
        {"contract_symbol": sym, "open_interest": oi, "volume": vol}
        for sym, oi, vol in rows
    ]


def _contracts():
    # 08-28：低（ΔOI 小）
    c = [
        _c("S0828C555", "2026-08-28", "call", 555, 5030, 800, 6.0, 0.30, 0.50),
        _c("S0828P545", "2026-08-28", "put", 545, 4010, 500, 5.0, 0.31, -0.49),
        # 09-04：中
        _c("S0904C560", "2026-09-04", "call", 560, 6200, 1000, 5.2, 0.33, 0.48),
        _c("S0904P550", "2026-09-04", "put", 550, 5100, 700, 4.8, 0.32, -0.47),
        # 09-11：中（Call 减仓）
        _c("S0911C565", "2026-09-11", "call", 565, 6800, 900, 4.6, 0.35, 0.46),
        _c("S0911P555", "2026-09-11", "put", 555, 3080, 600, 4.2, 0.34, -0.45),
        # 09-18：高（Call 大幅增仓）
        _c("S0918C515", "2026-09-18", "call", 515, 3100, 400, 5.84, 0.40, 0.52),
        _c("S0918P515", "2026-09-18", "put", 515, 2100, 300, 14.12, 0.38, -0.48),
        _c("S0918C575", "2026-09-18", "call", 575, 17348, 5840, 0.87, 0.42, 0.35),
        _c("S0918C670", "2026-09-18", "call", 670, 12120, 900, 0.49, 0.45, 0.20),
        _c("S0918P500", "2026-09-18", "put", 500, 9850, 2500, 8.10, 0.39, -0.45),
    ]
    return c


def _prev_rows():
    return _prev([
        ("S0828C555", 5000, 700), ("S0828P545", 4000, 400),
        ("S0904C560", 6000, 800), ("S0904P550", 5000, 600),
        ("S0911C565", 7000, 800), ("S0911P555", 3000, 500),
        ("S0918C515", 3000, 300), ("S0918P515", 2000, 200),
        ("S0918C575", 10000, 400), ("S0918C670", 8000, 300),
        ("S0918P500", 7000, 400),
    ])


def _build(**kw):
    kw.setdefault("contracts", _contracts())
    kw.setdefault("prev", _prev_rows())
    kw.setdefault("spot", 515.5)
    kw.setdefault("as_of_date", datetime.date(2026, 8, 24))
    kw.setdefault("config_root", "config")
    return fs.build_forward_structure(**kw)


def test_expirations_order_and_dte():
    out = _build()
    exps = [e["expiration"] for e in out["expirations"]]
    assert exps == ["2026-08-28", "2026-09-04", "2026-09-11", "2026-09-18"]
    assert [e["dte"] for e in out["expirations"]] == [4, 11, 18, 25]


def test_aggregation_and_atm():
    out = _build()
    e = next(x for x in out["expirations"] if x["expiration"] == "2026-09-18")
    assert e["call_oi"] == 32568
    assert e["put_oi"] == 11950
    assert e["call_delta_oi"] == 11568
    assert e["put_delta_oi"] == 2950
    assert e["atm_strike"] == 515
    assert e["atm_call_price"] == 5.84
    assert e["atm_put_price"] == 14.12
    assert abs(e["atm_iv"] - 0.39) < 1e-6
    assert e["activity"] == "HIGH"


def test_expmove_pct_per_expiry():
    out = _build()
    e = next(x for x in out["expirations"] if x["expiration"] == "2026-09-18")
    assert e["expmove_pct"] == round((5.84 + 14.12) / 515.5 * 100.0, 2)
    assert abs(e["expmove_pct"] - 3.87) < 0.01


def test_roll_candidates_backend_only():
    contracts = [
        _c("S0918C700", "2026-09-18", "call", 700, 12000, 300, 1.5, 0.40, 0.30),
        _c("S0918C720", "2026-09-18", "call", 720, 10000, 300, 1.2, 0.41, 0.28),
    ]
    prev = _prev([("S0918C700", 20000, 200), ("S0918C720", 1000, 100)])
    out = _build(contracts=contracts, prev=prev)
    e = next(x for x in out["expirations"] if x["expiration"] == "2026-09-18")
    assert e["roll_candidates"], "应识别同期限同类型一正一负大额 ΔOI"
    rc = e["roll_candidates"][0]
    assert rc["type"] == "call"
    assert rc["from_strike"] == 700 and rc["to_strike"] == 720
    assert rc["from_delta_oi"] == -8000 and rc["to_delta_oi"] == 9000
    assert rc["confidence"] == "MEDIUM"  # 行权价差 20 ≤ 10%×720


def test_activity_levels():
    out = _build()
    by_exp = {e["expiration"]: e["activity"] for e in out["expirations"]}
    assert by_exp["2026-08-28"] == "LOW"
    assert by_exp["2026-09-04"] == "MEDIUM"
    assert by_exp["2026-09-11"] == "MEDIUM"
    assert by_exp["2026-09-18"] == "HIGH"


def test_top_delta_oi_sorted_with_distance_and_notional():
    out = _build()
    e = next(x for x in out["expirations"] if x["expiration"] == "2026-09-18")
    top = e["top_delta_oi"]
    assert [t["strike"] for t in top] == [575, 670, 500]
    assert top[0]["delta_oi"] == 7348
    assert abs(top[0]["distance_pct"] - 11.5) < 0.1
    assert abs(top[0]["notional"] - (7348 * 0.87 * 100.0)) < 1


def test_delta_exposure_model_estimate():
    out = _build()
    e = next(x for x in out["expirations"] if x["expiration"] == "2026-09-18")
    assert e["delta_exposure"] == 211730


def test_significant_l3_conditions():
    out = _build()
    e = next(x for x in out["expirations"] if x["expiration"] == "2026-09-18")
    sig = e["significant"]
    assert [s["strike"] for s in sig] == [575, 500]
    assert all(s["magnitude"] == "HIGH" for s in sig)
    assert all((s.get("r1") or 0) >= 20 for s in sig)


def test_partial_prev_new_strike_matched_delta():
    """同一结算日新增行权价：ΔOI 只算同合约口径，新行权价 OI 单列。"""
    contracts = [
        _c("X1C575", "2026-09-18", "call", 575, 11000, 1000, 0.9, 0.40, 0.35),
        _c("X1C690", "2026-09-18", "call", 690, 500, 100, 0.2, 0.45, 0.25),   # 新行权价
        _c("X1P500", "2026-09-18", "put", 500, 7500, 800, 8.0, 0.39, -0.45),
    ]
    prev = _prev([("X1C575", 10000, 500), ("X1P500", 7000, 300)])
    out = _build(contracts=contracts, prev=prev)
    e = out["expirations"][0]
    assert e["call_delta_oi"] == 1000      # 不是 1500
    assert e["call_new_oi"] == 500
    assert e["put_delta_oi"] == 500
    assert e["put_new_oi"] == 0


def test_l3_requires_high_r1():
    """magnitude=HIGH 但 ΔOI/Volume 不高（r1<20%）→ 不得触发 L3。"""
    contracts = [
        _c("X2C500", "2026-09-18", "call", 500, 3000, 100000, 5.0, 0.40, 0.50),
        _c("X2P500", "2026-09-18", "put", 500, 100, 10, 8.0, 0.39, -0.45),
    ]
    prev = _prev([("X2C500", 1000, 90000), ("X2P500", 100, 5)])
    out = _build(contracts=contracts, prev=prev)
    e = out["expirations"][0]
    assert e["activity"] == "HIGH"
    assert e["top_delta_oi"][0]["magnitude"] == "HIGH"
    assert e["top_delta_oi"][0]["r1"] == 2.0
    assert e["significant"] == []


def test_new_listing_delta_na():
    contracts = [_c("S1025C600", "2026-10-25", "call", 600, 5000, 300, 3.0, 0.36, 0.40)]
    out = _build(contracts=contracts, prev=[])
    e = out["expirations"][0]
    assert e["new_listing"] is True
    assert e["call_delta_oi"] is None
    assert e["put_delta_oi"] is None
    assert e["activity"] == "LOW"
    assert e["top_delta_oi"] == []


def test_n_expirations_cap():
    contracts = []
    for i, exp in enumerate(
        ["2026-08-28", "2026-09-04", "2026-09-11", "2026-09-18", "2026-09-25"]
    ):
        contracts.append(_c(f"X{i}C", exp, "call", 500 + i, 1000, 100, 2.0, 0.30, 0.5))
    out = _build(contracts=contracts, prev=[])
    assert len(out["expirations"]) == 4
    assert out["expirations"][-1]["expiration"] == "2026-09-18"


def test_zero_dte_excluded():
    contracts = [
        _c("A0C", "2026-08-24", "call", 500, 1000, 100, 2.0, 0.30, 0.5),
        _c("A1C", "2026-08-28", "call", 510, 1000, 100, 2.0, 0.30, 0.5),
    ]
    out = _build(contracts=contracts, prev=[])
    assert [e["expiration"] for e in out["expirations"]] == ["2026-08-28"]


def test_config_root_accepts_repo_root():
    """回归：options_report 传仓库根目录（BASE_DIR）也能找到 thresholds.yaml（8/25 线上事故）。"""
    out = _build(config_root=fs.BASE_DIR)
    assert len(out["expirations"]) == 4
    assert out["expirations"][0]["expiration"] == "2026-08-28"
