# 期权晚报 2026-08-25

📊 市场环境

SPY $764.92 ｜ QQQ $709.44
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
GDX: 今晨 103.10 → 收盘 105.02（+1.9%） ｜ 今日高 105.25 ｜ 低 101.81
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞


## GDX

Options: P/C量 2.21 | OI比 0.63 | ATM IV 56.8% | Skew -1.1pp | Term 0.86 | ExpMove ±4.2% | Rank — (历史不足)
   ⇒ Put/Call Volume: 2.21×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.63×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: ≈54.78 / ≈65.01 / ≈103.03
结构观察区: 55–65（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 80: +31.3% | 距 Call Wall 104: +1.0%
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 80（Put Wall）；上方 104（Call Wall）。
• Gamma 区域：切换参考 55（Top-3 近似，需全链重定价验证）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

08-28  C +11.0k / P +10.7k ｜ Activity HIGH ｜ 3D
09-04  C +0.3k / P +0.8k ｜ Activity HIGH ｜ 10D
09-11  C +0.2k / P +0.1k ｜ Activity MEDIUM △ ｜ 17D
09-18  C +10.2k / P +7.3k ｜ Activity HIGH ｜ 24D

📆 08-28 Forward Structure
OI:       C 118.4k / P 74.2k
ΔOI:      C +11.0k / P +10.7k
ATM:      C 2.17 / P 2.17
ATM IV:   56.8%
ΔOI Δ Exposure*: 204k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 98 ｜ +3,535 ｜ $0.23 ｜ 名义 $81.3k* ｜ -6.7%
P 95 ｜ +3,254 ｜ $0.09 ｜ 名义 $29.3k* ｜ -9.5%
C 115 ｜ +3,001 ｜ $0.14 ｜ 名义 $42.0k* ｜ +9.5%
结构参考：115（+9.5%）上方 / 98（-6.7%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-04 Forward Structure
OI:       C 12.3k / P 40.2k
ΔOI:      C +0.3k / P +0.8k
ATM:      C 3.66 / P 3.57
ATM IV:   51.0%
ΔOI Δ Exposure*: -22k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 110 ｜ +305 ｜ $1.77 ｜ 名义 $54.0k* ｜ +4.7%
C 94 ｜ -296 ｜ $10.47 ｜ 名义 $-309.9k* ｜ -10.5%
P 100 ｜ +190 ｜ $1.53 ｜ 名义 $29.1k* ｜ -4.8%
结构参考：110（+4.7%）上方 / 100（-4.8%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

   Top ΔOI: 105C +107 ｜ 104C +106

📆 09-18 Forward Structure
OI:       C 251.9k / P 365.9k
ΔOI:      C +10.2k / P +7.3k
ATM:      C 5.45 / P 5.20
ATM IV:   49.2%
ΔOI Δ Exposure*: 22k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 135 ｜ +6,627 ｜ $0.31 ｜ 名义 $205.4k* ｜ +28.6%
P 90 ｜ +3,290 ｜ $0.65 ｜ 名义 $213.8k* ｜ -14.3%
C 115 ｜ +2,316 ｜ $2.13 ｜ 名义 $493.3k* ｜ +9.5%
结构参考：135（+28.6%）上方 / 90（-14.3%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-25/GDX_evening.json