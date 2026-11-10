# 期权晚报 2026-11-10（快照 16:40 ET）

📊 市场环境

SPY $749.92 ｜ QQQ $674.76
VIX 19.46 ↓2.3%（5D -6.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-10

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-10 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周二 11-10 08:30　【高】Inflation Rate MoM　预测 0.3 ｜ 实际 0.4 ｜ 前值 0.6　✅ 今日已公布
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **事件差分**: 11-13 ATM IV 94.5% vs 11-20 83.6%（差 +10.9pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-27 120P ΔOI -858（距现价 -0.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 121.95 → 收盘 121.07（-0.7%） ｜ 今日高 126.40 ｜ 低 118.43 ｜ 昨收 125.59 → 收盘 121.07（-3.6%）
Target 等待验证: 3D_mdd >= 0.03（3D） — PENDING（评估日 ≈ 2026-11-13，窗口结束前不做对错判定）

Options: P/C成交量 0.80 | OI比 0.63 | ATM IV 94.5% | Skew 3.4pp | Term 0.82 | ExpMove ±6.9%（近端） | Rank 73%
量化视角： IV 中性（Rank 73%）｜期限结构倒挂（Term 0.82，近月 IV 高于远月）｜保护溢价中性（Skew 3.4pp）｜存量 Call 偏重（OI比 0.63）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.80×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.63×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（3D）±6.9% ｜ 11-20（10D）±11.0% ｜ 11-27（17D）±13.2% ｜ 12-04（24D）±15.5%
   ⇒ IV–VIX Spread: +75.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 12,790,784 | GEX Change vs 上次快照 -23,935,431 | Flip: Primary Flip: 118.87（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 527 / LOW 175 / INVALID 280
结构观察区: Primary Flip 118.87（全链重定价，覆盖 100%）
最近结构参考: Flip 119（现价高于该位 1.9%）
量化视角： 正 Gamma（1279万，无历史分位）｜正 Gamma 减弱（2394万）｜现价位于 Flip 上方 1.85%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 130（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 119（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +16.5k / P -0.4k ｜ Activity HIGH ｜ 3D
11-20  C +3.3k / P +2.7k ｜ Activity MEDIUM △ ｜ 10D
11-27  C +1.2k / P +2.3k ｜ Activity HIGH ｜ 17D
12-04  C +1.0k / P +3.6k ｜ Activity HIGH ｜ 24D

📆 11-13 Forward Structure
存量OI: C 230.3k / P 145.1k，今日变化ΔOI: C +16.5k / P -0.4k，平值价格ATM: C $4.20 / P $4.15 ｜ ATM IV 94.5%，净 delta 敞口 610k shares
Top ΔOI: C 135 +3,378 ｜ C 130 +1,615
仓位参考: Max Pain 130 ｜ Call Wall 133（+9.9%，弱）（OI 44.6k）
量化解读： 存量 Call 重｜ATM IV 94.5%｜历史 Rank 73%（近端代理）｜IV/RV 1.43×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 610,292 股

11-20（MEDIUM △）Top ΔOI: 137C +576
11-20（MEDIUM △）仓位参考: Max Pain 135 ｜ Put Wall 110（-9.1%，弱）（OI 14.7k）

📆 11-27 Forward Structure
存量OI: C 15.6k / P 39.3k，今日变化ΔOI: C +1.2k / P +2.3k，平值价格ATM: C $8.25 / P $7.78 ｜ ATM IV 77.6%，净 delta 敞口 -17k shares
Top ΔOI: P 120 -858 ｜ P 90 +670 ｜ P 95 +649
仓位参考: Max Pain 152 ｜ Call Wall 130（+7.4%，弱）（OI 0.8k） ｜ Put Wall 115（-5.0%，弱）（OI 2.1k）
量化解读： 存量 Put 重｜ATM IV 77.6%｜历史 Rank 73%（近端代理）｜IV/RV 1.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 16,822 股

📆 12-04 Forward Structure
存量OI: C 15.6k / P 22.9k，今日变化ΔOI: C +1.0k / P +3.6k，平值价格ATM: C $10.01 / P $8.75 ｜ ATM IV 77.6%，净 delta 敞口 -105k shares
Top ΔOI: P 85 +847 ｜ C 135 +462 ｜ P 90 +447
仓位参考: Max Pain 150 ｜ Put Wall 130（+7.4%，弱）（OI 1.2k）
量化解读： 存量 Put 重｜ATM IV 77.6%｜历史 Rank 73%（近端代理）｜IV/RV 1.17×（近似）｜净 delta 敞口 负 105,045 股

📅 事件差分（观察，非因果）: 11-13（3D）ATM IV 94.5% vs 11-20 83.6%（差 +10.9pp）——覆盖 Core Inflation Rate MoM、Inflation Rate MoM 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-10/MSTR_evening.json