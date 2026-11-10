# 期权晚报 2026-11-09（快照 21:00 ET）

📊 市场环境

SPY $752.69 ｜ QQQ $679.35
VIX 19.92 ↓22.3%（5D -5.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-09

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-10 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周二 11-10 08:30　【高】Core Inflation Rate YoY　预测 2.8 ｜ 实际 待公布 ｜ 前值 2.6
- 周二 11-10 08:30　【高】Inflation Rate MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.6
- 周二 11-10 08:30　【高】Inflation Rate YoY　预测 3.9 ｜ 实际 待公布 ｜ 前值 3.7
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🔴 **事件差分**: 11-13（4D）ATM IV 118.1% vs 11-20 100.6%（差 +17.5pp），覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY 等
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 182.24 → 收盘 193.88（+6.4%） ｜ 今日高 199.83 ｜ 低 180.50 ｜ 昨收 173.24 → 收盘 193.88（+11.9%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.65 | OI比 0.78 | ATM IV 118.1% | Skew 9.6pp | Term 0.76 | ExpMove ±9.9%（近端） | Rank 75%
量化视角： IV 历史高位（Rank 75%，期权偏贵）｜期限结构倒挂（Term 0.76，近月 IV 高于远月）｜保护溢价显著（Skew 9.6pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.78）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.65×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.78×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（4D）±9.9% ｜ 11-20（11D）±14.0% ｜ 11-27（18D）±16.1% ｜ 12-04（25D）±19.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -5,014,778 | GEX Change vs 上次快照 -1,293,296 | Flip: Primary Flip: 212.11（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 574 / LOW 123 / INVALID 231
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 212.11（全链重定价，覆盖 100%）
Put Wall 200（现价低于该位 3.1%）
最近结构参考: Put Wall 200（现价低于该位 3.1%）
量化视角： 负 Gamma（501万，无历史分位）｜负 Gamma 加深（129万）｜现价位于 Flip 下方 8.60%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 185（MaxPain，仅结算参考）；上方 200（Put Wall）。
• Gamma 区域：切换参考 212（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +0 / P +0 ｜ Activity LOW ｜ 4D
11-20  C +0 / P +0 ｜ Activity LOW ｜ 11D
11-27  C +0 / P +0 ｜ Activity LOW ｜ 18D
12-04  C +0 / P +0 ｜ Activity LOW ｜ 25D

📆 11-13 Forward Structure
存量OI: C 30.8k / P 24.1k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $9.25 / P $10.00 ｜ ATM IV 118.1%，净 delta 敞口 0 shares
仓位参考: Max Pain 185 ｜ Call Wall 180（-7.2%）（OI 2.4k） ｜ Put Wall 175（-9.7%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 118.1%｜历史 Rank 75%（近端代理）｜IV/RV 1.00×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-20（Activity LOW）仓位参考: Max Pain 220 ｜ Call Wall 200（+3.2%，弱）（OI 3.5k） ｜ Put Wall 200（+3.2%，弱）（OI 5.4k）

11-27（Activity LOW）仓位参考: Max Pain 220 ｜ Call Wall 200（+3.2%，弱）（OI 0.6k） ｜ Put Wall 190（-2.0%，弱）（OI 1.2k）

12-04（Activity LOW）仓位参考: Max Pain 205 ｜ Call Wall 200（+3.2%，弱）（OI 0.6k） ｜ Put Wall 200（+3.2%）（OI 1.6k）

📅 事件差分（观察，非因果）: 11-13（4D）ATM IV 118.1% vs 11-20 100.6%（差 +17.5pp）——覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-09/BE_evening.json