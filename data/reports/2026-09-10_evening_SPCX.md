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
🟡 **事件差分**: 09-11 ATM IV 66.2% vs 09-18 54.7%（差 +11.5pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 09-11 152P ΔOI -6,941（距现价 +2.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPCX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPCX: 今开 145.10 → 收盘 148.18（+2.1%） ｜ 今日高 154.70 ｜ 低 144.89 ｜ 昨收 147.55 → 收盘 148.18（+0.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.54 | OI比 1.43 | ATM IV 66.2% | Skew -0.8pp | Term 0.79 | ExpMove ±2.8%（近端） | Rank 65%
量化视角： IV 中性（Rank 65%）｜期限结构倒挂（Term 0.79，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.8pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.54×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.43×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-11（1D）±2.8% ｜ 09-18（8D）±6.6% ｜ 09-25（15D）±8.6% ｜ 10-02（22D）±10.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 32,366,113 | GEX Change vs 上次快照 -30,542,774 | Flip: Primary Flip: 146.29（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 602 / LOW 166 / INVALID 336
结构观察区: Primary Flip 146.29（全链重定价，覆盖 100%）
Call Wall 150（弱结构｜现价低于该位 1.2%）
最近结构参考: Call Wall 150（现价低于该位 1.2%）
量化视角： 正 Gamma（3237万，无历史分位）｜正 Gamma 减弱（3054万）｜现价位于 Flip 上方 1.29%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 147（MaxPain，仅结算参考）；上方 150（Call Wall，弱结构）。
• Gamma 区域：切换参考 146（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 155.0C — Vol 37,422 | 最新价 $2.33 | OI 17299→55470 (ΔOI +38171张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增38171张（+220.7% vs前日OI），连续性待观察（方向未知）
09-18 150.0C — Vol 27,968 | 最新价 $4.05 | OI 44286→50058 (ΔOI +5772张) | ΔOI/Volume 20.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5772张（+13.0% vs前日OI），连续性待观察（方向未知）
09-18 165.0C — Vol 22,404 | 最新价 $0.70 | OI 23215→28808 (ΔOI +5593张) | ΔOI/Volume 25.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5593张（+24.1% vs前日OI），连续性待观察（方向未知）
09-11 147.0C — Vol 8,512 | 最新价 $2.75 | OI 1498→5016 (ΔOI +3518张) | ΔOI/Volume 41.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3518张（+234.8% vs前日OI），连续性待观察（方向未知）
09-11 152.5C — Vol 77,798 | 最新价 $0.66 | OI 6572→8898 (ΔOI +2326张) | ΔOI/Volume 3.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2326张（+35.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 55,380 张（Put 0 / Call 55,380），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +16.2k / P -15.1k ｜ Activity HIGH ｜ 1D
09-18  C +57.3k / P +2.6k ｜ Activity HIGH ｜ 8D
09-25  C +4.4k / P +1.4k ｜ Activity HIGH ｜ 15D
10-02  C +2.1k / P +3.4k ｜ Activity HIGH ｜ 22D

📆 09-11 Forward Structure
存量OI:      C 162.7k / P 231.8k
今日变化ΔOI: C +16.2k / P -15.1k
平值价格ATM:  C 2.19 / P 1.92
隐含波动率 ATM IV:  66.2%
净 delta 敞口变化 ΔOI Δ Exposure*: 1.5M shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 152 ｜ -6,941 ｜ $4.93 ｜ 名义 $-3.42M* ｜ +2.9%
P 150 ｜ -5,798 ｜ $3.09 ｜ 名义 $-1.79M* ｜ +1.2%
P 145 ｜ -4,713 ｜ $0.83 ｜ 名义 $-391.2k* ｜ -2.1%
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 147（结算参考） ｜ Call Wall 160（+8.0%）（OI 26.4k） ｜ Put Wall 140（-5.5%，弱）（OI 28.9k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 66.2%｜历史 Rank 65%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,458,253 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 590.1k / P 478.2k
今日变化ΔOI: C +57.3k / P +2.6k
平值价格ATM:  C 4.05 / P 5.68
隐含波动率 ATM IV:  54.7%
净 delta 敞口变化 ΔOI Δ Exposure*: 1.6M shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 155 ｜ +38,171 ｜ $2.33 ｜ 名义 $8.89M* ｜ +4.6%
C 150 ｜ +5,772 ｜ $4.05 ｜ 名义 $2.34M* ｜ +1.2%
C 165 ｜ +5,593 ｜ $0.70 ｜ 名义 $391.5k* ｜ +11.4%
结构参考：155（+4.6%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 145（结算参考） ｜ Call Wall 155（+4.6%，弱）（OI 55.5k） ｜ Put Wall 150（+1.2%，弱）（OI 45.8k）
量化解读： 存量 Call 重｜ATM IV 54.7%｜历史 Rank 65%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,627,440 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-25 Forward Structure
存量OI:      C 47.9k / P 65.7k
今日变化ΔOI: C +4.4k / P +1.4k
平值价格ATM:  C 6.65 / P 6.05
隐含波动率 ATM IV:  52.9%
净 delta 敞口变化 ΔOI Δ Exposure*: 91k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 170 ｜ +1,662 ｜ $1.00 ｜ 名义 $166.2k* ｜ +14.7%
C 160 ｜ +779 ｜ $2.50 ｜ 名义 $194.8k* ｜ +8.0%
C 148 ｜ +756 ｜ $6.65 ｜ 名义 $502.7k* ｜ -0.1%
结构参考：170（+14.7%） / 148（-0.1%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 144（结算参考）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 52.9%｜历史 Rank 65%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 91,377 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 10-02 Forward Structure
存量OI:      C 23.5k / P 35.3k
今日变化ΔOI: C +2.1k / P +3.4k
平值价格ATM:  C 7.95 / P 7.45
隐含波动率 ATM IV:  52.3%
净 delta 敞口变化 ΔOI Δ Exposure*: -14k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 130 ｜ +861 ｜ $1.67 ｜ 名义 $143.8k* ｜ -12.3%
C 170 ｜ +756 ｜ $1.70 ｜ 名义 $128.5k* ｜ +14.7%
P 147 ｜ +485 ｜ $6.98 ｜ 名义 $338.5k* ｜ -0.8%
结构参考：170（+14.7%） / 130（-12.3%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 145（结算参考）
量化解读： 存量 Put 重｜ATM IV 52.3%｜历史 Rank 65%（近端代理）｜净 delta 敞口 负 13,517 股（方向不可观测）——方向不可观测，观察点，非方向信号

📅 事件差分（观察，非因果）: 09-11（1D）ATM IV 66.2% vs 09-18 54.7%（差 +11.5pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-10/SPCX_evening.json