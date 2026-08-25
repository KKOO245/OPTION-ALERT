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
SOXX: 今晨 514.91 → 收盘 512.79（-0.4%） ｜ 今日高 520.09 ｜ 低 509.66
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞


## SOXX

Options: P/C量 0.50 | OI比 0.82 | ATM IV 48.3% | Skew 5.4pp | Term 0.85 | ExpMove ±3.6% | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.50×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.82×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: ≈292.50
   ⇒ Gamma Regime 判定为 NEGATIVE；GEX 数值不可用，不对 Gamma 强度做判断。
结构观察区: ≈292（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 500: +2.6% | 距 Call Wall 670: -23.5%
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 500（Put Wall）；上方 670（Call Wall）。
• Gamma 区域：切换参考 292（Top-3 近似，需全链重定价验证）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

08-28  C +1.5k / P +4.2k ｜ Activity HIGH ｜ 3D
09-04  C +0.1k / P +3.4k ｜ Activity HIGH ｜ 10D
09-11  C +31 / P +73 ｜ Activity MEDIUM △ ｜ 17D
09-18  C +1.7k / P +4.6k ｜ Activity HIGH ｜ 24D

📆 08-28 Forward Structure
OI:       C 34.6k / P 28.3k
ΔOI:      C +1.5k / P +4.2k
ATM:      C 9.00 / P 10.40
ATM IV:   48.3%
ΔOI Δ Exposure*: 76k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 460 ｜ +2,148 ｜ $0.35 ｜ 名义 $75.2k* ｜ -10.3%
P 507 ｜ -982 ｜ $7.48 ｜ 名义 $-734.5k* ｜ -1.0%
P 465 ｜ +904 ｜ $0.49 ｜ 名义 $44.3k* ｜ -9.3%
结构参考：460（-10.3%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-04 Forward Structure
OI:       C 22.0k / P 16.6k
ΔOI:      C +0.1k / P +3.4k
ATM:      C 18.80 / P 12.20
ATM IV:   44.4%
ΔOI Δ Exposure*: -15k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 440 ｜ +2,244 ｜ $0.85 ｜ 名义 $190.7k* ｜ -14.2%
P 442 ｜ +670 ｜ $1.15 ｜ 名义 $77.0k* ｜ -13.7%
P 505 ｜ +134 ｜ $10.50 ｜ 名义 $140.7k* ｜ -1.5%
结构参考：440（-14.2%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

   Top ΔOI: 535C +62 ｜ 537C -39

📆 09-18 Forward Structure
OI:       C 68.3k / P 66.0k
ΔOI:      C +1.7k / P +4.6k
ATM:      C 22.03 / P 0.00
ATM IV:   41.5%
ΔOI Δ Exposure*: -62k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 490 ｜ +2,685 ｜ $11.62 ｜ 名义 $3.12M* ｜ -4.4%
P 470 ｜ +1,219 ｜ $6.66 ｜ 名义 $811.9k* ｜ -8.3%
P 465 ｜ +1,150 ｜ $7.42 ｜ 名义 $853.3k* ｜ -9.3%
结构参考：490（-4.4%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-25/SOXX_evening.json