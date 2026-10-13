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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## XBI

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
XBI: 今开 150.52 → 收盘 146.80（-2.5%） ｜ 今日高 150.84 ｜ 低 146.70 ｜ 昨收 151.40 → 收盘 146.80（-3.0%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-16，窗口结束前不做对错判定）

Options: P/C成交量 3.68 | OI比 1.69 | ATM IV 37.3% | Skew -0.4pp | Term 0.90 | ExpMove ±2.5%（近端） | Rank 73%
量化视角： IV 中性（Rank 73%）｜期限结构倒挂（Term 0.90，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.4pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 3.68）——观察点，非方向信号
   ⇒ Put/Call Volume: 3.68×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.69×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-16（3D）±2.5% ｜ 10-23（10D）±4.3% ｜ 10-30（17D）±7.0% ｜ 11-06（24D）±2.7%
   ⇒ IV–VIX Spread: +22.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -63,869,417 | GEX Change vs 上次快照 2,678,359 | Flip: Primary Flip: 159.19（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 85%（带内） ｜ IV 有效性: VALID 334 / LOW 133 / INVALID 305
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 159.19（全链重定价，覆盖 85%）
Put Wall 150（现价低于该位 2.1%）
最近结构参考: Put Wall 150（现价低于该位 2.1%）
量化视角： 负 Gamma（6387万，无历史分位）｜负 Gamma 缓解（+268万）｜现价位于 Flip 下方 7.78%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 150（Put Wall） / 156（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 159（全链重定价，覆盖 85%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +0.3k / P -1.6k ｜ Activity MEDIUM △ ｜ 3D
10-23  C +77 / P +6 ｜ Activity MEDIUM △ ｜ 10D
10-30  C +27 / P -0.2k ｜ Activity MEDIUM △ ｜ 17D
11-06  C +22 / P +10 ｜ Activity MEDIUM △ ｜ 24D

📆 10-16 Forward Structure
存量OI: C 44.8k / P 75.6k，今日变化ΔOI: C +0.3k / P -1.6k，平值价格ATM: C $2.03 / P $1.59 ｜ ATM IV 37.3%，净 delta 敞口 153k shares
Top ΔOI: P 165 -1,096 ｜ C 156 +656
仓位参考: Max Pain 156 ｜ Call Wall 155（+5.6%，弱）（OI 2.5k） ｜ Put Wall 150（+2.2%）（OI 23.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 37.3%｜历史 Rank 73%（近端代理）｜IV/RV 1.39×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 153,415 股

10-23（MEDIUM △）Top ΔOI: 160C +22
10-23（MEDIUM △）仓位参考: Max Pain 154 ｜ Call Wall 155（+5.6%，弱）（OI 0.3k） ｜ Put Wall 140（-4.6%，弱）（OI 0.7k）

10-30（MEDIUM △）Top ΔOI: 140P -104 ｜ 150P -82
10-30（MEDIUM △）仓位参考: Max Pain 153 ｜ Call Wall 155（+5.6%）（OI 1.4k） ｜ Put Wall 150（+2.2%，弱）（OI 7.2k）

11-06（MEDIUM △）Top ΔOI: 160C +9 ｜ 148C +7
11-06（MEDIUM △）仓位参考: Max Pain 155 ｜ Call Wall 150（+2.2%，弱）（OI 35） ｜ Put Wall 143（-2.6%）（OI 0.2k）

📅 事件差分（观察，非因果）: 10-16（3D）ATM IV 37.3% vs 10-23 30.7%（差 +6.7pp）——覆盖 成屋销售、Core Inflation Rate MoM 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=50 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=50）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-13/XBI_evening.json