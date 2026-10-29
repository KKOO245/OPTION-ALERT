# 期权晚报 2026-10-29（快照 16:40 ET）

📊 市场环境

SPY $769.36 ｜ QQQ $715.34
VIX 17.20 ↑1.7%（5D -9.6%） ｜ Vol Regime: NORMAL
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
🟡 **近现价集中开仓**: 10-30 288C ΔOI +21,206（距现价 +1.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## IWM

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
IWM: 今开 282.41 → 收盘 284.01（+0.6%） ｜ 今日高 285.26 ｜ 低 282.15 ｜ 昨收 281.29 → 收盘 284.01（+1.0%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-05，窗口结束前不做对错判定）

Options: P/C成交量 0.95 | OI比 0.71 | ATM IV 31.4% | Skew -0.3pp | Term 0.57 | ExpMove ±0.8%（近端） | Rank 82%
量化视角： IV 历史高位（Rank 82%，期权偏贵）｜期限结构倒挂（Term 0.57，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.3pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.71）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.95×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.71×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（1D）±0.8% ｜ 11-02（4D）±1.2% ｜ 11-03（5D）±1.3% ｜ 11-04（6D）±1.8%
   ⇒ IV–VIX Spread: +14.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 258,984,724 | GEX Change vs 上次快照 -82,797,343 | Flip: Primary Flip: 282.17（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 1169 / LOW 221 / INVALID 1016
结构观察区: Primary Flip 282.17（全链重定价，覆盖 92%）
Put Wall 270（弱结构｜现价高于该位 5.2%） | Call Wall 285（弱结构｜现价低于该位 0.3%）
最近结构参考: Call Wall 285（现价低于该位 0.3%）
量化视角： 正 Gamma（2.59亿，无历史分位）｜正 Gamma 减弱（8280万）｜现价位于 Flip 上方 0.65%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 270（Put Wall，弱结构） / 280（MaxPain，仅结算参考）；上方 285（Call Wall，弱结构）。
• Gamma 区域：切换参考 282（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-30  C +66.9k / P -6.8k ｜ Activity HIGH ｜ 1D
11-02  C +2.7k / P +2.7k ｜ Activity HIGH ｜ 4D
11-03  C +2.2k / P +4.4k ｜ Activity HIGH ｜ 5D
11-04  C +2.2k / P +2.9k ｜ Activity HIGH ｜ 6D

📆 10-30 Forward Structure
存量OI: C 276.1k / P 480.8k，今日变化ΔOI: C +66.9k / P -6.8k，平值价格ATM: C $1.37 / P $1.00 ｜ ATM IV 19.7%，净 delta 敞口 2.0M shares
Top ΔOI: C 288 +21,206 ｜ C 283 +15,896 ｜ C 287 +12,689
仓位参考: Max Pain 278 ｜ Call Wall 284（-0.0%，弱）（OI 28.0k） ｜ Put Wall 260（-8.5%）（OI 82.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 19.7%｜历史 Rank 82%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,968,669 股

📆 11-02 Forward Structure
存量OI: C 13.0k / P 13.5k，今日变化ΔOI: C +2.7k / P +2.7k，平值价格ATM: C $1.87 / P $1.48 ｜ ATM IV 14.1%，净 delta 敞口 87k shares
Top ΔOI: C 285 +581 ｜ P 280 +463 ｜ C 292 +376
仓位参考: Max Pain 277 ｜ Call Wall 287（+1.1%，弱）（OI 1.4k） ｜ Put Wall 275（-3.2%，弱）（OI 1.5k）
量化解读： 存量两侧均衡｜ATM IV 14.1%｜历史 Rank 82%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 87,368 股

📆 11-03 Forward Structure
存量OI: C 9.6k / P 15.9k，今日变化ΔOI: C +2.2k / P +4.4k，平值价格ATM: C $1.94 / P $1.76 ｜ ATM IV 15.1%，净 delta 敞口 77k shares
Top ΔOI: P 269 +1,523 ｜ P 277 +553 ｜ P 270 +468
仓位参考: Max Pain 279 ｜ Call Wall 282（-0.7%，弱）（OI 1.5k） ｜ Put Wall 270（-4.9%）（OI 3.0k）
量化解读： 存量 Put 重｜ATM IV 15.1%｜历史 Rank 82%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 76,909 股

📆 11-04 Forward Structure
存量OI: C 4.6k / P 10.7k，今日变化ΔOI: C +2.2k / P +2.9k，平值价格ATM: C $2.69 / P $2.32 ｜ ATM IV 17.2%，净 delta 敞口 65k shares
Top ΔOI: C 285 +698 ｜ P 275 +640 ｜ P 276 +485
仓位参考: Max Pain 280 ｜ Call Wall 277（-2.5%，弱）（OI 0.7k） ｜ Put Wall 280（-1.4%，弱）（OI 1.8k）
量化解读： 存量 Put 重｜ATM IV 17.2%｜历史 Rank 82%（近端代理）｜净 delta 敞口 正 64,991 股

📅 事件差分（观察，非因果）: 10-30（1D）ATM IV 19.7% vs 11-02 14.1%（差 +5.6pp）——覆盖 GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM、PCE 物价 Price Index MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-29/IWM_evening.json