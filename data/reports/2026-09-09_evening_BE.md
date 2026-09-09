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
🟡 **单日价格波动**: -2.2%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 272.99 → 收盘 269.28（-1.4%） ｜ 今日高 280.48 ｜ 低 268.58 ｜ 昨收 277.22 → 收盘 269.28（-2.9%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.74 | OI比 1.09 | ATM IV 91.7% | Skew -6.7pp | Term 0.88 | ExpMove ±5.4%（近端） | Rank 53%
量化视角： IV 中性（Rank 53%）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜Put 保护异常便宜（Skew -6.7pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.74×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.09×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-11（2D）±5.4% ｜ 09-18（9D）±10.4% ｜ 09-25（16D）±13.3% ｜ 10-02（23D）±16.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 23,541,007 | GEX Change vs 上次快照 -101,336 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 589 / LOW 72 / INVALID 299
结构观察区: NO_CROSS
Call Wall 250（弱结构｜现价高于该位 7.7%）
最近结构参考: Call Wall 250（现价高于该位 7.7%）
量化视角： 正 Gamma（2354万，无历史分位）｜正 Gamma 减弱（10万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 248（MaxPain，仅结算参考） / 250（Call Wall，弱结构）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 280.0C — Vol 1,306 | 最新价 $9.60 | OI 5187→7716 (ΔOI +2529张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2529张（+48.8% vs前日OI），连续性待观察（方向未知）
09-11 260.0P — Vol 1,328 | 最新价 $3.35 | OI 83→1826 (ΔOI +1743张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1743张（+2100.0% vs前日OI），连续性待观察（方向未知）
09-11 325.0C — Vol 620 | 最新价 $0.07 | OI 124→1856 (ΔOI +1732张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1732张（+1396.8% vs前日OI），连续性待观察（方向未知）
09-11 240.0P — Vol 1,032 | 最新价 $0.35 | OI 472→2087 (ΔOI +1615张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1615张（+342.2% vs前日OI），连续性待观察（方向未知）
09-11 190.0P — Vol 125 | 最新价 $0.07 | OI 1062→2621 (ΔOI +1559张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1559张（+146.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 9,178 张（Put 4,917 / Call 4,261），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-18  C +0 / P +0 ｜ Activity LOW ｜ 9D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 16D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 23D

📆 09-11 Forward Structure
存量OI:      C 49.8k / P 54.1k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 6.90 / P 7.70
隐含波动率 ATM IV:  91.7%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 248（结算参考） ｜ Call Wall 275（+2.1%）（OI 4.8k）
量化解读： 存量两侧均衡｜ATM IV 91.7%｜历史 Rank 53%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（Activity LOW）仓位参考: Max Pain 230（结算参考） ｜ Call Wall 250（-7.2%）（OI 20.8k）

09-25（Activity LOW）仓位参考: Max Pain 230（结算参考） ｜ Call Wall 250（-7.2%，弱）（OI 0.8k）

10-02（Activity LOW）仓位参考: Max Pain 240（结算参考）

📅 事件差分（观察，非因果）: 09-11（2D）ATM IV 91.7% vs 09-18 82.7%（差 +9.0pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-09/BE_evening.json