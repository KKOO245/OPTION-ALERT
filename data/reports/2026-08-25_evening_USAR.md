# 期权晚报 2026-08-25

📊 市场环境

SPY $764.92 ｜ QQQ $709.43
VIX 15.56 ↓1.8%（5D -1.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 58.7（greed）

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
USAR: 今晨 18.36 → 收盘 19.05（+3.7%） ｜ 今日高 19.26 ｜ 低 17.97
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞


## USAR

Options: P/C量 0.20 | OI比 0.61 | ATM IV 105.2% | Skew -5.9pp | Term 0.86 | ExpMove ±7.8% | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.20×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.61×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: ≈6.69 / ≈19.62 / ≈21.75
结构观察区: 7–20（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 15: +27.0% | 距 Call Wall 20: -4.8%
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall）；上方 20（Call Wall）。
• Gamma 区域：切换参考 7（Top-3 近似，需全链重定价验证）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

08-28  C +1.1k / P +3.5k ｜ Activity HIGH ｜ 3D
09-04  C +0.7k / P +0.5k ｜ Activity HIGH ｜ 10D
09-11  C +2.5k / P +13 ｜ Activity HIGH ｜ 17D
09-18  C +2.8k / P +0.9k ｜ Activity HIGH ｜ 24D

📆 08-28 Forward Structure
OI:       C 17.5k / P 10.7k
ΔOI:      C +1.1k / P +3.5k
ATM:      C 0.74 / P 0.66
ATM IV:   105.2%
ΔOI Δ Exposure*: -9k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 17 ｜ +1,090 ｜ $0.19 ｜ 名义 $20.7k* ｜ -8.1%
P 17 ｜ +596 ｜ $0.10 ｜ 名义 $6.0k* ｜ -10.7%
P 16 ｜ +503 ｜ $0.03 ｜ 名义 $1.5k* ｜ -16.0%
结构参考：17（-8.1%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-04 Forward Structure
OI:       C 14.1k / P 2.3k
ΔOI:      C +0.7k / P +0.5k
ATM:      C 1.19 / P 1.22
ATM IV:   95.5%
ΔOI Δ Exposure*: -1k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 20 ｜ -554 ｜ $0.84 ｜ 名义 $-46.5k* ｜ +5.0%
C 22 ｜ +326 ｜ $0.35 ｜ 名义 $11.4k* ｜ +15.5%
C 20 ｜ +224 ｜ $0.74 ｜ 名义 $16.6k* ｜ +7.6%
结构参考：22（+15.5%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 7.8k / P 1.6k
ΔOI:      C +2.5k / P +13
ATM:      C 1.54 / P 1.66
ATM IV:   89.4%
ΔOI Δ Exposure*: 58k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 22 ｜ +1,209 ｜ $0.49 ｜ 名义 $59.2k* ｜ +18.1%
C 23 ｜ +1,200 ｜ $0.38 ｜ 名义 $45.6k* ｜ +23.4%
C 21 ｜ -58 ｜ $0.79 ｜ 名义 $-4.6k* ｜ +10.3%
结构参考：22（+18.1%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-18 Forward Structure
OI:       C 104.8k / P 63.9k
ΔOI:      C +2.8k / P +0.9k
ATM:      C 1.80 / P 1.70
ATM IV:   91.1%
ΔOI Δ Exposure*: 78k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 20 ｜ +1,190 ｜ $1.38 ｜ 名义 $164.2k* ｜ +5.0%
C 24 ｜ +471 ｜ $0.53 ｜ 名义 $25.0k* ｜ +26.0%
C 25 ｜ +397 ｜ $0.37 ｜ 名义 $14.7k* ｜ +31.3%
结构参考：20（+5.0%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-25/USAR_evening.json