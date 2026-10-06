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


## NOW

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NOW: 今开 135.22 → 收盘 136.08（+0.6%） ｜ 今日高 137.90 ｜ 低 134.15 ｜ 昨收 134.38 → 收盘 136.08（+1.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.48 | OI比 0.79 | ATM IV 52.8% | Skew -0.6pp | Term 1.11 | ExpMove ±4.6%（近端） | Rank 24%
量化视角： IV 历史低位（Rank 24%，期权偏便宜）｜期限结构正常（Term 1.11）｜Put 保护异常便宜（Skew -0.6pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.79）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.48×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.79×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（4D）±4.6% ｜ 10-16（11D）±6.8% ｜ 10-23（18D）±8.9% ｜ 10-30（25D）±12.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 7,014,786 | GEX Change vs 上次快照 53,780 | Flip: Primary Flip: 132.97（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 512 / LOW 33 / INVALID 145
结构观察区: Primary Flip 132.97（全链重定价，覆盖 100%）
最近结构参考: Flip 133（现价高于该位 2.3%）
量化视角： 正 Gamma（701万，无历史分位）｜正 Gamma 增强（+5万）｜现价位于 Flip 上方 2.34%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 135（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 133（全链重定价，覆盖 100%）。
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
存量OI: C 19.9k / P 15.7k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $3.15 / P $3.15 ｜ ATM IV 52.8%，净 delta 敞口 0 shares
仓位参考: Max Pain 135 ｜ Call Wall 140（+2.9%，弱）（OI 2.7k） ｜ Put Wall 130（-4.5%，弱）（OI 1.0k）
量化解读： 存量 Call 重｜ATM IV 52.8%｜历史 Rank 24%（近端代理）｜IV/RV 1.36×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

10-16（Activity LOW）仓位参考: Max Pain 130 ｜ Call Wall 140（+2.9%，弱）（OI 5.9k） ｜ Put Wall 125（-8.1%，弱）（OI 5.6k）

10-23（Activity LOW）仓位参考: Max Pain 134 ｜ Call Wall 140（+2.9%，弱）（OI 0.9k） ｜ Put Wall 125（-8.1%，弱）（OI 2.0k）

10-30（Activity LOW）仓位参考: Max Pain 134 ｜ Call Wall 140（+2.9%，弱）（OI 0.6k） ｜ Put Wall 123（-9.6%，弱）（OI 0.7k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-05/NOW_evening.json