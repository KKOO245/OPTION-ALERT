# 期权晚报 2026-11-16（快照 21:00 ET）

📊 市场环境

SPY $739.95 ｜ QQQ $661.75
VIX 22.91 ↑18.7%（5D +15.0%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 31.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-17 08:30　【高】零售销售 MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.8
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 待公布 ｜ 前值 1.221
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 待公布 ｜ 前值 1.4

🔍 重点速览
🟡 **事件差分**: 11-20 ATM IV 84.2% vs 11-27 70.0%（差 +14.1pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 37.50 → 收盘 36.09（-3.8%） ｜ 今日高 38.24 ｜ 低 36.06 ｜ 昨收 38.76 → 收盘 36.09（-6.9%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-23，窗口结束前不做对错判定）

Options: P/C成交量 0.57 | OI比 0.49 | ATM IV 84.2% | Skew -0.0pp | Term 0.81 | ExpMove ±8.4%（近端） | Rank 78%
量化视角： IV 历史高位（Rank 78%，期权偏贵）｜期限结构倒挂（Term 0.81，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.0pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.49）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.57×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.49×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（4D）±8.4% ｜ 11-27（11D）±9.1% ｜ 12-04（18D）±11.5% ｜ 12-11（25D）±16.0%
   ⇒ IV–VIX Spread: +61.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 3,275,054 | GEX Change vs 上次快照 -3,016,989 | Flip: Primary Flip: 34.20（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 233 / LOW 61 / INVALID 144
结构观察区: Primary Flip 34.20（全链重定价，覆盖 100%）
Put Wall 35（现价高于该位 3.1%）
最近结构参考: Put Wall 35（现价高于该位 3.1%）
量化视角： 正 Gamma（328万，无历史分位）｜正 Gamma 减弱（302万）｜现价位于 Flip 上方 5.53%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 35（Put Wall）；上方 40（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 34（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C +0 / P +0 ｜ Activity LOW ｜ 4D
11-27  C +0 / P +0 ｜ Activity LOW ｜ 11D
12-04  C +0 / P +0 ｜ Activity LOW ｜ 18D
12-11  C +0 / P +0 ｜ Activity LOW ｜ 25D

📆 11-20 Forward Structure
存量OI: C 28.2k / P 13.8k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $1.82 / P $1.20 ｜ ATM IV 84.2%，净 delta 敞口 0 shares
仓位参考: Max Pain 40 ｜ Call Wall 39.5（+9.4%，弱）（OI 1.7k） ｜ Put Wall 35（-3.0%）（OI 3.9k）
量化解读： 存量 Call 重｜ATM IV 84.2%｜历史 Rank 78%（近端代理）｜IV/RV 1.28×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-27（Activity LOW）仓位参考: Max Pain 42 ｜ Put Wall 33（-8.6%）（OI 2.5k）

12-04（Activity LOW）仓位参考: Max Pain 35 ｜ Call Wall 35（-3.0%）（OI 0.5k） ｜ Put Wall 34（-5.8%）（OI 0.2k）

12-11（Activity LOW）仓位参考: Max Pain 42 ｜ Call Wall 37（+2.5%，弱）（OI 68） ｜ Put Wall 37（+2.5%，弱）（OI 31）

📅 事件差分（观察，非因果）: 11-20（4D）ATM IV 84.2% vs 11-27 70.0%（差 +14.1pp）——覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-16/MP_evening.json