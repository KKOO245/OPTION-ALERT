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
🟡 **事件差分**: 10-02 ATM IV 91.0% vs 10-09 79.5%（差 +11.5pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 272.82 → 收盘 291.25（+6.8%） ｜ 今日高 302.35 ｜ 低 271.23 ｜ 昨收 262.87 → 收盘 291.25（+10.8%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.84 | OI比 1.26 | ATM IV 91.0% | Skew -5.5pp | Term 0.94 | ExpMove ±6.6%（近端） | Rank 53%
量化视角： IV 中性（Rank 53%）｜期限结构正常（Term 0.94）｜Put 保护异常便宜（Skew -5.5pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.84×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.26×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-02（3D）±6.6% ｜ 10-09（10D）±10.4% ｜ 10-16（17D）±13.5% ｜ 10-23（24D）±15.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 13,227,882 | GEX Change vs 上次快照 2,278,018 | Flip: Primary Flip: 266.15（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 612 / LOW 69 / INVALID 209
结构观察区: Primary Flip 266.15（全链重定价，覆盖 100%）
Call Wall 270（弱结构｜现价高于该位 7.9%）
最近结构参考: Call Wall 270（现价高于该位 7.9%）
量化视角： 正 Gamma（1323万，无历史分位）｜正 Gamma 增强（+228万）｜现价位于 Flip 上方 9.43%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 270（MaxPain，仅结算参考） / 270（Call Wall，弱结构）。
• Gamma 区域：切换参考 266（全链重定价，覆盖 100%）。
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
存量OI: C 36.9k / P 46.6k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $10.15 / P $8.98 ｜ ATM IV 91.0%，净 delta 敞口 0 shares
仓位参考: Max Pain 270 ｜ Call Wall 300（+3.0%）（OI 4.0k） ｜ Put Wall 290（-0.4%，弱）（OI 1.6k）
量化解读： 存量 Put 重｜ATM IV 91.0%｜历史 Rank 53%（近端代理）｜IV/RV 1.14×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-09（Activity LOW）仓位参考: Max Pain 260 ｜ Call Wall 300（+3.0%，弱）（OI 0.7k）

10-16（Activity LOW）仓位参考: Max Pain 260 ｜ Call Wall 270（-7.3%，弱）（OI 9.2k） ｜ Put Wall 270（-7.3%，弱）（OI 1.7k）

10-23（Activity LOW）仓位参考: Max Pain 250 ｜ Call Wall 280（-3.9%，弱）（OI 0.9k）

📅 事件差分（观察，非因果）: 10-02（3D）ATM IV 91.0% vs 10-09 79.5%（差 +11.5pp）——覆盖 职位空缺(JOLTS) Job Openings、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-29/BE_evening.json