# 期权晚报 2026-10-12（快照 21:00 ET）

📊 市场环境

SPY $778.10 ｜ QQQ $746.04
VIX 15.21 ↑2.5%（5D -2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 45.7（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-12

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-13 10:00　【高】成屋销售　预测 3.96 ｜ 实际 待公布 ｜ 前值 3.98
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.7 ｜ 实际 待公布 ｜ 前值 3.4
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 待公布 ｜ 前值 2.4
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 749.64 → 收盘 746.04（-0.5%） ｜ 今日高 749.79 ｜ 低 744.85 ｜ 昨收 751.27 → 收盘 746.04（-0.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.08 | OI比 2.91 | ATM IV 13.7% | Skew 1.9pp | Term 1.34 | ExpMove ±0.6%（近端） | Rank 22%
量化视角： IV 历史低位（Rank 22%，期权偏便宜）｜期限结构正常偏陡（Term 1.34）｜保护溢价薄（Skew 1.9pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.08×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 2.91×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 32% ｜ P/C OI(近端) 96%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 32%）｜近端 Put 显著偏重（P/C OI 分位 96%，历史高位区）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-13（1D）±0.6% ｜ 10-14（2D）±1.0% ｜ 10-15（3D）±1.2% ｜ 10-16（4D）±1.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -279,203,182 | GEX Change vs 上次快照 49,605,955 | Flip: Primary Flip: 749.65（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 3121 / LOW 290 / INVALID 1295
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 749.65（全链重定价，覆盖 98%）
Call Wall 760（弱结构｜现价低于该位 1.8%）
最近结构参考: Flip 750（现价低于该位 0.5%）
量化视角： 负 Gamma（2.79亿，历史分位 32%，中性区）｜负 Gamma 缓解（+4961万）｜现价位于 Flip 下方 0.48%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 751（MaxPain，仅结算参考） / 760（Call Wall，弱结构）。
• Gamma 区域：切换参考 750（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-13  C +0 / P +0 ｜ Activity LOW ｜ 1D
10-14  C +0 / P +0 ｜ Activity LOW ｜ 2D
10-15  C +0 / P +0 ｜ Activity LOW ｜ 3D
10-16  C +0 / P +0 ｜ Activity LOW ｜ 4D

📆 10-13 Forward Structure
存量OI: C 42.5k / P 123.6k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $2.00 / P $2.31 ｜ ATM IV 13.7%，净 delta 敞口 0 shares
仓位参考: Max Pain 751 ｜ Call Wall 760（+1.9%，弱）（OI 2.8k） ｜ Put Wall 750（+0.5%，弱）（OI 12.7k）
量化解读： 存量 Put 重｜ATM IV 13.7%｜历史 Rank 22%（近端代理）｜IV/RV 0.98×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

10-14（Activity LOW）仓位参考: Max Pain 751 ｜ Call Wall 755（+1.2%，弱）（OI 2.3k） ｜ Put Wall 730（-2.2%，弱）（OI 2.8k）

10-15（Activity LOW）仓位参考: Max Pain 750 ｜ Call Wall 767（+2.8%，弱）（OI 2.1k）

10-16（Activity LOW）仓位参考: Max Pain 734 ｜ Call Wall 760（+1.9%，弱）（OI 66.6k） ｜ Put Wall 740（-0.8%，弱）（OI 29.7k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-12/QQQ_evening.json