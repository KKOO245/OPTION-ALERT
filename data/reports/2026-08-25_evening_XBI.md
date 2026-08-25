# 期权晚报 2026-08-25

📊 市场环境

SPY $765.91 ｜ QQQ $710.72
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
XBI: 今晨 168.13 → 收盘 169.10（+0.6%） ｜ 今日高 169.88 ｜ 低 165.79
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞


## XBI

Options: P/C量 1.35 | OI比 1.41 | ATM IV 38.1% | Skew 0.3pp | Term 0.86 | ExpMove ±2.8% | Rank — (历史不足)
   ⇒ Put/Call Volume: 1.35×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.41×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: ≈80.03 / ≈159.24 / ≈159.31
结构观察区: 80–159（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 150: +12.7% | 距 Call Wall 155: +9.1%
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（Put Wall）；上方 155（Call Wall）。
• Gamma 区域：切换参考 80（Top-3 近似，需全链重定价验证）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

08-28  C +0 / P +0 ｜ Activity LOW ｜ 3D
09-04  C +0 / P +0 ｜ Activity LOW ｜ 10D
09-11  C +0 / P +0 ｜ Activity LOW ｜ 17D
09-18  C +0 / P +0 ｜ Activity LOW ｜ 24D

Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-25/XBI_evening.json