# 期权晚报 2026-10-12（快照 16:40 ET）

📊 市场环境

SPY $778.10 ｜ QQQ $746.04
VIX 15.21 ↑2.5%（5D -2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 45.7（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-12

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-13 10:00　【高】成屋销售　预测 3.96 ｜ 实际 待公布 ｜ 前值 3.98
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.7 ｜ 实际 待公布 ｜ 前值 3.4
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 待公布 ｜ 前值 2.4
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **事件差分**: 10-16 ATM IV 79.7% vs 10-23 68.6%（差 +11.1pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-23 14P ΔOI +184（距现价 -2.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 15.03 → 收盘 14.29（-4.9%） ｜ 今日高 15.04 ｜ 低 14.23 ｜ 昨收 15.34 → 收盘 14.29（-6.8%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.90 | OI比 0.25 | ATM IV 79.7% | Skew -7.5pp | Term 0.86 | ExpMove ±7.3%（近端） | Rank 10%
量化视角： IV 历史低位（Rank 10%，期权偏便宜）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜Put 保护异常便宜（Skew -7.5pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.25）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.90×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.25×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（4D）±7.3% ｜ 10-23（11D）±24.6% ｜ 10-30（18D）±14.5% ｜ 11-06（25D）±19.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 430,983 | GEX Change vs 上次快照 988,257 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 134 / LOW 94 / INVALID 176
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: NO_CROSS
Put Wall 15（弱结构｜现价低于该位 4.7%）
最近结构参考: Put Wall 15（现价低于该位 4.7%）
量化视角： 正 Gamma（43万，无历史分位）｜由负转正（+99万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 15（Put Wall，弱结构） / 18（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 15.5P — Vol 1 | 最新价 $1.12 | OI 128→318 (ΔOI +190张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增190张（+148.4% vs前日OI），值得跟踪（方向未知）
10-23 14.0P — Vol 265 | 最新价 $0.36 | OI 267→451 (ΔOI +184张) | ΔOI/Volume 69.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增184张（+68.9% vs前日OI），连续性待观察（方向未知）
10-23 16.5P — Vol 120（Yahoo补） | 最新价 $1.58 | OI 45→160 (ΔOI +115张) | ΔOI/Volume 95.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增115张（+255.6% vs前日OI），连续性待观察（方向未知）
10-16 16.5P — Vol 2 | 最新价 $1.85 | OI 18→116 (ΔOI +98张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增98张（+544.4% vs前日OI），值得跟踪（方向未知）
10-16 14.0P — Vol 19 | 最新价 $0.20 | OI 336→431 (ΔOI +95张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增95张（+28.3% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 682 张（Put 682 / Call 0），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +0.1k / P +0.2k ｜ Activity MEDIUM △ ｜ 4D
10-23  C +5 / P +0.5k ｜ Activity MEDIUM △ ｜ 11D
10-30  C +33 / P +46 ｜ Activity LOW ｜ 18D
11-06  C +16 / P +6 ｜ Activity MEDIUM △ ｜ 25D

📆 10-16 Forward Structure
存量OI: C 21.9k / P 5.6k，今日变化ΔOI: C +0.1k / P +0.2k，平值价格ATM: C $0.64 / P $0.40 ｜ ATM IV 79.7%，净 delta 敞口 -5k shares
Top ΔOI: P 14 +95
仓位参考: Max Pain 18 ｜ Put Wall 15（+5.0%，弱）（OI 1.0k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 79.7%｜历史 Rank 10%（近端代理）｜IV/RV 1.44×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 4,624 股

10-23（MEDIUM △）Top ΔOI: 15P +190 ｜ 14P +184
10-23（MEDIUM △）仓位参考: Max Pain 17 ｜ Put Wall 14（-2.0%，弱）（OI 0.5k）

10-30（Activity LOW）仓位参考: Max Pain 16 ｜ Put Wall 14（-2.0%）（OI 0.3k）

11-06（MEDIUM △）仓位参考: Max Pain 16 ｜ Put Wall 15.5（+8.5%，弱）（OI 63）

📅 事件差分（观察，非因果）: 10-16（4D）ATM IV 79.7% vs 10-23 68.6%（差 +11.1pp）——覆盖 成屋销售、Core Inflation Rate MoM 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-12/NNE_evening.json