# 期权晨报 2026-11-04（快照 10:20 ET）

📊 市场环境

SPY $767.96 ｜ QQQ $691.95
VIX 17.01 ↓18.3%（5D +0.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-04

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 54.5 ｜ 前值 54.9　✅ 今日已公布
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🔴 **事件差分**: 11-06（2D）ATM IV 126.2% vs 11-13 82.0%（差 +44.2pp），覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 37.83 → 今开 38.02（+0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 38.96 ｜ 低 36.95

Options: P/C成交量 2.71 | OI比 0.45 | ATM IV 126.2% | Skew -7.5pp | Term 0.54 | ExpMove ±8.3%（近端） | Rank 98%
量化视角： IV 历史高位（Rank 98%，期权偏贵）｜期限结构倒挂（Term 0.54，近月 IV 高于远月）｜Put 保护异常便宜（Skew -7.5pp，Put IV < Call IV）｜⚠️ 重点观察：存量 Call 重（OI比 0.45）+ 当日成交偏 Put（P/C量 2.71）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 2.71×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.45×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（2D）±8.3% ｜ 11-13（9D）±8.4% ｜ 11-20（16D）±13.7% ｜ 11-27（23D）±15.0%
   ⇒ IV–VIX Spread: +109.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 597,731 | GEX Change vs 上次快照 -43,617 | Flip: Primary Flip: 36.48（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 267 / LOW 43 / INVALID 158
结构观察区: Primary Flip 36.48（全链重定价，覆盖 99%）
Put Wall 35（现价高于该位 6.1%）
最近结构参考: Flip 36（现价高于该位 1.8%）
量化视角： 正 Gamma（60万，无历史分位）｜正 Gamma 减弱（4万）｜现价位于 Flip 上方 1.82%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 35（Put Wall）；上方 40（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 36（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 35.0P — Vol 2,034 | 最新价 $1.14 | OI 1673→3629 (ΔOI +1956张) | ΔOI/Volume 96.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1956张（+116.9% vs前日OI），连续性待观察（方向未知）
11-06 35.0P — Vol 1,228 | 最新价 $0.46 | OI 492→1533 (ΔOI +1041张) | ΔOI/Volume 84.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1041张（+211.6% vs前日OI），连续性待观察（方向未知）
11-06 39.5C — Vol 436 | 最新价 $0.94 | OI 54→475 (ΔOI +421张) | ΔOI/Volume 96.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增421张（+779.6% vs前日OI），连续性待观察（方向未知）
11-06 38.0C — Vol 348 | 最新价 $1.37 | OI 40→349 (ΔOI +309张) | ΔOI/Volume 88.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增309张（+772.5% vs前日OI），连续性待观察（方向未知）
11-20 45.5C — Vol 309 | 最新价 $0.56 | OI 331→606 (ΔOI +275张) | ΔOI/Volume 89.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增275张（+83.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,002 张（Put 2,997 / Call 1,005），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +1.3k / P +1.0k ｜ Activity MEDIUM △ ｜ 2D
11-13  C +0.5k / P +0.2k ｜ Activity MEDIUM △ ｜ 9D
11-20  C +0.5k / P +2.2k ｜ Activity HIGH ｜ 16D
11-27  C +52 / P +55 ｜ Activity MEDIUM △ ｜ 23D

📆 11-06 Forward Structure
存量OI: C 14.3k / P 6.4k，今日变化ΔOI: C +1.3k / P +1.0k，平值价格ATM: C $1.79 / P $1.31 ｜ ATM IV 126.2%，净 delta 敞口 29k shares
Top ΔOI: P 35 +1,041 ｜ C 39 +421 ｜ C 38 +309
仓位参考: Max Pain 40 ｜ Call Wall 40（+7.7%，弱）（OI 0.6k） ｜ Put Wall 35（-5.8%，弱）（OI 1.5k）
量化解读： 存量 Call 重｜ATM IV 126.2%｜历史 Rank 98%（近端代理）｜IV/RV 2.47×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 28,712 股

11-13（MEDIUM △）Top ΔOI: 35P +161 ｜ 40C +62
11-13（MEDIUM △）仓位参考: Max Pain 40 ｜ Call Wall 40（+7.7%，弱）（OI 0.9k） ｜ Put Wall 39（+5.0%）（OI 0.8k）

📆 11-20 Forward Structure
存量OI: C 17.4k / P 12.5k，今日变化ΔOI: C +0.5k / P +2.2k，平值价格ATM: C $3.30 / P $1.78 ｜ ATM IV 74.7%，净 delta 敞口 -69k shares
Top ΔOI: P 35 +1,956 ｜ P 42 +144
仓位参考: Max Pain 44 ｜ Call Wall 40（+7.7%，弱）（OI 0.9k） ｜ Put Wall 35（-5.8%）（OI 3.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 74.7%｜历史 Rank 98%（近端代理）｜IV/RV 1.46×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 68,883 股

11-27（MEDIUM △）Top ΔOI: 38C +34 ｜ 38P +19
11-27（MEDIUM △）仓位参考: Max Pain 44 ｜ Put Wall 38（+2.3%，弱）（OI 90）

📅 事件差分（观察，非因果）: 11-06（2D）ATM IV 126.2% vs 11-13 82.0%（差 +44.2pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-04/MP_morning.json