# 期权晚报 2026-11-25（快照 21:00 ET）

📊 市场环境

SPY $716.70 ｜ QQQ $633.93
VIX 28.29 ↑7.3%（5D +15.2%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 15.2（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-25

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-25 08:30　【高】Personal Spending MoM　预测 0.4 ｜ 实际 0.3 ｜ 前值 0.6　✅ 今日已公布
- 周三 11-25 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周三 11-25 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 0.7 ｜ 前值 0.3　✅ 今日已公布
- 周三 11-25 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 3.5 ｜ 实际 4.3 ｜ 前值 1.5　✅ 今日已公布
- 周三 11-25 08:30　【高】耐用品订单 Orders MoM　预测 0.6 ｜ 实际 0.2 ｜ 前值 1.8　✅ 今日已公布

🔍 重点速览
🔴 **事件差分**: 11-27（2D）ATM IV 68.8% vs 11-30 50.7%（差 +18.2pp），覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 370.23 → 收盘 380.14（+2.7%） ｜ 今日高 383.73 ｜ 低 357.64 ｜ 昨收 384.68 → 收盘 380.14（-1.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.98 | OI比 1.45 | ATM IV 59.9% | Skew 6.8pp | Term 0.92 | ExpMove ±0.0%（近端） | Rank 70%
量化视角： IV 中性（Rank 70%）｜期限结构正常（Term 0.92）｜保护溢价显著（Skew 6.8pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.98×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.45×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-27（2D）±0.0% ｜ 11-30（5D）±4.6% ｜ 12-02（7D）±6.0% ｜ 12-04（9D）±0.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 48,095,567 | GEX Change vs 上次快照 51,343,149 | Flip: Primary Flip: 365.86（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1222 / LOW 216 / INVALID 818
结构观察区: Primary Flip 365.86（全链重定价，覆盖 100%）
最近结构参考: Flip 366（现价高于该位 3.9%）
量化视角： 正 Gamma（4810万，无历史分位）｜由负转正（+5134万）｜现价位于 Flip 上方 3.90%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 368（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 366（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-27  C +0 / P +0 ｜ Activity LOW ｜ 2D
11-30  C +0 / P +0 ｜ Activity LOW ｜ 5D
12-02  C +0 / P +0 ｜ Activity LOW ｜ 7D
12-04  C +0 / P +0 ｜ Activity LOW ｜ 9D

📆 11-27 Forward Structure
存量OI: C 150.1k / P 218.2k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $0.00 / P $0.00 ｜ ATM IV 68.8%，净 delta 敞口 0 shares
仓位参考: Max Pain 368 ｜ Call Wall 410（+7.9%，弱）（OI 10.2k）
量化解读： 存量 Put 重｜ATM IV 68.8%｜历史 Rank 70%（近端代理）｜IV/RV 0.95×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-30（Activity LOW）仓位参考: Max Pain 388 ｜ Put Wall 392.5（+3.3%，弱）（OI 1.5k）

12-02（Activity LOW）仓位参考: Max Pain 372 ｜ Call Wall 372.5（-2.0%，弱）（OI 0.8k） ｜ Put Wall 352.5（-7.3%）（OI 4.2k）

12-04（Activity LOW）仓位参考: Max Pain 378 ｜ Call Wall 400（+5.2%）（OI 7.0k） ｜ Put Wall 350（-7.9%，弱）（OI 2.3k）

📅 事件差分（观察，非因果）: 11-27（2D）ATM IV 68.8% vs 11-30 50.7%（差 +18.2pp）——覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-25/TSLA_evening.json