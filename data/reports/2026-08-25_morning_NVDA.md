# 期权晨报 2026-08-25

📊 市场环境

SPY $764.92 ｜ QQQ $709.43
VIX 15.76 ↓0.6%（5D -0.5%） ｜ Vol Regime: INSUFFICIENT_DATA ⚠️
CNN 恐惧贪婪 58.7（greed）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。
⚠️ Vol Regime unavailable: rule evaluation incomplete.

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 08-26 08:30　【高】Personal Spending MoM　预测 0.1 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 08-26 08:30　【高】Personal Income MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 08-26 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 1.5 ｜ 实际 待公布 ｜ 前值 2.1
- 周三 08-26 08:30　【高】耐用品订单 Orders MoM　预测 0.7 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 08-26 08:30　【高】PCE 物价 Price Index MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.1
- 周五 08-28 10:00　【高】美联储主席讲话 Warsh Speech　实际 待公布
- 周五 08-28 10:00　【高】Non Farm Payrolls Annual Revision Prel　实际 待公布 ｜ 前值 -911

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 208.90 → 今晨 213.45（+2.2%） | 较昨收变动（含盘初走势） ｜ 今日高 214.73 ｜ 低 210.11


## NVDA

Options: P/C量 0.29 | OI比 0.53 | ATM IV 77.2% | Skew 0.0pp | Term 0.52 | ExpMove ±5.8% | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.29×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.53×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: ≈218.74 / ≈219.35 / ≈256.73
结构观察区: 219–219（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 190: +12.3% | 距 Call Wall 230: -7.2%
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 190（Put Wall）；上方 230（Call Wall）。
• Gamma 区域：切换参考 219（Top-3 近似，需全链重定价验证）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
08-28 210.0C — Vol N/A | OI 9479→27820 (ΔOI +18341张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增18341张（+193.5% vs前日OI），连续性待观察（方向未知）
08-28 220.0C — Vol N/A | OI 42861→57140 (ΔOI +14279张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增14279张（+33.3% vs前日OI），连续性待观察（方向未知）
08-28 230.0C — Vol N/A | OI 65232→78303 (ΔOI +13071张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增13071张（+20.0% vs前日OI），连续性待观察（方向未知）
08-28 195.0P — Vol N/A | OI 8949→21199 (ΔOI +12250张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增12250张（+136.9% vs前日OI），连续性待观察（方向未知）
08-28 215.0C — Vol N/A | OI 16095→28038 (ΔOI +11943张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增11943张（+74.2% vs前日OI），连续性待观察（方向未知）
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-25/NVDA_morning.json