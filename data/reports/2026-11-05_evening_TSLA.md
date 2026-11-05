# 期权晚报 2026-11-05（快照 16:40 ET）

📊 市场环境

SPY $733.00 ｜ QQQ $647.05
VIX 28.18 ↑69.7%（5D +63.8%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 19.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-05

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🔴 **事件差分**: 11-06（1D）ATM IV 96.8% vs 11-09 70.0%（差 +26.8pp），覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Vol Regime 升档**: ELEVATED → STRESS（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-06 360P ΔOI +4,876（距现价 +4.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 374.02 → 收盘 343.69（-8.1%） ｜ 今日高 374.23 ｜ 低 338.15 ｜ 昨收 385.19 → 收盘 343.69（-10.8%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-10，窗口结束前不做对错判定）

Options: P/C成交量 1.00 | OI比 1.48 | ATM IV 96.8% | Skew 12.6pp | Term 0.59 | ExpMove ±4.1%（近端） | Rank 95%
量化视角： IV 历史高位（Rank 95%，期权偏贵）｜期限结构倒挂（Term 0.59，近月 IV 高于远月）｜保护溢价显著（Skew 12.6pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.00×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.48×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-06（1D）±4.1% ｜ 11-09（4D）±5.8% ｜ 11-11（6D）±7.4% ｜ 11-13（8D）±8.3%
   ⇒ IV–VIX Spread: +68.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -59,686,077 | GEX Change vs 上次快照 -10,922,321 | Flip: Primary Flip: 373.41（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1285 / LOW 183 / INVALID 878
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 373.41（全链重定价，覆盖 99%）
最近结构参考: Flip 373（现价低于该位 8.0%）
量化视角： 负 Gamma（5969万，无历史分位）｜负 Gamma 加深（1092万）｜现价位于 Flip 下方 7.96%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 392（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 373（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-06  C +18.0k / P +20.2k ｜ Activity MEDIUM △ ｜ 1D
11-09  C +8.2k / P +8.2k ｜ Activity HIGH ｜ 4D
11-11  C +4.6k / P +5.3k ｜ Activity HIGH ｜ 6D
11-13  C +5.4k / P +6.2k ｜ Activity HIGH ｜ 8D

📆 11-06 Forward Structure
存量OI: C 188.3k / P 279.0k，今日变化ΔOI: C +18.0k / P +20.2k，平值价格ATM: C $7.50 / P $6.47 ｜ ATM IV 96.8%，净 delta 敞口 -1.1M shares
Top ΔOI: P 360 +4,876
仓位参考: Max Pain 392 ｜ Put Wall 360（+4.7%，弱）（OI 9.9k）
量化解读： 存量 Put 重｜ATM IV 96.8%｜历史 Rank 95%（近端代理）｜IV/RV 2.75×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,124,411 股

📆 11-09 Forward Structure
存量OI: C 28.3k / P 23.5k，今日变化ΔOI: C +8.2k / P +8.2k，平值价格ATM: C $10.61 / P $9.45 ｜ ATM IV 70.0%，净 delta 敞口 -394k shares
Top ΔOI: P 315 +3,004 ｜ P 380 +942
仓位参考: Max Pain 392 ｜ Put Wall 315（-8.3%，弱）（OI 3.0k）
量化解读： 存量 Call 重｜ATM IV 70.0%｜历史 Rank 95%（近端代理）｜IV/RV 1.99×（近似）｜净 delta 敞口 负 394,182 股

📆 11-11 Forward Structure
存量OI: C 14.6k / P 10.8k，今日变化ΔOI: C +4.6k / P +5.3k，平值价格ATM: C $13.40 / P $12.15 ｜ ATM IV 72.3%，净 delta 敞口 -241k shares
Top ΔOI: P 260 +1,751 ｜ C 390 +1,249 ｜ P 377 +553
仓位参考: Max Pain 390 ｜ Put Wall 350（+1.8%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 72.3%｜历史 Rank 95%（近端代理）｜IV/RV 2.06×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 240,745 股

📆 11-13 Forward Structure
存量OI: C 56.5k / P 43.3k，今日变化ΔOI: C +5.4k / P +6.2k，平值价格ATM: C $14.85 / P $13.85 ｜ ATM IV 70.8%，净 delta 敞口 -307k shares
Top ΔOI: P 380 +587 ｜ P 382 +471
仓位参考: Max Pain 380 ｜ Call Wall 375（+9.1%，弱）（OI 1.7k） ｜ Put Wall 350（+1.8%，弱）（OI 2.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 70.8%｜历史 Rank 95%（近端代理）｜IV/RV 2.01×（近似）｜净 delta 敞口 负 306,575 股

📅 事件差分（观察，非因果）: 11-06（1D）ATM IV 96.8% vs 11-09 70.0%（差 +26.8pp）——覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=85 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=85）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-05/TSLA_evening.json