# 期权晨报 2026-11-25（快照 10:20 ET）

📊 市场环境

SPY $701.98 ｜ QQQ $610.48
VIX 31.62 ↑19.9%（5D +28.8%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 9.1（extreme fear）
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


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 6.68 → 今开 6.28（-6.0%） | 较昨收变动（含盘初走势） ｜ 今日高 6.29 ｜ 低 6.01

Options: P/C成交量 0.19 | OI比 0.23 | ATM IV 119.8% | Skew 20.8pp | Term 0.93 | ExpMove ±18.1%（近端） | Rank 56%
量化视角： IV 中性（Rank 56%）｜期限结构正常（Term 0.93）｜保护溢价显著（Skew 20.8pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.23）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.19×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.23×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（2D）±18.1% ｜ 12-04（9D）±21.4% ｜ 12-11（16D）±25.8% ｜ 12-18（23D）±28.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) -917,469 | GEX Change vs 上次快照 -1,142,245 | Flip: Primary Flip: 6.61（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 217 / LOW 90 / INVALID 109
结构观察区: Primary Flip 6.61（全链重定价，覆盖 99%）
最近结构参考: Flip 7（现价低于该位 6.1%）
量化视角： 负 Gamma（92万，无历史分位）｜由正转负（114万）｜现价位于 Flip 下方 6.15%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 8（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 7（全链重定价，覆盖 99%）。
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
存量OI: C 22.7k / P 5.2k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $1.05 / P $0.07 ｜ ATM IV 119.8%，净 delta 敞口 0 shares
仓位参考: Max Pain 8 ｜ Put Wall 6.5（+4.8%，弱）（OI 0.9k）
量化解读： 存量 Call 重｜ATM IV 119.8%｜历史 Rank 56%（近端代理）｜IV/RV 1.12×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

12-04（Activity LOW）仓位参考: Max Pain 8 ｜ Put Wall 6（-3.3%，弱）（OI 0.2k）

12-11（Activity LOW）仓位参考: Max Pain 8 ｜ Put Wall 6（-3.3%，弱）（OI 0.1k）

12-18（Activity LOW）仓位参考: Max Pain 10

📅 事件差分（观察，非因果）: 11-27（2D）ATM IV 119.8% vs 12-04 114.0%（差 +5.8pp）——覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-25/USAR_morning.json