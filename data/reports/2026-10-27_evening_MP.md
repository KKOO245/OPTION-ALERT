# 期权晚报 2026-10-27（快照 21:00 ET）

📊 市场环境

SPY $769.66 ｜ QQQ $nan
VIX 17.52 ↓4.7%（5D +1.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-27

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-27 08:30　【高】耐用品订单 Orders MoM　预测 1.5 ｜ 实际 1.8 ｜ 前值 0.1　✅ 今日已公布
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 4
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.9
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 38.28 → 收盘 40.87（+6.8%） ｜ 今日高 41.04 ｜ 低 38.00 ｜ 昨收 37.47 → 收盘 40.87（+9.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.32 | OI比 0.62 | ATM IV 72.4% | Skew 1.7pp | Term 0.85 | ExpMove ±5.5%（近端） | Rank 60%
量化视角： IV 中性（Rank 60%）｜期限结构倒挂（Term 0.85，近月 IV 高于远月）｜保护溢价薄（Skew 1.7pp）｜存量 Call 偏重（OI比 0.62）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.32×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.62×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（3D）±5.5% ｜ 11-06（10D）±9.7% ｜ 11-13（17D）±17.1% ｜ 11-20（24D）±13.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,323,056 | GEX Change vs 上次快照 983,345 | Flip: Primary Flip: 39.43（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 311 / LOW 60 / INVALID 155
结构观察区: Primary Flip 39.43（全链重定价，覆盖 100%）
最近结构参考: Flip 39（现价高于该位 3.7%）
量化视角： 正 Gamma（132万，无历史分位）｜正 Gamma 增强（+98万）｜现价位于 Flip 上方 3.66%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 42（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 39（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-30  C +0 / P +0 ｜ Activity LOW ｜ 3D
11-06  C +0 / P +0 ｜ Activity LOW ｜ 10D
11-13  C +0 / P +0 ｜ Activity LOW ｜ 17D
11-20  C +0 / P +0 ｜ Activity LOW ｜ 24D

📆 10-30 Forward Structure
存量OI: C 12.1k / P 7.5k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $1.05 / P $1.20 ｜ ATM IV 72.4%，净 delta 敞口 0 shares
仓位参考: Max Pain 42 ｜ Call Wall 40（-2.1%，弱）（OI 1.1k） ｜ Put Wall 44（+7.7%，弱）（OI 1.7k）
量化解读： 存量 Call 重｜ATM IV 72.4%｜历史 Rank 60%（近端代理）｜IV/RV 1.68×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-06（Activity LOW）仓位参考: Max Pain 42 ｜ Call Wall 43（+5.2%，弱）（OI 0.9k） ｜ Put Wall 38（-7.0%）（OI 0.9k）

11-13（Activity LOW）仓位参考: Max Pain 42 ｜ Put Wall 39（-4.6%）（OI 0.8k）

11-20（Activity LOW）仓位参考: Max Pain 45 ｜ Call Wall 40（-2.1%，弱）（OI 0.9k） ｜ Put Wall 40（-2.1%，弱）（OI 1.6k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-27/MP_evening.json