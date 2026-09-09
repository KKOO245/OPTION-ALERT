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
🟡 **事件差分**: 09-11 ATM IV 48.7% vs 09-14 38.3%（差 +10.4pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 368.36 → 收盘 367.81（-0.1%） ｜ 今日高 375.44 ｜ 低 367.25 ｜ 昨收 368.16 → 收盘 367.81（-0.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.60 | OI比 0.52 | ATM IV 17.7% | Skew -3.4pp | Term 2.36 | ExpMove ±2.9%（近端） | Rank 0%
量化视角： IV 历史低位（Rank 0%，期权偏便宜）｜期限结构正常偏陡（Term 2.36）｜Put 保护异常便宜（Skew -3.4pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.52）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.60×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.52×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（2D）±2.9% ｜ 09-14（5D）±3.6% ｜ 09-16（7D）±4.6% ｜ 09-18（9D）±5.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 106,946,664 | GEX Change vs 上次快照 -38,173,335 | Flip: Primary Flip: 358.12（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 88%（带内） ｜ IV 有效性: VALID 1089 / LOW 218 / INVALID 595
结构观察区: Primary Flip 358.12（全链重定价，覆盖 88%）
Put Wall 350（弱结构｜现价高于该位 5.1%） | Call Wall 400（现价低于该位 8.0%）
最近结构参考: Flip 358（现价高于该位 2.7%）
量化视角： 正 Gamma（1.07亿，无历史分位）｜正 Gamma 减弱（3817万）｜现价位于 Flip 上方 2.71%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 350（Put Wall，弱结构） / 362（MaxPain，仅结算参考）；上方 400（Call Wall）。
• Gamma 区域：切换参考 358（全链重定价，覆盖 88%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-09 360.0P — Vol 64,312 | 最新价 $0.01 | OI 4678→16699 (ΔOI +12021张) | ΔOI/Volume 18.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12021张（+257.0% vs前日OI），连续性待观察（方向未知）
09-09 365.0P — Vol 151,880 | 最新价 $0.01 | OI 1141→10444 (ΔOI +9303张) | ΔOI/Volume 6.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9303张（+815.3% vs前日OI），连续性待观察（方向未知）
09-09 380.0C — Vol 196,876 | 最新价 $0.02 | OI 4012→12328 (ΔOI +8316张) | ΔOI/Volume 4.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8316张（+207.3% vs前日OI），连续性待观察（方向未知）
09-09 367.5C — Vol 61,496 | 最新价 $0.44 | OI 2084→9291 (ΔOI +7207张) | ΔOI/Volume 11.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7207张（+345.8% vs前日OI），连续性待观察（方向未知）
09-09 355.0P — Vol 10,831 | 最新价 $0.01 | OI 1461→8305 (ΔOI +6844张) | ΔOI/Volume 63.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6844张（+468.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 43,691 张（Put 28,168 / Call 15,523），跨 1 个期限｜彩票/名义 3 档（价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-14  C +0 / P +0 ｜ Activity LOW ｜ 5D
09-16  C +0 / P +0 ｜ Activity LOW ｜ 7D
09-18  C +0 / P +0 ｜ Activity LOW ｜ 9D

📆 09-11 Forward Structure
存量OI:      C 210.9k / P 189.2k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 5.55 / P 5.10
隐含波动率 ATM IV:  48.7%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 358（结算参考） ｜ Call Wall 370（+0.6%，弱）（OI 15.1k）
量化解读： 存量两侧均衡｜ATM IV 48.7%｜历史 Rank 0%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-14（Activity LOW）仓位参考: Max Pain 360（结算参考） ｜ Call Wall 400（+8.8%，弱）（OI 1.9k）

09-16（Activity LOW）仓位参考: Max Pain 360（结算参考） ｜ Call Wall 400（+8.8%，弱）（OI 0.8k） ｜ Put Wall 355（-3.5%，弱）（OI 1.0k）

09-18（Activity LOW）仓位参考: Max Pain 370（结算参考）

📅 事件差分（观察，非因果）: 09-11（2D）ATM IV 48.7% vs 09-14 38.3%（差 +10.4pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-09/TSLA_evening.json