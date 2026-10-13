# 期权晚报 2026-10-13（快照 16:40 ET）

📊 市场环境

SPY $778.01 ｜ QQQ $743.57
VIX 15.27 ↑0.4%（5D +1.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 44.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-13

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-13 10:00　【高】成屋销售　预测 3.95 ｜ 实际 3.99 ｜ 前值 3.93　✅ 今日已公布
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.6 ｜ 实际 待公布 ｜ 前值 3.4
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 待公布 ｜ 前值 2.4
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览
🟡 **事件差分**: 10-16 ATM IV 83.8% vs 10-23 72.5%（差 +11.3pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 13.81 → 收盘 14.35（+3.9%） ｜ 今日高 14.44 ｜ 低 13.71 ｜ 昨收 14.29 → 收盘 14.35（+0.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.72 | OI比 0.20 | ATM IV 83.8% | Skew -6.9pp | Term 0.86 | ExpMove ±6.3%（近端） | Rank 16%
量化视角： IV 历史低位（Rank 16%，期权偏便宜）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜Put 保护异常便宜（Skew -6.9pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.20）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.72×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.20×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（3D）±6.3% ｜ 10-23（10D）±8.0% ｜ 10-30（17D）±16.1% ｜ 11-06（24D）±12.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 849,440 | GEX Change vs 上次快照 841,269 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 138 / LOW 105 / INVALID 161
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: NO_CROSS
Put Wall 14（弱结构｜现价高于该位 2.5%）
最近结构参考: Put Wall 14（现价高于该位 2.5%）
量化视角： 正 Gamma（85万，无历史分位）｜正 Gamma 增强（+84万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 14（Put Wall，弱结构）；上方 17（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +0.5k / P -1.0k ｜ Activity MEDIUM △ ｜ 3D
10-23  C +0.2k / P +0.1k ｜ Activity MEDIUM △ ｜ 10D
10-30  C +57 / P +18 ｜ Activity LOW ｜ 17D
11-06  C +18 / P +42 ｜ Activity LOW ｜ 24D

📆 10-16 Forward Structure
存量OI: C 22.4k / P 4.6k，今日变化ΔOI: C +0.5k / P -1.0k，平值价格ATM: C $0.28 / P $0.63 ｜ ATM IV 83.8%，净 delta 敞口 114k shares
Top ΔOI: P 20 -327 ｜ P 18 -282 ｜ C 15 +227
仓位参考: Max Pain 17 ｜ Put Wall 15（+4.5%，弱）（OI 1.0k）
量化解读： 存量 Call 重｜ATM IV 83.8%｜历史 Rank 16%（近端代理）｜IV/RV 1.54×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 114,162 股

10-23（MEDIUM △）Top ΔOI: 14P +158 ｜ 14C +51
10-23（MEDIUM △）仓位参考: Max Pain 16 ｜ Put Wall 14（-2.4%）（OI 0.6k）

10-30（Activity LOW）仓位参考: Max Pain 16 ｜ Put Wall 14（-2.4%）（OI 0.3k）

11-06（Activity LOW）仓位参考: Max Pain 16 ｜ Put Wall 15.5（+8.0%，弱）（OI 63）

📅 事件差分（观察，非因果）: 10-16（3D）ATM IV 83.8% vs 10-23 72.5%（差 +11.3pp）——覆盖 成屋销售、Core Inflation Rate MoM 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-13/NNE_evening.json