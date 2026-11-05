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
🔴 **事件差分**: 11-06（1D）ATM IV 149.3% vs 11-13 133.8%（差 +15.5pp），覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Vol Regime 升档**: ELEVATED → STRESS（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🔵 **期限 OI 集中**: 11-27 10C ΔOI +4,907 占该期限总 OI 43.5%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 8.04 → 收盘 7.42（-7.7%） ｜ 今日高 8.21 ｜ 低 6.84 ｜ 昨收 8.20 → 收盘 7.42（-9.5%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-10，窗口结束前不做对错判定）

Options: P/C成交量 0.39 | OI比 0.47 | ATM IV 149.3% | Skew -32.2pp | Term 0.71 | ExpMove ±6.7%（近端） | Rank 82%
量化视角： IV 历史高位（Rank 82%，期权偏贵）｜期限结构倒挂（Term 0.71，近月 IV 高于远月）｜Put 保护异常便宜（Skew -32.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.47）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.39×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.47×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（1D）±6.7% ｜ 11-13（8D）±16.7% ｜ 11-20（15D）±20.6% ｜ 11-27（22D）±23.1%
   ⇒ IV–VIX Spread: +121.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -313,116 | GEX Change vs 上次快照 -126,923 | Flip: Primary Flip: 7.81（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 202 / LOW 75 / INVALID 135
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 7.81（全链重定价，覆盖 100%）
最近结构参考: Flip 8（现价低于该位 5.0%）
量化视角： 负 Gamma（31万，无历史分位）｜负 Gamma 加深（13万）｜现价位于 Flip 下方 4.96%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 10（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 8（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-06  C +1.5k / P -0.4k ｜ Activity HIGH ｜ 1D
11-13  C +0.5k / P +0.2k ｜ Activity MEDIUM △ ｜ 8D
11-20  C +3.1k / P +1.3k ｜ Activity HIGH ｜ 15D
11-27  C +4.6k / P +0.2k ｜ Activity HIGH ｜ 22D

📆 11-06 Forward Structure
存量OI: C 17.8k / P 8.4k，今日变化ΔOI: C +1.5k / P -0.4k，平值价格ATM: C $0.21 / P $0.29 ｜ ATM IV 149.3%，净 delta 敞口 50k shares
Top ΔOI: P 7 -391
仓位参考: Max Pain 10 ｜ Put Wall 8（+7.8%，弱）（OI 2.2k）
量化解读： 存量 Call 重｜ATM IV 149.3%｜历史 Rank 82%（近端代理）｜IV/RV 1.63×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 50,070 股

11-13（MEDIUM △）Top ΔOI: 8P +158
11-13（MEDIUM △）仓位参考: Max Pain 10 ｜ Put Wall 8（+7.8%，弱）（OI 0.3k）

📆 11-20 Forward Structure
存量OI: C 37.1k / P 30.3k，今日变化ΔOI: C +3.1k / P +1.3k，平值价格ATM: C $0.98 / P $0.55 ｜ ATM IV 128.0%，净 delta 敞口 -17k shares
仓位参考: Max Pain 12 ｜ Put Wall 8（+7.8%，弱）（OI 2.6k）
量化解读： 存量 Call 重｜ATM IV 128.0%｜历史 Rank 82%（近端代理）｜IV/RV 1.40×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 16,907 股

📆 11-27 Forward Structure
存量OI: C 8.5k / P 2.8k，今日变化ΔOI: C +4.6k / P +0.2k，平值价格ATM: C $1.08 / P $0.63 ｜ ATM IV 118.8%，净 delta 敞口 51k shares
Top ΔOI: C 10 +4,907 ｜ P 7 +101
仓位参考: Max Pain 10 ｜ Put Wall 8（+7.8%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 118.8%｜历史 Rank 82%（近端代理）｜IV/RV 1.29×（近似）｜净 delta 敞口 正 51,303 股

📅 事件差分（观察，非因果）: 11-06（1D）ATM IV 149.3% vs 11-13 133.8%（差 +15.5pp）——覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=85 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=85）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-05/USAR_evening.json