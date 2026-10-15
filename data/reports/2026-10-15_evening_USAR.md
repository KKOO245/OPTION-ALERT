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
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **事件差分**: 10-16 ATM IV 89.4% vs 10-23 78.2%（差 +11.2pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-16 11C ΔOI +1,928（距现价 -0.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 9.89 → 收盘 11.09（+12.1%） ｜ 今日高 11.13 ｜ 低 9.82 ｜ 昨收 10.32 → 收盘 11.09（+7.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.52 | OI比 0.22 | ATM IV 89.4% | Skew 1.2pp | Term 0.97 | ExpMove ±3.7%（近端） | Rank 20%
量化视角： IV 历史低位（Rank 20%，期权偏便宜）｜期限结构正常（Term 0.97）｜保护溢价薄（Skew 1.2pp）｜存量 Call 偏重（OI比 0.22）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.52×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.22×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（1D）±3.7% ｜ 10-23（8D）±9.6% ｜ 10-30（15D）±14.1% ｜ 11-06（22D）±17.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 592,886 | GEX Change vs 上次快照 1,387,886 | Flip: Primary Flip: 10.83（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 208 / LOW 95 / INVALID 109
结构观察区: Primary Flip 10.83（全链重定价，覆盖 97%）
最近结构参考: Flip 11（现价高于该位 2.4%）
量化视角： 正 Gamma（59万，无历史分位）｜由负转正（+139万）｜现价位于 Flip 上方 2.41%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 13（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 11（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +2.6k / P -1.0k ｜ Activity HIGH ｜ 1D
10-23  C +1.9k / P +1.1k ｜ Activity HIGH ｜ 8D
10-30  C +0.6k / P +0.3k ｜ Activity HIGH ｜ 15D
11-06  C +0.2k / P +0.6k ｜ Activity HIGH ｜ 22D

📆 10-16 Forward Structure
存量OI: C 59.2k / P 13.1k，今日变化ΔOI: C +2.6k / P -1.0k，平值价格ATM: C $0.23 / P $0.18 ｜ ATM IV 89.4%，净 delta 敞口 314k shares
Top ΔOI: C 11 +1,928 ｜ P 13 -671 ｜ C 11 +580
仓位参考: Max Pain 13 ｜ Call Wall 11（-0.8%，弱）（OI 2.5k）
量化解读： 存量 Call 重｜ATM IV 89.4%｜历史 Rank 20%（近端代理）｜IV/RV 1.96×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 314,258 股

📆 10-23 Forward Structure
存量OI: C 15.8k / P 5.9k，今日变化ΔOI: C +1.9k / P +1.1k，平值价格ATM: C $0.60 / P $0.46 ｜ ATM IV 78.2%，净 delta 敞口 130k shares
Top ΔOI: C 11 +824 ｜ C 12 +351
仓位参考: Max Pain 12 ｜ Put Wall 12（+8.2%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 78.2%｜历史 Rank 20%（近端代理）｜IV/RV 1.71×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 129,520 股

📆 10-30 Forward Structure
存量OI: C 8.5k / P 9.1k，今日变化ΔOI: C +0.6k / P +0.3k，平值价格ATM: C $0.78 / P $0.78 ｜ ATM IV 80.9%，净 delta 敞口 46k shares
Top ΔOI: P 10 +317 ｜ C 11 +177
仓位参考: Max Pain 14 ｜ Call Wall 11（-0.8%，弱）（OI 0.2k） ｜ Put Wall 12（+8.2%，弱）（OI 0.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 80.9%｜历史 Rank 20%（近端代理）｜IV/RV 1.77×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 46,325 股

📆 11-06 Forward Structure
存量OI: C 3.6k / P 5.3k，今日变化ΔOI: C +0.2k / P +0.6k，平值价格ATM: C $0.96 / P $0.96 ｜ ATM IV 86.9%，净 delta 敞口 22k shares
Top ΔOI: P 10 +119 ｜ C 11 +104
仓位参考: Max Pain 15 ｜ Put Wall 10（-9.8%，弱）（OI 0.8k）
量化解读： 存量 Put 重｜ATM IV 86.9%｜历史 Rank 20%（近端代理）｜IV/RV 1.90×（近似）｜净 delta 敞口 正 21,574 股

📅 事件差分（观察，非因果）: 10-16（1D）ATM IV 89.4% vs 10-23 78.2%（差 +11.2pp）——覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-15/USAR_evening.json