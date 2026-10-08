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


## SPCX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPCX: 今开 168.12 → 收盘 167.60（-0.3%） ｜ 今日高 171.31 ｜ 低 165.65 ｜ 昨收 171.92 → 收盘 167.60（-2.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.06 | OI比 1.16 | ATM IV 48.1% | Skew -1.1pp | Term 1.01 | ExpMove ±2.9%（近端） | Rank 20%
量化视角： IV 历史低位（Rank 20%，期权偏便宜）｜期限结构正常（Term 1.01）｜Put 保护异常便宜（Skew -1.1pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.06×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.16×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-09（2D）±2.9% ｜ 10-12（5D）±3.6% ｜ 10-14（7D）±4.9% ｜ 10-16（9D）±5.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 78,362,045 | GEX Change vs 上次快照 -10,752,327 | Flip: Primary Flip: 161.03（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 726 / LOW 112 / INVALID 440
结构观察区: Primary Flip 161.03（全链重定价，覆盖 99%）
Call Wall 180（弱结构｜现价低于该位 6.9%）
最近结构参考: Flip 161（现价高于该位 4.1%）
量化视角： 正 Gamma（7836万，无历史分位）｜正 Gamma 减弱（1075万）｜现价位于 Flip 上方 4.08%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 162（MaxPain，仅结算参考）；上方 180（Call Wall，弱结构）。
• Gamma 区域：切换参考 161（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +0 / P +0 ｜ Activity LOW ｜ 2D
10-12  C +0 / P +0 ｜ Activity LOW ｜ 5D
10-14  C +0 / P +0 ｜ Activity LOW ｜ 7D
10-16  C +0 / P +0 ｜ Activity LOW ｜ 9D

📆 10-09 Forward Structure
存量OI: C 191.3k / P 221.9k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $2.52 / P $2.32 ｜ ATM IV 48.1%，净 delta 敞口 0 shares
仓位参考: Max Pain 162 ｜ Call Wall 180（+7.4%，弱）（OI 26.3k） ｜ Put Wall 160（-4.5%，弱）（OI 19.3k）
量化解读： 存量两侧均衡｜ATM IV 48.1%｜历史 Rank 20%（近端代理）｜IV/RV 1.00×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-12（Activity LOW）仓位参考: Max Pain 170 ｜ Call Wall 180（+7.4%，弱）（OI 4.2k） ｜ Put Wall 165（-1.6%，弱）（OI 1.7k）

10-14（Activity LOW）仓位参考: Max Pain 172 ｜ Call Wall 180（+7.4%，弱）（OI 1.0k） ｜ Put Wall 170（+1.4%，弱）（OI 0.7k）

10-16（Activity LOW）仓位参考: Max Pain 150 ｜ Call Wall 160（-4.5%，弱）（OI 33.0k） ｜ Put Wall 155（-7.5%，弱）（OI 14.6k）

📅 事件差分（观察，非因果）: 10-09（2D）ATM IV 48.1% vs 10-12 38.8%（差 +9.3pp）——覆盖 美联储议息会议 Minutes、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-07/SPCX_evening.json