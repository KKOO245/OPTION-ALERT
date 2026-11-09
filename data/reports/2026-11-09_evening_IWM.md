# 期权晚报 2026-11-09（快照 16:40 ET）

📊 市场环境

SPY $752.69 ｜ QQQ $679.35
VIX 19.92 ↓22.3%（5D -5.8%） ｜ Vol Regime: NORMAL
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
🟡 **近现价集中开仓**: 11-10 283C ΔOI +6,509（距现价 +0.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-12 285C ΔOI +3,962 占该期限总 OI 13.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## IWM

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
IWM: 今开 277.44 → 收盘 282.51（+1.8%） ｜ 今日高 283.79 ｜ 低 276.81 ｜ 昨收 273.67 → 收盘 282.51（+3.2%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-16，窗口结束前不做对错判定）

Options: P/C成交量 0.65 | OI比 0.95 | ATM IV 32.8% | Skew -8.7pp | Term 0.60 | ExpMove ±1.1%（近端） | Rank 74%
量化视角： IV 中性（Rank 74%）｜期限结构倒挂（Term 0.60，近月 IV 高于远月）｜Put 保护异常便宜（Skew -8.7pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.65×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.95×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-10（1D）±1.1% ｜ 11-11（2D）±1.3% ｜ 11-12（3D）±1.5% ｜ 11-13（4D）±1.8%
   ⇒ IV–VIX Spread: +12.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -211,737,392 | GEX Change vs 上次快照 342,384,990 | Flip: Primary Flip: 285.15（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 1468 / LOW 196 / INVALID 1012
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 285.15（全链重定价，覆盖 98%）
Put Wall 260（弱结构｜现价高于该位 8.7%） | Call Wall 290（弱结构｜现价低于该位 2.6%）
最近结构参考: Flip 285（现价低于该位 0.9%）
量化视角： 负 Gamma（2.12亿，无历史分位）｜负 Gamma 缓解（+3.42亿）｜现价位于 Flip 下方 0.93%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 260（Put Wall，弱结构） / 276（MaxPain，仅结算参考）；上方 290（Call Wall，弱结构）。
• Gamma 区域：切换参考 285（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 260.0P — Vol 83,181 | 最新价 $0.36 | OI 115488→160408 (ΔOI +44920张) | ΔOI/Volume 54.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增44920张（+38.9% vs前日OI），连续性待观察（方向未知）
11-20 267.0P — Vol 30,869 | 最新价 $0.67 | OI 45591→75914 (ΔOI +30323张) | ΔOI/Volume 98.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增30323张（+66.5% vs前日OI），连续性待观察（方向未知）
11-27 267.0P — Vol 1,114 | 最新价 $1.04 | OI 1972→32084 (ΔOI +30112张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增30112张（+1527.0% vs前日OI），连续性待观察（方向未知）
量化视角： 3 个事件合计 ΔOI ≈ 105,355 张（Put 105,355 / Call 0），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-10  C +19.3k / P +5.5k ｜ Activity HIGH ｜ 1D
11-11  C +1.7k / P +1.1k ｜ Activity MEDIUM △ ｜ 2D
11-12  C +11.4k / P +2.3k ｜ Activity HIGH ｜ 3D
11-13  C +14.4k / P +27.7k ｜ Activity HIGH ｜ 4D

📆 11-10 Forward Structure
存量OI: C 43.5k / P 32.2k，今日变化ΔOI: C +19.3k / P +5.5k，平值价格ATM: C $1.17 / P $1.87 ｜ ATM IV 25.1%，净 delta 敞口 1.3M shares
Top ΔOI: C 283 +6,509 ｜ C 275 +5,130 ｜ C 281 +3,181
仓位参考: Max Pain 277 ｜ Call Wall 283（+0.2%，弱）（OI 6.9k） ｜ Put Wall 265（-6.2%，弱）（OI 4.6k）
量化解读： 存量 Call 重｜ATM IV 25.1%｜历史 Rank 74%（近端代理）｜IV/RV 1.11×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,294,743 股

11-11（MEDIUM △）Top ΔOI: 255P -2,469 ｜ 270P +2,211
11-11（MEDIUM △）仓位参考: Max Pain 279 ｜ Call Wall 286（+1.2%，弱）（OI 1.8k） ｜ Put Wall 270（-4.4%，弱）（OI 3.2k）

📆 11-12 Forward Structure
存量OI: C 19.1k / P 11.3k，今日变化ΔOI: C +11.4k / P +2.3k，平值价格ATM: C $1.97 / P $2.33 ｜ ATM IV 21.3%，净 delta 敞口 617k shares
Top ΔOI: C 285 +3,962 ｜ C 279 +1,606 ｜ C 283 +1,170
仓位参考: Max Pain 277 ｜ Call Wall 285（+0.9%）（OI 4.6k） ｜ Put Wall 257.5（-8.9%，弱）（OI 0.9k）
量化解读： 存量 Call 重｜ATM IV 21.3%｜历史 Rank 74%（近端代理）｜IV/RV 0.94×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 617,169 股

📆 11-13 Forward Structure
存量OI: C 92.7k / P 163.7k，今日变化ΔOI: C +14.4k / P +27.7k，平值价格ATM: C $2.50 / P $2.55 ｜ ATM IV 21.2%，净 delta 敞口 805k shares
Top ΔOI: P 264 +4,590 ｜ P 269 +4,376 ｜ P 256 +4,105
仓位参考: Max Pain 278 ｜ Call Wall 302（+6.9%，弱）（OI 13.7k） ｜ Put Wall 265（-6.2%，弱）（OI 14.1k）
量化解读： 存量 Put 重｜ATM IV 21.2%｜历史 Rank 74%（近端代理）｜IV/RV 0.94×（近似）｜净 delta 敞口 正 805,135 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-09/IWM_evening.json