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
🔴 **事件差分**: 09-11（1D）ATM IV 89.8% vs 09-18 73.0%（差 +16.8pp），覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 132.70 → 今开 128.46（-3.2%） | 较昨收变动（含盘初走势） ｜ 今日高 131.88 ｜ 低 126.91

Options: P/C成交量 0.28 | OI比 0.63 | ATM IV 89.8% | Skew -9.0pp | Term 0.79 | ExpMove ±4.2%（近端） | Rank 65%
量化视角： IV 中性（Rank 65%）｜期限结构倒挂（Term 0.79，近月 IV 高于远月）｜Put 保护异常便宜（Skew -9.0pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.63）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.28×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.63×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（1D）±4.2% ｜ 09-18（8D）±8.8% ｜ 09-25（15D）±12.1% ｜ 10-02（22D）±14.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 29,323,914 | GEX Change vs 上次快照 -20,789,448 | Flip: Primary Flip: 123.99（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 841 / LOW 137 / INVALID 274
结构观察区: Primary Flip 123.99（全链重定价，覆盖 100%）
最近结构参考: Flip 124（现价高于该位 5.6%）
量化视角： 正 Gamma（2932万，无历史分位）｜正 Gamma 减弱（2079万）｜现价位于 Flip 上方 5.56%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 131（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 124（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 140.0C — Vol 7,399 | 最新价 $1.24 | OI 7764→10161 (ΔOI +2397张) | ΔOI/Volume 32.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2397张（+30.9% vs前日OI），连续性待观察（方向未知）
09-18 140.0C — Vol 5,501 | 最新价 $3.70 | OI 6670→8874 (ΔOI +2204张) | ΔOI/Volume 40.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2204张（+33.0% vs前日OI），连续性待观察（方向未知）
09-18 123.0P — Vol 2,258 | 最新价 $2.21 | OI 1080→2915 (ΔOI +1835张) | ΔOI/Volume 81.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1835张（+169.9% vs前日OI），连续性待观察（方向未知）
09-11 160.0C — Vol 6,099 | 最新价 $0.07 | OI 4761→6332 (ΔOI +1571张) | ΔOI/Volume 25.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1571张（+33.0% vs前日OI），连续性待观察（方向未知）
09-18 120.0P — Vol 2,258 | 最新价 $1.55 | OI 4458→5996 (ΔOI +1538张) | ΔOI/Volume 68.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1538张（+34.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 9,545 张（Put 3,373 / Call 6,172），跨 2 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +8.5k / P +1.1k ｜ Activity MEDIUM △ ｜ 1D
09-18  C -3.0k / P +7.2k ｜ Activity HIGH ｜ 8D
09-25  C +1.0k / P +4.0k ｜ Activity HIGH ｜ 15D
10-02  C +0.4k / P +2.2k ｜ Activity MEDIUM △ ｜ 22D

📆 09-11 Forward Structure
存量OI:      C 252.8k / P 160.3k
今日变化ΔOI: C +8.5k / P +1.1k
平值价格ATM:  C 2.70 / P 2.80
隐含波动率 ATM IV:  89.8%
净 delta 敞口变化 ΔOI Δ Exposure*: 112k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 140 ｜ +2,397 ｜ $0.53 ｜ 名义 $127.0k* ｜ +7.0%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：140（+7.0%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 131（结算参考）
量化解读： 存量 Call 重｜ATM IV 89.8%｜历史 Rank 65%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 111,995 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 271.0k / P 211.0k
今日变化ΔOI: C -3.0k / P +7.2k
平值价格ATM:  C 5.74 / P 5.74
隐含波动率 ATM IV:  73.0%
净 delta 敞口变化 ΔOI Δ Exposure*: -763k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 100 ｜ -5,929 ｜ $30.30 ｜ 名义 $-17.96M* ｜ -23.6%
C 140 ｜ +2,204 ｜ $2.80 ｜ 名义 $617.1k* ｜ +7.0%
P 123 ｜ +1,835 ｜ $2.35 ｜ 名义 $431.2k* ｜ -6.0%
结构参考：140（+7.0%） / 123（-6.0%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 115（结算参考）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 73.0%｜历史 Rank 65%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 762,922 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-25 Forward Structure
存量OI:      C 21.4k / P 37.3k
今日变化ΔOI: C +1.0k / P +4.0k
平值价格ATM:  C 7.69 / P 8.10
隐含波动率 ATM IV:  71.2%
净 delta 敞口变化 ΔOI Δ Exposure*: -6k shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 125（结算参考） ｜ Call Wall 140（+7.0%，弱）（OI 1.5k）
量化解读： 存量 Put 重｜ATM IV 71.2%｜历史 Rank 65%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 5,592 股（方向不可观测）——方向不可观测，观察点，非方向信号

10-02（MEDIUM △）仓位参考: Max Pain 130（结算参考）

📅 事件差分（观察，非因果）: 09-11（1D）ATM IV 89.8% vs 09-18 73.0%（差 +16.8pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-10/MSTR_morning.json