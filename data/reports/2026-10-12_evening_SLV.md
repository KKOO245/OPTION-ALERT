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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 54.72 → 收盘 54.35（-0.7%） ｜ 今日高 54.74 ｜ 低 54.30 ｜ 昨收 54.78 → 收盘 54.35（-0.8%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.60 | OI比 0.72 | ATM IV 35.3% | Skew -0.9pp | Term 0.94 | ExpMove ±2.1%（近端） | Rank 57%
量化视角： IV 中性（Rank 57%）｜期限结构正常（Term 0.94）｜Put 保护异常便宜（Skew -0.9pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.72）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.60×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.72×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-14（2D）±2.1% ｜ 10-16（4D）±2.9% ｜ 10-19（7D）±3.2% ｜ 10-21（9D）±3.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 46,066,824 | GEX Change vs 上次快照 -23,518,480 | Flip: Primary Flip: 53.06（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 639 / LOW 162 / INVALID 423
结构观察区: Primary Flip 53.06（全链重定价，覆盖 95%）
Put Wall 50（弱结构｜现价高于该位 8.7%）
最近结构参考: Flip 53（现价高于该位 2.4%）
量化视角： 正 Gamma（4607万，无历史分位）｜正 Gamma 减弱（2352万）｜现价位于 Flip 上方 2.43%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 50（Put Wall，弱结构）；上方 55（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 53（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-14  C +0 / P +0 ｜ Activity LOW ｜ 2D
10-16  C +0 / P +0 ｜ Activity LOW ｜ 4D
10-19  C +0 / P +0 ｜ Activity LOW ｜ 7D
10-21  C +0 / P +0 ｜ Activity LOW ｜ 9D

📆 10-14 Forward Structure
存量OI: C 11.8k / P 8.5k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $0.51 / P $0.61 ｜ ATM IV 35.3%，净 delta 敞口 0 shares
仓位参考: Max Pain 55 ｜ Call Wall 57（+4.9%，弱）（OI 1.2k） ｜ Put Wall 53.5（-1.6%，弱）（OI 1.2k）
量化解读： 存量 Call 重｜ATM IV 35.3%｜历史 Rank 57%（近端代理）｜IV/RV 1.10×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-16（Activity LOW）仓位参考: Max Pain 56 ｜ Call Wall 50（-8.0%，弱）（OI 27.0k） ｜ Put Wall 50（-8.0%，弱）（OI 23.3k）

10-19（Activity LOW）仓位参考: Max Pain 54 ｜ Call Wall 56（+3.0%，弱）（OI 0.3k） ｜ Put Wall 55.5（+2.1%，弱）（OI 0.2k）

10-21（Activity LOW）仓位参考: Max Pain 54 ｜ Call Wall 53.5（-1.6%，弱）（OI 0.5k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-12/SLV_evening.json