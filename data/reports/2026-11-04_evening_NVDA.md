# 期权晚报 2026-11-04（快照 16:40 ET）

📊 市场环境

SPY $766.81 ｜ QQQ $691.95
VIX 16.61 ↓20.3%（5D -1.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-04

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 54.5 ｜ 前值 54.9　✅ 今日已公布
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **事件差分**: 11-06 ATM IV 55.9% vs 11-09 43.2%（差 +12.7pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-09 207P ΔOI +2,070（距现价 +3.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 203.58 → 收盘 200.13（-1.7%） ｜ 今日高 206.79 ｜ 低 199.68 ｜ 昨收 206.69 → 收盘 200.13（-3.2%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-09，窗口结束前不做对错判定）

Options: P/C成交量 0.94 | OI比 1.12 | ATM IV 47.0% | Skew -4.1pp | Term 1.00 | ExpMove ±3.4%（近端） | Rank 64%
量化视角： IV 中性（Rank 64%）｜期限结构正常（Term 1.00）｜Put 保护异常便宜（Skew -4.1pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.94×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.12×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-06（2D）±3.4% ｜ 11-09（5D）±4.0% ｜ 11-11（7D）±5.0% ｜ 11-13（9D）±5.7%
   ⇒ IV–VIX Spread: +30.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -43,679,517 | GEX Change vs 上次快照 -136,121,423 | Flip: Primary Flip: 201.87（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 692 / LOW 172 / INVALID 646
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 201.87（全链重定价，覆盖 94%）
Put Wall 200（弱结构｜现价高于该位 0.1%）
最近结构参考: Put Wall 200（现价高于该位 0.1%）
量化视角： 负 Gamma（4368万，无历史分位）｜由正转负（1.36亿）｜现价位于 Flip 下方 0.86%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall，弱结构）；上方 208（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 202（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-06  C +32.4k / P +17.4k ｜ Activity HIGH ｜ 2D
11-09  C +4.4k / P +4.8k ｜ Activity HIGH ｜ 5D
11-11  C +2.2k / P +5.1k ｜ Activity HIGH ｜ 7D
11-13  C +8.3k / P +9.3k ｜ Activity HIGH ｜ 9D

📆 11-06 Forward Structure
存量OI: C 403.0k / P 292.6k，今日变化ΔOI: C +32.4k / P +17.4k，平值价格ATM: C $3.55 / P $3.15 ｜ ATM IV 55.9%，净 delta 敞口 -253k shares
Top ΔOI: C 220 +4,560
仓位参考: Max Pain 208 ｜ Call Wall 220（+9.9%，弱）（OI 55.4k） ｜ Put Wall 200（-0.1%，弱）（OI 21.9k）
量化解读： 存量 Call 重｜ATM IV 55.9%｜历史 Rank 64%（近端代理）｜IV/RV 1.80×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 252,531 股

📆 11-09 Forward Structure
存量OI: C 16.0k / P 17.0k，今日变化ΔOI: C +4.4k / P +4.8k，平值价格ATM: C $4.25 / P $3.85 ｜ ATM IV 43.2%，净 delta 敞口 -194k shares
Top ΔOI: P 207 +2,070 ｜ P 190 +872
仓位参考: Max Pain 208 ｜ Call Wall 220（+9.9%，弱）（OI 2.2k） ｜ Put Wall 207.5（+3.7%，弱）（OI 2.5k）
量化解读： 存量两侧均衡｜ATM IV 43.2%｜历史 Rank 64%（近端代理）｜IV/RV 1.39×（近似）｜净 delta 敞口 负 194,239 股

📆 11-11 Forward Structure
存量OI: C 9.1k / P 17.3k，今日变化ΔOI: C +2.2k / P +5.1k，平值价格ATM: C $5.15 / P $4.80 ｜ ATM IV 44.9%，净 delta 敞口 -106k shares
Top ΔOI: P 192 +1,227 ｜ P 202 +759
仓位参考: Max Pain 210 ｜ Call Wall 220（+9.9%）（OI 2.4k） ｜ Put Wall 190（-5.1%）（OI 4.9k）
量化解读： 存量 Put 重｜ATM IV 44.9%｜历史 Rank 64%（近端代理）｜IV/RV 1.45×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 105,586 股

📆 11-13 Forward Structure
存量OI: C 170.8k / P 183.6k，今日变化ΔOI: C +8.3k / P +9.3k，平值价格ATM: C $5.90 / P $5.46 ｜ ATM IV 44.8%，净 delta 敞口 -166k shares
Top ΔOI: C 215 +2,527 ｜ P 185 +1,529 ｜ C 220 +1,406
仓位参考: Max Pain 215 ｜ Call Wall 220（+9.9%，弱）（OI 14.2k） ｜ Put Wall 200（-0.1%，弱）（OI 15.1k）
量化解读： 存量两侧均衡｜ATM IV 44.8%｜历史 Rank 64%（近端代理）｜IV/RV 1.45×（近似）｜净 delta 敞口 负 165,986 股

📅 事件差分（观察，非因果）: 11-06（2D）ATM IV 55.9% vs 11-09 43.2%（差 +12.7pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=83 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=83）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-04/NVDA_evening.json