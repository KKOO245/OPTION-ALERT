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


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 778.78 → 收盘 778.10（-0.1%） ｜ 今日高 779.40 ｜ 低 777.05 ｜ 昨收 778.57 → 收盘 778.10（-0.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.26 | OI比 1.38 | ATM IV 8.5% | Skew 0.8pp | Term 1.46 | ExpMove ±0.3%（近端） | Rank 15%
量化视角： IV 历史低位（Rank 15%，期权偏便宜）｜期限结构正常偏陡（Term 1.46）｜保护溢价薄（Skew 0.8pp）｜当日成交偏 Put（P/C量 1.26）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.26×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.38×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 61% ｜ P/C OI(近端) 15%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 61%）｜近端持仓结构中性（P/C OI 分位 15%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-13（1D）±0.3% ｜ 10-14（2D）±0.6% ｜ 10-15（3D）±0.8% ｜ 10-16（4D）±0.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 242,397,681 | GEX Change vs 上次快照 -231,881,228 | Flip: Primary Flip: 776.96（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 2803 / LOW 334 / INVALID 1441
结构观察区: Primary Flip 776.96（全链重定价，覆盖 98%）
Call Wall 800（弱结构｜现价低于该位 2.7%）
最近结构参考: Flip 777（现价高于该位 0.1%）
量化视角： 正 Gamma（2.42亿，历史分位 61%，中性区）｜正 Gamma 减弱（2.32亿）｜现价位于 Flip 上方 0.15%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 776（MaxPain，仅结算参考）；上方 800（Call Wall，弱结构）。
• Gamma 区域：切换参考 777（全链重定价，覆盖 98%）。
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
存量OI: C 88.0k / P 121.2k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $1.43 / P $1.33 ｜ ATM IV 8.5%，净 delta 敞口 0 shares
仓位参考: Max Pain 776 ｜ Call Wall 790（+1.5%，弱）（OI 5.4k） ｜ Put Wall 774（-0.5%，弱）（OI 4.1k）
量化解读： 存量 Put 重｜ATM IV 8.5%｜历史 Rank 15%（近端代理）｜IV/RV 0.99×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

10-14（Activity LOW）仓位参考: Max Pain 776 ｜ Call Wall 790（+1.5%）（OI 19.1k） ｜ Put Wall 755（-3.0%，弱）（OI 5.1k）

10-15（Activity LOW）仓位参考: Max Pain 776 ｜ Call Wall 796（+2.3%，弱）（OI 2.0k） ｜ Put Wall 772（-0.8%，弱）（OI 4.2k）

10-16（Activity LOW）仓位参考: Max Pain 770 ｜ Call Wall 785（+0.9%）（OI 73.9k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-12/SPY_evening.json