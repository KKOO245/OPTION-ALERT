# 期权晚报 2026-10-07（快照 21:00 ET）

📊 市场环境

SPY $777.22 ｜ QQQ $757.73
VIX 15.08 ↑0.5%（5D -7.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 44.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-07

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布　✅ 今日已公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 1,619.50 → 收盘 1,692.42（+4.5%） ｜ 今日高 1733.28 ｜ 低 1617.95 ｜ 昨收 1,660.46 → 收盘 1,692.42（+1.9%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.43 | OI比 1.04 | ATM IV 60.2% | Skew -2.9pp | Term 1.08 | ExpMove ±3.6%（近端） | Rank 17%
量化视角： IV 历史低位（Rank 17%，期权偏便宜）｜期限结构正常（Term 1.08）｜Put 保护异常便宜（Skew -2.9pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.43×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.04×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-09（2D）±3.6% ｜ 10-16（9D）±7.1% ｜ 10-23（16D）±9.5% ｜ 10-30（23D）±13.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 505,048 | GEX Change vs 上次快照 4,480,467 | Flip: Primary Flip: 1689.95（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1581 / LOW 441 / INVALID 1144
结构观察区: Primary Flip 1689.95（全链重定价，覆盖 100%）
最近结构参考: Flip 1690（现价高于该位 0.1%）
量化视角： 正 Gamma（51万，无历史分位）｜由负转正（+448万）｜现价位于 Flip 上方 0.15%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 1,695（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1690（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +0 / P +0 ｜ Activity LOW ｜ 2D
10-16  C +0 / P +0 ｜ Activity LOW ｜ 9D
10-23  C +0 / P +0 ｜ Activity LOW ｜ 16D
10-30  C +0 / P +0 ｜ Activity LOW ｜ 23D

📆 10-09 Forward Structure
存量OI: C 38.6k / P 40.0k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $31.85 / P $28.40 ｜ ATM IV 60.2%，净 delta 敞口 0 shares
仓位参考: Max Pain 1,695 ｜ Call Wall 1800（+6.4%，弱）（OI 2.5k） ｜ Put Wall 1600（-5.5%，弱）（OI 2.1k）
量化解读： 存量两侧均衡｜ATM IV 60.2%｜历史 Rank 17%（近端代理）｜IV/RV 1.02×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

10-16（Activity LOW）仓位参考: Max Pain 1,675 ｜ Call Wall 1800（+6.4%，弱）（OI 1.5k） ｜ Put Wall 1600（-5.5%，弱）（OI 1.5k）

10-23（Activity LOW）仓位参考: Max Pain 1,700 ｜ Call Wall 1800（+6.4%）（OI 0.5k） ｜ Put Wall 1650（-2.5%，弱）（OI 0.4k）

10-30（Activity LOW）仓位参考: Max Pain 1,700 ｜ Call Wall 1700（+0.4%，弱）（OI 0.4k） ｜ Put Wall 1600（-5.5%，弱）（OI 0.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-07/SNDK_evening.json