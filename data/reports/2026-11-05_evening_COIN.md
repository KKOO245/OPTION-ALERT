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
🔴 **事件差分**: 11-06（1D）ATM IV 116.8% vs 11-13 82.9%（差 +33.9pp），覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Vol Regime 升档**: ELEVATED → STRESS（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🔵 **期限 OI 集中**: 11-27 85P ΔOI +1,436 占该期限总 OI 12.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 149.00 → 收盘 136.82（-8.2%） ｜ 今日高 151.58 ｜ 低 133.51 ｜ 昨收 151.50 → 收盘 136.82（-9.7%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-12，窗口结束前不做对错判定）

Options: P/C成交量 1.29 | OI比 0.72 | ATM IV 116.8% | Skew 18.3pp | Term 0.66 | ExpMove ±4.9%（近端） | Rank 92%
量化视角： IV 历史高位（Rank 92%，期权偏贵）｜期限结构倒挂（Term 0.66，近月 IV 高于远月）｜保护溢价显著（Skew 18.3pp，Put 明显贵于 Call）｜⚠️ 重点观察：存量 Call 重（OI比 0.72）+ 当日成交偏 Put（P/C量 1.29）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.29×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.72×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（1D）±4.9% ｜ 11-13（8D）±9.5% ｜ 11-20（15D）±13.6% ｜ 11-27（22D）±14.9%
   ⇒ IV–VIX Spread: +88.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 8,383,631 | GEX Change vs 上次快照 -10,698,270 | Flip: Primary Flip: 134.09（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 351 / LOW 175 / INVALID 324
结构观察区: Primary Flip 134.09（全链重定价，覆盖 98%）
最近结构参考: Flip 134（现价高于该位 2.0%）
量化视角： 正 Gamma（838万，无历史分位）｜正 Gamma 减弱（1070万）｜现价位于 Flip 上方 2.04%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 142（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 134（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-06  C +2.4k / P -0.3k ｜ Activity MEDIUM △ ｜ 1D
11-13  C +1.3k / P +4.9k ｜ Activity HIGH ｜ 8D
11-20  C +0.5k / P +3.5k ｜ Activity HIGH ｜ 15D
11-27  C +0.1k / P +2.5k ｜ Activity HIGH ｜ 22D

📆 11-06 Forward Structure
存量OI: C 75.2k / P 53.9k，今日变化ΔOI: C +2.4k / P -0.3k，平值价格ATM: C $3.16 / P $3.55 ｜ ATM IV 116.8%，净 delta 敞口 -57k shares
Top ΔOI: C 144 +747
仓位参考: Max Pain 142 ｜ Call Wall 148（+8.2%，弱）（OI 8.5k） ｜ Put Wall 130（-5.0%，弱）（OI 4.6k）
量化解读： 存量 Call 重｜ATM IV 116.8%｜历史 Rank 92%（近端代理）｜IV/RV 1.76×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 56,891 股

📆 11-13 Forward Structure
存量OI: C 14.5k / P 24.4k，今日变化ΔOI: C +1.3k / P +4.9k，平值价格ATM: C $6.50 / P $6.50 ｜ ATM IV 82.9%，净 delta 敞口 -77k shares
Top ΔOI: P 146 +406
仓位参考: Max Pain 155 ｜ Call Wall 150（+9.6%，弱）（OI 0.7k） ｜ Put Wall 130（-5.0%，弱）（OI 1.1k）
量化解读： 存量 Put 重｜ATM IV 82.9%｜历史 Rank 92%（近端代理）｜IV/RV 1.25×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 76,993 股

📆 11-20 Forward Structure
存量OI: C 73.7k / P 60.8k，今日变化ΔOI: C +0.5k / P +3.5k，平值价格ATM: C $10.75 / P $7.80 ｜ ATM IV 79.5%，净 delta 敞口 -18k shares
Top ΔOI: P 120 +1,327
仓位参考: Max Pain 170 ｜ Put Wall 140（+2.3%，弱）（OI 3.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 79.5%｜历史 Rank 92%（近端代理）｜IV/RV 1.20×（近似）｜净 delta 敞口 负 18,407 股

📆 11-27 Forward Structure
存量OI: C 3.7k / P 7.7k，今日变化ΔOI: C +0.1k / P +2.5k，平值价格ATM: C $11.95 / P $8.47 ｜ ATM IV 79.9%，净 delta 敞口 -4k shares
Top ΔOI: P 110 -333
仓位参考: Max Pain 160 ｜ Call Wall 150（+9.6%，弱）（OI 0.1k） ｜ Put Wall 140（+2.3%，弱）（OI 0.3k）
量化解读： 存量 Put 重｜ATM IV 79.9%｜历史 Rank 92%（近端代理）｜IV/RV 1.20×（近似）｜净 delta 敞口 负 3,684 股

📅 事件差分（观察，非因果）: 11-06（1D）ATM IV 116.8% vs 11-13 82.9%（差 +33.9pp）——覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-05/COIN_evening.json