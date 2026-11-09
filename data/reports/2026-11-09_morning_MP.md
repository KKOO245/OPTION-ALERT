# 期权晨报 2026-11-09（快照 10:20 ET）

📊 市场环境

SPY $748.41 ｜ QQQ $674.67
VIX 21.34 ↓16.8%（5D +0.9%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 31.1（fear）
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
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-13 37C ΔOI +2,124（距现价 +1.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-13 37C ΔOI +2,124 占该期限总 OI 13.1%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 35.41 → 今开 36.13（+2.0%） | 较昨收变动（含盘初走势） ｜ 今日高 37.09 ｜ 低 35.10

Options: P/C成交量 0.49 | OI比 0.41 | ATM IV 86.4% | Skew 18.7pp | Term 0.77 | ExpMove ±9.1%（近端） | Rank 82%
量化视角： IV 历史高位（Rank 82%，期权偏贵）｜期限结构倒挂（Term 0.77，近月 IV 高于远月）｜保护溢价显著（Skew 18.7pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.41）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.49×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.41×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（4D）±9.1% ｜ 11-20（11D）±11.9% ｜ 11-27（18D）±5.9% ｜ 12-04（25D）±14.4%
   ⇒ IV–VIX Spread: +65.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,059,880 | GEX Change vs 上次快照 1,862,396 | Flip: Primary Flip: 35.61（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 305 / LOW 52 / INVALID 135
结构观察区: Primary Flip 35.61（全链重定价，覆盖 100%）
Put Wall 35（现价高于该位 4.4%）
最近结构参考: Flip 36（现价高于该位 2.6%）
量化视角： 正 Gamma（106万，无历史分位）｜由负转正（+186万）｜现价位于 Flip 上方 2.61%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 35（Put Wall）；上方 37（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 36（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 37.0C — Vol 2,698 | 最新价 $0.77 | OI 44→2168 (ΔOI +2124张) | ΔOI/Volume 78.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2124张（+4827.3% vs前日OI），连续性待观察（方向未知）
11-13 34.0P — Vol 938 | 最新价 $0.80 | OI 108→1008 (ΔOI +900张) | ΔOI/Volume 96.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增900张（+833.3% vs前日OI），连续性待观察（方向未知）
11-20 37.0C — Vol 487 | 最新价 $1.22 | OI 60→527 (ΔOI +467张) | ΔOI/Volume 95.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增467张（+778.3% vs前日OI），连续性待观察（方向未知）
11-13 38.0C — Vol 489 | 最新价 $0.50 | OI 207→548 (ΔOI +341张) | ΔOI/Volume 69.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增341张（+164.7% vs前日OI），连续性待观察（方向未知）
11-13 45.0C — Vol 302 | 最新价 $0.04 | OI 378→678 (ΔOI +300张) | ΔOI/Volume 99.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增300张（+79.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,132 张（Put 900 / Call 3,232），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +3.9k / P +1.4k ｜ Activity HIGH ｜ 4D
11-20  C +0.6k / P -0.4k ｜ Activity HIGH ｜ 11D
11-27  C +0.1k / P +96 ｜ Activity MEDIUM △ ｜ 18D
12-04  C +0.3k / P +94 ｜ Activity MEDIUM △ ｜ 25D

📆 11-13 Forward Structure
存量OI: C 11.5k / P 4.7k，今日变化ΔOI: C +3.9k / P +1.4k，平值价格ATM: C $1.31 / P $2.01 ｜ ATM IV 86.4%，净 delta 敞口 124k shares
Top ΔOI: C 37 +2,124 ｜ P 34 +900 ｜ C 38 +341
仓位参考: Max Pain 37 ｜ Call Wall 37（+1.3%，弱）（OI 2.2k） ｜ Put Wall 34（-7.0%，弱）（OI 1.0k）
量化解读： 存量 Call 重｜ATM IV 86.4%｜历史 Rank 82%（近端代理）｜IV/RV 1.55×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 124,453 股

📆 11-20 Forward Structure
存量OI: C 21.0k / P 12.8k，今日变化ΔOI: C +0.6k / P -0.4k，平值价格ATM: C $1.93 / P $2.43 ｜ ATM IV 77.5%，净 delta 敞口 61k shares
Top ΔOI: C 37 +467 ｜ P 40 -214 ｜ P 55 -120
仓位参考: Max Pain 43 ｜ Call Wall 40（+9.5%，弱）（OI 1.0k） ｜ Put Wall 35（-4.2%）（OI 3.8k）
量化解读： 存量 Call 重｜ATM IV 77.5%｜历史 Rank 82%（近端代理）｜IV/RV 1.39×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 61,421 股

11-27（MEDIUM △）Top ΔOI: 43P +66 ｜ 40C +56
11-27（MEDIUM △）仓位参考: Max Pain 43 ｜ Put Wall 38（+4.0%，弱）（OI 89）

12-04（MEDIUM △）仓位参考: Max Pain 35 ｜ Call Wall 35（-4.2%）（OI 0.5k） ｜ Put Wall 34（-7.0%）（OI 0.2k）

📅 事件差分（观察，非因果）: 11-13（4D）ATM IV 86.4% vs 11-20 77.5%（差 +8.8pp）——覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-09/MP_morning.json