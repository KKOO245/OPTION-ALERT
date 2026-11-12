# 期权晚报 2026-11-12（快照 16:40 ET）

📊 市场环境

SPY $757.12 ｜ QQQ $688.17
VIX 18.70 ↑6.9%（5D -33.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 39.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-12

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 3.75 ｜ 前值 3.97　✅ 今日已公布
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 129.97 → 收盘 130.67（+0.5%） ｜ 今日高 135.07 ｜ 低 129.62 ｜ 昨收 136.27 → 收盘 130.67（-4.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.27 | OI比 0.48 | ATM IV 78.5% | Skew -0.9pp | Term 0.89 | ExpMove ±3.3%（近端） | Rank 57%
量化视角： IV 中性（Rank 57%）｜期限结构倒挂（Term 0.89，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.9pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.48）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.27×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.48×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（1D）±3.3% ｜ 11-20（8D）±8.4% ｜ 11-27（15D）±10.7% ｜ 12-04（22D）±12.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 371,900 | GEX Change vs 上次快照 186,324 | Flip: Primary Flip: 130.58（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 410 / LOW 224 / INVALID 358
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 130.58（全链重定价，覆盖 96%）
Call Wall 140（弱结构｜现价低于该位 6.7%）
最近结构参考: Flip 131（现价高于该位 0.1%）
量化视角： 正 Gamma（37万，无历史分位）｜正 Gamma 增强（+19万）｜现价位于 Flip 上方 0.07%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 137（MaxPain，仅结算参考） / 140（Call Wall，弱结构）。
• Gamma 区域：切换参考 131（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +4.1k / P -0.2k ｜ Activity HIGH ｜ 1D
11-20  C +4.0k / P +0.7k ｜ Activity MEDIUM △ ｜ 8D
11-27  C +0.5k / P +0.2k ｜ Activity HIGH ｜ 15D
12-04  C +0.2k / P +0.4k ｜ Activity MEDIUM △ ｜ 22D

📆 11-13 Forward Structure
存量OI: C 76.6k / P 37.2k，今日变化ΔOI: C +4.1k / P -0.2k，平值价格ATM: C $2.00 / P $2.30 ｜ ATM IV 78.5%，净 delta 敞口 55k shares
Top ΔOI: C 140 +873
仓位参考: Max Pain 137 ｜ Call Wall 141（+7.9%，弱）（OI 9.3k） ｜ Put Wall 130（-0.5%，弱）（OI 2.2k）
量化解读： 存量 Call 重｜ATM IV 78.5%｜历史 Rank 57%（近端代理）｜IV/RV 1.16×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 54,748 股

11-20（MEDIUM △）Top ΔOI: 150C +2,475
11-20（MEDIUM △）仓位参考: Max Pain 155 ｜ Call Wall 140（+7.1%，弱）（OI 2.4k） ｜ Put Wall 120（-8.2%）（OI 7.3k）

📆 11-27 Forward Structure
存量OI: C 6.2k / P 8.4k，今日变化ΔOI: C +0.5k / P +0.2k，平值价格ATM: C $6.97 / P $6.98 ｜ ATM IV 65.0%，净 delta 敞口 7k shares
Top ΔOI: C 140 +91
仓位参考: Max Pain 142 ｜ Call Wall 140（+7.1%，弱）（OI 0.4k） ｜ Put Wall 120（-8.2%，弱）（OI 0.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 65.0%｜历史 Rank 57%（近端代理）｜IV/RV 0.96×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 7,478 股

12-04（MEDIUM △）仓位参考: Max Pain 140 ｜ Call Wall 140（+7.1%）（OI 1.4k） ｜ Put Wall 135（+3.3%）（OI 2.2k）

📅 事件差分（观察，非因果）: 11-13（1D）ATM IV 78.5% vs 11-20 71.2%（差 +7.3pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-12/COIN_evening.json