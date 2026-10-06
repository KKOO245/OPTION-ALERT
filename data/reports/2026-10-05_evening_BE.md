# 期权晚报 2026-10-05（快照 21:00 ET）

📊 市场环境

SPY $774.83 ｜ QQQ $nan
VIX 15.52 ↑1.4%（5D -3.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 43.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-05

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周一 10-05 10:00　【高】ISM 非制造业 PMI　预测 55 ｜ 实际 54.9 ｜ 前值 55.4　✅ 今日已公布
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 289.99 → 收盘 286.65（-1.2%） ｜ 今日高 291.96 ｜ 低 282.34 ｜ 昨收 289.15 → 收盘 286.65（-0.9%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.14 | OI比 1.13 | ATM IV 71.3% | Skew -0.3pp | Term 1.13 | ExpMove ±5.8%（近端） | Rank 28%
量化视角： IV 中性（Rank 28%）｜期限结构正常（Term 1.13）｜Put 保护异常便宜（Skew -0.3pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.14×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.13×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-09（4D）±5.8% ｜ 10-16（11D）±9.1% ｜ 10-23（18D）±11.8% ｜ 10-30（25D）±16.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 8,321,992 | GEX Change vs 上次快照 1,243,945 | Flip: Primary Flip: 269.90（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 567 / LOW 79 / INVALID 182
结构观察区: Primary Flip 269.90（全链重定价，覆盖 100%）
Call Wall 280（弱结构｜现价高于该位 2.4%）
最近结构参考: Call Wall 280（现价高于该位 2.4%）
量化视角： 正 Gamma（832万，无历史分位）｜正 Gamma 增强（+124万）｜现价位于 Flip 上方 6.20%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 280（MaxPain，仅结算参考） / 280（Call Wall，弱结构）。
• Gamma 区域：切换参考 270（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +0 / P +0 ｜ Activity LOW ｜ 4D
10-16  C +0 / P +0 ｜ Activity LOW ｜ 11D
10-23  C +0 / P +0 ｜ Activity LOW ｜ 18D
10-30  C +0 / P +0 ｜ Activity LOW ｜ 25D

📆 10-09 Forward Structure
存量OI: C 24.0k / P 27.1k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $8.30 / P $8.30 ｜ ATM IV 71.3%，净 delta 敞口 0 shares
仓位参考: Max Pain 280 ｜ Call Wall 300（+4.7%）（OI 2.4k） ｜ Put Wall 280（-2.3%，弱）（OI 1.4k）
量化解读： 存量两侧均衡｜ATM IV 71.3%｜历史 Rank 28%（近端代理）｜IV/RV 0.91×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

10-16（Activity LOW）仓位参考: Max Pain 265 ｜ Call Wall 270（-5.8%，弱）（OI 7.6k） ｜ Put Wall 260（-9.3%，弱）（OI 3.9k）

10-23（Activity LOW）仓位参考: Max Pain 270 ｜ Call Wall 300（+4.7%，弱）（OI 1.1k） ｜ Put Wall 280（-2.3%，弱）（OI 0.7k）

10-30（Activity LOW）仓位参考: Max Pain 285 ｜ Call Wall 300（+4.7%，弱）（OI 1.2k） ｜ Put Wall 285（-0.6%，弱）（OI 1.7k）

📅 事件差分（观察，非因果）: 10-09（4D）ATM IV 71.3% vs 10-16 65.9%（差 +5.4pp）——覆盖 ISM 非制造业 PMI、美联储议息会议 Minutes 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-05/BE_evening.json