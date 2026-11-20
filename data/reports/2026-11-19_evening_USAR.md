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
🟡 **近现价集中开仓**: 11-20 7C ΔOI +905（距现价 +1.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 12-11 8C ΔOI +1,977 占该期限总 OI 30.4%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 6.88 → 收盘 6.87（-0.1%） ｜ 今日高 7.32 ｜ 低 6.65 ｜ 昨收 6.56 → 收盘 6.87（+4.7%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-26，窗口结束前不做对错判定）

Options: P/C成交量 0.23 | OI比 0.42 | ATM IV 145.6% | Skew -2.5pp | Term 0.73 | ExpMove ±6.4%（近端） | Rank 79%
量化视角： IV 历史高位（Rank 79%，期权偏贵）｜期限结构倒挂（Term 0.73，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.5pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.42）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.23×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.42×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（1D）±6.4% ｜ 11-27（8D）±13.4% ｜ 12-04（15D）±18.5% ｜ 12-11（22D）±22.3%
   ⇒ IV–VIX Spread: +117.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 746,482 | GEX Change vs 上次快照 -42,356 | Flip: Primary Flip: 6.59（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 188 / LOW 102 / INVALID 142
结构观察区: Primary Flip 6.59（全链重定价，覆盖 100%）
最近结构参考: Flip 7（现价高于该位 4.2%）
量化视角： 正 Gamma（75万，无历史分位）｜正 Gamma 减弱（4万）｜现价位于 Flip 上方 4.21%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 9（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 7（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C +3.7k / P -1.8k ｜ Activity HIGH ｜ 1D
11-27  C +0.6k / P +0.8k ｜ Activity HIGH ｜ 8D
12-04  C +92 / P +0.6k ｜ Activity HIGH ｜ 15D
12-11  C +3.9k / P +72 ｜ Activity HIGH ｜ 22D

📆 11-20 Forward Structure
存量OI: C 60.4k / P 25.6k，今日变化ΔOI: C +3.7k / P -1.8k，平值价格ATM: C $0.15 / P $0.29 ｜ ATM IV 145.6%，净 delta 敞口 286k shares
Top ΔOI: C 7 +905 ｜ P 8 -783
仓位参考: Max Pain 9 ｜ Call Wall 7（+1.9%，弱）（OI 1.5k） ｜ Put Wall 7（+1.9%，弱）（OI 3.0k）
量化解读： 存量 Call 重｜ATM IV 145.6%｜历史 Rank 79%（近端代理）｜IV/RV 1.27×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 286,474 股

📆 11-27 Forward Structure
存量OI: C 18.0k / P 4.0k，今日变化ΔOI: C +0.6k / P +0.8k，平值价格ATM: C $0.39 / P $0.53 ｜ ATM IV 105.5%，净 delta 敞口 -20k shares
Top ΔOI: P 8 +786 ｜ C 7 +341
仓位参考: Max Pain 8 ｜ Put Wall 7（+1.9%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 105.5%｜历史 Rank 79%（近端代理）｜IV/RV 0.92×（近似）｜净 delta 敞口 负 19,720 股

📆 12-04 Forward Structure
存量OI: C 3.6k / P 2.2k，今日变化ΔOI: C +92 / P +0.6k，平值价格ATM: C $0.53 / P $0.74 ｜ ATM IV 104.6%，净 delta 敞口 -18k shares
Top ΔOI: P 7 +423
仓位参考: Max Pain 8 ｜ Call Wall 7.5（+9.2%，弱）（OI 0.2k） ｜ Put Wall 7（+1.9%）（OI 0.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 104.6%｜历史 Rank 79%（近端代理）｜IV/RV 0.91×（近似）｜净 delta 敞口 负 18,290 股

📆 12-11 Forward Structure
存量OI: C 5.3k / P 1.2k，今日变化ΔOI: C +3.9k / P +72，平值价格ATM: C $0.67 / P $0.86 ｜ ATM IV 105.8%，净 delta 敞口 83k shares
仓位参考: Max Pain 8 ｜ Put Wall 7.5（+9.2%，弱）（OI 0.1k）
量化解读： 存量 Call 重｜ATM IV 105.8%｜历史 Rank 79%（近端代理）｜IV/RV 0.92×（近似）｜净 delta 敞口 正 83,006 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-19/USAR_evening.json