# 期权晚报 2026-08-24

📊 市场环境

SPY $763.76 ｜ QQQ $706.32
VIX 15.85 ↑4.8%（5D +4.3%）
CNN 恐惧贪婪 55.0（greed）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 08-26 08:30　【高】Personal Spending MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 08-26 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 08-26 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 1.5 ｜ 实际 待公布 ｜ 前值 2.1
- 周三 08-26 08:30　【高】耐用品订单 Orders MoM　预测 0.7 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 08-26 08:30　【高】PCE 物价 Price Index MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.1
- 周五 08-28 10:00　【高】美联储主席讲话 Warsh Speech　实际 待公布
- 周五 08-28 10:00　【高】Non Farm Payrolls Annual Revision Prel　实际 待公布 ｜ 前值 -911

📋 Thesis Scorecard（今晨条件 vs 收盘实况，只打事实勾）
SPY: 今晨 764.19 → 收盘 763.73（-0.1%）
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞


## SPY

Options: P/C量 1.26 | OI比 1.40 | ATM IV 11.4% | Skew 3.1pp | Term 1.12 | ExpMove ±0.1% | Rank — (历史不足)
   ⇒ Put/Call Volume: 1.26×（Put 成交显著高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.40×（Put OI 高于 Call OI）→ 存量 Put-dominant
   ⇒ 两者结构一致
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma: NEGATIVE | GEX(存量) N/A | GEX Change N/A | Flip: N/A
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: N/A（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 535: +42.8% | 距 Call Wall 800: -4.5%
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 535（Put Wall）；上方 800（Call Wall）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-24/SPY_evening.json