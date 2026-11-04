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
🔴 **事件差分**: 11-06（2D）ATM IV 138.7% vs 11-13 86.2%（差 +52.4pp），覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-06 35P ΔOI +1,041（距现价 -2.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 38.02 → 收盘 35.91（-5.5%） ｜ 今日高 38.96 ｜ 低 35.57 ｜ 昨收 37.83 → 收盘 35.91（-5.1%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-09，窗口结束前不做对错判定）

Options: P/C成交量 0.86 | OI比 0.45 | ATM IV 138.7% | Skew 1.1pp | Term 0.48 | ExpMove ±7.9%（近端） | Rank 98%
量化视角： IV 历史高位（Rank 98%，期权偏贵）｜期限结构倒挂（Term 0.48，近月 IV 高于远月）｜保护溢价薄（Skew 1.1pp）｜存量 Call 偏重（OI比 0.45）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.86×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.45×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（2D）±7.9% ｜ 11-13（9D）±10.6% ｜ 11-20（16D）±12.5% ｜ 11-27（23D）±14.2%
   ⇒ IV–VIX Spread: +122.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -135,617 | GEX Change vs 上次快照 -733,349 | Flip: Primary Flip: 36.10（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 305 / LOW 41 / INVALID 122
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 36.10（全链重定价，覆盖 100%）
Put Wall 35（现价高于该位 2.6%）
最近结构参考: Flip 36（现价低于该位 0.5%）
量化视角： 负 Gamma（14万，无历史分位）｜由正转负（73万）｜现价位于 Flip 下方 0.53%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 35（Put Wall）；上方 40（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 36（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-06  C +1.3k / P +1.0k ｜ Activity HIGH ｜ 2D
11-13  C +0.5k / P +0.2k ｜ Activity HIGH ｜ 9D
11-20  C +0.5k / P +2.2k ｜ Activity HIGH ｜ 16D
11-27  C +52 / P +55 ｜ Activity MEDIUM △ ｜ 23D

📆 11-06 Forward Structure
存量OI: C 14.3k / P 6.4k，今日变化ΔOI: C +1.3k / P +1.0k，平值价格ATM: C $1.25 / P $1.60 ｜ ATM IV 138.7%，净 delta 敞口 -4k shares
Top ΔOI: P 35 +1,041 ｜ C 39 +421 ｜ C 38 +309
仓位参考: Max Pain 40 ｜ Call Wall 39.5（+10.0%，弱）（OI 0.5k） ｜ Put Wall 35（-2.5%，弱）（OI 1.5k）
量化解读： 存量 Call 重｜ATM IV 138.7%｜历史 Rank 98%（近端代理）｜IV/RV 2.71×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 4,241 股

📆 11-13 Forward Structure
存量OI: C 6.3k / P 3.0k，今日变化ΔOI: C +0.5k / P +0.2k，平值价格ATM: C $1.80 / P $2.02 ｜ ATM IV 86.2%，净 delta 敞口 173 shares
Top ΔOI: P 35 +161
仓位参考: Max Pain 40 ｜ Call Wall 35（-2.5%，弱）（OI 0.5k） ｜ Put Wall 39（+8.6%）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 86.2%｜历史 Rank 98%（近端代理）｜IV/RV 1.68×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 173 股

📆 11-20 Forward Structure
存量OI: C 17.4k / P 12.5k，今日变化ΔOI: C +0.5k / P +2.2k，平值价格ATM: C $2.26 / P $2.24 ｜ ATM IV 75.3%，净 delta 敞口 -92k shares
Top ΔOI: P 35 +1,956 ｜ P 42 +144
仓位参考: Max Pain 44 ｜ Put Wall 35（-2.5%）（OI 3.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 75.3%｜历史 Rank 98%（近端代理）｜IV/RV 1.47×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 91,854 股

11-27（MEDIUM △）Top ΔOI: 38C +34 ｜ 38P +19
11-27（MEDIUM △）仓位参考: Max Pain 44 ｜ Put Wall 38（+5.8%，弱）（OI 90）

📅 事件差分（观察，非因果）: 11-06（2D）ATM IV 138.7% vs 11-13 86.2%（差 +52.4pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=83 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=83）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-04/MP_evening.json