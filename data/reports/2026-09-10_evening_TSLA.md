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
🟡 **事件差分**: 09-11 ATM IV 48.3% vs 09-14 34.4%（差 +13.9pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 09-11 360P ΔOI +4,446（距现价 -1.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 360.40 → 收盘 363.56（+0.9%） ｜ 今日高 369.21 ｜ 低 357.68 ｜ 昨收 367.81 → 收盘 363.56（-1.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.78 | OI比 0.87 | ATM IV 48.3% | Skew -0.8pp | Term 0.84 | ExpMove ±2.0%（近端） | Rank 34%
量化视角： IV 中性（Rank 34%）｜期限结构倒挂（Term 0.84，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.8pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.78×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.87×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-11（1D）±2.0% ｜ 09-14（4D）±2.9% ｜ 09-16（6D）±4.0% ｜ 09-18（8D）±4.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 45,544,546 | GEX Change vs 上次快照 -41,153,844 | Flip: Primary Flip: 358.63（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1017 / LOW 173 / INVALID 808
结构观察区: Primary Flip 358.63（全链重定价，覆盖 99%）
Put Wall 340（弱结构｜现价高于该位 6.9%）
最近结构参考: Flip 359（现价高于该位 1.4%）
量化视角： 正 Gamma（4554万，无历史分位）｜正 Gamma 减弱（4115万）｜现价位于 Flip 上方 1.37%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 340（Put Wall，弱结构） / 360（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 359（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 360.0P — Vol 98,671 | 最新价 $2.12 | OI 5093→9539 (ΔOI +4446张) | ΔOI/Volume 4.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4446张（+87.3% vs前日OI），连续性待观察（方向未知）
09-11 370.0C — Vol 92,855 | 最新价 $1.50 | OI 15128→19432 (ΔOI +4304张) | ΔOI/Volume 4.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4304张（+28.4% vs前日OI），连续性待观察（方向未知）
09-11 375.0C — Vol 64,329 | 最新价 $0.65 | OI 5823→9785 (ΔOI +3962张) | ΔOI/Volume 6.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3962张（+68.0% vs前日OI），连续性待观察（方向未知）
09-11 410.0C — Vol 4,576 | 最新价 $0.02 | OI 2774→6648 (ΔOI +3874张) | ΔOI/Volume 84.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3874张（+139.7% vs前日OI），连续性待观察（方向未知）
09-11 372.5C — Vol 39,827 | 最新价 $0.99 | OI 2987→6797 (ΔOI +3810张) | ΔOI/Volume 9.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3810张（+127.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 20,396 张（Put 4,446 / Call 15,950），跨 1 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +40.9k / P +29.5k ｜ Activity HIGH ｜ 1D
09-14  C +7.2k / P +7.5k ｜ Activity HIGH ｜ 4D
09-16  C +3.3k / P +1.9k ｜ Activity HIGH ｜ 6D
09-18  C +7.6k / P +7.9k ｜ Activity MEDIUM △ ｜ 8D

📆 09-11 Forward Structure
存量OI:      C 251.8k / P 218.6k
今日变化ΔOI: C +40.9k / P +29.5k
平值价格ATM:  C 4.38 / P 3.05
隐含波动率 ATM IV:  48.3%
净 delta 敞口变化 ΔOI Δ Exposure*: -428k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 360 ｜ +4,446 ｜ $2.12 ｜ 名义 $942.6k* ｜ -1.0%
C 370 ｜ +4,304 ｜ $1.50 ｜ 名义 $645.6k* ｜ +1.8%
C 375 ｜ +3,962 ｜ $0.65 ｜ 名义 $257.5k* ｜ +3.1%
结构参考：370（+1.8%） / 360（-1.0%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 360（结算参考） ｜ Call Wall 370（+1.8%，弱）（OI 19.4k）
量化解读： 存量两侧均衡｜ATM IV 48.3%｜历史 Rank 34%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 428,245 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-14 Forward Structure
存量OI:      C 23.5k / P 24.5k
今日变化ΔOI: C +7.2k / P +7.5k
平值价格ATM:  C 5.95 / P 4.64
隐含波动率 ATM IV:  34.4%
净 delta 敞口变化 ΔOI Δ Exposure*: -24k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 375 ｜ +1,407 ｜ $1.63 ｜ 名义 $229.3k* ｜ +3.1%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：375（+3.1%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 365（结算参考） ｜ Call Wall 370（+1.8%，弱）（OI 2.8k）
量化解读： 存量两侧均衡｜ATM IV 34.4%｜历史 Rank 34%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 负 23,505 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-16 Forward Structure
存量OI:      C 11.6k / P 8.1k
今日变化ΔOI: C +3.3k / P +1.9k
平值价格ATM:  C 8.04 / P 6.70
隐含波动率 ATM IV:  39.5%
净 delta 敞口变化 ΔOI Δ Exposure*: 22k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 370 ｜ +1,026 ｜ $4.80 ｜ 名义 $492.5k* ｜ +1.8%
C 385 ｜ +397 ｜ $1.46 ｜ 名义 $58.0k* ｜ +5.9%
P 360 ｜ +370 ｜ $5.70 ｜ 名义 $210.9k* ｜ -1.0%
结构参考：370（+1.8%） / 360（-1.0%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 360（结算参考） ｜ Call Wall 370（+1.8%）（OI 1.7k） ｜ Put Wall 360（-1.0%，弱）（OI 1.1k）
量化解读： 存量 Call 重｜ATM IV 39.5%｜历史 Rank 34%（近端代理）｜净 delta 敞口 正 21,643 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（MEDIUM △）Top ΔOI: 390C +1,735 ｜ 350P +1,366
09-18（MEDIUM △）仓位参考: Max Pain 370（结算参考）

📅 事件差分（观察，非因果）: 09-11（1D）ATM IV 48.3% vs 09-14 34.4%（差 +13.9pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-10/TSLA_evening.json