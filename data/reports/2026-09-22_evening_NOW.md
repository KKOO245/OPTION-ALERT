# 期权晚报 2026-09-22（快照 16:40 ET）

📊 市场环境

SPY $773.38 ｜ QQQ $747.46
VIX 14.21 ↓4.4%（5D -17.4%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 35.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🟡 **近现价集中开仓**: 09-25 140C ΔOI +1,098（距现价 +2.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NOW

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NOW: 今开 141.83 → 收盘 137.00（-3.4%） ｜ 今日高 142.10 ｜ 低 135.25 ｜ 昨收 137.68 → 收盘 137.00（-0.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.29 | OI比 0.63 | ATM IV 58.1% | Skew -1.7pp | Term 0.96 | ExpMove ±4.3%（近端） | Rank 30%
量化视角： IV 中性（Rank 30%）｜期限结构正常（Term 0.96）｜Put 保护异常便宜（Skew -1.7pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.63）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.29×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.63×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（3D）±4.3% ｜ 10-02（10D）±7.3% ｜ 10-09（17D）±8.4% ｜ 10-16（24D）±10.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 10,227,782 | GEX Change vs 上次快照 914,094 | Flip: Primary Flip: 131.13（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 580 / LOW 35 / INVALID 111
结构观察区: Primary Flip 131.13（全链重定价，覆盖 100%）
Call Wall 150（现价低于该位 8.7%）
最近结构参考: Flip 131（现价高于该位 4.5%）
量化视角： 正 Gamma（1023万，无历史分位）｜正 Gamma 增强（+91万）｜现价位于 Flip 上方 4.48%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 136（MaxPain，仅结算参考）；上方 150（Call Wall）。
• Gamma 区域：切换参考 131（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +5.4k / P +2.1k ｜ Activity HIGH ｜ 3D
10-02  C +2.1k / P +1.0k ｜ Activity HIGH ｜ 10D
10-09  C +0.8k / P +0.9k ｜ Activity HIGH ｜ 17D
10-16  C +2.4k / P +2.3k ｜ Activity HIGH ｜ 24D

📆 09-25 Forward Structure
存量OI: C 30.0k / P 18.9k，今日变化ΔOI: C +5.4k / P +2.1k，平值价格ATM: C $3.23 / P $2.61 ｜ ATM IV 58.1%，净 delta 敞口 106k shares
Top ΔOI: C 140 +1,098 ｜ C 150 +982 ｜ C 145 +865
仓位参考: Max Pain 136 ｜ Call Wall 150（+9.5%，弱）（OI 6.1k） ｜ Put Wall 130（-5.1%，弱）（OI 1.5k）
量化解读： 存量 Call 重｜ATM IV 58.1%｜历史 Rank 30%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 106,216 股

📆 10-02 Forward Structure
存量OI: C 13.0k / P 11.2k，今日变化ΔOI: C +2.1k / P +1.0k，平值价格ATM: C $5.30 / P $4.65 ｜ ATM IV 55.0%，净 delta 敞口 34k shares
Top ΔOI: C 150 +451 ｜ C 145 +372
仓位参考: Max Pain 132 ｜ Call Wall 150（+9.5%）（OI 2.3k） ｜ Put Wall 130（-5.1%）（OI 1.1k）
量化解读： 存量两侧均衡｜ATM IV 55.0%｜历史 Rank 30%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 33,613 股

📆 10-09 Forward Structure
存量OI: C 5.0k / P 5.5k，今日变化ΔOI: C +0.8k / P +0.9k，平值价格ATM: C $6.55 / P $5.00 ｜ ATM IV 52.9%，净 delta 敞口 19k shares
Top ΔOI: P 128 +263 ｜ P 126 +262
仓位参考: Max Pain 136 ｜ Call Wall 150（+9.5%）（OI 1.0k） ｜ Put Wall 140（+2.2%，弱）（OI 0.5k）
量化解读： 存量两侧均衡｜ATM IV 52.9%｜历史 Rank 30%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 19,028 股

📆 10-16 Forward Structure
存量OI: C 68.1k / P 54.8k，今日变化ΔOI: C +2.4k / P +2.3k，平值价格ATM: C $7.67 / P $7.12 ｜ ATM IV 52.5%，净 delta 敞口 22k shares
Top ΔOI: C 140 +773 ｜ P 130 +754 ｜ P 127 +531
仓位参考: Max Pain 125 ｜ Call Wall 150（+9.5%）（OI 11.2k） ｜ Put Wall 130（-5.1%，弱）（OI 4.7k）
量化解读： 存量 Call 重｜ATM IV 52.5%｜历史 Rank 30%（近端代理）｜净 delta 敞口 正 22,135 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-22/NOW_evening.json