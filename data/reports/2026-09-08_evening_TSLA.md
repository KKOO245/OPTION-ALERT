# 期权晚报 2026-09-08（快照 17:30 ET）

📊 市场环境

SPY $765.96 ｜ QQQ $718.36
VIX 15.72 ↑2.8%（5D -3.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 40.8（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-10 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0
- 周四 09-10 10:00　【高】成屋销售　预测 3.99 ｜ 实际 待公布 ｜ 前值 4.06
- 周五 09-11 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.2
- 周五 09-11 08:30　【高】Inflation Rate MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.1
- 周五 09-11 08:30　【高】Inflation Rate YoY　预测 3.4 ｜ 实际 待公布 ｜ 前值 3.4
- 周五 09-11 08:30　【高】Core Inflation Rate YoY　预测 2.4 ｜ 实际 待公布 ｜ 前值 2.5
- 周五 09-11 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 51 ｜ 实际 待公布 ｜ 前值 51.7

🔍 重点速览
🟡 **单日价格波动**: +3.3%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 357.27 → 收盘 368.16（+3.0%） ｜ 今日高 370.00 ｜ 低 355.80 ｜ 昨收 354.08 → 收盘 368.16（+4.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.53 | OI比 0.34 | ATM IV 46.1% | Skew -1.8pp | Term 0.90 | ExpMove ±1.9%（近端） | Rank 25%
量化视角： IV 历史低位（Rank 25%，期权偏便宜）｜期限结构倒挂（Term 0.90，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.8pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.34）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.53×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.34×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-09（1D）±1.9% ｜ 09-11（3D）±3.4% ｜ 09-14（6D）±4.1% ｜ 09-16（8D）±5.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 109,965,571 | GEX Change vs 上次快照 18,264,167 | Flip: Primary Flip: 351.11（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1059 / LOW 169 / INVALID 674
结构观察区: Primary Flip 351.11（全链重定价，覆盖 99%）
Put Wall 340（弱结构｜现价高于该位 8.3%） | Call Wall 400（现价低于该位 8.0%）
最近结构参考: Flip 351（现价高于该位 4.9%）
量化视角： 正 Gamma（1.10亿，无历史分位）｜正 Gamma 增强（+1826万）｜现价位于 Flip 上方 4.86%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 340（Put Wall，弱结构） / 358（MaxPain，仅结算参考）；上方 400（Call Wall）。
• Gamma 区域：切换参考 351（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-09  C +0 / P +0 ｜ Activity LOW ｜ 1D
09-11  C +0 / P +0 ｜ Activity LOW ｜ 3D
09-14  C +0 / P +0 ｜ Activity LOW ｜ 6D
09-16  C +0 / P +0 ｜ Activity LOW ｜ 8D

📆 09-09 Forward Structure
存量OI:      C 168.0k / P 56.8k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 3.90 / P 3.25
隐含波动率 ATM IV:  46.1%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 358（结算参考） ｜ Call Wall 400（+8.6%）（OI 19.6k）
量化解读： 存量 Call 重｜ATM IV 46.1%｜历史 Rank 25%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-11（Activity LOW）仓位参考: Max Pain 355（结算参考） ｜ Call Wall 370（+0.5%，弱）（OI 14.2k）

09-14（Activity LOW）仓位参考: Max Pain 360（结算参考） ｜ Call Wall 400（+8.6%）（OI 2.0k） ｜ Put Wall 345（-6.3%，弱）（OI 0.6k）

09-16（Activity LOW）仓位参考: Max Pain 355（结算参考） ｜ Call Wall 400（+8.6%，弱）（OI 0.8k） ｜ Put Wall 355（-3.6%）（OI 0.9k）

📅 事件差分（观察，非因果）: 09-11（3D）ATM IV 47.4% vs 09-14 39.2%（差 +8.2pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-08/TSLA_evening.json