# 期权晚报 2026-11-11（快照 16:40 ET）

📊 市场环境

SPY $759.81 ｜ QQQ $690.38
VIX 17.49 ↓10.1%（5D +5.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 37.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-11

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-13 85P ΔOI +436（距现价 -0.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-16 84P ΔOI +435 占该期限总 OI 13.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 86.93 → 收盘 85.21（-2.0%） ｜ 今日高 86.92 ｜ 低 85.13 ｜ 昨收 86.49 → 收盘 85.21（-1.5%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-18，窗口结束前不做对错判定）

Options: P/C成交量 1.51 | OI比 0.63 | ATM IV 49.1% | Skew 21.2pp | Term 0.88 | ExpMove ±2.9%（近端） | Rank 79%
量化视角： IV 历史高位（Rank 79%，期权偏贵）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜保护溢价显著（Skew 21.2pp，Put 明显贵于 Call）｜⚠️ 重点观察：存量 Call 重（OI比 0.63）+ 当日成交偏 Put（P/C量 1.51）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.51×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.63×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（2D）±2.9% ｜ 11-16（5D）±4.0% ｜ 11-18（7D）±5.5% ｜ 11-20（9D）±5.5%
   ⇒ IV–VIX Spread: +31.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 15,171,307 | GEX Change vs 上次快照 -16,205,207 | Flip: Primary Flip: 84.52（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 621 / LOW 215 / INVALID 496
结构观察区: Primary Flip 84.52（全链重定价，覆盖 93%）
最近结构参考: Flip 85（现价高于该位 0.8%）
量化视角： 正 Gamma（1517万，无历史分位）｜正 Gamma 减弱（1621万）｜现价位于 Flip 上方 0.82%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 85（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 85（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +1.4k / P +2.2k ｜ Activity HIGH ｜ 2D
11-16  C +0.1k / P +0.8k ｜ Activity HIGH ｜ 5D
11-18  C +19 / P +55 ｜ Activity MEDIUM △ ｜ 7D
11-20  C +0.6k / P +2.2k ｜ Activity HIGH ｜ 9D

📆 11-13 Forward Structure
存量OI: C 83.3k / P 37.1k，今日变化ΔOI: C +1.4k / P +2.2k，平值价格ATM: C $1.45 / P $1.00 ｜ ATM IV 48.4%，净 delta 敞口 -70k shares
Top ΔOI: P 84 +457 ｜ P 85 +436
仓位参考: Max Pain 85 ｜ Call Wall 88（+3.3%，弱）（OI 13.5k） ｜ Put Wall 82（-3.8%，弱）（OI 4.9k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 48.4%｜历史 Rank 79%（近端代理）｜IV/RV 0.88×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 69,863 股

📆 11-16 Forward Structure
存量OI: C 1.9k / P 1.5k，今日变化ΔOI: C +0.1k / P +0.8k，平值价格ATM: C $2.10 / P $1.34 ｜ ATM IV 38.6%，净 delta 敞口 -19k shares
Top ΔOI: P 84 +435 ｜ P 77 +150
仓位参考: Max Pain 86 ｜ Call Wall 88（+3.3%，弱）（OI 0.2k） ｜ Put Wall 84（-1.4%）（OI 0.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 38.6%｜历史 Rank 79%（近端代理）｜IV/RV 0.70×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 19,178 股

11-18（MEDIUM △）Top ΔOI: 82P +30 ｜ 80P +19
11-18（MEDIUM △）仓位参考: Max Pain 85 ｜ Call Wall 87（+2.1%）（OI 98） ｜ Put Wall 84（-1.4%）（OI 0.2k）

📆 11-20 Forward Structure
存量OI: C 102.5k / P 168.5k，今日变化ΔOI: C +0.6k / P +2.2k，平值价格ATM: C $2.55 / P $2.17 ｜ ATM IV 44.8%，净 delta 敞口 -74k shares
Top ΔOI: P 85 +594 ｜ P 82 +521
仓位参考: Max Pain 87 ｜ Call Wall 90（+5.6%，弱）（OI 10.5k） ｜ Put Wall 80（-6.1%，弱）（OI 23.9k）
量化解读： 存量 Put 重｜ATM IV 44.8%｜历史 Rank 79%（近端代理）｜IV/RV 0.81×（近似）｜净 delta 敞口 负 73,893 股

📅 事件差分（观察，非因果）: 11-13（2D）ATM IV 48.4% vs 11-16 38.6%（差 +9.8pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-11/GDX_evening.json