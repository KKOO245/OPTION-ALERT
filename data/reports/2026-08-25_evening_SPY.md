# 期权晚报 2026-08-25

📊 市场环境

SPY $764.92 ｜ QQQ $709.47
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
SPY: 今晨 765.41 → 收盘 764.92（-0.1%） ｜ 今日高 766.78 ｜ 低 763.05
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞


## SPY

Options: P/C量 1.00 | OI比 1.48 | ATM IV 8.8% | Skew 2.8pp | Term 1.43 | ExpMove ±0.1% | Rank — (历史不足)
   ⇒ Put/Call Volume: 1.00×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.48×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: NO_FLIP_IN_RANGE
   ⇒ Gamma Regime 判定为 NEGATIVE；GEX 数值不可用，不对 Gamma 强度做判断。
结构观察区: NO_FLIP_IN_RANGE
距 Put Wall 535: +43.0% | 距 Call Wall 800: -4.4%
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 535（Put Wall）；上方 800（Call Wall）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

08-26  C +16.3k / P +30.6k ｜ Activity HIGH ｜ 1D
08-27  C +9.2k / P +10.5k ｜ Activity HIGH ｜ 2D
08-28  C +17.8k / P +21.7k ｜ Activity HIGH ｜ 3D
08-31  C +7.5k / P +21.8k ｜ Activity HIGH ｜ 6D

📆 08-26 Forward Structure
OI:       C 65.3k / P 140.2k
ΔOI:      C +16.3k / P +30.6k
ATM:      C 1.94 / P 1.99
ATM IV:   11.8%
ΔOI Δ Exposure*: 394k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 765 ｜ -4,875 ｜ $1.99 ｜ 名义 $-970.1k* ｜ +0.0%
P 718 ｜ +4,017 ｜ $0.01 ｜ 名义 $4.0k* ｜ -6.1%
P 763 ｜ +3,722 ｜ $1.22 ｜ 名义 $454.1k* ｜ -0.3%
结构参考：718（-6.1%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 08-27 Forward Structure
OI:       C 49.0k / P 61.5k
ΔOI:      C +9.2k / P +10.5k
ATM:      C 2.91 / P 2.92
ATM IV:   12.6%
ΔOI Δ Exposure*: 56k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 774 ｜ +2,846 ｜ $0.30 ｜ 名义 $85.4k* ｜ +1.2%
P 759 ｜ +2,288 ｜ $1.04 ｜ 名义 $238.0k* ｜ -0.8%
C 769 ｜ +1,610 ｜ $1.24 ｜ 名义 $199.6k* ｜ +0.5%
结构参考：774（+1.2%）上方 / 759（-0.8%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 08-28 Forward Structure
OI:       C 203.3k / P 289.0k
ΔOI:      C +17.8k / P +21.7k
ATM:      C 3.89 / P 3.65
ATM IV:   13.3%
ΔOI Δ Exposure*: 469k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 750 ｜ -4,416 ｜ $0.48 ｜ 名义 $-212.0k* ｜ -2.0%
C 765 ｜ +3,652 ｜ $3.89 ｜ 名义 $1.42M* ｜ +0.0%
P 752 ｜ +3,104 ｜ $0.66 ｜ 名义 $204.9k* ｜ -1.7%
结构参考：752（-1.7%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 08-31 Forward Structure
OI:       C 313.7k / P 680.1k
ΔOI:      C +7.5k / P +21.8k
ATM:      C 4.56 / P 4.24
ATM IV:   11.1%
ΔOI Δ Exposure*: -222k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 770 ｜ +5,048 ｜ $6.95 ｜ 名义 $3.51M* ｜ +0.7%
P 616 ｜ +2,841 ｜ $0.01 ｜ 名义 $2.8k* ｜ -19.5%
P 615 ｜ +2,706 ｜ $0.01 ｜ 名义 $2.7k* ｜ -19.6%
结构参考：770（+0.7%）上方 / 616（-19.5%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-25/SPY_evening.json