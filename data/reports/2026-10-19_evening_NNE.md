# 期权晚报 2026-10-19（快照 21:00 ET）

📊 市场环境

SPY $766.48 ｜ QQQ $718.36
VIX 18.44 ↓7.8%（5D +21.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 23.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.4 ｜ 实际 待公布 ｜ 前值 1.403
- 周二 10-20 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.275

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **事件差分**: 10-23 ATM IV 91.9% vs 10-30 77.8%（差 +14.1pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 13.26 → 收盘 13.01（-1.9%） ｜ 今日高 13.32 ｜ 低 12.77 ｜ 昨收 12.88 → 收盘 13.01（+1.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.12 | OI比 0.29 | ATM IV 91.9% | Skew -6.5pp | Term 0.80 | ExpMove ±8.0%（近端） | Rank 28%
量化视角： IV 中性（Rank 28%）｜期限结构倒挂（Term 0.80，近月 IV 高于远月）｜Put 保护异常便宜（Skew -6.5pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.29）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.12×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.29×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（4D）±8.0% ｜ 10-30（11D）±11.4% ｜ 11-06（18D）±14.2% ｜ 11-13（25D）±17.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 274,220 | GEX Change vs 上次快照 14,917 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 147 / LOW 82 / INVALID 169
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: NO_CROSS
Put Wall 14（现价低于该位 7.1%）
最近结构参考: Put Wall 14（现价低于该位 7.1%）
量化视角： 正 Gamma（27万，无历史分位）｜正 Gamma 增强（+1万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 14（Put Wall） / 16（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +0 / P +0 ｜ Activity LOW ｜ 4D
10-30  C +0 / P +0 ｜ Activity LOW ｜ 11D
11-06  C +0 / P +0 ｜ Activity LOW ｜ 18D
11-13  C +0 / P +0 ｜ Activity LOW ｜ 25D

📆 10-23 Forward Structure
存量OI: C 5.8k / P 1.7k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $0.51 / P $0.53 ｜ ATM IV 91.9%，净 delta 敞口 0 shares
仓位参考: Max Pain 16 ｜ Put Wall 14（+7.6%）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 91.9%｜历史 Rank 28%（近端代理）｜IV/RV 1.56×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-30（Activity LOW）仓位参考: Max Pain 15 ｜ Put Wall 14（+7.6%）（OI 0.4k）

11-06（Activity LOW）仓位参考: Max Pain 16 ｜ Put Wall 13（-0.1%，弱）（OI 76）

11-13（Activity LOW）仓位参考: Max Pain 14 ｜ Call Wall 13.5（+3.8%，弱）（OI 50） ｜ Put Wall 12.5（-3.9%）（OI 0.2k）

📅 事件差分（观察，非因果）: 10-23（4D）ATM IV 91.9% vs 10-30 77.8%（差 +14.1pp）——覆盖 建筑许可 Prel、新屋开工
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-19/NNE_evening.json