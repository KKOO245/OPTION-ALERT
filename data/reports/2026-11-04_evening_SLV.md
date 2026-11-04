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
🟡 **事件差分**: 11-06 ATM IV 49.0% vs 11-09 38.7%（差 +10.3pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-06 46C ΔOI +1,240（距现价 -2.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 46.78 → 收盘 47.16（+0.8%） ｜ 今日高 47.35 ｜ 低 46.73 ｜ 昨收 44.84 → 收盘 47.16（+5.2%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-11，窗口结束前不做对错判定）

Options: P/C成交量 0.44 | OI比 0.42 | ATM IV 65.0% | Skew -13.4pp | Term 0.61 | ExpMove ±2.9%（近端） | Rank 93%
量化视角： IV 历史高位（Rank 93%，期权偏贵）｜期限结构倒挂（Term 0.61，近月 IV 高于远月）｜Put 保护异常便宜（Skew -13.4pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.42）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.44×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.42×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（2D）±2.9% ｜ 11-09（5D）±3.4% ｜ 11-11（7D）±4.6% ｜ 11-13（9D）±5.4%
   ⇒ IV–VIX Spread: +48.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 44,294,570 | GEX Change vs 上次快照 -7,107,094 | Flip: Primary Flip: 45.12（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 717 / LOW 112 / INVALID 425
结构观察区: Primary Flip 45.12（全链重定价，覆盖 95%）
最近结构参考: Flip 45（现价高于该位 4.5%）
量化视角： 正 Gamma（4429万，无历史分位）｜正 Gamma 减弱（711万）｜现价位于 Flip 上方 4.51%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 44（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 45（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-06  C +5.5k / P +0.5k ｜ Activity MEDIUM △ ｜ 2D
11-09  C +3.4k / P +2.0k ｜ Activity HIGH ｜ 5D
11-11  C +3.9k / P +1.3k ｜ Activity HIGH ｜ 7D
11-13  C +2.8k / P +1.1k ｜ Activity HIGH ｜ 9D

📆 11-06 Forward Structure
存量OI: C 147.5k / P 40.7k，今日变化ΔOI: C +5.5k / P +0.5k，平值价格ATM: C $0.78 / P $0.60 ｜ ATM IV 49.0%，净 delta 敞口 377k shares
Top ΔOI: C 46 +1,240 ｜ C 49 +1,157 ｜ C 47 +907
仓位参考: Max Pain 47 ｜ Call Wall 50（+6.0%，弱）（OI 12.9k） ｜ Put Wall 45（-4.6%，弱）（OI 4.5k）
量化解读： 存量 Call 重｜ATM IV 49.0%｜历史 Rank 93%（近端代理）｜IV/RV 1.19×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 376,851 股

📆 11-09 Forward Structure
存量OI: C 7.9k / P 5.6k，今日变化ΔOI: C +3.4k / P +2.0k，平值价格ATM: C $0.88 / P $0.74 ｜ ATM IV 38.7%，净 delta 敞口 129k shares
Top ΔOI: C 49 +1,152 ｜ C 46 +724
仓位参考: Max Pain 46 ｜ Call Wall 49.5（+5.0%，弱）（OI 1.2k） ｜ Put Wall 43（-8.8%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 38.7%｜历史 Rank 93%（近端代理）｜IV/RV 0.94×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 129,123 股

📆 11-11 Forward Structure
存量OI: C 9.8k / P 3.2k，今日变化ΔOI: C +3.9k / P +1.3k，平值价格ATM: C $1.16 / P $1.02 ｜ ATM IV 41.8%，净 delta 敞口 85k shares
Top ΔOI: C 51 +1,021 ｜ C 50 +934 ｜ P 44 +593
仓位参考: Max Pain 45 ｜ Call Wall 51（+8.1%）（OI 2.6k） ｜ Put Wall 44（-6.7%，弱）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 41.8%｜历史 Rank 93%（近端代理）｜IV/RV 1.01×（近似）｜净 delta 敞口 正 85,270 股

📆 11-13 Forward Structure
存量OI: C 49.6k / P 22.5k，今日变化ΔOI: C +2.8k / P +1.1k，平值价格ATM: C $1.35 / P $1.19 ｜ ATM IV 42.3%，净 delta 敞口 112k shares
Top ΔOI: C 47 +968 ｜ C 50 +685
仓位参考: Max Pain 49 ｜ Call Wall 50（+6.0%，弱）（OI 5.6k） ｜ Put Wall 45（-4.6%，弱）（OI 2.9k）
量化解读： 存量 Call 重｜ATM IV 42.3%｜历史 Rank 93%（近端代理）｜IV/RV 1.03×（近似）｜净 delta 敞口 正 112,036 股

📅 事件差分（观察，非因果）: 11-06（2D）ATM IV 49.0% vs 11-09 38.7%（差 +10.3pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-04/SLV_evening.json