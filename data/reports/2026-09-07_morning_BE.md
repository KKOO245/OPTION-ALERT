# 期权晨报 2026-09-07（快照 12:20 ET）

📊 市场环境

SPY $770.19 ｜ QQQ $718.96
VIX 15.30 ↑5.3%（5D +2.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 41.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-10 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0
- 周四 09-10 10:00　【高】成屋销售　预测 3.99 ｜ 实际 待公布 ｜ 前值 4.06
- 周五 09-11 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.2
- 周五 09-11 08:30　【高】Inflation Rate YoY　预测 3.4 ｜ 实际 待公布 ｜ 前值 3.4
- 周五 09-11 08:30　【高】Inflation Rate MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.1
- 周五 09-11 08:30　【高】Core Inflation Rate YoY　预测 2.4 ｜ 实际 待公布 ｜ 前值 2.5
- 周五 09-11 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 51 ｜ 实际 待公布 ｜ 前值 51.7

🔍 重点速览
🔴 **Vol Regime 升档**: LOW → NORMAL（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **单日价格波动**: +5.3%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **事件差分**: 09-11 ATM IV 109.1% vs 09-18 97.8%（差 +11.3pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 252.87 → 今开 236.82（-6.3%） | 较昨收变动（含盘初走势） ｜ 今日高 253.30 ｜ 低 235.55

Options: P/C成交量 0.50 | OI比 0.85 | ATM IV 109.1% | Skew -12.0pp | Term 0.82 | ExpMove ±12.3%（近端） | Rank 67%
量化视角： IV 中性（Rank 67%）｜期限结构倒挂（Term 0.82，近月 IV 高于远月）｜Put 保护异常便宜（Skew -12.0pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.85）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.50×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.85×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-11（4D）±12.3% ｜ 09-18（11D）±16.1% ｜ 09-25（18D）±17.4% ｜ 10-02（25D）±21.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 24,578,987 | GEX Change vs 上次快照 8,651,511 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 595 / LOW 63 / INVALID 88
结构观察区: NO_CROSS
Call Wall 250（现价高于该位 6.5%）
最近结构参考: Call Wall 250（现价高于该位 6.5%）
量化视角： 正 Gamma（2458万，无历史分位）｜正 Gamma 增强（+865万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 225（MaxPain，仅结算参考） / 250（Call Wall）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 280.0C — Vol 7,329 | 最新价 $6.29 | OI 995→3400 (ΔOI +2405张) | ΔOI/Volume 32.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2405张（+241.7% vs前日OI），连续性待观察（方向未知）
09-11 260.0C — Vol 4,874 | 最新价 $12.05 | OI 1026→3105 (ΔOI +2079张) | ΔOI/Volume 42.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2079张（+202.6% vs前日OI），连续性待观察（方向未知）
09-11 275.0C — Vol 3,860 | 最新价 $7.50 | OI 2451→4413 (ΔOI +1962张) | ΔOI/Volume 50.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1962张（+80.0% vs前日OI），连续性待观察（方向未知）
09-11 200.0P — Vol 2,474 | 最新价 $0.50 | OI 1255→2373 (ΔOI +1118张) | ΔOI/Volume 45.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1118张（+89.1% vs前日OI），连续性待观察（方向未知）
09-11 230.0P — Vol 1,755 | 最新价 $4.83 | OI 341→1459 (ΔOI +1118张) | ΔOI/Volume 63.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1118张（+327.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 8,682 张（Put 2,236 / Call 6,446），跨 1 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +11.9k / P +10.1k ｜ Activity HIGH ｜ 4D
09-18  C +2.2k / P +2.2k ｜ Activity MEDIUM △ ｜ 11D
09-25  C +0.8k / P +0.2k ｜ Activity HIGH ｜ 18D
10-02  C +0.8k / P +1.3k ｜ Activity HIGH ｜ 25D

📆 09-11 Forward Structure
存量OI:      C 42.2k / P 35.8k
今日变化ΔOI: C +11.9k / P +10.1k
平值价格ATM:  C 10.39 / P 22.27
隐含波动率 ATM IV:  109.1%
净 delta 敞口变化 ΔOI Δ Exposure*: 92k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 280 ｜ +2,405 ｜ $6.29 ｜ 名义 $1.51M* ｜ +5.2%
C 260 ｜ +2,079 ｜ $12.05 ｜ 名义 $2.51M* ｜ -2.3%
C 275 ｜ +1,962 ｜ $7.50 ｜ 名义 $1.47M* ｜ +3.3%
结构参考：280（+5.2%） / 260（-2.3%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 225（结算参考） ｜ Call Wall 275（+3.3%，弱）（OI 4.4k）
量化解读： 存量 Call 重｜ATM IV 109.1%｜历史 Rank 67%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 91,667 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（MEDIUM △）Top ΔOI: 270C +799 ｜ 250C -682
09-18（MEDIUM △）仓位参考: Max Pain 220（结算参考） ｜ Call Wall 250（-6.1%）（OI 21.7k）

📆 09-25 Forward Structure
存量OI:      C 8.8k / P 9.4k
今日变化ΔOI: C +0.8k / P +0.2k
平值价格ATM:  C 17.36 / P 29.02
隐含波动率 ATM IV:  91.1%
净 delta 敞口变化 ΔOI Δ Exposure*: 23k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 270 ｜ +443 ｜ $15.46 ｜ 名义 $684.9k* ｜ +1.4%
P 210 ｜ +348 ｜ $4.73 ｜ 名义 $164.6k* ｜ -21.1%
C 275 ｜ +124 ｜ $13.80 ｜ 名义 $171.1k* ｜ +3.3%
结构参考：270（+1.4%） / 210（-21.1%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 215（结算参考） ｜ Call Wall 250（-6.1%，弱）（OI 0.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 91.1%｜历史 Rank 67%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 23,463 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 10-02 Forward Structure
存量OI:      C 6.2k / P 7.7k
今日变化ΔOI: C +0.8k / P +1.3k
平值价格ATM:  C 19.80 / P 38.00
隐含波动率 ATM IV:  89.3%
净 delta 敞口变化 ΔOI Δ Exposure*: 14k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 205 ｜ +607 ｜ $5.45 ｜ 名义 $330.8k* ｜ -23.0%
C 300 ｜ +434 ｜ $11.03 ｜ 名义 $478.7k* ｜ +12.7%
P 185 ｜ +257 ｜ $2.13 ｜ 名义 $54.7k* ｜ -30.5%
结构参考：300（+12.7%） / 205（-23.0%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 220（结算参考）
量化解读： 存量 Put 重｜ATM IV 89.3%｜历史 Rank 67%（近端代理）｜净 delta 敞口 正 14,492 股（方向不可观测）——方向不可观测，观察点，非方向信号

📅 事件差分（观察，非因果）: 09-11（4D）ATM IV 109.1% vs 09-18 97.8%（差 +11.3pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate YoY、Inflation Rate MoM、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-07/BE_morning.json