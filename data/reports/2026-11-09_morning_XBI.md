# 期权晨报 2026-11-09（快照 10:20 ET）

📊 市场环境

SPY $752.69 ｜ QQQ $679.35
VIX 21.34 ↓16.8%（5D +0.9%） ｜ Vol Regime: ELEVATED
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
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **事件差分**: 11-13 ATM IV 57.0% vs 11-20 45.3%（差 +11.8pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-13 147P ΔOI +1,730（距现价 -4.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 152.21 → 今开 153.21（+0.7%） | 较昨收变动（含盘初走势） ｜ 今日高 154.52 ｜ 低 151.00

Options: P/C成交量 2.62 | OI比 1.27 | ATM IV 57.0% | Skew 13.5pp | Term 0.68 | ExpMove ±4.5%（近端） | Rank 98%
量化视角： IV 历史高位（Rank 98%，期权偏贵）｜期限结构倒挂（Term 0.68，近月 IV 高于远月）｜保护溢价显著（Skew 13.5pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 2.62）——观察点，非方向信号
   ⇒ Put/Call Volume: 2.62×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.27×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-13（4D）±4.5% ｜ 11-20（11D）±7.4% ｜ 11-27（18D）±9.3% ｜ 12-04（25D）±0.0%
   ⇒ IV–VIX Spread: +35.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 8,133,670 | GEX Change vs 上次快照 16,633,259 | Flip: Primary Flip: 150.77（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 423 / LOW 114 / INVALID 385
结构观察区: Primary Flip 150.77（全链重定价，覆盖 99%）
最近结构参考: Flip 151（现价高于该位 2.1%）
量化视角： 正 Gamma（813万，无历史分位）｜由负转正（+1663万）｜现价位于 Flip 上方 2.15%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 148（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 151（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 140.0P — Vol 9,205 | 最新价 $0.85 | OI 1192→9661 (ΔOI +8469张) | ΔOI/Volume 92.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8469张（+710.5% vs前日OI），连续性待观察（方向未知）
11-13 147.0P — Vol 1,755 | 最新价 $1.40 | OI 68→1798 (ΔOI +1730张) | ΔOI/Volume 98.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1730张（+2544.1% vs前日OI），连续性待观察（方向未知）
11-13 142.0C — Vol 1,000 | 最新价 $10.53 | OI 0→1000 (ΔOI +1000张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1000张（前日OI缺失），连续性待观察（方向未知）
11-20 153.0C — Vol 816 | 最新价 $4.40 | OI 332→958 (ΔOI +626张) | ΔOI/Volume 76.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增626张（+188.6% vs前日OI），连续性待观察（方向未知）
11-20 163.0C — Vol 519 | 最新价 $0.69 | OI 252→738 (ΔOI +486张) | ΔOI/Volume 93.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增486张（+192.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 12,311 张（Put 10,199 / Call 2,112），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +1.9k / P +1.6k ｜ Activity HIGH ｜ 4D
11-20  C +0.8k / P +7.6k ｜ Activity HIGH ｜ 11D
11-27  C +21 / P +78 ｜ Activity LOW ｜ 18D
12-04  C +8 / P -3 ｜ Activity LOW ｜ 25D

📆 11-13 Forward Structure
存量OI: C 5.0k / P 6.4k，今日变化ΔOI: C +1.9k / P +1.6k，平值价格ATM: C $3.00 / P $3.85 ｜ ATM IV 57.0%，净 delta 敞口 88k shares
Top ΔOI: P 147 +1,730 ｜ C 142 +1,000 ｜ P 142 -654
仓位参考: Max Pain 148 ｜ Call Wall 160（+3.9%，弱）（OI 0.8k） ｜ Put Wall 147（-4.6%，弱）（OI 1.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 57.0%｜历史 Rank 98%（近端代理）｜IV/RV 1.43×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 87,609 股

📆 11-20 Forward Structure
存量OI: C 23.5k / P 52.6k，今日变化ΔOI: C +0.8k / P +7.6k，平值价格ATM: C $4.00 / P $7.35 ｜ ATM IV 45.3%，净 delta 敞口 -48k shares
Top ΔOI: P 140 +8,469 ｜ P 145 -1,020 ｜ C 153 +626
仓位参考: Max Pain 153 ｜ Call Wall 160（+3.9%，弱）（OI 2.2k） ｜ Put Wall 145（-5.9%，弱）（OI 6.2k）
量化解读： 存量 Put 重｜ATM IV 45.3%｜历史 Rank 98%（近端代理）｜IV/RV 1.13×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 47,976 股

11-27（Activity LOW）仓位参考: Max Pain 158 ｜ Call Wall 152.5（-1.0%，弱）（OI 0.1k） ｜ Put Wall 156（+1.3%）（OI 0.2k）

12-04（Activity LOW）仓位参考: Max Pain 161 ｜ Call Wall 162（+5.2%，弱）（OI 44） ｜ Put Wall 147（-4.6%，弱）（OI 45）

📅 事件差分（观察，非因果）: 11-13（4D）ATM IV 57.0% vs 11-20 45.3%（差 +11.8pp）——覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-09/XBI_morning.json