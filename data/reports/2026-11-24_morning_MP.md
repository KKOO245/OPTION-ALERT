# 期权晨报 2026-11-24（快照 10:20 ET）

📊 市场环境

SPY $717.83 ｜ QQQ $636.91
VIX 27.25 ↑2.4%（5D +7.0%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 17.0（extreme fear）
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
🟡 **事件差分**: 11-27 ATM IV 82.3% vs 12-04 71.6%（差 +10.7pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 35.54 → 今开 36.00（+1.3%） | 较昨收变动（含盘初走势） ｜ 今日高 36.85 ｜ 低 35.68

Options: P/C成交量 0.11 | OI比 0.51 | ATM IV 82.3% | Skew 8.9pp | Term 0.82 | ExpMove ±9.7%（近端） | Rank 74%
量化视角： IV 中性（Rank 74%）｜期限结构倒挂（Term 0.82，近月 IV 高于远月）｜保护溢价显著（Skew 8.9pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.51）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.11×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.51×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（3D）±9.7% ｜ 12-04（10D）±10.6% ｜ 12-11（17D）±0.0% ｜ 12-18（24D）±6.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,793,697 | GEX Change vs 上次快照 1,294,138 | Flip: Primary Flip: 34.50（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 245 / LOW 63 / INVALID 190
结构观察区: Primary Flip 34.50（全链重定价，覆盖 100%）
Put Wall 35（弱结构｜现价高于该位 3.9%）
最近结构参考: Put Wall 35（现价高于该位 3.9%）
量化视角： 正 Gamma（279万，无历史分位）｜正 Gamma 增强（+129万）｜现价位于 Flip 上方 5.36%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 35（Put Wall，弱结构）；上方 37（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 35（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-27  C +0 / P +0 ｜ Activity LOW ｜ 3D
12-04  C +0 / P +0 ｜ Activity LOW ｜ 10D
12-11  C +0 / P +0 ｜ Activity LOW ｜ 17D
12-18  C +0 / P +0 ｜ Activity LOW ｜ 24D

📆 11-27 Forward Structure
存量OI: C 12.6k / P 6.5k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $0.72 / P $2.82 ｜ ATM IV 82.3%，净 delta 敞口 0 shares
仓位参考: Max Pain 37 ｜ Put Wall 33（-9.2%）（OI 2.6k）
量化解读： 存量 Call 重｜ATM IV 82.3%｜历史 Rank 74%（近端代理）｜IV/RV 1.26×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

12-04（Activity LOW）仓位参考: Max Pain 36 ｜ Call Wall 35（-3.7%，弱）（OI 0.6k） ｜ Put Wall 34（-6.5%，弱）（OI 0.2k）

12-11（Activity LOW）仓位参考: Max Pain 38 ｜ Call Wall 38（+4.5%，弱）（OI 0.8k）

12-18（Activity LOW）仓位参考: Max Pain 45 ｜ Put Wall 35（-3.7%，弱）（OI 6.0k）

📅 事件差分（观察，非因果）: 11-27（3D）ATM IV 82.3% vs 12-04 71.6%（差 +10.7pp）——覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-24/MP_morning.json