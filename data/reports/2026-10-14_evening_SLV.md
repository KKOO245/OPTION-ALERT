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
🟡 **近现价集中开仓**: 10-16 52P ΔOI +574（距现价 +4.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-19 53C ΔOI +1,285 占该期限总 OI 13.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 51.31 → 收盘 50.22（-2.1%） ｜ 今日高 51.67 ｜ 低 50.01 ｜ 昨收 53.49 → 收盘 50.22（-6.1%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-19，窗口结束前不做对错判定）

Options: P/C成交量 0.64 | OI比 0.35 | ATM IV 66.4% | Skew -31.0pp | Term 0.56 | ExpMove ±2.8%（近端） | Rank 93%
量化视角： IV 历史高位（Rank 93%，期权偏贵）｜期限结构倒挂（Term 0.56，近月 IV 高于远月）｜Put 保护异常便宜（Skew -31.0pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.35）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.64×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.35×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（2D）±2.8% ｜ 10-19（5D）±3.4% ｜ 10-21（7D）±4.2% ｜ 10-23（9D）±4.8%
   ⇒ IV–VIX Spread: +49.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 6,277,727 | GEX Change vs 上次快照 6,741,045 | Flip: Primary Flip: 49.70（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 82%（带内） ｜ IV 有效性: VALID 694 / LOW 159 / INVALID 485
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 49.70（全链重定价，覆盖 82%）
Put Wall 50（弱结构｜现价高于该位 0.4%）
最近结构参考: Put Wall 50（现价高于该位 0.4%）
量化视角： 正 Gamma（628万，无历史分位）｜由负转正（+674万）｜现价位于 Flip 上方 1.04%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 50（Put Wall，弱结构）；上方 54（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 50（全链重定价，覆盖 82%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +3.6k / P +0.6k ｜ Activity MEDIUM △ ｜ 2D
10-19  C +2.3k / P +1.0k ｜ Activity HIGH ｜ 5D
10-21  C +2.0k / P +1.2k ｜ Activity HIGH ｜ 7D
10-23  C +7.0k / P +2.1k ｜ Activity HIGH ｜ 9D

📆 10-16 Forward Structure
存量OI: C 475.0k / P 196.5k，今日变化ΔOI: C +3.6k / P +0.6k，平值价格ATM: C $0.83 / P $0.57 ｜ ATM IV 47.0%，净 delta 敞口 153k shares
Top ΔOI: C 55 +1,038 ｜ C 54 +919 ｜ P 52 +574
仓位参考: Max Pain 56 ｜ Call Wall 50（-0.4%，弱）（OI 27.0k） ｜ Put Wall 50（-0.4%，弱）（OI 23.5k）
量化解读： 存量 Call 重｜ATM IV 47.0%｜历史 Rank 93%（近端代理）｜IV/RV 1.50×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 153,302 股

📆 10-19 Forward Structure
存量OI: C 5.9k / P 3.4k，今日变化ΔOI: C +2.3k / P +1.0k，平值价格ATM: C $0.97 / P $0.72 ｜ ATM IV 37.2%，净 delta 敞口 -66k shares
Top ΔOI: C 53 +1,285 ｜ C 54 +331 ｜ P 53 +325
仓位参考: Max Pain 53 ｜ Call Wall 53（+5.5%）（OI 1.4k） ｜ Put Wall 52.5（+4.5%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 37.2%｜历史 Rank 93%（近端代理）｜IV/RV 1.19×（近似）｜净 delta 敞口 负 66,284 股

📆 10-21 Forward Structure
存量OI: C 5.7k / P 2.6k，今日变化ΔOI: C +2.0k / P +1.2k，平值价格ATM: C $1.18 / P $0.92 ｜ ATM IV 37.8%，净 delta 敞口 -64k shares
Top ΔOI: P 50 +277 ｜ C 53 +242
仓位参考: Max Pain 54 ｜ Call Wall 53.5（+6.5%，弱）（OI 0.7k） ｜ Put Wall 50.5（+0.6%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 37.8%｜历史 Rank 93%（近端代理）｜IV/RV 1.20×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 64,382 股

📆 10-23 Forward Structure
存量OI: C 45.0k / P 35.1k，今日变化ΔOI: C +7.0k / P +2.1k，平值价格ATM: C $1.33 / P $1.08 ｜ ATM IV 37.5%，净 delta 敞口 37k shares
Top ΔOI: C 54 +800
仓位参考: Max Pain 57 ｜ Call Wall 55（+9.5%，弱）（OI 1.6k） ｜ Put Wall 55（+9.5%，弱）（OI 3.3k）
量化解读： 存量 Call 重｜ATM IV 37.5%｜历史 Rank 93%（近端代理）｜IV/RV 1.20×（近似）｜净 delta 敞口 正 36,754 股

📅 事件差分（观察，非因果）: 10-16（2D）ATM IV 47.0% vs 10-19 37.2%（差 +9.8pp）——覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY、Inflation Rate YoY、Inflation Rate MoM、PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-14/SLV_evening.json