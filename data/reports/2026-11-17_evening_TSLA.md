# 期权晚报 2026-11-17（快照 21:00 ET）

📊 市场环境

SPY $732.44 ｜ QQQ $nan
VIX 25.46 ↑11.1%（5D +30.8%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 25.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-17

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-17 08:30　【高】零售销售 MoM　预测 0.2 ｜ 实际 0.2 ｜ 前值 0.8　✅ 今日已公布
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 待公布 ｜ 前值 1.221
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 待公布 ｜ 前值 1.4

🔍 重点速览
🔴 **事件差分**: 11-18（1D）ATM IV 66.9% vs 11-20 9.6%（差 +57.2pp），覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Vol Regime 升档**: ELEVATED → STRESS（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 382.28 → 收盘 380.11（-0.6%） ｜ 今日高 382.84 ｜ 低 374.15 ｜ 昨收 379.74 → 收盘 380.11（+0.1%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-24，窗口结束前不做对错判定）

Options: P/C成交量 0.86 | OI比 0.95 | ATM IV 66.9% | Skew 9.4pp | Term 0.53 | ExpMove ±2.8%（近端） | Rank 80%
量化视角： IV 历史高位（Rank 80%，期权偏贵）｜期限结构倒挂（Term 0.53，近月 IV 高于远月）｜保护溢价显著（Skew 9.4pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.86×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.95×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-18（1D）±2.8% ｜ 11-20（3D）±0.1% ｜ 11-23（6D）±5.6% ｜ 11-25（8D）±6.6%
   ⇒ IV–VIX Spread: +41.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 29,143,157 | GEX Change vs 上次快照 -13,178,801 | Flip: Primary Flip: 373.83（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1280 / LOW 271 / INVALID 995
结构观察区: Primary Flip 373.83（全链重定价，覆盖 99%）
Call Wall 400（弱结构｜现价低于该位 5.0%）
最近结构参考: Flip 374（现价高于该位 1.7%）
量化视角： 正 Gamma（2914万，无历史分位）｜正 Gamma 减弱（1318万）｜现价位于 Flip 上方 1.68%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 382（MaxPain，仅结算参考） / 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 374（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-18  C +0 / P +0 ｜ Activity LOW ｜ 1D
11-20  C +0 / P +0 ｜ Activity LOW ｜ 3D
11-23  C +0 / P +0 ｜ Activity LOW ｜ 6D
11-25  C +0 / P +0 ｜ Activity LOW ｜ 8D

📆 11-18 Forward Structure
存量OI: C 41.1k / P 39.1k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $5.45 / P $5.35 ｜ ATM IV 66.9%，净 delta 敞口 0 shares
仓位参考: Max Pain 382 ｜ Call Wall 410（+7.9%，弱）（OI 4.7k） ｜ Put Wall 392.5（+3.3%，弱）（OI 2.5k）
量化解读： 存量两侧均衡｜ATM IV 66.9%｜历史 Rank 80%（近端代理）｜IV/RV 1.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-20（Activity LOW）仓位参考: Max Pain 375 ｜ Call Wall 400（+5.2%，弱）（OI 27.1k）

11-23（Activity LOW）仓位参考: Max Pain 385 ｜ Put Wall 360（-5.3%，弱）（OI 0.4k）

11-25（Activity LOW）仓位参考: Max Pain 382 ｜ Call Wall 400（+5.2%，弱）（OI 0.2k） ｜ Put Wall 345（-9.2%，弱）（OI 0.2k）

📅 事件差分（观察，非因果）: 11-18（1D）ATM IV 66.9% vs 11-20 9.6%（差 +57.2pp）——覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-17/TSLA_evening.json