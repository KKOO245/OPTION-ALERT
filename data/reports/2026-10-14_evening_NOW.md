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
🟡 **事件差分**: 10-16 ATM IV 65.6% vs 10-23 53.9%（差 +11.7pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-16 140C ΔOI -1,799（距现价 +0.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NOW

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NOW: 今开 139.49 → 收盘 139.98（+0.4%） ｜ 今日高 142.80 ｜ 低 138.39 ｜ 昨收 138.61 → 收盘 139.98（+1.0%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-21，窗口结束前不做对错判定）

Options: P/C成交量 0.48 | OI比 0.81 | ATM IV 65.6% | Skew 0.4pp | Term 0.96 | ExpMove ±3.9%（近端） | Rank 93%
量化视角： IV 历史高位（Rank 93%，期权偏贵）｜期限结构正常（Term 0.96）｜保护溢价薄（Skew 0.4pp）｜存量 Call 偏重（OI比 0.81）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.48×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.81×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（2D）±3.9% ｜ 10-23（9D）±6.9% ｜ 10-30（16D）±12.2% ｜ 11-06（23D）±13.9%
   ⇒ IV–VIX Spread: +48.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 16,177,961 | GEX Change vs 上次快照 -2,593,970 | Flip: Primary Flip: 134.76（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 552 / LOW 28 / INVALID 58
结构观察区: Primary Flip 134.76（全链重定价，覆盖 100%）
Call Wall 150（现价低于该位 6.7%）
最近结构参考: Flip 135（现价高于该位 3.9%）
量化视角： 正 Gamma（1618万，无历史分位）｜正 Gamma 减弱（259万）｜现价位于 Flip 上方 3.87%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 132（MaxPain，仅结算参考）；上方 150（Call Wall）。
• Gamma 区域：切换参考 135（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C -0.9k / P +2.4k ｜ Activity HIGH ｜ 2D
10-23  C +0.9k / P +1.2k ｜ Activity HIGH ｜ 9D
10-30  C +1.1k / P +1.1k ｜ Activity HIGH ｜ 16D
11-06  C +0.4k / P +0.4k ｜ Activity HIGH ｜ 23D

📆 10-16 Forward Structure
存量OI: C 87.4k / P 70.5k，今日变化ΔOI: C -0.9k / P +2.4k，平值价格ATM: C $2.76 / P $2.73 ｜ ATM IV 65.6%，净 delta 敞口 -205k shares
Top ΔOI: C 140 -1,799 ｜ P 142 +654 ｜ P 137 +615
仓位参考: Max Pain 132 ｜ Call Wall 150（+7.2%）（OI 15.3k） ｜ Put Wall 130（-7.1%，弱）（OI 5.0k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 65.6%｜历史 Rank 93%（近端代理）｜IV/RV 2.39×（近似）｜净 delta 敞口 负 204,711 股

📆 10-23 Forward Structure
存量OI: C 19.6k / P 20.4k，今日变化ΔOI: C +0.9k / P +1.2k，平值价格ATM: C $4.90 / P $4.70 ｜ ATM IV 53.9%，净 delta 敞口 -9k shares
Top ΔOI: C 140 +351 ｜ P 139 +241
仓位参考: Max Pain 136 ｜ Call Wall 145（+3.6%，弱）（OI 1.5k） ｜ Put Wall 130（-7.1%，弱）（OI 0.7k）
量化解读： 存量两侧均衡｜ATM IV 53.9%｜历史 Rank 93%（近端代理）｜IV/RV 1.96×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 8,758 股

📆 10-30 Forward Structure
存量OI: C 10.0k / P 12.5k，今日变化ΔOI: C +1.1k / P +1.1k，平值价格ATM: C $8.91 / P $8.20 ｜ ATM IV 73.5%，净 delta 敞口 6k shares
Top ΔOI: P 130 +770 ｜ C 160 +456 ｜ C 143 +89
仓位参考: Max Pain 135 ｜ Call Wall 150（+7.2%，弱）（OI 1.0k） ｜ Put Wall 130（-7.1%，弱）（OI 1.4k）
量化解读： 存量 Put 重｜ATM IV 73.5%｜历史 Rank 93%（近端代理）｜IV/RV 2.68×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 6,340 股

📆 11-06 Forward Structure
存量OI: C 4.1k / P 3.2k，今日变化ΔOI: C +0.4k / P +0.4k，平值价格ATM: C $10.09 / P $9.33 ｜ ATM IV 67.7%，净 delta 敞口 -5k shares
Top ΔOI: P 131 +63
仓位参考: Max Pain 140 ｜ Call Wall 150（+7.2%，弱）（OI 0.3k） ｜ Put Wall 140（+0.0%）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 67.7%｜历史 Rank 93%（近端代理）｜IV/RV 2.47×（近似）｜净 delta 敞口 负 4,662 股

📅 事件差分（观察，非因果）: 10-16（2D）ATM IV 65.6% vs 10-23 53.9%（差 +11.7pp）——覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY、Inflation Rate YoY、Inflation Rate MoM、PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-14/NOW_evening.json