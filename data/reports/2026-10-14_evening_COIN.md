# 期权晚报 2026-10-14（快照 16:42 ET）

📊 市场环境

SPY $769.60 ｜ QQQ $728.95
VIX 16.87 ↑10.5%（5D +11.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 32.4（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-14

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 2.6 ｜ 前值 2.4　✅ 今日已公布
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.6 ｜ 实际 3.7 ｜ 前值 3.4　✅ 今日已公布
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 0.6 ｜ 前值 0.4　✅ 今日已公布
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览
🟡 **事件差分**: 10-16 ATM IV 72.5% vs 10-23 62.3%（差 +10.2pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-16 172P ΔOI +553（距现价 -0.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 178.66 → 收盘 172.89（-3.2%） ｜ 今日高 182.39 ｜ 低 171.41 ｜ 昨收 181.79 → 收盘 172.89（-4.9%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.80 | OI比 0.81 | ATM IV 72.5% | Skew -0.9pp | Term 0.96 | ExpMove ±4.4%（近端） | Rank 39%
量化视角： IV 中性（Rank 39%）｜期限结构正常（Term 0.96）｜Put 保护异常便宜（Skew -0.9pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.81）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.80×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.81×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（2D）±4.4% ｜ 10-23（9D）±7.8% ｜ 10-30（16D）±11.8% ｜ 11-06（23D）±14.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 3,887,914 | GEX Change vs 上次快照 -9,088,095 | Flip: Primary Flip: 171.57（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 457 / LOW 115 / INVALID 250
结构观察区: Primary Flip 171.57（全链重定价，覆盖 96%）
最近结构参考: Flip 172（现价高于该位 0.8%）
量化视角： 正 Gamma（389万，无历史分位）｜正 Gamma 减弱（909万）｜现价位于 Flip 上方 0.77%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 180（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 172（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +0.9k / P +1.3k ｜ Activity MEDIUM △ ｜ 2D
10-23  C +1.5k / P +1.0k ｜ Activity HIGH ｜ 9D
10-30  C +0.3k / P +0.2k ｜ Activity MEDIUM △ ｜ 16D
11-06  C +0.5k / P +0.3k ｜ Activity HIGH ｜ 23D

📆 10-16 Forward Structure
存量OI: C 139.4k / P 113.0k，今日变化ΔOI: C +0.9k / P +1.3k，平值价格ATM: C $4.00 / P $3.60 ｜ ATM IV 72.5%，净 delta 敞口 -78k shares
Top ΔOI: C 185 -702 ｜ P 172 +553
仓位参考: Max Pain 180 ｜ Call Wall 185（+7.0%，弱）（OI 10.6k） ｜ Put Wall 165（-4.6%，弱）（OI 9.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 72.5%｜历史 Rank 39%（近端代理）｜IV/RV 2.21×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 78,477 股

📆 10-23 Forward Structure
存量OI: C 13.6k / P 19.3k，今日变化ΔOI: C +1.5k / P +1.0k，平值价格ATM: C $7.20 / P $6.35 ｜ ATM IV 62.3%，净 delta 敞口 -7k shares
仓位参考: Max Pain 185 ｜ Call Wall 190（+9.9%，弱）（OI 1.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 62.3%｜历史 Rank 39%（近端代理）｜IV/RV 1.90×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 7,340 股

10-30（MEDIUM △）仓位参考: Max Pain 185 ｜ Call Wall 185（+7.0%，弱）（OI 1.3k） ｜ Put Wall 180（+4.1%，弱）（OI 0.8k）

📆 11-06 Forward Structure
存量OI: C 3.9k / P 7.0k，今日变化ΔOI: C +0.5k / P +0.3k，平值价格ATM: C $12.84 / P $12.68 ｜ ATM IV 70.5%，净 delta 敞口 9k shares
Top ΔOI: P 180 +63
仓位参考: Max Pain 178 ｜ Call Wall 177.5（+2.7%，弱）（OI 0.2k） ｜ Put Wall 170（-1.7%，弱）（OI 0.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 70.5%｜历史 Rank 39%（近端代理）｜IV/RV 2.15×（近似）｜净 delta 敞口 正 9,071 股

📅 事件差分（观察，非因果）: 10-16（2D）ATM IV 72.5% vs 10-23 62.3%（差 +10.2pp）——覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY、Inflation Rate YoY、Inflation Rate MoM、PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-14/COIN_evening.json