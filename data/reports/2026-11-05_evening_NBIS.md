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


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 134.16 → 收盘 120.37（-10.3%） ｜ 今日高 134.80 ｜ 低 113.30 ｜ 昨收 141.52 → 收盘 120.37（-14.9%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-12，窗口结束前不做对错判定）

Options: P/C成交量 1.01 | OI比 0.47 | ATM IV 199.1% | Skew 18.2pp | Term 0.66 | ExpMove ±8.4%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.66，近月 IV 高于远月）｜保护溢价显著（Skew 18.2pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.47）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.01×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.47×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（1D）±8.4% ｜ 11-13（8D）±22.4% ｜ 11-20（15D）±25.8% ｜ 11-27（22D）±27.3%
   ⇒ IV–VIX Spread: +171.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -10,349,289 | GEX Change vs 上次快照 506,987 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 566 / LOW 76 / INVALID 160
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: NO_CROSS
Put Wall 115（弱结构｜现价高于该位 4.7%）
最近结构参考: Put Wall 115（现价高于该位 4.7%）
量化视角： 负 Gamma（1035万，无历史分位）｜负 Gamma 缓解（+51万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 115（Put Wall，弱结构）；上方 150（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-06  C +5.6k / P -2.5k ｜ Activity HIGH ｜ 1D
11-13  C +5.0k / P +1.3k ｜ Activity HIGH ｜ 8D
11-20  C +0.6k / P -1.0k ｜ Activity MEDIUM △ ｜ 15D
11-27  C +0.7k / P +0.3k ｜ Activity HIGH ｜ 22D

📆 11-06 Forward Structure
存量OI: C 89.9k / P 42.4k，今日变化ΔOI: C +5.6k / P -2.5k，平值价格ATM: C $5.22 / P $4.84 ｜ ATM IV 199.1%，净 delta 敞口 344k shares
Top ΔOI: P 200 -1,824
仓位参考: Max Pain 150 ｜ Put Wall 130（+8.0%，弱）（OI 3.1k）
量化解读： 存量 Call 重｜ATM IV 199.1%｜历史 Rank 100%（近端代理）｜IV/RV 1.97×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 344,107 股

📆 11-13 Forward Structure
存量OI: C 42.8k / P 30.0k，今日变化ΔOI: C +5.0k / P +1.3k，平值价格ATM: C $13.96 / P $13.00 ｜ ATM IV 191.8%，净 delta 敞口 -14k shares
Top ΔOI: C 160 +741
仓位参考: Max Pain 185 ｜ Put Wall 130（+8.0%，弱）（OI 2.7k）
量化解读： 存量 Call 重｜ATM IV 191.8%｜历史 Rank 100%（近端代理）｜IV/RV 1.90×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 13,758 股

11-20（MEDIUM △）Top ΔOI: 200C +597 ｜ 170C -449
11-20（MEDIUM △）仓位参考: Max Pain 180 ｜ Put Wall 115（-4.5%）（OI 11.9k）

📆 11-27 Forward Structure
存量OI: C 11.1k / P 10.3k，今日变化ΔOI: C +0.7k / P +0.3k，平值价格ATM: C $17.04 / P $15.80 ｜ ATM IV 142.4%，净 delta 敞口 -11k shares
Top ΔOI: P 175 +136
仓位参考: Max Pain 180 ｜ Put Wall 130（+8.0%，弱）（OI 0.4k）
量化解读： 存量两侧均衡｜ATM IV 142.4%｜历史 Rank 100%（近端代理）｜IV/RV 1.41×（近似）｜净 delta 敞口 负 11,332 股

📅 事件差分（观察，非因果）: 11-06（1D）ATM IV 199.1% vs 11-13 191.8%（差 +7.3pp）——覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location ? | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-05/NBIS_evening.json