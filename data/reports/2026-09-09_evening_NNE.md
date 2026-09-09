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
🟡 **单日价格波动**: -6.0%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **事件差分**: 09-11 ATM IV 87.5% vs 09-18 75.6%（差 +11.9pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 19.03 → 收盘 18.17（-4.5%） ｜ 今日高 19.33 ｜ 低 18.13 ｜ 昨收 19.35 → 收盘 18.17（-6.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.98 | OI比 0.60 | ATM IV 87.5% | Skew -31.1pp | Term 0.99 | ExpMove ±5.5%（近端） | Rank 14%
量化视角： IV 历史低位（Rank 14%，期权偏便宜）｜期限结构正常（Term 0.99）｜Put 保护异常便宜（Skew -31.1pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.60）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.98×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.60×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（2D）±5.5% ｜ 09-18（9D）±9.6% ｜ 09-25（16D）±13.8% ｜ 10-02（23D）±15.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,388,216 | GEX Change vs 上次快照 -605,988 | Flip: Primary Flip: 16.52（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 200 / LOW 88 / INVALID 152
结构观察区: Primary Flip 16.52（全链重定价，覆盖 91%）
最近结构参考: Flip 17（现价高于该位 10.0%）
量化视角： 正 Gamma（239万，无历史分位）｜正 Gamma 减弱（61万）｜现价位于 Flip 上方 9.97%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 19（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 17（全链重定价，覆盖 91%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 30.0C — Vol 5 | 最新价 $0.15 | OI 9→753 (ΔOI +744张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增744张（+8266.7% vs前日OI），连续性待观察（方向未知）
09-11 20.0C — Vol 135 | 最新价 $0.10 | OI 224→870 (ΔOI +646张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增646张（+288.4% vs前日OI），连续性待观察（方向未知）
09-18 19.0C — Vol 1,463 | 最新价 $0.70 | OI 241→675 (ΔOI +434张) | ΔOI/Volume 29.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增434张（+180.1% vs前日OI），连续性待观察（方向未知）
09-11 21.0C — Vol 2 | 最新价 $0.15 | OI 165→587 (ΔOI +422张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增422张（+255.8% vs前日OI），值得跟踪（方向未知）
09-18 21.0C — Vol 8 | 最新价 $0.26 | OI 252→658 (ΔOI +406张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增406张（+161.1% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,652 张（Put 0 / Call 2,652），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-18  C +0 / P +0 ｜ Activity LOW ｜ 9D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 16D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 23D

📆 09-11 Forward Structure
存量OI:      C 5.4k / P 3.2k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 0.70 / P 0.29
隐含波动率 ATM IV:  87.5%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 19（结算参考）
量化解读： 存量 Call 重｜ATM IV 87.5%｜历史 Rank 14%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（Activity LOW）仓位参考: Max Pain 19（结算参考） ｜ Put Wall 18（-0.9%）（OI 0.7k）

09-25（Activity LOW）仓位参考: Max Pain 18（结算参考）

10-02（Activity LOW）仓位参考: Max Pain 19（结算参考） ｜ Put Wall 18.5（+1.8%）（OI 0.1k）

📅 事件差分（观察，非因果）: 09-11（2D）ATM IV 87.5% vs 09-18 75.6%（差 +11.9pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-09/NNE_evening.json