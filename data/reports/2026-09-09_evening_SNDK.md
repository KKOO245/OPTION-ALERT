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


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 1,749.72 → 收盘 1,764.17（+0.8%） ｜ 今日高 1807.00 ｜ 低 1728.02 ｜ 昨收 1,737.99 → 收盘 1,764.17（+1.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.62 | OI比 0.98 | ATM IV 79.1% | Skew -4.3pp | Term 0.96 | ExpMove ±4.7%（近端） | Rank 32%
量化视角： IV 中性（Rank 32%）｜期限结构正常（Term 0.96）｜Put 保护异常便宜（Skew -4.3pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.62×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.98×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-11（2D）±4.7% ｜ 09-18（9D）±9.1% ｜ 09-25（16D）±12.3% ｜ 10-02（23D）±16.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 7,456,902 | GEX Change vs 上次快照 -1,809,125 | Flip: Primary Flip: 1677.02（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1956 / LOW 416 / INVALID 1028
结构观察区: Primary Flip 1677.02（全链重定价，覆盖 99%）
最近结构参考: Flip 1677（现价高于该位 5.2%）
量化视角： 正 Gamma（746万，无历史分位）｜正 Gamma 减弱（181万）｜现价位于 Flip 上方 5.20%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 1,670（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1677（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 2000.0C — Vol 12,289 | 最新价 $2.00 | OI 2121→4613 (ΔOI +2492张) | ΔOI/Volume 20.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2492张（+117.5% vs前日OI），连续性待观察（方向未知）
09-11 1600.0P — Vol 2,799 | 最新价 $2.40 | OI 1095→2027 (ΔOI +932张) | ΔOI/Volume 33.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增932张（+85.1% vs前日OI），连续性待观察（方向未知）
09-11 1950.0P — Vol 5 | 最新价 $199.12 | OI 2→718 (ΔOI +716张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增716张（+35800.0% vs前日OI），连续性待观察（方向未知）
09-11 1750.0P — Vol 4,865 | 最新价 $34.15 | OI 215→838 (ΔOI +623张) | ΔOI/Volume 12.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增623张（+289.8% vs前日OI），连续性待观察（方向未知）
09-18 1510.0P — Vol 59 | 最新价 $8.10 | OI 87→694 (ΔOI +607张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增607张（+697.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,370 张（Put 2,878 / Call 2,492），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $17M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-18  C +0 / P +0 ｜ Activity LOW ｜ 9D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 16D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 23D

📆 09-11 Forward Structure
存量OI:      C 39.4k / P 38.5k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 41.40 / P 41.60
隐含波动率 ATM IV:  79.1%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 1,670（结算参考） ｜ Put Wall 1600（-9.3%，弱）（OI 2.0k）
量化解读： 存量两侧均衡｜ATM IV 79.1%｜历史 Rank 32%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（Activity LOW）仓位参考: Max Pain 1,450（结算参考）

09-25（Activity LOW）仓位参考: Max Pain 1,590（结算参考） ｜ Call Wall 1800（+2.0%，弱）（OI 0.4k）

10-02（Activity LOW）仓位参考: Max Pain 1,560（结算参考） ｜ Call Wall 1800（+2.0%，弱）（OI 0.3k）

📅 事件差分（观察，非因果）: 09-11（2D）ATM IV 79.1% vs 09-18 72.8%（差 +6.3pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-09/SNDK_evening.json