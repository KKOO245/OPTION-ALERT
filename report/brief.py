"""QQQ 期权简报渲染器（v1）。

定位：盘前/盘后精简解读，不替代完整晨报/晚报。
纪律：只呈现快照中已验证字段；方向性语句一律标"观察/候选/研究层"；
不写"负 Gamma = 看跌"类未验证断言。
"""

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple


_SESSION_ZH = {"morning": "晨报简报", "evening": "晚报简报"}

# 负 Gamma 波动放大 / 方向 edge 的 15 年回测（3 个交易日，来源 work/summary_backtest*.py）
_BACKTEST = {
    "QQQ": {"lo": 2011, "hi": 2025, "n": 1929, "abs_neg": 1.95, "abs_pos": 1.19,
            "med_neg": 0.47, "up_neg": 59.3},
    "SPY": {"lo": 2008, "hi": 2025, "n": 2517, "abs_neg": 1.73, "abs_pos": 0.96,
            "med_neg": 0.33, "up_neg": 57.6},
}


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


def _risk_opportunity(
    snap: Dict[str, Any], session: str = "morning", ticker: str = "QQQ"
) -> List[str]:
    """🔴 风险 / 🟢 机会：结论行（规则层）。

    每条 = 加粗触发点 + 冒号 + 怎么看 + 括号标注认知状态。
    只用快照已验证字段；宏观事件名只在日历层提供时写入，绝不编造。
    """
    loc = snap.get("location") or {}
    spot = snap.get("spot")
    flip = loc.get("flip_primary")
    cw, pw = loc.get("call_wall"), loc.get("put_wall")
    gamma = (snap.get("regime") or {}).get("gamma", "UNKNOWN")
    gex = ((snap.get("p3") or {}).get("gex") or {}).get("net_gex")
    ctx = snap.get("context") or {}
    mp = ctx.get("max_pain")
    exps = ((snap.get("forward") or {}).get("expirations")) or []
    lines: List[str] = []

    # 1) 状态句：Regime + 相对 Flip + 最近防守
    if gamma == "NEGATIVE" and spot is not None and flip is not None:
        side = "下方" if spot < flip else "上方"
        ref = f"{pw:.0f} Put Wall" if (pw and spot is not None and pw <= spot) else (f"{cw:.0f} Call Wall" if cw else "结构位")
        st = _BACKTEST.get(ticker.upper())
        if gex is not None and float(gex) < 0:
            if st:
                ev = (
                    f"；同一样本不支持下行方向 edge（3日中位 +{st['med_neg']:.2f}%、"
                    f"上涨率 {st['up_neg']:.0f}%）（{ticker.upper()} {st['lo']}-{st['hi']} 回测，"
                    f"|3日| ≈{st['abs_neg']:.2f}% vs 正 Gamma {st['abs_pos']:.2f}%"
                    f"；最近防守看 {ref}）"
                )
                claim = "负 Gamma（GEX<0）的波动放大已回测验证——只说明幅度风险，不预设方向"
            else:
                ev = f"；最近防守看 {ref}"
                claim = (
                    f"负 Gamma（GEX<0）波动放大为 QQQ/SPY 回测结论——{ticker.upper()} "
                    "无同口径 15 年历史，未验证（观察）"
                )
            lines.append(
                f"🔴 **Regime NEGATIVE + GEX {float(gex) / 1e6:+.0f}M + 现价 {spot:.2f} 在 Flip {flip:.2f} {side}**："
                f"{claim}{ev}。"
            )
        else:
            gex_txt = f"GEX {float(gex) / 1e6:+.0f}M" if gex is not None else "GEX 不可用"
            lines.append(
                f"🔴 **Regime 标签 NEGATIVE 但 {gex_txt}**：模型标签与 GEX 数值口径不一致——"
                "只作状态标注，不引用'波动放大已验证'结论（研究层，需口径统一后再启用）。"
            )
    elif gamma == "POSITIVE" and spot is not None and flip is not None:
        side = "上方" if spot >= flip else "下方"
        st = _BACKTEST.get(ticker.upper())
        if st:
            claim = (
                f"正 Gamma 样本的历史波动中枢低于负 Gamma（|3日| {st['abs_pos']:.2f}% vs "
                f"{st['abs_neg']:.2f}%，{st['lo']}-{st['hi']} 回测）——环境级统计，不是当日断言，更不是看涨理由"
            )
        else:
            claim = (
                f"正 Gamma：{ticker.upper()} 无同口径 15 年历史回测，仅作状态标注，不作波动或方向断言"
            )
        lines.append(
            f"🟢 **Regime POSITIVE + 现价 {spot:.2f} 在 Flip {flip:.2f} {side}（条件句）**："
            f"{claim}。"
        )

    # 2) 结构锚 / IV 凸起（未来四档）
    def oi_sum(e) -> float:
        return float(e.get("call_oi") or 0) + float(e.get("put_oi") or 0)

    if len(exps) >= 3:
        total = sum(oi_sum(e) for e in exps[:4])
        main = max(exps[:4], key=oi_sum)
        ivs = [(float(e.get("atm_iv") or 0), e) for e in exps[:4] if e.get("atm_iv")]
        if total > 0 and oi_sum(main) / total >= 0.3:
            exp_txt = _exp_short(str(main.get("expiration", "")))
            ck = float(main.get("call_oi") or 0) / 1000
            pk = float(main.get("put_oi") or 0) / 1000
            lines.append(
                f"🟢 **结构锚 {exp_txt}（C {ck:.0f}k / P {pk:.0f}k，"
                f"占四档 {oi_sum(main) / total * 100:.0f}%）**：未来 {main.get('dte')} 个交易日的"
                "Gamma/对冲结构由它主导——该档到期前，其余档墙位权重较低"
                "（OI 存量事实，非预测）。"
            )
        if len(ivs) >= 3:
            hi = max(ivs, key=lambda x: x[0])
            near = min(ivs, key=lambda x: x[1].get("expiration", ""))
            far = max(ivs, key=lambda x: x[1].get("expiration", ""))
            if hi[0] > near[0] and hi[0] > far[0] and hi[0] - far[0] >= 0.01:
                lines.append(
                    f"🔴 **IV 凸起：近端 {near[0]*100:.1f}% → {_exp_short(str(hi[1].get('expiration','')))} "
                    f"{hi[0]*100:.1f}% → 远端 {far[0]*100:.1f}%**：最大不确定性已被定价在 "
                    f"{_exp_short(str(hi[1].get('expiration','')))}——今天追任何方向都买在贵的位置"
                    "（期限结构事实，不点事件名）。"
                )

    # 3) ΔOI flow：晨报有真实终值；晚报给信息缺口
    if session == "morning":
        flow = []
        for e in exps[:4]:
            exp_txt = _exp_short(str(e.get("expiration", "")))
            dp = e.get("put_delta_oi")
            dc = e.get("call_delta_oi")
            if dp is not None and abs(float(dp)) >= 5000:
                flow.append(f"{exp_txt} Put {float(dp) / 1000:+.1f}k")
            if dc is not None and abs(float(dc)) >= 5000:
                flow.append(f"{exp_txt} Call {float(dc) / 1000:+.1f}k")
        if flow:
            lines.append(
                f"🔴 **flow 异动：{'、'.join(flow[:2])}**：OI 净变化已确认（跨日链快照），"
                "但无法拆分开/平仓——若 IV 未同步走强，属'换手候选'而非'新开仓确认'"
                "（待次日验证）。"
            )
    elif session == "evening":
        lines.append(
            "🔴 **信息缺口：今晚 OI 终值未更新（ΔOI 全 0）**：仓位增减/换手信号明早晨报才可读"
            "——勿把 0 当无变化（数据时序，非结论）。"
        )

    # 4) 到期 + MaxPain
    if (
        exps
        and exps[0].get("dte") is not None
        and int(exps[0].get("dte")) <= 1
        and mp is not None
        and spot is not None
    ):
        exp_txt = _exp_short(str(exps[0].get("expiration", "")))
        pos = "下方" if mp <= spot else "上方"
        lines.append(
            f"🔴 **明日 {exp_txt} 到期 + MaxPain {mp:.0f} 在现价{pos}**：结算磁吸{pos}与集中位失效叠加，"
            "结构参考将快速迁移到下一档（仅结算机制参考，不作方向）。"
        )

    # 5) 机会雷达（固定占位；Setup/事件窗口由上层日历层接入）
    lines.append(
        "🟢 **机会雷达：空**。规则层无 Setup 触发；事件窗口/宏观叙事需日历层接入"
        "（固定占位，非结论）。"
    )
    return lines[:6]


def _fmt_k(v: Any) -> str:
    try:
        return f"{float(v) / 1000:.1f}k"
    except (TypeError, ValueError):
        return "N/A"


def _zero_dte_lines(zero: Optional[Dict[str, Any]], spot: Any) -> List[str]:
    """0DTE（今日到期）区块：规模、近端集中、ATM 隐含波动。仅事实 + 机制参考。"""
    if not zero:
        return []
    rows = zero.get("rows") or []
    if not rows and not (zero.get("C") or zero.get("P")):
        return []
    best: Dict[Tuple[float, str], Dict[str, Any]] = {}
    for r in rows:
        key = (float(r["s"]), str(r["right"]))
        if r["oi"] > best.get(key, {}).get("oi", -1):
            best[key] = r
    ck = float(zero.get("C") or 0)
    pk = float(zero.get("P") or 0)
    ratio = (pk / ck) if ck else None
    lines = ["## ⏱ 0DTE（今日到期）"]
    scale = f"C {_fmt_k(ck)} / P {_fmt_k(pk)}" + (f"（P/C {ratio:.2f}）" if ratio else "")
    lines.append(f"- **规模：{scale}**——当日到期的 Gamma/钉住行为由该档主导（OI 存量事实）。")
    if spot:
        def _top(right: str) -> str:
            items = sorted(
                (v for v in best.values() if v["right"] == right),
                key=lambda x: x["oi"], reverse=True,
            )[:2]
            return " / ".join(
                f"{x['s']:.0f}（{_fmt_k(x['oi'])}，{100 * (x['s'] / float(spot) - 1):+.0f}%）"
                for x in items
            ) or "无"

        lines.append(
            f"- **近端集中（±15%）：Put {_top('PUT')}｜Call {_top('CALL')}**"
            "——当日盘中参考位（位置观察，非预测）。"
        )
        strikes = sorted({k[0] for k in best}, key=lambda s: abs(s / float(spot) - 1))[:3]
        for s in strikes:
            c = best.get((s, "CALL"))
            p = best.get((s, "PUT"))
            if c and p and c.get("mid") and p.get("mid"):
                imp = (float(c["mid"]) + float(p["mid"])) / float(spot) * 100
                ivs = [float(x["iv"]) for x in (c, p) if x.get("iv")]
                iv_txt = f"｜ATM IV {sum(ivs) / len(ivs) * 100:.1f}%" if ivs else ""
                lines.append(
                    f"- **ATM {s:.0f}｜Straddle 隐含波动 ±{imp:.2f}%{iv_txt}**"
                    "——当日波动定价（事实；不构成方向）。"
                )
                break
    lines.append("- 到期后失效：上述 0DTE 集中位今日收盘后全部失效（机制参考）。")
    return lines


# 近档 P/C OI 历史分位（20/80）与同状态 3 日方向统计（QQQ/SPY，2011-2025 / 2008-2025）
_PCR_STATS = {
    "QQQ": {"lo": 1.28, "hi": 2.06, "lo_mean": 0.35, "lo_n": 741, "hi_mean": 0.17, "hi_era_ok": False},
    "SPY": {"lo": 1.45, "hi": 2.31, "lo_mean": 0.26, "lo_n": 820, "hi_mean": 0.15, "hi_era_ok": True},
}


def _signal_layer(
    snap: Dict[str, Any], chain: Optional[Dict[str, Any]], ticker: str
) -> List[str]:
    """📶 信号层：环境/结构/事件三层，全部标"建议，非指令"，含证据与置信度。"""
    t = ticker.upper()
    exps = ((snap.get("forward") or {}).get("expirations")) or []
    lines = ["## 📶 信号层（建议，非指令）"]

    # 环境层：GEX 波动（已验证）
    gex = ((snap.get("p3") or {}).get("gex") or {}).get("net_gex")
    st = _BACKTEST.get(t)
    if gex is not None and float(gex) < 0:
        if st:
            lines.append(
                f"- **环境层（已验证）**：GEX<0 → 波动放大（{t} {st['lo']}-{st['hi']} 回测 |3日| "
                f"{st['abs_neg']:.2f}% vs 正 Gamma {st['abs_pos']:.2f}%）；无下行方向 edge。"
                "建议：只调整仓位/结构，不据此做空。"
            )
        else:
            lines.append(
                "- **环境层（本标的未验证）**：GEX<0 的波动放大结论仅来自 QQQ/SPY 回测，"
                f"{t} 无同口径历史——建议仅作风险提示。"
            )
    else:
        lines.append("- **环境层**：GEX≥0 或数值不可用——波动放大结论不适用，无环境信号。")
    # 结构层：近档 P/C OI 分位（跨标的验证过的唯一方向倾向）
    info = (chain or {}).get(str(exps[0].get("expiration"))) if exps else None
    if info and info.get("seq"):
        last = info["seq"][-1]
        ck, pk = float(last.get("C") or 0), float(last.get("P") or 0)
        pst = _PCR_STATS.get(t)
        if ck > 0 and pst:
            pcr = pk / ck
            if pcr <= pst["lo"]:
                lines.append(
                    f"- **结构层（已验证，跨标的）**：近档 P/C OI {pcr:.2f} ≤ 20 分位 "
                    f"{pst['lo']}（call-heavy）→ 历史同状态 3 日均值 {pst['lo_mean']:+.2f}%"
                    f"（N={pst['lo_n']}，CI 不含 0，效应小、非因果）——建议：偏多倾向，低置信。"
                )
            elif pcr >= pst["hi"]:
                era = "时代一致" if pst["hi_era_ok"] else "时代不一致"
                lines.append(
                    f"- **结构层（观察）**：近档 P/C OI {pcr:.2f} ≥ 80 分位 {pst['hi']}"
                    f"（put-heavy）→ 历史 3 日均值 {pst['hi_mean']:+.2f}% 但 {era}——"
                    "不足以作为方向信号（不作建议）。"
                )
            else:
                lines.append(
                    f"- **结构层**：近档 P/C OI {pcr:.2f} 位于历史中段（20/80 分位 "
                    f"{pst['lo']}/{pst['hi']}）——无结构化方向信号。"
                )
        elif ck > 0:
            lines.append(
                f"- **结构层（未验证）**：近档 P/C OI {pk/ck:.2f}；{t} 无同口径历史分位，"
                "仅作结构观察，不给方向建议。"
            )
    # 事件层：0DTE / OI 轨迹（候选，未验证）
    zero = (chain or {}).get("_0dte")
    if zero and (zero.get("C") or zero.get("P")):
        lines.append(
            "- **事件层（候选，未验证）**：0DTE 规模与近端 OI 见上方 ⏱ 区块——"
            "到期日钉住/磁吸属机制参考，未做历史验证，不建议据此下单。"
        )
    lines.append("- 以上为建议性信号（含置信度与证据），不是指令；决定权在你。")
    return lines


def _exp_interpretation(e: Dict[str, Any], ds: List[float], spot: Any) -> str:
    """单档解读句：全部基于已给字段，方向性一律带观察/机制标签。"""
    pk = float(e.get("put_oi") or 0)
    ck = float(e.get("call_oi") or 0)
    dte = e.get("dte")
    pw = (e.get("put_wall") or {}).get("strike")
    cw = (e.get("call_wall") or {}).get("strike")
    if dte is not None and int(dte) <= 2 and ck > 0 and pk / ck >= 2.0:
        return (
            f"明日到期 + P/C OI {pk / ck:.2f}——该档 Gamma/磁吸集中，"
            "上述 MaxPain/集中位在到期后失效（OI 存量事实 + 到期机制参考，不作方向预测）。"
        )
    if len(ds) >= 2 and ds[-1] > 0 and ds[-2] < 0:
        return (
            "减仓后回补——拥挤度回到峰值附近；若下一入账日续增则趋势成立，"
            "若回落则前次只是事件前对冲（待验证，非结论）。"
        )
    if ds:
        net = sum(ds)
        if abs(net) / 1000 >= 10:
            side = "增厚" if net > 0 else "去化"
            return f"该档 put 仓位近端整体{side}（净 {net / 1000:+.1f}k）——观察是否与 IV 同向（待验证）。"
    ref = pw or cw
    if ref and spot is not None:
        side = "上方" if float(ref) >= float(spot) else "下方"
        return f"档内第一结构参考 {_fmt(ref, 0)} 在现价{side}——观察线（位置参考，非预测）。"
    return "仓位与波动结构并存，方向需 flow + IV 双侧确认（观察项）。"


def _feature_picks(
    exps: List[Dict[str, Any]], forced: List[str] | None = None
) -> List[Tuple[Dict[str, Any], str]]:
    """四档专题的档位选择（透明规则）：强制确认档优先 > R1 最近到期 > R2 OI 锚 > R3 PRIMARY。"""
    forced = forced or []

    def oi_total(e) -> float:
        return float(e.get("call_oi") or 0) + float(e.get("put_oi") or 0)

    picks: List[Tuple[Dict[str, Any], str]] = []
    for f in forced:
        for e in exps:
            if str(e.get("expiration", "")) == f:
                picks.append((e, "上日候选确认（升级置顶）"))
                break
    for e in exps:
        if e.get("dte") is not None and int(e.get("dte")) <= 2:
            if not any(e is x for x, _ in picks):
                picks.append((e, "最近到期（Gamma/磁吸窗口）"))
            break
    anchor = max(exps, key=oi_total)
    if not any(e is anchor for e, _ in picks):
        picks.append((anchor, "四档总 OI 最大（结构锚）"))
    for e in exps:
        if any(e is x for x, _ in picks):
            continue
        cls_c = (e.get("call_wall") or {}).get("class")
        cls_p = (e.get("put_wall") or {}).get("class")
        if cls_c == "PRIMARY" or cls_p == "PRIMARY":
            picks.append((e, "含 PRIMARY 墙位（全链重定价确认位）"))
            break
    return picks[:3]


def _pending_signals(
    snap: Dict[str, Any],
    chain: Optional[Dict[str, Any]],
    session: str,
    ticker: str,
    force_exps: Optional[List[str]] = None,
) -> List[Dict[str, Any]]:
    """提取"待兑现"条件：减仓后回补的档，若下一入账日续增则趋势成立。"""
    if not chain:
        return []
    exps = ((snap.get("forward") or {}).get("expirations")) or []
    signals = []
    for e, _reason in _feature_picks(exps, forced=force_exps):
        info = chain.get(str(e.get("expiration", ""))) or {}
        raw_seq = info.get("seq") or []
        seq: List[Dict[str, Any]] = []
        prev = None
        for x in raw_seq:
            if prev is not None and float(x["C"]) == float(prev["C"]) and float(x["P"]) == float(prev["P"]):
                continue
            seq.append(x)
            prev = x
        if len(seq) >= 2:
            vals = [float(x["P"]) for x in seq]
            ds = [vals[i + 1] - vals[i] for i in range(len(vals) - 1)]
            if len(ds) >= 2 and ds[-1] > 0 and ds[-2] < 0:
                exp = str(e.get("expiration", ""))
                signals.append({
                    "ticker": ticker,
                    "expiry": exp,
                    "kind": "put_reclaim_continuation",
                    "created": (snap.get("created_at") or "")[:10],
                    "chain_date": str(seq[-1]["date"]),
                    "last_delta": ds[-1],
                    "expect": "increase",
                })
    return signals


def _eval_prior_signals(
    snap: Dict[str, Any],
    chain: Optional[Dict[str, Any]],
    prior_state: Optional[Dict[str, Any]],
    ticker: str,
) -> Tuple[List[str], List[str], List[str]]:
    """检查上日待确认条件。返回 (提示行, 已结算的 key, 应置顶的到期档)。"""
    if not prior_state or not chain:
        return [], [], []
    lines: List[str] = []
    resolved: List[str] = []
    confirmed: List[str] = []
    for key, st in (prior_state.get("signals") or {}).items():
        if st.get("ticker") != ticker:
            continue
        exp = st.get("expiry")
        info = chain.get(exp) or {}
        seq = info.get("seq") or []
        base_date = st.get("chain_date")
        base_val = None
        idx_base = None
        for i, x in enumerate(seq):
            if str(x["date"]) == base_date:
                base_val = float(x["P"])
                idx_base = i
                break
        if base_val is None or idx_base is None:
            continue
        nxt = None
        for x in seq[idx_base + 1:]:
            if float(x["P"]) != base_val:
                nxt = x
                break
        if nxt is None:
            continue  # 数据未到，保持待定
        d = float(nxt["P"]) - base_val
        resolved.append(key)
        exp_txt = _exp_short(exp)
        if st.get("expect") == "increase" and d > 0:
            confirmed.append(exp)
            lines.append(
                f"⚠️ **上日候选确认：{exp_txt} Put 续增 {d / 1000:+.1f}k"
                f"（{base_date} → {nxt['date']}）**——'减仓后回补'升级为连续增仓观察重点；"
                "仍属仓位观察，需 IV 同向才算情绪确认（非方向）。"
            )
        else:
            lines.append(
                f"⚠️ **上日候选证伪：{exp_txt} Put 未续增（{d / 1000:+.1f}k）**——"
                "前次增仓维持'事件对冲'解释，降级观察（非方向）。"
            )
    return lines, resolved, confirmed


def _expiry_trend_lines(
    snap: Dict[str, Any],
    chain: Optional[Dict[str, Any]],
    session: str = "morning",
    force_exps: Optional[List[str]] = None,
) -> List[str]:
    """四档专题：per-expiry 结构 + 跨日 OI 轨迹（chain_history 提供的分析行）。

    选中规则（透明、可审计）：
      R1 最近到期档（dte<=2）：Gamma/磁吸窗口；
      R2 四档总 OI 最大档：结构锚；
      R3 含 PRIMARY 墙位的档（未选中时补入）：该档存在全链重定价确认的关键位。
    输出中每行标注选中依据。
    """
    if not chain:
        return []
    exps = ((snap.get("forward") or {}).get("expirations")) or []
    spot = snap.get("spot")
    if not exps:
        return []

    def oi_total(e) -> float:
        return float(e.get("call_oi") or 0) + float(e.get("put_oi") or 0)

    picks = _feature_picks(exps, forced=force_exps)

    def _concentration_txt(
        e: Dict[str, Any], info: Dict[str, Any], spot_v: Any
    ) -> Tuple[str, str]:
        """返回 (补充说明, 集中 strike 文本)。

        规则：近端集中 = 距现价 ±12% 带内 OI 最大 strike（真正的结构参考）；
        带外的巨量 OI 单列为"深虚值尾部"（保护/彩票盘，不是近端结构位）。
        """
        cw = e.get("call_wall") or {}
        pw = e.get("put_wall") or {}
        top_p = info.get("topP") or []
        top_c = info.get("topC") or []
        notes = []
        if not pw.get("strike"):
            notes.append("PW 无（wall_quality_v1 阈值未达标）")
        if not cw.get("strike"):
            notes.append("CW 无（wall_quality_v1 阈值未达标）")
        band = 0.12

        def _tag(items):
            return " / ".join(
                f"{_fmt(x['s'], 0)}（{_fmt_k(x['oi'])}，"
                f"{100 * (float(x['s']) / float(spot_v) - 1):+.0f}%）"
                for x in items
            )

        conc = []
        if spot_v:
            near_p = [x for x in top_p if abs(float(x["s"]) / float(spot_v) - 1) <= band][:2]
            near_c = [x for x in top_c if abs(float(x["s"]) / float(spot_v) - 1) <= band][:2]
            far_p = [x for x in top_p if abs(float(x["s"]) / float(spot_v) - 1) > band][:2]
            far_c = [x for x in top_c if abs(float(x["s"]) / float(spot_v) - 1) > band][:2]
            conc.append("近端 Put 集中 " + (_tag(near_p) if near_p else "±12% 内无显著集中"))
            conc.append("近端 Call 集中 " + (_tag(near_c) if near_c else "±12% 内无显著集中"))
            if far_p or far_c:
                tail = []
                if far_p:
                    tail.append("Put " + _tag(far_p))
                if far_c:
                    tail.append("Call " + _tag(far_c))
                conc.append("深虚值尾部（保护/彩票盘，非近端位）" + "；".join(tail))
        else:
            if top_p:
                conc.append("Put 集中 " + _tag(top_p[:2]))
            if top_c:
                conc.append("Call 集中 " + _tag(top_c[:2]))
        return ("；".join(notes), "｜".join(conc))

    lines: List[str] = []
    for e, reason in picks:
        exp = str(e.get("expiration", ""))
        exp_txt = _exp_short(exp)
        info = chain.get(exp) or {}
        dte = e.get("dte")
        ck, pk = e.get("call_oi"), e.get("put_oi")
        ratio = (float(pk) / float(ck)) if ck else None
        em = e.get("expmove_pct")
        em_txt = f"±{float(em):.2f}%" if em is not None else "N/A"
        wall_notes, conc_txt = _concentration_txt(e, info, spot)

        parts = [f"MaxPain {_fmt(e.get('max_pain'), 0)}"]
        cw = e.get("call_wall") or {}
        pw = e.get("put_wall") or {}
        if cw.get("strike"):
            cls_txt = "（PRIMARY）" if cw.get("class") == "PRIMARY" else "（WEAK）"
            parts.append(f"CW {_fmt(cw.get('strike'), 0)}{cls_txt}")
        if pw.get("strike"):
            parts.append(f"PW {_fmt(pw.get('strike'), 0)}（WEAK）")
        elif wall_notes:
            parts.append(wall_notes.split("；")[0] if "PW" in wall_notes else wall_notes)
        if conc_txt:
            parts.append(conc_txt)
        if ratio is not None:
            parts.append(f"P/C OI {ratio:.2f}")
        parts.append(f"ExpMove {em_txt}")
        struct_txt = "｜".join(parts)
        if spot is not None and pw.get("strike"):
            dist = (float(spot) / float(pw.get("strike")) - 1.0) * 100
            struct_txt += f"（现价距 PW {dist:+.1f}%）"

        # 剔除 OI 零变化的快照日（假日/周末占位文件），避免把"无交易日"误读为趋势中断
        raw_seq = info.get("seq") or []
        seq: List[Dict[str, Any]] = []
        prev = None
        for x in raw_seq:
            if prev is not None and float(x["C"]) == float(prev["C"]) and float(x["P"]) == float(prev["P"]):
                continue
            seq.append(x)
            prev = x
        ds: List[float] = []
        flow_txt = ""
        if len(seq) >= 2:
            vals = [float(x["P"]) for x in seq]
            ds = [vals[i + 1] - vals[i] for i in range(len(vals) - 1)][-3:]
            d_txt = " / ".join(f"{d / 1000:+.1f}k" for d in ds)
            if all(d > 0 for d in ds):
                flow_txt = f"Put 连续 {len(ds)} 个入账日增仓（{d_txt}）"
            elif all(d < 0 for d in ds):
                flow_txt = f"Put 连续 {len(ds)} 个入账日减仓（{d_txt}）"
            else:
                flow_txt = f"Put 入账日轨迹（{d_txt}）"
            peak = max(vals)
            cur_now = float(pk) if pk else vals[-1]
            flow_txt += (
                f"；当前 {_fmt_k(cur_now)}（快照）"
                f" = 链峰值 {_fmt_k(peak)} 的 {cur_now / peak * 100:.0f}%"
            )
        flow_txt = f"；{flow_txt}" if flow_txt else ""

        time_txt = f"剩 {int(dte)} 个交易日" if dte is not None else "到期档"
        head = f"**{exp_txt} 档（{time_txt}）C {_fmt_k(ck)} / P {_fmt_k(pk)}**"
        body = f"{struct_txt}{flow_txt}。{_exp_interpretation(e, ds, spot)}（选中依据：{reason}）"
        lines.append(f"🔴 {head}：{body}")

    if session == "evening" and exps and all(
        not (e.get("put_delta_oi") or e.get("call_delta_oi")) for e in exps[:4]
    ):
        lines.append(
            "🔴 **信息缺口：今晚 OI 终值未更新（ΔOI 全 0）**：今天的仓位方向明早晨报才可读——"
            "若明晨 put 续增则趋势成立，若回落则此前只是事件前对冲（待验证，非结论）。"
        )
    return lines[:3]


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
    spot = snap.get("spot")
    lines.append("")
    lines += _risk_items(snap)
    lines.append("")
    lines.append("— 完整版晨报/晚报仍在原频道推送；本简报仅作提醒，不构成投资建议。")
    return "\n".join(lines)


def _full_block_parts(
    snap: Dict[str, Any],
    session: str,
    ticker: str,
    chain: Optional[Dict[str, Any]],
    prior_state: Optional[Dict[str, Any]],
) -> Tuple[List[str], List[Dict[str, Any]], List[str]]:
    """QQQ 完整区块。返回 (行, 新增待兑现条件, 已结算的旧条件 key)。"""
    date_str, _ts = _parse_created(snap.get("created_at"))
    sess_zh = "晨" if session == "morning" else "晚"
    lines = [f"### {ticker}｜{sess_zh}简报 {date_str}", "", _one_line(snap), ""]
    lines += _structural_map(snap)
    lines.append("")
    lines += _conditional_path(snap)
    spot = snap.get("spot")
    confirm_lines, resolved, confirmed = _eval_prior_signals(snap, chain, prior_state, ticker)
    trend = _expiry_trend_lines(snap, chain, session, force_exps=confirmed)
    pending = _pending_signals(snap, chain, session, ticker, force_exps=confirmed)
    generic = _risk_opportunity(snap, session=session, ticker=ticker)
    if chain:
        generic = [
            g for g in generic
            if not any(k in g for k in ("信息缺口", "明日 ", "结构锚"))
        ]
    if confirm_lines or trend:
        lines.append("")
        lines.append("## 🎯 四档专题")
        lines.append("*集中位 = 该档 OI 最大的行权价；括号 = OI 与距现价%。带外巨量 OI 单列为深虚值尾部。*")
        lines += [f"- {x}" for x in confirm_lines]
        if trend:
            lines += [f"- {x}" for x in trend]
    zero_lines = _zero_dte_lines((chain or {}).get("_0dte"), spot)
    if zero_lines:
        lines += [""] + zero_lines
    sig_lines = _signal_layer(snap, chain, ticker)
    if sig_lines:
        lines += [""] + sig_lines
    lines.append("")
    lines.append("## 🔴 风险 / 🟢 机会")
    lines += [f"- {x}" for x in generic]
    lines.append("")
    lines.append(f"**一句话：{_closing_line(snap, session, ticker)}**")
    return lines, pending, resolved


def render_ticker_block_with_state(
    snap: Dict[str, Any],
    session: str = "morning",
    ticker: str = "QQQ",
    full: bool = False,
    chain: Optional[Dict[str, Any]] = None,
    prior_state: Optional[Dict[str, Any]] = None,
) -> Tuple[str, List[Dict[str, Any]], List[str]]:
    """单标的区块；完整档返回 (文本, 新增待兑现条件, 已结算 key)。"""
    if full:
        lines, pending, resolved = _full_block_parts(snap, session, ticker, chain, prior_state)
        return "\n".join(lines), pending, resolved
    date_str, _ts = _parse_created(snap.get("created_at"))
    sess_zh = "晨" if session == "morning" else "晚"
    lines = [f"### {ticker}｜{sess_zh}简报 {date_str}", "", _one_line(snap), ""]
    lines += _structural_map(snap)
    lines.append("")
    lines += _conditional_path(snap)
    risk = _risk_items(snap)
    if len(risk) > 1:
        lines.append("")
        lines += risk[:3]
    return "\n".join(lines), [], []


def render_ticker_block(
    snap: Dict[str, Any],
    session: str = "morning",
    ticker: str = "QQQ",
    full: bool = False,
    chain: Optional[Dict[str, Any]] = None,
    prior_state: Optional[Dict[str, Any]] = None,
) -> str:
    """多标的摘要里的单个标的区块（兼容旧调用，仅返回文本）。"""
    text, _p, _r = render_ticker_block_with_state(
        snap, session=session, ticker=ticker, full=full, chain=chain, prior_state=prior_state
    )
    return text


def _closing_line(
    snap: Dict[str, Any], session: str = "morning", ticker: str = "QQQ"
) -> str:
    """收束句：状态事实 + 时间框架，全部来自快照字段，不做方向断言。"""
    loc = snap.get("location") or {}
    spot = snap.get("spot")
    flip = loc.get("flip_primary")
    gamma = (snap.get("regime") or {}).get("gamma", "UNKNOWN")
    gex = ((snap.get("p3") or {}).get("gex") or {}).get("net_gex")
    cw, pw = loc.get("call_wall"), loc.get("put_wall")
    exps = ((snap.get("forward") or {}).get("expirations")) or []
    parts = []
    if spot is not None and flip is not None:
        parts.append(f"现价 {spot:.2f} 在 Flip {flip:.2f} {'下方' if spot < flip else '上方'}")
    if gamma in ("POSITIVE", "NEGATIVE"):
        parts.append(f"Gamma {gamma}")
    near = exps[0] if exps else None
    if near and near.get("dte") is not None and int(near.get("dte")) <= 2:
        parts.append(f"明日 {_exp_short(str(near.get('expiration','')))} 到期先移仓")
    if len(exps) >= 3:
        def oi_sum(e) -> float:
            return float(e.get("call_oi") or 0) + float(e.get("put_oi") or 0)
        main = max(exps[:4], key=oi_sum)
        if oi_sum(main) > 0:
            parts.append(f"真正结构在 {_exp_short(str(main.get('expiration','')))}")
    ref = pw or cw
    if ref:
        parts.append(f"{ref:.0f} 是观察线不是预测线")
    base = "；".join(parts) + "。" if parts else "今日结构数据不足。"
    st = _BACKTEST.get(ticker.upper())
    if gamma == "NEGATIVE" and gex is not None and float(gex) < 0:
        tag = "" if st else f"（{ticker.upper()} 未回测，观察）"
        base += f" 负 Gamma（GEX<0）下触线波动易放大{tag}（幅度风险，方向不预设）。"
    elif gamma == "NEGATIVE":
        base += " Gamma 标签与 GEX 口径不一致，波动放大结论不启用。"
    return base


def render_digest_with_state(
    snapshots: List[Tuple[str, Dict[str, Any]]],
    session: str = "morning",
    date_str: str = "",
    full_tickers: Optional[List[str]] = None,
    chain_data: Optional[Dict[str, Any]] = None,
    prior_state: Optional[Dict[str, Any]] = None,
) -> Tuple[str, List[Dict[str, Any]], List[str]]:
    """合并多标的摘要；返回 (文本, 新增待兑现条件, 已结算 key)。"""
    full_set = {t.upper() for t in (full_tickers or ["QQQ"])}
    sess_zh = "晨报简报" if session == "morning" else "晚报简报"
    blocks = []
    pending_all: List[Dict[str, Any]] = []
    resolved_all: List[str] = []
    for t, snap in snapshots:
        full = t.upper() in full_set
        if full:
            txt, pending, resolved = render_ticker_block_with_state(
                snap,
                session=session,
                ticker=t,
                full=True,
                chain=(chain_data or {}).get(t.upper()),
                prior_state=prior_state,
            )
            pending_all += pending
            resolved_all += resolved
            blocks.append(txt)
        else:
            blocks.append(
                render_ticker_block(
                    snap, session=session, ticker=t, full=False,
                    chain=(chain_data or {}).get(t.upper()),
                )
            )
    head = f"# 📋 期权简报（多标的·{sess_zh}）{date_str}".rstrip()
    lines = [head, f"共 {len(snapshots)} 个标的；个别标的缺快照时自动跳过，不阻塞整批。", ""]
    lines.append("\n\n---\n\n".join(blocks))
    lines.append("— 完整版晨报/晚报仍在原频道推送；本简报仅作提醒，不构成投资建议。")
    return "\n".join(lines), pending_all, resolved_all


def render_digest(
    snapshots: List[Tuple[str, Dict[str, Any]]],
    session: str = "morning",
    date_str: str = "",
    full_tickers: Optional[List[str]] = None,
    chain_data: Optional[Dict[str, Any]] = None,
) -> str:
    """兼容旧调用（无跨日状态），仅返回文本。"""
    text, _p, _r = render_digest_with_state(
        snapshots,
        session=session,
        date_str=date_str,
        full_tickers=full_tickers,
        chain_data=chain_data,
        prior_state=None,
    )
    return text


if __name__ == "__main__":  # 本地自检入口：python report/brief.py <snapshot.json> [morning|evening]
    import json
    import sys

    path = sys.argv[1] if len(sys.argv) > 1 else ""
    session = sys.argv[2] if len(sys.argv) > 2 else "morning"
    with open(path, encoding="utf-8") as f:
        print(render_brief(json.load(f), session=session))
