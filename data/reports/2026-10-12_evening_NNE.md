# 期权晚报 2026-10-12（快照 21:00 ET）

📊 市场环境

SPY $778.10 ｜ QQQ $746.04
VIX 15.21 ↑2.5%（5D -2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 45.7（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-12

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-13 10:00　【高】成屋销售　预测 3.96 ｜ 实际 待公布 ｜ 前值 3.98
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.7 ｜ 实际 待公布 ｜ 前值 3.4
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 待公布 ｜ 前值 2.4
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **事件差分**: 10-16 ATM IV 83.9% vs 10-23 72.2%（差 +11.8pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 15.03 → 收盘 14.29（-4.9%） ｜ 今日高 15.04 ｜ 低 14.23 ｜ 昨收 15.34 → 收盘 14.29（-6.8%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.79 | OI比 0.25 | ATM IV 83.9% | Skew 0.2pp | Term 0.87 | ExpMove ±6.7%（近端） | Rank 15%
量化视角： IV 历史低位（Rank 15%，期权偏便宜）｜期限结构倒挂（Term 0.87，近月 IV 高于远月）｜保护溢价薄（Skew 0.2pp）｜存量 Call 偏重（OI比 0.25）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.79×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.25×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（4D）±6.7% ｜ 10-23（11D）±8.8% ｜ 10-30（18D）±16.2% ｜ 11-06（25D）±12.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 65,831 | GEX Change vs 上次快照 623,105 | Flip: Primary Flip: 14.19（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 143 / LOW 96 / INVALID 165
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 14.19（全链重定价，覆盖 95%）
Put Wall 15（弱结构｜现价低于该位 4.7%）
最近结构参考: Flip 14（现价高于该位 0.7%）
量化视角： 正 Gamma（7万，无历史分位）｜由负转正（+62万）｜现价位于 Flip 上方 0.72%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 15（Put Wall，弱结构） / 18（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 14（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +0 / P +0 ｜ Activity LOW ｜ 4D
10-23  C +0 / P +0 ｜ Activity LOW ｜ 11D
10-30  C +0 / P +0 ｜ Activity LOW ｜ 18D
11-06  C +0 / P +0 ｜ Activity LOW ｜ 25D

📆 10-16 Forward Structure
存量OI: C 21.9k / P 5.6k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $0.37 / P $0.58 ｜ ATM IV 83.9%，净 delta 敞口 0 shares
仓位参考: Max Pain 18 ｜ Put Wall 15（+5.0%，弱）（OI 1.0k）
量化解读： 存量 Call 重｜ATM IV 83.9%｜历史 Rank 15%（近端代理）｜IV/RV 1.40×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-23（Activity LOW）仓位参考: Max Pain 17 ｜ Put Wall 14（-2.0%，弱）（OI 0.5k）

10-30（Activity LOW）仓位参考: Max Pain 16 ｜ Put Wall 14（-2.0%）（OI 0.3k）

11-06（Activity LOW）仓位参考: Max Pain 16 ｜ Put Wall 15.5（+8.5%，弱）（OI 63）

📅 事件差分（观察，非因果）: 10-16（4D）ATM IV 83.9% vs 10-23 72.2%（差 +11.8pp）——覆盖 成屋销售、Core Inflation Rate MoM 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-12/NNE_evening.json