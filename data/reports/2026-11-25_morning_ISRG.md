# 期权晨报 2026-11-25（快照 10:20 ET）

📊 市场环境

SPY $701.98 ｜ QQQ $610.89
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


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 434.46 → 今开 426.27（-1.9%） | 较昨收变动（含盘初走势） ｜ 今日高 431.34 ｜ 低 419.54

Options: P/C成交量 0.14 | OI比 0.60 | ATM IV 35.2% | Skew 3.6pp | Term 0.98 | ExpMove ±3.3%（近端） | Rank 22%
量化视角： IV 历史低位（Rank 22%，期权偏便宜）｜期限结构正常（Term 0.98）｜保护溢价中性（Skew 3.6pp）｜存量 Call 偏重（OI比 0.60）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.14×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.60×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（2D）±3.3% ｜ 12-04（9D）±4.1% ｜ 12-11（16D）±0.0% ｜ 12-18（23D）±0.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,766,219 | GEX Change vs 上次快照 -376,140 | Flip: Primary Flip: 401.00（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 243 / LOW 170 / INVALID 571
结构观察区: Primary Flip 401.00（全链重定价，覆盖 95%）
Call Wall 400（弱结构｜现价高于该位 6.6%）
最近结构参考: Flip 401（现价高于该位 6.4%）
量化视角： 正 Gamma（177万，无历史分位）｜正 Gamma 减弱（38万）｜现价位于 Flip 上方 6.38%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 410（MaxPain，仅结算参考） / 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 401（全链重定价，覆盖 95%）。
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
存量OI: C 1.3k / P 0.8k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $1.64 / P $12.37 ｜ ATM IV 35.2%，净 delta 敞口 0 shares
仓位参考: Max Pain 410 ｜ Call Wall 410（-3.9%，弱）（OI 0.2k） ｜ Put Wall 395（-7.4%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 35.2%｜历史 Rank 22%（近端代理）｜IV/RV 0.73×（近似）｜净 delta 敞口 正 0 股

12-04（Activity LOW）仓位参考: Max Pain 420 ｜ Call Wall 450（+5.5%，弱）（OI 46） ｜ Put Wall 405（-5.1%，弱）（OI 29）

12-11（Activity LOW）仓位参考: Max Pain 435 ｜ Call Wall 450（+5.5%）（OI 0.1k） ｜ Put Wall 435（+2.0%）（OI 36）

12-18（Activity LOW）仓位参考: Max Pain 410 ｜ Call Wall 400（-6.2%，弱）（OI 1.5k） ｜ Put Wall 420（-1.5%，弱）（OI 0.6k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-25/ISRG_morning.json