# 期权晚报 2026-09-29（快照 21:00 ET）

📊 市场环境

SPY $764.20 ｜ QQQ $nan
VIX 16.04 ↓0.2%（5D +12.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-29

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-29 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.23 ｜ 实际 7.079 ｜ 前值 7.335　✅ 今日已公布
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 待公布 ｜ 前值 2.1
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）


## SPCX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPCX: 今开 146.68 → 收盘 149.24（+1.7%） ｜ 今日高 150.06 ｜ 低 145.47 ｜ 昨收 145.47 → 收盘 149.24（+2.6%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.43 | OI比 1.04 | ATM IV 50.3% | Skew -0.1pp | Term 0.90 | ExpMove ±3.6%（近端） | Rank 25%
量化视角： IV 历史低位（Rank 25%，期权偏便宜）｜期限结构倒挂（Term 0.90，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.1pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.43×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.04×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-02（3D）±3.6% ｜ 10-09（10D）±6.0% ｜ 10-16（17D）±7.8% ｜ 10-23（24D）±9.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 27,182,932 | GEX Change vs 上次快照 46,171,795 | Flip: Primary Flip: 147.55（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 535 / LOW 84 / INVALID 303
结构观察区: Primary Flip 147.55（全链重定价，覆盖 100%）
Call Wall 160（弱结构｜现价低于该位 6.7%）
最近结构参考: Flip 148（现价高于该位 1.1%）
量化视角： 正 Gamma（2718万，无历史分位）｜由负转正（+4617万）｜现价位于 Flip 上方 1.14%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 148（MaxPain，仅结算参考）；上方 160（Call Wall，弱结构）。
• Gamma 区域：切换参考 148（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C +0 / P +0 ｜ Activity LOW ｜ 3D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 10D
10-16  C +0 / P +0 ｜ Activity LOW ｜ 17D
10-23  C +0 / P +0 ｜ Activity LOW ｜ 24D

📆 10-02 Forward Structure
存量OI: C 180.9k / P 188.6k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $2.88 / P $2.54 ｜ ATM IV 50.3%，净 delta 敞口 0 shares
仓位参考: Max Pain 148 ｜ Call Wall 160（+7.2%，弱）（OI 21.8k） ｜ Put Wall 140（-6.2%，弱）（OI 19.0k）
量化解读： 存量两侧均衡｜ATM IV 50.3%｜历史 Rank 25%（近端代理）｜IV/RV 1.32×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-09（Activity LOW）仓位参考: Max Pain 148 ｜ Call Wall 155（+3.9%，弱）（OI 5.1k） ｜ Put Wall 135（-9.5%）（OI 5.4k）

10-16（Activity LOW）仓位参考: Max Pain 142 ｜ Call Wall 160（+7.2%，弱）（OI 35.2k） ｜ Put Wall 135（-9.5%，弱）（OI 30.6k）

10-23（Activity LOW）仓位参考: Max Pain 149 ｜ Call Wall 150（+0.5%）（OI 3.3k） ｜ Put Wall 135（-9.5%，弱）（OI 2.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-29/SPCX_evening.json