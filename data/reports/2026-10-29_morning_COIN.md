# 期权晨报 2026-10-29（快照 10:20 ET）

📊 市场环境

SPY $769.48 ｜ QQQ $716.11
VIX 16.74 ↓1.0%（5D -12.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.6（fear）
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
🔴 **事件差分**: 10-30（1D）ATM IV 163.5% vs 11-06 89.4%（差 +74.0pp），覆盖 GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM、PCE 物价 Price Index MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 162.32 → 今开 157.62（-2.9%） | 较昨收变动（含盘初走势） ｜ 今日高 163.00 ｜ 低 157.61

Options: P/C成交量 1.25 | OI比 0.64 | ATM IV 163.5% | Skew -0.1pp | Term 0.41 | ExpMove ±7.7%（近端） | Rank 98%
量化视角： IV 历史高位（Rank 98%，期权偏贵）｜期限结构倒挂（Term 0.41，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.1pp，Put IV < Call IV）｜⚠️ 重点观察：存量 Call 重（OI比 0.64）+ 当日成交偏 Put（P/C量 1.25）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.25×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.64×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（1D）±7.7% ｜ 11-06（8D）±10.8% ｜ 11-13（15D）±12.6% ｜ 11-20（22D）±14.7%
   ⇒ IV–VIX Spread: +146.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 12,279,506 | GEX Change vs 上次快照 1,120,041 | Flip: Primary Flip: 153.02（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 460 / LOW 135 / INVALID 295
结构观察区: Primary Flip 153.02（全链重定价，覆盖 100%）
Call Wall 170（弱结构｜现价低于该位 4.6%）
最近结构参考: Call Wall 170（现价低于该位 4.6%）
量化视角： 正 Gamma（1228万，无历史分位）｜正 Gamma 增强（+112万）｜现价位于 Flip 上方 5.93%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 170（MaxPain，仅结算参考） / 170（Call Wall，弱结构）。
• Gamma 区域：切换参考 153（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 90.0P — Vol 12,986 | 最新价 $0.05 | OI 1644→9630 (ΔOI +7986张) | ΔOI/Volume 61.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7986张（+485.8% vs前日OI），连续性待观察（方向未知）
10-30 100.0P — Vol 1,586 | 最新价 $0.05 | OI 3248→4610 (ΔOI +1362张) | ΔOI/Volume 85.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1362张（+41.9% vs前日OI），连续性待观察（方向未知）
10-30 85.0P — Vol 1,116 | 最新价 $0.03 | OI 417→1507 (ΔOI +1090张) | ΔOI/Volume 97.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1090张（+261.4% vs前日OI），连续性待观察（方向未知）
10-30 165.0C — Vol 797 | 最新价 $5.52 | OI 426→851 (ΔOI +425张) | ΔOI/Volume 53.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增425张（+99.8% vs前日OI），连续性待观察（方向未知）
10-30 80.0P — Vol 353 | 最新价 $0.04 | OI 187→536 (ΔOI +349张) | ΔOI/Volume 98.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增349张（+186.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 11,212 张（Put 10,787 / Call 425），跨 1 个期限｜远端彩票/名义（4 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +2.1k / P +11.8k ｜ Activity HIGH ｜ 1D
11-06  C +0.9k / P +0.6k ｜ Activity MEDIUM △ ｜ 8D
11-13  C +0.6k / P +0.4k ｜ Activity MEDIUM △ ｜ 15D
11-20  C +0.3k / P +0.4k ｜ Activity MEDIUM △ ｜ 22D

📆 10-30 Forward Structure
存量OI: C 73.8k / P 47.0k，今日变化ΔOI: C +2.1k / P +11.8k，平值价格ATM: C $6.16 / P $6.33 ｜ ATM IV 163.5%，净 delta 敞口 83k shares
仓位参考: Max Pain 170 ｜ Call Wall 172.5（+6.4%，弱）（OI 11.9k） ｜ Put Wall 150（-7.5%，弱）（OI 2.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 163.5%｜历史 Rank 98%（近端代理）｜IV/RV 3.20×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 82,887 股

11-06（MEDIUM △）仓位参考: Max Pain 170 ｜ Call Wall 175（+8.0%，弱）（OI 0.9k）

11-13（MEDIUM △）Top ΔOI: 180C +217 ｜ 162C +108
11-13（MEDIUM △）仓位参考: Max Pain 172 ｜ Call Wall 177.5（+9.5%）（OI 1.2k） ｜ Put Wall 155（-4.4%，弱）（OI 1.1k）

11-20（MEDIUM △）Top ΔOI: 140P +233
11-20（MEDIUM △）仓位参考: Max Pain 170 ｜ Call Wall 170（+4.9%）（OI 13.7k） ｜ Put Wall 150（-7.5%，弱）（OI 3.2k）

📅 事件差分（观察，非因果）: 10-30（1D）ATM IV 163.5% vs 11-06 89.4%（差 +74.0pp）——覆盖 GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM、PCE 物价 Price Index MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-29/COIN_morning.json