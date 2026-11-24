# 期权晚报 2026-11-24（快照 16:40 ET）

📊 市场环境

SPY $718.78 ｜ QQQ $638.10
VIX 26.36 ↓1.0%（5D +3.5%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 17.4（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-24

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-25 08:30　【高】Personal Spending MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.5
- 周三 11-25 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 11-25 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 11-25 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 3.5 ｜ 实际 待公布 ｜ 前值 1.5
- 周三 11-25 08:30　【高】耐用品订单 Orders MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 1.8

🔍 重点速览
🔴 **事件差分**: 11-25（1D）ATM IV 61.6% vs 11-27 1.6%（差 +60.0pp），覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 11-25 400C ΔOI +2,287（距现价 +4.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-25 275P ΔOI +10,067 占该期限总 OI 13.5%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 383.89 → 收盘 384.68（+0.2%） ｜ 今日高 390.09 ｜ 低 375.50 ｜ 昨收 385.46 → 收盘 384.68（-0.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.96 | OI比 1.09 | ATM IV 61.6% | Skew 9.1pp | Term 0.99 | ExpMove ±2.6%（近端） | Rank 72%
量化视角： IV 中性（Rank 72%）｜期限结构正常（Term 0.99）｜保护溢价显著（Skew 9.1pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.96×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.09×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-25（1D）±2.6% ｜ 11-27（3D）±0.1% ｜ 11-30（6D）±4.7% ｜ 12-02（8D）±6.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 60,935,998 | GEX Change vs 上次快照 -4,288,646 | Flip: Primary Flip: 364.68（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1273 / LOW 208 / INVALID 843
结构观察区: Primary Flip 364.68（全链重定价，覆盖 100%）
Call Wall 400（弱结构｜现价低于该位 3.8%）
最近结构参考: Call Wall 400（现价低于该位 3.8%）
量化视角： 正 Gamma（6094万，无历史分位）｜正 Gamma 减弱（429万）｜现价位于 Flip 上方 5.49%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 380（MaxPain，仅结算参考）；上方 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 365（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-25  C +21.7k / P +25.3k ｜ Activity HIGH ｜ 1D
11-27  C +25.0k / P +27.7k ｜ Activity HIGH ｜ 3D
11-30  C +1.0k / P +0.2k ｜ Activity MEDIUM △ ｜ 6D
12-02  C +1.4k / P +1.0k ｜ Activity HIGH ｜ 8D

📆 11-25 Forward Structure
存量OI: C 35.5k / P 38.8k，今日变化ΔOI: C +21.7k / P +25.3k，平值价格ATM: C $4.90 / P $4.99 ｜ ATM IV 61.6%，净 delta 敞口 -34k shares
Top ΔOI: C 415 +2,995 ｜ C 400 +2,287
仓位参考: Max Pain 380 ｜ Call Wall 400（+4.0%，弱）（OI 3.5k）
量化解读： 存量两侧均衡｜ATM IV 61.6%｜历史 Rank 72%（近端代理）｜IV/RV 0.85×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 34,478 股

📆 11-27 Forward Structure
存量OI: C 143.0k / P 207.1k，今日变化ΔOI: C +25.0k / P +27.7k，平值价格ATM: C $0.00 / P $0.42 ｜ ATM IV 1.6%，净 delta 敞口 -130k shares
Top ΔOI: C 415 +5,901 ｜ C 420 +3,816
仓位参考: Max Pain 365 ｜ Call Wall 410（+6.6%，弱）（OI 9.8k）
量化解读： 存量 Put 重｜ATM IV 1.6%｜历史 Rank 72%（近端代理）｜IV/RV 0.02×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 129,922 股

11-30（MEDIUM △）Top ΔOI: 420C -3,302 ｜ 395P -1,421
11-30（MEDIUM △）仓位参考: Max Pain 392 ｜ Call Wall 420（+9.2%）（OI 8.0k） ｜ Put Wall 392.5（+2.0%，弱）（OI 1.5k）

📆 12-02 Forward Structure
存量OI: C 4.5k / P 3.3k，今日变化ΔOI: C +1.4k / P +1.0k，平值价格ATM: C $11.65 / P $11.80 ｜ ATM IV 50.8%，净 delta 敞口 -854 shares
Top ΔOI: C 420 +253
仓位参考: Max Pain 372 ｜ Call Wall 420（+9.2%，弱）（OI 0.4k） ｜ Put Wall 380（-1.2%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 50.8%｜历史 Rank 72%（近端代理）｜IV/RV 0.70×（近似）｜净 delta 敞口 负 854 股

📅 事件差分（观察，非因果）: 11-25（1D）ATM IV 61.6% vs 11-27 1.6%（差 +60.0pp）——覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-24/TSLA_evening.json