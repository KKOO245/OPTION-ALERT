# 期权晨报 2026-10-29（快照 10:20 ET）

📊 市场环境

SPY $765.72 ｜ QQQ $715.34
VIX 16.74 ↓1.0%（5D -12.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.6（fear）
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
🔴 **事件差分**: 10-30（1D）ATM IV 123.9% vs 11-06 81.6%（差 +42.3pp），覆盖 GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM、PCE 物价 Price Index MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 10-30 147C ΔOI +3,868（距现价 +4.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 145.16 → 今开 141.42（-2.6%） | 较昨收变动（含盘初走势） ｜ 今日高 142.07 ｜ 低 138.88

Options: P/C成交量 0.95 | OI比 0.66 | ATM IV 123.9% | Skew -1.1pp | Term 0.57 | ExpMove ±5.8%（近端） | Rank 92%
量化视角： IV 历史高位（Rank 92%，期权偏贵）｜期限结构倒挂（Term 0.57，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.1pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.66）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.95×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.66×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（1D）±5.8% ｜ 11-06（8D）±9.8% ｜ 11-13（15D）±11.4% ｜ 11-20（22D）±15.0%
   ⇒ IV–VIX Spread: +107.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 29,326,562 | GEX Change vs 上次快照 -15,994,984 | Flip: Primary Flip: 135.93（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 589 / LOW 87 / INVALID 240
结构观察区: Primary Flip 135.93（全链重定价，覆盖 100%）
Call Wall 135（弱结构｜现价高于该位 4.6%）
最近结构参考: Flip 136（现价高于该位 3.9%）
量化视角： 正 Gamma（2933万，无历史分位）｜正 Gamma 减弱（1599万）｜现价位于 Flip 上方 3.90%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 135（Call Wall，弱结构）；上方 142（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 136（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 157.5C — Vol 20,582 | 最新价 $1.00 | OI 10400→24614 (ΔOI +14214张) | ΔOI/Volume 69.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14214张（+136.7% vs前日OI），连续性待观察（方向未知）
10-30 147.0C — Vol 5,570 | 最新价 $3.81 | OI 6295→10163 (ΔOI +3868张) | ΔOI/Volume 69.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3868张（+61.5% vs前日OI），连续性待观察（方向未知）
11-06 150.0C — Vol 2,562 | 最新价 $5.50 | OI 1372→2660 (ΔOI +1288张) | ΔOI/Volume 50.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1288张（+93.9% vs前日OI），连续性待观察（方向未知）
11-06 116.0P — Vol 1,245 | 最新价 $0.70 | OI 149→1363 (ΔOI +1214张) | ΔOI/Volume 97.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1214张（+814.8% vs前日OI），连续性待观察（方向未知）
11-06 118.0P — Vol 1,187 | 最新价 $0.84 | OI 53→1194 (ΔOI +1141张) | ΔOI/Volume 96.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1141张（+2152.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 21,725 张（Put 2,355 / Call 19,370），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +14.9k / P -6.3k ｜ Activity HIGH ｜ 1D
11-06  C +5.0k / P +11.3k ｜ Activity HIGH ｜ 8D
11-13  C +0.7k / P +3.8k ｜ Activity MEDIUM △ ｜ 15D
11-20  C +1.0k / P +2.7k ｜ Activity HIGH ｜ 22D

📆 10-30 Forward Structure
存量OI: C 248.6k / P 165.1k，今日变化ΔOI: C +14.9k / P -6.3k，平值价格ATM: C $4.28 / P $3.95 ｜ ATM IV 123.9%，净 delta 敞口 386k shares
Top ΔOI: C 157 +14,214 ｜ C 160 -5,556 ｜ C 147 +3,868
仓位参考: Max Pain 142 ｜ Call Wall 152.5（+8.0%，弱）（OI 38.8k）
量化解读： 存量 Call 重｜ATM IV 123.9%｜历史 Rank 92%（近端代理）｜IV/RV 1.86×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 386,069 股

📆 11-06 Forward Structure
存量OI: C 29.2k / P 66.1k，今日变化ΔOI: C +5.0k / P +11.3k，平值价格ATM: C $7.12 / P $6.75 ｜ ATM IV 81.6%，净 delta 敞口 -33k shares
Top ΔOI: C 150 +1,288 ｜ P 116 +1,214 ｜ P 118 +1,141
仓位参考: Max Pain 155 ｜ Call Wall 150（+6.2%，弱）（OI 2.7k） ｜ Put Wall 155（+9.7%，弱）（OI 3.6k）
量化解读： 存量 Put 重｜ATM IV 81.6%｜历史 Rank 92%（近端代理）｜IV/RV 1.22×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 33,376 股

11-13（MEDIUM △）仓位参考: Max Pain 160 ｜ Put Wall 155（+9.7%，弱）（OI 2.4k）

📆 11-20 Forward Structure
存量OI: C 147.9k / P 114.5k，今日变化ΔOI: C +1.0k / P +2.7k，平值价格ATM: C $10.75 / P $10.40 ｜ ATM IV 73.5%，净 delta 敞口 -17k shares
仓位参考: Max Pain 135 ｜ Call Wall 135（-4.4%）（OI 42.4k） ｜ Put Wall 130（-8.0%，弱）（OI 4.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 73.5%｜历史 Rank 92%（近端代理）｜IV/RV 1.10×（近似）｜净 delta 敞口 负 17,391 股

📅 事件差分（观察，非因果）: 10-30（1D）ATM IV 123.9% vs 11-06 81.6%（差 +42.3pp）——覆盖 GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM、PCE 物价 Price Index MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-29/MSTR_morning.json