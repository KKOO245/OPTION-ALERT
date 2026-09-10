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
🟡 **近现价集中开仓**: 09-11 692P ΔOI +3,176（距现价 -2.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-15 650P ΔOI +7,917 占该期限总 OI 12.6%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 707.57 → 收盘 708.69（+0.2%） ｜ 今日高 712.06 ｜ 低 706.85 ｜ 昨收 716.31 → 收盘 708.69（-1.1%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-09-15，窗口结束前不做对错判定）

Options: P/C成交量 1.12 | OI比 1.73 | ATM IV 12.2% | Skew 0.7pp | Term 1.65 | ExpMove ±1.1%（近端） | Rank 16%
量化视角： IV 历史低位（Rank 16%，期权偏便宜）｜期限结构正常偏陡（Term 1.65）｜保护溢价薄（Skew 0.7pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.12×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.73×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 13% ｜ P/C OI(近端) 58%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 13%）｜近端持仓结构中性（P/C OI 分位 58%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-11（1D）±1.1% ｜ 09-14（4D）±1.5% ｜ 09-15（5D）±1.7% ｜ 09-16（6D）±2.1%
   ⇒ IV–VIX Spread: -5.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -690,270,768 | GEX Change vs 上次快照 -113,805,114 | Flip: Primary Flip: 719.78（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 2276 / LOW 568 / INVALID 3118
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 719.78（全链重定价，覆盖 94%）
Put Wall 700（弱结构｜现价高于该位 1.2%） | Call Wall 750（弱结构｜现价低于该位 5.5%）
最近结构参考: Put Wall 700（现价高于该位 1.2%）
量化视角： 负 Gamma（6.90亿，历史分位偏负区，比 87% 的交易日更负）｜负 Gamma 加深（1.14亿）｜现价位于 Flip 下方 1.54%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 700（Put Wall，弱结构）；上方 717（MaxPain，仅结算参考） / 750（Call Wall，弱结构）。
• Gamma 区域：切换参考 720（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-30 695.0P — Vol 398 | 最新价 $8.35 | OI 22392→31603 (ΔOI +9211张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9211张（+41.1% vs前日OI），连续性待观察（方向未知）
09-30 705.0P — Vol 1,358 | 最新价 $11.25 | OI 28507→37456 (ΔOI +8949张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8949张（+31.4% vs前日OI），连续性待观察（方向未知）
09-15 650.0P — Vol 7,752 | 最新价 $0.14 | OI 481→8398 (ΔOI +7917张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7917张（+1646.0% vs前日OI），连续性待观察（方向未知）
09-10 722.0C — Vol 13,151 | 最新价 $0.01 | OI 3230→8956 (ΔOI +5726张) | ΔOI/Volume 43.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5726张（+177.3% vs前日OI），连续性待观察（方向未知）
09-10 720.0C — Vol 22,004 | 最新价 $0.01 | OI 2449→7761 (ΔOI +5312张) | ΔOI/Volume 24.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5312张（+216.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 37,115 张（Put 26,077 / Call 11,038），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $18M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +25.8k / P +27.5k ｜ Activity HIGH ｜ 1D
09-14  C +3.6k / P +11.9k ｜ Activity HIGH ｜ 4D
09-15  C +3.0k / P +19.3k ｜ Activity HIGH ｜ 5D
09-16  C +3.6k / P +9.5k ｜ Activity HIGH ｜ 6D

📆 09-11 Forward Structure
存量OI:      C 192.8k / P 310.7k
今日变化ΔOI: C +25.8k / P +27.5k
平值价格ATM:  C 4.00 / P 3.72
隐含波动率 ATM IV:  25.9%
净 delta 敞口变化 ΔOI Δ Exposure*: -308k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 692 ｜ +3,176 ｜ $0.28 ｜ 名义 $88.9k* ｜ -2.4%
C 729 ｜ +2,407 ｜ $0.03 ｜ 名义 $7.2k* ｜ +2.9%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：729（+2.9%） / 692（-2.4%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 716（结算参考） ｜ Call Wall 750（+5.8%，弱）（OI 12.6k） ｜ Put Wall 705（-0.5%，弱）（OI 26.4k）
量化解读： 存量 Put 重｜ATM IV 25.9%｜历史 Rank 16%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 308,427 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-14 Forward Structure
存量OI:      C 18.9k / P 55.7k
今日变化ΔOI: C +3.6k / P +11.9k
平值价格ATM:  C 5.35 / P 5.21
隐含波动率 ATM IV:  17.2%
净 delta 敞口变化 ΔOI Δ Exposure*: -66k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 655 ｜ +3,610 ｜ $0.10 ｜ 名义 $36.1k* ｜ -7.6%
C 745 ｜ +1,387 ｜ $0.02 ｜ 名义 $2.8k* ｜ +5.1%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：745（+5.1%） / 655（-7.6%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 715（结算参考） ｜ Call Wall 725（+2.3%，弱）（OI 3.1k） ｜ Put Wall 655（-7.6%）（OI 11.5k）
量化解读： 存量 Put 重｜ATM IV 17.2%｜历史 Rank 16%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 负 66,222 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-15 Forward Structure
存量OI:      C 13.5k / P 49.5k
今日变化ΔOI: C +3.0k / P +19.3k
平值价格ATM:  C 6.26 / P 5.90
隐含波动率 ATM IV:  18.2%
净 delta 敞口变化 ΔOI Δ Exposure*: -70k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 650 ｜ +7,917 ｜ $0.14 ｜ 名义 $110.8k* ｜ -8.3%
P 655 ｜ +3,756 ｜ $0.19 ｜ 名义 $71.4k* ｜ -7.6%
C 725 ｜ +1,048 ｜ $0.68 ｜ 名义 $71.3k* ｜ +2.3%
结构参考：725（+2.3%） / 650（-8.3%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 715（结算参考） ｜ Call Wall 730（+3.0%，弱）（OI 2.9k） ｜ Put Wall 650（-8.3%，弱）（OI 8.4k）
量化解读： 存量 Put 重｜ATM IV 18.2%｜历史 Rank 16%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 负 69,790 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-16 Forward Structure
存量OI:      C 8.2k / P 18.5k
今日变化ΔOI: C +3.6k / P +9.5k
平值价格ATM:  C 7.67 / P 7.20
隐含波动率 ATM IV:  20.3%
净 delta 敞口变化 ΔOI Δ Exposure*: -89k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 730 ｜ +1,063 ｜ $0.62 ｜ 名义 $65.9k* ｜ +3.0%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：730（+3.0%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 715（结算参考） ｜ Call Wall 730（+3.0%，弱）（OI 1.6k）
量化解读： 存量 Put 重｜ATM IV 20.3%｜历史 Rank 16%（近端代理）｜净 delta 敞口 负 88,881 股（方向不可观测）——方向不可观测，观察点，非方向信号

📅 事件差分（观察，非因果）: 09-11（1D）ATM IV 25.9% vs 09-14 17.2%（差 +8.7pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=14 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=14）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-10/QQQ_evening.json