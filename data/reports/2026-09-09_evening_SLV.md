# 期权晚报 2026-09-09（快照 18:23 ET）

📊 市场环境

SPY $762.40 ｜ QQQ $716.31
VIX 16.46 ↑4.7%（5D +8.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 39.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-10 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0
- 周四 09-10 10:00　【高】成屋销售　预测 3.98 ｜ 实际 待公布 ｜ 前值 4.06
- 周五 09-11 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.2
- 周五 09-11 08:30　【高】Inflation Rate MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.1
- 周五 09-11 08:30　【高】Inflation Rate YoY　预测 3.4 ｜ 实际 待公布 ｜ 前值 3.4
- 周五 09-11 08:30　【高】Core Inflation Rate YoY　预测 2.4 ｜ 实际 待公布 ｜ 前值 2.5
- 周五 09-11 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 51 ｜ 实际 待公布 ｜ 前值 51.7

🔍 重点速览
🟡 **单日价格波动**: +2.5%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **事件差分**: 09-11 ATM IV 51.1% vs 09-14 38.6%（差 +12.5pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 61.17 → 收盘 60.72（-0.7%） ｜ 今日高 61.71 ｜ 低 60.16 ｜ 昨收 59.37 → 收盘 60.72（+2.3%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-09-16，窗口结束前不做对错判定）

Options: P/C成交量 0.64 | OI比 0.72 | ATM IV 48.8% | Skew -13.0pp | Term 0.90 | ExpMove ±3.1%（近端） | Rank 81%
量化视角： IV 历史高位（Rank 81%，期权偏贵）｜期限结构正常（Term 0.90）｜Put 保护异常便宜（Skew -13.0pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.72）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.64×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.72×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（2D）±3.1% ｜ 09-14（5D）±3.6% ｜ 09-16（7D）±4.7% ｜ 09-18（9D）±5.6%
   ⇒ IV–VIX Spread: +32.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 138,189,209 | GEX Change vs 上次快照 -23,165,707 | Flip: Primary Flip: 55.90（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 1040 / LOW 187 / INVALID 403
结构观察区: Primary Flip 55.90（全链重定价，覆盖 97%）
最近结构参考: Flip 56（现价高于该位 8.6%）
量化视角： 正 Gamma（1.38亿，无历史分位）｜正 Gamma 减弱（2317万）｜现价位于 Flip 上方 8.62%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 60（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 56（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-09 60.0C — Vol 5,697 | 最新价 $0.70 | OI 2603→4481 (ΔOI +1878张) | ΔOI/Volume 33.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1878张（+72.2% vs前日OI），连续性待观察（方向未知）
09-09 62.0C — Vol 15,066 | 最新价 $0.01 | OI 2898→4607 (ΔOI +1709张) | ΔOI/Volume 11.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1709张（+59.0% vs前日OI），连续性待观察（方向未知）
09-16 64.0C — Vol 228 | 最新价 $0.48 | OI 66→1632 (ΔOI +1566张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1566张（+2372.7% vs前日OI），连续性待观察（方向未知）
09-09 62.5C — Vol 4,725 | 最新价 $0.01 | OI 3460→4987 (ΔOI +1527张) | ΔOI/Volume 32.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1527张（+44.1% vs前日OI），连续性待观察（方向未知）
09-09 59.5P — Vol 8,039 | 最新价 $0.01 | OI 2198→3534 (ΔOI +1336张) | ΔOI/Volume 16.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1336张（+60.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 8,016 张（Put 1,336 / Call 6,680），跨 2 个期限｜彩票/名义 1 档（价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-14  C +0 / P +0 ｜ Activity LOW ｜ 5D
09-16  C +0 / P +0 ｜ Activity LOW ｜ 7D
09-18  C +0 / P +0 ｜ Activity LOW ｜ 9D

📆 09-11 Forward Structure
存量OI:      C 74.6k / P 42.7k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 1.05 / P 0.81
隐含波动率 ATM IV:  51.1%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 60（结算参考） ｜ Put Wall 56（-7.8%）（OI 9.0k）
量化解读： 存量 Call 重｜ATM IV 51.1%｜历史 Rank 81%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-14（Activity LOW）仓位参考: Max Pain 60（结算参考） ｜ Call Wall 65（+7.0%）（OI 1.4k） ｜ Put Wall 60（-1.2%，弱）（OI 0.5k）

09-16（Activity LOW）仓位参考: Max Pain 59（结算参考） ｜ Call Wall 64（+5.4%）（OI 1.6k） ｜ Put Wall 59（-2.8%，弱）（OI 0.4k）

09-18（Activity LOW）仓位参考: Max Pain 60（结算参考）

📅 事件差分（观察，非因果）: 09-11（2D）ATM IV 51.1% vs 09-14 38.6%（差 +12.5pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-09/SLV_evening.json