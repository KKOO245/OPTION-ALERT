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
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **事件差分**: 11-06 ATM IV 49.0% vs 11-13 38.8%（差 +10.2pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-13 160C ΔOI +105（距现价 +0.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## XBI

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
XBI: 今开 158.35 → 收盘 159.10（+0.5%） ｜ 今日高 159.30 ｜ 低 152.65 ｜ 昨收 154.97 → 收盘 159.10（+2.7%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-11，窗口结束前不做对错判定）

Options: P/C成交量 1.87 | OI比 1.74 | ATM IV 49.0% | Skew 8.7pp | Term 0.72 | ExpMove ±2.7%（近端） | Rank 97%
量化视角： IV 历史高位（Rank 97%，期权偏贵）｜期限结构倒挂（Term 0.72，近月 IV 高于远月）｜保护溢价显著（Skew 8.7pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 1.87）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.87×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.74×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-06（2D）±2.7% ｜ 11-13（9D）±4.3% ｜ 11-20（16D）±6.9% ｜ 11-27（23D）±8.5%
   ⇒ IV–VIX Spread: +32.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 716,011 | GEX Change vs 上次快照 9,559,123 | Flip: Primary Flip: 158.69（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 305 / LOW 92 / INVALID 375
结构观察区: Primary Flip 158.69（全链重定价，覆盖 96%）
Call Wall 165（现价低于该位 3.6%）
最近结构参考: Flip 159（现价高于该位 0.3%）
量化视角： 正 Gamma（72万，无历史分位）｜由负转正（+956万）｜现价位于 Flip 上方 0.26%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 153（MaxPain，仅结算参考）；上方 165（Call Wall）。
• Gamma 区域：切换参考 159（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-06  C +0.1k / P +0.2k ｜ Activity MEDIUM △ ｜ 2D
11-13  C +0.4k / P +0.3k ｜ Activity HIGH ｜ 9D
11-20  C -0.1k / P +0.8k ｜ Activity MEDIUM △ ｜ 16D
11-27  C +8 / P +0.1k ｜ Activity MEDIUM △ ｜ 23D

📆 11-06 Forward Structure
存量OI: C 5.7k / P 9.9k，今日变化ΔOI: C +0.1k / P +0.2k，平值价格ATM: C $1.25 / P $3.11 ｜ ATM IV 49.0%，净 delta 敞口 -1k shares
Top ΔOI: C 162 +55 ｜ P 154 +51
仓位参考: Max Pain 153 ｜ Call Wall 159（-0.1%，弱）（OI 0.4k） ｜ Put Wall 153（-3.8%）（OI 3.1k）
量化解读： 存量 Put 重｜ATM IV 49.0%｜历史 Rank 97%（近端代理）｜IV/RV 1.59×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,332 股

📆 11-13 Forward Structure
存量OI: C 2.5k / P 2.3k，今日变化ΔOI: C +0.4k / P +0.3k，平值价格ATM: C $2.72 / P $4.10 ｜ ATM IV 38.8%，净 delta 敞口 8k shares
Top ΔOI: C 165 +116 ｜ P 146 +111 ｜ C 160 +105
仓位参考: Max Pain 153 ｜ Call Wall 160（+0.6%，弱）（OI 0.6k） ｜ Put Wall 153（-3.8%，弱）（OI 0.2k）
量化解读： 存量两侧均衡｜ATM IV 38.8%｜历史 Rank 97%（近端代理）｜IV/RV 1.26×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 7,892 股

11-20（MEDIUM △）Top ΔOI: 150P +389 ｜ 160C +278
11-20（MEDIUM △）仓位参考: Max Pain 155 ｜ Call Wall 165（+3.7%）（OI 6.9k）

11-27（MEDIUM △）Top ΔOI: 155P +51 ｜ 165P +51
11-27（MEDIUM △）仓位参考: Max Pain 158 ｜ Call Wall 167.5（+5.3%，弱）（OI 0.1k） ｜ Put Wall 156（-1.9%）（OI 0.2k）

📅 事件差分（观察，非因果）: 11-06（2D）ATM IV 49.0% vs 11-13 38.8%（差 +10.2pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-04/XBI_evening.json