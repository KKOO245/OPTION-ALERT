# 期权晚报 2026-11-18（快照 16:40 ET）

📊 市场环境

SPY $730.20 ｜ QQQ $nan
VIX 24.56 ↓3.5%（5D +40.4%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 24.6（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 1.309 ｜ 前值 1.191　✅ 今日已公布
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 1.295 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🟡 **事件差分**: 11-20 ATM IV 63.0% vs 11-23 50.1%（差 +12.9pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-20 390C ΔOI +1,046（距现价 +1.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 385.19 → 收盘 383.72（-0.4%） ｜ 今日高 389.27 ｜ 低 378.36 ｜ 昨收 380.11 → 收盘 383.72（+0.9%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.65 | OI比 0.90 | ATM IV 41.4% | Skew -6.4pp | Term 0.61 | ExpMove ±3.8%（近端） | Rank 14%
量化视角： IV 历史低位（Rank 14%，期权偏便宜）｜期限结构倒挂（Term 0.61，近月 IV 高于远月）｜Put 保护异常便宜（Skew -6.4pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.65×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.90×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-20（2D）±3.8% ｜ 11-23（5D）±4.7% ｜ 11-25（7D）±5.9% ｜ 11-27（9D）±6.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 66,220,441 | GEX Change vs 上次快照 -6,060,724 | Flip: Primary Flip: 371.35（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 1323 / LOW 325 / INVALID 972
结构观察区: Primary Flip 371.35（全链重定价，覆盖 94%）
Call Wall 400（弱结构｜现价低于该位 4.1%）
最近结构参考: Flip 371（现价高于该位 3.3%）
量化视角： 正 Gamma（6622万，无历史分位）｜正 Gamma 减弱（606万）｜现价位于 Flip 上方 3.33%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 380（MaxPain，仅结算参考）；上方 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 371（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C +9.8k / P +1.7k ｜ Activity MEDIUM △ ｜ 2D
11-23  C +2.4k / P +5.1k ｜ Activity HIGH ｜ 5D
11-25  C +1.2k / P +0.8k ｜ Activity HIGH ｜ 7D
11-27  C +3.5k / P +3.2k ｜ Activity HIGH ｜ 9D

📆 11-20 Forward Structure
存量OI: C 363.2k / P 508.2k，今日变化ΔOI: C +9.8k / P +1.7k，平值价格ATM: C $7.82 / P $6.58 ｜ ATM IV 63.0%，净 delta 敞口 169k shares
Top ΔOI: C 410 +2,396 ｜ C 405 +1,607 ｜ C 390 +1,046
仓位参考: Max Pain 375 ｜ Call Wall 400（+4.2%，弱）（OI 26.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 63.0%｜历史 Rank 14%（近端代理）｜IV/RV 1.13×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 169,396 股

📆 11-23 Forward Structure
存量OI: C 24.0k / P 12.0k，今日变化ΔOI: C +2.4k / P +5.1k，平值价格ATM: C $9.75 / P $8.30 ｜ ATM IV 50.1%，净 delta 敞口 -21k shares
Top ΔOI: P 357 +1,190 ｜ P 355 +1,108 ｜ P 377 +619
仓位参考: Max Pain 382 ｜ Put Wall 357.5（-6.8%，弱）（OI 1.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 50.1%｜历史 Rank 14%（近端代理）｜IV/RV 0.90×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 21,160 股

📆 11-25 Forward Structure
存量OI: C 3.8k / P 4.7k，今日变化ΔOI: C +1.2k / P +0.8k，平值价格ATM: C $12.46 / P $10.17 ｜ ATM IV 52.2%，净 delta 敞口 8k shares
Top ΔOI: C 420 +271 ｜ C 400 +208 ｜ P 380 +116
仓位参考: Max Pain 380 ｜ Call Wall 400（+4.2%，弱）（OI 0.4k） ｜ Put Wall 370（-3.6%，弱）（OI 0.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 52.2%｜历史 Rank 14%（近端代理）｜IV/RV 0.93×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 7,883 股

📆 11-27 Forward Structure
存量OI: C 62.1k / P 56.8k，今日变化ΔOI: C +3.5k / P +3.2k，平值价格ATM: C $13.05 / P $10.15 ｜ ATM IV 48.9%，净 delta 敞口 67k shares
Top ΔOI: C 382 +393 ｜ C 420 +381
仓位参考: Max Pain 375 ｜ Call Wall 410（+6.8%）（OI 9.1k） ｜ Put Wall 350（-8.8%，弱）（OI 2.7k）
量化解读： 存量两侧均衡｜ATM IV 48.9%｜历史 Rank 14%（近端代理）｜IV/RV 0.87×（近似）｜净 delta 敞口 正 66,625 股

📅 事件差分（观察，非因果）: 11-20（2D）ATM IV 63.0% vs 11-23 50.1%（差 +12.9pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-18/TSLA_evening.json