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
🔴 **事件差分**: 11-06（1D）ATM IV 70.5% vs 11-13 46.9%（差 +23.6pp），覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🔴 **Vol Regime 升档**: ELEVATED → STRESS（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate


## XBI

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
XBI: 今开 157.45 → 收盘 148.40（-5.7%） ｜ 今日高 157.61 ｜ 低 148.25 ｜ 昨收 159.10 → 收盘 148.40（-6.7%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-10，窗口结束前不做对错判定）

Options: P/C成交量 1.01 | OI比 1.70 | ATM IV 70.5% | Skew -35.5pp | Term 0.56 | ExpMove ±3.1%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.56，近月 IV 高于远月）｜Put 保护异常便宜（Skew -35.5pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.01×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.70×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-06（1D）±3.1% ｜ 11-13（8D）±6.6% ｜ 11-20（15D）±6.3% ｜ 11-27（22D）±2.2%
   ⇒ IV–VIX Spread: +42.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -16,889,940 | GEX Change vs 上次快照 -7,950,861 | Flip: Primary Flip: 158.50（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 331 / LOW 100 / INVALID 351
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 158.50（全链重定价，覆盖 96%）
Put Wall 145（现价高于该位 2.3%）
最近结构参考: Put Wall 145（现价高于该位 2.3%）
量化视角： 负 Gamma（1689万，无历史分位）｜负 Gamma 加深（795万）｜现价位于 Flip 下方 6.37%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 145（Put Wall）；上方 153（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 159（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-06  C +0.2k / P +0.2k ｜ Activity MEDIUM △ ｜ 1D
11-13  C +0.1k / P +0.3k ｜ Activity MEDIUM △ ｜ 8D
11-20  C +0.8k / P -0.6k ｜ Activity HIGH ｜ 15D
11-27  C +0.1k / P +15 ｜ Activity HIGH ｜ 22D

📆 11-06 Forward Structure
存量OI: C 5.9k / P 10.1k，今日变化ΔOI: C +0.2k / P +0.2k，平值价格ATM: C $2.80 / P $1.80 ｜ ATM IV 70.5%，净 delta 敞口 -5k shares
Top ΔOI: C 157 +265 ｜ P 150 +192 ｜ P 153 -106
仓位参考: Max Pain 153 ｜ Call Wall 142（-4.3%）（OI 1.5k） ｜ Put Wall 153（+3.1%）（OI 3.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 70.5%｜历史 Rank 100%（近端代理）｜IV/RV 2.21×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 5,458 股

11-13（MEDIUM △）Top ΔOI: 156P +103 ｜ 155P +82
11-13（MEDIUM △）仓位参考: Max Pain 155 ｜ Call Wall 158（+6.5%，弱）（OI 0.4k） ｜ Put Wall 140（-5.7%）（OI 0.4k）

📆 11-20 Forward Structure
存量OI: C 24.1k / P 46.1k，今日变化ΔOI: C +0.8k / P -0.6k，平值价格ATM: C $7.10 / P $2.20 ｜ ATM IV 40.8%，净 delta 敞口 -10k shares
Top ΔOI: C 164 +874 ｜ P 153 +824
仓位参考: Max Pain 154 ｜ Put Wall 145（-2.3%，弱）（OI 8.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 40.8%｜历史 Rank 100%（近端代理）｜IV/RV 1.28×（近似）｜净 delta 敞口 负 10,100 股

📆 11-27 Forward Structure
存量OI: C 1.1k / P 1.5k，今日变化ΔOI: C +0.1k / P +15，平值价格ATM: C $0.00 / P $3.21 ｜ ATM IV 41.5%，净 delta 敞口 2k shares
Top ΔOI: C 157 +69 ｜ C 160 +52
仓位参考: Max Pain 158 ｜ Call Wall 152.5（+2.8%，弱）（OI 0.1k） ｜ Put Wall 156（+5.1%）（OI 0.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 41.5%｜历史 Rank 100%（近端代理）｜IV/RV 1.30×（近似）｜净 delta 敞口 正 2,300 股

📅 事件差分（观察，非因果）: 11-06（1D）ATM IV 70.5% vs 11-13 46.9%（差 +23.6pp）——覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=85 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=85）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-05/XBI_evening.json