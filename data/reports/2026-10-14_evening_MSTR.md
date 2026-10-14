# 期权晚报 2026-10-14（快照 16:42 ET）

📊 市场环境

SPY $769.60 ｜ QQQ $728.95
VIX 16.87 ↑10.5%（5D +11.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 32.4（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-14

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 2.6 ｜ 前值 2.4　✅ 今日已公布
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.6 ｜ 实际 3.7 ｜ 前值 3.4　✅ 今日已公布
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 0.6 ｜ 前值 0.4　✅ 今日已公布
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览
🔴 **事件差分**: 10-16（2D）ATM IV 86.4% vs 10-23 70.6%（差 +15.7pp），覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY、Inflation Rate YoY、Inflation Rate MoM、PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 10-16 149P ΔOI +1,124（距现价 +4.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 149.70 → 收盘 143.24（-4.3%） ｜ 今日高 152.18 ｜ 低 141.74 ｜ 昨收 152.18 → 收盘 143.24（-5.9%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.62 | OI比 0.67 | ATM IV 86.4% | Skew 4.8pp | Term 0.81 | ExpMove ±5.1%（近端） | Rank 61%
量化视角： IV 中性（Rank 61%）｜期限结构倒挂（Term 0.81，近月 IV 高于远月）｜保护溢价中性（Skew 4.8pp）｜存量 Call 偏重（OI比 0.67）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.62×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.67×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（2D）±5.1% ｜ 10-23（9D）±9.0% ｜ 10-30（16D）±11.9% ｜ 11-06（23D）±14.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) -610,037 | GEX Change vs 上次快照 -25,053,320 | Flip: Primary Flip: 143.36（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 620 / LOW 81 / INVALID 183
结构观察区: Primary Flip 143.36（全链重定价，覆盖 100%）
最近结构参考: Flip 143（现价低于该位 0.1%）
量化视角： 负 Gamma（61万，无历史分位）｜由正转负（2505万）｜现价位于 Flip 下方 0.08%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 142（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 143（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +3.9k / P +0.8k ｜ Activity MEDIUM △ ｜ 2D
10-23  C +2.2k / P +7.0k ｜ Activity HIGH ｜ 9D
10-30  C +1.0k / P +2.2k ｜ Activity MEDIUM △ ｜ 16D
11-06  C +0.4k / P +1.0k ｜ Activity HIGH ｜ 23D

📆 10-16 Forward Structure
存量OI: C 352.6k / P 234.8k，今日变化ΔOI: C +3.9k / P +0.8k，平值价格ATM: C $3.80 / P $3.50 ｜ ATM IV 86.4%，净 delta 敞口 -12k shares
Top ΔOI: C 155 +1,165 ｜ P 149 +1,124 ｜ P 162 -983
仓位参考: Max Pain 142 ｜ Call Wall 157.5（+10.0%，弱）（OI 40.7k） ｜ Put Wall 140（-2.3%，弱）（OI 7.3k）
量化解读： 存量 Call 重｜ATM IV 86.4%｜历史 Rank 61%（近端代理）｜IV/RV 2.39×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 12,248 股

📆 10-23 Forward Structure
存量OI: C 46.2k / P 96.4k，今日变化ΔOI: C +2.2k / P +7.0k，平值价格ATM: C $6.75 / P $6.20 ｜ ATM IV 70.6%，净 delta 敞口 -237k shares
Top ΔOI: P 145 +1,306 ｜ P 135 +877
仓位参考: Max Pain 158 ｜ Call Wall 155（+8.2%，弱）（OI 1.9k）
量化解读： 存量 Put 重｜ATM IV 70.6%｜历史 Rank 61%（近端代理）｜IV/RV 1.95×（近似）｜净 delta 敞口 负 237,454 股

10-30（MEDIUM △）Top ΔOI: 120P +435 ｜ 125P +335
10-30（MEDIUM △）仓位参考: Max Pain 160 ｜ Call Wall 155（+8.2%，弱）（OI 1.4k） ｜ Put Wall 155（+8.2%，弱）（OI 3.4k）

📆 11-06 Forward Structure
存量OI: C 10.3k / P 20.1k，今日变化ΔOI: C +0.4k / P +1.0k，平值价格ATM: C $10.80 / P $10.18 ｜ ATM IV 72.7%，净 delta 敞口 -12k shares
Top ΔOI: P 115 +408 ｜ P 165 -336 ｜ P 150 +252
仓位参考: Max Pain 160 ｜ Call Wall 152.5（+6.5%，弱）（OI 0.7k） ｜ Put Wall 155（+8.2%，弱）（OI 2.9k）
量化解读： 存量 Put 重｜ATM IV 72.7%｜历史 Rank 61%（近端代理）｜IV/RV 2.01×（近似）｜净 delta 敞口 负 12,407 股

📅 事件差分（观察，非因果）: 10-16（2D）ATM IV 86.4% vs 10-23 70.6%（差 +15.7pp）——覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY、Inflation Rate YoY、Inflation Rate MoM、PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-14/MSTR_evening.json