# 期权晚报 2026-10-06（快照 21:00 ET）

📊 市场环境

SPY $779.09 ｜ QQQ $759.66
VIX 15.01 ↓3.3%（5D -6.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 47.4（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-06

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 237.22 → 收盘 249.87（+5.3%） ｜ 今日高 255.08 ｜ 低 237.00 ｜ 昨收 232.57 → 收盘 249.87（+7.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.61 | OI比 0.94 | ATM IV 78.8% | Skew -3.2pp | Term 0.94 | ExpMove ±5.7%（近端） | Rank 10%
量化视角： IV 历史低位（Rank 10%，期权偏便宜）｜期限结构正常（Term 0.94）｜Put 保护异常便宜（Skew -3.2pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.61×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.94×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-09（3D）±5.7% ｜ 10-16（10D）±9.8% ｜ 10-23（17D）±12.4% ｜ 10-30（24D）±14.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 22,066,966 | GEX Change vs 上次快照 4,916,954 | Flip: Primary Flip: 230.69（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 522 / LOW 29 / INVALID 101
结构观察区: Primary Flip 230.69（全链重定价，覆盖 100%）
最近结构参考: Flip 231（现价高于该位 8.3%）
量化视角： 正 Gamma（2207万，无历史分位）｜正 Gamma 增强（+492万）｜现价位于 Flip 上方 8.31%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 232（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 231（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +0 / P +0 ｜ Activity LOW ｜ 3D
10-16  C +0 / P +0 ｜ Activity LOW ｜ 10D
10-23  C +0 / P +0 ｜ Activity LOW ｜ 17D
10-30  C +0 / P +0 ｜ Activity LOW ｜ 24D

📆 10-09 Forward Structure
存量OI: C 47.0k / P 44.0k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $7.11 / P $7.05 ｜ ATM IV 78.8%，净 delta 敞口 0 shares
仓位参考: Max Pain 232 ｜ Call Wall 242.5（-2.9%，弱）（OI 4.4k） ｜ Put Wall 225（-10.0%，弱）（OI 3.2k）
量化解读： 存量两侧均衡｜ATM IV 78.8%｜历史 Rank 10%（近端代理）｜IV/RV 1.51×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-16（Activity LOW）仓位参考: Max Pain 220 ｜ Call Wall 270（+8.1%，弱）（OI 6.2k） ｜ Put Wall 225（-10.0%，弱）（OI 2.2k）

10-23（Activity LOW）仓位参考: Max Pain 225 ｜ Call Wall 237.5（-5.0%，弱）（OI 0.9k） ｜ Put Wall 225（-10.0%，弱）（OI 0.5k）

10-30（Activity LOW）仓位参考: Max Pain 230 ｜ Put Wall 240（-4.0%，弱）（OI 0.4k）

📅 事件差分（观察，非因果）: 10-09（3D）ATM IV 78.8% vs 10-16 73.7%（差 +5.1pp）——覆盖 美联储议息会议 Minutes、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-06/NBIS_evening.json