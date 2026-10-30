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

🔍 重点速览
🔴 **事件差分**: 10-30（1D）ATM IV 96.3% vs 11-06 80.6%（差 +15.7pp），覆盖 GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM、PCE 物价 Price Index MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔵 **Flip 状态**: CONDITIONAL（Candidates: 11.7）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 12.11 → 收盘 12.21（+0.8%） ｜ 今日高 12.90 ｜ 低 12.06 ｜ 昨收 12.39 → 收盘 12.21（-1.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.14 | OI比 0.17 | ATM IV 96.3% | Skew -2.9pp | Term 0.80 | ExpMove ±3.9%（近端） | Rank 37%
量化视角： IV 中性（Rank 37%）｜期限结构倒挂（Term 0.80，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.9pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.17）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.14×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.17×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（1D）±3.9% ｜ 11-06（8D）±8.8% ｜ 11-13（15D）±14.3% ｜ 11-20（22D）±16.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 656,014 | GEX Change vs 上次快照 144,749 | Flip: Candidates 11.67 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 78%（带内） ｜ IV 有效性: VALID 120 / LOW 90 / INVALID 198
结构观察区: ≈12（全链重定价，覆盖 78%，CONDITIONAL）
Put Wall 12（弱结构｜现价高于该位 1.8%）
最近结构参考: Put Wall 12（现价高于该位 1.8%）
量化视角： 正 Gamma（66万，无历史分位）｜正 Gamma 增强（+14万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 12（Put Wall，弱结构）；上方 13（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 12（全链重定价，覆盖 78%）。
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
存量OI: C 8.5k / P 1.4k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $0.43 / P $0.05 ｜ ATM IV 96.3%，净 delta 敞口 0 shares
仓位参考: Max Pain 13 ｜ Put Wall 13（+6.5%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 96.3%｜历史 Rank 37%（近端代理）｜IV/RV 1.48×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-06（Activity LOW）仓位参考: Max Pain 14 ｜ Put Wall 11（-9.9%，弱）（OI 0.3k）

11-13（Activity LOW）仓位参考: Max Pain 14 ｜ Put Wall 13（+6.5%，弱）（OI 68）

11-20（Activity LOW）仓位参考: Max Pain 15 ｜ Put Wall 12（-1.7%，弱）（OI 0.3k）

📅 事件差分（观察，非因果）: 10-30（1D）ATM IV 96.3% vs 11-06 80.6%（差 +15.7pp）——覆盖 GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM、PCE 物价 Price Index MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-29/NNE_evening.json