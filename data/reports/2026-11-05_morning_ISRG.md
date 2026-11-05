# 期权晨报 2026-11-05（快照 10:20 ET）

📊 市场环境

SPY $732.06 ｜ QQQ $647.05
VIX 21.04 ↑26.7%（5D +22.3%） ｜ Vol Regime: ELEVATED
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
🔴 **事件差分**: 11-06（1D）ATM IV 53.8% vs 11-13 35.8%（差 +17.9pp），覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Vol Regime 升档**: NORMAL → ELEVATED（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 482.10 → 今开 482.90（+0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 485.17 ｜ 低 478.80

Options: P/C成交量 0.11 | OI比 0.65 | ATM IV 53.8% | Skew 8.1pp | Term 0.63 | ExpMove ±2.5%（近端） | Rank 86%
量化视角： IV 历史高位（Rank 86%，期权偏贵）｜期限结构倒挂（Term 0.63，近月 IV 高于远月）｜保护溢价显著（Skew 8.1pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.65）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.11×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.65×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（1D）±2.5% ｜ 11-13（8D）±4.5% ｜ 11-20（15D）±5.9% ｜ 11-27（22D）±6.9%
   ⇒ IV–VIX Spread: +32.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,862,226 | GEX Change vs 上次快照 34,531 | Flip: Primary Flip: 423.17（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 85%（带内） ｜ IV 有效性: VALID 297 / LOW 168 / INVALID 497
结构观察区: Primary Flip 423.17（全链重定价，覆盖 85%）
Call Wall 450（弱结构｜现价高于该位 7.0%）
最近结构参考: Call Wall 450（现价高于该位 7.0%）
量化视角： 正 Gamma（286万，无历史分位）｜正 Gamma 增强（+3万）｜现价位于 Flip 上方 13.75%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 438（MaxPain，仅结算参考） / 450（Call Wall，弱结构）。
• Gamma 区域：切换参考 423（全链重定价，覆盖 85%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 495.0C — Vol 166 | 最新价 $1.85 | OI 0→125 (ΔOI +125张) | ΔOI/Volume 75.3% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增125张（前日OI缺失），值得跟踪（方向未知）
11-06 492.5C — Vol 112 | 最新价 $2.64 | OI 0→112 (ΔOI +112张) | ΔOI/Volume 100.0% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增112张（前日OI缺失），值得跟踪（方向未知）
11-06 485.0P — Vol 119 | 最新价 $6.82 | OI 0→101 (ΔOI +101张) | ΔOI/Volume 84.9% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增101张（前日OI缺失），值得跟踪（方向未知）
11-06 487.5C — Vol 96 | 最新价 $5.00 | OI 15→91 (ΔOI +76张) | ΔOI/Volume 79.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增76张（+506.7% vs前日OI），连续性待观察（方向未知）
11-20 480.0P — Vol 70 | 最新价 $11.20 | OI 1→60 (ΔOI +59张) | ΔOI/Volume 84.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增59张（+5900.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 473 张（Put 160 / Call 313），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +0.4k / P +0.3k ｜ Activity MEDIUM △ ｜ 1D
11-13  C +94 / P +90 ｜ Activity MEDIUM △ ｜ 8D
11-20  C -59 / P -17 ｜ Activity LOW ｜ 15D
11-27  C +20 / P +12 ｜ Activity LOW ｜ 22D

📆 11-06 Forward Structure
存量OI: C 3.0k / P 1.9k，今日变化ΔOI: C +0.4k / P +0.3k，平值价格ATM: C $6.00 / P $6.00 ｜ ATM IV 53.8%，净 delta 敞口 -9k shares
Top ΔOI: C 495 +125 ｜ C 492 +112 ｜ P 485 +101
仓位参考: Max Pain 438 ｜ Call Wall 445（-7.6%）（OI 0.5k） ｜ Put Wall 485（+0.8%，弱）（OI 0.1k）
量化解读： 存量 Call 重｜ATM IV 53.8%｜历史 Rank 86%（近端代理）｜IV/RV 1.33×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 8,775 股

11-13（MEDIUM △）Top ΔOI: 500C +24 ｜ 485C +22
11-13（MEDIUM △）仓位参考: Max Pain 435 ｜ Call Wall 440（-8.6%，弱）（OI 0.1k） ｜ Put Wall 435（-9.6%，弱）（OI 55）

11-20（Activity LOW）仓位参考: Max Pain 405 ｜ Call Wall 435（-9.6%，弱）（OI 0.6k）

11-27（Activity LOW）仓位参考: Max Pain 430 ｜ Call Wall 460（-4.4%，弱）（OI 43）

📅 事件差分（观察，非因果）: 11-06（1D）ATM IV 53.8% vs 11-13 35.8%（差 +17.9pp）——覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-05/ISRG_morning.json