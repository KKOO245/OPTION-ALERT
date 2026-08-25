# 期权晚报 2026-08-25

📊 市场环境

SPY $765.00 ｜ QQQ $709.46
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
XBI: 今晨 168.13 → 收盘 169.59（+0.9%） ｜ 今日高 169.88 ｜ 低 165.79
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞


## XBI

Options: P/C量 1.33 | OI比 1.41 | ATM IV 39.0% | Skew 0.4pp | Term 0.85 | ExpMove ±2.9% | Rank — (历史不足)
   ⇒ Put/Call Volume: 1.33×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.41×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: ≈80.03 / ≈159.29 / ≈159.31
结构观察区: 80–159（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 150: +13.1% | 距 Call Wall 155: +9.4%
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（Put Wall）；上方 155（Call Wall）。
• Gamma 区域：切换参考 80（Top-3 近似，需全链重定价验证）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

08-28  C +0.3k / P +0.9k ｜ Activity HIGH ｜ 3D
09-04  C -28 / P +0.6k ｜ Activity HIGH ｜ 10D
09-11  C +21 / P +46 ｜ Activity MEDIUM △ ｜ 17D
09-18  C +1.2k / P +14.8k ｜ Activity HIGH ｜ 24D

📆 08-28 Forward Structure
OI:       C 7.2k / P 10.2k
ΔOI:      C +0.3k / P +0.9k
ATM:      C 1.90 / P 2.93
ATM IV:   39.0%
ΔOI Δ Exposure*: 13k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 162 ｜ +265 ｜ $0.47 ｜ 名义 $12.5k* ｜ -4.2%
C 163 ｜ +185 ｜ $6.45 ｜ 名义 $119.3k* ｜ -3.9%
P 156 ｜ +168 ｜ $0.06 ｜ 名义 $1.0k* ｜ -8.0%
结构参考：162（-4.2%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-04 Forward Structure
OI:       C 2.2k / P 2.2k
ΔOI:      C -28 / P +0.6k
ATM:      C 3.36 / P 4.12
ATM IV:   34.9%
ΔOI Δ Exposure*: -8k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 155 ｜ +270 ｜ $0.40 ｜ 名义 $10.8k* ｜ -8.6%
C 167 ｜ -91 ｜ $5.30 ｜ 名义 $-48.2k* ｜ -1.5%
P 160 ｜ +81 ｜ $0.91 ｜ 名义 $7.4k* ｜ -5.7%
结构参考：155（-8.6%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

   Top ΔOI: 155P +31 ｜ 151C +22

📆 09-18 Forward Structure
OI:       C 66.8k / P 92.7k
ΔOI:      C +1.2k / P +14.8k
ATM:      C 5.45 / P 5.95
ATM IV:   33.8%
ΔOI Δ Exposure*: -192k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 160 ｜ +4,513 ｜ $2.27 ｜ 名义 $1.02M* ｜ -5.7%
P 147 ｜ +3,999 ｜ $0.45 ｜ 名义 $180.0k* ｜ -13.3%
P 156 ｜ +2,029 ｜ $1.38 ｜ 名义 $280.0k* ｜ -8.0%
结构参考：160（-5.7%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-25/XBI_evening.json