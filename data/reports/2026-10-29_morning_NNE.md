# 期权晨报 2026-10-29（快照 10:20 ET）

📊 市场环境

SPY $769.36 ｜ QQQ $715.34
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
🟡 **事件差分**: 10-30 ATM IV 94.0% vs 11-06 82.9%（差 +11.0pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-06 12P ΔOI +176（距现价 +1.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 12.39 → 今开 12.11（-2.3%） | 较昨收变动（含盘初走势） ｜ 今日高 12.44 ｜ 低 12.06

Options: P/C成交量 3.77 | OI比 0.17 | ATM IV 94.0% | Skew 22.5pp | Term 0.82 | ExpMove ±6.5%（近端） | Rank 33%
量化视角： IV 中性（Rank 33%）｜期限结构倒挂（Term 0.82，近月 IV 高于远月）｜保护溢价显著（Skew 22.5pp，Put 明显贵于 Call）｜⚠️ 重点观察：存量 Call 重（OI比 0.17）+ 当日成交偏 Put（P/C量 3.77）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 3.77×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.17×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（1D）±6.5% ｜ 11-06（8D）±10.4% ｜ 11-13（15D）±14.5% ｜ 11-20（22D）±15.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 511,265 | GEX Change vs 上次快照 -67,964 | Flip: Primary Flip: 11.82（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 189 / LOW 86 / INVALID 133
结构观察区: Primary Flip 11.82（全链重定价，覆盖 94%）
Put Wall 12（弱结构｜现价高于该位 2.9%）
最近结构参考: Put Wall 12（现价高于该位 2.9%）
量化视角： 正 Gamma（51万，无历史分位）｜正 Gamma 减弱（7万）｜现价位于 Flip 上方 4.44%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 12（Put Wall，弱结构）；上方 13（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 12（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 12.5P — Vol 176 | 最新价 $0.73 | OI 26→202 (ΔOI +176张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增176张（+676.9% vs前日OI），连续性待观察（方向未知）
11-06 12.0P — Vol 176 | 最新价 $0.57 | OI 25→182 (ΔOI +157张) | ΔOI/Volume 89.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增157张（+628.0% vs前日OI），连续性待观察（方向未知）
11-06 11.0P — Vol 126 | 最新价 $0.20 | OI 168→294 (ΔOI +126张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增126张（+75.0% vs前日OI），连续性待观察（方向未知）
10-30 13.0C — Vol 76 | 最新价 $0.07 | OI 751→824 (ΔOI +73张) | ΔOI/Volume 96.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增73张（+9.7% vs前日OI），连续性待观察（方向未知）
11-06 14.0P — Vol 67 | 最新价 $1.90 | OI 41→103 (ΔOI +62张) | ΔOI/Volume 92.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增62张（+151.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 594 张（Put 521 / Call 73），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +60 / P -0.2k ｜ Activity HIGH ｜ 1D
11-06  C +53 / P +0.5k ｜ Activity HIGH ｜ 8D
11-13  C -3 / P +5 ｜ Activity MEDIUM △ ｜ 15D
11-20  C +21 / P +12 ｜ Activity MEDIUM △ ｜ 22D

📆 10-30 Forward Structure
存量OI: C 8.5k / P 1.4k，今日变化ΔOI: C +60 / P -0.2k，平值价格ATM: C $0.20 / P $0.60 ｜ ATM IV 94.0%，净 delta 敞口 24k shares
Top ΔOI: P 13 -81 ｜ C 13 +73
仓位参考: Max Pain 13 ｜ Put Wall 13（+5.3%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 94.0%｜历史 Rank 33%（近端代理）｜IV/RV 1.44×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 23,893 股

📆 11-06 Forward Structure
存量OI: C 1.9k / P 1.5k，今日变化ΔOI: C +53 / P +0.5k，平值价格ATM: C $0.55 / P $0.73 ｜ ATM IV 82.9%，净 delta 敞口 -21k shares
Top ΔOI: P 12 +176 ｜ P 12 +157
仓位参考: Max Pain 14 ｜ Put Wall 11.5（-6.9%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 82.9%｜历史 Rank 33%（近端代理）｜IV/RV 1.27×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 21,138 股

11-13（MEDIUM △）Top ΔOI: 11P +2
11-13（MEDIUM △）仓位参考: Max Pain 14 ｜ Call Wall 13.5（+9.3%，弱）（OI 0.1k） ｜ Put Wall 13（+5.3%，弱）（OI 68）

11-20（MEDIUM △）仓位参考: Max Pain 15 ｜ Put Wall 12（-2.8%，弱）（OI 0.3k）

📅 事件差分（观察，非因果）: 10-30（1D）ATM IV 94.0% vs 11-06 82.9%（差 +11.0pp）——覆盖 GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM、PCE 物价 Price Index MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-29/NNE_morning.json