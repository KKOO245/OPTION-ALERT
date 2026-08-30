# -*- coding: utf-8 -*-
"""规则型分析与报告组装（v3）"""


def _fmt(v, digits=2, suffix=""):
    if v is None:
        return "N/A"
    try:
        return f"{v:,.{digits}f}{suffix}"
    except (TypeError, ValueError):
        return str(v)


def _fmt_pct(v):
    if v is None:
        return "N/A"
    return f"{v * 100:.1f}%" if abs(v) < 3 else f"{v:.1f}%"


def price_line(ticker, price, prev_close):
    if price is None:
        return f"{ticker} 现价：暂未获取到（数据源临时问题）"
    if prev_close:
        change_pct = (price - prev_close) / prev_close * 100
        arrow = "▲" if change_pct >= 0 else "▼"
        return (f"{ticker} **现价 ${price:,.2f}**　{arrow} {change_pct:+.2f}%　"
                f"(前收盘 ${prev_close:,.2f})")
    return f"{ticker} **现价 ${price:,.2f}**"


def metrics_block(metrics, iv_rank_val):
    """一行式的核心指标速览（Discord 代码块内对齐）"""
    m = metrics
    at = _fmt_pct(m.get("atm_iv_near"))
    rank = f"{iv_rank_val:.0f}%" if iv_rank_val is not None else "N/A"
    skew = _fmt(m.get("iv_skew_25"), 1, "pp")
    term = _fmt(m.get("term_ratio"), 2)
    expm = _fmt(m.get("expected_move_pct"), 1, "%")
    pcr_v = _fmt(m.get("pcr_vol_near"), 2)
    pcr_o = _fmt(m.get("pcr_oi_near"), 2)
    mp = _fmt(m.get("max_pain_near"), 0)
    nd = _fmt(m.get("net_delta_oi"), 0)
    return (f"近月P/C量比 {pcr_v} | OI比 {pcr_o} | MaxPain {mp} | ATM IV {at} | "
            f"IV Rank {rank} | 25Δ偏度 {skew} | 期限结构 {term} | 预期波动 ±{expm} | "
            f"净Δ敞口 {nd} 股")


def _oi_zone_text(conc):
    if not conc:
        return "现价附近没有明显 OI 堆积"
    parts = []
    for row in conc:
        kind = "看涨" if row["type"] == "call" else "看跌"
        parts.append(f"{_fmt(row['strike'], 0)}({kind} {row['oi']:,}张)")
    return "OI 集中带: " + " / ".join(parts)


def rules_text(metrics, iv_rank_val, session, morning_iv=None):
    """基于指标的规则型解读（LLM 不可用时自动退回这个版本）"""
    m = metrics
    lines = []

    pcr_o = m.get("pcr_oi_near")
    pcr_v = m.get("pcr_vol_near")
    if pcr_o is not None:
        if pcr_o > 1.2:
            lines.append("→ 近月未平仓偏向看跌，市场对下行保护/投机需求较高。")
        elif pcr_o < 0.8:
            lines.append("→ 近月未平仓偏向看涨，市场情绪偏乐观或有杠杆多头布局。")
        else:
            lines.append("→ 近月看涨看跌未平仓大致平衡，没有明显方向倾斜。")
    if pcr_v is not None and pcr_o is not None and pcr_v / pcr_o > 1.5:
        lines.append("→ 今日成交量偏向与持仓结构不一致，短线资金可能在调仓/博弈。")

    if iv_rank_val is not None:
        if iv_rank_val >= 80:
            lines.append(f"→ ATM IV 处于近一年 {iv_rank_val:.0f}% 分位，属于高位，期权贵，注意 IV 回落风险。")
        elif iv_rank_val <= 20:
            lines.append(f"→ ATM IV 处于近一年 {iv_rank_val:.0f}% 分位，属于低位，期权相对便宜。")
        else:
            lines.append(f"→ ATM IV 处于近一年 {iv_rank_val:.0f}% 分位，中性区间。")

    skew = m.get("iv_skew_25")
    if skew is not None:
        if skew > 3:
            lines.append(f"→ 25Δ 偏度 {skew:.1f}pp，看跌期权明显更贵，市场在防备大跌/黑天鹅。")
        elif skew < -2:
            lines.append(f"→ 25Δ 偏度 {skew:.1f}pp，看涨期权相对更贵，市场偏乐观。")

    term = m.get("term_ratio")
    if term is not None:
        if term > 1.05:
            lines.append("→ 期限结构向上倾斜（远月 IV 高于近月），波动率预期平稳或略升。")
        elif term < 0.95:
            lines.append("→ 期限结构倒挂（近月 IV 高于远月），短期事件/恐慌压制近月，注意事件后 IV 回落。")

    expm = m.get("expected_move_pct")
    if expm is not None:
        lines.append(f"→ 期权市场隐含到期前预期波动约 ±{expm:.1f}%（ATM 跨式）。")

    if morning_iv is not None and m.get("atm_iv_near") is not None:
        chg = (m["atm_iv_near"] - morning_iv) / morning_iv * 100
        arrow = "升" if chg >= 0 else "降"
        lines.append(f"→ 较早报 ATM IV {arrow} {abs(chg):.1f}%。")

    zone = _oi_zone_text(m.get("oi_concentration") or [])
    lines.append(f"→ {zone}。")

    unusual = m.get("top_unusual") or []
    if unusual:
        u = unusual[0]
        kind = "看涨" if u["type"] == "call" else "看跌"
        vol_ratio_txt = ""
        if u.get("volume_ratio"):
            vol_ratio_txt = f"，昨量 {u.get('volume_prev') or 0:,}、放量 {u['volume_ratio']:.1f}×"
        elif u.get("volume_prev") == 0:
            vol_ratio_txt = "（新合约，无昨量对比）"
        oi_txt = ""
        if u.get("oi_prev") is not None:
            if u.get("oi_prev", 0) == 0:
                oi_txt = "，OI 为全新开仓"
            elif u.get("oi_change_pct") is not None:
                oi_txt = (f"，OI {u['oi_prev']:,}→{u['open_interest']:,}"
                          f"（{u['oi_change']:+,}，{u['oi_change_pct']:+.1f}%）")
        lines.append(
            f"→ 最大异动：{kind} {_fmt(u['strike'], 0)} 行权价 {u['expiration']} 到期，"
            f"今量 {u['volume']:,} 张{vol_ratio_txt}"
            + (f"（量/OI {u['vol_oi_ratio']:.1f}）" if u.get("vol_oi_ratio") else "")
            + f"{oi_txt}"
            + (f"，{u['flow']}" if u.get("flow") in ("开仓", "平仓", "换手", "新") else "")
            + "，值得跟踪。"
        )
    elif m.get("has_surge_data"):
        lines.append("→ 本次没有观察到明显异动成交。")

    surge = m.get("top_surge") or []
    if surge:
        s = surge[0]
        kind = "看涨" if s["type"] == "call" else "看跌"
        lines.append(
            f"→ OI 增仓最大：{kind} {_fmt(s['strike'], 0)} 行权价 "
            f"{s['expiration']}，较上次增加 {s['oi_change']:,} 张（{s['oi_prev']:,}→{s['oi']:,}）。"
        )
    elif m.get("has_surge_data") is False:
        lines.append("→ 首次运行，暂无前一日快照可对比 OI 增仓。")

    lines.append("（以上为基于公开期权数据的量化观察，不构成投资建议。）")
    return "\n".join(lines)


def _table(rows, col_map, title=None):
    if not rows:
        return "```\n(无数据)\n```"
    headers = list(col_map.keys())
    labels = [col_map[h] for h in headers]

    def fmt_cell(v):
        if v is None:
            return "N/A"
        if isinstance(v, float):
            return f"{v:,.2f}" if abs(v) >= 1 else f"{v:.4f}"
        if isinstance(v, int):
            return f"{v:,}"
        return str(v)

    body = [[fmt_cell(r.get(h)) for h in headers] for r in rows]
    widths = [len(l) for l in labels]
    for row in body:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(cell))

    def pad(cells):
        return " | ".join(c.ljust(widths[i]) for i, c in enumerate(cells))

    out = [pad(labels), "-+-".join("-" * w for w in widths)]
    out += [pad(r) for r in body]
    block = "```\n" + "\n".join(out) + "\n```"
    return f"**{title}**\n{block}" if title else block


def unusual_table(metrics):
    rows = metrics.get("top_unusual") or []
    col_map = {
        "type": "类型", "strike": "行权价", "expiration": "到期", "volume": "今量", "volume_prev": "昨量",
        "volume_ratio": "放量×", "oi_prev": "OI前", "open_interest": "OI现",
        "oi_change_pct": "OI增%", "premium": "成交额($)", "flow": "流向",
    }
    return _table(rows, col_map, "🔺 异动成交 Top（含前后对比）")


def _oi_top_table(calls, puts, title_prefix, include_exp=False):
    col_map = {
        "type": "类型", "strike": "行权价", "last": "最新价",
        "iv": "IV", "open_interest": "未平仓量",
    }
    if include_exp:
        col_map = {
            "type": "类型", "expiration": "到期日", "strike": "行权价",
            "last": "最新价", "iv": "IV", "open_interest": "未平仓量",
        }
    t1 = _table(calls, col_map, f"{title_prefix} Top5 看涨（按未平仓量）")
    t2 = _table(puts, col_map, f"{title_prefix} Top5 看跌（按未平仓量）")
    return t1 + "\n" + t2


def structure_block(metrics, spot):
    """🔧 市场结构数字块（做市商定位）"""
    structure = metrics.get("structure")
    if not structure or spot is None:
        return None
    s = structure
    near = metrics.get("structure_near") or {}
    monthly = metrics.get("structure_monthly") or {}
    ng = s.get("net_gex")
    ng_txt = f"{ng:+,.0f}" if ng is not None else "N/A"
    dg = -ng if ng is not None else None
    dg_txt = f"{dg:+,.0f}" if dg is not None else "N/A"
    nflip = _fmt(near.get("gamma_flip"), 0) if near.get("gamma_flip") is not None else "N/A"
    mflip = _fmt(monthly.get("gamma_flip"), 0) if monthly.get("gamma_flip") is not None else "N/A"
    vanna_txt = f"{s['net_vanna']:+,.0f}" if s.get("net_vanna") is not None else "N/A"
    charm_txt = f"{s['net_charm']:+,.0f}" if s.get("net_charm") is not None else "N/A"
    tg = " / ".join(
        f"{t['strike']:.0f}({'正' if t['gex'] > 0 else '负'})"
        for t in (s.get("top_gamma") or [])
    ) or "N/A"
    cvt = _fmt(s.get("call_vol_top"), 0)
    pvt = _fmt(s.get("put_vol_top"), 0)
    ng2 = metrics.get("new_gex")
    nd2 = metrics.get("new_delta")
    ng2_txt = f"{ng2:+,.0f}" if ng2 is not None else "N/A"
    nd2_txt = f"{nd2:+,.0f}" if nd2 is not None else "N/A"
    cw_cls = s.get("call_wall_class")
    pw_cls = s.get("put_wall_class")
    line1 = " | ".join([
        f"Call Wall {_fmt(s.get('call_wall'), 0)}{'（弱）' if cw_cls == 'WEAK' else ''}",
        f"Put Wall {_fmt(s.get('put_wall'), 0)}{'（弱）' if pw_cls == 'WEAK' else ''}",
        f"近周Flip {nflip}",
        f"月度Flip {mflip}",
        f"GEX失衡 {ng_txt}",
        f"反推Dealer {dg_txt}",
    ])
    line2 = " | ".join([
        f"Top Gamma {tg}",
        f"今日GEX {ng2_txt}",
        f"今日Δ {nd2_txt}",
        f"Net Vanna {vanna_txt}",
        f"Net Charm {charm_txt}",
        f"量集中C/P {cvt}/{pvt}",
    ])
    return "```\n" + line1 + "\n" + line2 + "\n```"


def structure_text(metrics, spot):
    """🧭 市场结构解读：压力/支撑/Gamma区域/做市商对冲/短线倾向"""
    structure = metrics.get("structure")
    if not structure or spot is None:
        return None
    s = structure
    near = metrics.get("structure_near") or {}
    monthly = metrics.get("structure_monthly") or {}
    lines = ["🧭 市场结构解读"]
    mp = metrics.get("max_pain_near")
    cw, pw, flip = s.get("call_wall"), s.get("put_wall"), s.get("gamma_flip")
    cw_cls, pw_cls = s.get("call_wall_class"), s.get("put_wall_class")
    nflip = near.get("gamma_flip")
    mflip = monthly.get("gamma_flip")
    ng, nd = s.get("net_gex"), metrics.get("net_delta_oi")

    ups = [x for x in (cw, mp if mp and mp > spot else None,
                       nflip if nflip and nflip > spot else None,
                       mflip if mflip and mflip > spot else None) if x]
    downs = [x for x in (pw, mp if mp and mp < spot else None,
                         nflip if nflip and nflip < spot else None,
                         mflip if mflip and mflip < spot else None) if x]
    if ups:
        lines.append(f"• 上方压力位：{_fmt(min(ups), 0)}（Call Wall {_fmt(cw, 0)}"
                     + ("，弱结构" if cw_cls == "WEAK" else "")
                     + (f" / MaxPain {_fmt(mp, 0)}" if mp and mp > spot else "")
                     + (f" / 近周Flip {_fmt(nflip, 0)}" if nflip and nflip > spot else "")
                     + (f" / 月度Flip {_fmt(mflip, 0)}" if mflip and mflip > spot else "") + "）。")
    if downs:
        lines.append(f"• 下方支撑位：{_fmt(max(downs), 0)}（Put Wall {_fmt(pw, 0)}"
                     + ("，弱结构" if pw_cls == "WEAK" else "")
                     + (f" / MaxPain {_fmt(mp, 0)}" if mp and mp < spot else "")
                     + (f" / 近周Flip {_fmt(nflip, 0)}" if nflip and nflip < spot else "")
                     + (f" / 月度Flip {_fmt(mflip, 0)}" if mflip and mflip < spot else "") + "）。")
    if mp:
        if mp > spot:
            lines.append(f"• Max Pain {_fmt(mp, 0)} 位于现价上方，有向该处回拉的磁吸倾向。")
        elif mp < spot:
            lines.append(f"• Max Pain {_fmt(mp, 0)} 位于现价下方，有向该处回落的磁吸倾向。")
        else:
            lines.append("• Max Pain 与现价基本重合，磁吸作用中性。")

    if nflip:
        lines.append(
            f"• Gamma 区域：近周主导切换位在 {_fmt(nflip, 0)}"
            + (f"（月度 {_fmt(mflip, 0)}）" if mflip else "")
            + "——其下 Put Gamma 主导、其上 Call Gamma 主导。"
        )
    elif ng is not None:
        lines.append(
            f"• Gamma 区域：近周无主导切换位（单边），全链 GEX 失衡 {ng:+,.0f}"
            "（Put 侧主导 / Call 侧主导）。"
        )
    ng2 = metrics.get("new_gex")
    nd2 = metrics.get("new_delta")
    if ng2 is not None and nd2 is not None:
        side = "看涨(Call)侧" if ng2 > 0 else ("看跌(Put)侧" if ng2 < 0 else "两侧均衡")
        lines.append(
            f"• 今日新增仓位：新增 GEX {ng2:+,.0f}、新增 Δ {nd2:+,.0f} 股——"
            f"近两日资金在 {side} 加码。"
        )
    lines.append(
        "• 做市商定位（按 OI 全为散户多头假设反推）：Put/Call Gamma 失衡说明做市商站在对手方——"
        "价格回落到 Put 重仓区下方时，做市商买盘对冲增加（承接）；"
        "反弹接近 Call 重仓区时卖盘对冲增加（压制）。OI 无法区分开平仓方向，此结论依赖假设。"
    )
    if nd is not None:
        lines.append(
            f"• 净 Delta 敞口（多头口径）{nd:+,.0f} 股：客户持仓整体"
            f"{'偏空（put 权重高）' if nd < 0 else '偏多（call 权重高）'}；"
            "做市商为反方，其对冲行为随价格与 IV 变化，方向需结合当日开平仓验证。"
        )

    bull = 0
    if nd is not None:
        bull += 1 if nd > 0 else -1
    if ng2 is not None:
        bull += 1 if ng2 > 0 else (-1 if ng2 < 0 else 0)
    pcr = metrics.get("pcr_oi_all")
    if pcr is not None:
        bull += 1 if pcr < 0.9 else (-1 if pcr > 1.1 else 0)
    skew = metrics.get("iv_skew_25")
    if skew is not None:
        bull += 1 if skew < -1 else (-1 if skew > 2 else 0)
    verdict = ("结构性偏多" if bull >= 2 else "结构性偏空" if bull <= -2
               else "中性偏多" if bull >= 1 else "中性偏空" if bull <= -1
               else "中性（区间震荡）")
    lines.append(f"• 短线倾向：{verdict}（Delta/PCR/偏度/今日GEX综合分 {bull:+d}）。")
    invalids = [f"Put Wall {_fmt(pw, 0)}" if pw else None,
                f"Flip {_fmt(flip, 0)}" if flip else None]
    invalids = [x for x in invalids if x]
    lines.append(
        f"• 失效条件：跌破 {' / '.join(invalids) if invalids else '下方支撑'} 则多头结构转弱；"
        f"站上 Call Wall {_fmt(cw, 0)} 才打开上方空间。"
    )
    return "\n".join(lines)


def surge_table(metrics):
    rows = metrics.get("top_surge") or []
    col_map = {
        "type": "类型", "strike": "行权价", "expiration": "到期",
        "oi_prev": "上次OI", "oi": "今日OI", "oi_change": "增仓",
    }
    return _table(rows, col_map, "📈 OI 增仓 Top（vs 上次快照）")


def build_ticker_section(ticker, price, prev_close, metrics, iv_rank_val,
                         session, morning_iv=None, show_surge=True):
    parts = [f"## {ticker}"]
    parts.append(price_line(ticker, price, prev_close))
    parts.append("")
    parts.append("```\n" + metrics_block(metrics, iv_rank_val) + "\n```")
    sb = structure_block(metrics, price)
    if sb:
        parts.append(sb)
    st = structure_text(metrics, price)
    if st:
        parts.append(st)
        parts.append("")
    parts.append("")
    parts.append(_oi_top_table(
        metrics.get("nearest_top_calls") or [],
        metrics.get("nearest_top_puts") or [],
        f"📌 最近到期日 {metrics.get('near_exp')}",
        include_exp=False,
    ))
    parts.append("")
    parts.append(_oi_top_table(
        metrics.get("window_top_calls") or [],
        metrics.get("window_top_puts") or [],
        f"📅 未来4个期权日（{metrics.get('window_label')}）合并",
        include_exp=True,
    ))
    parts.append("")
    parts.append(unusual_table(metrics))
    if show_surge:
        parts.append(surge_table(metrics))
    parts.append("")
    parts.append(rules_text(metrics, iv_rank_val, session, morning_iv))
    return "\n".join(parts)


def appendix_line(ticker, metrics, iv_rank_val):
    m = metrics
    parts = [
        ticker,
        f"P/C量 {_fmt(m.get('pcr_vol_all'), 2)}",
        f"P/C OI {_fmt(m.get('pcr_oi_all'), 2)}",
        f"IV {_fmt_pct(m.get('atm_iv_near'))}",
        f"Rank {int(iv_rank_val)}%" if iv_rank_val is not None else "Rank N/A",
        f"Skew {_fmt(m.get('iv_skew_25'), 1)}",
        f"ExpMove ±{_fmt(m.get('expected_move_pct'), 1)}%",
        f"MaxPain {_fmt(m.get('max_pain_near'), 0)}",
    ]
    return " | ".join(parts)


def market_context_line(spy_price, vix_price):
    parts = []
    if spy_price is not None:
        parts.append(f"SPY ${spy_price:,.2f}")
    if vix_price is not None:
        parts.append(f"VIX {vix_price:.2f}")
    return "市场背景： " + " ｜ ".join(parts) if parts else None


def build_report(date_str, session, ticker_sections, deep_analysis,
                 market_line, appendix_lines, disclaimer, calendar_sections=None):
    parts = [f"# 📊 期权{session} — {date_str}"]
    if market_line:
        parts.append(market_line)
    if calendar_sections:
        parts.append("")
        parts += calendar_sections
    if deep_analysis:
        parts.append("")
        parts.append("## 🧠 AI 深度分析")
        parts.append(deep_analysis)
    parts += ["", "---", ""]
    parts += ticker_sections
    if appendix_lines:
        parts.append("")
        parts.append("## 数据附录（核对用）")
        parts.append("```\n" + "\n".join(appendix_lines) + "\n```")
    parts.append("")
    parts.append(disclaimer)
    return "\n".join(parts)
