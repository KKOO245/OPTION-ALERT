# 期权晚报 2026-10-12（快照 21:00 ET）

📊 市场环境

SPY $778.10 ｜ QQQ $746.04
VIX 15.21 ↑2.5%（5D -2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 45.7（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-12

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-13 10:00　【高】成屋销售　预测 3.96 ｜ 实际 待公布 ｜ 前值 3.98
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.7 ｜ 实际 待公布 ｜ 前值 3.4
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 待公布 ｜ 前值 2.4
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 382.61 → 收盘 378.03（-1.2%） ｜ 今日高 382.70 ｜ 低 377.58 ｜ 昨收 382.70 → 收盘 378.03（-1.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.63 | OI比 1.03 | ATM IV 35.9% | Skew 0.3pp | Term 1.16 | ExpMove ±2.1%（近端） | Rank 7%
量化视角： IV 历史低位（Rank 7%，期权偏便宜）｜期限结构正常偏陡（Term 1.16）｜保护溢价薄（Skew 0.3pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.63×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.03×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-14（2D）±2.1% ｜ 10-16（4D）±3.6% ｜ 10-19（7D）±4.0% ｜ 10-23（11D）±7.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 55,817,769 | GEX Change vs 上次快照 -25,513,426 | Flip: Primary Flip: 367.54（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1122 / LOW 94 / INVALID 518
结构观察区: Primary Flip 367.54（全链重定价，覆盖 100%）
Call Wall 400（现价低于该位 5.5%）
最近结构参考: Flip 368（现价高于该位 2.9%）
量化视角： 正 Gamma（5582万，无历史分位）｜正 Gamma 减弱（2551万）｜现价位于 Flip 上方 2.85%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 378（MaxPain，仅结算参考）；上方 400（Call Wall）。
• Gamma 区域：切换参考 368（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-14  C +0 / P +0 ｜ Activity LOW ｜ 2D
10-16  C +0 / P +0 ｜ Activity LOW ｜ 4D
10-19  C +0 / P +0 ｜ Activity LOW ｜ 7D
10-23  C +0 / P +0 ｜ Activity LOW ｜ 11D

📆 10-14 Forward Structure
存量OI: C 19.9k / P 20.5k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $4.31 / P $3.73 ｜ ATM IV 35.9%，净 delta 敞口 0 shares
仓位参考: Max Pain 378 ｜ Call Wall 400（+5.8%，弱）（OI 3.1k） ｜ Put Wall 370（-2.1%，弱）（OI 1.4k）
量化解读： 存量两侧均衡｜ATM IV 35.9%｜历史 Rank 7%（近端代理）｜IV/RV 1.24×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

10-16（Activity LOW）仓位参考: Max Pain 370 ｜ Call Wall 400（+5.8%，弱）（OI 24.3k） ｜ Put Wall 380（+0.5%，弱）（OI 15.4k）

10-19（Activity LOW）仓位参考: Max Pain 378 ｜ Call Wall 400（+5.8%，弱）（OI 1.7k） ｜ Put Wall 360（-4.8%，弱）（OI 0.5k）

10-23（Activity LOW）仓位参考: Max Pain 370 ｜ Call Wall 400（+5.8%，弱）（OI 5.4k） ｜ Put Wall 360（-4.8%，弱）（OI 2.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-12/TSLA_evening.json