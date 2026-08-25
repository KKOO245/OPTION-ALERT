# 期权晚报 2026-08-25

📊 市场环境

SPY $765.95 ｜ QQQ $710.72
VIX 15.45 ↓2.5%（5D -2.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 58.8（greed）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 08-26 08:30　【高】Personal Spending MoM　预测 0.1 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 08-26 08:30　【高】Personal Income MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 08-26 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 1.5 ｜ 实际 待公布 ｜ 前值 2.1
- 周三 08-26 08:30　【高】耐用品订单 Orders MoM　预测 0.7 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 08-26 08:30　【高】PCE 物价 Price Index MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.1
- 周五 08-28 10:00　【高】美联储主席讲话 Warsh Speech　实际 待公布
- 周五 08-28 10:00　【高】Non Farm Payrolls Annual Revision Prel　实际 待公布 ｜ 前值 -911

📋 Thesis Scorecard（今晨条件 vs 收盘实况，只打事实勾）
SLV: 今晨 61.35 → 收盘 62.20（+1.4%） ｜ 今日高 62.62 ｜ 低 60.94
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞


## SLV

Options: P/C量 0.48 | OI比 0.38 | ATM IV 43.6% | Skew -5.3pp | Term 1.01 | ExpMove ±1.9% | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.48×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.38×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: ≈19.02 / ≈39.09 / ≈61.21
结构观察区: 19–39（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 50: +24.4% | 距 Call Wall 70: -11.1%
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 50（Put Wall）；上方 70（Call Wall）。
• Gamma 区域：切换参考 19（Top-3 近似，需全链重定价验证）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

08-26  C +0 / P +0 ｜ Activity LOW ｜ 1D
08-28  C +0 / P +0 ｜ Activity LOW ｜ 3D
08-31  C +0 / P +0 ｜ Activity LOW ｜ 6D
09-02  C +0 / P +0 ｜ Activity LOW ｜ 8D

Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-25/SLV_evening.json