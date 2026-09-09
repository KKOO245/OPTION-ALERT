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
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **单日价格波动**: -4.2%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 17.46 → 收盘 17.06（-2.3%） ｜ 今日高 17.62 ｜ 低 17.01 ｜ 昨收 17.66 → 收盘 17.06（-3.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.53 | OI比 0.48 | ATM IV 88.5% | Skew -5.4pp | Term 0.94 | ExpMove ±5.2%（近端） | Rank 8%
量化视角： IV 历史低位（Rank 8%，期权偏便宜）｜期限结构正常（Term 0.94）｜Put 保护异常便宜（Skew -5.4pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.48）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.53×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.48×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（2D）±5.2% ｜ 09-18（9D）±10.3% ｜ 09-25（16D）±13.5% ｜ 10-02（23D）±16.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 852,920 | GEX Change vs 上次快照 -475,856 | Flip: Primary Flip: 16.95（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 238 / LOW 97 / INVALID 141
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 16.95（全链重定价，覆盖 99%）
最近结构参考: Flip 17（现价高于该位 0.7%）
量化视角： 正 Gamma（85万，无历史分位）｜正 Gamma 减弱（48万）｜现价位于 Flip 上方 0.66%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 18（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 17（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 17.0P — Vol 1,352 | 最新价 $0.40 | OI 1565→4020 (ΔOI +2455张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2455张（+156.9% vs前日OI），连续性待观察（方向未知）
09-11 16.5P — Vol 503 | 最新价 $0.19 | OI 796→2227 (ΔOI +1431张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1431张（+179.8% vs前日OI），连续性待观察（方向未知）
09-11 20.0C — Vol 106 | 最新价 $0.01 | OI 791→1789 (ΔOI +998张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增998张（+126.2% vs前日OI），连续性待观察（方向未知）
09-11 18.5C — Vol 395 | 最新价 $0.11 | OI 503→1471 (ΔOI +968张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增968张（+192.4% vs前日OI），连续性待观察（方向未知）
09-11 19.5C — Vol 348 | 最新价 $0.03 | OI 2861→3510 (ΔOI +649张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增649张（+22.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 6,501 张（Put 3,886 / Call 2,615），跨 1 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-18  C +0 / P +0 ｜ Activity LOW ｜ 9D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 16D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 23D

📆 09-11 Forward Structure
存量OI:      C 23.2k / P 11.2k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 0.48 / P 0.40
隐含波动率 ATM IV:  88.4%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 18（结算参考） ｜ Put Wall 17（-0.4%）（OI 4.0k）
量化解读： 存量 Call 重｜ATM IV 88.4%｜历史 Rank 8%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（Activity LOW）仓位参考: Max Pain 20（结算参考）

09-25（Activity LOW）仓位参考: Max Pain 18（结算参考）

10-02（Activity LOW）仓位参考: Max Pain 18（结算参考）

📅 事件差分（观察，非因果）: 09-11（2D）ATM IV 88.4% vs 09-18 78.9%（差 +9.5pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-09/USAR_evening.json