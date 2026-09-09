# 期权晨报 2026-09-09（快照 11:03 ET）

📊 市场环境

SPY $762.70 ｜ QQQ $716.31
VIX 16.06 ↑2.2%（5D +5.7%） ｜ Vol Regime: NORMAL
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
🟡 **单日价格波动**: +3.5%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **事件差分**: 09-11 ATM IV 53.0% vs 09-14 40.5%（差 +12.5pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 09-16 64C ΔOI +1,566（距现价 +4.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 59.37 → 今开 61.17（+3.0%） | 较昨收变动（含盘初走势） ｜ 今日高 61.69 ｜ 低 60.67

Options: P/C成交量 0.70 | OI比 0.72 | ATM IV 57.5% | Skew -2.9pp | Term 0.79 | ExpMove ±3.4%（近端） | Rank 89%
量化视角： IV 历史高位（Rank 89%，期权偏贵）｜期限结构倒挂（Term 0.79，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.9pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.72）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.70×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.72×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（2D）±3.4% ｜ 09-14（5D）±4.0% ｜ 09-16（7D）±5.2% ｜ 09-18（9D）±5.7%
   ⇒ IV–VIX Spread: +41.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 161,354,916 | GEX Change vs 上次快照 67,473,142 | Flip: Primary Flip: 56.40（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1007 / LOW 217 / INVALID 406
结构观察区: Primary Flip 56.40（全链重定价，覆盖 99%）
最近结构参考: Flip 56（现价高于该位 9.0%）
量化视角： 正 Gamma（1.61亿，无历史分位）｜正 Gamma 增强（+6747万）｜现价位于 Flip 上方 8.96%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 60（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 56（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-09 60.0C — Vol 7,529 | 最新价 $0.27 | OI 2603→4481 (ΔOI +1878张) | ΔOI/Volume 24.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1878张（+72.2% vs前日OI），连续性待观察（方向未知）
09-09 62.0C — Vol 2,734 | 最新价 $0.03 | OI 2898→4607 (ΔOI +1709张) | ΔOI/Volume 62.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1709张（+59.0% vs前日OI），连续性待观察（方向未知）
09-16 64.0C — Vol 1,610 | 最新价 $0.30 | OI 66→1632 (ΔOI +1566张) | ΔOI/Volume 97.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1566张（+2372.7% vs前日OI），连续性待观察（方向未知）
09-09 62.5C — Vol 2,418 | 最新价 $0.01 | OI 3460→4987 (ΔOI +1527张) | ΔOI/Volume 63.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1527张（+44.1% vs前日OI），连续性待观察（方向未知）
09-09 59.5P — Vol 2,888 | 最新价 $0.59 | OI 2198→3534 (ΔOI +1336张) | ΔOI/Volume 46.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1336张（+60.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 8,016 张（Put 1,336 / Call 6,680），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +5.3k / P +4.0k ｜ Activity HIGH ｜ 2D
09-14  C +2.4k / P +1.1k ｜ Activity HIGH ｜ 5D
09-16  C +2.5k / P +0.4k ｜ Activity HIGH ｜ 7D
09-18  C -10.8k / P +0.3k ｜ Activity HIGH ｜ 9D

📆 09-11 Forward Structure
存量OI:      C 74.6k / P 42.7k
今日变化ΔOI: C +5.3k / P +4.0k
平值价格ATM:  C 1.03 / P 1.03
隐含波动率 ATM IV:  53.0%
净 delta 敞口变化 ΔOI Δ Exposure*: 68k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 66 ｜ +1,146 ｜ $0.09 ｜ 名义 $10.3k* ｜ +8.2%
C 66 ｜ +904 ｜ $0.10 ｜ 名义 $9.0k* ｜ +7.4%
P 58 ｜ +796 ｜ $0.11 ｜ 名义 $8.8k* ｜ -5.6%
结构参考：66（+8.2%） / 58（-5.6%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 60（结算参考） ｜ Put Wall 56（-8.9%）（OI 9.0k）
量化解读： 存量 Call 重｜ATM IV 53.0%｜历史 Rank 89%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 68,159 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-14 Forward Structure
存量OI:      C 4.6k / P 2.8k
今日变化ΔOI: C +2.4k / P +1.1k
平值价格ATM:  C 1.46 / P 0.97
隐含波动率 ATM IV:  40.5%
净 delta 敞口变化 ΔOI Δ Exposure*: 63k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 65 ｜ +1,245 ｜ $0.27 ｜ 名义 $33.6k* ｜ +5.8%
P 60 ｜ +390 ｜ $0.53 ｜ 名义 $20.7k* ｜ -2.4%
C 62 ｜ +348 ｜ $0.97 ｜ 名义 $33.8k* ｜ +0.9%
结构参考：65（+5.8%） / 60（-2.4%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 60（结算参考） ｜ Call Wall 65（+5.8%）（OI 1.4k） ｜ Put Wall 60（-2.4%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 40.5%｜历史 Rank 89%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 63,363 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-16 Forward Structure
存量OI:      C 4.8k / P 1.9k
今日变化ΔOI: C +2.5k / P +0.4k
平值价格ATM:  C 1.91 / P 1.31
隐含波动率 ATM IV:  44.3%
净 delta 敞口变化 ΔOI Δ Exposure*: 74k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 64 ｜ +1,566 ｜ $0.70 ｜ 名义 $109.6k* ｜ +4.1%
C 60 ｜ +268 ｜ $2.39 ｜ 名义 $64.1k* ｜ -2.4%
C 63 ｜ +210 ｜ $0.95 ｜ 名义 $19.9k* ｜ +2.5%
结构参考：64（+4.1%） / 60（-2.4%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 59（结算参考） ｜ Call Wall 64（+4.1%）（OI 1.6k） ｜ Put Wall 59（-4.0%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 44.3%｜历史 Rank 89%（近端代理）｜净 delta 敞口 正 73,893 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 976.3k / P 456.5k
今日变化ΔOI: C -10.8k / P +0.3k
平值价格ATM:  C 1.74 / P 1.74
隐含波动率 ATM IV:  45.5%
净 delta 敞口变化 ΔOI Δ Exposure*: -304k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 63 ｜ -10,106 ｜ $1.21 ｜ 名义 $-1.22M* ｜ +2.5%
C 65 ｜ -1,783 ｜ $0.71 ｜ 名义 $-126.6k* ｜ +5.8%
P 59 ｜ +1,198 ｜ $0.74 ｜ 名义 $88.7k* ｜ -4.0%
结构参考：59（-4.0%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 60（结算参考）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 45.5%｜历史 Rank 89%（近端代理）｜净 delta 敞口 负 303,585 股（方向不可观测）——方向不可观测，观察点，非方向信号

📅 事件差分（观察，非因果）: 09-11（2D）ATM IV 53.0% vs 09-14 40.5%（差 +12.5pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-09/SLV_morning.json