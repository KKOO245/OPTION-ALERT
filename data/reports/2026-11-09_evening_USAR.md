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

🔍 重点速览
🔴 **事件差分**: 11-13（4D）ATM IV 148.5% vs 11-20 121.8%（差 +26.7pp），覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY 等
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 8.39 → 收盘 8.76（+4.4%） ｜ 今日高 9.14 ｜ 低 8.17 ｜ 昨收 8.23 → 收盘 8.76（+6.5%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-16，窗口结束前不做对错判定）

Options: P/C成交量 0.22 | OI比 0.22 | ATM IV 148.5% | Skew -3.6pp | Term 0.73 | ExpMove ±12.4%（近端） | Rank 81%
量化视角： IV 历史高位（Rank 81%，期权偏贵）｜期限结构倒挂（Term 0.73，近月 IV 高于远月）｜Put 保护异常便宜（Skew -3.6pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.22）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.22×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.22×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（4D）±12.4% ｜ 11-20（11D）±17.9% ｜ 11-27（18D）±20.4% ｜ 12-04（25D）±22.9%
   ⇒ IV–VIX Spread: +128.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,739,879 | GEX Change vs 上次快照 507,970 | Flip: Primary Flip: 7.91（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 216 / LOW 70 / INVALID 138
结构观察区: Primary Flip 7.91（全链重定价，覆盖 100%）
Put Wall 9（弱结构｜现价低于该位 2.7%） | Call Wall 9（现价低于该位 2.7%）
最近结构参考: Put Wall 9（现价低于该位 2.7%）
量化视角： 正 Gamma（174万，无历史分位）｜正 Gamma 增强（+51万）｜现价位于 Flip 上方 10.82%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 8（MaxPain，仅结算参考）；上方 9（Put Wall，弱结构） / 9（Call Wall）。
• Gamma 区域：切换参考 8（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +0 / P +0 ｜ Activity LOW ｜ 4D
11-20  C +0 / P +0 ｜ Activity LOW ｜ 11D
11-27  C +0 / P +0 ｜ Activity LOW ｜ 18D
12-04  C +0 / P +0 ｜ Activity LOW ｜ 25D

📆 11-13 Forward Structure
存量OI: C 19.6k / P 4.3k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $0.43 / P $0.66 ｜ ATM IV 148.5%，净 delta 敞口 0 shares
仓位参考: Max Pain 8 ｜ Call Wall 9（+2.7%，弱）（OI 3.0k） ｜ Put Wall 9.5（+8.4%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 148.5%｜历史 Rank 81%（近端代理）｜IV/RV 1.47×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-20（Activity LOW）仓位参考: Max Pain 10 ｜ Call Wall 9（+2.7%，弱）（OI 4.4k） ｜ Put Wall 8（-8.7%，弱）（OI 6.9k）

11-27（Activity LOW）仓位参考: Max Pain 10 ｜ Call Wall 8.5（-3.0%，弱）（OI 1.0k） ｜ Put Wall 9.5（+8.4%，弱）（OI 0.5k）

12-04（Activity LOW）仓位参考: Max Pain 10 ｜ Call Wall 9.5（+8.4%，弱）（OI 0.3k） ｜ Put Wall 8.5（-3.0%，弱）（OI 0.1k）

📅 事件差分（观察，非因果）: 11-13（4D）ATM IV 148.5% vs 11-20 121.8%（差 +26.7pp）——覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-09/USAR_evening.json