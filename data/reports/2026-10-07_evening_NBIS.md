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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 242.21 → 收盘 237.15（-2.1%） ｜ 今日高 243.62 ｜ 低 234.03 ｜ 昨收 249.87 → 收盘 237.15（-5.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.69 | OI比 1.00 | ATM IV 75.4% | Skew -1.6pp | Term 0.95 | ExpMove ±4.5%（近端） | Rank 7%
量化视角： IV 历史低位（Rank 7%，期权偏便宜）｜期限结构正常（Term 0.95）｜Put 保护异常便宜（Skew -1.6pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.69×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.00×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-09（2D）±4.5% ｜ 10-16（9D）±8.7% ｜ 10-23（16D）±11.5% ｜ 10-30（23D）±13.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 3,269,133 | GEX Change vs 上次快照 -3,987,772 | Flip: Primary Flip: 235.63（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 513 / LOW 34 / INVALID 137
结构观察区: Primary Flip 235.63（全链重定价，覆盖 100%）
Put Wall 220（弱结构｜现价高于该位 7.8%）
最近结构参考: Flip 236（现价高于该位 0.6%）
量化视角： 正 Gamma（327万，无历史分位）｜正 Gamma 减弱（399万）｜现价位于 Flip 上方 0.64%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 220（Put Wall，弱结构）；上方 240（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 236（全链重定价，覆盖 100%）。
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
存量OI: C 53.9k / P 53.8k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $5.20 / P $5.45 ｜ ATM IV 75.4%，净 delta 敞口 0 shares
仓位参考: Max Pain 240 ｜ Call Wall 260（+9.6%，弱）（OI 4.1k） ｜ Put Wall 225（-5.1%）（OI 9.1k）
量化解读： 存量两侧均衡｜ATM IV 75.4%｜历史 Rank 7%（近端代理）｜IV/RV 1.42×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-16（Activity LOW）仓位参考: Max Pain 225 ｜ Call Wall 250（+5.4%，弱）（OI 7.1k） ｜ Put Wall 220（-7.2%，弱）（OI 5.9k）

10-23（Activity LOW）仓位参考: Max Pain 225 ｜ Call Wall 220（-7.2%，弱）（OI 0.9k） ｜ Put Wall 225（-5.1%，弱）（OI 0.5k）

10-30（Activity LOW）仓位参考: Max Pain 235 ｜ Put Wall 220（-7.2%，弱）（OI 0.9k）

📅 事件差分（观察，非因果）: 10-09（2D）ATM IV 75.4% vs 10-16 69.6%（差 +5.8pp）——覆盖 美联储议息会议 Minutes、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-07/NBIS_evening.json