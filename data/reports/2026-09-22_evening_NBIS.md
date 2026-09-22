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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 233.51 → 收盘 236.12（+1.1%） ｜ 今日高 246.61 ｜ 低 231.76 ｜ 昨收 232.80 → 收盘 236.12（+1.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.52 | OI比 0.86 | ATM IV 87.6% | Skew -2.5pp | Term 0.92 | ExpMove ±6.4%（近端） | Rank 20%
量化视角： IV 历史低位（Rank 20%，期权偏便宜）｜期限结构正常（Term 0.92）｜Put 保护异常便宜（Skew -2.5pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.52×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.86×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-25（3D）±6.4% ｜ 10-02（10D）±10.6% ｜ 10-09（17D）±14.1% ｜ 10-16（24D）±16.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 14,234,835 | GEX Change vs 上次快照 -2,924,794 | Flip: Primary Flip: 218.24（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 533 / LOW 36 / INVALID 157
结构观察区: Primary Flip 218.24（全链重定价，覆盖 98%）
最近结构参考: Flip 218（现价高于该位 8.2%）
量化视角： 正 Gamma（1423万，无历史分位）｜正 Gamma 减弱（292万）｜现价位于 Flip 上方 8.19%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 220（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 218（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +16.5k / P +8.6k ｜ Activity HIGH ｜ 3D
10-02  C +7.7k / P +1.7k ｜ Activity HIGH ｜ 10D
10-09  C +1.8k / P +1.1k ｜ Activity HIGH ｜ 17D
10-16  C +4.2k / P +2.2k ｜ Activity HIGH ｜ 24D

📆 09-25 Forward Structure
存量OI: C 60.5k / P 52.0k，今日变化ΔOI: C +16.5k / P +8.6k，平值价格ATM: C $8.20 / P $6.90 ｜ ATM IV 87.6%，净 delta 敞口 130k shares
Top ΔOI: C 250 +3,124 ｜ C 260 +2,352 ｜ P 220 +2,126
仓位参考: Max Pain 220 ｜ Call Wall 250（+5.9%，弱）（OI 6.6k） ｜ Put Wall 220（-6.8%）（OI 5.7k）
量化解读： 存量两侧均衡｜ATM IV 87.6%｜历史 Rank 20%（近端代理）｜IV/RV 1.51×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 129,750 股

📆 10-02 Forward Structure
存量OI: C 21.7k / P 16.7k，今日变化ΔOI: C +7.7k / P +1.7k，平值价格ATM: C $13.50 / P $11.60 ｜ ATM IV 81.6%，净 delta 敞口 107k shares
Top ΔOI: C 310 +3,333 ｜ C 250 +998
仓位参考: Max Pain 220 ｜ Call Wall 250（+5.9%，弱）（OI 1.9k） ｜ Put Wall 220（-6.8%，弱）（OI 1.9k）
量化解读： 存量 Call 重｜ATM IV 81.6%｜历史 Rank 20%（近端代理）｜IV/RV 1.40×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 107,396 股

📆 10-09 Forward Structure
存量OI: C 10.5k / P 10.2k，今日变化ΔOI: C +1.8k / P +1.1k，平值价格ATM: C $18.30 / P $14.96 ｜ ATM IV 80.0%，净 delta 敞口 47k shares
Top ΔOI: C 200 +399
仓位参考: Max Pain 220 ｜ Call Wall 240（+1.6%）（OI 1.8k） ｜ Put Wall 225（-4.7%，弱）（OI 0.7k）
量化解读： 存量两侧均衡｜ATM IV 80.0%｜历史 Rank 20%（近端代理）｜IV/RV 1.38×（近似）｜净 delta 敞口 正 47,399 股

📆 10-16 Forward Structure
存量OI: C 53.2k / P 74.4k，今日变化ΔOI: C +4.2k / P +2.2k，平值价格ATM: C $20.45 / P $18.30 ｜ ATM IV 81.0%，净 delta 敞口 38k shares
Top ΔOI: C 275 +2,077 ｜ P 245 +1,001 ｜ C 300 +572
仓位参考: Max Pain 210 ｜ Call Wall 240（+1.6%，弱）（OI 4.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 81.0%｜历史 Rank 20%（近端代理）｜IV/RV 1.39×（近似）｜净 delta 敞口 正 38,327 股

📅 事件差分（观察，非因果）: 09-25（3D）ATM IV 87.6% vs 10-02 81.6%（差 +6.0pp）——覆盖 President Trump and President Xi Summit、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-22/NBIS_evening.json