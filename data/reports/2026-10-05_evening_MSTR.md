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


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 164.68 → 收盘 164.43（-0.2%） ｜ 今日高 166.20 ｜ 低 160.12 ｜ 昨收 160.01 → 收盘 164.43（+2.8%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.47 | OI比 0.75 | ATM IV 66.6% | Skew -7.6pp | Term 0.96 | ExpMove ±5.6%（近端） | Rank 22%
量化视角： IV 历史低位（Rank 22%，期权偏便宜）｜期限结构正常（Term 0.96）｜Put 保护异常便宜（Skew -7.6pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.75）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.47×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.75×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（4D）±5.6% ｜ 10-16（11D）±8.6% ｜ 10-23（18D）±11.1% ｜ 10-30（25D）±13.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 81,911,006 | GEX Change vs 上次快照 10,723,531 | Flip: Primary Flip: 147.87（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 661 / LOW 86 / INVALID 185
结构观察区: Primary Flip 147.87（全链重定价，覆盖 100%）
最近结构参考: Flip 148（现价高于该位 11.2%）
量化视角： 正 Gamma（8191万，无历史分位）｜正 Gamma 增强（+1072万）｜现价位于 Flip 上方 11.20%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 152（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 148（全链重定价，覆盖 100%）。
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
存量OI: C 202.0k / P 150.6k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $4.29 / P $4.90 ｜ ATM IV 66.6%，净 delta 敞口 0 shares
仓位参考: Max Pain 152 ｜ Call Wall 165（+0.3%，弱）（OI 24.6k）
量化解读： 存量 Call 重｜ATM IV 66.6%｜历史 Rank 22%（近端代理）｜IV/RV 0.90×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-16（Activity LOW）仓位参考: Max Pain 130 ｜ Call Wall 155（-5.7%，弱）（OI 10.4k） ｜ Put Wall 150（-8.8%，弱）（OI 5.3k）

10-23（Activity LOW）仓位参考: Max Pain 160 ｜ Call Wall 172.5（+4.9%，弱）（OI 2.5k） ｜ Put Wall 155（-5.7%，弱）（OI 3.0k）

10-30（Activity LOW）仓位参考: Max Pain 160 ｜ Call Wall 162.5（-1.2%，弱）（OI 2.5k） ｜ Put Wall 160（-2.7%，弱）（OI 2.7k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-05/MSTR_evening.json