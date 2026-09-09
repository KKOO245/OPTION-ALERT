# 期权晨报 2026-09-09（快照 11:03 ET）

📊 市场环境

SPY $762.70 ｜ QQQ $716.31
VIX 16.06 ↑2.2%（5D +5.7%） ｜ Vol Regime: NORMAL
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


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 178.94 → 今开 184.29（+3.0%） | 较昨收变动（含盘初走势） ｜ 今日高 184.80 ｜ 低 178.12

Options: P/C成交量 0.26 | OI比 0.51 | ATM IV 81.8% | Skew -9.9pp | Term 0.85 | ExpMove ±5.1%（近端） | Rank 63%
量化视角： IV 中性（Rank 63%）｜期限结构倒挂（Term 0.85，近月 IV 高于远月）｜Put 保护异常便宜（Skew -9.9pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.51）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.26×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.51×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（2D）±5.1% ｜ 09-18（9D）±9.4% ｜ 09-25（16D）±12.0% ｜ 10-02（23D）±13.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 20,959,220 | GEX Change vs 上次快照 1,641,832 | Flip: Primary Flip: 164.48（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 558 / LOW 156 / INVALID 258
结构观察区: Primary Flip 164.48（全链重定价，覆盖 100%）
Call Wall 170（弱结构｜现价高于该位 5.6%）
最近结构参考: Call Wall 170（现价高于该位 5.6%）
量化视角： 正 Gamma（2096万，无历史分位）｜正 Gamma 增强（+164万）｜现价位于 Flip 上方 9.13%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 170（Call Wall，弱结构）；上方 180（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 164（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 190.0C — Vol 5,301 | 最新价 $1.66 | OI 3418→5271 (ΔOI +1853张) | ΔOI/Volume 35.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1853张（+54.2% vs前日OI），连续性待观察（方向未知）
09-18 160.0P — Vol 1,433 | 最新价 $1.62 | OI 7207→7930 (ΔOI +723张) | ΔOI/Volume 50.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增723张（+10.0% vs前日OI），连续性待观察（方向未知）
09-11 200.0C — Vol 1,541 | 最新价 $0.56 | OI 3441→3945 (ΔOI +504张) | ΔOI/Volume 32.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增504张（+14.7% vs前日OI），连续性待观察（方向未知）
09-11 195.0C — Vol 2,249 | 最新价 $0.95 | OI 5923→6341 (ΔOI +418张) | ΔOI/Volume 18.6% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增418张（+7.1% vs前日OI），值得跟踪（方向未知）
09-11 157.5P — Vol 512 | 最新价 $0.17 | OI 430→847 (ΔOI +417张) | ΔOI/Volume 81.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增417张（+97.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,915 张（Put 1,140 / Call 2,775），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +5.9k / P +3.3k ｜ Activity HIGH ｜ 2D
09-18  C +0.7k / P +1.5k ｜ Activity MEDIUM △ ｜ 9D
09-25  C +0.7k / P +0.4k ｜ Activity MEDIUM △ ｜ 16D
10-02  C +0.2k / P +0.6k ｜ Activity MEDIUM △ ｜ 23D

📆 09-11 Forward Structure
存量OI:      C 61.2k / P 31.0k
今日变化ΔOI: C +5.9k / P +3.3k
平值价格ATM:  C 4.50 / P 4.69
隐含波动率 ATM IV:  81.8%
净 delta 敞口变化 ΔOI Δ Exposure*: 59k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 190 ｜ +1,853 ｜ $1.56 ｜ 名义 $289.1k* ｜ +5.8%
C 195 ｜ +418 ｜ $1.01 ｜ 名义 $42.2k* ｜ +8.6%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：190（+5.8%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 180（结算参考） ｜ Call Wall 187.5（+4.5%，弱）（OI 6.7k）
量化解读： 存量 Call 重｜ATM IV 81.8%｜历史 Rank 63%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 59,412 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（MEDIUM △）Top ΔOI: 160P +723 ｜ 170P +384
09-18（MEDIUM △）仓位参考: Max Pain 170（结算参考） ｜ Call Wall 170（-5.3%）（OI 16.1k）

09-25（MEDIUM △）Top ΔOI: 200C +128
09-25（MEDIUM △）仓位参考: Max Pain 170（结算参考） ｜ Call Wall 185（+3.1%，弱）（OI 1.0k）

10-02（MEDIUM △）Top ΔOI: 170P +318 ｜ 162P +62
10-02（MEDIUM △）仓位参考: Max Pain 188（结算参考） ｜ Put Wall 172.5（-3.9%，弱）（OI 1.1k）

📅 事件差分（观察，非因果）: 09-11（2D）ATM IV 81.8% vs 09-18 73.1%（差 +8.7pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-09/COIN_morning.json