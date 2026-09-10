# 期权晨报 2026-09-10（快照 10:56 ET）

📊 市场环境

SPY $758.27 ｜ QQQ $708.69
VIX 17.34 ↑5.3%（5D +21.1%） ｜ Vol Regime: NORMAL
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
🟡 **近现价集中开仓**: 09-11 692P ΔOI +3,176（距现价 -2.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-15 650P ΔOI +7,917 占该期限总 OI 12.6%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 716.31 → 今开 707.57（-1.2%） | 较昨收变动（含盘初走势） ｜ 今日高 712.06 ｜ 低 706.85

Options: P/C成交量 0.92 | OI比 1.73 | ATM IV 22.7% | Skew 2.8pp | Term 0.87 | ExpMove ±1.1%（近端） | Rank 71%
量化视角： IV 中性（Rank 71%）｜期限结构倒挂（Term 0.87，近月 IV 高于远月）｜保护溢价中性（Skew 2.8pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.92×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.73×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 17% ｜ P/C OI(近端) 58%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 17%）｜近端持仓结构中性（P/C OI 分位 58%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-11（1D）±1.1% ｜ 09-14（4D）±1.4% ｜ 09-15（5D）±1.7% ｜ 09-16（6D）±2.0%
   ⇒ IV–VIX Spread: +5.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -576,465,654 | GEX Change vs 上次快照 -329,929,504 | Flip: Primary Flip: 719.66（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 2466 / LOW 491 / INVALID 3005
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 719.66（全链重定价，覆盖 96%）
Put Wall 700（弱结构｜现价高于该位 1.7%） | Call Wall 750（弱结构｜现价低于该位 5.1%）
最近结构参考: Flip 720（现价低于该位 1.1%）
量化视角： 负 Gamma（5.76亿，历史分位偏负区，比 83% 的交易日更负）｜负 Gamma 加深（3.30亿）｜现价位于 Flip 下方 1.09%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 700（Put Wall，弱结构）；上方 717（MaxPain，仅结算参考） / 750（Call Wall，弱结构）。
• Gamma 区域：切换参考 720（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-30 695.0P — Vol 10,268 | 最新价 $6.06 | OI 22392→31603 (ΔOI +9211张) | ΔOI/Volume 89.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9211张（+41.1% vs前日OI），连续性待观察（方向未知）
09-30 705.0P — Vol 10,126 | 最新价 $8.56 | OI 28507→37456 (ΔOI +8949张) | ΔOI/Volume 88.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8949张（+31.4% vs前日OI），连续性待观察（方向未知）
09-15 650.0P — Vol 8,417 | 最新价 $0.14 | OI 481→8398 (ΔOI +7917张) | ΔOI/Volume 94.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7917张（+1646.0% vs前日OI），连续性待观察（方向未知）
09-10 722.0C — Vol 14,390 | 最新价 $0.56 | OI 3230→8956 (ΔOI +5726张) | ΔOI/Volume 39.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5726张（+177.3% vs前日OI），连续性待观察（方向未知）
09-10 720.0C — Vol 40,531 | 最新价 $1.10 | OI 2449→7761 (ΔOI +5312张) | ΔOI/Volume 13.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5312张（+216.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 37,115 张（Put 26,077 / Call 11,038），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $13M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +25.8k / P +27.5k ｜ Activity HIGH ｜ 1D
09-14  C +3.6k / P +11.9k ｜ Activity HIGH ｜ 4D
09-15  C +3.0k / P +19.3k ｜ Activity HIGH ｜ 5D
09-16  C +3.6k / P +9.5k ｜ Activity HIGH ｜ 6D

📆 09-11 Forward Structure
存量OI:      C 192.8k / P 310.7k
今日变化ΔOI: C +25.8k / P +27.5k
平值价格ATM:  C 4.03 / P 4.15
隐含波动率 ATM IV:  24.7%
净 delta 敞口变化 ΔOI Δ Exposure*: -76k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 692 ｜ +3,176 ｜ $0.29 ｜ 名义 $92.1k* ｜ -2.8%
C 729 ｜ +2,407 ｜ $0.11 ｜ 名义 $26.5k* ｜ +2.4%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：729（+2.4%） / 692（-2.8%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 716（结算参考） ｜ Call Wall 750（+5.4%，弱）（OI 12.6k） ｜ Put Wall 705（-1.0%，弱）（OI 26.4k）
量化解读： 存量 Put 重｜ATM IV 24.7%｜历史 Rank 71%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 76,168 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-14 Forward Structure
存量OI:      C 18.9k / P 55.7k
今日变化ΔOI: C +3.6k / P +11.9k
平值价格ATM:  C 5.16 / P 5.15
隐含波动率 ATM IV:  16.9%
净 delta 敞口变化 ΔOI Δ Exposure*: -43k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 655 ｜ +3,610 ｜ $0.11 ｜ 名义 $39.7k* ｜ -8.0%
C 745 ｜ +1,387 ｜ $0.01 ｜ 名义 $1.4k* ｜ +4.7%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：745（+4.7%） / 655（-8.0%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 715（结算参考） ｜ Call Wall 725（+1.9%，弱）（OI 3.1k） ｜ Put Wall 655（-8.0%）（OI 11.5k）
量化解读： 存量 Put 重｜ATM IV 16.9%｜历史 Rank 71%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 负 42,635 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-15 Forward Structure
存量OI:      C 13.5k / P 49.5k
今日变化ΔOI: C +3.0k / P +19.3k
平值价格ATM:  C 5.98 / P 6.00
隐含波动率 ATM IV:  17.6%
净 delta 敞口变化 ΔOI Δ Exposure*: -43k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 650 ｜ +7,917 ｜ $0.19 ｜ 名义 $150.4k* ｜ -8.7%
P 655 ｜ +3,756 ｜ $0.15 ｜ 名义 $56.3k* ｜ -8.0%
C 725 ｜ +1,048 ｜ $1.20 ｜ 名义 $125.8k* ｜ +1.9%
结构参考：725（+1.9%） / 650（-8.7%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 715（结算参考） ｜ Call Wall 730（+2.6%，弱）（OI 2.9k） ｜ Put Wall 650（-8.7%，弱）（OI 8.4k）
量化解读： 存量 Put 重｜ATM IV 17.6%｜历史 Rank 71%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 负 42,937 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-16 Forward Structure
存量OI:      C 8.2k / P 18.5k
今日变化ΔOI: C +3.6k / P +9.5k
平值价格ATM:  C 7.06 / P 7.35
隐含波动率 ATM IV:  19.5%
净 delta 敞口变化 ΔOI Δ Exposure*: -58k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 730 ｜ +1,063 ｜ $1.03 ｜ 名义 $109.5k* ｜ +2.6%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：730（+2.6%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 715（结算参考） ｜ Call Wall 730（+2.6%，弱）（OI 1.6k）
量化解读： 存量 Put 重｜ATM IV 19.5%｜历史 Rank 71%（近端代理）｜净 delta 敞口 负 57,805 股（方向不可观测）——方向不可观测，观察点，非方向信号

📅 事件差分（观察，非因果）: 09-11（1D）ATM IV 24.7% vs 09-14 16.9%（差 +7.8pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=14 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=14）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-10/QQQ_morning.json