# 期权晚报 2026-10-14（快照 16:42 ET）

📊 市场环境

SPY $769.60 ｜ QQQ $728.95
VIX 16.87 ↑10.5%（5D +11.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 32.4（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-14

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 2.6 ｜ 前值 2.4　✅ 今日已公布
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.6 ｜ 实际 3.7 ｜ 前值 3.4　✅ 今日已公布
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 0.6 ｜ 前值 0.4　✅ 今日已公布
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览
🔴 **事件差分**: 10-16（2D）ATM IV 91.6% vs 10-23 76.2%（差 +15.4pp），覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY、Inflation Rate YoY、Inflation Rate MoM、PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔵 **期限 OI 集中**: 11-06 18C ΔOI +999 占该期限总 OI 12.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 10.89 → 收盘 10.32（-5.2%） ｜ 今日高 11.07 ｜ 低 10.15 ｜ 昨收 11.28 → 收盘 10.32（-8.5%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-19，窗口结束前不做对错判定）

Options: P/C成交量 0.39 | OI比 0.25 | ATM IV 91.6% | Skew 8.9pp | Term 0.87 | ExpMove ±6.3%（近端） | Rank 22%
量化视角： IV 历史低位（Rank 22%，期权偏便宜）｜期限结构倒挂（Term 0.87，近月 IV 高于远月）｜保护溢价显著（Skew 8.9pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.25）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.39×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.25×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（2D）±6.3% ｜ 10-23（9D）±9.8% ｜ 10-30（16D）±13.9% ｜ 11-06（23D）±16.4%
   ⇒ IV–VIX Spread: +74.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,526,649 | GEX Change vs 上次快照 -1,579,921 | Flip: Primary Flip: 11.33（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 194 / LOW 95 / INVALID 89
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 11.33（全链重定价，覆盖 100%）
最近结构参考: Flip 11（现价低于该位 8.9%）
量化视角： 负 Gamma（153万，无历史分位）｜由正转负（158万）｜现价位于 Flip 下方 8.94%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 14（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 11（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +1.6k / P -2.2k ｜ Activity HIGH ｜ 2D
10-23  C +0.8k / P -0.1k ｜ Activity HIGH ｜ 9D
10-30  C +0.6k / P +60 ｜ Activity HIGH ｜ 16D
11-06  C +1.3k / P +1.2k ｜ Activity HIGH ｜ 23D

📆 10-16 Forward Structure
存量OI: C 56.6k / P 14.1k，今日变化ΔOI: C +1.6k / P -2.2k，平值价格ATM: C $0.19 / P $0.46 ｜ ATM IV 91.6%，净 delta 敞口 254k shares
Top ΔOI: P 15 -746 ｜ P 14 -528 ｜ P 13 -508
仓位参考: Max Pain 14
量化解读： 存量 Call 重｜ATM IV 91.6%｜历史 Rank 22%（近端代理）｜IV/RV 2.32×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 253,677 股

📆 10-23 Forward Structure
存量OI: C 14.0k / P 4.9k，今日变化ΔOI: C +0.8k / P -0.1k，平值价格ATM: C $0.40 / P $0.61 ｜ ATM IV 76.2%，净 delta 敞口 43k shares
Top ΔOI: P 15 -172
仓位参考: Max Pain 14 ｜ Put Wall 10（-3.1%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 76.2%｜历史 Rank 22%（近端代理）｜IV/RV 1.93×（近似）｜净 delta 敞口 正 43,405 股

📆 10-30 Forward Structure
存量OI: C 8.0k / P 8.8k，今日变化ΔOI: C +0.6k / P +60，平值价格ATM: C $0.60 / P $0.83 ｜ ATM IV 78.5%，净 delta 敞口 22k shares
Top ΔOI: P 13 -354 ｜ P 10 +258
仓位参考: Max Pain 14
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 78.5%｜历史 Rank 22%（近端代理）｜IV/RV 1.99×（近似）｜净 delta 敞口 正 21,924 股

📆 11-06 Forward Structure
存量OI: C 3.4k / P 4.8k，今日变化ΔOI: C +1.3k / P +1.2k，平值价格ATM: C $0.98 / P $0.71 ｜ ATM IV 79.4%，净 delta 敞口 -22k shares
Top ΔOI: P 11 +201
仓位参考: Max Pain 15 ｜ Put Wall 10（-3.1%，弱）（OI 0.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 79.4%｜历史 Rank 22%（近端代理）｜IV/RV 2.01×（近似）｜净 delta 敞口 负 22,461 股

📅 事件差分（观察，非因果）: 10-16（2D）ATM IV 91.6% vs 10-23 76.2%（差 +15.4pp）——覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY、Inflation Rate YoY、Inflation Rate MoM、PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-14/USAR_evening.json