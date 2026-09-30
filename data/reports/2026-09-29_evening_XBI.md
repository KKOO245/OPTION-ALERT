# 期权晚报 2026-09-29（快照 21:00 ET）

📊 市场环境

SPY $764.20 ｜ QQQ $nan
VIX 16.04 ↓0.2%（5D +12.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-29

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-29 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.23 ｜ 实际 7.079 ｜ 前值 7.335　✅ 今日已公布
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 待公布 ｜ 前值 2.1
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## XBI

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
XBI: 今开 156.13 → 收盘 156.81（+0.4%） ｜ 今日高 157.80 ｜ 低 154.51 ｜ 昨收 156.61 → 收盘 156.81（+0.1%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-06，窗口结束前不做对错判定）

Options: P/C成交量 10.56 | OI比 2.63 | ATM IV 40.4% | Skew 7.4pp | Term 0.78 | ExpMove ±2.9%（近端） | Rank 86%
量化视角： IV 历史高位（Rank 86%，期权偏贵）｜期限结构倒挂（Term 0.78，近月 IV 高于远月）｜保护溢价显著（Skew 7.4pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 10.56）——观察点，非方向信号
   ⇒ Put/Call Volume: 10.56×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 2.63×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-02（3D）±2.9% ｜ 10-09（10D）±4.1% ｜ 10-16（17D）±5.3% ｜ 10-23（24D）±7.2%
   ⇒ IV–VIX Spread: +24.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -33,265,630 | GEX Change vs 上次快照 6,387,798 | Flip: Primary Flip: 163.46（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 332 / LOW 81 / INVALID 349
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 163.46（全链重定价，覆盖 95%）
Put Wall 150（现价高于该位 4.5%）
最近结构参考: Flip 163（现价低于该位 4.1%）
量化视角： 负 Gamma（3327万，无历史分位）｜负 Gamma 缓解（+639万）｜现价位于 Flip 下方 4.07%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（Put Wall） / 155（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 163（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C +0 / P +0 ｜ Activity LOW ｜ 3D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 10D
10-16  C +0 / P +0 ｜ Activity LOW ｜ 17D
10-23  C +0 / P +0 ｜ Activity LOW ｜ 24D

📆 10-02 Forward Structure
存量OI: C 12.2k / P 32.1k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $2.00 / P $2.56 ｜ ATM IV 40.4%，净 delta 敞口 0 shares
仓位参考: Max Pain 155 ｜ Call Wall 162（+3.3%，弱）（OI 1.6k） ｜ Put Wall 148（-5.6%）（OI 9.9k）
量化解读： 存量 Put 重｜ATM IV 40.4%｜历史 Rank 86%（近端代理）｜IV/RV 1.66×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-09（Activity LOW）仓位参考: Max Pain 156 ｜ Call Wall 158（+0.8%，弱）（OI 0.2k） ｜ Put Wall 150（-4.3%，弱）（OI 0.5k）

10-16（Activity LOW）仓位参考: Max Pain 162 ｜ Call Wall 165（+5.2%，弱）（OI 2.9k） ｜ Put Wall 150（-4.3%）（OI 22.6k）

10-23（Activity LOW）仓位参考: Max Pain 159 ｜ Call Wall 154（-1.8%，弱）（OI 75） ｜ Put Wall 153（-2.4%）（OI 0.4k）

📅 事件差分（观察，非因果）: 10-02（3D）ATM IV 40.4% vs 10-09 31.6%（差 +8.9pp）——覆盖 职位空缺(JOLTS) Job Openings、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-29/XBI_evening.json