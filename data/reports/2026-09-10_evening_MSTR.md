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
🟡 **单日价格波动**: -3.4%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **事件差分**: 09-11 ATM IV 85.1% vs 09-18 72.3%（差 +12.8pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 09-18 123P ΔOI +1,835（距现价 -4.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 128.46 → 收盘 128.56（+0.1%） ｜ 今日高 131.88 ｜ 低 126.91 ｜ 昨收 132.70 → 收盘 128.56（-3.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.28 | OI比 0.63 | ATM IV 85.1% | Skew -7.9pp | Term 0.83 | ExpMove ±3.6%（近端） | Rank 58%
量化视角： IV 中性（Rank 58%）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜Put 保护异常便宜（Skew -7.9pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.63）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.28×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.63×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（1D）±3.6% ｜ 09-18（8D）±8.4% ｜ 09-25（15D）±11.4% ｜ 10-02（22D）±13.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 18,525,370 | GEX Change vs 上次快照 -10,798,543 | Flip: Primary Flip: 123.42（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 809 / LOW 148 / INVALID 295
结构观察区: Primary Flip 123.42（全链重定价，覆盖 99%）
最近结构参考: Flip 123（现价高于该位 4.2%）
量化视角： 正 Gamma（1853万，无历史分位）｜正 Gamma 减弱（1080万）｜现价位于 Flip 上方 4.16%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 131（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 123（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 140.0C — Vol 11,162 | 最新价 $0.22 | OI 7764→10161 (ΔOI +2397张) | ΔOI/Volume 21.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2397张（+30.9% vs前日OI），连续性待观察（方向未知）
09-18 140.0C — Vol 6,215 | 最新价 $2.08 | OI 6670→8874 (ΔOI +2204张) | ΔOI/Volume 35.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2204张（+33.0% vs前日OI），连续性待观察（方向未知）
09-18 123.0P — Vol 4,075 | 最新价 $2.84 | OI 1080→2915 (ΔOI +1835张) | ΔOI/Volume 45.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1835张（+169.9% vs前日OI），连续性待观察（方向未知）
09-11 160.0C — Vol 2,035 | 最新价 $0.02 | OI 4761→6332 (ΔOI +1571张) | ΔOI/Volume 77.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1571张（+33.0% vs前日OI），连续性待观察（方向未知）
09-18 120.0P — Vol 4,587 | 最新价 $1.96 | OI 4458→5996 (ΔOI +1538张) | ΔOI/Volume 33.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1538张（+34.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 9,545 张（Put 3,373 / Call 6,172），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +8.5k / P +1.1k ｜ Activity MEDIUM △ ｜ 1D
09-18  C -3.0k / P +7.2k ｜ Activity MEDIUM △ ｜ 8D
09-25  C +1.0k / P +4.0k ｜ Activity HIGH ｜ 15D
10-02  C +0.4k / P +2.2k ｜ Activity HIGH ｜ 22D

📆 09-11 Forward Structure
存量OI:      C 252.8k / P 160.3k
今日变化ΔOI: C +8.5k / P +1.1k
平值价格ATM:  C 2.14 / P 2.45
隐含波动率 ATM IV:  85.1%
净 delta 敞口变化 ΔOI Δ Exposure*: 49k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 140 ｜ +2,397 ｜ $0.22 ｜ 名义 $52.7k* ｜ +8.9%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：140（+8.9%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 131（结算参考）
量化解读： 存量 Call 重｜ATM IV 85.1%｜历史 Rank 58%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 48,899 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（MEDIUM △）Top ΔOI: 100C -5,929 ｜ 140C +2,204
09-18（MEDIUM △）仓位参考: Max Pain 115（结算参考）

📆 09-25 Forward Structure
存量OI:      C 21.4k / P 37.3k
今日变化ΔOI: C +1.0k / P +4.0k
平值价格ATM:  C 7.35 / P 7.33
隐含波动率 ATM IV:  70.6%
净 delta 敞口变化 ΔOI Δ Exposure*: -14k shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 125（结算参考） ｜ Call Wall 140（+8.9%，弱）（OI 1.5k）
量化解读： 存量 Put 重｜ATM IV 70.6%｜历史 Rank 58%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 13,921 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 10-02 Forward Structure
存量OI:      C 19.4k / P 27.5k
今日变化ΔOI: C +0.4k / P +2.2k
平值价格ATM:  C 9.00 / P 8.48
隐含波动率 ATM IV:  70.2%
净 delta 敞口变化 ΔOI Δ Exposure*: -36k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 105 ｜ +391 ｜ $1.28 ｜ 名义 $50.0k* ｜ -18.3%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：105（-18.3%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 130（结算参考）
量化解读： 存量 Put 重｜ATM IV 70.2%｜历史 Rank 58%（近端代理）｜净 delta 敞口 负 35,877 股（方向不可观测）——方向不可观测，观察点，非方向信号

📅 事件差分（观察，非因果）: 09-11（1D）ATM IV 85.1% vs 09-18 72.3%（差 +12.8pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-10/MSTR_evening.json