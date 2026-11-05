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
🔴 **事件差分**: 11-06（1D）ATM IV 184.7% vs 11-13 98.5%（差 +86.2pp），覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Vol Regime 升档**: ELEVATED → STRESS（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-06 35P ΔOI +994（距现价 +3.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 36.15 → 收盘 33.74（-6.7%） ｜ 今日高 36.54 ｜ 低 31.90 ｜ 昨收 35.91 → 收盘 33.74（-6.0%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-10，窗口结束前不做对错判定）

Options: P/C成交量 0.86 | OI比 0.47 | ATM IV 184.7% | Skew -0.8pp | Term 0.42 | ExpMove ±7.9%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.42，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.8pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.47）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.86×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.47×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（1D）±7.9% ｜ 11-13（8D）±12.9% ｜ 11-20（15D）±15.8% ｜ 11-27（22D）±16.5%
   ⇒ IV–VIX Spread: +156.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -842,707 | GEX Change vs 上次快照 -413,178 | Flip: Primary Flip: 35.40（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 335 / LOW 55 / INVALID 118
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 35.40（全链重定价，覆盖 100%）
Put Wall 35（现价低于该位 3.6%）
最近结构参考: Put Wall 35（现价低于该位 3.6%）
量化视角： 负 Gamma（84万，无历史分位）｜负 Gamma 加深（41万）｜现价位于 Flip 下方 4.69%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 35（Put Wall） / 38（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 35（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-06  C +2.8k / P +1.7k ｜ Activity HIGH ｜ 1D
11-13  C +0.8k / P +72 ｜ Activity HIGH ｜ 8D
11-20  C +2.2k / P +0.7k ｜ Activity HIGH ｜ 15D
11-27  C +0.1k / P +0.2k ｜ Activity HIGH ｜ 22D

📆 11-06 Forward Structure
存量OI: C 17.2k / P 8.1k，今日变化ΔOI: C +2.8k / P +1.7k，平值价格ATM: C $1.46 / P $1.20 ｜ ATM IV 184.7%，净 delta 敞口 -39k shares
Top ΔOI: C 36 +1,466 ｜ P 35 +994 ｜ C 37 +840
仓位参考: Max Pain 38 ｜ Call Wall 36（+6.7%，弱）（OI 1.5k） ｜ Put Wall 35（+3.7%）（OI 2.5k）
量化解读： 存量 Call 重｜ATM IV 184.7%｜历史 Rank 100%（近端代理）｜IV/RV 3.45×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 38,737 股

📆 11-13 Forward Structure
存量OI: C 7.1k / P 3.0k，今日变化ΔOI: C +0.8k / P +72，平值价格ATM: C $2.35 / P $2.00 ｜ ATM IV 98.5%，净 delta 敞口 13k shares
仓位参考: Max Pain 40 ｜ Call Wall 35（+3.7%，弱）（OI 0.5k） ｜ Put Wall 35（+3.7%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 98.5%｜历史 Rank 100%（近端代理）｜IV/RV 1.84×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 13,089 股

📆 11-20 Forward Structure
存量OI: C 19.6k / P 13.2k，今日变化ΔOI: C +2.2k / P +0.7k，平值价格ATM: C $2.08 / P $3.25 ｜ ATM IV 92.0%，净 delta 敞口 -37k shares
Top ΔOI: P 42 +248 ｜ P 32 +131
仓位参考: Max Pain 44 ｜ Put Wall 35（+3.7%）（OI 3.7k）
量化解读： 存量 Call 重｜ATM IV 92.0%｜历史 Rank 100%（近端代理）｜IV/RV 1.72×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 37,298 股

📆 11-27 Forward Structure
存量OI: C 4.9k / P 1.2k，今日变化ΔOI: C +0.1k / P +0.2k，平值价格ATM: C $2.78 / P $2.80 ｜ ATM IV 82.3%，净 delta 敞口 -6k shares
Top ΔOI: P 31 +70 ｜ P 42 +66 ｜ C 36 +44
仓位参考: Max Pain 44 ｜ Put Wall 31（-8.1%，弱）（OI 71）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 82.3%｜历史 Rank 100%（近端代理）｜IV/RV 1.54×（近似）｜净 delta 敞口 负 5,857 股

📅 事件差分（观察，非因果）: 11-06（1D）ATM IV 184.7% vs 11-13 98.5%（差 +86.2pp）——覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=85 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=85）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-05/MP_evening.json