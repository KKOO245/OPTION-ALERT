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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## SPCX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPCX: 今开 161.98 → 收盘 156.54（-3.4%） ｜ 今日高 161.98 ｜ 低 156.11 ｜ 昨收 163.42 → 收盘 156.54（-4.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.57 | OI比 0.63 | ATM IV 52.6% | Skew -1.4pp | Term 0.98 | ExpMove ±2.3%（近端） | Rank 46%
量化视角： IV 中性（Rank 46%）｜期限结构正常（Term 0.98）｜Put 保护异常便宜（Skew -1.4pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.63）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.57×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.63×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-14（1D）±2.3% ｜ 10-16（3D）±3.7% ｜ 10-19（6D）±4.3% ｜ 10-21（8D）±5.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 10,442,774 | GEX Change vs 上次快照 -25,484,364 | Flip: Primary Flip: 155.58（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 691 / LOW 175 / INVALID 550
结构观察区: Primary Flip 155.58（全链重定价，覆盖 99%）
最近结构参考: Flip 156（现价高于该位 0.6%）
量化视角： 正 Gamma（1044万，无历史分位）｜正 Gamma 减弱（2548万）｜现价位于 Flip 上方 0.62%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 162（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 156（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-14  C +9.6k / P +7.8k ｜ Activity HIGH ｜ 1D
10-16  C +19.1k / P +7.2k ｜ Activity HIGH ｜ 3D
10-19  C +6.3k / P +1.3k ｜ Activity HIGH ｜ 6D
10-21  C +0.5k / P +0.4k ｜ Activity MEDIUM △ ｜ 8D

📆 10-14 Forward Structure
存量OI: C 28.6k / P 18.0k，今日变化ΔOI: C +9.6k / P +7.8k，平值价格ATM: C $1.34 / P $2.21 ｜ ATM IV 52.6%，净 delta 敞口 -387k shares
Top ΔOI: C 170 +3,358 ｜ C 165 +1,989 ｜ C 167 +1,518
仓位参考: Max Pain 162 ｜ Call Wall 170（+8.6%，弱）（OI 5.5k） ｜ Put Wall 160（+2.2%，弱）（OI 3.1k）
量化解读： 存量 Call 重｜ATM IV 52.6%｜历史 Rank 46%（近端代理）｜IV/RV 1.12×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 387,350 股

📆 10-16 Forward Structure
存量OI: C 397.9k / P 414.9k，今日变化ΔOI: C +19.1k / P +7.2k，平值价格ATM: C $2.50 / P $3.30 ｜ ATM IV 50.6%，净 delta 敞口 -283k shares
Top ΔOI: C 165 +5,103 ｜ C 170 +3,084
仓位参考: Max Pain 150 ｜ Call Wall 170（+8.6%，弱）（OI 34.1k） ｜ Put Wall 150（-4.2%，弱）（OI 26.0k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 50.6%｜历史 Rank 46%（近端代理）｜IV/RV 1.08×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 282,820 股

📆 10-19 Forward Structure
存量OI: C 15.4k / P 5.9k，今日变化ΔOI: C +6.3k / P +1.3k，平值价格ATM: C $2.95 / P $3.75 ｜ ATM IV 41.3%，净 delta 敞口 -13k shares
Top ΔOI: C 165 +1,013 ｜ C 170 +894
仓位参考: Max Pain 165 ｜ Call Wall 170（+8.6%，弱）（OI 1.7k） ｜ Put Wall 165（+5.4%，弱）（OI 1.3k）
量化解读： 存量 Call 重｜ATM IV 41.3%｜历史 Rank 46%（近端代理）｜IV/RV 0.88×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 13,128 股

10-21（MEDIUM △）Top ΔOI: 162P +182 ｜ 170C +98
10-21（MEDIUM △）仓位参考: Max Pain 162 ｜ Call Wall 170（+8.6%，弱）（OI 0.8k） ｜ Put Wall 162.5（+3.8%）（OI 0.8k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-13/SPCX_evening.json