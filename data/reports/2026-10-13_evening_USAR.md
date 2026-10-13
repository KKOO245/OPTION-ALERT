# 期权晚报 2026-10-13（快照 16:40 ET）

📊 市场环境

SPY $778.01 ｜ QQQ $743.57
VIX 15.27 ↑0.4%（5D +1.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 44.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-13

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-13 10:00　【高】成屋销售　预测 3.95 ｜ 实际 3.99 ｜ 前值 3.93　✅ 今日已公布
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.6 ｜ 实际 待公布 ｜ 前值 3.4
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 待公布 ｜ 前值 2.4
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-06 11P ΔOI +133（距现价 -2.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 11.60 → 收盘 11.28（-2.8%） ｜ 今日高 11.64 ｜ 低 11.26 ｜ 昨收 11.82 → 收盘 11.28（-4.6%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-16，窗口结束前不做对错判定）

Options: P/C成交量 0.56 | OI比 0.30 | ATM IV 76.6% | Skew -3.2pp | Term 1.06 | ExpMove ±5.8%（近端） | Rank 10%
量化视角： IV 历史低位（Rank 10%，期权偏便宜）｜期限结构正常（Term 1.06）｜Put 保护异常便宜（Skew -3.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.30）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.56×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.30×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（3D）±5.8% ｜ 10-23（10D）±9.5% ｜ 10-30（17D）±12.4% ｜ 11-06（24D）±15.6%
   ⇒ IV–VIX Spread: +61.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,421,488 | GEX Change vs 上次快照 -392,138 | Flip: Primary Flip: 12.03（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 181 / LOW 93 / INVALID 100
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 12.03（全链重定价，覆盖 100%）
最近结构参考: Flip 12（现价低于该位 6.2%）
量化视角： 负 Gamma（142万，无历史分位）｜负 Gamma 加深（39万）｜现价位于 Flip 下方 6.22%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 15（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 12（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +2.9k / P -0.2k ｜ Activity HIGH ｜ 3D
10-23  C +1.1k / P -44 ｜ Activity HIGH ｜ 10D
10-30  C +0.2k / P +46 ｜ Activity MEDIUM △ ｜ 17D
11-06  C +0.3k / P +0.3k ｜ Activity MEDIUM △ ｜ 24D

📆 10-16 Forward Structure
存量OI: C 55.0k / P 16.3k，今日变化ΔOI: C +2.9k / P -0.2k，平值价格ATM: C $0.22 / P $0.43 ｜ ATM IV 76.6%，净 delta 敞口 87k shares
Top ΔOI: C 12 +455
仓位参考: Max Pain 15
量化解读： 存量 Call 重｜ATM IV 76.6%｜历史 Rank 10%（近端代理）｜IV/RV 1.43×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 87,168 股

📆 10-23 Forward Structure
存量OI: C 13.1k / P 5.0k，今日变化ΔOI: C +1.1k / P -44，平值价格ATM: C $0.44 / P $0.63 ｜ ATM IV 68.4%，净 delta 敞口 48k shares
Top ΔOI: C 12 +275 ｜ P 16 -270
仓位参考: Max Pain 14 ｜ Put Wall 12（+6.4%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 68.4%｜历史 Rank 10%（近端代理）｜IV/RV 1.28×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 48,054 股

10-30（MEDIUM △）Top ΔOI: 15P -392 ｜ 14P +207
10-30（MEDIUM △）仓位参考: Max Pain 14 ｜ Put Wall 12（+6.4%，弱）（OI 0.9k）

11-06（MEDIUM △）Top ΔOI: 16P -345 ｜ 11P +133
11-06（MEDIUM △）仓位参考: Max Pain 16 ｜ Put Wall 11（-2.5%，弱）（OI 0.2k）

📅 事件差分（观察，非因果）: 10-16（3D）ATM IV 76.6% vs 10-23 68.4%（差 +8.2pp）——覆盖 成屋销售、Core Inflation Rate MoM 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=50 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=50）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-13/USAR_evening.json