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


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 237.68 → 收盘 237.47（-0.1%） ｜ 今日高 239.08 ｜ 低 236.38 ｜ 昨收 239.24 → 收盘 237.47（-0.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.86 | OI比 1.11 | ATM IV 29.8% | Skew 2.4pp | Term 1.01 | ExpMove ±1.8%（近端） | Rank 8%
量化视角： IV 历史低位（Rank 8%，期权偏便宜）｜期限结构正常（Term 1.01）｜保护溢价中性（Skew 2.4pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.86×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.11×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-09（2D）±1.8% ｜ 10-12（5D）±2.3% ｜ 10-14（7D）±3.0% ｜ 10-16（9D）±3.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 488,847,778 | GEX Change vs 上次快照 -69,616,887 | Flip: Primary Flip: 225.60（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 699 / LOW 161 / INVALID 548
结构观察区: Primary Flip 225.60（全链重定价，覆盖 99%）
Put Wall 220（弱结构｜现价高于该位 7.9%） | Call Wall 240（弱结构｜现价低于该位 1.1%）
最近结构参考: Call Wall 240（现价低于该位 1.1%）
量化视角： 正 Gamma（4.89亿，无历史分位）｜正 Gamma 减弱（6962万）｜现价位于 Flip 上方 5.26%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 220（Put Wall，弱结构） / 232（MaxPain，仅结算参考）；上方 240（Call Wall，弱结构）。
• Gamma 区域：切换参考 226（全链重定价，覆盖 99%）。
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
存量OI: C 398.6k / P 442.3k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $2.14 / P $2.10 ｜ ATM IV 29.8%，净 delta 敞口 0 shares
仓位参考: Max Pain 232 ｜ Call Wall 240（+1.1%，弱）（OI 75.1k） ｜ Put Wall 230（-3.1%，弱）（OI 35.2k）
量化解读： 存量两侧均衡｜ATM IV 29.8%｜历史 Rank 8%（近端代理）｜IV/RV 1.83×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-12（Activity LOW）仓位参考: Max Pain 238 ｜ Call Wall 240（+1.1%）（OI 7.1k） ｜ Put Wall 237.5（+0.0%，弱）（OI 3.8k）

10-14（Activity LOW）仓位参考: Max Pain 235 ｜ Call Wall 260（+9.5%，弱）（OI 2.1k） ｜ Put Wall 237.5（+0.0%，弱）（OI 1.2k）

10-16（Activity LOW）仓位参考: Max Pain 210 ｜ Call Wall 220（-7.4%，弱）（OI 99.8k） ｜ Put Wall 220（-7.4%，弱）（OI 51.7k）

📅 事件差分（观察，非因果）: 10-09（2D）ATM IV 29.8% vs 10-12 24.3%（差 +5.6pp）——覆盖 美联储议息会议 Minutes、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-07/NVDA_evening.json