# 期权晚报 2026-08-25

📊 市场环境

SPY $764.97 ｜ QQQ $709.43
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
SNDK: 今晨 1,516.59 → 收盘 1,488.00（-1.9%） ｜ 今日高 1564.99 ｜ 低 1478.00
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞


## SNDK

Options: P/C量 0.64 | OI比 0.79 | ATM IV 86.2% | Skew -1.0pp | Term 0.88 | ExpMove ±6.4% | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.64×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.79×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ⇒ IV–VIX Spread: +70.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: ≈1697.43
   ⇒ Gamma Regime 判定为 NEGATIVE；GEX 数值不可用，不对 Gamma 强度做判断。
结构观察区: ≈1697（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 800: +86.0% | 距 Call Wall 2,000: -25.6%
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 800（Put Wall）；上方 2,000（Call Wall）。
• Gamma 区域：切换参考 1697（Top-3 近似，需全链重定价验证）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

08-28  C +16.8k / P +9.3k ｜ Activity HIGH ｜ 3D
09-04  C +4.5k / P +2.2k ｜ Activity HIGH ｜ 10D
09-11  C +0.3k / P +0.9k ｜ Activity HIGH ｜ 17D
09-18  C +1.5k / P +0.8k ｜ Activity HIGH ｜ 24D

📆 08-28 Forward Structure
OI:       C 56.9k / P 44.8k
ΔOI:      C +16.8k / P +9.3k
ATM:      C 47.57 / P 47.19
ATM IV:   86.2%
ΔOI Δ Exposure*: 272k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 1700 ｜ +3,764 ｜ $3.55 ｜ 名义 $1.34M* ｜ +14.2%
P 1200 ｜ +1,257 ｜ $0.45 ｜ 名义 $56.6k* ｜ -19.4%
C 1500 ｜ +1,177 ｜ $43.00 ｜ 名义 $5.06M* ｜ +0.8%
结构参考：1700（+14.2%）上方 / 1200（-19.4%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-04 Forward Structure
OI:       C 14.2k / P 13.8k
ΔOI:      C +4.5k / P +2.2k
ATM:      C 80.10 / P 80.51
ATM IV:   79.2%
ΔOI Δ Exposure*: 78k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 1550 ｜ +879 ｜ $54.61 ｜ 名义 $4.80M* ｜ +4.2%
C 1900 ｜ +615 ｜ $4.55 ｜ 名义 $279.8k* ｜ +27.7%
C 2100 ｜ +480 ｜ $1.15 ｜ 名义 $55.2k* ｜ +41.1%
结构参考：1550（+4.2%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 4.4k / P 8.6k
ΔOI:      C +0.3k / P +0.9k
ATM:      C 98.47 / P 90.18
ATM IV:   74.9%
ΔOI Δ Exposure*: -15k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 1300 ｜ +228 ｜ $28.00 ｜ 名义 $638.4k* ｜ -12.6%
P 1400 ｜ +199 ｜ $55.16 ｜ 名义 $1.10M* ｜ -5.9%
P 1250 ｜ +60 ｜ $17.25 ｜ 名义 $103.5k* ｜ -16.0%
结构参考：1300（-12.6%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-18 Forward Structure
OI:       C 49.8k / P 67.7k
ΔOI:      C +1.5k / P +0.8k
ATM:      C 116.80 / P 113.70
ATM IV:   75.4%
ΔOI Δ Exposure*: -482 shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 1300 ｜ +641 ｜ $37.90 ｜ 名义 $2.43M* ｜ -12.6%
C 2420 ｜ +634 ｜ $2.51 ｜ 名义 $159.1k* ｜ +62.6%
P 650 ｜ -464 ｜ $0.21 ｜ 名义 $-9.7k* ｜ -56.3%
结构参考：2420（+62.6%）上方 / 1300（-12.6%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-25/SNDK_evening.json