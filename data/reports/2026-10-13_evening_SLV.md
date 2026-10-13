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
🟡 **近现价集中开仓**: 10-14 56C ΔOI +3,095（距现价 +4.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 54.28 → 收盘 53.49（-1.5%） ｜ 今日高 54.33 ｜ 低 53.19 ｜ 昨收 54.35 → 收盘 53.49（-1.6%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.34 | OI比 0.55 | ATM IV 42.7% | Skew -0.9pp | Term 0.79 | ExpMove ±1.8%（近端） | Rank 72%
量化视角： IV 中性（Rank 72%）｜期限结构倒挂（Term 0.79，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.9pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.55）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.34×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.55×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-14（1D）±1.8% ｜ 10-16（3D）±2.8% ｜ 10-19（6D）±3.1% ｜ 10-21（8D）±3.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 38,644,546 | GEX Change vs 上次快照 -13,845,762 | Flip: Primary Flip: 52.06（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 770 / LOW 147 / INVALID 417
结构观察区: Primary Flip 52.06（全链重定价，覆盖 99%）
Put Wall 50（弱结构｜现价高于该位 7.0%）
最近结构参考: Flip 52（现价高于该位 2.7%）
量化视角： 正 Gamma（3864万，无历史分位）｜正 Gamma 减弱（1385万）｜现价位于 Flip 上方 2.74%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 50（Put Wall，弱结构）；上方 54（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 52（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-14  C +8.9k / P +2.9k ｜ Activity HIGH ｜ 1D
10-16  C -2.8k / P +0.9k ｜ Activity MEDIUM △ ｜ 3D
10-19  C +1.1k / P +0.8k ｜ Activity HIGH ｜ 6D
10-21  C +1.5k / P +0.5k ｜ Activity HIGH ｜ 8D

📆 10-14 Forward Structure
存量OI: C 20.8k / P 11.4k，今日变化ΔOI: C +8.9k / P +2.9k，平值价格ATM: C $0.47 / P $0.48 ｜ ATM IV 42.7%，净 delta 敞口 -41k shares
Top ΔOI: C 56 +3,095 ｜ C 55 +1,488 ｜ C 55 +1,058
仓位参考: Max Pain 54 ｜ Call Wall 56（+4.7%）（OI 3.8k） ｜ Put Wall 54（+1.0%，弱）（OI 1.7k）
量化解读： 存量 Call 重｜ATM IV 42.7%｜历史 Rank 72%（近端代理）｜IV/RV 1.37×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 41,423 股

10-16（MEDIUM △）Top ΔOI: 55C +950 ｜ 55C +627
10-16（MEDIUM △）仓位参考: Max Pain 56 ｜ Call Wall 50（-6.5%，弱）（OI 26.9k） ｜ Put Wall 50（-6.5%，弱）（OI 23.4k）

📆 10-19 Forward Structure
存量OI: C 3.6k / P 2.4k，今日变化ΔOI: C +1.1k / P +0.8k，平值价格ATM: C $0.88 / P $0.79 ｜ ATM IV 30.6%，净 delta 敞口 -19k shares
Top ΔOI: C 55 +357 ｜ C 55 +354 ｜ P 52 +147
仓位参考: Max Pain 54 ｜ Call Wall 55（+2.8%，弱）（OI 0.5k） ｜ Put Wall 55（+2.8%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 30.6%｜历史 Rank 72%（近端代理）｜IV/RV 0.98×（近似）｜净 delta 敞口 负 19,330 股

📆 10-21 Forward Structure
存量OI: C 3.7k / P 1.4k，今日变化ΔOI: C +1.5k / P +0.5k，平值价格ATM: C $1.02 / P $0.97 ｜ ATM IV 31.8%，净 delta 敞口 -2k shares
Top ΔOI: C 57 +307
仓位参考: Max Pain 54 ｜ Call Wall 53.5（+0.0%，弱）（OI 0.5k） ｜ Put Wall 53（-0.9%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 31.8%｜历史 Rank 72%（近端代理）｜IV/RV 1.02×（近似）｜净 delta 敞口 负 1,944 股

📅 事件差分（观察，非因果）: 10-14（1D）ATM IV 42.7% vs 10-16 37.2%（差 +5.5pp）——覆盖 成屋销售、Core Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、Inflation Rate MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-13/SLV_evening.json