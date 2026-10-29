# 期权晚报 2026-10-29（快照 16:40 ET）

📊 市场环境

SPY $769.36 ｜ QQQ $715.34
VIX 17.20 ↑1.7%（5D -9.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-29

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 3.4 ｜ 前值 2.2　✅ 今日已公布
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 0.5 ｜ 前值 0.9　✅ 今日已公布
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-30 10P ΔOI -324（距现价 -4.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 10.15 → 收盘 10.52（+3.6%） ｜ 今日高 10.89 ｜ 低 10.08 ｜ 昨收 10.48 → 收盘 10.52（+0.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.30 | OI比 0.35 | ATM IV 94.1% | Skew 5.7pp | Term 0.94 | ExpMove ±3.9%（近端） | Rank 28%
量化视角： IV 中性（Rank 28%）｜期限结构正常（Term 0.94）｜保护溢价中性（Skew 5.7pp）｜存量 Call 偏重（OI比 0.35）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.30×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.35×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（1D）±3.9% ｜ 11-06（8D）±10.5% ｜ 11-13（15D）±15.5% ｜ 11-20（22D）±18.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 6,460,439 | GEX Change vs 上次快照 354,855 | Flip: Primary Flip: 9.57（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 225 / LOW 71 / INVALID 124
结构观察区: Primary Flip 9.57（全链重定价，覆盖 95%）
Put Wall 10（弱结构｜现价高于该位 5.2%） | Call Wall 11（弱结构｜现价低于该位 4.4%）
最近结构参考: Call Wall 11（现价低于该位 4.4%）
量化视角： 正 Gamma（646万，无历史分位）｜正 Gamma 增强（+35万）｜现价位于 Flip 上方 9.93%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 10（Put Wall，弱结构） / 10（MaxPain，仅结算参考）；上方 11（Call Wall，弱结构）。
• Gamma 区域：切换参考 10（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-30  C +0.2k / P -0.5k ｜ Activity MEDIUM △ ｜ 1D
11-06  C +0.4k / P +1.0k ｜ Activity HIGH ｜ 8D
11-13  C +0.4k / P +12 ｜ Activity HIGH ｜ 15D
11-20  C +0.5k / P -0.1k ｜ Activity HIGH ｜ 22D

📆 10-30 Forward Structure
存量OI: C 29.3k / P 10.4k，今日变化ΔOI: C +0.2k / P -0.5k，平值价格ATM: C $0.22 / P $0.19 ｜ ATM IV 94.1%，净 delta 敞口 9k shares
Top ΔOI: P 10 -324 ｜ C 10 +318 ｜ C 11 +202
仓位参考: Max Pain 10 ｜ Call Wall 10（-4.9%，弱）（OI 5.1k） ｜ Put Wall 10（-4.9%，弱）（OI 1.7k）
量化解读： 存量 Call 重｜ATM IV 94.1%｜历史 Rank 28%（近端代理）｜IV/RV 1.10×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 9,363 股

📆 11-06 Forward Structure
存量OI: C 8.5k / P 5.3k，今日变化ΔOI: C +0.4k / P +1.0k，平值价格ATM: C $0.58 / P $0.52 ｜ ATM IV 88.1%，净 delta 敞口 -8k shares
Top ΔOI: P 9 +1,051 ｜ C 11 +118
仓位参考: Max Pain 10 ｜ Call Wall 11（+4.6%，弱）（OI 1.0k） ｜ Put Wall 9.5（-9.7%，弱）（OI 1.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 88.1%｜历史 Rank 28%（近端代理）｜IV/RV 1.03×（近似）｜净 delta 敞口 负 7,744 股

📆 11-13 Forward Structure
存量OI: C 5.3k / P 2.7k，今日变化ΔOI: C +0.4k / P +12，平值价格ATM: C $0.87 / P $0.76 ｜ ATM IV 92.4%，净 delta 敞口 19k shares
Top ΔOI: C 11 +211 ｜ C 10 +106
仓位参考: Max Pain 10 ｜ Call Wall 11（+4.6%）（OI 1.1k） ｜ Put Wall 11（+4.6%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 92.4%｜历史 Rank 28%（近端代理）｜IV/RV 1.08×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 19,141 股

📆 11-20 Forward Structure
存量OI: C 32.0k / P 26.4k，今日变化ΔOI: C +0.5k / P -0.1k，平值价格ATM: C $0.99 / P $0.91 ｜ ATM IV 91.7%，净 delta 敞口 30k shares
Top ΔOI: C 11 +192 ｜ C 10 +163
仓位参考: Max Pain 13 ｜ Call Wall 11（+4.6%，弱）（OI 2.0k） ｜ Put Wall 10（-4.9%，弱）（OI 6.3k）
量化解读： 存量 Call 重｜ATM IV 91.7%｜历史 Rank 28%（近端代理）｜IV/RV 1.07×（近似）｜净 delta 敞口 正 30,458 股

📅 事件差分（观察，非因果）: 10-30（1D）ATM IV 94.1% vs 11-06 88.1%（差 +6.0pp）——覆盖 GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM、PCE 物价 Price Index MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-29/USAR_evening.json