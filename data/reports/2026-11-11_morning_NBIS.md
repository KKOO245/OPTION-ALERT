# 期权晨报 2026-11-11（快照 10:20 ET）

📊 市场环境

SPY $759.81 ｜ QQQ $nan
VIX 18.31 ↓5.9%（5D +10.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 37.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-11

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🔴 **事件差分**: 11-13（2D）ATM IV 220.1% vs 11-20 137.7%（差 +82.3pp），覆盖 成屋销售、PPI 生产者物价 MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-13 150C ΔOI +915（距现价 -2.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 134.00 → 今开 149.72（+11.7%） | 较昨收变动（含盘初走势） ｜ 今日高 155.96 ｜ 低 147.36

Options: P/C成交量 0.38 | OI比 0.60 | ATM IV 220.1% | Skew 6.6pp | Term 0.50 | ExpMove ±13.9%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.50，近月 IV 高于远月）｜保护溢价显著（Skew 6.6pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.60）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.38×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.60×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（2D）±13.9% ｜ 11-20（9D）±17.7% ｜ 11-27（16D）±19.8% ｜ 12-04（23D）±23.9%
   ⇒ IV–VIX Spread: +201.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 5,520,001 | GEX Change vs 上次快照 8,768,610 | Flip: Primary Flip: 142.61（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 694 / LOW 50 / INVALID 136
结构观察区: Primary Flip 142.61（全链重定价，覆盖 100%）
Put Wall 150（弱结构｜现价高于该位 2.9%）
最近结构参考: Put Wall 150（现价高于该位 2.9%）
量化视角： 正 Gamma（552万，无历史分位）｜由负转正（+877万）｜现价位于 Flip 上方 8.24%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（Put Wall，弱结构） / 140（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 143（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 75.0P — Vol 5,302 | 最新价 $0.14 | OI 767→5840 (ΔOI +5073张) | ΔOI/Volume 95.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5073张（+661.4% vs前日OI），连续性待观察（方向未知）
11-13 135.0C — Vol 1,586 | 最新价 $11.25 | OI 793→1774 (ΔOI +981张) | ΔOI/Volume 61.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增981张（+123.7% vs前日OI），连续性待观察（方向未知）
11-13 150.0C — Vol 2,684 | 最新价 $5.85 | OI 2639→3554 (ΔOI +915张) | ΔOI/Volume 34.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增915张（+34.7% vs前日OI），连续性待观察（方向未知）
11-20 150.0C — Vol 1,559 | 最新价 $7.85 | OI 1920→2712 (ΔOI +792张) | ΔOI/Volume 50.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增792张（+41.2% vs前日OI），连续性待观察（方向未知）
11-20 140.0C — Vol 1,125 | 最新价 $11.50 | OI 1535→2302 (ΔOI +767张) | ΔOI/Volume 68.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增767张（+50.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 8,528 张（Put 5,073 / Call 3,455），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +7.2k / P +9.0k ｜ Activity HIGH ｜ 2D
11-20  C +4.4k / P -1.0k ｜ Activity HIGH ｜ 9D
11-27  C +1.2k / P +0.2k ｜ Activity HIGH ｜ 16D
12-04  C +0.2k / P +80 ｜ Activity HIGH ｜ 23D

📆 11-13 Forward Structure
存量OI: C 83.0k / P 50.0k，今日变化ΔOI: C +7.2k / P +9.0k，平值价格ATM: C $10.95 / P $10.57 ｜ ATM IV 220.1%，净 delta 敞口 417k shares
Top ΔOI: C 135 +981 ｜ C 150 +915
仓位参考: Max Pain 140 ｜ Call Wall 140（-9.3%，弱）（OI 6.1k） ｜ Put Wall 150（-2.8%，弱）（OI 1.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 220.1%｜历史 Rank 100%（近端代理）｜IV/RV 1.96×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 417,361 股

📆 11-20 Forward Structure
存量OI: C 123.6k / P 109.1k，今日变化ΔOI: C +4.4k / P -1.0k，平值价格ATM: C $13.75 / P $13.55 ｜ ATM IV 137.7%，净 delta 敞口 241k shares
Top ΔOI: C 150 +792 ｜ C 140 +767 ｜ P 135 -691
仓位参考: Max Pain 175 ｜ Call Wall 150（-2.8%，弱）（OI 2.7k） ｜ Put Wall 150（-2.8%，弱）（OI 6.8k）
量化解读： 存量两侧均衡｜ATM IV 137.7%｜历史 Rank 100%（近端代理）｜IV/RV 1.23×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 240,878 股

📆 11-27 Forward Structure
存量OI: C 14.5k / P 16.9k，今日变化ΔOI: C +1.2k / P +0.2k，平值价格ATM: C $15.48 / P $15.14 ｜ ATM IV 118.2%，净 delta 敞口 34k shares
Top ΔOI: C 170 +129
仓位参考: Max Pain 190 ｜ Call Wall 150（-2.8%，弱）（OI 1.0k） ｜ Put Wall 155（+0.4%，弱）（OI 1.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 118.2%｜历史 Rank 100%（近端代理）｜IV/RV 1.05×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 34,074 股

📆 12-04 Forward Structure
存量OI: C 4.0k / P 5.0k，今日变化ΔOI: C +0.2k / P +80，平值价格ATM: C $16.50 / P $20.42 ｜ ATM IV 112.1%，净 delta 敞口 5k shares
仓位参考: Max Pain 155 ｜ Call Wall 150（-2.8%，弱）（OI 0.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 112.1%｜历史 Rank 100%（近端代理）｜IV/RV 1.00×（近似）｜净 delta 敞口 正 4,815 股

📅 事件差分（观察，非因果）: 11-13（2D）ATM IV 220.1% vs 11-20 137.7%（差 +82.3pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-11/NBIS_morning.json