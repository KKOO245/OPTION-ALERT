# 期权晚报 2026-11-11（快照 16:40 ET）

📊 市场环境

SPY $759.81 ｜ QQQ $nan
VIX 17.49 ↓10.1%（5D +5.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 37.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-11

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **事件差分**: 11-13 ATM IV 108.0% vs 11-20 95.5%（差 +12.4pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-20 220C ΔOI +1,413（距现价 +5.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 199.52 → 收盘 209.47（+5.0%） ｜ 今日高 217.85 ｜ 低 199.48 ｜ 昨收 185.42 → 收盘 209.47（+13.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.03 | OI比 0.82 | ATM IV 108.0% | Skew 2.2pp | Term 0.78 | ExpMove ±6.4%（近端） | Rank 67%
量化视角： IV 中性（Rank 67%）｜期限结构倒挂（Term 0.78，近月 IV 高于远月）｜保护溢价中性（Skew 2.2pp）｜存量 Call 偏重（OI比 0.82）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.03×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.82×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-13（2D）±6.4% ｜ 11-20（9D）±12.0% ｜ 11-27（16D）±14.8% ｜ 12-04（23D）±17.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 3,625,570 | GEX Change vs 上次快照 2,175,142 | Flip: Primary Flip: 201.76（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 601 / LOW 155 / INVALID 172
结构观察区: Primary Flip 201.76（全链重定价，覆盖 100%）
Put Wall 200（弱结构｜现价高于该位 4.7%）
最近结构参考: Flip 202（现价高于该位 3.8%）
量化视角： 正 Gamma（363万，无历史分位）｜正 Gamma 增强（+218万）｜现价位于 Flip 上方 3.82%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall，弱结构） / 190（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 202（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +2.1k / P +4.0k ｜ Activity HIGH ｜ 2D
11-20  C +4.6k / P +1.1k ｜ Activity HIGH ｜ 9D
11-27  C +0.5k / P +0.7k ｜ Activity HIGH ｜ 16D
12-04  C +0.3k / P +0.4k ｜ Activity HIGH ｜ 23D

📆 11-13 Forward Structure
存量OI: C 43.4k / P 35.7k，今日变化ΔOI: C +2.1k / P +4.0k，平值价格ATM: C $6.42 / P $7.00 ｜ ATM IV 108.0%，净 delta 敞口 170k shares
Top ΔOI: C 190 +536
仓位参考: Max Pain 190 ｜ Call Wall 220（+5.0%，弱）（OI 2.3k） ｜ Put Wall 190（-9.3%，弱）（OI 1.8k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 108.0%｜历史 Rank 67%（近端代理）｜IV/RV 0.92×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 170,374 股

📆 11-20 Forward Structure
存量OI: C 80.2k / P 81.1k，今日变化ΔOI: C +4.6k / P +1.1k，平值价格ATM: C $12.50 / P $12.55 ｜ ATM IV 95.5%，净 delta 敞口 172k shares
Top ΔOI: C 250 +1,977 ｜ C 220 +1,413 ｜ P 172 +611
仓位参考: Max Pain 215 ｜ Call Wall 220（+5.0%，弱）（OI 4.8k） ｜ Put Wall 200（-4.5%，弱）（OI 5.4k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 95.5%｜历史 Rank 67%（近端代理）｜IV/RV 0.82×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 171,517 股

📆 11-27 Forward Structure
存量OI: C 9.1k / P 10.9k，今日变化ΔOI: C +0.5k / P +0.7k，平值价格ATM: C $15.85 / P $15.20 ｜ ATM IV 85.8%，净 delta 敞口 16k shares
Top ΔOI: P 185 +355
仓位参考: Max Pain 215 ｜ Call Wall 200（-4.5%，弱）（OI 0.7k） ｜ Put Wall 190（-9.3%，弱）（OI 1.2k）
量化解读： 存量 Put 重｜ATM IV 85.8%｜历史 Rank 67%（近端代理）｜IV/RV 0.73×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 16,263 股

📆 12-04 Forward Structure
存量OI: C 6.5k / P 7.0k，今日变化ΔOI: C +0.3k / P +0.4k，平值价格ATM: C $18.20 / P $17.95 ｜ ATM IV 85.6%，净 delta 敞口 11k shares
Top ΔOI: P 185 +192 ｜ C 180 +97 ｜ C 200 +66
仓位参考: Max Pain 200 ｜ Call Wall 200（-4.5%，弱）（OI 0.6k） ｜ Put Wall 200（-4.5%）（OI 1.8k）
量化解读： 存量两侧均衡｜ATM IV 85.6%｜历史 Rank 67%（近端代理）｜IV/RV 0.73×（近似）｜净 delta 敞口 正 10,991 股

📅 事件差分（观察，非因果）: 11-13（2D）ATM IV 108.0% vs 11-20 95.5%（差 +12.4pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-11/BE_evening.json