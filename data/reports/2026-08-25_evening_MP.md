# 期权晚报 2026-08-25

📊 市场环境

SPY $764.92 ｜ QQQ $709.41
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
MP: 今晨 57.33 → 收盘 59.48（+3.7%） ｜ 今日高 59.90 ｜ 低 55.60
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞


## MP

Options: P/C量 0.41 | OI比 0.63 | ATM IV 80.5% | Skew -2.2pp | Term 0.80 | ExpMove ±6.0% | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.41×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.63×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: ≈56.98 / ≈59.50 / ≈59.88
结构观察区: 57–60（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 55: +8.1% | 距 Call Wall 60: -0.9%
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 55（Put Wall）；上方 60（Call Wall）。
• Gamma 区域：切换参考 57（Top-3 近似，需全链重定价验证）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

08-28  C +1.0k / P +1.2k ｜ Activity HIGH ｜ 3D
09-04  C +0.3k / P +0.3k ｜ Activity HIGH ｜ 10D
09-11  C +0.2k / P +53 ｜ Activity HIGH ｜ 17D
09-18  C +49 / P +0.3k ｜ Activity MEDIUM △ ｜ 24D

📆 08-28 Forward Structure
OI:       C 13.0k / P 8.2k
ΔOI:      C +1.0k / P +1.2k
ATM:      C 2.16 / P 1.61
ATM IV:   80.5%
ΔOI Δ Exposure*: 23k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 55 ｜ +324 ｜ $0.32 ｜ 名义 $10.4k* ｜ -7.5%
C 60 ｜ +231 ｜ $1.55 ｜ 名义 $35.8k* ｜ +0.9%
C 65 ｜ +231 ｜ $0.34 ｜ 名义 $7.9k* ｜ +9.3%
结构参考：60（+0.9%）上方 / 55（-7.5%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-04 Forward Structure
OI:       C 5.7k / P 4.4k
ΔOI:      C +0.3k / P +0.3k
ATM:      C 3.23 / P 3.95
ATM IV:   73.0%
ΔOI Δ Exposure*: 5k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 65 ｜ +150 ｜ $1.13 ｜ 名义 $16.9k* ｜ +9.3%
C 64 ｜ +101 ｜ $1.31 ｜ 名义 $13.2k* ｜ +7.6%
P 52 ｜ +51 ｜ $0.49 ｜ 名义 $2.5k* ｜ -12.6%
结构参考：65（+9.3%）上方 / 52（-12.6%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 2.4k / P 2.9k
ΔOI:      C +0.2k / P +53
ATM:      C 4.00 / P 3.35
ATM IV:   69.0%
ΔOI Δ Exposure*: 7k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 65 ｜ +198 ｜ $1.60 ｜ 名义 $31.7k* ｜ +9.3%
C 63 ｜ +23 ｜ $2.27 ｜ 名义 $5.2k* ｜ +5.9%
P 52 ｜ +20 ｜ $0.80 ｜ 名义 $1.6k* ｜ -12.6%
结构参考：65（+9.3%）上方 / 52（-12.6%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

   Top ΔOI: 80C -218 ｜ 70C +165

Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-25/MP_evening.json