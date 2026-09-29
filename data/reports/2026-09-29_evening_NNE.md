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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 16.55 → 收盘 15.79（-4.6%） ｜ 今日高 16.60 ｜ 低 15.76 ｜ 昨收 16.16 → 收盘 15.79（-2.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.43 | OI比 0.46 | ATM IV 88.5% | Skew -2.9pp | Term 0.89 | ExpMove ±6.9%（近端） | Rank 18%
量化视角： IV 历史低位（Rank 18%，期权偏便宜）｜期限结构倒挂（Term 0.89，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.9pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.46）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.43×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.46×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（3D）±6.9% ｜ 10-09（10D）±11.5% ｜ 10-16（17D）±12.9% ｜ 10-23（24D）±16.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 635,825 | GEX Change vs 上次快照 -388,481 | Flip: Primary Flip: 15.11（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 173 / LOW 81 / INVALID 182
结构观察区: Primary Flip 15.11（全链重定价，覆盖 96%）
Put Wall 15（弱结构｜现价高于该位 5.3%）
最近结构参考: Flip 15（现价高于该位 4.5%）
量化视角： 正 Gamma（64万，无历史分位）｜正 Gamma 减弱（39万）｜现价位于 Flip 上方 4.51%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall，弱结构）；上方 17（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 15（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C +0.5k / P +0.4k ｜ Activity MEDIUM △ ｜ 3D
10-09  C +55 / P +0.2k ｜ Activity MEDIUM △ ｜ 10D
10-16  C +64 / P +36 ｜ Activity MEDIUM △ ｜ 17D
10-23  C +5 / P +0.1k ｜ Activity MEDIUM △ ｜ 24D

📆 10-02 Forward Structure
存量OI: C 5.1k / P 2.3k，今日变化ΔOI: C +0.5k / P +0.4k，平值价格ATM: C $0.50 / P $0.59 ｜ ATM IV 88.5%，净 delta 敞口 -7k shares
Top ΔOI: P 15 +202
仓位参考: Max Pain 17 ｜ Put Wall 15.5（-1.8%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 88.5%｜历史 Rank 18%（近端代理）｜IV/RV 1.21×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 7,470 股

10-09（MEDIUM △）Top ΔOI: 15P +275 ｜ 14P -137
10-09（MEDIUM △）仓位参考: Max Pain 18 ｜ Put Wall 15（-5.0%，弱）（OI 0.3k）

10-16（MEDIUM △）Top ΔOI: 16P +31
10-16（MEDIUM △）仓位参考: Max Pain 20 ｜ Put Wall 15（-5.0%，弱）（OI 0.8k）

10-23（MEDIUM △）Top ΔOI: 17P +40 ｜ 16P +19
10-23（MEDIUM △）仓位参考: Max Pain 18 ｜ Put Wall 16（+1.3%）（OI 0.2k）

📅 事件差分（观察，非因果）: 10-02（3D）ATM IV 88.5% vs 10-09 80.1%（差 +8.5pp）——覆盖 职位空缺(JOLTS) Job Openings、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-29/NNE_evening.json