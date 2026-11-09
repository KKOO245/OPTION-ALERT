# 期权晨报 2026-11-09（快照 10:20 ET）

📊 市场环境

SPY $752.91 ｜ QQQ $679.35
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
🔴 **事件差分**: 11-13（4D）ATM IV 127.7% vs 11-20 107.7%（差 +20.0pp），覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY 等
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 11-13 200C ΔOI +749（距现价 +2.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 173.24 → 今开 182.24（+5.2%） | 较昨收变动（含盘初走势） ｜ 今日高 198.40 ｜ 低 180.50

Options: P/C成交量 0.37 | OI比 0.78 | ATM IV 127.7% | Skew 13.7pp | Term 0.74 | ExpMove ±10.8%（近端） | Rank 82%
量化视角： IV 历史高位（Rank 82%，期权偏贵）｜期限结构倒挂（Term 0.74，近月 IV 高于远月）｜保护溢价显著（Skew 13.7pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.78）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.37×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.78×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（4D）±10.8% ｜ 11-20（11D）±14.8% ｜ 11-27（18D）±20.8% ｜ 12-04（25D）±20.4%
   ⇒ IV–VIX Spread: +106.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -3,721,482 | GEX Change vs 上次快照 1,208,548 | Flip: Primary Flip: 209.12（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 582 / LOW 121 / INVALID 225
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 209.12（全链重定价，覆盖 100%）
Put Wall 200（现价低于该位 2.7%）
最近结构参考: Put Wall 200（现价低于该位 2.7%）
量化视角： 负 Gamma（372万，无历史分位）｜负 Gamma 缓解（+121万）｜现价位于 Flip 下方 6.98%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 185（MaxPain，仅结算参考）；上方 200（Put Wall）。
• Gamma 区域：切换参考 209（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 172.5P — Vol 1,221 | 最新价 $14.37 | OI 81→1140 (ΔOI +1059张) | ΔOI/Volume 86.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1059张（+1307.4% vs前日OI），连续性待观察（方向未知）
11-13 200.0C — Vol 2,417 | 最新价 $2.86 | OI 665→1414 (ΔOI +749张) | ΔOI/Volume 31.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增749张（+112.6% vs前日OI），连续性待观察（方向未知）
11-20 200.0C — Vol 2,361 | 最新价 $5.45 | OI 2894→3535 (ΔOI +641张) | ΔOI/Volume 27.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增641张（+22.1% vs前日OI），连续性待观察（方向未知）
11-13 175.0P — Vol 1,413 | 最新价 $12.18 | OI 1039→1626 (ΔOI +587张) | ΔOI/Volume 41.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增587张（+56.5% vs前日OI），连续性待观察（方向未知）
11-13 180.0P — Vol 1,041 | 最新价 $15.10 | OI 426→977 (ΔOI +551张) | ΔOI/Volume 52.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增551张（+129.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,587 张（Put 2,197 / Call 1,390），跨 2 个期限｜有实质成本保护 3 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +6.3k / P +6.9k ｜ Activity HIGH ｜ 4D
11-20  C +1.8k / P +0.6k ｜ Activity HIGH ｜ 11D
11-27  C +0.3k / P +0.1k ｜ Activity MEDIUM △ ｜ 18D
12-04  C +0.5k / P +0.1k ｜ Activity HIGH ｜ 25D

📆 11-13 Forward Structure
存量OI: C 30.8k / P 24.1k，今日变化ΔOI: C +6.3k / P +6.9k，平值价格ATM: C $10.60 / P $10.40 ｜ ATM IV 127.7%，净 delta 敞口 200k shares
Top ΔOI: C 200 +749 ｜ P 175 +587 ｜ P 180 +551
仓位参考: Max Pain 185 ｜ Call Wall 180（-7.5%）（OI 2.4k） ｜ Put Wall 180（-7.5%，弱）（OI 1.0k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 127.7%｜历史 Rank 82%（近端代理）｜IV/RV 1.15×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 199,656 股

📆 11-20 Forward Structure
存量OI: C 73.8k / P 78.6k，今日变化ΔOI: C +1.8k / P +0.6k，平值价格ATM: C $14.67 / P $14.15 ｜ ATM IV 107.7%，净 delta 敞口 102k shares
Top ΔOI: P 172 +1,059 ｜ C 200 +641
仓位参考: Max Pain 220 ｜ Call Wall 200（+2.8%，弱）（OI 3.5k） ｜ Put Wall 200（+2.8%，弱）（OI 5.4k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 107.7%｜历史 Rank 82%（近端代理）｜IV/RV 0.97×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 102,109 股

11-27（MEDIUM △）Top ΔOI: 200C +136 ｜ 190P +38
11-27（MEDIUM △）仓位参考: Max Pain 220 ｜ Call Wall 200（+2.8%，弱）（OI 0.6k） ｜ Put Wall 190（-2.3%，弱）（OI 1.2k）

📆 12-04 Forward Structure
存量OI: C 5.6k / P 5.9k，今日变化ΔOI: C +0.5k / P +0.1k，平值价格ATM: C $20.28 / P $19.30 ｜ ATM IV 93.6%，净 delta 敞口 15k shares
Top ΔOI: C 225 +304 ｜ C 200 +125 ｜ P 200 +89
仓位参考: Max Pain 205 ｜ Call Wall 200（+2.8%，弱）（OI 0.6k） ｜ Put Wall 200（+2.8%）（OI 1.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 93.6%｜历史 Rank 82%（近端代理）｜IV/RV 0.84×（近似）｜净 delta 敞口 正 15,104 股

📅 事件差分（观察，非因果）: 11-13（4D）ATM IV 127.7% vs 11-20 107.7%（差 +20.0pp）——覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-09/BE_morning.json