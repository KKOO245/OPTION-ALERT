# 期权晚报 2026-09-30（快照 21:00 ET）

📊 市场环境

SPY $762.63 ｜ QQQ $nan
VIX 16.34 ↑1.9%（5D +7.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 30.8（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-30

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.2 ｜ 前值 0.1　✅ 今日已公布
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 2.2 ｜ 前值 2.5　✅ 今日已公布
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 0.9 ｜ 前值 0.1　✅ 今日已公布
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## SOXX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SOXX: 今开 568.81 → 收盘 568.64（-0.0%） ｜ 今日高 572.32 ｜ 低 564.01 ｜ 昨收 567.44 → 收盘 568.64（+0.2%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-07，窗口结束前不做对错判定）

Options: P/C成交量 5.46 | OI比 1.59 | ATM IV 45.5% | Skew 0.4pp | Term 0.81 | ExpMove ±2.3%（近端） | Rank 81%
量化视角： IV 历史高位（Rank 81%，期权偏贵）｜期限结构倒挂（Term 0.81，近月 IV 高于远月）｜保护溢价薄（Skew 0.4pp）｜当日成交偏 Put（P/C量 5.46）——观察点，非方向信号
   ⇒ Put/Call Volume: 5.46×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.59×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-02（2D）±2.3% ｜ 10-09（9D）±4.6% ｜ 10-16（16D）±6.3% ｜ 10-23（23D）±7.0%
   ⇒ IV–VIX Spread: +29.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 8,989,672 | GEX Change vs 上次快照 915,330 | Flip: Primary Flip: 558.62（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 480 / LOW 326 / INVALID 746
结构观察区: Primary Flip 558.62（全链重定价，覆盖 91%）
Call Wall 600（现价低于该位 5.2%）
最近结构参考: Flip 559（现价高于该位 1.8%）
量化视角： 正 Gamma（899万，无历史分位）｜正 Gamma 增强（+92万）｜现价位于 Flip 上方 1.79%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 542（MaxPain，仅结算参考）；上方 600（Call Wall）。
• Gamma 区域：切换参考 559（全链重定价，覆盖 91%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C +0 / P +0 ｜ Activity LOW ｜ 2D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 9D
10-16  C +0 / P +0 ｜ Activity LOW ｜ 16D
10-23  C +0 / P +0 ｜ Activity LOW ｜ 23D

📆 10-02 Forward Structure
存量OI: C 16.5k / P 26.3k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $7.00 / P $6.20 ｜ ATM IV 45.5%，净 delta 敞口 0 shares
仓位参考: Max Pain 542 ｜ Call Wall 542.5（-4.6%，弱）（OI 2.8k）
量化解读： 存量 Put 重｜ATM IV 45.5%｜历史 Rank 81%（近端代理）｜IV/RV 1.25×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-09（Activity LOW）仓位参考: Max Pain 525 ｜ Call Wall 537.5（-5.5%，弱）（OI 0.4k） ｜ Put Wall 555（-2.4%，弱）（OI 0.2k）

10-16（Activity LOW）仓位参考: Max Pain 530 ｜ Call Wall 600（+5.5%）（OI 9.4k）

10-23（Activity LOW）仓位参考: Max Pain 528 ｜ Call Wall 570（+0.2%，弱）（OI 95）

📅 事件差分（观察，非因果）: 10-02（2D）ATM IV 45.5% vs 10-09 36.7%（差 +8.7pp）——覆盖 PCE 物价 Price Index MoM、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-30/SOXX_evening.json