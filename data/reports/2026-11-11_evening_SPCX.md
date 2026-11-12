# 期权晚报 2026-11-11（快照 16:40 ET）

📊 市场环境

SPY $759.81 ｜ QQQ $nan
VIX 17.49 ↓10.1%（5D +5.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 37.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-11

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-13 145C ΔOI +2,870（距现价 +3.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-16 145C ΔOI +2,538 占该期限总 OI 11.1%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SPCX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPCX: 今开 143.40 → 收盘 139.75（-2.5%） ｜ 今日高 145.16 ｜ 低 138.62 ｜ 昨收 143.09 → 收盘 139.75（-2.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.64 | OI比 0.88 | ATM IV 44.9% | Skew -0.3pp | Term 1.30 | ExpMove ±4.5%（近端） | Rank 12%
量化视角： IV 历史低位（Rank 12%，期权偏便宜）｜期限结构正常偏陡（Term 1.30）｜Put 保护异常便宜（Skew -0.3pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.64×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.88×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-13（2D）±4.5% ｜ 11-16（5D）±6.4% ｜ 11-18（7D）±7.8% ｜ 11-20（9D）±9.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 24,333,433 | GEX Change vs 上次快照 -3,380,829 | Flip: Primary Flip: 137.48（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 883 / LOW 230 / INVALID 635
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 137.48（全链重定价，覆盖 96%）
Put Wall 135（弱结构｜现价高于该位 3.5%）
最近结构参考: Flip 137（现价高于该位 1.7%）
量化视角： 正 Gamma（2433万，无历史分位）｜正 Gamma 减弱（338万）｜现价位于 Flip 上方 1.65%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 135（Put Wall，弱结构）；上方 140（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 137（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +9.7k / P +9.2k ｜ Activity HIGH ｜ 2D
11-16  C +9.0k / P +1.1k ｜ Activity HIGH ｜ 5D
11-18  C +2.5k / P +10.1k ｜ Activity HIGH ｜ 7D
11-20  C +7.0k / P +4.8k ｜ Activity MEDIUM △ ｜ 9D

📆 11-13 Forward Structure
存量OI: C 194.7k / P 144.1k，今日变化ΔOI: C +9.7k / P +9.2k，平值价格ATM: C $3.07 / P $3.24 ｜ ATM IV 75.8%，净 delta 敞口 -146k shares
Top ΔOI: C 145 +2,870 ｜ P 141 +2,681 ｜ P 135 +1,783
仓位参考: Max Pain 140 ｜ Call Wall 150（+7.3%，弱）（OI 17.2k） ｜ Put Wall 135（-3.4%，弱）（OI 8.8k）
量化解读： 存量 Call 重｜ATM IV 75.8%｜历史 Rank 12%（近端代理）｜IV/RV 1.01×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 146,070 股

📆 11-16 Forward Structure
存量OI: C 17.9k / P 4.9k，今日变化ΔOI: C +9.0k / P +1.1k，平值价格ATM: C $4.35 / P $4.55 ｜ ATM IV 68.0%，净 delta 敞口 199k shares
Top ΔOI: C 145 +2,538 ｜ C 150 +1,029 ｜ C 140 +809
仓位参考: Max Pain 137 ｜ Call Wall 150（+7.3%，弱）（OI 3.3k） ｜ Put Wall 135（-3.4%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 68.0%｜历史 Rank 12%（近端代理）｜IV/RV 0.91×（近似）｜净 delta 敞口 正 198,975 股

📆 11-18 Forward Structure
存量OI: C 7.7k / P 12.3k，今日变化ΔOI: C +2.5k / P +10.1k，平值价格ATM: C $5.30 / P $5.55 ｜ ATM IV 70.1%，净 delta 敞口 -262k shares
Top ΔOI: P 135 +8,752
仓位参考: Max Pain 135 ｜ Call Wall 145（+3.8%，弱）（OI 0.9k） ｜ Put Wall 135（-3.4%）（OI 8.9k）
量化解读： 存量 Put 重｜ATM IV 70.1%｜历史 Rank 12%（近端代理）｜IV/RV 0.94×（近似）｜净 delta 敞口 负 262,030 股

11-20（MEDIUM △）Top ΔOI: 145C +1,921 ｜ 142P +1,427
11-20（MEDIUM △）仓位参考: Max Pain 145 ｜ Call Wall 145（+3.8%，弱）（OI 40.2k） ｜ Put Wall 130（-7.0%，弱）（OI 33.9k）

📅 事件差分（观察，非因果）: 11-13（2D）ATM IV 75.8% vs 11-16 68.0%（差 +7.8pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-11/SPCX_evening.json