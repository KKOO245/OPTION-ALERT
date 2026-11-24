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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## XBI

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
XBI: 今开 147.54 → 收盘 156.82（+6.3%） ｜ 今日高 157.30 ｜ 低 147.54 ｜ 昨收 147.16 → 收盘 156.82（+6.6%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-12-01，窗口结束前不做对错判定）

Options: P/C成交量 1.54 | OI比 1.17 | ATM IV 45.4% | Skew 8.9pp | Term 0.79 | ExpMove ±6.7%（近端） | Rank 92%
量化视角： IV 历史高位（Rank 92%，期权偏贵）｜期限结构倒挂（Term 0.79，近月 IV 高于远月）｜保护溢价显著（Skew 8.9pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 1.54）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.54×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.17×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-27（3D）±6.7% ｜ 12-04（10D）±9.1% ｜ 12-11（17D）±0.8% ｜ 12-18（24D）±10.1%
   ⇒ IV–VIX Spread: +19.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 18,300,803 | GEX Change vs 上次快照 7,869,081 | Flip: Primary Flip: 147.34（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 370 / LOW 133 / INVALID 409
结构观察区: Primary Flip 147.34（全链重定价，覆盖 99%）
最近结构参考: Flip 147（现价高于该位 6.4%）
量化视角： 正 Gamma（1830万，无历史分位）｜正 Gamma 增强（+787万）｜现价位于 Flip 上方 6.43%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 145（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 147（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-27  C +0 / P +0 ｜ Activity LOW ｜ 3D
12-04  C +0 / P +0 ｜ Activity LOW ｜ 10D
12-11  C +0 / P +0 ｜ Activity LOW ｜ 17D
12-18  C +0 / P +0 ｜ Activity LOW ｜ 24D

📆 11-27 Forward Structure
存量OI: C 5.6k / P 6.6k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $0.01 / P $10.42 ｜ ATM IV 45.4%，净 delta 敞口 0 shares
仓位参考: Max Pain 145 ｜ Call Wall 151（-3.7%，弱）（OI 0.4k） ｜ Put Wall 147（-6.3%，弱）（OI 0.3k）
量化解读： 存量两侧均衡｜ATM IV 45.4%｜历史 Rank 92%（近端代理）｜IV/RV 1.07×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

12-04（Activity LOW）仓位参考: Max Pain 154 ｜ Call Wall 154（-1.8%，弱）（OI 0.2k）

12-11（Activity LOW）仓位参考: Max Pain 147 ｜ Call Wall 147（-6.3%）（OI 0.8k）

12-18（Activity LOW）仓位参考: Max Pain 137

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-24/XBI_evening.json