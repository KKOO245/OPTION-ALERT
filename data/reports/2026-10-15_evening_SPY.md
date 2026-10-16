# 期权晚报 2026-10-15（快照 21:00 ET）

📊 市场环境

SPY $771.79 ｜ QQQ $728.00
VIX 16.46 ↓2.4%（5D +6.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-15

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 1.3 ｜ 前值 0.5　✅ 今日已公布
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 0.8 ｜ 前值 1.3　✅ 今日已公布
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布　⏰ 今日

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 766.25 → 收盘 771.79（+0.7%） ｜ 今日高 772.87 ｜ 低 764.43 ｜ 昨收 769.60 → 收盘 771.79（+0.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.10 | OI比 3.18 | ATM IV 12.9% | Skew 1.6pp | Term 1.00 | ExpMove ±0.5%（近端） | Rank 51%
量化视角： IV 中性（Rank 51%）｜期限结构正常（Term 1.00）｜保护溢价薄（Skew 1.6pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.10×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 3.18×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 35% ｜ P/C OI(近端) 97%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 35%）｜近端 Put 显著偏重（P/C OI 分位 97%，历史高位区）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-16（1D）±0.5% ｜ 10-19（4D）±0.8% ｜ 10-20（5D）±0.9% ｜ 10-21（6D）±1.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -936,658,029 | GEX Change vs 上次快照 677,465,529 | Flip: Primary Flip: 775.47（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 2715 / LOW 271 / INVALID 1584
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 775.47（全链重定价，覆盖 98%）
最近结构参考: Flip 775（现价低于该位 0.5%）
量化视角： 负 Gamma（9.37亿，历史分位 35%，中性区）｜负 Gamma 缓解（+6.77亿）｜现价位于 Flip 下方 0.47%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 770（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 775（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +0 / P +0 ｜ Activity LOW ｜ 1D
10-19  C +0 / P +0 ｜ Activity LOW ｜ 4D
10-20  C +0 / P +0 ｜ Activity LOW ｜ 5D
10-21  C +0 / P +0 ｜ Activity LOW ｜ 6D

📆 10-16 Forward Structure
存量OI: C 786.9k / P 2503.0k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $2.12 / P $2.08 ｜ ATM IV 12.9%，净 delta 敞口 0 shares
仓位参考: Max Pain 770 ｜ Call Wall 785（+1.7%，弱）（OI 56.8k） ｜ Put Wall 750（-2.8%，弱）（OI 66.1k）
量化解读： 存量 Put 重｜ATM IV 12.9%｜历史 Rank 51%（近端代理）｜IV/RV 1.66×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-19（Activity LOW）仓位参考: Max Pain 774 ｜ Call Wall 790（+2.4%，弱）（OI 4.9k） ｜ Put Wall 750（-2.8%，弱）（OI 8.0k）

10-20（Activity LOW）仓位参考: Max Pain 774 ｜ Call Wall 789（+2.2%）（OI 4.5k） ｜ Put Wall 751（-2.7%，弱）（OI 12.5k）

10-21（Activity LOW）仓位参考: Max Pain 773 ｜ Call Wall 788（+2.1%，弱）（OI 2.6k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-15/SPY_evening.json