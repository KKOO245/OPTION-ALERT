# 期权晚报 2026-10-28（快照 16:40 ET）

📊 市场环境

SPY $772.31 ｜ QQQ $725.61
VIX 16.91 ↓3.5%（5D +1.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-28

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布　✅ 今日已公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 4 ｜ 前值 4　✅ 今日已公布
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布　✅ 今日已公布
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.9

🔍 重点速览
🟡 **事件差分**: 10-30 ATM IV 46.8% vs 11-06 35.5%（差 +11.3pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-30 152P ΔOI +3,473（距现价 -3.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## XBI

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
XBI: 今开 153.27 → 收盘 157.51（+2.8%） ｜ 今日高 157.55 ｜ 低 152.83 ｜ 昨收 154.84 → 收盘 157.51（+1.7%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-04，窗口结束前不做对错判定）

Options: P/C成交量 7.38 | OI比 5.75 | ATM IV 46.8% | Skew 9.2pp | Term 0.75 | ExpMove ±6.3%（近端） | Rank 95%
量化视角： IV 历史高位（Rank 95%，期权偏贵）｜期限结构倒挂（Term 0.75，近月 IV 高于远月）｜保护溢价显著（Skew 9.2pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 7.38）——观察点，非方向信号
   ⇒ Put/Call Volume: 7.38×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 5.75×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-30（2D）±6.3% ｜ 11-06（9D）±4.5% ｜ 11-13（16D）±2.1% ｜ 11-20（23D）±7.1%
   ⇒ IV–VIX Spread: +29.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -7,020,406 | GEX Change vs 上次快照 7,155,895 | Flip: Primary Flip: 159.49（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 85%（带内） ｜ IV 有效性: VALID 298 / LOW 104 / INVALID 368
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 159.49（全链重定价，覆盖 85%）
Call Wall 165（现价低于该位 4.5%）
最近结构参考: Flip 159（现价低于该位 1.2%）
量化视角： 负 Gamma（702万，无历史分位）｜负 Gamma 缓解（+716万）｜现价位于 Flip 下方 1.24%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 152（MaxPain，仅结算参考）；上方 165（Call Wall）。
• Gamma 区域：切换参考 159（全链重定价，覆盖 85%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-30  C +1.2k / P +10.0k ｜ Activity HIGH ｜ 2D
11-06  C +0.4k / P +0.1k ｜ Activity HIGH ｜ 9D
11-13  C +64 / P +0.2k ｜ Activity HIGH ｜ 16D
11-20  C +0.2k / P +1.9k ｜ Activity HIGH ｜ 23D

📆 10-30 Forward Structure
存量OI: C 11.2k / P 64.4k，今日变化ΔOI: C +1.2k / P +10.0k，平值价格ATM: C $1.35 / P $8.65 ｜ ATM IV 46.8%，净 delta 敞口 -70k shares
Top ΔOI: P 152 +3,473 ｜ P 152 +3,067 ｜ P 145 +1,713
仓位参考: Max Pain 152 ｜ Call Wall 155（-1.6%，弱）（OI 2.2k） ｜ Put Wall 150（-4.8%，弱）（OI 9.1k）
量化解读： 存量 Put 重｜ATM IV 46.8%｜历史 Rank 95%（近端代理）｜IV/RV 1.43×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 70,208 股

📆 11-06 Forward Structure
存量OI: C 2.1k / P 3.8k，今日变化ΔOI: C +0.4k / P +0.1k，平值价格ATM: C $3.00 / P $4.05 ｜ ATM IV 35.5%，净 delta 敞口 19k shares
Top ΔOI: C 156 +210 ｜ P 148 +61 ｜ C 159 +36
仓位参考: Max Pain 152 ｜ Call Wall 156（-1.0%，弱）（OI 0.3k） ｜ Put Wall 151（-4.1%，弱）（OI 0.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 35.5%｜历史 Rank 95%（近端代理）｜IV/RV 1.09×（近似）｜净 delta 敞口 正 19,496 股

📆 11-13 Forward Structure
存量OI: C 1.3k / P 1.8k，今日变化ΔOI: C +64 / P +0.2k，平值价格ATM: C $3.28 / P $0.00 ｜ ATM IV 38.2%，净 delta 敞口 990 shares
Top ΔOI: P 145 +70 ｜ P 148 +38
仓位参考: Max Pain 153 ｜ Call Wall 160（+1.6%）（OI 0.4k） ｜ Put Wall 153（-2.9%，弱）（OI 0.4k）
量化解读： 存量 Put 重｜ATM IV 38.2%｜历史 Rank 95%（近端代理）｜IV/RV 1.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 990 股

📆 11-20 Forward Structure
存量OI: C 20.0k / P 39.5k，今日变化ΔOI: C +0.2k / P +1.9k，平值价格ATM: C $5.00 / P $6.25 ｜ ATM IV 37.3%，净 delta 敞口 -39k shares
Top ΔOI: P 147 +1,999 ｜ P 149 +118
仓位参考: Max Pain 155 ｜ Call Wall 165（+4.8%）（OI 7.3k）
量化解读： 存量 Put 重｜ATM IV 37.3%｜历史 Rank 95%（近端代理）｜IV/RV 1.14×（近似）｜净 delta 敞口 负 39,010 股

📅 事件差分（观察，非因果）: 10-30（2D）ATM IV 46.8% vs 11-06 35.5%（差 +11.3pp）——覆盖 美联储议息会议 Statement、美联储利率决议 Decision、Fed Press Conference、GDP 增速 Rate QoQ Adv、PCE 物价 Price Index MoM、Personal Income MoM、Personal Spending MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-28/XBI_evening.json