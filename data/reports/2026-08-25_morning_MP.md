# 期权晨报 2026-08-25

📊 市场环境

SPY $764.92 ｜ QQQ $709.40
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
MP  昨收 57.47 → 今晨 57.33（-0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 57.89 ｜ 低 55.60


## MP

Options: P/C量 2.83 | OI比 0.63 | ATM IV 80.4% | Skew -2.4pp | Term 0.86 | ExpMove ±6.1% | Rank — (历史不足)
   ⇒ Put/Call Volume: 2.83×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.63×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: ≈58.16 / ≈59.77 / ≈64.25
结构观察区: 58–60（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 55: +4.2% | 距 Call Wall 60: -4.4%
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 55（Put Wall）；上方 60（Call Wall）。
• Gamma 区域：切换参考 58（Top-3 近似，需全链重定价验证）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
08-28 55.0P — Vol N/A | OI 463→787 (ΔOI +324张) | ΔOI/Volume N/A | Magnitude: MEDIUM | 完整度: LOW
   ⇒ 净增324张（+70.0% vs前日OI），值得跟踪（方向未知）
08-28 65.0C — Vol N/A | OI 1358→1589 (ΔOI +231张) | ΔOI/Volume N/A | Magnitude: MEDIUM | 完整度: LOW
   ⇒ 净增231张（+17.0% vs前日OI），值得跟踪（方向未知）
08-28 60.0C — Vol N/A | OI 1642→1873 (ΔOI +231张) | ΔOI/Volume N/A | Magnitude: MEDIUM | 完整度: LOW
   ⇒ 净增231张（+14.1% vs前日OI），值得跟踪（方向未知）
09-11 65.0C — Vol N/A | OI 224→422 (ΔOI +198张) | ΔOI/Volume N/A | Magnitude: MEDIUM | 完整度: LOW
   ⇒ 净增198张（+88.4% vs前日OI），值得跟踪（方向未知）
08-28 57.0C — Vol N/A | OI 1215→1380 (ΔOI +165张) | ΔOI/Volume N/A | Magnitude: MEDIUM | 完整度: LOW
   ⇒ 净增165张（+13.6% vs前日OI），值得跟踪（方向未知）
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-25/MP_morning.json