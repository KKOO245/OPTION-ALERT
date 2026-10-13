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
🟡 **近现价集中开仓**: 10-14 390C ΔOI +3,250（距现价 +3.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 372.17 → 收盘 375.23（+0.8%） ｜ 今日高 377.05 ｜ 低 371.30 ｜ 昨收 378.03 → 收盘 375.23（-0.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.79 | OI比 0.76 | ATM IV 37.7% | Skew -0.6pp | Term 1.12 | ExpMove ±1.6%（近端） | Rank 8%
量化视角： IV 历史低位（Rank 8%，期权偏便宜）｜期限结构正常（Term 1.12）｜Put 保护异常便宜（Skew -0.6pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.76）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.79×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.76×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-14（1D）±1.6% ｜ 10-16（3D）±3.4% ｜ 10-19（6D）±3.8% ｜ 10-23（10D）±7.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 54,506,190 | GEX Change vs 上次快照 15,346,915 | Flip: Primary Flip: 367.75（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1122 / LOW 143 / INVALID 583
结构观察区: Primary Flip 367.75（全链重定价，覆盖 99%）
Call Wall 400（现价低于该位 6.2%）
最近结构参考: Flip 368（现价高于该位 2.0%）
量化视角： 正 Gamma（5451万，无历史分位）｜正 Gamma 增强（+1535万）｜现价位于 Flip 上方 2.04%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 378（MaxPain，仅结算参考） / 400（Call Wall）。
• Gamma 区域：切换参考 368（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-14  C +33.3k / P +20.2k ｜ Activity HIGH ｜ 1D
10-16  C +25.9k / P +14.3k ｜ Activity HIGH ｜ 3D
10-19  C +8.1k / P +3.4k ｜ Activity HIGH ｜ 6D
10-23  C +4.7k / P +2.9k ｜ Activity HIGH ｜ 10D

📆 10-14 Forward Structure
存量OI: C 53.2k / P 40.7k，今日变化ΔOI: C +33.3k / P +20.2k，平值价格ATM: C $3.14 / P $2.88 ｜ ATM IV 37.7%，净 delta 敞口 -33k shares
Top ΔOI: C 400 +4,252 ｜ C 390 +3,250
仓位参考: Max Pain 378 ｜ Call Wall 400（+6.6%，弱）（OI 7.4k） ｜ Put Wall 370（-1.4%，弱）（OI 2.8k）
量化解读： 存量 Call 重｜ATM IV 37.7%｜历史 Rank 8%（近端代理）｜IV/RV 1.31×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 33,476 股

📆 10-16 Forward Structure
存量OI: C 395.1k / P 392.5k，今日变化ΔOI: C +25.9k / P +14.3k，平值价格ATM: C $6.58 / P $6.16 ｜ ATM IV 46.8%，净 delta 敞口 89k shares
Top ΔOI: C 382 +2,580 ｜ C 380 +2,310
仓位参考: Max Pain 372 ｜ Call Wall 400（+6.6%，弱）（OI 24.4k） ｜ Put Wall 380（+1.3%，弱）（OI 15.4k）
量化解读： 存量两侧均衡｜ATM IV 46.8%｜历史 Rank 8%（近端代理）｜IV/RV 1.62×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 89,227 股

📆 10-19 Forward Structure
存量OI: C 22.4k / P 8.1k，今日变化ΔOI: C +8.1k / P +3.4k，平值价格ATM: C $7.47 / P $6.80 ｜ ATM IV 36.5%，净 delta 敞口 60k shares
Top ΔOI: C 400 +916
仓位参考: Max Pain 378 ｜ Call Wall 400（+6.6%，弱）（OI 2.7k） ｜ Put Wall 360（-4.1%，弱）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 36.5%｜历史 Rank 8%（近端代理）｜IV/RV 1.27×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 60,293 股

📆 10-23 Forward Structure
存量OI: C 67.3k / P 45.7k，今日变化ΔOI: C +4.7k / P +2.9k，平值价格ATM: C $13.80 / P $13.04 ｜ ATM IV 54.0%，净 delta 敞口 53k shares
Top ΔOI: C 390 +448
仓位参考: Max Pain 370 ｜ Call Wall 400（+6.6%，弱）（OI 5.7k） ｜ Put Wall 360（-4.1%，弱）（OI 2.7k）
量化解读： 存量 Call 重｜ATM IV 54.0%｜历史 Rank 8%（近端代理）｜IV/RV 1.87×（近似）｜净 delta 敞口 正 53,237 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-13/TSLA_evening.json