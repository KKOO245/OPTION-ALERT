# 期权晚报 2026-10-29（快照 21:00 ET）

📊 市场环境

SPY $769.36 ｜ QQQ $715.34
VIX 17.20 ↑1.7%（5D -9.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-29

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 3.4 ｜ 前值 2.2　✅ 今日已公布
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 0.5 ｜ 前值 0.9　✅ 今日已公布
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 173.15 → 收盘 171.99（-0.7%） ｜ 今日高 178.33 ｜ 低 168.76 ｜ 昨收 182.34 → 收盘 171.99（-5.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.69 | OI比 0.57 | ATM IV 98.6% | Skew 2.5pp | Term 0.98 | ExpMove ±4.2%（近端） | Rank 43%
量化视角： IV 中性（Rank 43%）｜期限结构正常（Term 0.98）｜保护溢价中性（Skew 2.5pp）｜存量 Call 偏重（OI比 0.57）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.69×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.57×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（1D）±4.2% ｜ 11-06（8D）±10.9% ｜ 11-13（15D）±16.9% ｜ 11-20（22D）±20.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,436,140 | GEX Change vs 上次快照 -1,303,214 | Flip: Primary Flip: 170.76（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 601 / LOW 68 / INVALID 185
结构观察区: Primary Flip 170.76（全链重定价，覆盖 99%）
最近结构参考: Flip 171（现价高于该位 0.7%）
量化视角： 正 Gamma（144万，无历史分位）｜正 Gamma 减弱（130万）｜现价位于 Flip 上方 0.72%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 175（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 171（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-30  C +0 / P +0 ｜ Activity LOW ｜ 1D
11-06  C +0 / P +0 ｜ Activity LOW ｜ 8D
11-13  C +0 / P +0 ｜ Activity LOW ｜ 15D
11-20  C +0 / P +0 ｜ Activity LOW ｜ 22D

📆 10-30 Forward Structure
存量OI: C 96.3k / P 54.9k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $3.40 / P $3.80 ｜ ATM IV 98.6%，净 delta 敞口 0 shares
仓位参考: Max Pain 175 ｜ Call Wall 180（+4.7%，弱）（OI 3.9k） ｜ Put Wall 160（-7.0%，弱）（OI 3.1k）
量化解读： 存量 Call 重｜ATM IV 98.6%｜历史 Rank 43%（近端代理）｜IV/RV 1.06×（近似）｜净 delta 敞口 正 0 股

11-06（Activity LOW）仓位参考: Max Pain 190 ｜ Call Wall 170（-1.2%，弱）（OI 2.3k） ｜ Put Wall 170（-1.2%，弱）（OI 1.9k）

11-13（Activity LOW）仓位参考: Max Pain 190 ｜ Call Wall 175（+1.8%，弱）（OI 1.1k） ｜ Put Wall 165（-4.1%，弱）（OI 1.4k）

11-20（Activity LOW）仓位参考: Max Pain 195 ｜ Call Wall 180（+4.7%，弱）（OI 5.5k） ｜ Put Wall 180（+4.7%，弱）（OI 3.2k）

📅 事件差分（观察，非因果）: 10-30（1D）ATM IV 98.6% vs 11-06 91.3%（差 +7.3pp）——覆盖 GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM、PCE 物价 Price Index MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-29/NBIS_evening.json