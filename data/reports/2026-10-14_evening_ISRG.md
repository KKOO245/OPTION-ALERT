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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 424.81 → 收盘 420.24（-1.1%） ｜ 今日高 425.39 ｜ 低 414.65 ｜ 昨收 422.06 → 收盘 420.24（-0.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.40 | OI比 0.92 | ATM IV 38.6% | Skew 14.6pp | Term 1.18 | ExpMove ±2.2%（近端） | Rank 48%
量化视角： IV 中性（Rank 48%）｜期限结构正常偏陡（Term 1.18）｜保护溢价显著（Skew 14.6pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.40×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.92×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（2D）±2.2% ｜ 10-23（9D）±7.9% ｜ 10-30（16D）±9.7% ｜ 11-06（23D）±9.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,877,750 | GEX Change vs 上次快照 210,433 | Flip: Primary Flip: 403.49（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 87%（带内） ｜ IV 有效性: VALID 343 / LOW 170 / INVALID 451
结构观察区: Primary Flip 403.49（全链重定价，覆盖 87%）
Call Wall 420（弱结构｜现价高于该位 0.1%）
最近结构参考: Call Wall 420（现价高于该位 0.1%）
量化视角： 正 Gamma（288万，无历史分位）｜正 Gamma 增强（+21万）｜现价位于 Flip 上方 4.15%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 395（MaxPain，仅结算参考） / 420（Call Wall，弱结构）。
• Gamma 区域：切换参考 403（全链重定价，覆盖 87%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +72 / P +87 ｜ Activity MEDIUM △ ｜ 2D
10-23  C +93 / P +0.1k ｜ Activity HIGH ｜ 9D
10-30  C +72 / P +24 ｜ Activity HIGH ｜ 16D
11-06  C +27 / P +22 ｜ Activity MEDIUM △ ｜ 23D

📆 10-16 Forward Structure
存量OI: C 11.7k / P 10.8k，今日变化ΔOI: C +72 / P +87，平值价格ATM: C $4.65 / P $4.55 ｜ ATM IV 38.6%，净 delta 敞口 3k shares
Top ΔOI: C 400 -38 ｜ P 405 +25 ｜ C 245 +23
仓位参考: Max Pain 395 ｜ Call Wall 400（-4.8%，弱）（OI 0.8k） ｜ Put Wall 380（-9.6%，弱）（OI 0.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 38.6%｜历史 Rank 48%（近端代理）｜IV/RV 1.63×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 3,260 股

📆 10-23 Forward Structure
存量OI: C 2.5k / P 1.8k，今日变化ΔOI: C +93 / P +0.1k，平值价格ATM: C $15.50 / P $17.70 ｜ ATM IV 61.6%，净 delta 敞口 2k shares
Top ΔOI: C 460 +18 ｜ P 380 +17 ｜ C 387 +17
仓位参考: Max Pain 415 ｜ Call Wall 425（+1.1%，弱）（OI 0.5k） ｜ Put Wall 415（-1.2%）（OI 0.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 61.6%｜历史 Rank 48%（近端代理）｜IV/RV 2.59×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,979 股

📆 10-30 Forward Structure
存量OI: C 1.2k / P 0.7k，今日变化ΔOI: C +72 / P +24，平值价格ATM: C $20.00 / P $20.70 ｜ ATM IV 54.4%，净 delta 敞口 437 shares
Top ΔOI: P 390 +10
仓位参考: Max Pain 395 ｜ Call Wall 460（+9.5%，弱）（OI 95） ｜ Put Wall 380（-9.6%，弱）（OI 50）
量化解读： 存量 Call 重｜ATM IV 54.4%｜历史 Rank 48%（近端代理）｜IV/RV 2.29×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 437 股

11-06（MEDIUM △）Top ΔOI: 420P +14 ｜ 400C +8
11-06（MEDIUM △）仓位参考: Max Pain 405 ｜ Call Wall 455（+8.3%，弱）（OI 50） ｜ Put Wall 390（-7.2%）（OI 52）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-14/ISRG_evening.json