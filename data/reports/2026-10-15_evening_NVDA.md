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

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **事件差分**: 10-16 ATM IV 48.5% vs 10-19 34.0%（差 +14.5pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 215.34 → 收盘 217.23（+0.9%） ｜ 今日高 218.47 ｜ 低 212.85 ｜ 昨收 221.30 → 收盘 217.23（-1.8%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.58 | OI比 0.83 | ATM IV 48.5% | Skew 3.8pp | Term 0.72 | ExpMove ±2.0%（近端） | Rank 69%
量化视角： IV 中性（Rank 69%）｜期限结构倒挂（Term 0.72，近月 IV 高于远月）｜保护溢价中性（Skew 3.8pp）｜存量 Call 偏重（OI比 0.83）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.58×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.83×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（1D）±2.0% ｜ 10-19（4D）±2.9% ｜ 10-21（6D）±3.8% ｜ 10-23（8D）±4.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 16,112,930 | GEX Change vs 上次快照 50,770,953 | Flip: Primary Flip: 216.74（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 770 / LOW 194 / INVALID 518
结构观察区: Primary Flip 216.74（全链重定价，覆盖 98%）
Put Wall 220（弱结构｜现价低于该位 1.3%）
最近结构参考: Flip 217（现价高于该位 0.2%）
量化视角： 正 Gamma（1611万，无历史分位）｜由负转正（+5077万）｜现价位于 Flip 上方 0.23%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 220（Put Wall，弱结构） / 220（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 217（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +0 / P +0 ｜ Activity LOW ｜ 1D
10-19  C +0 / P +0 ｜ Activity LOW ｜ 4D
10-21  C +0 / P +0 ｜ Activity LOW ｜ 6D
10-23  C +0 / P +0 ｜ Activity LOW ｜ 8D

📆 10-16 Forward Structure
存量OI: C 1065.0k / P 882.3k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $2.17 / P $2.29 ｜ ATM IV 48.5%，净 delta 敞口 0 shares
仓位参考: Max Pain 220 ｜ Call Wall 220（+1.3%，弱）（OI 100.4k） ｜ Put Wall 220（+1.3%，弱）（OI 71.7k）
量化解读： 存量 Call 重｜ATM IV 48.5%｜历史 Rank 69%（近端代理）｜IV/RV 2.22×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-19（Activity LOW）仓位参考: Max Pain 225 ｜ Call Wall 225（+3.6%，弱）（OI 4.6k） ｜ Put Wall 230（+5.9%，弱）（OI 4.4k）

10-21（Activity LOW）仓位参考: Max Pain 225 ｜ Call Wall 230（+5.9%，弱）（OI 4.2k） ｜ Put Wall 220（+1.3%）（OI 3.9k）

10-23（Activity LOW）仓位参考: Max Pain 225 ｜ Call Wall 235（+8.2%，弱）（OI 15.0k） ｜ Put Wall 220（+1.3%，弱）（OI 13.3k）

📅 事件差分（观察，非因果）: 10-16（1D）ATM IV 48.5% vs 10-19 34.0%（差 +14.5pp）——覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-15/NVDA_evening.json