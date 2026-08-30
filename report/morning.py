# -*- coding: utf-8 -*-
"""晨报渲染（P0.3 规格 v1）：对比区 + 每标的展开块 + 注解 + Setup/Gate 状态。"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from engine.annotations import event_card, options_annotation
from engine.gate import gate_pipeline
from report.format import fmt, ticker_heading


def _trading_gap(a_date: str, b_date: str) -> int:
    """两个日期之间的工作日数（不含两端），与 Episode 聚类口径一致。"""
    from datetime import date, timedelta

    try:
        a = date.fromisoformat(a_date[:10])
        b = date.fromisoformat(b_date[:10])
    except (TypeError, ValueError):
        return 0
    if b <= a:
        return 0
    n = 0
    d = a
    while True:
        d += timedelta(days=1)
        if d >= b:
            break
        if d.weekday() < 5:
            n += 1
    return n


def _distance(spot: float, level: Optional[float]) -> Optional[float]:
    if spot is None or level is None:
        return None
    return (spot / level - 1.0) * 100.0


def _options_block(snapshot: Dict[str, Any]) -> List[str]:
    m = snapshot.get("momentum") or {}
    rank = m.get("iv_rank")
    if rank is None:
        rank_txt = "— (历史不足)"
    else:
        rank_txt = f"{rank * 100:.0f}%" if rank <= 1 else f"{rank:.0f}%"
    expmove = m.get("expected_move_pct")
    expmove_txt = f"±{fmt(expmove, 1)}%" if expmove is not None else "N/A"
    fwd = snapshot.get("forward") or {}
    exps = fwd.get("expirations") or []
    if expmove is not None and exps:
        expmove_txt = f"±{fmt(expmove, 1)}%（近端）"
    skew = m.get("skew")
    skew_txt = f"{fmt(skew, 1)}pp" if skew is not None else "N/A"
    line = (
        f"Options: P/C量 {fmt(m.get('pc_ratio'), 2)} | OI比 {fmt(m.get('pc_oi_ratio'), 2)} | "
        f"ATM IV {fmt_pct_safe(m.get('atm_iv'))} | Skew {skew_txt} | "
        f"Term {fmt(m.get('term_ratio'), 2)} | ExpMove {expmove_txt} | Rank {rank_txt}"
    )
    lines = [line]
    for a in options_annotation(m.get("pc_ratio"), m.get("pc_oi_ratio")):
        lines.append("   ⇒ " + a)
    # ExpMove 期限化（expmove_v1）：逐结算日独立计算，杜绝单值混用期限
    exp_parts = []
    for e in exps:
        ev = e.get("expmove_pct")
        if ev is None:
            # 旧快照兜底：用 ATM C/P 与 spot 现算（与 expmove_v1 同公式）
            cp, pp = e.get("atm_call_price"), e.get("atm_put_price")
            if cp is not None and pp is not None and snapshot.get("spot"):
                ev = round((float(cp) + float(pp)) / float(snapshot["spot"]) * 100.0, 2)
        if ev is not None:
            exp_parts.append(f"{e['expiration'][5:]}（{e.get('dte', '?')}D）±{ev:.1f}%")
    if exp_parts:
        lines.append("   ExpMove 期限化（expmove_v1）: " + " ｜ ".join(exp_parts))
    return lines


def fmt_pct_safe(v: Any) -> str:
    if v is None:
        return "N/A"
    return f"{v * 100:.1f}%"


def _structure_block(snapshot: Dict[str, Any], gex: Optional[float] = None, gex_change: Optional[float] = None) -> List[str]:
    loc = snapshot.get("location") or {}
    spot = snapshot.get("spot")
    lines = ["🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）"]
    gamma = (snapshot.get("regime") or {}).get("gamma", "UNKNOWN")
    gex_txt = f"GEX(存量) {fmt(gex, 0)}" if gex is not None else "GEX(存量) N/A"
    chg_txt = f"GEX Change vs 上次快照 {fmt(gex_change, 0)}" if gex_change is not None else "GEX Change N/A"
    flip_status = loc.get("flip_status")
    flip_reason = loc.get("flip_reason")
    flip_candidates = loc.get("flip_candidates") or loc.get("flip_levels") or []
    flip_primary = loc.get("flip_primary")
    if flip_candidates:
        shown = flip_candidates[:5]
        cand_txt = " / ".join(f"{f:.2f}" for f in shown)
        if len(flip_candidates) > 5:
            cand_txt += f" …共{len(flip_candidates)}个"
        if flip_primary is not None and flip_status == "PRIMARY":
            flip_txt = f"Primary Flip: {flip_primary:.2f}（PRIMARY，全链重定价 + 覆盖达标）"
        else:
            status_txt = flip_status or "CONDITIONAL"
            flip_txt = f"Candidates {cand_txt} ｜ Primary: N/A（{status_txt}）"
    else:
        flip_txt = flip_status or "N/A"
    lines.append(f"Gamma Regime: {gamma}（模型分类） | {gex_txt} | {chg_txt} | Flip: {flip_txt}")
    p3 = snapshot.get("p3") or {}
    cov = p3.get("coverage") or {}
    eff = cov.get("effective_gex_coverage_pct")
    ivv = cov.get("iv_valid") or {}
    eff_txt = f"{eff:.0f}%（带内）" if eff is not None else "待盘点"
    if ivv:
        iv_txt = (
            f"VALID {ivv.get('VALID', 0)} / LOW {ivv.get('LOW_LIQUIDITY', 0)} / "
            f"INVALID {ivv.get('INVALID', 0)}"
        )
    else:
        iv_txt = "待审计"
    gamma_calc = "全链重定价" if loc.get("flip_source") == "full_chain" else "Top-3 近似"
    lines.append(
        "🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ "
        f"Gamma 口径 {gamma_calc} ｜ Effective GEX 覆盖: {eff_txt} ｜ IV 有效性: {iv_txt}"
    )
    if gamma == "NEGATIVE":
        if gex is not None:
            lines.append("   ⇒ 全链负Gamma，波动易被放大（模型层）")
        else:
            lines.append("   ⇒ Gamma Regime 判定为 NEGATIVE；GEX 数值不可用，不对 Gamma 强度做判断。")
    flips = loc.get("flip_levels") or []
    if loc.get("flip_source") == "full_chain":
        # 全链口径：不再出现 Top-3 近似文案
        cov_short = f"覆盖 {eff:.0f}%" if eff is not None else "覆盖待盘点"
        if flip_primary is not None and flip_status == "PRIMARY":
            lines.append(f"结构观察区: Primary Flip {flip_primary:.2f}（全链重定价，{cov_short}）")
        elif len(flips) >= 2:
            lines.append(f"结构观察区: {flips[0]:.0f}–{flips[1]:.0f}（全链重定价，{cov_short}，CONDITIONAL）")
        elif len(flips) == 1:
            lines.append(f"结构观察区: ≈{flips[0]:.0f}（全链重定价，{cov_short}，CONDITIONAL）")
        else:
            lines.append(f"结构观察区: {flip_status or 'N/A'}")
    elif len(flips) >= 2:
        lines.append(
            f"结构观察区: {flips[0]:.0f}–{flips[1]:.0f}"
            "（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）"
        )
    elif len(flips) == 1:
        lines.append(
            f"结构观察区: ≈{flips[0]:.0f}"
            "（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）"
        )
    else:
        lines.append(f"结构观察区: {flip_status or 'N/A'}")
    cw, pw = loc.get("call_wall"), loc.get("put_wall")
    cw_cls, pw_cls = loc.get("call_wall_class"), loc.get("put_wall_class")
    if cw or pw:
        parts = []
        if pw:
            parts.append(f"Put Wall {fmt(pw, 0)}（{_wall_label(spot, pw, pw_cls)}）")
        if cw:
            parts.append(f"Call Wall {fmt(cw, 0)}（{_wall_label(spot, cw, cw_cls)}）")
        lines.append(" | ".join(parts))
    # 最近结构参考：离现价最近的结构位（Wall / Flip 候选），一行给结论
    cands = []
    if pw:
        cands.append(("Put Wall", pw))
    if cw:
        cands.append(("Call Wall", cw))
    for f in flip_candidates:
        cands.append(("Flip", f))
    if cands and spot is not None:
        name, lvl = min(cands, key=lambda x: abs(spot / float(x[1]) - 1.0))
        lines.append(f"最近结构参考: {name} {lvl:.0f}（{_dist_label(spot, lvl)}）")
    return [l for l in lines if l]


def _dist_str(v: Optional[float]) -> str:
    return "N/A" if v is None else f"{v:+.1f}%"


def _dist_label(spot: Optional[float], level: Optional[float]) -> str:
    """结构位相对现价的明确方向标签：口径 (spot/level - 1) × 100。"""
    dist = _distance(spot, level)
    if dist is None:
        return "N/A"
    if dist >= 0:
        return f"现价高于该位 {dist:.1f}%"
    return f"现价低于该位 {abs(dist):.1f}%"


def _wall_label(spot: Optional[float], level: Optional[float], cls: Optional[str]) -> str:
    """Wall 显示标签：WEAK 结构标注"弱结构｜"，PRIMARY/REMOTE 不加（REMOTE 已不在显示值里）。"""
    base = _dist_label(spot, level)
    return ("弱结构｜" + base) if cls == "WEAK" else base


def _structure_interpretation(snapshot: Dict[str, Any]) -> List[str]:
    loc = snapshot.get("location") or {}
    spot = snapshot.get("spot")
    mp = (snapshot.get("context") or {}).get("max_pain")
    cw, pw = loc.get("call_wall"), loc.get("put_wall")
    cw_cls, pw_cls = loc.get("call_wall_class"), loc.get("put_wall_class")
    lines = ["🧭 结构解读（全部依赖上方假设）"]
    downs = [f"{fmt(pw, 0)}（Put Wall{('，弱结构' if pw_cls == 'WEAK' else '')}）"] if pw else []
    ups = []
    if mp:
        ups.append(f"{fmt(mp, 0)}（MaxPain，仅结算参考）")
    if cw:
        ups.append(f"{fmt(cw, 0)}（Call Wall{('，弱结构' if cw_cls == 'WEAK' else '')}）")
    if downs:
        lines.append(f"• 支撑/压力参考：下方 {' / '.join(downs)}；上方 {' / '.join(ups) if ups else 'N/A'}。")
    flips = loc.get("flip_levels") or []
    if flips:
        ref = (loc.get("flip_primary") or flips[0])
        if loc.get("flip_source") == "full_chain":
            p3 = snapshot.get("p3") or {}
            cov = p3.get("coverage") or {}
            eff = cov.get("effective_gex_coverage_pct")
            cov_txt = f"覆盖 {eff:.0f}%" if eff is not None else "覆盖待盘点"
            lines.append(f"• Gamma 区域：切换参考 {ref:.0f}（全链重定价，{cov_txt}）。")
        else:
            lines.append(f"• Gamma 区域：切换参考 {ref:.0f}（Top-3 近似，需全链重定价验证）。")
    lines.append(
        "• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；"
        "实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。"
    )
    lines.append("• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。")
    return lines


def _setup_block(setup_status: Optional[Dict[str, Any]], vol_env: Optional[Dict[str, Any]] = None) -> List[str]:
    if not setup_status:
        return ["Setup: 今日无 Setup 触发（机械检查全部 Setup）"]
    core = setup_status.get("core", {})
    conf = setup_status.get("confirmation", {})
    lines = [
        f"Setup {setup_status.get('setup_id')} {setup_status.get('version', '')} — Core Conditions",
        f"Price Regime {core.get('trend', '?')} | Location {core.get('location', '?')} | Gamma Regime {core.get('gamma', '?')}",
        f"Confirmation: ✓ {conf.get('satisfied', 0)} ｜ ✗ {conf.get('rejected', 0)} ｜ ? {conf.get('unknown', 0)}"
        + (f"（? {', '.join(conf.get('unknown_fields', []))}）" if conf.get("unknown_fields") else ""),
    ]
    q = setup_status.get("qualification")
    if q:
        lift = q.get("oos_lift_pp")
        lift_txt = f"{fmt(lift, 1)}pp" if lift is not None else "N/A"
        lines.append(f"验证状态: N={q.get('n_episodes', 'N/A')} ｜ OOS Lift {lift_txt} ｜ CI 下界 {fmt(q.get('ci_lower'), 2)}")
    pt = setup_status.get("primary_target")
    if pt:
        lines.append(f"Target: {pt.get('metric')} {pt.get('direction')} {pt.get('threshold')} — PENDING（evaluation date 待窗口结束）")
    st = setup_status.get("status")
    if st:
        lines.append(f"Status: {st}")
    label = None
    if isinstance(vol_env, dict):
        label = (vol_env.get("regime") or {}).get("label")
    if label and label != "INSUFFICIENT_DATA":
        lines.append(f"环境: Vol {label}（仅环境标签，不参与计票）")
    return lines


def _activity_block(events: Optional[List[Dict[str, Any]]], stale_note: Optional[str] = None) -> List[str]:
    lines = ["🔺 Activity（事实层，方向 Unknown）"]
    if stale_note:
        lines.append(f"- ⚠️ {stale_note}")
    if events is None:
        lines.append("- Activity 数据缺失（analytics 未提供），不猜测")
        return lines
    if not events:
        lines.append("- 无中高变动事件（全部低等级）")
        return lines
    for ev in events:
        exp = ev.get("expiration") or "?"
        exp_txt = exp[5:] if isinstance(exp, str) and len(exp) >= 10 else str(exp)
        side = "P" if ev.get("type") == "put" else "C"
        lines.extend(
            event_card(
                f"{exp_txt} {ev.get('strike', '?')}{side}",
                ev.get("volume"),
                ev.get("oi_prev"),
                ev.get("open_interest"),
                has_prev_vol=ev.get("volume_prev") is not None,
                last_price=ev.get("last_price"),
                vol_source=ev.get("volume_source"),
            )
        )
    return lines


def _event_differential_lines(
    snapshot: Dict[str, Any],
    event_dates: Optional[List[Dict[str, Any]]],
) -> List[str]:
    from report.highlight import event_differential

    diff = event_differential(snapshot, event_dates)
    if diff is None:
        return []
    return [
        f"📅 事件差分（观察，非因果）: {diff['expiration'][5:]}（{diff['dte']}D）ATM IV "
        f"{diff['covered_iv_pct']:.1f}% vs {diff['control_expiration'][5:]} "
        f"{diff['control_iv_pct']:.1f}%（差 {diff['diff_pp']:+.1f}pp）——覆盖 {diff['events']}",
        "   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）",
        "",
    ]


def _data_quality_line(snapshot: Dict[str, Any]) -> Optional[str]:
    dq = snapshot.get("data_quality") or {}
    if not dq:
        return None
    parts = []
    for k, label in (
        ("market_data", "行情"),
        ("options_structure", "期权结构"),
        ("flow", "流向"),
        ("dealer_mechanism", "做市商机制"),
    ):
        if dq.get(k):
            parts.append(f"{label} {dq[k]}")
    if not parts:
        return None
    return (
        "数据质量: " + " ｜ ".join(parts)
        + " —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。"
    )


def market_block(market: Optional[Dict[str, Any]]) -> List[str]:
    """市场环境块（整份报告只出现一次）。"""
    if not market:
        return []
    ve = market.get("vol_environment")
    if isinstance(ve, dict) and (ve.get("vix") or {}).get("value") is not None:
        lines = ["📊 市场环境", ""]
        parts = []
        if market.get("spy") is not None:
            parts.append(f"SPY ${market['spy']:,.2f}")
        if market.get("qqq") is not None:
            parts.append(f"QQQ ${market['qqq']:,.2f}")
        if parts:
            lines.append(" ｜ ".join(parts))
        v = ve["vix"]
        vix_txt = f"VIX {v['value']:.2f}"
        c1 = v.get("change_1d_pct")
        if c1 is not None:
            arrow = "↑" if c1 >= 0 else "↓"
            vix_txt += f" {arrow}{abs(c1):.1f}%"
        c5 = v.get("change_5d_pct")
        if c5 is not None:
            vix_txt += f"（5D {c5:+.1f}%）"
        label = (ve.get("regime") or {}).get("label")
        if label:
            if label == "INSUFFICIENT_DATA":
                vix_txt += " ｜ Vol Regime: INSUFFICIENT_DATA ⚠️"
            else:
                vix_txt += f" ｜ Vol Regime: {label}"
        lines.append(vix_txt)
        fg = market.get("fg_score")
        fg_rating = market.get("fg_rating")
        if fg is not None:
            lines.append(f"CNN 恐惧贪婪 {fg}{'（' + str(fg_rating) + '）' if fg_rating else ''}")
        lines.append("")
        lines.append("⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。")
        if label == "INSUFFICIENT_DATA":
            lines.append("⚠️ Vol Regime unavailable: rule evaluation incomplete.")
        lines.append("")
        return lines
    m = []
    if market.get("spy") is not None:
        m.append(f"SPY ${market['spy']:,.2f}")
    if market.get("vix") is not None:
        m.append(f"VIX {market['vix']:.2f}")
    fg = market.get("fg_score")
    fg_rating = market.get("fg_rating")
    if fg is not None:
        m.append(f"CNN 恐惧贪婪 {fg}{'（' + str(fg_rating) + '）' if fg_rating else ''}")
    return ["市场背景： " + " ｜ ".join(m), ""] if m else []


def calendar_block(calendar: Optional[List[str]]) -> List[str]:
    """宏观日历块（整份报告只出现一次）。"""
    if not calendar:
        return []
    return ["## 📅 本周重要美国宏观日历（仅【高】，美东时间）"] + list(calendar) + [""]


def _vol_env(snapshot: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    return (snapshot.get("context") or {}).get("vol_environment")


def _day_range(snapshot: Dict[str, Any]) -> Optional[str]:
    """当日高/低（真实数据，随快照保存；缺失则返回 None，不猜测）。"""
    ctx = snapshot.get("context") or {}
    hi = ctx.get("day_high")
    lo = ctx.get("day_low")
    if hi is None or lo is None:
        return None
    try:
        return f" ｜ 今日高 {float(hi):.2f} ｜ 低 {float(lo):.2f}"
    except (TypeError, ValueError):
        return None


def _vix_spread_line(snapshot: Dict[str, Any]) -> Optional[str]:
    """IV–VIX Spread（Proxy）：近月 ATM IV − VIX，只在 Setup 触发时显示。"""
    ctx = snapshot.get("context") or {}
    ve = ctx.get("vol_environment") or {}
    vix = (ve.get("vix") or {}).get("value")
    if vix is None:
        vix = ctx.get("vix")
    atm_iv = (snapshot.get("momentum") or {}).get("atm_iv")
    if atm_iv is None or vix is None:
        return None
    try:
        spread_pp = (float(atm_iv) - float(vix) / 100.0) * 100.0
    except (TypeError, ValueError):
        return None
    return (
        f"   ⇒ IV–VIX Spread: {spread_pp:+.1f}pp*"
        "（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）"
    )


def _fwd_k(v, signed: bool = True) -> str:
    if v is None:
        return "N/A"
    a = abs(float(v))
    if a >= 100:
        sign = "+" if signed and float(v) >= 0 else ""
        return f"{sign}{float(v) / 1000.0:.1f}k"
    sign = "+" if signed and float(v) >= 0 else ""
    return f"{sign}{float(v):.0f}"


def _fwd_money(v) -> str:
    if v is None:
        return "N/A"
    a = abs(float(v))
    if a >= 1e6:
        return f"${float(v) / 1e6:.2f}M"
    if a >= 1e3:
        return f"${float(v) / 1e3:.1f}k"
    return f"${float(v):.0f}"


def _fwd_shares(v) -> str:
    if v is None:
        return "N/A"
    a = abs(float(v))
    if a >= 1e6:
        return f"{float(v) / 1e6:.1f}M shares"
    if a >= 1e3:
        return f"{float(v) / 1e3:.0f}k shares"
    return f"{float(v):.0f} shares"


def _fwd_l2(e: Dict[str, Any]) -> List[str]:
    lines = [f"📆 {e['expiration'][5:]} Forward Structure"]
    lines.append(f"OI:       C {_fwd_k(e.get('call_oi'), signed=False)} / P {_fwd_k(e.get('put_oi'), signed=False)}")
    dline = f"ΔOI:      C {_fwd_k(e.get('call_delta_oi'))} / P {_fwd_k(e.get('put_delta_oi'))}"
    new_txt = []
    if e.get("call_new_oi"):
        new_txt.append(f"C {_fwd_k(e['call_new_oi'], signed=False)}")
    if e.get("put_new_oi"):
        new_txt.append(f"P {_fwd_k(e['put_new_oi'], signed=False)}")
    if new_txt:
        dline += "（含新行权价 " + " / ".join(new_txt) + "）"
    lines.append(dline)
    if e.get("atm_call_price") is not None and e.get("atm_put_price") is not None:
        lines.append(
            f"ATM:      C {fmt(e['atm_call_price'], 2)} / P {fmt(e['atm_put_price'], 2)}"
        )
    if e.get("atm_iv") is not None:
        lines.append(f"ATM IV:   {e['atm_iv'] * 100:.1f}%")
    if e.get("delta_exposure") is not None:
        lines.append(f"ΔOI Δ Exposure*: {_fwd_shares(e['delta_exposure'])}")
    top = e.get("top_delta_oi") or []
    if top:
        lines.append("Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:")
        for t in top:
            dist_txt = f"{t['distance_pct']:+.1f}%" if t.get("distance_pct") is not None else "N/A"
            last_txt = f"${fmt(t['last_price'], 2)}" if t.get("last_price") is not None else "N/A"
            lines.append(
                f"{t['type'][0].upper()} {int(t['strike'])} ｜ {t['delta_oi']:+,} ｜ "
                f"{last_txt} ｜ 名义 {_fwd_money(t.get('notional'))}* ｜ {dist_txt}"
            )
    ref = _fwd_structure_ref(top)
    if ref:
        lines.append(f"结构参考：{ref}（结构观察，非价格预测）")
    lines.append("*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）")
    lines.append("")
    return lines


def _fwd_structure_ref(top: List[Dict[str, Any]]) -> Optional[str]:
    """从 Top ΔOI 提取支撑/压力参考：上方（距现价>0）与下方（<0）各取 ΔOI 最大的正变化行。"""
    pos = [t for t in top if (t.get("delta_oi") or 0) > 0 and t.get("distance_pct") is not None]
    if not pos:
        return None
    above = max((t for t in pos if t["distance_pct"] > 0), key=lambda t: t["delta_oi"], default=None)
    below = max((t for t in pos if t["distance_pct"] < 0), key=lambda t: t["delta_oi"], default=None)
    parts = []
    if above is not None:
        parts.append(f"{int(above['strike'])}（{above['distance_pct']:+.1f}%）上方")
    if below is not None:
        parts.append(f"{int(below['strike'])}（{below['distance_pct']:+.1f}%）下方")
    if not parts:
        return None
    return " / ".join(parts) + "形成 OI 变化集中区"


def _fwd_medium_top(e: Dict[str, Any]) -> Optional[str]:
    """Medium 结算日一行紧凑 Top ΔOI（跨两侧 |ΔOI| 排序，取前 2）。"""
    top = (e.get("top_delta_oi") or [])[:2]
    if not top:
        return None
    parts = [f"{int(t['strike'])}{t['type'][0].upper()} {t['delta_oi']:+,}" for t in top]
    return "   Top ΔOI: " + " ｜ ".join(parts)


def _fwd_l3(e: Dict[str, Any], sig: Dict[str, Any]) -> List[str]:
    lines = ["⚠️ Significant Forward Positioning"]
    lines.append(
        f"{e['expiration'][5:]} / {int(sig['strike'])}{sig['type'][0].upper()}"
    )
    dist_txt = f"{sig['distance_pct']:+.1f}%" if sig.get("distance_pct") is not None else "N/A"
    r1_txt = f"{sig['r1']:.0f}%" if sig.get("r1") is not None else "N/A"
    lines.append(
        f"ΔOI {sig['delta_oi']:+,} ｜ 距现价 {dist_txt} ｜ OI 集中 Top3 ｜ ΔOI/Volume {r1_txt}"
    )
    lines.append("⇒ 该期限/行权价出现显著 OI 变化集中。")
    lines.append("⇒ 买开/卖开方向不可观测（Scenario A/B）。")
    lines.append("⇒ 独立结构观察，不进入 Direction Edge / Gate。")
    lines.append("")
    return lines


def _forward_block(snapshot: Dict[str, Any]) -> List[str]:
    """Forward Expiration Structure（独立观察层）：L1 固定 4 行，L2 仅 High 展开，L3 极端。"""
    fwd = snapshot.get("forward")
    if not isinstance(fwd, dict) or not fwd.get("expirations"):
        return []
    lines = ["📆 Forward Expiration Structure", ""]
    for e in fwd["expirations"]:
        c_txt = _fwd_k(e.get("call_delta_oi"))
        p_txt = _fwd_k(e.get("put_delta_oi"))
        act = e.get("activity") or "LOW"
        mark = " △" if act == "MEDIUM" else ""
        line = (
            f"{e['expiration'][5:]}  C {c_txt} / P {p_txt} ｜ "
            f"Activity {act}{mark} ｜ {e.get('dte', '?')}D"
        )
        if e.get("new_listing"):
            line += "（新上架）"
        else:
            new_txt = []
            if e.get("call_new_oi"):
                new_txt.append(f"C {_fwd_k(e['call_new_oi'], signed=False)}")
            if e.get("put_new_oi"):
                new_txt.append(f"P {_fwd_k(e['put_new_oi'], signed=False)}")
            if new_txt:
                line += "（新行权价 " + " / ".join(new_txt) + "）"
        lines.append(line)
    lines.append("")
    for e in fwd["expirations"]:
        if e.get("activity") == "HIGH":
            lines += _fwd_l2(e)
        elif e.get("activity") == "MEDIUM":
            compact = _fwd_medium_top(e)
            if compact:
                lines.append(compact)
                lines.append("")
    return lines


def ticker_morning(
    snapshot: Dict[str, Any],
    prev_snapshot: Optional[Dict[str, Any]] = None,
    activity: Optional[List[Dict[str, Any]]] = None,
    setup_status: Optional[Dict[str, Any]] = None,
    gex: Optional[float] = None,
    gex_change: Optional[float] = None,
    event_dates: Optional[List[Dict[str, Any]]] = None,
) -> str:
    """单个标的的晨报区块（不含标题/市场/日历）。"""
    ticker = snapshot.get("ticker", "?")
    lines: List[str] = [ticker_heading(ticker)]
    stale_note = None
    if prev_snapshot:
        p = prev_snapshot.get("spot")
        day_open = snapshot.get("day_open")
        c = day_open or snapshot.get("spot")
        ref_label = "今开" if day_open else "今晨"
        chg = (c / p - 1.0) * 100 if (p and c) else None
        lines.append("📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）")
        lines.append(
            f"{ticker}  昨收 {fmt(p, 2)} → {ref_label} {fmt(c, 2)}"
            + (f"（{chg:+.1f}%）" if chg is not None else "")
            + " | 较昨收变动（含盘初走势）"
            + (_day_range(snapshot) or "")
        )
        gap = _trading_gap(prev_snapshot.get("created_at", "")[:10], snapshot.get("created_at", "")[:10])
        if gap >= 1:
            prev_date = prev_snapshot.get("created_at", "")[:10]
            stale_note = (
                f"OI 增仓/异动基于 {prev_date} 快照对比（标的停更 {gap} 个交易日），"
                "前几日数据可能失真，请谨慎解读"
            )
            lines.append(
                f"⚠️ 标的停更 {gap} 个交易日：以下对比基于 {prev_date} 晚报，"
                f"趋势与 OI 增仓指标需 {gap} 个交易日数据恢复"
            )
        lines.append("")
    lines += _options_block(snapshot)
    if setup_status:
        spread = _vix_spread_line(snapshot)
        if spread:
            lines.append(spread)
    lines += _structure_block(snapshot, gex=gex, gex_change=gex_change)
    lines += _structure_interpretation(snapshot)
    lines += _activity_block(activity, stale_note=stale_note)
    lines += _forward_block(snapshot)
    lines += _event_differential_lines(snapshot, event_dates)
    dq_line = _data_quality_line(snapshot)
    if dq_line:
        lines.append(dq_line)
    lines += _setup_block(setup_status, _vol_env(snapshot))
    lines.append("")
    lines.append(f"数据溯源：完整表见附录 / thesis / analytics/daily/{snapshot.get('created_at', '')[:10]}/{ticker}_morning.json")
    return "\n".join(lines)


def render_morning(
    snapshot: Dict[str, Any],
    prev_snapshot: Optional[Dict[str, Any]] = None,
    activity: Optional[List[Dict[str, Any]]] = None,
    setup_status: Optional[Dict[str, Any]] = None,
    gex: Optional[float] = None,
    gex_change: Optional[float] = None,
    reminders: Optional[List[str]] = None,
    calendar: Optional[List[str]] = None,
    market: Optional[Dict[str, Any]] = None,
    event_dates: Optional[List[Dict[str, Any]]] = None,
) -> str:
    date = snapshot.get("created_at", "")[:10]
    lines = [f"# 期权晨报 {date}", ""]
    if market:
        snap_ve = (snapshot.get("context") or {}).get("vol_environment")
        if isinstance(snap_ve, dict):
            market = {**market, "vol_environment": snap_ve}
        lines += market_block(market)
    if calendar:
        lines += calendar_block(calendar)
    from report.highlight import build_highlights, highlights_section

    hl_items = build_highlights(snapshot, activity=activity, prev=prev_snapshot, event_dates=event_dates)
    lines += highlights_section(hl_items)
    if reminders:
        lines += [r for r in reminders if r]
        lines.append("")
    lines.append(
        ticker_morning(
            snapshot, prev_snapshot, activity, setup_status, gex, gex_change, event_dates
        )
    )
    return "\n".join(lines)
