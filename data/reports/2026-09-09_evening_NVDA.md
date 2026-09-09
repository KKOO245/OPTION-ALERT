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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 225.27 → 收盘 223.67（-0.7%） ｜ 今日高 226.18 ｜ 低 223.46 ｜ 昨收 225.73 → 收盘 223.67（-0.9%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.58 | OI比 0.76 | ATM IV 40.1% | Skew -3.4pp | Term 0.85 | ExpMove ±2.2%（近端） | Rank 38%
量化视角： IV 中性（Rank 38%）｜期限结构倒挂（Term 0.85，近月 IV 高于远月）｜Put 保护异常便宜（Skew -3.4pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.76）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.58×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.76×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（2D）±2.2% ｜ 09-14（5D）±2.9% ｜ 09-16（7D）±3.7% ｜ 09-18（9D）±4.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 373,283,245 | GEX Change vs 上次快照 -81,672,047 | Flip: Primary Flip: 212.37（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 673 / LOW 176 / INVALID 603
结构观察区: Primary Flip 212.37（全链重定价，覆盖 94%）
最近结构参考: Flip 212（现价高于该位 5.3%）
量化视角： 正 Gamma（3.73亿，无历史分位）｜正 Gamma 减弱（8167万）｜现价位于 Flip 上方 5.32%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 225（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 212（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 235.0C — Vol 37,203 | 最新价 $0.16 | OI 32767→57012 (ΔOI +24245张) | ΔOI/Volume 65.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增24245张（+74.0% vs前日OI），连续性待观察（方向未知）
09-11 227.5C — Vol 45,801 | 最新价 $1.00 | OI 24169→47467 (ΔOI +23298张) | ΔOI/Volume 50.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增23298张（+96.4% vs前日OI），连续性待观察（方向未知）
09-09 230.0C — Vol 97,637 | 最新价 $0.01 | OI 16990→39880 (ΔOI +22890张) | ΔOI/Volume 23.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增22890张（+134.7% vs前日OI），连续性待观察（方向未知）
09-09 235.0C — Vol 29,832 | 最新价 $0.01 | OI 19009→37014 (ΔOI +18005张) | ΔOI/Volume 60.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18005张（+94.7% vs前日OI），连续性待观察（方向未知）
09-11 315.0C — Vol 15,083（Yahoo补） | 最新价 $0.01 | OI 111→15142 (ΔOI +15031张) | ΔOI/Volume 99.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15031张（+13541.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 103,469 张（Put 0 / Call 103,469），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-14  C +0 / P +0 ｜ Activity LOW ｜ 5D
09-16  C +0 / P +0 ｜ Activity LOW ｜ 7D
09-18  C +0 / P +0 ｜ Activity LOW ｜ 9D

📆 09-11 Forward Structure
存量OI:      C 519.8k / P 307.0k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 3.05 / P 1.99
隐含波动率 ATM IV:  37.7%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 225（结算参考） ｜ Call Wall 235（+5.1%，弱）（OI 57.0k） ｜ Put Wall 220（-1.6%）（OI 31.2k）
量化解读： 存量 Call 重｜ATM IV 37.7%｜历史 Rank 38%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-14（Activity LOW）仓位参考: Max Pain 225（结算参考） ｜ Call Wall 235（+5.1%，弱）（OI 13.1k）

09-16（Activity LOW）仓位参考: Max Pain 225（结算参考） ｜ Call Wall 235（+5.1%）（OI 8.9k） ｜ Put Wall 205（-8.3%）（OI 2.2k）

09-18（Activity LOW）仓位参考: Max Pain 195（结算参考）

📅 事件差分（观察，非因果）: 09-11（2D）ATM IV 37.7% vs 09-14 30.1%（差 +7.6pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-09/NVDA_evening.json