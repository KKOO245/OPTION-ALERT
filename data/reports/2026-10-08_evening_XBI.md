# 期权晚报 2026-10-08（快照 16:40 ET）

📊 市场环境

SPY $773.93 ｜ QQQ $747.58
VIX 15.41 ↑2.2%（5D -6.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-08

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **事件差分**: 10-09 ATM IV 46.0% vs 10-16 35.3%（差 +10.7pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-09 155C ΔOI +117（距现价 +3.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## XBI

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
XBI: 今开 149.00 → 收盘 149.29（+0.2%） ｜ 今日高 149.69 ｜ 低 146.01 ｜ 昨收 150.23 → 收盘 149.29（-0.6%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-15，窗口结束前不做对错判定）

Options: P/C成交量 1.80 | OI比 2.26 | ATM IV 46.0% | Skew -1.0pp | Term 0.76 | ExpMove ±2.6%（近端） | Rank 95%
量化视角： IV 历史高位（Rank 95%，期权偏贵）｜期限结构倒挂（Term 0.76，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.0pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 1.80）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.80×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 2.26×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-09（1D）±2.6% ｜ 10-16（8D）±4.1% ｜ 10-23（15D）±4.9% ｜ 10-30（22D）±10.5%
   ⇒ IV–VIX Spread: +30.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -54,578,232 | GEX Change vs 上次快照 7,253,572 | Flip: Primary Flip: 164.44（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 312 / LOW 126 / INVALID 334
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 164.44（全链重定价，覆盖 95%）
Put Wall 150（现价低于该位 0.5%）
最近结构参考: Put Wall 150（现价低于该位 0.5%）
量化视角： 负 Gamma（5458万，无历史分位）｜负 Gamma 缓解（+725万）｜现价位于 Flip 下方 9.21%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 150（Put Wall） / 155（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 164（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +0.4k / P +0.4k ｜ Activity MEDIUM △ ｜ 1D
10-16  C -1.5k / P -4.0k ｜ Activity HIGH ｜ 8D
10-23  C +0.3k / P +95 ｜ Activity MEDIUM △ ｜ 15D
10-30  C +0.3k / P +0.2k ｜ Activity MEDIUM △ ｜ 22D

📆 10-09 Forward Structure
存量OI: C 6.0k / P 13.5k，今日变化ΔOI: C +0.4k / P +0.4k，平值价格ATM: C $1.56 / P $2.35 ｜ ATM IV 46.0%，净 delta 敞口 5k shares
Top ΔOI: C 153 +247 ｜ P 145 +206 ｜ C 155 +117
仓位参考: Max Pain 155 ｜ Call Wall 145（-2.9%）（OI 1.0k） ｜ Put Wall 148（-0.9%，弱）（OI 4.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 46.0%｜历史 Rank 95%（近端代理）｜IV/RV 1.77×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 5,399 股

📆 10-16 Forward Structure
存量OI: C 40.8k / P 74.8k，今日变化ΔOI: C -1.5k / P -4.0k，平值价格ATM: C $3.25 / P $2.90 ｜ ATM IV 35.3%，净 delta 敞口 224k shares
Top ΔOI: P 154 -2,245 ｜ P 144 -973 ｜ C 155 -955
仓位参考: Max Pain 160 ｜ Call Wall 155（+3.8%，弱）（OI 1.8k） ｜ Put Wall 150（+0.5%）（OI 22.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 35.3%｜历史 Rank 95%（近端代理）｜IV/RV 1.36×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 223,695 股

10-23（MEDIUM △）Top ΔOI: 145P +89 ｜ 164C +51
10-23（MEDIUM △）仓位参考: Max Pain 155 ｜ Call Wall 154（+3.2%，弱）（OI 89） ｜ Put Wall 140（-6.2%，弱）（OI 0.7k）

10-30（MEDIUM △）Top ΔOI: 145P +200
10-30（MEDIUM △）仓位参考: Max Pain 153 ｜ Call Wall 150（+0.5%，弱）（OI 0.1k） ｜ Put Wall 150（+0.5%，弱）（OI 7.6k）

📅 事件差分（观察，非因果）: 10-09（1D）ATM IV 46.0% vs 10-16 35.3%（差 +10.7pp）——覆盖 密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-08/XBI_evening.json