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
🔴 **事件差分**: 11-06（1D）ATM IV 73.9% vs 11-09 48.2%（差 +25.8pp），覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Vol Regime 升档**: ELEVATED → STRESS（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-06 89C ΔOI +2,386（距现价 +3.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 86.61 → 收盘 85.75（-1.0%） ｜ 今日高 87.96 ｜ 低 82.50 ｜ 昨收 84.59 → 收盘 85.75（+1.4%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-12，窗口结束前不做对错判定）

Options: P/C成交量 1.48 | OI比 0.33 | ATM IV 73.9% | Skew 1.6pp | Term 0.62 | ExpMove ±3.0%（近端） | Rank 99%
量化视角： IV 历史高位（Rank 99%，期权偏贵）｜期限结构倒挂（Term 0.62，近月 IV 高于远月）｜保护溢价薄（Skew 1.6pp）｜⚠️ 重点观察：存量 Call 重（OI比 0.33）+ 当日成交偏 Put（P/C量 1.48）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.48×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.33×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（1D）±3.0% ｜ 11-09（4D）±4.2% ｜ 11-11（6D）±6.3% ｜ 11-13（8D）±6.4%
   ⇒ IV–VIX Spread: +45.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 24,550,963 | GEX Change vs 上次快照 -6,645,051 | Flip: Primary Flip: 79.03（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 530 / LOW 125 / INVALID 485
结构观察区: Primary Flip 79.03（全链重定价，覆盖 92%）
Call Wall 81（弱结构｜现价高于该位 5.9%）
最近结构参考: Call Wall 81（现价高于该位 5.9%）
量化视角： 正 Gamma（2455万，无历史分位）｜正 Gamma 减弱（665万）｜现价位于 Flip 上方 8.50%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 78（MaxPain，仅结算参考） / 81（Call Wall，弱结构）。
• Gamma 区域：切换参考 79（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-06  C +3.7k / P +2.0k ｜ Activity HIGH ｜ 1D
11-09  C +0.4k / P +0.8k ｜ Activity HIGH ｜ 4D
11-11  C +1.2k / P +62 ｜ Activity HIGH ｜ 6D
11-13  C +5.0k / P +13.9k ｜ Activity HIGH ｜ 8D

📆 11-06 Forward Structure
存量OI: C 98.6k / P 33.0k，今日变化ΔOI: C +3.7k / P +2.0k，平值价格ATM: C $1.42 / P $1.17 ｜ ATM IV 73.9%，净 delta 敞口 -104k shares
Top ΔOI: C 89 +2,386 ｜ C 86 +1,388 ｜ C 88 +866
仓位参考: Max Pain 78 ｜ Call Wall 81（-5.5%，弱）（OI 21.9k） ｜ Put Wall 81（-5.5%，弱）（OI 1.3k）
量化解读： 存量 Call 重｜ATM IV 73.9%｜历史 Rank 99%（近端代理）｜IV/RV 1.38×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 104,345 股

📆 11-09 Forward Structure
存量OI: C 1.7k / P 1.4k，今日变化ΔOI: C +0.4k / P +0.8k，平值价格ATM: C $1.52 / P $2.05 ｜ ATM IV 48.2%，净 delta 敞口 12k shares
Top ΔOI: P 86 +131 ｜ C 85 +106
仓位参考: Max Pain 79 ｜ Call Wall 83（-3.2%）（OI 0.4k） ｜ Put Wall 86（+0.3%，弱）（OI 0.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 48.2%｜历史 Rank 99%（近端代理）｜IV/RV 0.90×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 11,582 股

📆 11-11 Forward Structure
存量OI: C 3.9k / P 1.4k，今日变化ΔOI: C +1.2k / P +62，平值价格ATM: C $2.14 / P $3.28 ｜ ATM IV 52.5%，净 delta 敞口 24k shares
Top ΔOI: C 94 +880 ｜ C 85 +239 ｜ P 82 +36
仓位参考: Max Pain 78 ｜ Call Wall 85（-0.9%）（OI 2.1k）
量化解读： 存量 Call 重｜ATM IV 52.5%｜历史 Rank 99%（近端代理）｜IV/RV 0.98×（近似）｜净 delta 敞口 正 23,699 股

📆 11-13 Forward Structure
存量OI: C 12.2k / P 23.1k，今日变化ΔOI: C +5.0k / P +13.9k，平值价格ATM: C $2.77 / P $2.71 ｜ ATM IV 54.0%，净 delta 敞口 -34k shares
Top ΔOI: P 79 +6,080 ｜ P 82 +3,251 ｜ C 88 +3,137
仓位参考: Max Pain 84 ｜ Call Wall 88.5（+3.2%）（OI 3.3k） ｜ Put Wall 82（-4.4%，弱）（OI 3.5k）
量化解读： 存量 Put 重｜ATM IV 54.0%｜历史 Rank 99%（近端代理）｜IV/RV 1.01×（近似）｜净 delta 敞口 负 33,508 股

📅 事件差分（观察，非因果）: 11-06（1D）ATM IV 73.9% vs 11-09 48.2%（差 +25.8pp）——覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-05/GDX_evening.json