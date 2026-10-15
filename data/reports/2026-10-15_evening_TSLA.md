# 期权晚报 2026-10-15（快照 16:40 ET）

📊 市场环境

SPY $771.79 ｜ QQQ $728.00
VIX 16.46 ↓2.4%（5D +6.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-15

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 1.3 ｜ 前值 0.5　✅ 今日已公布
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 0.8 ｜ 前值 1.3　✅ 今日已公布
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布　⏰ 今日

🔍 重点速览
🔴 **事件差分**: 10-16（1D）ATM IV 69.1% vs 10-19 42.6%（差 +26.5pp），覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-16 365P ΔOI +3,782（距现价 +0.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 360.58 → 收盘 362.44（+0.5%） ｜ 今日高 363.75 ｜ 低 355.23 ｜ 昨收 367.16 → 收盘 362.44（-1.3%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-22，窗口结束前不做对错判定）

Options: P/C成交量 0.65 | OI比 0.95 | ATM IV 69.1% | Skew -1.4pp | Term 0.66 | ExpMove ±2.9%（近端） | Rank 83%
量化视角： IV 历史高位（Rank 83%，期权偏贵）｜期限结构倒挂（Term 0.66，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.4pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.65×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.95×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（1D）±2.9% ｜ 10-19（4D）±3.5% ｜ 10-23（8D）±7.5% ｜ 10-26（11D）±7.9%
   ⇒ IV–VIX Spread: +52.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 8,456,742 | GEX Change vs 上次快照 40,650,335 | Flip: Primary Flip: 360.97（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 1220 / LOW 116 / INVALID 522
结构观察区: Primary Flip 360.97（全链重定价，覆盖 98%）
最近结构参考: Flip 361（现价高于该位 0.4%）
量化视角： 正 Gamma（846万，无历史分位）｜由负转正（+4065万）｜现价位于 Flip 上方 0.41%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 370（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 361（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +32.6k / P +12.3k ｜ Activity HIGH ｜ 1D
10-19  C +11.9k / P +14.7k ｜ Activity HIGH ｜ 4D
10-23  C +11.4k / P +5.5k ｜ Activity HIGH ｜ 8D
10-26  C +1.0k / P +1.1k ｜ Activity HIGH ｜ 11D

📆 10-16 Forward Structure
存量OI: C 436.7k / P 414.7k，今日变化ΔOI: C +32.6k / P +12.3k，平值价格ATM: C $5.25 / P $5.25 ｜ ATM IV 69.1%，净 delta 敞口 -2k shares
Top ΔOI: P 365 +3,782
仓位参考: Max Pain 370 ｜ Call Wall 380（+4.8%，弱）（OI 18.3k） ｜ Put Wall 380（+4.8%，弱）（OI 15.2k）
量化解读： 存量两侧均衡｜ATM IV 69.1%｜历史 Rank 83%（近端代理）｜IV/RV 2.46×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,934 股

📆 10-19 Forward Structure
存量OI: C 38.9k / P 25.3k，今日变化ΔOI: C +11.9k / P +14.7k，平值价格ATM: C $6.50 / P $6.32 ｜ ATM IV 42.6%，净 delta 敞口 84k shares
Top ΔOI: C 367 +1,587
仓位参考: Max Pain 370 ｜ Call Wall 390（+7.6%，弱）（OI 2.4k） ｜ Put Wall 365（+0.7%，弱）（OI 1.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 42.6%｜历史 Rank 83%（近端代理）｜IV/RV 1.52×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 84,430 股

📆 10-23 Forward Structure
存量OI: C 84.4k / P 55.5k，今日变化ΔOI: C +11.4k / P +5.5k，平值价格ATM: C $13.80 / P $13.31 ｜ ATM IV 63.0%，净 delta 敞口 86k shares
Top ΔOI: C 395 +1,890 ｜ C 450 +1,111 ｜ P 365 +988
仓位参考: Max Pain 370 ｜ Call Wall 390（+7.6%，弱）（OI 5.8k） ｜ Put Wall 360（-0.7%，弱）（OI 3.2k）
量化解读： 存量 Call 重｜ATM IV 63.0%｜历史 Rank 83%（近端代理）｜IV/RV 2.25×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 85,618 股

📆 10-26 Forward Structure
存量OI: C 2.7k / P 3.9k，今日变化ΔOI: C +1.0k / P +1.1k，平值价格ATM: C $14.65 / P $13.90 ｜ ATM IV 56.4%，净 delta 敞口 -7k shares
Top ΔOI: P 367 +370 ｜ C 360 +203
仓位参考: Max Pain 368 ｜ Call Wall 380（+4.8%，弱）（OI 0.4k） ｜ Put Wall 367.5（+1.4%，弱）（OI 0.4k）
量化解读： 存量 Put 重｜ATM IV 56.4%｜历史 Rank 83%（近端代理）｜IV/RV 2.01×（近似）｜净 delta 敞口 负 6,801 股

📅 事件差分（观察，非因果）: 10-16（1D）ATM IV 69.1% vs 10-19 42.6%（差 +26.5pp）——覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-15/TSLA_evening.json