# 期权晚报 2026-10-15（快照 21:00 ET）

📊 市场环境

SPY $771.79 ｜ QQQ $728.00
VIX 16.46 ↓2.4%（5D +6.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-15

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 1.3 ｜ 前值 0.5　✅ 今日已公布
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 0.8 ｜ 前值 1.3　✅ 今日已公布
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布　⏰ 今日

🔍 重点速览
🔴 **事件差分**: 10-16（1D）ATM IV 90.4% vs 10-23 73.2%（差 +17.2pp），覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 12.50 → 收盘 13.59（+8.7%） ｜ 今日高 13.64 ｜ 低 12.01 ｜ 昨收 13.01 → 收盘 13.59（+4.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.04 | OI比 0.17 | ATM IV 90.4% | Skew 14.3pp | Term 0.82 | ExpMove ±3.7%（近端） | Rank 23%
量化视角： IV 历史低位（Rank 23%，期权偏便宜）｜期限结构倒挂（Term 0.82，近月 IV 高于远月）｜保护溢价显著（Skew 14.3pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.17）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.04×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.17×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（1D）±3.7% ｜ 10-23（8D）±9.8% ｜ 10-30（15D）±10.3% ｜ 11-06（22D）±22.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 432,500 | GEX Change vs 上次快照 501,546 | Flip: Primary Flip: 13.13（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 160 / LOW 104 / INVALID 152
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 13.13（全链重定价，覆盖 90%）
Put Wall 14（弱结构｜现价低于该位 2.9%）
最近结构参考: Put Wall 14（现价低于该位 2.9%）
量化视角： 正 Gamma（43万，无历史分位）｜由负转正（+50万）｜现价位于 Flip 上方 3.49%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 14（Put Wall，弱结构） / 15（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 13（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +0 / P +0 ｜ Activity LOW ｜ 1D
10-23  C +0 / P +0 ｜ Activity LOW ｜ 8D
10-30  C +0 / P +0 ｜ Activity LOW ｜ 15D
11-06  C +0 / P +0 ｜ Activity LOW ｜ 22D

📆 10-16 Forward Structure
存量OI: C 23.1k / P 3.9k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $0.25 / P $0.25 ｜ ATM IV 90.4%，净 delta 敞口 0 shares
仓位参考: Max Pain 15 ｜ Put Wall 13（-4.3%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 90.4%｜历史 Rank 23%（近端代理）｜IV/RV 1.69×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-23（Activity LOW）仓位参考: Max Pain 16 ｜ Put Wall 14（+3.0%）（OI 0.6k）

10-30（Activity LOW）仓位参考: Max Pain 16 ｜ Put Wall 14（+3.0%）（OI 0.4k）

11-06（Activity LOW）仓位参考: Max Pain 16 ｜ Put Wall 13（-4.3%，弱）（OI 76）

📅 事件差分（观察，非因果）: 10-16（1D）ATM IV 90.4% vs 10-23 73.2%（差 +17.2pp）——覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-15/NNE_evening.json