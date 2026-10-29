# 期权晨报 2026-10-29（快照 10:20 ET）

📊 市场环境

SPY $769.48 ｜ QQQ $715.67
VIX 16.74 ↓1.0%（5D -12.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-29

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 3.4 ｜ 前值 2.2　✅ 今日已公布
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 0.5 ｜ 前值 0.9　✅ 今日已公布
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-30 155P ΔOI +2,192（距现价 -2.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-06 151P ΔOI +1,348 占该期限总 OI 17.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 157.51 → 今开 157.64（+0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 160.27 ｜ 低 156.95

Options: P/C成交量 21.65 | OI比 5.24 | ATM IV 44.4% | Skew 13.6pp | Term 0.76 | ExpMove ±1.6%（近端） | Rank 93%
量化视角： IV 历史高位（Rank 93%，期权偏贵）｜期限结构倒挂（Term 0.76，近月 IV 高于远月）｜保护溢价显著（Skew 13.6pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 21.65）——观察点，非方向信号
   ⇒ Put/Call Volume: 21.65×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 5.24×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-30（1D）±1.6% ｜ 11-06（8D）±5.6% ｜ 11-13（15D）±5.3% ｜ 11-20（22D）±7.8%
   ⇒ IV–VIX Spread: +27.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,134,731 | GEX Change vs 上次快照 -50,385 | Flip: Candidates 158.95 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 79%（带内） ｜ IV 有效性: VALID 326 / LOW 86 / INVALID 362
结构观察区: ≈159（全链重定价，覆盖 79%，CONDITIONAL）
Call Wall 165（现价低于该位 3.5%）
最近结构参考: Flip 159（现价高于该位 0.2%）
量化视角： 正 Gamma（113万，无历史分位）｜正 Gamma 减弱（5万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 154（MaxPain，仅结算参考）；上方 165（Call Wall）。
• Gamma 区域：切换参考 159（全链重定价，覆盖 79%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 155.0P — Vol 2,305 | 最新价 $1.18 | OI 130→2322 (ΔOI +2192张) | ΔOI/Volume 95.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2192张（+1686.2% vs前日OI），连续性待观察（方向未知）
11-06 151.0P — Vol 1,746 | 最新价 $1.10 | OI 535→1883 (ΔOI +1348张) | ΔOI/Volume 77.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1348张（+252.0% vs前日OI），连续性待观察（方向未知）
10-30 163.0C — Vol 1,273 | 最新价 $0.23 | OI 110→1080 (ΔOI +970张) | ΔOI/Volume 76.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增970张（+881.8% vs前日OI），连续性待观察（方向未知）
10-30 154.0P — Vol 2,506 | 最新价 $0.97 | OI 61→1003 (ΔOI +942张) | ΔOI/Volume 37.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增942张（+1544.3% vs前日OI），连续性待观察（方向未知）
11-20 175.0C — Vol 1,055 | 最新价 $0.66 | OI 680→1188 (ΔOI +508张) | ΔOI/Volume 48.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增508张（+74.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,960 张（Put 4,482 / Call 1,478），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +0.9k / P -0.8k ｜ Activity MEDIUM △ ｜ 1D
11-06  C +0.5k / P +1.5k ｜ Activity HIGH ｜ 8D
11-13  C +39 / P -0.3k ｜ Activity MEDIUM △ ｜ 15D
11-20  C +0.8k / P -3.1k ｜ Activity HIGH ｜ 22D

📆 10-30 Forward Structure
存量OI: C 12.1k / P 63.6k，今日变化ΔOI: C +0.9k / P -0.8k，平值价格ATM: C $1.22 / P $1.41 ｜ ATM IV 44.4%，净 delta 敞口 -9k shares
Top ΔOI: P 155 +2,192 ｜ P 152 -2,137 ｜ P 148 -1,004
仓位参考: Max Pain 154 ｜ Call Wall 155（-2.7%，弱）（OI 2.2k） ｜ Put Wall 150（-5.8%，弱）（OI 9.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 44.4%｜历史 Rank 93%（近端代理）｜IV/RV 1.33×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 8,552 股

📆 11-06 Forward Structure
存量OI: C 2.5k / P 5.2k，今日变化ΔOI: C +0.5k / P +1.5k，平值价格ATM: C $3.78 / P $5.10 ｜ ATM IV 38.2%，净 delta 敞口 -4k shares
Top ΔOI: P 151 +1,348 ｜ C 160 +74 ｜ C 163 +53
仓位参考: Max Pain 153 ｜ Call Wall 156（-2.0%，弱）（OI 0.3k） ｜ Put Wall 151（-5.2%）（OI 1.9k）
量化解读： 存量 Put 重｜ATM IV 38.2%｜历史 Rank 93%（近端代理）｜IV/RV 1.15×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 4,188 股

11-13（MEDIUM △）Top ΔOI: 153P -203 ｜ 148P +154
11-13（MEDIUM △）仓位参考: Max Pain 150 ｜ Call Wall 160（+0.5%）（OI 0.4k） ｜ Put Wall 153（-3.9%，弱）（OI 0.2k）

📆 11-20 Forward Structure
存量OI: C 20.8k / P 36.4k，今日变化ΔOI: C +0.8k / P -3.1k，平值价格ATM: C $4.42 / P $8.03 ｜ ATM IV 33.8%，净 delta 敞口 47k shares
Top ΔOI: P 145 -1,730 ｜ C 175 +508
仓位参考: Max Pain 154 ｜ Call Wall 165（+3.6%）（OI 7.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 33.8%｜历史 Rank 93%（近端代理）｜IV/RV 1.02×（近似）｜净 delta 敞口 正 46,819 股

📅 事件差分（观察，非因果）: 10-30（1D）ATM IV 44.4% vs 11-06 38.2%（差 +6.2pp）——覆盖 GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM、PCE 物价 Price Index MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-29/XBI_morning.json