# 期权晚报 2026-09-10（快照 17:04 ET）

📊 市场环境

SPY $757.83 ｜ QQQ $708.69
VIX 17.84 ↑8.4%（5D +24.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-10 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 0.4 ｜ 前值 0.1　✅ 今日已公布
- 周四 09-10 10:00　【高】成屋销售　预测 3.98 ｜ 实际 3.98 ｜ 前值 4.06　✅ 今日已公布
- 周五 09-11 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.2
- 周五 09-11 08:30　【高】Inflation Rate MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.1
- 周五 09-11 08:30　【高】Inflation Rate YoY　预测 3.4 ｜ 实际 待公布 ｜ 前值 3.4
- 周五 09-11 08:30　【高】Core Inflation Rate YoY　预测 2.4 ｜ 实际 待公布 ｜ 前值 2.5
- 周五 09-11 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 51 ｜ 实际 待公布 ｜ 前值 51.7

🔍 重点速览
🔴 **事件差分**: 09-11（1D）ATM IV 64.6% vs 09-14 41.5%（差 +23.1pp），覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **单日价格波动**: -5.3%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-11 58P ΔOI +4,325（距现价 +0.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 58.42 → 收盘 57.50（-1.6%） ｜ 今日高 58.72 ｜ 低 57.38 ｜ 昨收 60.72 → 收盘 57.50（-5.3%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-09-17，窗口结束前不做对错判定）

Options: P/C成交量 0.80 | OI比 0.66 | ATM IV 64.6% | Skew -5.4pp | Term 0.68 | ExpMove ±2.7%（近端） | Rank 92%
量化视角： IV 历史高位（Rank 92%，期权偏贵）｜期限结构倒挂（Term 0.68，近月 IV 高于远月）｜Put 保护异常便宜（Skew -5.4pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.66）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.80×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.66×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（1D）±2.7% ｜ 09-14（4D）±3.6% ｜ 09-16（6D）±4.8% ｜ 09-18（8D）±5.6%
   ⇒ IV–VIX Spread: +46.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 36,235,785 | GEX Change vs 上次快照 -19,391,944 | Flip: Primary Flip: 55.99（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 952 / LOW 186 / INVALID 322
结构观察区: Primary Flip 55.99（全链重定价，覆盖 100%）
最近结构参考: Flip 56（现价高于该位 2.7%）
量化视角： 正 Gamma（3624万，无历史分位）｜正 Gamma 减弱（1939万）｜现价位于 Flip 上方 2.70%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 60（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 56（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 58.0P — Vol 4,601 | 最新价 $1.04 | OI 1742→6067 (ΔOI +4325张) | ΔOI/Volume 94.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4325张（+248.3% vs前日OI），连续性待观察（方向未知）
10-09 75.0C — Vol 88 | 最新价 $0.25 | OI 147→4461 (ΔOI +4314张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4314张（+2934.7% vs前日OI），连续性待观察（方向未知）
09-25 68.0C — Vol 4,066 | 最新价 $0.22 | OI 694→4640 (ΔOI +3946张) | ΔOI/Volume 97.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3946张（+568.6% vs前日OI），连续性待观察（方向未知）
09-25 60.5P — Vol 54 | 最新价 $3.85 | OI 91→3842 (ΔOI +3751张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3751张（+4122.0% vs前日OI），连续性待观察（方向未知）
09-11 60.0P — Vol 1,468 | 最新价 $2.65 | OI 1526→5090 (ΔOI +3564张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3564张（+233.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 19,900 张（Put 11,640 / Call 8,260），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $3M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +6.4k / P +10.5k ｜ Activity HIGH ｜ 1D
09-14  C +6.1k / P +2.2k ｜ Activity HIGH ｜ 4D
09-16  C +1.4k / P +1.9k ｜ Activity HIGH ｜ 6D
09-18  C -8.9k / P +6.8k ｜ Activity HIGH ｜ 8D

📆 09-11 Forward Structure
存量OI:      C 81.0k / P 53.2k
今日变化ΔOI: C +6.4k / P +10.5k
平值价格ATM:  C 0.78 / P 0.76
隐含波动率 ATM IV:  64.6%
净 delta 敞口变化 ΔOI Δ Exposure*: -711k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 58 ｜ +4,325 ｜ $1.04 ｜ 名义 $449.8k* ｜ +0.9%
P 60 ｜ +3,564 ｜ $2.65 ｜ 名义 $944.5k* ｜ +4.3%
C 60 ｜ -2,712 ｜ $0.14 ｜ 名义 $-38.0k* ｜ +4.3%
结构参考：58（+0.9%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 60（结算参考） ｜ Put Wall 56（-2.6%，弱）（OI 9.0k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 64.6%｜历史 Rank 92%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 711,119 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-14 Forward Structure
存量OI:      C 10.7k / P 4.9k
今日变化ΔOI: C +6.1k / P +2.2k
平值价格ATM:  C 1.33 / P 0.73
隐含波动率 ATM IV:  41.5%
净 delta 敞口变化 ΔOI Δ Exposure*: -83k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 58 ｜ +632 ｜ $1.26 ｜ 名义 $79.6k* ｜ +0.9%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：58（+0.9%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 60（结算参考） ｜ Put Wall 60（+4.3%，弱）（OI 0.9k）
量化解读： 存量 Call 重｜ATM IV 41.5%｜历史 Rank 92%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 负 83,000 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-16 Forward Structure
存量OI:      C 6.1k / P 3.8k
今日变化ΔOI: C +1.4k / P +1.9k
平值价格ATM:  C 1.62 / P 1.11
隐含波动率 ATM IV:  46.9%
净 delta 敞口变化 ΔOI Δ Exposure*: -77k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 54 ｜ +666 ｜ $0.30 ｜ 名义 $20.0k* ｜ -6.1%
P 61 ｜ +350 ｜ $3.91 ｜ 名义 $136.8k* ｜ +6.1%
P 60 ｜ +331 ｜ $3.10 ｜ 名义 $102.6k* ｜ +4.3%
结构参考：61（+6.1%） / 54（-6.1%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 60（结算参考） ｜ Put Wall 54（-6.1%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 46.9%｜历史 Rank 92%（近端代理）｜净 delta 敞口 负 77,395 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 967.5k / P 463.3k
今日变化ΔOI: C -8.9k / P +6.8k
平值价格ATM:  C 1.65 / P 1.59
隐含波动率 ATM IV:  47.8%
净 delta 敞口变化 ΔOI Δ Exposure*: -573k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 63 ｜ -6,100 ｜ $0.31 ｜ 名义 $-189.1k* ｜ +9.6%
P 57 ｜ +2,059 ｜ $1.35 ｜ 名义 $278.0k* ｜ -0.9%
P 57 ｜ +1,851 ｜ $1.59 ｜ 名义 $294.3k* ｜ +0.0%
结构参考：57（-0.9%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 60（结算参考）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 47.8%｜历史 Rank 92%（近端代理）｜净 delta 敞口 负 573,143 股（方向不可观测）——方向不可观测，观察点，非方向信号

📅 事件差分（观察，非因果）: 09-11（1D）ATM IV 64.6% vs 09-14 41.5%（差 +23.1pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-10/SLV_evening.json