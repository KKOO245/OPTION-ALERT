# 期权晚报 2026-11-19（快照 16:40 ET）

📊 市场环境

SPY $715.87 ｜ QQQ $nan
VIX 28.44 ↑15.8%（5D +52.1%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 18.7（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🔴 **Vol Regime 升档**: ELEVATED → STRESS（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-20 148C ΔOI +1,740（距现价 +2.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## XBI

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
XBI: 今开 145.38 → 收盘 144.12（-0.9%） ｜ 今日高 148.92 ｜ 低 143.59 ｜ 昨收 145.04 → 收盘 144.12（-0.6%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-24，窗口结束前不做对错判定）

Options: P/C成交量 0.60 | OI比 1.55 | ATM IV 60.2% | Skew -7.2pp | Term 0.64 | ExpMove ±3.4%（近端） | Rank 99%
量化视角： IV 历史高位（Rank 99%，期权偏贵）｜期限结构倒挂（Term 0.64，近月 IV 高于远月）｜Put 保护异常便宜（Skew -7.2pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.60×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.55×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-20（1D）±3.4% ｜ 11-27（8D）±4.5% ｜ 12-04（15D）±7.3% ｜ 12-11（22D）±3.8%
   ⇒ IV–VIX Spread: +31.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -33,432,562 | GEX Change vs 上次快照 1,234,801 | Flip: Primary Flip: 148.38（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 87%（带内） ｜ IV 有效性: VALID 360 / LOW 194 / INVALID 372
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 148.38（全链重定价，覆盖 87%）
最近结构参考: Flip 148（现价低于该位 2.9%）
量化视角： 负 Gamma（3343万，无历史分位）｜负 Gamma 缓解（+123万）｜现价位于 Flip 下方 2.87%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 150（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 148（全链重定价，覆盖 87%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C +2.5k / P -3.1k ｜ Activity HIGH ｜ 1D
11-27  C +0.4k / P -88 ｜ Activity HIGH ｜ 8D
12-04  C +0.1k / P -12 ｜ Activity MEDIUM △ ｜ 15D
12-11  C +52 / P +36 ｜ Activity MEDIUM △ ｜ 22D

📆 11-20 Forward Structure
存量OI: C 38.5k / P 59.8k，今日变化ΔOI: C +2.5k / P -3.1k，平值价格ATM: C $3.20 / P $1.71 ｜ ATM IV 60.2%，净 delta 敞口 298k shares
Top ΔOI: C 148 +1,740 ｜ P 147 -1,603 ｜ C 147 +590
仓位参考: Max Pain 150 ｜ Call Wall 150（+4.1%，弱）（OI 4.4k） ｜ Put Wall 140（-2.9%，弱）（OI 12.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 60.2%｜历史 Rank 99%（近端代理）｜IV/RV 1.53×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 297,990 股

📆 11-27 Forward Structure
存量OI: C 2.3k / P 5.2k，今日变化ΔOI: C +0.4k / P -88，平值价格ATM: C $4.70 / P $1.85 ｜ ATM IV 36.4%，净 delta 敞口 13k shares
Top ΔOI: C 152 +172 ｜ P 146 -140 ｜ P 145 +36
仓位参考: Max Pain 152 ｜ Call Wall 152.5（+5.8%）（OI 0.3k） ｜ Put Wall 143（-0.8%，弱）（OI 1.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 36.4%｜历史 Rank 99%（近端代理）｜IV/RV 0.93×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 13,268 股

12-04（MEDIUM △）Top ΔOI: 156C +110 ｜ 156P -26
12-04（MEDIUM △）仓位参考: Max Pain 158 ｜ Call Wall 144（-0.1%，弱）（OI 50） ｜ Put Wall 148（+2.7%，弱）（OI 93）

12-11（MEDIUM △）Top ΔOI: 147C +60 ｜ 135P +21
12-11（MEDIUM △）仓位参考: Max Pain 147 ｜ Call Wall 147（+2.0%）（OI 0.4k） ｜ Put Wall 135（-6.3%，弱）（OI 0.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-19/XBI_evening.json