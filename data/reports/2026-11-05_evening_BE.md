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
🔴 **事件差分**: 11-06（1D）ATM IV 198.9% vs 11-13 139.3%（差 +59.5pp），覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Vol Regime 升档**: ELEVATED → STRESS（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-06 167C ΔOI -1,050（距现价 -0.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 188.00 → 收盘 167.52（-10.9%） ｜ 今日高 188.80 ｜ 低 156.00 ｜ 昨收 200.40 → 收盘 167.52（-16.4%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-12，窗口结束前不做对错判定）

Options: P/C成交量 0.86 | OI比 0.62 | ATM IV 198.9% | Skew 20.4pp | Term 0.54 | ExpMove ±8.5%（近端） | Rank 97%
量化视角： IV 历史高位（Rank 97%，期权偏贵）｜期限结构倒挂（Term 0.54，近月 IV 高于远月）｜保护溢价显著（Skew 20.4pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.62）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.86×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.62×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（1D）±8.5% ｜ 11-13（8D）±16.5% ｜ 11-20（15D）±18.8% ｜ 11-27（22D）±22.2%
   ⇒ IV–VIX Spread: +170.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -8,415,530 | GEX Change vs 上次快照 1,407,596 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 490 / LOW 136 / INVALID 272
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: NO_CROSS
量化视角： 负 Gamma（842万，无历史分位）｜负 Gamma 缓解（+141万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 210（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-06  C +5.5k / P +0.4k ｜ Activity HIGH ｜ 1D
11-13  C +1.7k / P +1.8k ｜ Activity HIGH ｜ 8D
11-20  C +2.2k / P -41 ｜ Activity MEDIUM △ ｜ 15D
11-27  C +0.3k / P +0.3k ｜ Activity MEDIUM △ ｜ 22D

📆 11-06 Forward Structure
存量OI: C 54.7k / P 33.7k，今日变化ΔOI: C +5.5k / P +0.4k，平值价格ATM: C $7.10 / P $7.08 ｜ ATM IV 198.9%，净 delta 敞口 -35k shares
Top ΔOI: C 167 -1,050
仓位参考: Max Pain 210 ｜ Call Wall 175（+4.5%，弱）（OI 1.4k） ｜ Put Wall 180（+7.4%，弱）（OI 1.4k）
量化解读： 存量 Call 重｜ATM IV 198.9%｜历史 Rank 97%（近端代理）｜IV/RV 2.10×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 34,982 股

📆 11-13 Forward Structure
存量OI: C 15.0k / P 14.3k，今日变化ΔOI: C +1.7k / P +1.8k，平值价格ATM: C $13.92 / P $13.67 ｜ ATM IV 139.3%，净 delta 敞口 -66k shares
Top ΔOI: C 195 +338 ｜ P 155 +260
仓位参考: Max Pain 228 ｜ Put Wall 160（-4.5%，弱）（OI 0.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 139.3%｜历史 Rank 97%（近端代理）｜IV/RV 1.47×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 65,758 股

11-20（MEDIUM △）Top ΔOI: 205P -1,050 ｜ 220C +585
11-20（MEDIUM △）仓位参考: Max Pain 228 ｜ Call Wall 180（+7.4%，弱）（OI 1.2k） ｜ Put Wall 170（+1.5%，弱）（OI 4.3k）

11-27（MEDIUM △）Top ΔOI: 200P +132 ｜ 210P +101
11-27（MEDIUM △）仓位参考: Max Pain 225

📅 事件差分（观察，非因果）: 11-06（1D）ATM IV 198.9% vs 11-13 139.3%（差 +59.5pp）——覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location ? | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-05/BE_evening.json