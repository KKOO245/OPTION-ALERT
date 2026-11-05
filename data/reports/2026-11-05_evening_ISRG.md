# 期权晚报 2026-11-05（快照 16:40 ET）

📊 市场环境

SPY $733.00 ｜ QQQ $647.05
VIX 28.18 ↑69.7%（5D +63.8%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 19.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-05

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🔴 **事件差分**: 11-06（1D）ATM IV 59.5% vs 11-13 43.7%（差 +15.9pp），覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Vol Regime 升档**: ELEVATED → STRESS（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 482.90 → 收盘 468.52（-3.0%） ｜ 今日高 485.17 ｜ 低 461.19 ｜ 昨收 482.10 → 收盘 468.52（-2.8%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-12，窗口结束前不做对错判定）

Options: P/C成交量 0.56 | OI比 0.65 | ATM IV 59.5% | Skew 15.3pp | Term 0.60 | ExpMove ±1.2%（近端） | Rank 91%
量化视角： IV 历史高位（Rank 91%，期权偏贵）｜期限结构倒挂（Term 0.60，近月 IV 高于远月）｜保护溢价显著（Skew 15.3pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.65）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.56×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.65×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（1D）±1.2% ｜ 11-13（8D）±5.3% ｜ 11-20（15D）±5.8% ｜ 11-27（22D）±6.3%
   ⇒ IV–VIX Spread: +31.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,918,331 | GEX Change vs 上次快照 56,104 | Flip: Primary Flip: 423.50（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 83%（带内） ｜ IV 有效性: VALID 279 / LOW 169 / INVALID 514
结构观察区: Primary Flip 423.50（全链重定价，覆盖 83%）
Call Wall 450（弱结构｜现价高于该位 4.1%）
最近结构参考: Call Wall 450（现价高于该位 4.1%）
量化视角： 正 Gamma（292万，无历史分位）｜正 Gamma 增强（+6万）｜现价位于 Flip 上方 10.63%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 438（MaxPain，仅结算参考） / 450（Call Wall，弱结构）。
• Gamma 区域：切换参考 423（全链重定价，覆盖 83%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-06  C +0.4k / P +0.3k ｜ Activity HIGH ｜ 1D
11-13  C +94 / P +90 ｜ Activity HIGH ｜ 8D
11-20  C -59 / P -17 ｜ Activity MEDIUM △ ｜ 15D
11-27  C +20 / P +12 ｜ Activity MEDIUM △ ｜ 22D

📆 11-06 Forward Structure
存量OI: C 3.0k / P 1.9k，今日变化ΔOI: C +0.4k / P +0.3k，平值价格ATM: C $4.70 / P $1.05 ｜ ATM IV 59.5%，净 delta 敞口 -24k shares
Top ΔOI: C 495 +125 ｜ C 492 +112 ｜ P 485 +101
仓位参考: Max Pain 438 ｜ Call Wall 445（-5.0%）（OI 0.5k） ｜ Put Wall 422.5（-9.8%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 59.5%｜历史 Rank 91%（近端代理）｜IV/RV 1.47×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 23,752 股

📆 11-13 Forward Structure
存量OI: C 1.1k / P 1.1k，今日变化ΔOI: C +94 / P +90，平值价格ATM: C $19.70 / P $5.15 ｜ ATM IV 43.7%，净 delta 敞口 -2k shares
Top ΔOI: C 500 +24 ｜ C 485 +22 ｜ P 447 +20
仓位参考: Max Pain 435 ｜ Call Wall 440（-6.1%，弱）（OI 0.1k） ｜ Put Wall 435（-7.2%，弱）（OI 55）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 43.7%｜历史 Rank 91%（近端代理）｜IV/RV 1.08×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 2,408 股

11-20（MEDIUM △）Top ΔOI: 475C +59 ｜ 480P +59
11-20（MEDIUM △）仓位参考: Max Pain 405 ｜ Call Wall 435（-7.2%，弱）（OI 0.6k） ｜ Put Wall 427.5（-8.8%，弱）（OI 0.4k）

11-27（MEDIUM △）Top ΔOI: 490C +11 ｜ 455P +6
11-27（MEDIUM △）仓位参考: Max Pain 430 ｜ Call Wall 430（-8.2%，弱）（OI 64）

📅 事件差分（观察，非因果）: 11-06（1D）ATM IV 59.5% vs 11-13 43.7%（差 +15.9pp）——覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-05/ISRG_evening.json