# 期权晚报 2026-10-08（快照 16:40 ET）

📊 市场环境

SPY $773.93 ｜ QQQ $747.58
VIX 15.41 ↑2.2%（5D -6.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-08

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **事件差分**: 10-09 ATM IV 79.2% vs 10-16 67.5%（差 +11.7pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 15.78 → 收盘 15.26（-3.3%） ｜ 今日高 15.93 ｜ 低 14.82 ｜ 昨收 16.01 → 收盘 15.26（-4.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 7.15 | OI比 0.36 | ATM IV 79.2% | Skew -24.7pp | Term 0.89 | ExpMove ±3.9%（近端） | Rank 9%
量化视角： IV 历史低位（Rank 9%，期权偏便宜）｜期限结构倒挂（Term 0.89，近月 IV 高于远月）｜Put 保护异常便宜（Skew -24.7pp，Put IV < Call IV）｜⚠️ 重点观察：存量 Call 重（OI比 0.36）+ 当日成交偏 Put（P/C量 7.15）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 7.15×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.36×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（1D）±3.9% ｜ 10-16（8D）±8.2% ｜ 10-23（15D）±11.1% ｜ 10-30（22D）±13.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 544,169 | GEX Change vs 上次快照 -777,836 | Flip: Primary Flip: 14.69（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 88%（带内） ｜ IV 有效性: VALID 180 / LOW 99 / INVALID 149
结构观察区: Primary Flip 14.69（全链重定价，覆盖 88%）
Put Wall 15（弱结构｜现价高于该位 1.7%）
最近结构参考: Put Wall 15（现价高于该位 1.7%）
量化视角： 正 Gamma（54万，无历史分位）｜正 Gamma 减弱（78万）｜现价位于 Flip 上方 3.85%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall，弱结构）；上方 16（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 15（全链重定价，覆盖 88%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C -4 / P +0.2k ｜ Activity MEDIUM △ ｜ 1D
10-16  C +0.1k / P +17 ｜ Activity LOW ｜ 8D
10-23  C +37 / P +40 ｜ Activity LOW ｜ 15D
10-30  C +19 / P +29 ｜ Activity LOW ｜ 22D

📆 10-09 Forward Structure
存量OI: C 7.8k / P 2.8k，今日变化ΔOI: C -4 / P +0.2k，平值价格ATM: C $0.45 / P $0.15 ｜ ATM IV 79.2%，净 delta 敞口 -1k shares
Top ΔOI: P 15 +197 ｜ C 16 +48
仓位参考: Max Pain 16 ｜ Put Wall 15.5（+1.6%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 79.2%｜历史 Rank 9%（近端代理）｜IV/RV 1.30×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,332 股

10-16（Activity LOW）仓位参考: Max Pain 18 ｜ Put Wall 15（-1.7%，弱）（OI 0.9k）

10-23（Activity LOW）仓位参考: Max Pain 17 ｜ Put Wall 14（-8.3%）（OI 0.3k）

10-30（Activity LOW）仓位参考: Max Pain 16 ｜ Put Wall 14（-8.3%）（OI 0.3k）

📅 事件差分（观察，非因果）: 10-09（1D）ATM IV 79.2% vs 10-16 67.5%（差 +11.7pp）——覆盖 密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-08/NNE_evening.json