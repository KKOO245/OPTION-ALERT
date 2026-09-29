# 期权晚报 2026-09-29（快照 16:40 ET）

📊 市场环境

SPY $764.20 ｜ QQQ $737.93
VIX 16.04 ↓0.2%（5D +12.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-29

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-29 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.23 ｜ 实际 7.079 ｜ 前值 7.335　✅ 今日已公布
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 待公布 ｜ 前值 2.1
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 197.41 → 收盘 190.02（-3.7%） ｜ 今日高 197.63 ｜ 低 188.15 ｜ 昨收 191.79 → 收盘 190.02（-0.9%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.51 | OI比 0.60 | ATM IV 72.4% | Skew -4.1pp | Term 0.88 | ExpMove ±5.3%（近端） | Rank 38%
量化视角： IV 中性（Rank 38%）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜Put 保护异常便宜（Skew -4.1pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.60）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.51×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.60×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（3D）±5.3% ｜ 10-09（10D）±8.6% ｜ 10-16（17D）±10.7% ｜ 10-23（24D）±12.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 16,327,679 | GEX Change vs 上次快照 -4,399,172 | Flip: Primary Flip: 177.96（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 515 / LOW 118 / INVALID 251
结构观察区: Primary Flip 177.96（全链重定价，覆盖 100%）
Call Wall 202（弱结构｜现价低于该位 6.2%）
最近结构参考: Call Wall 202（现价低于该位 6.2%）
量化视角： 正 Gamma（1633万，无历史分位）｜正 Gamma 减弱（440万）｜现价位于 Flip 上方 6.78%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 190（MaxPain，仅结算参考）；上方 202（Call Wall，弱结构）。
• Gamma 区域：切换参考 178（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C +5.5k / P +2.5k ｜ Activity HIGH ｜ 3D
10-09  C +1.1k / P +1.1k ｜ Activity HIGH ｜ 10D
10-16  C +0.5k / P +0.9k ｜ Activity HIGH ｜ 17D
10-23  C +0.6k / P +0.6k ｜ Activity HIGH ｜ 24D

📆 10-02 Forward Structure
存量OI: C 71.3k / P 42.9k，今日变化ΔOI: C +5.5k / P +2.5k，平值价格ATM: C $5.10 / P $4.95 ｜ ATM IV 72.4%，净 delta 敞口 43k shares
Top ΔOI: C 205 +709
仓位参考: Max Pain 190 ｜ Call Wall 202.5（+6.6%，弱）（OI 16.1k） ｜ Put Wall 190（-0.0%，弱）（OI 1.9k）
量化解读： 存量 Call 重｜ATM IV 72.4%｜历史 Rank 38%（近端代理）｜IV/RV 0.96×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 42,668 股

📆 10-09 Forward Structure
存量OI: C 8.7k / P 21.0k，今日变化ΔOI: C +1.1k / P +1.1k，平值价格ATM: C $8.07 / P $8.33 ｜ ATM IV 62.5%，净 delta 敞口 14k shares
Top ΔOI: C 200 +364
仓位参考: Max Pain 190 ｜ Call Wall 200（+5.3%）（OI 1.8k）
量化解读： 存量 Put 重｜ATM IV 62.5%｜历史 Rank 38%（近端代理）｜IV/RV 0.83×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 14,001 股

📆 10-16 Forward Structure
存量OI: C 83.1k / P 74.5k，今日变化ΔOI: C +0.5k / P +0.9k，平值价格ATM: C $10.30 / P $10.00 ｜ ATM IV 61.9%，净 delta 敞口 -12k shares
Top ΔOI: P 180 +265
仓位参考: Max Pain 175 ｜ Call Wall 200（+5.3%，弱）（OI 6.3k） ｜ Put Wall 200（+5.3%，弱）（OI 3.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 61.9%｜历史 Rank 38%（近端代理）｜IV/RV 0.82×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 12,121 股

📆 10-23 Forward Structure
存量OI: C 5.1k / P 4.9k，今日变化ΔOI: C +0.6k / P +0.6k，平值价格ATM: C $11.80 / P $12.40 ｜ ATM IV 61.8%，净 delta 敞口 7k shares
Top ΔOI: C 187 +355 ｜ P 192 +349
仓位参考: Max Pain 190 ｜ Call Wall 187.5（-1.3%，弱）（OI 0.4k） ｜ Put Wall 192.5（+1.3%，弱）（OI 0.4k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 61.8%｜历史 Rank 38%（近端代理）｜IV/RV 0.82×（近似）｜净 delta 敞口 正 7,141 股

📅 事件差分（观察，非因果）: 10-02（3D）ATM IV 72.4% vs 10-09 62.5%（差 +9.9pp）——覆盖 职位空缺(JOLTS) Job Openings、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-29/COIN_evening.json