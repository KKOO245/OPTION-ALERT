# 期权晨报 2026-11-10（快照 10:20 ET）

📊 市场环境

SPY $750.86 ｜ QQQ $674.76
VIX 19.85 ↓0.3%（5D -4.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-10

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-10 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周二 11-10 08:30　【高】Inflation Rate MoM　预测 0.3 ｜ 实际 0.4 ｜ 前值 0.6　✅ 今日已公布
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🔴 **事件差分**: 11-13（3D）ATM IV 222.6% vs 11-20 150.2%（差 +72.4pp），覆盖 Core Inflation Rate MoM、Inflation Rate MoM 等
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 11-13 140C ΔOI +4,463（距现价 -3.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 141.45 → 今开 137.42（-2.8%） | 较昨收变动（含盘初走势） ｜ 今日高 146.23 ｜ 低 135.30

Options: P/C成交量 0.49 | OI比 0.54 | ATM IV 222.6% | Skew 11.0pp | Term 0.53 | ExpMove ±16.2%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.53，近月 IV 高于远月）｜保护溢价显著（Skew 11.0pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.54）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.49×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.54×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（3D）±16.2% ｜ 11-20（10D）±20.1% ｜ 11-27（17D）±21.5% ｜ 12-04（24D）±24.4%
   ⇒ IV–VIX Spread: +202.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 1,381,724 | GEX Change vs 上次快照 4,665,966 | Flip: Primary Flip: 141.44（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 694 / LOW 49 / INVALID 137
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 141.44（全链重定价，覆盖 100%）
Put Wall 150（弱结构｜现价低于该位 3.5%）
最近结构参考: Flip 141（现价高于该位 2.3%）
量化视角： 正 Gamma（138万，无历史分位）｜由负转正（+467万）｜现价位于 Flip 上方 2.33%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 150（Put Wall，弱结构） / 145（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 141（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 140.0C — Vol 6,840 | 最新价 $12.60 | OI 1287→5750 (ΔOI +4463张) | ΔOI/Volume 65.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4463张（+346.8% vs前日OI），连续性待观察（方向未知）
11-13 187.5C — Vol 2,042 | 最新价 $1.20 | OI 2639→4112 (ΔOI +1473张) | ΔOI/Volume 72.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1473张（+55.8% vs前日OI），连续性待观察（方向未知）
11-13 144.0C — Vol 1,083 | 最新价 $10.84 | OI 70→1006 (ΔOI +936张) | ΔOI/Volume 86.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增936张（+1337.1% vs前日OI），连续性待观察（方向未知）
11-13 85.0P — Vol 1,014 | 最新价 $0.20 | OI 176→987 (ΔOI +811张) | ΔOI/Volume 80.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增811张（+460.8% vs前日OI），连续性待观察（方向未知）
11-13 177.5C — Vol 1,004 | 最新价 $2.06 | OI 225→1032 (ΔOI +807张) | ΔOI/Volume 80.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增807张（+358.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 8,490 张（Put 811 / Call 7,679），跨 1 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +15.9k / P +6.6k ｜ Activity HIGH ｜ 3D
11-20  C +2.1k / P -0.7k ｜ Activity HIGH ｜ 10D
11-27  C +0.6k / P +1.3k ｜ Activity MEDIUM △ ｜ 17D
12-04  C +0.4k / P +0.2k ｜ Activity MEDIUM △ ｜ 24D

📆 11-13 Forward Structure
存量OI: C 75.8k / P 41.1k，今日变化ΔOI: C +15.9k / P +6.6k，平值价格ATM: C $11.40 / P $12.10 ｜ ATM IV 222.6%，净 delta 敞口 519k shares
Top ΔOI: C 140 +4,463 ｜ C 187 +1,473 ｜ C 144 +936
仓位参考: Max Pain 145 ｜ Call Wall 140（-3.3%，弱）（OI 5.8k） ｜ Put Wall 150（+3.6%，弱）（OI 1.5k）
量化解读： 存量 Call 重｜ATM IV 222.6%｜历史 Rank 100%（近端代理）｜IV/RV 1.99×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 518,976 股

📆 11-20 Forward Structure
存量OI: C 119.2k / P 110.1k，今日变化ΔOI: C +2.1k / P -0.7k，平值价格ATM: C $14.20 / P $14.90 ｜ ATM IV 150.2%，净 delta 敞口 96k shares
Top ΔOI: P 115 -967 ｜ C 170 +423 ｜ C 150 +400
仓位参考: Max Pain 175 ｜ Call Wall 155（+7.1%，弱）（OI 1.9k） ｜ Put Wall 150（+3.6%，弱）（OI 6.8k）
量化解读： 存量两侧均衡｜ATM IV 150.2%｜历史 Rank 100%（近端代理）｜IV/RV 1.34×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 95,716 股

11-27（MEDIUM △）Top ΔOI: 90P +530 ｜ 95P +414
11-27（MEDIUM △）仓位参考: Max Pain 190 ｜ Call Wall 150（+3.6%，弱）（OI 1.0k） ｜ Put Wall 155（+7.1%，弱）（OI 1.2k）

12-04（MEDIUM △）Top ΔOI: 160C +54 ｜ 205P +43
12-04（MEDIUM △）仓位参考: Max Pain 155 ｜ Call Wall 150（+3.6%，弱）（OI 0.4k）

📅 事件差分（观察，非因果）: 11-13（3D）ATM IV 222.6% vs 11-20 150.2%（差 +72.4pp）——覆盖 Core Inflation Rate MoM、Inflation Rate MoM 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-10/NBIS_morning.json