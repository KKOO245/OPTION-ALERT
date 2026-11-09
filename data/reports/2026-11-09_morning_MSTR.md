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
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **事件差分**: 11-13 ATM IV 96.4% vs 11-20 85.4%（差 +11.0pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-20 120P ΔOI +3,235（距现价 -4.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 128.93 → 今开 124.58（-3.4%） | 较昨收变动（含盘初走势） ｜ 今日高 128.33 ｜ 低 122.48

Options: P/C成交量 0.50 | OI比 0.68 | ATM IV 96.4% | Skew 9.5pp | Term 0.81 | ExpMove ±8.2%（近端） | Rank 76%
量化视角： IV 历史高位（Rank 76%，期权偏贵）｜期限结构倒挂（Term 0.81，近月 IV 高于远月）｜保护溢价显著（Skew 9.5pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.68）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.50×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.68×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（4D）±8.2% ｜ 11-20（11D）±12.3% ｜ 11-27（18D）±14.3% ｜ 12-04（25D）±16.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 31,612,103 | GEX Change vs 上次快照 30,759,391 | Flip: Primary Flip: 118.95（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 510 / LOW 154 / INVALID 318
结构观察区: Primary Flip 118.95（全链重定价，覆盖 100%）
Call Wall 135（弱结构｜现价低于该位 6.8%）
最近结构参考: Flip 119（现价高于该位 5.8%）
量化视角： 正 Gamma（3161万，无历史分位）｜正 Gamma 增强（+3076万）｜现价位于 Flip 上方 5.82%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 132（MaxPain，仅结算参考） / 135（Call Wall，弱结构）。
• Gamma 区域：切换参考 119（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 133.0C — Vol 43,370 | 最新价 $4.10 | OI 132→43164 (ΔOI +43032张) | ΔOI/Volume 99.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增43032张（+32600.0% vs前日OI），连续性待观察（方向未知）
11-13 139.0C — Vol 45,795 | 最新价 $2.27 | OI 210→41153 (ΔOI +40943张) | ΔOI/Volume 89.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增40943张（+19496.7% vs前日OI），连续性待观察（方向未知）
11-13 80.0P — Vol 19,650 | 最新价 $0.15 | OI 5049→24055 (ΔOI +19006张) | ΔOI/Volume 96.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增19006张（+376.4% vs前日OI），连续性待观察（方向未知）
11-13 138.0C — Vol 21,658 | 最新价 $2.43 | OI 242→18425 (ΔOI +18183张) | ΔOI/Volume 84.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18183张（+7513.6% vs前日OI），连续性待观察（方向未知）
11-13 132.0C — Vol 17,040 | 最新价 $4.60 | OI 392→15768 (ΔOI +15376张) | ΔOI/Volume 90.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15376张（+3922.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 136,540 张（Put 19,006 / Call 117,534），跨 1 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +162.5k / P +54.1k ｜ Activity HIGH ｜ 4D
11-20  C +5.0k / P +6.9k ｜ Activity MEDIUM △ ｜ 11D
11-27  C +0.6k / P +2.3k ｜ Activity HIGH ｜ 18D
12-04  C +0.4k / P +2.4k ｜ Activity MEDIUM △ ｜ 25D

📆 11-13 Forward Structure
存量OI: C 213.8k / P 145.4k，今日变化ΔOI: C +162.5k / P +54.1k，平值价格ATM: C $5.10 / P $5.20 ｜ ATM IV 96.4%，净 delta 敞口 4.0M shares
Top ΔOI: C 133 +43,032 ｜ C 139 +40,943 ｜ P 80 +19,006
仓位参考: Max Pain 132 ｜ Call Wall 133（+5.7%，弱）（OI 43.2k） ｜ Put Wall 125（-0.7%，弱）（OI 5.8k）
量化解读： 存量 Call 重｜ATM IV 96.4%｜历史 Rank 76%（近端代理）｜IV/RV 1.29×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 3,964,198 股

11-20（MEDIUM △）Top ΔOI: 120P +3,235 ｜ 145C +2,847
11-20（MEDIUM △）仓位参考: Max Pain 135 ｜ Call Wall 135（+7.3%）（OI 43.1k） ｜ Put Wall 120（-4.7%，弱）（OI 10.5k）

📆 11-27 Forward Structure
存量OI: C 14.4k / P 37.0k，今日变化ΔOI: C +0.6k / P +2.3k，平值价格ATM: C $8.86 / P $9.20 ｜ ATM IV 79.1%，净 delta 敞口 -50k shares
Top ΔOI: P 90 +575
仓位参考: Max Pain 155 ｜ Call Wall 130（+3.3%，弱）（OI 0.9k） ｜ Put Wall 135（+7.3%，弱）（OI 2.6k）
量化解读： 存量 Put 重｜ATM IV 79.1%｜历史 Rank 76%（近端代理）｜IV/RV 1.06×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 49,953 股

12-04（MEDIUM △）Top ΔOI: 85P +693 ｜ 125P +190
12-04（MEDIUM △）仓位参考: Max Pain 150 ｜ Put Wall 135（+7.3%，弱）（OI 1.7k）

📅 事件差分（观察，非因果）: 11-13（4D）ATM IV 96.4% vs 11-20 85.4%（差 +11.0pp）——覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-09/MSTR_morning.json