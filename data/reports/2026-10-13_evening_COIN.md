# 期权晚报 2026-10-13（快照 16:40 ET）

📊 市场环境

SPY $778.01 ｜ QQQ $743.57
VIX 15.27 ↑0.4%（5D +1.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 44.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-13

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-13 10:00　【高】成屋销售　预测 3.95 ｜ 实际 3.99 ｜ 前值 3.93　✅ 今日已公布
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.6 ｜ 实际 待公布 ｜ 前值 3.4
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 待公布 ｜ 前值 2.4
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-16 190C ΔOI +675（距现价 +4.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 179.57 → 收盘 181.79（+1.2%） ｜ 今日高 183.00 ｜ 低 178.66 ｜ 昨收 180.39 → 收盘 181.79（+0.8%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.43 | OI比 0.81 | ATM IV 67.9% | Skew -4.3pp | Term 0.98 | ExpMove ±4.9%（近端） | Rank 28%
量化视角： IV 中性（Rank 28%）｜期限结构正常（Term 0.98）｜Put 保护异常便宜（Skew -4.3pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.81）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.43×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.81×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（3D）±4.9% ｜ 10-23（10D）±8.0% ｜ 10-30（17D）±11.3% ｜ 11-06（24D）±14.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 24,836,042 | GEX Change vs 上次快照 2,484,144 | Flip: Primary Flip: 171.25（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 483 / LOW 125 / INVALID 214
结构观察区: Primary Flip 171.25（全链重定价，覆盖 100%）
最近结构参考: Flip 171（现价高于该位 6.2%）
量化视角： 正 Gamma（2484万，无历史分位）｜正 Gamma 增强（+248万）｜现价位于 Flip 上方 6.16%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 180（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 171（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +4.0k / P +1.5k ｜ Activity HIGH ｜ 3D
10-23  C +0.9k / P +1.4k ｜ Activity HIGH ｜ 10D
10-30  C +0.6k / P +0.4k ｜ Activity MEDIUM △ ｜ 17D
11-06  C +0.5k / P +0.4k ｜ Activity HIGH ｜ 24D

📆 10-16 Forward Structure
存量OI: C 138.5k / P 111.7k，今日变化ΔOI: C +4.0k / P +1.5k，平值价格ATM: C $4.25 / P $4.70 ｜ ATM IV 67.9%，净 delta 敞口 74k shares
Top ΔOI: C 190 +675 ｜ C 185 +465
仓位参考: Max Pain 180 ｜ Call Wall 185（+1.8%，弱）（OI 11.3k） ｜ Put Wall 165（-9.2%，弱）（OI 9.1k）
量化解读： 存量 Call 重｜ATM IV 67.9%｜历史 Rank 28%（近端代理）｜IV/RV 1.92×（近似）｜净 delta 敞口 正 73,647 股

📆 10-23 Forward Structure
存量OI: C 12.1k / P 18.3k，今日变化ΔOI: C +0.9k / P +1.4k，平值价格ATM: C $7.02 / P $7.54 ｜ ATM IV 62.3%，净 delta 敞口 10k shares
Top ΔOI: P 160 +547 ｜ C 190 +137
仓位参考: Max Pain 185 ｜ Call Wall 190（+4.5%，弱）（OI 1.4k）
量化解读： 存量 Put 重｜ATM IV 62.3%｜历史 Rank 28%（近端代理）｜IV/RV 1.76×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 10,407 股

10-30（MEDIUM △）Top ΔOI: 200C +386
10-30（MEDIUM △）仓位参考: Max Pain 185 ｜ Call Wall 185（+1.8%，弱）（OI 1.3k） ｜ Put Wall 180（-1.0%，弱）（OI 0.8k）

📆 11-06 Forward Structure
存量OI: C 3.4k / P 6.7k，今日变化ΔOI: C +0.5k / P +0.4k，平值价格ATM: C $12.50 / P $13.20 ｜ ATM IV 68.8%，净 delta 敞口 13k shares
Top ΔOI: C 177 +141
仓位参考: Max Pain 178 ｜ Call Wall 177.5（-2.4%，弱）（OI 0.2k） ｜ Put Wall 170（-6.5%，弱）（OI 0.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 68.8%｜历史 Rank 28%（近端代理）｜IV/RV 1.94×（近似）｜净 delta 敞口 正 13,084 股

📅 事件差分（观察，非因果）: 10-16（3D）ATM IV 67.9% vs 10-23 62.3%（差 +5.6pp）——覆盖 成屋销售、Core Inflation Rate MoM 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-13/COIN_evening.json