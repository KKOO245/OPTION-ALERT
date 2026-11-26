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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 34.55 → 收盘 35.30（+2.2%） ｜ 今日高 35.58 ｜ 低 33.04 ｜ 昨收 35.91 → 收盘 35.30（-1.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.11 | OI比 0.51 | ATM IV 79.0% | Skew 8.9pp | Term 0.89 | ExpMove ±6.5%（近端） | Rank 70%
量化视角： IV 中性（Rank 70%）｜期限结构倒挂（Term 0.89，近月 IV 高于远月）｜保护溢价显著（Skew 8.9pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.51）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.11×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.51×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（2D）±6.5% ｜ 12-04（9D）±10.9% ｜ 12-11（16D）±6.6% ｜ 12-18（23D）±14.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 494,593 | GEX Change vs 上次快照 1,418,116 | Flip: Primary Flip: 35.07（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 245 / LOW 63 / INVALID 190
结构观察区: Primary Flip 35.07（全链重定价，覆盖 100%）
Put Wall 35（弱结构｜现价高于该位 0.9%）
最近结构参考: Flip 35（现价高于该位 0.7%）
量化视角： 正 Gamma（49万，无历史分位）｜由负转正（+142万）｜现价位于 Flip 上方 0.67%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 35（Put Wall，弱结构）；上方 37（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 35（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-27  C +0 / P +0 ｜ Activity LOW ｜ 2D
12-04  C +0 / P +0 ｜ Activity LOW ｜ 9D
12-11  C +0 / P +0 ｜ Activity LOW ｜ 16D
12-18  C +0 / P +0 ｜ Activity LOW ｜ 23D

📆 11-27 Forward Structure
存量OI: C 12.6k / P 6.5k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $1.20 / P $1.10 ｜ ATM IV 79.0%，净 delta 敞口 0 shares
仓位参考: Max Pain 37 ｜ Put Wall 33（-6.5%）（OI 2.6k）
量化解读： 存量 Call 重｜ATM IV 79.0%｜历史 Rank 70%（近端代理）｜IV/RV 1.22×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

12-04（Activity LOW）仓位参考: Max Pain 36 ｜ Call Wall 35（-0.8%，弱）（OI 0.6k） ｜ Put Wall 34（-3.7%，弱）（OI 0.2k）

12-11（Activity LOW）仓位参考: Max Pain 38 ｜ Call Wall 38（+7.6%，弱）（OI 0.8k）

12-18（Activity LOW）仓位参考: Max Pain 45 ｜ Put Wall 35（-0.8%，弱）（OI 6.0k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-25/MP_evening.json