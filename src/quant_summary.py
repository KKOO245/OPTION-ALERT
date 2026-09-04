# -*- coding: utf-8 -*-
"""量化视角综合解读（quant_summary_v1）：纯规则合成，可溯源，禁止编造。

纪律（最重要）：
  - 每条结论必须能回溯到快照里的具体指标；数据缺失 → 省略该条，绝不猜测；
  - 阈值全部为候选参数（quant_summary_v1，登记于 config/thresholds.yaml），不冻结；
  - 永远不输出方向结论；任何组合升级都只标"需重点观察/观察点"，结尾固定
    "观察点，非方向信号"。

覆盖四个位置（早/晚报共用）：
  options_quant    → Options 行后（全标的）
  hist_quant_line  → 历史分位行后（仅 SPY/QQQ，有 15 年 oi_history）
  gex_quant_line   → 结构区块底部（GEX 程度 × 日内变化 × 相对 Flip）
  activity_quant   → Activity 区块底部（事件模式：汇总/分层/尾部对冲特征）
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Optional

DEFAULTS = {
    "rank_low_pct": 25.0,
    "rank_high_pct": 75.0,
    "term_inverted": 0.9,
    "term_steep": 1.15,
    "skew_low_pp": 2.0,
    "skew_high_pp": 6.0,
    "pcr_oi_crowded_low": 0.85,   # 存量 OI 比 ≤ 此值 → Call 拥挤（绝对水平代理）
    "pcr_vol_put_bias": 1.15,     # 当日 P/C 量 ≥ 此值 → 成交偏 Put
    "gex_pct_low": 25.0,
    "gex_pct_high": 75.0,
    "pcr_pct_crowded_low": 10.0,  # P/C OI 历史分位 ≤ 此值 → 极端 Call 重
    "pcr_pct_crowded_high": 90.0,
    "premium_real": 1.0,          # last > $1 → 实质成本保护
    "premium_lottery": 0.05,      # last ≤ $0.05 → 彩票/名义
    "dist_near_pct": 5.0,
    "dist_far_pct": 10.0,
    "notional_low_k": 50.0,       # Top ΔOI 名义 < 50k → 低相关性（彩票）
}
DISCIPLINE = "观察点，非方向信号"


def _num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def _load_params(root) -> Dict[str, Any]:
    p = dict(DEFAULTS)
    try:
        from engine.yaml_mini import load

        cfg = load(Path(root) / "config" / "thresholds.yaml")
        qs = (cfg or {}).get("quant_summary_v1") or {}
        for k in p:
            if qs.get(k) is not None:
                p[k] = float(qs[k])
    except Exception:  # noqa: BLE001
        pass
    return p


def _rank_pct(rank) -> Optional[float]:
    r = _num(rank)
    if r is None:
        return None
    return r * 100.0 if r <= 1.0 else r


def options_quant(momentum: Dict[str, Any], params: Optional[Dict[str, Any]] = None) -> Optional[str]:
    """Options 行后的综合解读（全标的）。缺字段 → 省略该条，不编造。"""
    p = params or DEFAULTS
    clauses: List[str] = []
    rank = _rank_pct(momentum.get("iv_rank"))
    if rank is not None:
        if rank <= p["rank_low_pct"]:
            clauses.append(f"IV 历史低位（Rank {rank:.0f}%，期权偏便宜）")
        elif rank >= p["rank_high_pct"]:
            clauses.append(f"IV 历史高位（Rank {rank:.0f}%，期权偏贵）")
        else:
            clauses.append(f"IV 中性（Rank {rank:.0f}%）")
    term = _num(momentum.get("term_ratio"))
    if term is not None:
        if term < p["term_inverted"]:
            clauses.append(f"期限结构倒挂（Term {term:.2f}，近月 IV 高于远月）")
        elif term > p["term_steep"]:
            clauses.append(f"期限结构正常偏陡（Term {term:.2f}）")
        else:
            clauses.append(f"期限结构正常（Term {term:.2f}）")
    skew = _num(momentum.get("skew"))
    if skew is not None:
        if skew < 0:
            clauses.append(f"Put 保护异常便宜（Skew {skew:.1f}pp，Put IV < Call IV）")
        elif skew <= p["skew_low_pp"]:
            clauses.append(f"保护溢价薄（Skew {skew:.1f}pp）")
        elif skew >= p["skew_high_pp"]:
            clauses.append(f"保护溢价显著（Skew {skew:.1f}pp，Put 明显贵于 Call）")
        else:
            clauses.append(f"保护溢价中性（Skew {skew:.1f}pp）")
    # 存量 vs 当日：背离组合升级为"重点观察"
    oi_ratio = _num(momentum.get("pc_oi_ratio"))
    vol_ratio = _num(momentum.get("pc_ratio"))
    if oi_ratio is not None and vol_ratio is not None:
        call_crowded = oi_ratio <= p["pcr_oi_crowded_low"]
        put_flow = vol_ratio >= p["pcr_vol_put_bias"]
        if call_crowded and put_flow:
            clauses.append(
                f"⚠️ 重点观察：存量 Call 重（OI比 {oi_ratio:.2f}）+ 当日成交偏 Put（P/C量 {vol_ratio:.2f}）"
                "——结构背离，买/卖方向不可观测"
            )
        elif call_crowded:
            clauses.append(f"存量 Call 偏重（OI比 {oi_ratio:.2f}）")
        elif put_flow:
            clauses.append(f"当日成交偏 Put（P/C量 {vol_ratio:.2f}）")
        else:
            clauses.append("当日成交与存量接近均衡")
    elif oi_ratio is not None:
        clauses.append(f"存量 OI 比 {oi_ratio:.2f}")
    elif vol_ratio is not None:
        clauses.append(f"当日 P/C 量 {vol_ratio:.2f}")
    if not clauses:
        return None
    return "量化视角： " + "｜".join(clauses) + f"——{DISCIPLINE}"


def _oi_hist(ticker: str, root) -> Optional[Dict[str, List[float]]]:
    """SPY/QQQ 15 年 oi_history 分布（net_gex 与 pcr_oi_near）。"""
    p = Path(root) / "data" / "oi_history" / f"{ticker}.csv"
    if not p.exists():
        return None
    import pandas as pd

    try:
        df = pd.read_csv(p)
    except Exception:  # noqa: BLE001
        return None
    out: Dict[str, List[float]] = {}
    if "net_gex" in df.columns:
        out["net_gex"] = df["net_gex"].dropna().tolist()
    if "pcr_oi_near" in df.columns:
        out["pcr_oi_near"] = df["pcr_oi_near"].dropna().tolist()
    return out or None


def _pct_rank(value, hist: List[float]) -> Optional[float]:
    v = _num(value)
    if v is None or not hist:
        return None
    return sum(1 for x in hist if x <= v) / len(hist) * 100.0


def hist_quant_line(snapshot: Dict[str, Any], root) -> Optional[str]:
    """历史分位行后的组合解读（仅 SPY/QQQ；缺 15 年分布 → 不输出）。"""
    ticker = (snapshot.get("ticker") or "").upper()
    if ticker not in ("SPY", "QQQ"):
        return None
    p = _load_params(root)
    hist = _oi_hist(ticker, root)
    if not hist:
        return None
    p3 = snapshot.get("p3") or {}
    gex = (p3.get("gex") or {}).get("net_gex")
    pcr = (snapshot.get("momentum") or {}).get("pc_oi_ratio")
    gex_pct = _pct_rank(gex, hist.get("net_gex", []))
    pcr_pct = _pct_rank(pcr, hist.get("pcr_oi_near", []))
    clauses: List[str] = []
    if gex_pct is not None:
        if gex_pct <= p["gex_pct_low"]:
            clauses.append(f"Gamma 异常偏负（GEX 分位 {gex_pct:.0f}%）")
        elif gex_pct >= p["gex_pct_high"]:
            clauses.append(f"Gamma 异常偏正（GEX 分位 {gex_pct:.0f}%）")
        else:
            clauses.append(f"Gamma 处于历史中位（GEX 分位 {gex_pct:.0f}%）")
    if pcr_pct is not None:
        if pcr_pct <= p["pcr_pct_crowded_low"]:
            clauses.append(f"近端持仓极端 Call 重（P/C OI 分位 {pcr_pct:.0f}%，历史极低区）")
        elif pcr_pct >= p["pcr_pct_crowded_high"]:
            clauses.append(f"近端 Put 显著偏重（P/C OI 分位 {pcr_pct:.0f}%，历史高位区）")
        else:
            clauses.append(f"近端持仓结构中性（P/C OI 分位 {pcr_pct:.0f}%）")
    if not clauses:
        return None
    # 组合升级：持仓极端 + Gamma 异常侧 → 重点观察
    extreme_pcr = (pcr_pct is not None and (pcr_pct <= p["pcr_pct_crowded_low"] or pcr_pct >= p["pcr_pct_crowded_high"]))
    extreme_gex = (gex_pct is not None and (gex_pct <= p["gex_pct_low"] or gex_pct >= p["gex_pct_high"]))
    if extreme_pcr and extreme_gex:
        clauses.append("⚠️ 需重点观察：持仓极端 + Gamma 异常侧组合")
    return "量化视角的组合解读： " + "｜".join(clauses) + f"——{DISCIPLINE}"


def gex_quant_line(snapshot: Dict[str, Any], prev_snapshot: Optional[Dict[str, Any]],
                   root, params: Optional[Dict[str, Any]] = None) -> Optional[str]:
    """结构区块底部的 GEX 量化视角（Gamma 程度 × 日内变化 × 相对 Flip）。"""
    p = params or _load_params(root)
    p3 = snapshot.get("p3") or {}
    gex = (p3.get("gex") or {}).get("net_gex")
    gex_v = _num(gex)
    if gex_v is None:
        return None
    clauses: List[str] = []
    def _money(v: float) -> str:
        # 金额单位规范：≥1亿 用"X.XX亿"，<1亿 用"XXXX万"（不用"百万"）
        return f"{abs(v)/1e8:.2f}亿" if abs(v) >= 1e8 else f"{abs(v)/1e4:.0f}万"
    # 程度（有 15 年分位则用分位，否则用数值符号）
    ticker = (snapshot.get("ticker") or "").upper()
    gex_pct = None
    if ticker in ("SPY", "QQQ"):
        hist = _oi_hist(ticker, root)
        if hist:
            gex_pct = _pct_rank(gex_v, hist.get("net_gex", []))
    if gex_pct is not None:
        if gex_pct <= p["gex_pct_low"]:
            # 低分位（带符号）：负值=深度负，正值=轻度正（多数交易日更正）
            clauses.append(
                f"负 Gamma（{_money(gex_v)}，历史分位偏负区，比 {100 - gex_pct:.0f}% 的交易日更负）"
                if gex_v < 0 else
                f"正 Gamma（{_money(gex_v)}，历史分位偏正区，弱于 {100 - gex_pct:.0f}% 的交易日）"
            )
        elif gex_pct >= p["gex_pct_high"]:
            # 高分位（带符号）：正值=显著正，负值=轻负（多数交易日更负）
            clauses.append(
                f"正 Gamma（{_money(gex_v)}，历史分位偏正区，比 {gex_pct:.0f}% 的交易日更正）"
                if gex_v > 0 else
                f"负 Gamma（{_money(gex_v)}，历史分位偏负区，轻于 {gex_pct:.0f}% 的交易日）"
            )
        else:
            clauses.append(f"{'负' if gex_v < 0 else '正'} Gamma（{_money(gex_v)}，历史分位 {gex_pct:.0f}%，中性区）")
    else:
        clauses.append(f"{'负' if gex_v < 0 else '正'} Gamma（{_money(gex_v)}，无历史分位）")
    # 日内变化（vs 上次快照）
    prev_gex = None
    if prev_snapshot is not None:
        prev_gex = ((prev_snapshot.get("p3") or {}).get("gex") or {}).get("net_gex")
    change = None
    if prev_gex is not None:
        change = gex_v - _num(prev_gex)
    if change is not None:
        prev_v = _num(prev_gex)
        if prev_v is not None:
            if prev_v < 0 and gex_v < 0:
                verb = "负 Gamma 缓解" if change > 0 else "负 Gamma 加深"
            elif prev_v < 0 and gex_v > 0:
                verb = "由负转正"
            elif prev_v > 0 and gex_v > 0:
                verb = "正 Gamma 增强" if change > 0 else "正 Gamma 减弱"
            elif prev_v > 0 and gex_v < 0:
                verb = "由正转负"
            else:
                verb = "GEX 变化"
            clauses.append(f"{verb}（{'+' if change > 0 else ''}{_money(change)}）")
        else:
            clauses.append(f"GEX 变化（{'+' if change > 0 else ''}{_money(change)}）")
    # 相对 Flip
    loc = snapshot.get("location") or {}
    svf = loc.get("spot_vs_primary_flip") or {}
    if svf.get("distance_pct") is not None:
        side = "上方" if svf.get("side") == "ABOVE" else "下方"
        clauses.append(f"现价位于 Flip {side} {abs(float(svf['distance_pct'])):.2f}%")
    # 重点观察：负 Gamma 且加深；或真正发生符号翻转（由正转负）
    if gex_v < 0 and change is not None and change < 0:
        clauses.append("⚠️ 重点观察：负 Gamma 且日内加深")
    elif gex_v > 0 and change is not None and change < 0 and _num(prev_gex) is not None and _num(prev_gex) > 0:
        clauses.append("⚠️ 重点观察：正 Gamma 由正转负（结构切换）")
    if not clauses:
        return None
    return "量化视角： " + "｜".join(clauses) + f"——{DISCIPLINE}"


def activity_quant(events: Optional[List[Dict[str, Any]]], spot: Optional[float],
                   params: Optional[Dict[str, Any]] = None) -> Optional[str]:
    """Activity 区块底部：事件模式解读（汇总/分层/尾部对冲特征）。"""
    p = params or DEFAULTS
    evs = [e for e in (events or []) if isinstance(e, dict)]
    if not evs:
        return None
    puts = [e for e in evs if str(e.get("type") or "").lower() == "put"]
    calls = [e for e in evs if str(e.get("type") or "").lower() == "call"]
    def _d(e):
        oi_now = _num(e.get("open_interest"))
        oi_prev = _num(e.get("oi_prev"))
        if oi_now is None or oi_prev is None:
            return None
        return oi_now - oi_prev
    total_put = sum(_d(e) or 0 for e in puts)
    total_call = sum(_d(e) or 0 for e in calls)
    total = total_put + total_call
    exps = {str(e.get("expiration") or "") for e in evs if e.get("expiration")}
    clauses: List[str] = []
    clauses.append(f"{len(evs)} 个事件合计 ΔOI ≈ {total:,.0f} 张（Put {total_put:,.0f} / Call {total_call:,.0f}），跨 {len(exps)} 个期限")
    # 按价格/距离分层
    real_put = [e for e in puts if _num(e.get("last_price")) is not None and _num(e.get("last_price")) > p["premium_real"]]
    lottery_put = [e for e in puts if _num(e.get("last_price")) is not None and 0 < _num(e.get("last_price")) <= p["premium_lottery"]]
    if spot:
        near = [e for e in puts if _num(e.get("strike")) is not None
                and abs(_num(e.get("strike")) / spot - 1.0) * 100.0 <= p["dist_near_pct"]]
        far = [e for e in puts if _num(e.get("strike")) is not None
               and abs(_num(e.get("strike")) / spot - 1.0) * 100.0 > p["dist_far_pct"]]
        if real_put:
            rp_notional = sum((_d(e) or 0) * _num(e.get("last_price")) * 100.0 for e in real_put)
            clauses.append(f"近端保护（{len(near)} 档，距现价 ≤{p['dist_near_pct']:.0f}%，权利金合计约 ${rp_notional/1e6:.0f}M，买/卖方向不可观测）" if near
                           else f"有实质成本保护 {len(real_put)} 档（权利金 >${p['premium_real']:.0f}，买/卖方向不可观测）")
        if lottery_put:
            clauses.append(f"远端彩票/名义（{len(far)} 档，距现价 >{p['dist_far_pct']:.0f}%，价 ≤${p['premium_lottery']:.2f}）" if far
                           else f"彩票/名义 {len(lottery_put)} 档（价 ≤${p['premium_lottery']:.2f}）")
    # 模式：多期限 Put 集中加仓 → 尾部对冲特征
    if total_put >= 3 * abs(total_call) + 1 and len(exps) >= 2 and total_put >= 10000:
        clauses.append("多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）")
    elif puts:
        clauses.append("Put 增仓为主（孤立/局部，暂不构成模式推断）")
    return "量化视角： " + "｜".join(clauses) + f"——方向未知，观察连续性，{DISCIPLINE}"
