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
🔴 **事件差分**: 10-16（2D）ATM IV 54.8% vs 10-19 39.6%（差 +15.2pp），覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY、Inflation Rate YoY、Inflation Rate MoM、PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 10-19 375C ΔOI +602（距现价 +2.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 371.15 → 收盘 367.16（-1.1%） ｜ 今日高 371.39 ｜ 低 363.82 ｜ 昨收 375.23 → 收盘 367.16（-2.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.12 | OI比 0.76 | ATM IV 23.1% | Skew 8.8pp | Term 1.89 | ExpMove ±3.2%（近端） | Rank 90%
量化视角： IV 历史高位（Rank 90%，期权偏贵）｜期限结构正常偏陡（Term 1.89）｜保护溢价显著（Skew 8.8pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.76）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.12×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.76×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（2D）±3.2% ｜ 10-19（5D）±3.7% ｜ 10-23（9D）±7.4% ｜ 10-26（12D）±7.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 4,319,525 | GEX Change vs 上次快照 10,796,105 | Flip: Primary Flip: 366.36（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 1049 / LOW 167 / INVALID 762
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 366.36（全链重定价，覆盖 94%）
Call Wall 400（现价低于该位 8.2%）
最近结构参考: Flip 366（现价高于该位 0.2%）
量化视角： 正 Gamma（432万，无历史分位）｜由负转正（+1080万）｜现价位于 Flip 上方 0.22%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 375（MaxPain，仅结算参考） / 400（Call Wall）。
• Gamma 区域：切换参考 366（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +9.0k / P +9.8k ｜ Activity MEDIUM △ ｜ 2D
10-19  C +4.7k / P +2.5k ｜ Activity HIGH ｜ 5D
10-23  C +5.7k / P +4.3k ｜ Activity HIGH ｜ 9D
10-26  C +1.0k / P +1.5k ｜ Activity HIGH ｜ 12D

📆 10-16 Forward Structure
存量OI: C 404.1k / P 402.4k，今日变化ΔOI: C +9.0k / P +9.8k，平值价格ATM: C $6.00 / P $5.95 ｜ ATM IV 54.8%，净 delta 敞口 97k shares
Top ΔOI: C 400 +1,711
仓位参考: Max Pain 372 ｜ Call Wall 400（+8.9%，弱）（OI 26.1k） ｜ Put Wall 380（+3.5%，弱）（OI 15.0k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 54.8%｜历史 Rank 90%（近端代理）｜IV/RV 2.03×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 97,246 股

📆 10-19 Forward Structure
存量OI: C 27.0k / P 10.6k，今日变化ΔOI: C +4.7k / P +2.5k，平值价格ATM: C $6.70 / P $7.02 ｜ ATM IV 39.6%，净 delta 敞口 -33k shares
Top ΔOI: C 375 +602 ｜ C 390 +573
仓位参考: Max Pain 375 ｜ Call Wall 400（+8.9%，弱）（OI 3.2k） ｜ Put Wall 360（-2.0%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 39.6%｜历史 Rank 90%（近端代理）｜IV/RV 1.47×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 33,387 股

📆 10-23 Forward Structure
存量OI: C 73.0k / P 50.0k，今日变化ΔOI: C +5.7k / P +4.3k，平值价格ATM: C $13.60 / P $13.59 ｜ ATM IV 58.4%，净 delta 敞口 -51k shares
Top ΔOI: C 390 +1,242 ｜ P 375 +792 ｜ P 362 +670
仓位参考: Max Pain 372 ｜ Call Wall 400（+8.9%，弱）（OI 6.3k） ｜ Put Wall 360（-2.0%，弱）（OI 3.0k）
量化解读： 存量 Call 重｜ATM IV 58.4%｜历史 Rank 90%（近端代理）｜IV/RV 2.16×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 50,927 股

📆 10-26 Forward Structure
存量OI: C 1.7k / P 2.8k，今日变化ΔOI: C +1.0k / P +1.5k，平值价格ATM: C $13.65 / P $14.40 ｜ ATM IV 52.2%，净 delta 敞口 -10k shares
Top ΔOI: P 350 +217
仓位参考: Max Pain 375 ｜ Call Wall 380（+3.5%，弱）（OI 0.3k） ｜ Put Wall 350（-4.7%，弱）（OI 0.2k）
量化解读： 存量 Put 重｜ATM IV 52.2%｜历史 Rank 90%（近端代理）｜IV/RV 1.93×（近似）｜净 delta 敞口 负 10,366 股

📅 事件差分（观察，非因果）: 10-16（2D）ATM IV 54.8% vs 10-19 39.6%（差 +15.2pp）——覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY、Inflation Rate YoY、Inflation Rate MoM、PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-14/TSLA_evening.json