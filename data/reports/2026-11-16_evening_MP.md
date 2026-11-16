# 期权晚报 2026-11-16（快照 16:40 ET）

📊 市场环境

SPY $739.95 ｜ QQQ $661.75
VIX 22.91 ↑18.7%（5D +15.0%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 31.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-17 08:30　【高】零售销售 MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.8
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 待公布 ｜ 前值 1.221
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 待公布 ｜ 前值 1.4

🔍 重点速览
🟡 **事件差分**: 11-20 ATM IV 84.2% vs 11-27 70.0%（差 +14.1pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 37.50 → 收盘 36.09（-3.8%） ｜ 今日高 38.24 ｜ 低 36.06 ｜ 昨收 38.76 → 收盘 36.09（-6.9%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-23，窗口结束前不做对错判定）

Options: P/C成交量 0.57 | OI比 0.49 | ATM IV 84.2% | Skew -0.0pp | Term 0.81 | ExpMove ±8.4%（近端） | Rank 78%
量化视角： IV 历史高位（Rank 78%，期权偏贵）｜期限结构倒挂（Term 0.81，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.0pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.49）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.57×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.49×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（4D）±8.4% ｜ 11-27（11D）±9.1% ｜ 12-04（18D）±11.5% ｜ 12-11（25D）±16.0%
   ⇒ IV–VIX Spread: +61.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 3,895,515 | GEX Change vs 上次快照 -2,396,528 | Flip: Primary Flip: 33.51（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 233 / LOW 61 / INVALID 144
结构观察区: Primary Flip 33.51（全链重定价，覆盖 100%）
Put Wall 35（现价高于该位 3.1%）
最近结构参考: Put Wall 35（现价高于该位 3.1%）
量化视角： 正 Gamma（390万，无历史分位）｜正 Gamma 减弱（240万）｜现价位于 Flip 上方 7.70%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 35（Put Wall）；上方 40（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 34（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 40.0C — Vol 1,278 | 最新价 $1.53 | OI 2166→16729 (ΔOI +14563张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14563张（+672.4% vs前日OI），连续性待观察（方向未知）
12-18 45.0C — Vol 637 | 最新价 $0.62 | OI 5735→16598 (ΔOI +10863张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10863张（+189.4% vs前日OI），连续性待观察（方向未知）
11-20 40.0C — Vol 726 | 最新价 $0.26 | OI 1277→1989 (ΔOI +712张) | ΔOI/Volume 98.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增712张（+55.8% vs前日OI），连续性待观察（方向未知）
11-27 50.0C — Vol 1 | 最新价 $0.06 | OI 1964→2553 (ΔOI +589张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增589张（+30.0% vs前日OI），连续性待观察（方向未知）
11-20 42.5C — Vol 44 | 最新价 $0.08 | OI 139→486 (ΔOI +347张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增347张（+249.6% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 27,074 张（Put 0 / Call 27,074），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C +2.0k / P +0.3k ｜ Activity HIGH ｜ 4D
11-27  C +1.0k / P +0.3k ｜ Activity HIGH ｜ 11D
12-04  C +0.1k / P +74 ｜ Activity HIGH ｜ 18D
12-11  C +61 / P +32 ｜ Activity MEDIUM △ ｜ 25D

📆 11-20 Forward Structure
存量OI: C 28.2k / P 13.8k，今日变化ΔOI: C +2.0k / P +0.3k，平值价格ATM: C $1.82 / P $1.20 ｜ ATM IV 84.2%，净 delta 敞口 3k shares
仓位参考: Max Pain 40 ｜ Call Wall 39.5（+9.4%，弱）（OI 1.7k） ｜ Put Wall 35（-3.0%）（OI 3.9k）
量化解读： 存量 Call 重｜ATM IV 84.2%｜历史 Rank 78%（近端代理）｜IV/RV 1.37×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 3,135 股

📆 11-27 Forward Structure
存量OI: C 7.8k / P 4.6k，今日变化ΔOI: C +1.0k / P +0.3k，平值价格ATM: C $1.98 / P $1.32 ｜ ATM IV 70.0%，净 delta 敞口 -3k shares
Top ΔOI: P 35 +209
仓位参考: Max Pain 42 ｜ Put Wall 33（-8.6%）（OI 2.5k）
量化解读： 存量 Call 重｜ATM IV 70.0%｜历史 Rank 78%（近端代理）｜IV/RV 1.14×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 2,545 股

📆 12-04 Forward Structure
存量OI: C 2.4k / P 0.9k，今日变化ΔOI: C +0.1k / P +74，平值价格ATM: C $2.45 / P $1.70 ｜ ATM IV 68.2%，净 delta 敞口 -4k shares
仓位参考: Max Pain 35 ｜ Call Wall 35（-3.0%）（OI 0.5k） ｜ Put Wall 34（-5.8%）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 68.2%｜历史 Rank 78%（近端代理）｜IV/RV 1.11×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 4,148 股

12-11（MEDIUM △）Top ΔOI: 39C -21
12-11（MEDIUM △）仓位参考: Max Pain 42 ｜ Call Wall 37（+2.5%，弱）（OI 68） ｜ Put Wall 37（+2.5%，弱）（OI 31）

📅 事件差分（观察，非因果）: 11-20（4D）ATM IV 84.2% vs 11-27 70.0%（差 +14.1pp）——覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-16/MP_evening.json