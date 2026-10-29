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
🔴 **事件差分**: 10-30（1D）ATM IV 59.1% vs 11-06 43.9%（差 +15.2pp），覆盖 GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM、PCE 物价 Price Index MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-30 535C ΔOI +1,742（距现价 +4.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SOXX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SOXX: 今开 512.03 → 收盘 513.86（+0.4%） ｜ 今日高 518.74 ｜ 低 506.62 ｜ 昨收 521.94 → 收盘 513.86（-1.5%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-05，窗口结束前不做对错判定）

Options: P/C成交量 2.94 | OI比 6.19 | ATM IV 59.1% | Skew -2.2pp | Term 0.71 | ExpMove ±2.2%（近端） | Rank 93%
量化视角： IV 历史高位（Rank 93%，期权偏贵）｜期限结构倒挂（Term 0.71，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.2pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 2.94）——观察点，非方向信号
   ⇒ Put/Call Volume: 2.94×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 6.19×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-30（1D）±2.2% ｜ 11-06（8D）±4.8% ｜ 11-13（15D）±6.7% ｜ 11-20（22D）±8.8%
   ⇒ IV–VIX Spread: +41.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 13,245,353 | GEX Change vs 上次快照 5,916,608 | Flip: Primary Flip: 507.43（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 89%（带内） ｜ IV 有效性: VALID 516 / LOW 363 / INVALID 713
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 507.43（全链重定价，覆盖 89%）
最近结构参考: Flip 507（现价高于该位 1.3%）
量化视角： 正 Gamma（1325万，无历史分位）｜正 Gamma 增强（+592万）｜现价位于 Flip 上方 1.27%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 515（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 507（全链重定价，覆盖 89%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-30  C +2.8k / P +17.0k ｜ Activity HIGH ｜ 1D
11-06  C +15.0k / P +1.6k ｜ Activity HIGH ｜ 8D
11-13  C -0.6k / P +36 ｜ Activity MEDIUM △ ｜ 15D
11-20  C -1.0k / P -1.5k ｜ Activity HIGH ｜ 22D

📆 10-30 Forward Structure
存量OI: C 31.0k / P 191.8k，今日变化ΔOI: C +2.8k / P +17.0k，平值价格ATM: C $5.00 / P $6.20 ｜ ATM IV 59.1%，净 delta 敞口 -86k shares
Top ΔOI: P 480 +9,597 ｜ P 470 +9,012 ｜ C 535 +1,742
仓位参考: Max Pain 515 ｜ Call Wall 500（-2.7%，弱）（OI 2.8k）
量化解读： 存量 Put 重｜ATM IV 59.1%｜历史 Rank 93%（近端代理）｜IV/RV 1.41×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 86,080 股

📆 11-06 Forward Structure
存量OI: C 37.9k / P 10.2k，今日变化ΔOI: C +15.0k / P +1.6k，平值价格ATM: C $11.53 / P $13.40 ｜ ATM IV 43.9%，净 delta 敞口 37k shares
Top ΔOI: C 550 +7,514 ｜ C 540 +7,475 ｜ P 497 +802
仓位参考: Max Pain 505 ｜ Call Wall 540（+5.1%，弱）（OI 14.1k） ｜ Put Wall 500（-2.7%，弱）（OI 1.0k）
量化解读： 存量 Call 重｜ATM IV 43.9%｜历史 Rank 93%（近端代理）｜IV/RV 1.04×（近似）｜净 delta 敞口 正 37,233 股

11-13（MEDIUM △）Top ΔOI: 520C -360 ｜ 500C -85
11-13（MEDIUM △）仓位参考: Max Pain 510 ｜ Call Wall 510（-0.8%，弱）（OI 9.6k）

📆 11-20 Forward Structure
存量OI: C 39.4k / P 63.1k，今日变化ΔOI: C -1.0k / P -1.5k，平值价格ATM: C $21.18 / P $23.89 ｜ ATM IV 44.1%，净 delta 敞口 -15k shares
Top ΔOI: P 430 -1,107 ｜ C 555 -629 ｜ P 475 +609
仓位参考: Max Pain 535 ｜ Call Wall 505（-1.7%，弱）（OI 2.7k） ｜ Put Wall 490（-4.6%，弱）（OI 3.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 44.1%｜历史 Rank 93%（近端代理）｜IV/RV 1.05×（近似）｜净 delta 敞口 负 14,569 股

📅 事件差分（观察，非因果）: 10-30（1D）ATM IV 59.1% vs 11-06 43.9%（差 +15.2pp）——覆盖 GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM、PCE 物价 Price Index MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-29/SOXX_evening.json