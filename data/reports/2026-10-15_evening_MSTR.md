# 期权晚报 2026-10-15（快照 16:40 ET）

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

🔍 重点速览
🔴 **事件差分**: 10-16（1D）ATM IV 89.3% vs 10-23 70.6%（差 +18.7pp），覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-23 150P ΔOI +2,243（距现价 -0.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 137.72 → 收盘 151.29（+9.9%） ｜ 今日高 151.33 ｜ 低 134.89 ｜ 昨收 143.24 → 收盘 151.29（+5.6%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.39 | OI比 0.64 | ATM IV 89.3% | Skew -4.2pp | Term 0.78 | ExpMove ±3.9%（近端） | Rank 66%
量化视角： IV 中性（Rank 66%）｜期限结构倒挂（Term 0.78，近月 IV 高于远月）｜Put 保护异常便宜（Skew -4.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.64）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.39×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.64×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（1D）±3.9% ｜ 10-23（8D）±8.4% ｜ 10-30（15D）±11.8% ｜ 11-06（22D）±14.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 54,290,078 | GEX Change vs 上次快照 78,956,212 | Flip: Primary Flip: 145.53（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 566 / LOW 94 / INVALID 224
结构观察区: Primary Flip 145.53（全链重定价，覆盖 97%）
最近结构参考: Flip 146（现价高于该位 4.0%）
量化视角： 正 Gamma（5429万，无历史分位）｜由负转正（+7896万）｜现价位于 Flip 上方 3.96%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 139（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 146（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C -8.0k / P -13.8k ｜ Activity HIGH ｜ 1D
10-23  C +4.3k / P +12.2k ｜ Activity HIGH ｜ 8D
10-30  C +0.4k / P +4.4k ｜ Activity HIGH ｜ 15D
11-06  C +0.4k / P +1.0k ｜ Activity MEDIUM △ ｜ 22D

📆 10-16 Forward Structure
存量OI: C 344.6k / P 221.1k，今日变化ΔOI: C -8.0k / P -13.8k，平值价格ATM: C $2.31 / P $3.60 ｜ ATM IV 89.3%，净 delta 敞口 1.1M shares
Top ΔOI: C 165 -10,179 ｜ C 160 -5,074 ｜ P 142 -3,713
仓位参考: Max Pain 139 ｜ Call Wall 157.5（+4.1%，弱）（OI 41.1k） ｜ Put Wall 150（-0.9%，弱）（OI 7.0k）
量化解读： 存量 Call 重｜ATM IV 89.3%｜历史 Rank 66%（近端代理）｜IV/RV 2.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,099,249 股

📆 10-23 Forward Structure
存量OI: C 50.5k / P 108.6k，今日变化ΔOI: C +4.3k / P +12.2k，平值价格ATM: C $5.85 / P $6.87 ｜ ATM IV 70.6%，净 delta 敞口 34k shares
Top ΔOI: P 150 +2,243 ｜ C 167 +1,160
仓位参考: Max Pain 155 ｜ Call Wall 165（+9.1%，弱）（OI 3.3k） ｜ Put Wall 150（-0.9%，弱）（OI 5.5k）
量化解读： 存量 Put 重｜ATM IV 70.6%｜历史 Rank 66%（近端代理）｜IV/RV 1.72×（近似）｜净 delta 敞口 正 34,206 股

📆 10-30 Forward Structure
存量OI: C 34.7k / P 57.4k，今日变化ΔOI: C +0.4k / P +4.4k，平值价格ATM: C $8.25 / P $9.65 ｜ ATM IV 72.0%，净 delta 敞口 -120k shares
Top ΔOI: C 160 -1,279 ｜ P 152 +952 ｜ P 147 +552
仓位参考: Max Pain 160 ｜ Call Wall 162.5（+7.4%，弱）（OI 2.8k） ｜ Put Wall 155（+2.5%，弱）（OI 3.7k）
量化解读： 存量 Put 重｜ATM IV 72.0%｜历史 Rank 66%（近端代理）｜IV/RV 1.75×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 120,407 股

11-06（MEDIUM △）Top ΔOI: 140P +223 ｜ 145P +165
11-06（MEDIUM △）仓位参考: Max Pain 160 ｜ Call Wall 160（+5.8%）（OI 1.9k） ｜ Put Wall 160（+5.8%，弱）（OI 3.0k）

📅 事件差分（观察，非因果）: 10-16（1D）ATM IV 89.3% vs 10-23 70.6%（差 +18.7pp）——覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-15/MSTR_evening.json