# 期权晚报 2026-11-09（快照 21:00 ET）

📊 市场环境

SPY $752.69 ｜ QQQ $679.35
VIX 19.92 ↓22.3%（5D -5.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-09

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-10 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周二 11-10 08:30　【高】Core Inflation Rate YoY　预测 2.8 ｜ 实际 待公布 ｜ 前值 2.6
- 周二 11-10 08:30　【高】Inflation Rate MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.6
- 周二 11-10 08:30　【高】Inflation Rate YoY　预测 3.9 ｜ 实际 待公布 ｜ 前值 3.7
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 360.25 → 收盘 378.05（+4.9%） ｜ 今日高 382.20 ｜ 低 360.02 ｜ 昨收 358.22 → 收盘 378.05（+5.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.95 | OI比 0.85 | ATM IV 52.5% | Skew 6.5pp | Term 0.86 | ExpMove ±3.1%（近端） | Rank 52%
量化视角： IV 中性（Rank 52%）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜保护溢价显著（Skew 6.5pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.95×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.85×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-11（2D）±3.1% ｜ 11-13（4D）±4.3% ｜ 11-16（7D）±4.8% ｜ 11-18（9D）±5.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 59,270,513 | GEX Change vs 上次快照 -10,289,846 | Flip: Primary Flip: 356.15（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1384 / LOW 157 / INVALID 909
结构观察区: Primary Flip 356.15（全链重定价，覆盖 99%）
Call Wall 400（弱结构｜现价低于该位 5.5%）
最近结构参考: Call Wall 400（现价低于该位 5.5%）
量化视角： 正 Gamma（5927万，无历史分位）｜正 Gamma 减弱（1029万）｜现价位于 Flip 上方 6.15%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 365（MaxPain，仅结算参考）；上方 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 356（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-11  C +0 / P +0 ｜ Activity LOW ｜ 2D
11-13  C +0 / P +0 ｜ Activity LOW ｜ 4D
11-16  C +0 / P +0 ｜ Activity LOW ｜ 7D
11-18  C +0 / P +0 ｜ Activity LOW ｜ 9D

📆 11-11 Forward Structure
存量OI: C 30.3k / P 25.8k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $6.21 / P $5.50 ｜ ATM IV 52.5%，净 delta 敞口 0 shares
仓位参考: Max Pain 365 ｜ Call Wall 390（+3.2%，弱）（OI 1.9k） ｜ Put Wall 360（-4.8%，弱）（OI 0.6k）
量化解读： 存量两侧均衡｜ATM IV 52.5%｜历史 Rank 52%（近端代理）｜IV/RV 0.89×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-13（Activity LOW）仓位参考: Max Pain 360 ｜ Call Wall 362.5（-4.1%，弱）（OI 7.9k）

11-16（Activity LOW）仓位参考: Max Pain 368 ｜ Call Wall 400（+5.8%，弱）（OI 0.8k） ｜ Put Wall 380（+0.5%，弱）（OI 0.3k）

11-18（Activity LOW）仓位参考: Max Pain 355 ｜ Call Wall 380（+0.5%，弱）（OI 0.3k） ｜ Put Wall 350（-7.4%，弱）（OI 0.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-09/TSLA_evening.json