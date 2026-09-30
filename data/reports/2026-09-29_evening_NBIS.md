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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 235.01 → 收盘 237.35（+1.0%） ｜ 今日高 246.98 ｜ 低 233.61 ｜ 昨收 231.88 → 收盘 237.35（+2.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.53 | OI比 0.73 | ATM IV 88.3% | Skew -1.3pp | Term 0.89 | ExpMove ±6.3%（近端） | Rank 23%
量化视角： IV 历史低位（Rank 23%，期权偏便宜）｜期限结构倒挂（Term 0.89，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.3pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.73）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.53×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.73×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（3D）±6.3% ｜ 10-09（10D）±10.6% ｜ 10-16（17D）±13.4% ｜ 10-23（24D）±16.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 11,806,136 | GEX Change vs 上次快照 61,805 | Flip: Primary Flip: 224.93（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 541 / LOW 27 / INVALID 130
结构观察区: Primary Flip 224.93（全链重定价，覆盖 100%）
最近结构参考: Flip 225（现价高于该位 5.5%）
量化视角： 正 Gamma（1181万，无历史分位）｜正 Gamma 增强（+6万）｜现价位于 Flip 上方 5.52%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 230（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 225（全链重定价，覆盖 100%）。
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
存量OI: C 57.8k / P 42.2k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $7.51 / P $7.54 ｜ ATM IV 88.3%，净 delta 敞口 0 shares
仓位参考: Max Pain 230 ｜ Call Wall 235（-1.0%）（OI 7.3k） ｜ Put Wall 220（-7.3%，弱）（OI 4.7k）
量化解读： 存量 Call 重｜ATM IV 88.3%｜历史 Rank 23%（近端代理）｜IV/RV 1.41×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-09（Activity LOW）仓位参考: Max Pain 222 ｜ Call Wall 240（+1.1%，弱）（OI 2.1k） ｜ Put Wall 225（-5.2%，弱）（OI 1.0k）

10-16（Activity LOW）仓位参考: Max Pain 220 ｜ Call Wall 240（+1.1%，弱）（OI 5.2k） ｜ Put Wall 220（-7.3%，弱）（OI 3.1k）

10-23（Activity LOW）仓位参考: Max Pain 230 ｜ Call Wall 240（+1.1%，弱）（OI 0.4k） ｜ Put Wall 215（-9.4%，弱）（OI 0.3k）

📅 事件差分（观察，非因果）: 10-02（3D）ATM IV 88.3% vs 10-09 78.5%（差 +9.8pp）——覆盖 职位空缺(JOLTS) Job Openings、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-29/NBIS_evening.json