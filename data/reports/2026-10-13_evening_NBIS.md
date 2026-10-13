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
🟡 **事件差分**: 10-16 ATM IV 83.0% vs 10-23 71.6%（差 +11.4pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-16 200P ΔOI +1,103（距现价 -3.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 200.91 → 收盘 206.86（+3.0%） ｜ 今日高 207.92 ｜ 低 197.60 ｜ 昨收 210.06 → 收盘 206.86（-1.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.50 | OI比 0.96 | ATM IV 83.0% | Skew -4.1pp | Term 0.95 | ExpMove ±6.0%（近端） | Rank 14%
量化视角： IV 历史低位（Rank 14%，期权偏便宜）｜期限结构正常（Term 0.95）｜Put 保护异常便宜（Skew -4.1pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.50×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.96×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（3D）±6.0% ｜ 10-23（10D）±9.4% ｜ 10-30（17D）±12.3% ｜ 11-06（24D）±14.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -12,736,843 | GEX Change vs 上次快照 7,443,858 | Flip: Primary Flip: 218.50（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 516 / LOW 46 / INVALID 112
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 218.50（全链重定价，覆盖 100%）
Put Wall 200（弱结构｜现价高于该位 3.4%）
最近结构参考: Put Wall 200（现价高于该位 3.4%）
量化视角： 负 Gamma（1274万，无历史分位）｜负 Gamma 缓解（+744万）｜现价位于 Flip 下方 5.33%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall，弱结构）；上方 220（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 219（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +12.6k / P +5.4k ｜ Activity HIGH ｜ 3D
10-23  C +5.2k / P +3.7k ｜ Activity HIGH ｜ 10D
10-30  C +1.7k / P +1.0k ｜ Activity HIGH ｜ 17D
11-06  C +0.6k / P +1.7k ｜ Activity HIGH ｜ 24D

📆 10-16 Forward Structure
存量OI: C 126.5k / P 121.6k，今日变化ΔOI: C +12.6k / P +5.4k，平值价格ATM: C $5.97 / P $6.48 ｜ ATM IV 83.0%，净 delta 敞口 266k shares
Top ΔOI: C 230 +2,543 ｜ C 220 +1,690 ｜ P 200 +1,103
仓位参考: Max Pain 220 ｜ Call Wall 220（+6.4%，弱）（OI 4.4k） ｜ Put Wall 220（+6.4%，弱）（OI 8.7k）
量化解读： 存量两侧均衡｜ATM IV 83.0%｜历史 Rank 14%（近端代理）｜IV/RV 1.30×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 265,981 股

📆 10-23 Forward Structure
存量OI: C 24.4k / P 18.9k，今日变化ΔOI: C +5.2k / P +3.7k，平值价格ATM: C $9.70 / P $9.77 ｜ ATM IV 71.6%，净 delta 敞口 43k shares
Top ΔOI: C 215 +1,270 ｜ P 190 +867
仓位参考: Max Pain 215 ｜ Call Wall 212.5（+2.7%，弱）（OI 2.1k） ｜ Put Wall 200（-3.3%）（OI 3.0k）
量化解读： 存量 Call 重｜ATM IV 71.6%｜历史 Rank 14%（近端代理）｜IV/RV 1.12×（近似）｜净 delta 敞口 正 42,958 股

📆 10-30 Forward Structure
存量OI: C 22.6k / P 17.6k，今日变化ΔOI: C +1.7k / P +1.0k，平值价格ATM: C $12.70 / P $12.78 ｜ ATM IV 72.0%，净 delta 敞口 23k shares
Top ΔOI: C 220 +430 ｜ C 260 +299
仓位参考: Max Pain 225 ｜ Call Wall 220（+6.4%，弱）（OI 0.7k） ｜ Put Wall 200（-3.3%，弱）（OI 2.2k）
量化解读： 存量 Call 重｜ATM IV 72.0%｜历史 Rank 14%（近端代理）｜IV/RV 1.13×（近似）｜净 delta 敞口 正 23,211 股

📆 11-06 Forward Structure
存量OI: C 7.8k / P 13.0k，今日变化ΔOI: C +0.6k / P +1.7k，平值价格ATM: C $16.70 / P $14.19 ｜ ATM IV 73.5%，净 delta 敞口 -27k shares
Top ΔOI: P 200 +493 ｜ P 220 +230 ｜ C 215 +214
仓位参考: Max Pain 230 ｜ Put Wall 200（-3.3%）（OI 3.0k）
量化解读： 存量 Put 重｜ATM IV 73.5%｜历史 Rank 14%（近端代理）｜IV/RV 1.15×（近似）｜净 delta 敞口 负 26,753 股

📅 事件差分（观察，非因果）: 10-16（3D）ATM IV 83.0% vs 10-23 71.6%（差 +11.4pp）——覆盖 成屋销售、Core Inflation Rate MoM 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-13/NBIS_evening.json