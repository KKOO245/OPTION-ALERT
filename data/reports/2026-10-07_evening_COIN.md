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


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 180.23 → 收盘 178.45（-1.0%） ｜ 今日高 181.20 ｜ 低 177.00 ｜ 昨收 185.74 → 收盘 178.45（-3.9%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.36 | OI比 0.54 | ATM IV 60.7% | Skew -4.0pp | Term 1.07 | ExpMove ±3.7%（近端） | Rank 12%
量化视角： IV 历史低位（Rank 12%，期权偏便宜）｜期限结构正常（Term 1.07）｜Put 保护异常便宜（Skew -4.0pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.54）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.36×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.54×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（2D）±3.7% ｜ 10-16（9D）±6.9% ｜ 10-23（16D）±9.0% ｜ 10-30（23D）±12.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) -2,417,064 | GEX Change vs 上次快照 -8,050,442 | Flip: Primary Flip: 179.35（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 454 / LOW 120 / INVALID 270
结构观察区: Primary Flip 179.35（全链重定价，覆盖 100%）
最近结构参考: Flip 179（现价低于该位 0.5%）
量化视角： 负 Gamma（242万，无历史分位）｜由正转负（805万）｜现价位于 Flip 下方 0.50%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 188（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 179（全链重定价，覆盖 100%）。
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
存量OI: C 68.5k / P 37.2k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $3.80 / P $2.83 ｜ ATM IV 60.7%，净 delta 敞口 0 shares
仓位参考: Max Pain 188 ｜ Call Wall 195（+9.3%）（OI 13.7k） ｜ Put Wall 170（-4.7%，弱）（OI 2.1k）
量化解读： 存量 Call 重｜ATM IV 60.7%｜历史 Rank 12%（近端代理）｜IV/RV 0.91×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-16（Activity LOW）仓位参考: Max Pain 180 ｜ Call Wall 190（+6.5%，弱）（OI 2.6k） ｜ Put Wall 165（-7.5%，弱）（OI 3.1k）

10-23（Activity LOW）仓位参考: Max Pain 190 ｜ Call Wall 190（+6.5%）（OI 0.9k） ｜ Put Wall 170（-4.7%，弱）（OI 0.5k）

10-30（Activity LOW）仓位参考: Max Pain 185 ｜ Call Wall 185（+3.7%，弱）（OI 1.2k） ｜ Put Wall 170（-4.7%，弱）（OI 0.7k）

📅 事件差分（观察，非因果）: 10-09（2D）ATM IV 60.7% vs 10-16 55.5%（差 +5.2pp）——覆盖 美联储议息会议 Minutes、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-07/COIN_evening.json