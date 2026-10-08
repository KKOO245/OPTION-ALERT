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


## NOW

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NOW: 今开 139.50 → 收盘 137.87（-1.2%） ｜ 今日高 140.80 ｜ 低 137.49 ｜ 昨收 137.97 → 收盘 137.87（-0.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.39 | OI比 0.77 | ATM IV 54.2% | Skew -1.4pp | Term 1.09 | ExpMove ±3.1%（近端） | Rank 33%
量化视角： IV 中性（Rank 33%）｜期限结构正常（Term 1.09）｜Put 保护异常便宜（Skew -1.4pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.77）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.39×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.77×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（2D）±3.1% ｜ 10-16（9D）±6.1% ｜ 10-23（16D）±8.4% ｜ 10-30（23D）±12.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 14,453,315 | GEX Change vs 上次快照 -160,848 | Flip: Primary Flip: 134.05（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 532 / LOW 42 / INVALID 124
结构观察区: Primary Flip 134.05（全链重定价，覆盖 100%）
Call Wall 150（现价低于该位 8.1%）
最近结构参考: Flip 134（现价高于该位 2.9%）
量化视角： 正 Gamma（1445万，无历史分位）｜正 Gamma 减弱（16万）｜现价位于 Flip 上方 2.85%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 135（MaxPain，仅结算参考）；上方 150（Call Wall）。
• Gamma 区域：切换参考 134（全链重定价，覆盖 100%）。
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
存量OI: C 24.7k / P 19.0k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $2.15 / P $2.19 ｜ ATM IV 54.2%，净 delta 敞口 0 shares
仓位参考: Max Pain 135 ｜ Call Wall 150（+8.8%）（OI 5.3k） ｜ Put Wall 135（-2.1%，弱）（OI 1.2k）
量化解读： 存量 Call 重｜ATM IV 54.2%｜历史 Rank 33%（近端代理）｜IV/RV 1.88×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

10-16（Activity LOW）仓位参考: Max Pain 130 ｜ Call Wall 150（+8.8%）（OI 14.2k） ｜ Put Wall 125（-9.3%，弱）（OI 5.4k）

10-23（Activity LOW）仓位参考: Max Pain 134 ｜ Call Wall 140（+1.5%，弱）（OI 1.0k） ｜ Put Wall 125（-9.3%，弱）（OI 2.0k）

10-30（Activity LOW）仓位参考: Max Pain 135 ｜ Call Wall 150（+8.8%，弱）（OI 0.7k） ｜ Put Wall 130（-5.7%，弱）（OI 0.5k）

📅 事件差分（观察，非因果）: 10-09（2D）ATM IV 54.2% vs 10-16 48.6%（差 +5.6pp）——覆盖 美联储议息会议 Minutes、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-07/NOW_evening.json