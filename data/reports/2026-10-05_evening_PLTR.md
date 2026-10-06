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


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 189.15 → 收盘 189.40（+0.1%） ｜ 今日高 192.69 ｜ 低 187.63 ｜ 昨收 188.75 → 收盘 189.40（+0.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.39 | OI比 0.72 | ATM IV 43.9% | Skew 2.2pp | Term 1.30 | ExpMove ±3.7%（近端） | Rank 15%
量化视角： IV 历史低位（Rank 15%，期权偏便宜）｜期限结构正常偏陡（Term 1.30）｜保护溢价中性（Skew 2.2pp）｜存量 Call 偏重（OI比 0.72）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.39×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.72×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（4D）±3.7% ｜ 10-16（11D）±5.8% ｜ 10-23（18D）±7.4% ｜ 10-30（25D）±8.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 43,679,699 | GEX Change vs 上次快照 2,192,373 | Flip: Primary Flip: 179.67（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 522 / LOW 83 / INVALID 207
结构观察区: Primary Flip 179.67（全链重定价，覆盖 100%）
Call Wall 200（现价低于该位 5.3%）
最近结构参考: Call Wall 200（现价低于该位 5.3%）
量化视角： 正 Gamma（4368万，无历史分位）｜正 Gamma 增强（+219万）｜现价位于 Flip 上方 5.42%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 188（MaxPain，仅结算参考）；上方 200（Call Wall）。
• Gamma 区域：切换参考 180（全链重定价，覆盖 100%）。
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
存量OI: C 90.8k / P 65.2k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $3.25 / P $3.79 ｜ ATM IV 43.9%，净 delta 敞口 0 shares
仓位参考: Max Pain 188 ｜ Call Wall 197.5（+4.3%，弱）（OI 12.7k） ｜ Put Wall 190（+0.3%，弱）（OI 6.8k）
量化解读： 存量 Call 重｜ATM IV 43.9%｜历史 Rank 15%（近端代理）｜IV/RV 1.96×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-16（Activity LOW）仓位参考: Max Pain 170 ｜ Call Wall 200（+5.6%，弱）（OI 16.2k） ｜ Put Wall 175（-7.6%，弱）（OI 9.0k）

10-23（Activity LOW）仓位参考: Max Pain 180 ｜ Call Wall 180（-5.0%）（OI 4.6k） ｜ Put Wall 175（-7.6%，弱）（OI 1.9k）

10-30（Activity LOW）仓位参考: Max Pain 180 ｜ Call Wall 192.5（+1.6%，弱）（OI 2.7k） ｜ Put Wall 180（-5.0%，弱）（OI 1.5k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-05/PLTR_evening.json