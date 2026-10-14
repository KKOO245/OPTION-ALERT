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
🟡 **事件差分**: 10-16 ATM IV 45.7% vs 10-19 34.8%（差 +10.8pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-19 225C ΔOI +1,430（距现价 +1.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 225.60 → 收盘 221.30（-1.9%） ｜ 今日高 226.00 ｜ 低 219.64 ｜ 昨收 228.52 → 收盘 221.30（-3.2%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-21，窗口结束前不做对错判定）

Options: P/C成交量 0.77 | OI比 0.91 | ATM IV 71.2% | Skew -2.3pp | Term 0.47 | ExpMove ±2.8%（近端） | Rank 91%
量化视角： IV 历史高位（Rank 91%，期权偏贵）｜期限结构倒挂（Term 0.47，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.3pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.77×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.91×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（2D）±2.8% ｜ 10-19（5D）±3.4% ｜ 10-21（7D）±4.1% ｜ 10-23（9D）±4.5%
   ⇒ IV–VIX Spread: +54.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 158,580,678 | GEX Change vs 上次快照 -138,127,539 | Flip: Primary Flip: 215.52（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 701 / LOW 223 / INVALID 638
结构观察区: Primary Flip 215.52（全链重定价，覆盖 96%）
Put Wall 220（弱结构｜现价高于该位 0.6%） | Call Wall 240（弱结构｜现价低于该位 7.8%）
最近结构参考: Put Wall 220（现价高于该位 0.6%）
量化视角： 正 Gamma（1.59亿，无历史分位）｜正 Gamma 减弱（1.38亿）｜现价位于 Flip 上方 2.68%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 220（Put Wall，弱结构）；上方 228（MaxPain，仅结算参考） / 240（Call Wall，弱结构）。
• Gamma 区域：切换参考 216（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +32.8k / P +12.7k ｜ Activity MEDIUM △ ｜ 2D
10-19  C +11.4k / P +3.5k ｜ Activity HIGH ｜ 5D
10-21  C +11.7k / P +6.1k ｜ Activity HIGH ｜ 7D
10-23  C +10.6k / P +5.6k ｜ Activity HIGH ｜ 9D

📆 10-16 Forward Structure
存量OI: C 1076.0k / P 829.4k，今日变化ΔOI: C +32.8k / P +12.7k，平值价格ATM: C $2.59 / P $3.50 ｜ ATM IV 45.7%，净 delta 敞口 37k shares
Top ΔOI: C 237 +11,047 ｜ C 235 +8,251 ｜ C 240 +4,380
仓位参考: Max Pain 220 ｜ Call Wall 220（-0.6%，弱）（OI 99.0k） ｜ Put Wall 220（-0.6%，弱）（OI 68.0k）
量化解读： 存量 Call 重｜ATM IV 45.7%｜历史 Rank 91%（近端代理）｜IV/RV 2.45×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 37,366 股

📆 10-19 Forward Structure
存量OI: C 48.7k / P 18.4k，今日变化ΔOI: C +11.4k / P +3.5k，平值价格ATM: C $3.16 / P $4.30 ｜ ATM IV 34.8%，净 delta 敞口 85k shares
Top ΔOI: C 242 +2,160 ｜ C 225 +1,430
仓位参考: Max Pain 230 ｜ Call Wall 235（+6.2%，弱）（OI 4.1k） ｜ Put Wall 230（+3.9%）（OI 4.3k）
量化解读： 存量 Call 重｜ATM IV 34.8%｜历史 Rank 91%（近端代理）｜IV/RV 1.87×（近似）｜净 delta 敞口 正 84,843 股

📆 10-21 Forward Structure
存量OI: C 21.7k / P 12.6k，今日变化ΔOI: C +11.7k / P +6.1k，平值价格ATM: C $3.92 / P $5.06 ｜ ATM IV 35.6%，净 delta 敞口 -88k shares
Top ΔOI: P 220 +3,051 ｜ C 240 +3,047 ｜ C 230 +2,673
仓位参考: Max Pain 228 ｜ Call Wall 240（+8.5%）（OI 6.7k） ｜ Put Wall 220（-0.6%）（OI 3.3k）
量化解读： 存量 Call 重｜ATM IV 35.6%｜历史 Rank 91%（近端代理）｜IV/RV 1.91×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 88,305 股

📆 10-23 Forward Structure
存量OI: C 169.7k / P 134.8k，今日变化ΔOI: C +10.6k / P +5.6k，平值价格ATM: C $4.60 / P $5.45 ｜ ATM IV 35.4%，净 delta 敞口 -30k shares
Top ΔOI: C 227 +1,364
仓位参考: Max Pain 228 ｜ Call Wall 240（+8.5%）（OI 60.1k） ｜ Put Wall 205（-7.4%，弱）（OI 10.7k）
量化解读： 存量 Call 重｜ATM IV 35.4%｜历史 Rank 91%（近端代理）｜IV/RV 1.90×（近似）｜净 delta 敞口 负 30,026 股

📅 事件差分（观察，非因果）: 10-16（2D）ATM IV 45.7% vs 10-19 34.8%（差 +10.8pp）——覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY、Inflation Rate YoY、Inflation Rate MoM、PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-14/NVDA_evening.json