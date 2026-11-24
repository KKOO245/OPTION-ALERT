# 期权晚报 2026-11-24（快照 16:40 ET）

📊 市场环境

SPY $718.78 ｜ QQQ $638.10
VIX 26.36 ↓1.0%（5D +3.5%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 17.4（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-24

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-25 08:30　【高】Personal Spending MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.5
- 周三 11-25 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 11-25 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 11-25 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 3.5 ｜ 实际 待公布 ｜ 前值 1.5
- 周三 11-25 08:30　【高】耐用品订单 Orders MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 1.8

🔍 重点速览
🟡 **近现价集中开仓**: 11-25 263P ΔOI +2,702（距现价 -1.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 12-01 270C ΔOI +2,965 占该期限总 OI 10.5%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## IWM

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
IWM: 今开 264.02 → 收盘 267.14（+1.2%） ｜ 今日高 268.31 ｜ 低 263.97 ｜ 昨收 265.74 → 收盘 267.14（+0.5%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-12-01，窗口结束前不做对错判定）

Options: P/C成交量 1.08 | OI比 2.12 | ATM IV 36.0% | Skew -4.0pp | Term 0.67 | ExpMove ±1.1%（近端） | Rank 74%
量化视角： IV 中性（Rank 74%）｜期限结构倒挂（Term 0.67，近月 IV 高于远月）｜Put 保护异常便宜（Skew -4.0pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.08×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 2.12×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-25（1D）±1.1% ｜ 11-27（3D）±1.5% ｜ 11-30（6D）±2.1% ｜ 12-01（7D）±2.5%
   ⇒ IV–VIX Spread: +9.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -746,176,287 | GEX Change vs 上次快照 59,095,308 | Flip: Primary Flip: 280.12（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 1187 / LOW 269 / INVALID 1264
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 280.12（全链重定价，覆盖 92%）
Put Wall 260（弱结构｜现价高于该位 2.7%）
最近结构参考: Put Wall 260（现价高于该位 2.7%）
量化视角： 负 Gamma（7.46亿，无历史分位）｜负 Gamma 缓解（+5910万）｜现价位于 Flip 下方 4.63%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 260（Put Wall，弱结构） / 266（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 280（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-25  C +6.0k / P +4.5k ｜ Activity HIGH ｜ 1D
11-27  C +15.5k / P -2.4k ｜ Activity HIGH ｜ 3D
11-30  C +5.4k / P +6.4k ｜ Activity HIGH ｜ 6D
12-01  C +4.2k / P +4.0k ｜ Activity HIGH ｜ 7D

📆 11-25 Forward Structure
存量OI: C 29.8k / P 43.1k，今日变化ΔOI: C +6.0k / P +4.5k，平值价格ATM: C $1.34 / P $1.72 ｜ ATM IV 27.0%，净 delta 敞口 23k shares
Top ΔOI: P 263 +2,702 ｜ C 270 +2,591
仓位参考: Max Pain 266 ｜ Call Wall 277（+3.7%，弱）（OI 4.4k） ｜ Put Wall 261（-2.3%，弱）（OI 6.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 27.0%｜历史 Rank 74%（近端代理）｜IV/RV 0.89×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 22,659 股

📆 11-27 Forward Structure
存量OI: C 112.0k / P 240.4k，今日变化ΔOI: C +15.5k / P -2.4k，平值价格ATM: C $1.91 / P $2.20 ｜ ATM IV 21.5%，净 delta 敞口 1.4M shares
Top ΔOI: P 255 +6,537 ｜ C 270 +6,434 ｜ P 276 -5,280
仓位参考: Max Pain 270 ｜ Call Wall 270（+1.1%，弱）（OI 9.7k） ｜ Put Wall 270（+1.1%，弱）（OI 35.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 21.5%｜历史 Rank 74%（近端代理）｜IV/RV 0.71×（近似）｜净 delta 敞口 正 1,439,370 股

📆 11-30 Forward Structure
存量OI: C 21.7k / P 61.3k，今日变化ΔOI: C +5.4k / P +6.4k，平值价格ATM: C $2.65 / P $2.89 ｜ ATM IV 20.1%，净 delta 敞口 37k shares
Top ΔOI: P 257 +4,562 ｜ C 273 +1,561 ｜ C 270 +1,122
仓位参考: Max Pain 269 ｜ Call Wall 276（+3.3%，弱）（OI 3.9k） ｜ Put Wall 255（-4.5%，弱）（OI 10.0k）
量化解读： 存量 Put 重｜ATM IV 20.1%｜历史 Rank 74%（近端代理）｜IV/RV 0.67×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 37,071 股

📆 12-01 Forward Structure
存量OI: C 13.7k / P 14.5k，今日变化ΔOI: C +4.2k / P +4.0k，平值价格ATM: C $3.25 / P $3.30 ｜ ATM IV 21.6%，净 delta 敞口 39k shares
Top ΔOI: C 270 +2,965 ｜ P 260 +2,164 ｜ C 271 +459
仓位参考: Max Pain 265 ｜ Call Wall 270（+1.1%，弱）（OI 3.1k） ｜ Put Wall 260（-2.7%）（OI 6.0k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 21.6%｜历史 Rank 74%（近端代理）｜IV/RV 0.71×（近似）｜净 delta 敞口 正 38,589 股

📅 事件差分（观察，非因果）: 11-25（1D）ATM IV 27.0% vs 11-27 21.5%（差 +5.5pp）——覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-24/IWM_evening.json