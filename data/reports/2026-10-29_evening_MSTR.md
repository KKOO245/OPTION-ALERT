# 期权晚报 2026-10-29（快照 21:00 ET）

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
🔴 **事件差分**: 10-30（1D）ATM IV 112.7% vs 11-06 78.3%（差 +34.4pp），覆盖 GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM、PCE 物价 Price Index MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 141.42 → 收盘 141.62（+0.1%） ｜ 今日高 144.76 ｜ 低 138.88 ｜ 昨收 145.16 → 收盘 141.62（-2.4%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-05，窗口结束前不做对错判定）

Options: P/C成交量 0.65 | OI比 0.66 | ATM IV 112.7% | Skew -3.2pp | Term 0.61 | ExpMove ±4.8%（近端） | Rank 88%
量化视角： IV 历史高位（Rank 88%，期权偏贵）｜期限结构倒挂（Term 0.61，近月 IV 高于远月）｜Put 保护异常便宜（Skew -3.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.66）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.65×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.66×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（1D）±4.8% ｜ 11-06（8D）±9.4% ｜ 11-13（15D）±11.7% ｜ 11-20（22D）±14.1%
   ⇒ IV–VIX Spread: +95.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 31,018,489 | GEX Change vs 上次快照 1,691,927 | Flip: Primary Flip: 136.57（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 610 / LOW 98 / INVALID 208
结构观察区: Primary Flip 136.57（全链重定价，覆盖 99%）
Call Wall 135（弱结构｜现价高于该位 4.9%）
最近结构参考: Flip 137（现价高于该位 3.7%）
量化视角： 正 Gamma（3102万，无历史分位）｜正 Gamma 增强（+169万）｜现价位于 Flip 上方 3.70%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 135（Call Wall，弱结构）；上方 142（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 137（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-30  C +0 / P +0 ｜ Activity LOW ｜ 1D
11-06  C +0 / P +0 ｜ Activity LOW ｜ 8D
11-13  C +0 / P +0 ｜ Activity LOW ｜ 15D
11-20  C +0 / P +0 ｜ Activity LOW ｜ 22D

📆 10-30 Forward Structure
存量OI: C 248.6k / P 165.1k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $3.20 / P $3.55 ｜ ATM IV 112.7%，净 delta 敞口 0 shares
仓位参考: Max Pain 142 ｜ Call Wall 152.5（+7.7%，弱）（OI 38.8k）
量化解读： 存量 Call 重｜ATM IV 112.7%｜历史 Rank 88%（近端代理）｜IV/RV 1.69×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-06（Activity LOW）仓位参考: Max Pain 155 ｜ Call Wall 150（+5.9%，弱）（OI 2.7k） ｜ Put Wall 155（+9.4%，弱）（OI 3.6k）

11-13（Activity LOW）仓位参考: Max Pain 160 ｜ Put Wall 155（+9.4%，弱）（OI 2.4k）

11-20（Activity LOW）仓位参考: Max Pain 135 ｜ Call Wall 135（-4.7%）（OI 42.4k） ｜ Put Wall 130（-8.2%，弱）（OI 4.5k）

📅 事件差分（观察，非因果）: 10-30（1D）ATM IV 112.7% vs 11-06 78.3%（差 +34.4pp）——覆盖 GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM、PCE 物价 Price Index MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-29/MSTR_evening.json