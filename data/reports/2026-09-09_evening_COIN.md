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
🟡 **单日价格波动**: -2.4%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 184.29 → 收盘 174.72（-5.2%） ｜ 今日高 184.80 ｜ 低 174.61 ｜ 昨收 178.94 → 收盘 174.72（-2.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.29 | OI比 0.51 | ATM IV 73.9% | Skew -7.3pp | Term 0.89 | ExpMove ±4.3%（近端） | Rank 42%
量化视角： IV 中性（Rank 42%）｜期限结构倒挂（Term 0.89，近月 IV 高于远月）｜Put 保护异常便宜（Skew -7.3pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.51）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.29×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.51×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（2D）±4.3% ｜ 09-18（9D）±8.5% ｜ 09-25（16D）±11.2% ｜ 10-02（23D）±12.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 14,882,571 | GEX Change vs 上次快照 -6,076,648 | Flip: Primary Flip: 164.60（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 535 / LOW 163 / INVALID 274
结构观察区: Primary Flip 164.60（全链重定价，覆盖 100%）
Call Wall 170（弱结构｜现价高于该位 2.8%）
最近结构参考: Call Wall 170（现价高于该位 2.8%）
量化视角： 正 Gamma（1488万，无历史分位）｜正 Gamma 减弱（608万）｜现价位于 Flip 上方 6.15%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 170（Call Wall，弱结构）；上方 180（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 165（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 190.0C — Vol 5,811 | 最新价 $0.52 | OI 3418→5271 (ΔOI +1853张) | ΔOI/Volume 31.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1853张（+54.2% vs前日OI），连续性待观察（方向未知）
09-18 160.0P — Vol 2,636 | 最新价 $1.82 | OI 7207→7930 (ΔOI +723张) | ΔOI/Volume 27.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增723张（+10.0% vs前日OI），连续性待观察（方向未知）
09-11 200.0C — Vol 4,035 | 最新价 $0.14 | OI 3441→3945 (ΔOI +504张) | ΔOI/Volume 12.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增504张（+14.7% vs前日OI），连续性待观察（方向未知）
09-11 195.0C — Vol 2,074 | 最新价 $0.25 | OI 5923→6341 (ΔOI +418张) | ΔOI/Volume 20.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增418张（+7.1% vs前日OI），连续性待观察（方向未知）
09-11 157.5P — Vol 123 | 最新价 $0.15 | OI 430→847 (ΔOI +417张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增417张（+97.0% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,915 张（Put 1,140 / Call 2,775），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-18  C +0 / P +0 ｜ Activity LOW ｜ 9D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 16D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 23D

📆 09-11 Forward Structure
存量OI:      C 61.2k / P 31.0k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 3.79 / P 3.80
隐含波动率 ATM IV:  73.9%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 180（结算参考） ｜ Call Wall 187.5（+7.3%，弱）（OI 6.7k）
量化解读： 存量 Call 重｜ATM IV 73.9%｜历史 Rank 42%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（Activity LOW）仓位参考: Max Pain 170（结算参考） ｜ Call Wall 170（-2.7%）（OI 16.1k）

09-25（Activity LOW）仓位参考: Max Pain 170（结算参考） ｜ Call Wall 185（+5.9%，弱）（OI 1.0k）

10-02（Activity LOW）仓位参考: Max Pain 188（结算参考） ｜ Put Wall 172.5（-1.3%，弱）（OI 1.1k）

📅 事件差分（观察，非因果）: 09-11（2D）ATM IV 73.9% vs 09-18 67.3%（差 +6.6pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-09/COIN_evening.json