# 期权晨报 2026-11-24（快照 10:20 ET）

📊 市场环境

SPY $717.83 ｜ QQQ $636.76
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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 416.23 → 今开 413.43（-0.7%） | 较昨收变动（含盘初走势） ｜ 今日高 429.80 ｜ 低 410.50

Options: P/C成交量 0.14 | OI比 0.60 | ATM IV 35.2% | Skew 3.6pp | Term 0.96 | ExpMove ±3.3%（近端） | Rank 22%
量化视角： IV 历史低位（Rank 22%，期权偏便宜）｜期限结构正常（Term 0.96）｜保护溢价中性（Skew 3.6pp）｜存量 Call 偏重（OI比 0.60）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.14×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.60×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（3D）±3.3% ｜ 12-04（10D）±4.1% ｜ 12-11（17D）±0.0% ｜ 12-18（24D）±0.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,824,486 | GEX Change vs 上次快照 741,677 | Flip: Primary Flip: 399.74（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 243 / LOW 170 / INVALID 571
结构观察区: Primary Flip 399.74（全链重定价，覆盖 95%）
Call Wall 400（弱结构｜现价高于该位 7.2%）
最近结构参考: Call Wall 400（现价高于该位 7.2%）
量化视角： 正 Gamma（182万，无历史分位）｜正 Gamma 增强（+74万）｜现价位于 Flip 上方 7.25%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 410（MaxPain，仅结算参考） / 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 400（全链重定价，覆盖 95%）。
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
存量OI: C 1.3k / P 0.8k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $1.64 / P $12.37 ｜ ATM IV 35.2%，净 delta 敞口 0 shares
仓位参考: Max Pain 410 ｜ Call Wall 410（-4.4%，弱）（OI 0.2k） ｜ Put Wall 395（-7.9%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 35.2%｜历史 Rank 22%（近端代理）｜IV/RV 0.77×（近似）｜净 delta 敞口 正 0 股

12-04（Activity LOW）仓位参考: Max Pain 420 ｜ Call Wall 450（+5.0%，弱）（OI 46） ｜ Put Wall 405（-5.5%，弱）（OI 29）

12-11（Activity LOW）仓位参考: Max Pain 435 ｜ Call Wall 450（+5.0%）（OI 0.1k） ｜ Put Wall 435（+1.5%）（OI 36）

12-18（Activity LOW）仓位参考: Max Pain 410 ｜ Call Wall 400（-6.7%，弱）（OI 1.5k） ｜ Put Wall 420（-2.0%，弱）（OI 0.6k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-24/ISRG_morning.json