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


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 55.03 → 收盘 55.48（+0.8%） ｜ 今日高 55.49 ｜ 低 54.81 ｜ 昨收 54.95 → 收盘 55.48（+1.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.63 | OI比 0.40 | ATM IV 38.4% | Skew -0.1pp | Term 0.93 | ExpMove ±1.6%（近端） | Rank 63%
量化视角： IV 中性（Rank 63%）｜期限结构正常（Term 0.93）｜Put 保护异常便宜（Skew -0.1pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.40）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.63×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.40×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-30（1D）±1.6% ｜ 10-02（3D）±2.9% ｜ 10-05（6D）±3.4% ｜ 10-07（8D）±4.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 12,499,365 | GEX Change vs 上次快照 9,671,138 | Flip: Primary Flip: 55.17（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 739 / LOW 202 / INVALID 403
结构观察区: Primary Flip 55.17（全链重定价，覆盖 94%）
Put Wall 50（弱结构｜现价高于该位 11.0%） | Call Wall 60（弱结构｜现价低于该位 7.5%）
最近结构参考: Flip 55（现价高于该位 0.6%）
量化视角： 正 Gamma（1250万，无历史分位）｜正 Gamma 增强（+967万）｜现价位于 Flip 上方 0.56%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 50（Put Wall，弱结构） / 55（MaxPain，仅结算参考）；上方 60（Call Wall，弱结构）。
• Gamma 区域：切换参考 55（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-30  C +0 / P +0 ｜ Activity LOW ｜ 1D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 3D
10-05  C +0 / P +0 ｜ Activity LOW ｜ 6D
10-07  C +0 / P +0 ｜ Activity LOW ｜ 8D

📆 09-30 Forward Structure
存量OI: C 312.3k / P 123.6k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $0.44 / P $0.47 ｜ ATM IV 38.4%，净 delta 敞口 0 shares
仓位参考: Max Pain 55 ｜ Call Wall 60（+8.1%，弱）（OI 6.5k） ｜ Put Wall 53（-4.5%）（OI 13.8k）
量化解读： 存量 Call 重｜ATM IV 38.4%｜历史 Rank 63%（近端代理）｜IV/RV 1.01×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-02（Activity LOW）仓位参考: Max Pain 58 ｜ Call Wall 60（+8.1%，弱）（OI 11.2k） ｜ Put Wall 50（-9.9%）（OI 7.5k）

10-05（Activity LOW）仓位参考: Max Pain 58 ｜ Call Wall 58（+4.5%，弱）（OI 0.4k） ｜ Put Wall 59.5（+7.2%，弱）（OI 0.5k）

10-07（Activity LOW）仓位参考: Max Pain 57 ｜ Call Wall 59（+6.3%，弱）（OI 0.7k） ｜ Put Wall 57（+2.7%）（OI 1.8k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-29/SLV_evening.json