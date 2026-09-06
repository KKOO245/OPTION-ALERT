"""QQQ 期权简报渲染器（v1）。

定位：盘前/盘后精简解读，不替代完整晨报/晚报。
纪律：只呈现快照中已验证字段；方向性语句一律标"观察/候选/研究层"；
不写"负 Gamma = 看跌"类未验证断言。
"""

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple


_SESSION_ZH = {"morning": "晨报简报", "evening": "晚报简报"}


def _parse_created(created: Any) -> Tuple[str, str]:
    """快照 created_at 兼容 US 格式与 ISO 格式；返回 (date_str, ts_text)。"""
    if not created:
        return "", ""
    text = str(created).strip()
    for fmt in ("%m/%d/%Y %H:%M:%S", "%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%d %H:%M:%S"):
        try:
            dt = datetime.strptime(text, fmt)
            return dt.strftime("%Y-%m-%d"), dt.strftime("%Y-%m-%d %H:%M")
        except ValueError:
            continue
    return text[:10], text


def _fmt(v: Any, digits: int = 2, suffix: str = "") -> str:
    if v is None:
        return "N/A"
    try:
        return f"{float(v):,.{digits}f}{suffix}"
    except (TypeError, ValueError):
        return str(v)


def _signed_oi(v: Any, has_prev: bool = True) -> str:
    """ΔOI 显示：正=增仓/负=减仓。方向仅描述持仓变化，不构成行情断言。"""
    if not has_prev or v is None:
        return "N/A"
    try:
        x = float(v)
    except (TypeError, ValueError):
        return "N/A"
    if abs(x) < 500:
        return "0"
    arrow = "↑增" if x > 0 else "↓减"
    return f"{x / 1000:+.1f}k {arrow}"


def _exp_short(exp: str) -> str:
    return exp[5:] if len(exp) >= 10 else exp


def _one_line(snap: Dict[str, Any]) -> str:
    loc = snap.get("location") or {}
    spot = snap.get("spot")
    flip = loc.get("flip_primary")
    cw = loc.get("call_wall")
    pw = loc.get("put_wall")
    gamma = (snap.get("regime") or {}).get("gamma", "UNKNOWN")
    parts = []
    if spot is not None:
        parts.append(f"现价 {spot:.2f}")
    if flip is not None:
        parts.append(f"Primary Flip {flip:.2f}（决策位）")
    if gamma in ("POSITIVE", "NEGATIVE", "UNKNOWN"):
        parts.append(f"Gamma {gamma}")
    seg = "｜".join(parts) if parts else "关键结构位数据不足"
    if flip is not None and spot is not None:
        if spot >= flip:
            seg += f" → 上方焦点 {_fmt(cw, 0)} Call Wall" if cw else ""
        else:
            seg += f" → 下方焦点 {_fmt(pw, 0)} Put Wall" if pw else ""
    return f"一句话：{seg}。本简报为盘前/盘后风险提醒，不构成交易建议。"


def _expiration_clock(snap: Dict[str, Any], session: str = "morning") -> List[str]:
    """③ 到期钟：未来 4 个到期档，标注 ΔOI 增减（持仓净变化，非方向结论）。"""
    exps = ((snap.get("forward") or {}).get("expirations")) or []
    if not exps:
        return ["③ 到期钟：数据不足"]
    out = ["③ EXPIRATION CLOCK（未来 4 档｜ΔOI = 跨快照 OI 净变化）", ""]
    out.append("到期日   DTE  ExpMove  ATM IV   Put ΔOI      Call ΔOI")
    all_zero = True
    for e in exps[:4]:
        dte = e.get("dte")
        em = e.get("expmove_pct")
        iv = e.get("atm_iv")
        em_txt = f"{float(em):.1f}%" if em is not None else "N/A"  # 快照单位为百分数
        iv_txt = f"{float(iv) * 100:.1f}%" if iv is not None else "N/A"
        poi = _signed_oi(e.get("put_delta_oi"), e.get("has_prev", True))
        coi = _signed_oi(e.get("call_delta_oi"), e.get("has_prev", True))
        if poi != "0" or coi != "0":
            all_zero = False
        out.append(
            f"{_exp_short(str(e.get('expiration','')))}   "
            f"{str(dte):>3}  {em_txt:>6}  {iv_txt:>6}   "
            f"{poi:>12}   {coi:>12}"
        )
    out.append("")
    basis = (
        "ΔOI = 前一交易日 OI 终值 vs 再前一日（跨日链快照真实净变化，已抽样核对）"
        if session == "morning"
        else "ΔOI = 晚报快照 vs 当日晨报快照"
    )
    out.append(f"解读：{basis}。增/减是净变化，无法拆分开仓/平仓构成，不做方向推导。")
    if all_zero:
        out.append("注：ΔOI 全为 0 通常表示晚报时点 OI 终值尚未更新，非真实无变化。")
    return out


def _map_row(price_txt: str, label: str, spot: bool = False) -> str:
    """结构图行：标签列对齐（价格 + 空格 + 线至第 11 列 + 空格 + 标签）；Spot 行 ● 落在线上。"""
    sep_len = max(2, 10 - len(price_txt))
    if spot:
        n1 = (sep_len - 1) // 2
        sep = "─" * n1 + "●" + "─" * (sep_len - 1 - n1)
    else:
        sep = "─" * sep_len
    return f"{price_txt} {sep} {label}"


def _structural_map(snap: Dict[str, Any]) -> List[str]:
    """④ 结构图：单列价格地图，只记位置，不构成支撑/压力断言。"""
    loc = snap.get("location") or {}
    spot = snap.get("spot")
    ctx = snap.get("context") or {}
    rows: List[Tuple[float, str, str]] = []  # (price, kind, label)

    cw, pw = loc.get("call_wall"), loc.get("put_wall")
    if cw is not None:
        cls = loc.get("call_wall_class")
        tag = "（WEAK）" if cls == "WEAK" else ""
        rows.append((float(cw), "cw", f"Call Wall{tag}"))
    flip = loc.get("flip_primary")
    if flip is not None:
        rows.append((float(flip), "flip", "Primary Flip（决策位）"))
    if pw is not None:
        cls = loc.get("put_wall_class")
        tag = "（WEAK）" if cls == "WEAK" else ""
        rows.append((float(pw), "pw", f"Put Wall{tag}"))

    # ExpMove 下沿：最近到期档，作为"当日波动下沿"位置参考
    exps = ((snap.get("forward") or {}).get("expirations")) or []
    if exps and spot is not None:
        e0 = exps[0]
        em = e0.get("expmove_pct")
        if em is not None:
            lo = spot * (1.0 - float(em) / 100.0)
            rows.append((lo, "exp", f"ExpMove 下沿（{_exp_short(str(e0.get('expiration','')))}）"))

    # 集中位（观察）：避免与墙重复
    conc = loc.get("concentration") or []
    added = {r[0] for r in rows}
    seen = 0
    for item in conc:
        if seen >= 2:
            break
        try:
            strike = float(item.get("strike"))
            typ = item.get("type")
        except (TypeError, ValueError):
            continue
        if strike in added or (spot is not None and abs(strike / spot - 1.0) > 0.09):
            continue
        if typ == "put" and strike < (spot if spot is not None else 1e9):
            label = "Put 集中（全档聚合·观察）"
        elif typ == "call" and strike > (spot if spot is not None else 0):
            label = "Call 集中（全档聚合·观察）"
        else:
            continue
        rows.append((strike, "conc", label))
        added.add(strike)
        seen += 1

    if spot is not None:
        rows.append((float(spot), "spot", f"Spot {spot:.2f}"))

    rows.sort(key=lambda r: r[0], reverse=True)
    # 合并同价位行（如 spot 与 flip 重合）
    merged: List[Tuple[float, str, List[str]]] = []
    for price, kind, label in rows:
        if merged and abs(merged[-1][0] - price) < 1e-9:
            merged[-1][2].append(label)
        else:
            merged.append((price, kind, [label]))

    text_rows: List[str] = []
    for price, kind, labels in merged:
        if kind == "spot":
            text_rows.append(_map_row(f"{price:.2f}", " ｜ ".join(labels), spot=True))
        else:
            txt = f"{price:.2f}" if abs(price - round(price)) > 0.001 else f"{int(round(price))}"
            text_rows.append(_map_row(txt, " ｜ ".join(labels)))

    out = ["④ STRUCTURAL MAP（只记位置｜WEAK=弱结构）", "```"]
    out += text_rows
    if ctx.get("max_pain") is not None:
        mp = ctx.get("max_pain")
        pos = "现价下方" if (spot is not None and mp <= spot) else "现价上方"
        out.append(f"MaxPain {_fmt(mp, 0)}（{pos}，仅结算参考）")
    out.append("```")
    out.append("失效规则：到期后该档集中位消失，结构位需按新到期档重看；"
               "集中行 = 全部到期档聚合（未按到期细分）。")
    return out


def _nearest_above_below(spot: float, levels: List[float]) -> Tuple[Optional[float], Optional[float]]:
    above = [l for l in levels if l > spot]
    below = [l for l in levels if l < spot]
    return (min(above) if above else None, max(below) if below else None)


def _conditional_path(snap: Dict[str, Any]) -> List[str]:
    """⑤ 条件路径：一句话触发式，不做方向预测。"""
    loc = snap.get("location") or {}
    spot = snap.get("spot")
    if spot is None:
        return ["⑤ 条件路径：现价缺失，跳过"]
    flip = loc.get("flip_primary")
    cw = loc.get("call_wall")
    pw = loc.get("put_wall")
    cands = [l for l in (flip, cw, pw) if l is not None]
    if not cands:
        return ["⑤ 条件路径：结构位缺失，跳过"]
    above, below = _nearest_above_below(float(spot), [float(l) for l in cands])
    lines = ["⑤ CONDITIONAL PATH"]
    if above is not None:
        name = "Primary Flip" if flip is not None and abs(float(flip) - above) < 1e-9 else "上方结构位"
        lines.append(f"IF 站上 {above:.2f}（{name}）→ 上方观察 {_fmt(cw, 0)} Call Wall / 更高集中位。")
    if below is not None:
        name = "Primary Flip" if flip is not None and abs(float(flip) - below) < 1e-9 else "下方结构位"
        lines.append(f"IF 跌破 {below:.2f}（{name}）→ 下方观察 {_fmt(pw, 0)} Put Wall / 更低集中位。")
    lines.append("判定口径：以收盘/稳定站上为准；盘中瞬时触线只算警报，不算确认。")
    return lines


def _risk_items(snap: Dict[str, Any]) -> List[str]:
    """风险/机会提醒（候选观察，全部标注置信边界）。"""
    items: List[str] = []
    ctx = snap.get("context") or {}
    p3 = snap.get("p3") or {}
    gex = (p3.get("gex") or {}).get("net_gex")
    gamma = (snap.get("regime") or {}).get("gamma", "UNKNOWN")
    exps = ((snap.get("forward") or {}).get("expirations")) or []

    gex_txt = f"｜GEX(存量) {float(gex) / 1e6:+.0f}M" if gex is not None else ""
    if gamma == "NEGATIVE":
        items.append(
            f"Gamma Regime: NEGATIVE（模型分类）{gex_txt}——负 Gamma 的波动放大已回测验证，"
            "只说明幅度风险，不构成方向理由。"
        )
    elif gamma == "POSITIVE":
        items.append(
            f"Gamma Regime: POSITIVE（模型分类）{gex_txt}——仅标注结构，"
            "正 Gamma 的波动抑制未做等价验证，不作断言。"
        )
    else:
        items.append(f"Gamma Regime: {gamma}{gex_txt}（模型分类，研究层）。")

    vix = (ctx.get("vol_environment") or {}).get("vix") if isinstance(ctx.get("vol_environment"), dict) else None
    if isinstance(vix, dict) and vix.get("value") is not None:
        chg = vix.get("change_1d_pct")
        chg_txt = f"（1d {float(chg):+.1f}%）" if chg is not None else ""
        items.append(f"VIX {float(vix['value']):.1f}{chg_txt}：仅标注波动环境，不做方向解读。")

    # ΔOI 最大异动（候选观察）
    biggest: List[Tuple[float, str, Any]] = []
    for e in exps[:4]:
        for key, side in (("put_delta_oi", "Put"), ("call_delta_oi", "Call")):
            v = e.get(key)
            if v is not None and abs(float(v)) >= 5000:
                biggest.append((abs(float(v)), side, e))
    biggest.sort(reverse=True)
    for _, side, e in biggest[:2]:
        v = float(e.get("put_delta_oi" if side == "Put" else "call_delta_oi"))
        action = "增仓" if v > 0 else "减仓"
        exp = _exp_short(str(e.get("expiration", "")))
        items.append(
            f"{exp} {side} {action}（{_signed_oi(v)}）：仓位变化观察——"
            "OI 净变化无法拆分开/平仓构成；仅候选信号，不做方向推导。"
        )

    if exps and exps[0].get("dte") is not None:
        dte = int(exps[0].get("dte"))
        if dte <= 7:
            exp = _exp_short(str(exps[0].get("expiration", "")))
            items.append(f"近期到期 {exp}（剩 {dte} 个交易日）：该档集中位到期后消失，结构参考需迁移。")

    mp = ctx.get("max_pain")
    if mp is not None:
        items.append(f"MaxPain {_fmt(mp, 0)}：结算引力参考，不构成支撑/压力断言。")

    if len(items) > 6:
        items = items[:6]
    out = ["⚠️ 风险 / 机会（候选观察）"]
    out += [f"- {x}" for x in items] if items else ["- 今日无显著异动项（机械检查）。"]
    return out


def render_brief(snap: Dict[str, Any], session: str = "morning", ticker: str = "QQQ") -> str:
    """渲染单标的简报。snap 为 SnapshotStore.load() 返回的 dict。"""
    date_str, ts = _parse_created(snap.get("created_at"))
    sess_zh = _SESSION_ZH.get(session, session)
    head = f"# 📋 {ticker} 期权简报（{sess_zh}）{date_str}".rstrip()
    lines = [head, f"数据时点：{ts}｜来源 {snap.get('source', 'N/A')}", ""]
    lines.append(_one_line(snap))
    lines.append("")
    lines += _expiration_clock(snap, session=session)
    lines.append("")
    lines += _structural_map(snap)
    lines.append("")
    lines += _conditional_path(snap)
    lines.append("")
    lines += _risk_items(snap)
    lines.append("")
    lines.append("— 完整版晨报/晚报仍在原频道推送；本简报仅作提醒，不构成投资建议。")
    return "\n".join(lines)


if __name__ == "__main__":  # 本地自检入口：python report/brief.py <snapshot.json> [morning|evening]
    import json
    import sys

    path = sys.argv[1] if len(sys.argv) > 1 else ""
    session = sys.argv[2] if len(sys.argv) > 2 else "morning"
    with open(path, encoding="utf-8") as f:
        print(render_brief(json.load(f), session=session))
