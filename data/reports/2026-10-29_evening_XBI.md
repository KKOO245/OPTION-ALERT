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
🟡 **事件差分**: 10-30 ATM IV 44.1% vs 11-06 32.9%（差 +11.2pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-30 155P ΔOI +2,192（距现价 -1.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-06 151P ΔOI +1,348 占该期限总 OI 17.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## XBI

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
XBI: 今开 157.64 → 收盘 157.79（+0.1%） ｜ 今日高 160.27 ｜ 低 156.43 ｜ 昨收 157.51 → 收盘 157.79（+0.2%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-05，窗口结束前不做对错判定）

Options: P/C成交量 4.80 | OI比 5.24 | ATM IV 44.1% | Skew 6.3pp | Term 0.73 | ExpMove ±2.0%（近端） | Rank 92%
量化视角： IV 历史高位（Rank 92%，期权偏贵）｜期限结构倒挂（Term 0.73，近月 IV 高于远月）｜保护溢价显著（Skew 6.3pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 4.80）——观察点，非方向信号
   ⇒ Put/Call Volume: 4.80×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 5.24×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-30（1D）±2.0% ｜ 11-06（8D）±4.1% ｜ 11-13（15D）±2.2% ｜ 11-20（22D）±6.3%
   ⇒ IV–VIX Spread: +26.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) -3,302,476 | GEX Change vs 上次快照 -4,437,208 | Flip: Candidates 158.38 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 77%（带内） ｜ IV 有效性: VALID 323 / LOW 93 / INVALID 358
结构观察区: ≈158（全链重定价，覆盖 77%，CONDITIONAL）
Call Wall 165（现价低于该位 4.4%）
最近结构参考: Flip 158（现价低于该位 0.4%）
量化视角： 负 Gamma（330万，无历史分位）｜由正转负（444万）｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 154（MaxPain，仅结算参考）；上方 165（Call Wall）。
• Gamma 区域：切换参考 158（全链重定价，覆盖 77%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-30  C +0.9k / P -0.8k ｜ Activity HIGH ｜ 1D
11-06  C +0.5k / P +1.5k ｜ Activity HIGH ｜ 8D
11-13  C +39 / P -0.3k ｜ Activity MEDIUM △ ｜ 15D
11-20  C +0.8k / P -3.1k ｜ Activity HIGH ｜ 22D

📆 10-30 Forward Structure
存量OI: C 12.1k / P 63.6k，今日变化ΔOI: C +0.9k / P -0.8k，平值价格ATM: C $1.42 / P $1.78 ｜ ATM IV 44.1%，净 delta 敞口 -40k shares
Top ΔOI: P 155 +2,192 ｜ P 152 -2,137 ｜ P 148 -1,004
仓位参考: Max Pain 154 ｜ Call Wall 155（-1.8%，弱）（OI 2.2k） ｜ Put Wall 150（-4.9%，弱）（OI 9.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 44.1%｜历史 Rank 92%（近端代理）｜IV/RV 1.32×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 39,868 股

📆 11-06 Forward Structure
存量OI: C 2.5k / P 5.2k，今日变化ΔOI: C +0.5k / P +1.5k，平值价格ATM: C $3.20 / P $3.28 ｜ ATM IV 32.9%，净 delta 敞口 -12k shares
Top ΔOI: P 151 +1,348 ｜ C 160 +74 ｜ C 163 +53
仓位参考: Max Pain 153 ｜ Call Wall 156（-1.1%，弱）（OI 0.3k） ｜ Put Wall 151（-4.3%）（OI 1.9k）
量化解读： 存量 Put 重｜ATM IV 32.9%｜历史 Rank 92%（近端代理）｜IV/RV 0.99×（近似）｜净 delta 敞口 负 12,029 股

11-13（MEDIUM △）Top ΔOI: 153P -203 ｜ 143P -185
11-13（MEDIUM △）仓位参考: Max Pain 150 ｜ Call Wall 160（+1.4%）（OI 0.4k） ｜ Put Wall 148（-6.2%，弱）（OI 0.2k）

📆 11-20 Forward Structure
存量OI: C 20.8k / P 36.4k，今日变化ΔOI: C +0.8k / P -3.1k，平值价格ATM: C $4.90 / P $4.99 ｜ ATM IV 33.4%，净 delta 敞口 49k shares
Top ΔOI: P 145 -1,730
仓位参考: Max Pain 154 ｜ Call Wall 165（+4.6%）（OI 7.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 33.4%｜历史 Rank 92%（近端代理）｜IV/RV 1.00×（近似）｜净 delta 敞口 正 48,619 股

📅 事件差分（观察，非因果）: 10-30（1D）ATM IV 44.1% vs 11-06 32.9%（差 +11.2pp）——覆盖 GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM、PCE 物价 Price Index MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-29/XBI_evening.json