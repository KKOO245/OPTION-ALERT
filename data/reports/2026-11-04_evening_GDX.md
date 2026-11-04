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
🔵 **期限 OI 集中**: 11-09 83C ΔOI +271 占该期限总 OI 13.6%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 81.92 → 收盘 84.59（+3.3%） ｜ 今日高 85.00 ｜ 低 81.56 ｜ 昨收 77.60 → 收盘 84.59（+9.0%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-11，窗口结束前不做对错判定）

Options: P/C成交量 0.31 | OI比 0.74 | ATM IV 77.0% | Skew 22.2pp | Term 0.53 | ExpMove ±2.8%（近端） | Rank 99%
量化视角： IV 历史高位（Rank 99%，期权偏贵）｜期限结构倒挂（Term 0.53，近月 IV 高于远月）｜保护溢价显著（Skew 22.2pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.74）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.31×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.74×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（2D）±2.8% ｜ 11-09（5D）±4.9% ｜ 11-11（7D）±7.1% ｜ 11-13（9D）±10.0%
   ⇒ IV–VIX Spread: +60.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 26,214,880 | GEX Change vs 上次快照 -23,267,253 | Flip: Primary Flip: 79.24（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 84%（带内） ｜ IV 有效性: VALID 501 / LOW 137 / INVALID 574
结构观察区: Primary Flip 79.24（全链重定价，覆盖 84%）
Call Wall 81（弱结构｜现价高于该位 4.4%）
最近结构参考: Call Wall 81（现价高于该位 4.4%）
量化视角： 正 Gamma（2621万，无历史分位）｜正 Gamma 减弱（2327万）｜现价位于 Flip 上方 6.75%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 78（MaxPain，仅结算参考） / 81（Call Wall，弱结构）。
• Gamma 区域：切换参考 79（全链重定价，覆盖 84%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-06  C +1.3k / P +0.6k ｜ Activity MEDIUM △ ｜ 2D
11-09  C +0.5k / P +0.2k ｜ Activity HIGH ｜ 5D
11-11  C +0.1k / P +68 ｜ Activity HIGH ｜ 7D
11-13  C +0.2k / P +0.5k ｜ Activity MEDIUM △ ｜ 9D

📆 11-06 Forward Structure
存量OI: C 95.0k / P 30.9k，今日变化ΔOI: C +1.3k / P +0.6k，平值价格ATM: C $1.00 / P $1.37 ｜ ATM IV 45.9%，净 delta 敞口 127k shares
Top ΔOI: P 78 +441 ｜ C 83 +350 ｜ C 82 +252
仓位参考: Max Pain 78 ｜ Call Wall 81（-4.2%，弱）（OI 22.7k） ｜ Put Wall 80（-5.4%，弱）（OI 2.2k）
量化解读： 存量 Call 重｜ATM IV 45.9%｜历史 Rank 99%（近端代理）｜IV/RV 1.09×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 126,881 股

📆 11-09 Forward Structure
存量OI: C 1.3k / P 0.7k，今日变化ΔOI: C +0.5k / P +0.2k，平值价格ATM: C $1.35 / P $2.81 ｜ ATM IV 37.2%，净 delta 敞口 36k shares
Top ΔOI: C 83 +271 ｜ C 82 +82 ｜ C 78 +75
仓位参考: Max Pain 78 ｜ Call Wall 83（-1.9%）（OI 0.4k） ｜ Put Wall 84（-0.7%，弱）（OI 51）
量化解读： 存量 Call 重｜ATM IV 37.2%｜历史 Rank 99%（近端代理）｜IV/RV 0.88×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 36,121 股

📆 11-11 Forward Structure
存量OI: C 2.7k / P 1.3k，今日变化ΔOI: C +0.1k / P +68，平值价格ATM: C $1.89 / P $4.15 ｜ ATM IV 40.9%，净 delta 敞口 8k shares
Top ΔOI: C 83 +62 ｜ P 77 +22
仓位参考: Max Pain 78 ｜ Call Wall 85（+0.5%）（OI 1.9k）
量化解读： 存量 Call 重｜ATM IV 40.9%｜历史 Rank 99%（近端代理）｜IV/RV 0.97×（近似）｜净 delta 敞口 正 7,956 股

11-13（MEDIUM △）Top ΔOI: 79P +220
11-13（MEDIUM △）仓位参考: Max Pain 82 ｜ Call Wall 84.5（-0.1%，弱）（OI 0.6k） ｜ Put Wall 80（-5.4%，弱）（OI 0.8k）

📅 事件差分（观察，非因果）: 11-06（2D）ATM IV 45.9% vs 11-09 37.2%（差 +8.7pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-04/GDX_evening.json