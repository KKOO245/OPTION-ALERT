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
🟡 **事件差分**: 10-16 ATM IV 86.0% vs 10-23 74.9%（差 +11.1pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-30 13C ΔOI +13（距现价 +3.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 13.91 → 收盘 13.01（-6.5%） ｜ 今日高 13.99 ｜ 低 12.73 ｜ 昨收 14.35 → 收盘 13.01（-9.3%）
Target 等待验证: 3D_mdd >= 0.03（3D） — PENDING（评估日 ≈ 2026-10-19，窗口结束前不做对错判定）

Options: P/C成交量 0.92 | OI比 0.20 | ATM IV 86.0% | Skew -9.8pp | Term 0.87 | ExpMove ±5.6%（近端） | Rank 18%
量化视角： IV 历史低位（Rank 18%，期权偏便宜）｜期限结构倒挂（Term 0.87，近月 IV 高于远月）｜Put 保护异常便宜（Skew -9.8pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.20）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.92×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.20×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（2D）±5.6% ｜ 10-23（9D）±8.5% ｜ 10-30（16D）±11.8% ｜ 11-06（23D）±26.6%
   ⇒ IV–VIX Spread: +69.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 790,241 | GEX Change vs 上次快照 1,008,951 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 87%（带内） ｜ IV 有效性: VALID 100 / LOW 114 / INVALID 190
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: NO_CROSS
Put Wall 14（弱结构｜现价低于该位 7.1%）
最近结构参考: Put Wall 14（现价低于该位 7.1%）
量化视角： 正 Gamma（79万，无历史分位）｜由负转正（+101万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 14（Put Wall，弱结构） / 17（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +0.3k / P +34 ｜ Activity MEDIUM △ ｜ 2D
10-23  C +58 / P +48 ｜ Activity MEDIUM △ ｜ 9D
10-30  C +51 / P +7 ｜ Activity MEDIUM △ ｜ 16D
11-06  C +29 / P +17 ｜ Activity MEDIUM △ ｜ 23D

📆 10-16 Forward Structure
存量OI: C 22.7k / P 4.6k，今日变化ΔOI: C +0.3k / P +34，平值价格ATM: C $0.35 / P $0.38 ｜ ATM IV 86.0%，净 delta 敞口 4k shares
Top ΔOI: C 14 +71
仓位参考: Max Pain 17 ｜ Put Wall 14（+7.6%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 86.0%｜历史 Rank 18%（近端代理）｜IV/RV 1.98×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 3,901 股

10-23（MEDIUM △）仓位参考: Max Pain 16 ｜ Put Wall 14（+7.6%）（OI 0.6k）

10-30（MEDIUM △）Top ΔOI: 13C +13
10-30（MEDIUM △）仓位参考: Max Pain 16 ｜ Put Wall 14（+7.6%）（OI 0.3k）

11-06（MEDIUM △）Top ΔOI: 13P +14
11-06（MEDIUM △）仓位参考: Max Pain 16 ｜ Put Wall 13（-0.1%，弱）（OI 24）

📅 事件差分（观察，非因果）: 10-16（2D）ATM IV 86.0% vs 10-23 74.9%（差 +11.1pp）——覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY、Inflation Rate YoY、Inflation Rate MoM、PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime DOWN | Location ? | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-14/NNE_evening.json