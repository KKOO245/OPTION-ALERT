# 期权晚报 2026-08-25

📊 市场环境

SPY $765.00 ｜ QQQ $709.42
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
NBIS: 今晨 216.15 → 收盘 219.94（+1.8%） ｜ 今日高 221.12 ｜ 低 213.55
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞


## NBIS

Options: P/C量 0.54 | OI比 0.95 | ATM IV 98.4% | Skew -1.4pp | Term 0.91 | ExpMove ±7.3% | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.54×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.95×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: ≈248.92
   ⇒ Gamma Regime 判定为 NEGATIVE；GEX 数值不可用，不对 Gamma 强度做判断。
结构观察区: ≈249（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 200: +10.0% | 距 Call Wall 250: -12.0%
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall）；上方 250（Call Wall）。
• Gamma 区域：切换参考 249（Top-3 近似，需全链重定价验证）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

08-28  C +7.0k / P +5.6k ｜ Activity HIGH ｜ 3D
09-04  C +11.0k / P +4.2k ｜ Activity HIGH ｜ 10D
09-11  C +1.4k / P +0.6k ｜ Activity HIGH ｜ 17D
09-18  C +67 / P +64 ｜ Activity LOW ｜ 24D

📆 08-28 Forward Structure
OI:       C 63.8k / P 60.5k
ΔOI:      C +7.0k / P +5.6k
ATM:      C 8.00 / P 7.97
ATM IV:   98.4%
ΔOI Δ Exposure*: 92k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 220 ｜ +1,678 ｜ $8.00 ｜ 名义 $1.34M* ｜ +0.0%
C 240 ｜ +1,457 ｜ $2.10 ｜ 名义 $306.0k* ｜ +9.1%
C 185 ｜ -1,231 ｜ $35.36 ｜ 名义 $-4.35M* ｜ -15.9%
结构参考：240（+9.1%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-04 Forward Structure
OI:       C 25.7k / P 20.0k
ΔOI:      C +11.0k / P +4.2k
ATM:      C 13.60 / P 13.65
ATM IV:   91.7%
ΔOI Δ Exposure*: 610k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 215 ｜ +3,583 ｜ $16.20 ｜ 名义 $5.80M* ｜ -2.2%
C 207 ｜ +2,921 ｜ $20.20 ｜ 名义 $5.90M* ｜ -5.7%
C 190 ｜ +1,801 ｜ $32.09 ｜ 名义 $5.78M* ｜ -13.6%
结构参考：215（-2.2%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 6.9k / P 10.9k
ΔOI:      C +1.4k / P +0.6k
ATM:      C 17.09 / P 16.72
ATM IV:   88.8%
ΔOI Δ Exposure*: 32k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 250 ｜ +459 ｜ $6.98 ｜ 名义 $320.4k* ｜ +13.7%
C 300 ｜ +224 ｜ $1.50 ｜ 名义 $33.6k* ｜ +36.4%
P 150 ｜ +150 ｜ $0.98 ｜ 名义 $14.7k* ｜ -31.8%
结构参考：250（+13.7%）上方 / 150（-31.8%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-25/NBIS_evening.json