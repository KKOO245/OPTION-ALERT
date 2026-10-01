# 期权晚报 2026-09-30（快照 21:00 ET）

📊 市场环境

SPY $762.63 ｜ QQQ $nan
VIX 16.34 ↑1.9%（5D +7.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 30.8（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-30

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.2 ｜ 前值 0.1　✅ 今日已公布
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 2.2 ｜ 前值 2.5　✅ 今日已公布
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 0.9 ｜ 前值 0.1　✅ 今日已公布
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **事件差分**: 10-02 ATM IV 50.1% vs 10-05 38.5%（差 +11.6pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 351.79 → 收盘 354.81（+0.9%） ｜ 今日高 355.22 ｜ 低 345.88 ｜ 昨收 352.84 → 收盘 354.81（+0.6%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.52 | OI比 1.03 | ATM IV 50.1% | Skew -2.7pp | Term 0.91 | ExpMove ±3.0%（近端） | Rank 45%
量化视角： IV 中性（Rank 45%）｜期限结构正常（Term 0.91）｜Put 保护异常便宜（Skew -2.7pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.52×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.03×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-02（2D）±3.0% ｜ 10-05（5D）±3.6% ｜ 10-07（7D）±4.4% ｜ 10-09（9D）±5.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 27,600,873 | GEX Change vs 上次快照 38,319,179 | Flip: Primary Flip: 350.95（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1093 / LOW 108 / INVALID 659
结构观察区: Primary Flip 350.95（全链重定价，覆盖 100%）
最近结构参考: Flip 351（现价高于该位 1.1%）
量化视角： 正 Gamma（2760万，无历史分位）｜由负转正（+3832万）｜现价位于 Flip 上方 1.10%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 360（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 351（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C +0 / P +0 ｜ Activity LOW ｜ 2D
10-05  C +0 / P +0 ｜ Activity LOW ｜ 5D
10-07  C +0 / P +0 ｜ Activity LOW ｜ 7D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 9D

📆 10-02 Forward Structure
存量OI: C 246.5k / P 254.1k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $5.25 / P $5.40 ｜ ATM IV 50.1%，净 delta 敞口 0 shares
仓位参考: Max Pain 360 ｜ Call Wall 390（+9.9%，弱）（OI 16.6k） ｜ Put Wall 350（-1.4%，弱）（OI 7.0k）
量化解读： 存量两侧均衡｜ATM IV 50.1%｜历史 Rank 45%（近端代理）｜IV/RV 1.83×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-05（Activity LOW）仓位参考: Max Pain 360 ｜ Call Wall 390（+9.9%，弱）（OI 6.4k） ｜ Put Wall 325（-8.4%，弱）（OI 1.4k）

10-07（Activity LOW）仓位参考: Max Pain 360 ｜ Call Wall 375（+5.7%，弱）（OI 1.1k） ｜ Put Wall 360（+1.5%，弱）（OI 0.5k）

10-09（Activity LOW）仓位参考: Max Pain 360 ｜ Call Wall 370（+4.3%，弱）（OI 3.7k） ｜ Put Wall 350（-1.4%，弱）（OI 1.8k）

📅 事件差分（观察，非因果）: 10-02（2D）ATM IV 50.1% vs 10-05 38.5%（差 +11.6pp）——覆盖 PCE 物价 Price Index MoM、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-30/TSLA_evening.json