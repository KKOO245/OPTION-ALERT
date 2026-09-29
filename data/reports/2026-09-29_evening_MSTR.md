# 期权晚报 2026-09-29（快照 16:40 ET）

📊 市场环境

SPY $764.20 ｜ QQQ $737.93
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
🟡 **事件差分**: 10-02 ATM IV 77.3% vs 10-09 66.1%（差 +11.2pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-02 160C ΔOI +1,928（距现价 +3.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 161.45 → 收盘 154.67（-4.2%） ｜ 今日高 161.62 ｜ 低 152.34 ｜ 昨收 157.14 → 收盘 154.67（-1.6%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.63 | OI比 0.82 | ATM IV 77.3% | Skew -5.0pp | Term 0.84 | ExpMove ±5.6%（近端） | Rank 43%
量化视角： IV 中性（Rank 43%）｜期限结构倒挂（Term 0.84，近月 IV 高于远月）｜Put 保护异常便宜（Skew -5.0pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.82）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.63×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.82×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-02（3D）±5.6% ｜ 10-09（10D）±8.9% ｜ 10-16（17D）±11.2% ｜ 10-23（24D）±13.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 38,709,792 | GEX Change vs 上次快照 -11,167,143 | Flip: Primary Flip: 146.07（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 729 / LOW 66 / INVALID 247
结构观察区: Primary Flip 146.07（全链重定价，覆盖 99%）
Call Wall 170（弱结构｜现价低于该位 9.0%）
最近结构参考: Flip 146（现价高于该位 5.9%）
量化视角： 正 Gamma（3871万，无历史分位）｜正 Gamma 减弱（1117万）｜现价位于 Flip 上方 5.89%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 155（MaxPain，仅结算参考） / 170（Call Wall，弱结构）。
• Gamma 区域：切换参考 146（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C +9.5k / P +7.9k ｜ Activity MEDIUM △ ｜ 3D
10-09  C +0.4k / P +4.1k ｜ Activity HIGH ｜ 10D
10-16  C +1.0k / P +1.1k ｜ Activity MEDIUM △ ｜ 17D
10-23  C +1.6k / P +2.5k ｜ Activity HIGH ｜ 24D

📆 10-02 Forward Structure
存量OI: C 239.5k / P 195.5k，今日变化ΔOI: C +9.5k / P +7.9k，平值价格ATM: C $4.20 / P $4.50 ｜ ATM IV 77.3%，净 delta 敞口 -32k shares
Top ΔOI: C 160 +1,928 ｜ C 165 +1,830
仓位参考: Max Pain 155 ｜ Call Wall 170（+9.9%，弱）（OI 44.9k） ｜ Put Wall 150（-3.0%，弱）（OI 12.4k）
量化解读： 存量 Call 重｜ATM IV 77.3%｜历史 Rank 43%（近端代理）｜IV/RV 1.00×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 31,611 股

📆 10-09 Forward Structure
存量OI: C 38.3k / P 54.2k，今日变化ΔOI: C +0.4k / P +4.1k，平值价格ATM: C $6.70 / P $7.02 ｜ ATM IV 66.1%，净 delta 敞口 -225k shares
Top ΔOI: C 144 -2,619 ｜ C 165 +852
仓位参考: Max Pain 147 ｜ Call Wall 165（+6.7%，弱）（OI 5.0k） ｜ Put Wall 155（+0.2%，弱）（OI 1.9k）
量化解读： 存量 Put 重｜ATM IV 66.1%｜历史 Rank 43%（近端代理）｜IV/RV 0.86×（近似）｜净 delta 敞口 负 225,477 股

10-16（MEDIUM △）Top ΔOI: 175C +454 ｜ 160C +392
10-16（MEDIUM △）仓位参考: Max Pain 120 ｜ Call Wall 155（+0.2%，弱）（OI 10.4k） ｜ Put Wall 140（-9.5%，弱）（OI 5.4k）

📆 10-23 Forward Structure
存量OI: C 15.9k / P 23.3k，今日变化ΔOI: C +1.6k / P +2.5k，平值价格ATM: C $9.90 / P $10.56 ｜ ATM IV 66.7%，净 delta 敞口 -20k shares
Top ΔOI: C 180 +482 ｜ C 170 +469
仓位参考: Max Pain 158 ｜ Call Wall 170（+9.9%，弱）（OI 1.5k） ｜ Put Wall 155（+0.2%，弱）（OI 2.0k）
量化解读： 存量 Put 重｜ATM IV 66.7%｜历史 Rank 43%（近端代理）｜IV/RV 0.87×（近似）｜净 delta 敞口 负 20,007 股

📅 事件差分（观察，非因果）: 10-02（3D）ATM IV 77.3% vs 10-09 66.1%（差 +11.2pp）——覆盖 职位空缺(JOLTS) Job Openings、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-29/MSTR_evening.json