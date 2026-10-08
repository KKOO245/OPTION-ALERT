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


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 157.82 → 收盘 153.37（-2.8%） ｜ 今日高 158.66 ｜ 低 152.53 ｜ 昨收 164.55 → 收盘 153.37（-6.8%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.48 | OI比 0.73 | ATM IV 66.1% | Skew -3.6pp | Term 0.89 | ExpMove ±3.9%（近端） | Rank 22%
量化视角： IV 历史低位（Rank 22%，期权偏便宜）｜期限结构倒挂（Term 0.89，近月 IV 高于远月）｜Put 保护异常便宜（Skew -3.6pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.73）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.48×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.73×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（2D）±3.9% ｜ 10-16（9D）±7.6% ｜ 10-23（16D）±10.0% ｜ 10-30（23D）±12.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) -311,653 | GEX Change vs 上次快照 -31,697,850 | Flip: Primary Flip: 153.42（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 628 / LOW 105 / INVALID 209
结构观察区: Primary Flip 153.42（全链重定价，覆盖 100%）
最近结构参考: Flip 153（现价低于该位 0.0%）
量化视角： 负 Gamma（31万，无历史分位）｜由正转负（3170万）｜现价位于 Flip 下方 0.03%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 155（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 153（全链重定价，覆盖 100%）。
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
存量OI: C 214.8k / P 156.8k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $3.50 / P $2.54 ｜ ATM IV 66.1%，净 delta 敞口 0 shares
仓位参考: Max Pain 155 ｜ Call Wall 165（+7.6%，弱）（OI 24.7k）
量化解读： 存量 Call 重｜ATM IV 66.1%｜历史 Rank 22%（近端代理）｜IV/RV 0.90×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-16（Activity LOW）仓位参考: Max Pain 130 ｜ Call Wall 155（+1.1%，弱）（OI 10.5k） ｜ Put Wall 150（-2.2%，弱）（OI 9.8k）

10-23（Activity LOW）仓位参考: Max Pain 160 ｜ Call Wall 165（+7.6%，弱）（OI 1.9k） ｜ Put Wall 160（+4.3%，弱）（OI 3.8k）

10-30（Activity LOW）仓位参考: Max Pain 160 ｜ Call Wall 162.5（+6.0%，弱）（OI 2.6k） ｜ Put Wall 160（+4.3%，弱）（OI 3.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-07/MSTR_evening.json