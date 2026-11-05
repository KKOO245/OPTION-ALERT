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
🔴 **Vol Regime 升档**: ELEVATED → STRESS（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **事件差分**: 11-06 ATM IV 115.6% vs 11-13 105.0%（差 +10.6pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🔵 **期限 OI 集中**: 11-27 12C ΔOI +4,003 占该期限总 OI 78.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 10.48 → 收盘 9.64（-8.1%） ｜ 今日高 10.83 ｜ 低 9.29 ｜ 昨收 10.95 → 收盘 9.64（-12.0%）
Target 等待验证: 3D_mdd >= 0.03（3D） — PENDING（评估日 ≈ 2026-11-10，窗口结束前不做对错判定）

Options: P/C成交量 1.18 | OI比 0.44 | ATM IV 115.6% | Skew 9.9pp | Term 0.78 | ExpMove ±6.2%（近端） | Rank 64%
量化视角： IV 中性（Rank 64%）｜期限结构倒挂（Term 0.78，近月 IV 高于远月）｜保护溢价显著（Skew 9.9pp，Put 明显贵于 Call）｜⚠️ 重点观察：存量 Call 重（OI比 0.44）+ 当日成交偏 Put（P/C量 1.18）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.18×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.44×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（1D）±6.2% ｜ 11-13（8D）±4.5% ｜ 11-20（15D）±14.5% ｜ 11-27（22D）±16.3%
   ⇒ IV–VIX Spread: +87.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 478,565 | GEX Change vs 上次快照 303,356 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 105 / LOW 91 / INVALID 212
结构观察区: NO_CROSS
量化视角： 正 Gamma（48万，无历史分位）｜正 Gamma 增强（+30万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 12（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-06  C +0.2k / P -0.3k ｜ Activity MEDIUM △ ｜ 1D
11-13  C +0.3k / P +0.2k ｜ Activity MEDIUM △ ｜ 8D
11-20  C +46 / P +5 ｜ Activity MEDIUM △ ｜ 15D
11-27  C +4.0k / P +10 ｜ Activity HIGH ｜ 22D

📆 11-06 Forward Structure
存量OI: C 3.6k / P 1.6k，今日变化ΔOI: C +0.2k / P -0.3k，平值价格ATM: C $0.55 / P $0.05 ｜ ATM IV 115.6%，净 delta 敞口 28k shares
仓位参考: Max Pain 12
量化解读： 存量 Call 重｜ATM IV 115.6%｜历史 Rank 64%（近端代理）｜IV/RV 1.87×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 28,316 股

11-13（MEDIUM △）仓位参考: Max Pain 12 ｜ Put Wall 10.5（+9.0%，弱）（OI 0.2k）

11-20（MEDIUM △）Top ΔOI: 10P +30
11-20（MEDIUM △）仓位参考: Max Pain 15 ｜ Put Wall 9（-6.6%，弱）（OI 0.2k）

📆 11-27 Forward Structure
存量OI: C 4.5k / P 0.7k，今日变化ΔOI: C +4.0k / P +10，平值价格ATM: C $0.65 / P $0.92 ｜ ATM IV 91.4%，净 delta 敞口 63k shares
Top ΔOI: C 12 +4,003 ｜ C 10 +10
仓位参考: Max Pain 12
量化解读： 存量 Call 重｜ATM IV 91.4%｜历史 Rank 64%（近端代理）｜IV/RV 1.48×（近似）｜净 delta 敞口 正 62,533 股

📅 事件差分（观察，非因果）: 11-06（1D）ATM IV 115.6% vs 11-13 105.0%（差 +10.6pp）——覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime DOWN | Location ? | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-05/NNE_evening.json