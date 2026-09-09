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


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 716.29 → 收盘 716.31（+0.0%） ｜ 今日高 719.70 ｜ 低 714.02 ｜ 昨收 718.36 → 收盘 716.31（-0.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.11 | OI比 2.12 | ATM IV 8.3% | Skew -1.8pp | Term 2.32 | ExpMove ±0.8%（近端） | Rank 3%
量化视角： IV 历史低位（Rank 3%，期权偏便宜）｜期限结构正常偏陡（Term 2.32）｜Put 保护异常便宜（Skew -1.8pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.11×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 2.12×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 34% ｜ P/C OI(近端) 82%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 34%）｜近端持仓结构中性（P/C OI 分位 82%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-10（1D）±0.8% ｜ 09-11（2D）±1.3% ｜ 09-14（5D）±1.6% ｜ 09-15（6D）±1.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -246,536,150 | GEX Change vs 上次快照 -79,382,369 | Flip: Primary Flip: 720.29（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 2438 / LOW 572 / INVALID 1436
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 720.29（全链重定价，覆盖 94%）
Put Wall 700（弱结构｜现价高于该位 2.3%） | Call Wall 750（弱结构｜现价低于该位 4.5%）
最近结构参考: Flip 720（现价低于该位 0.6%）
量化视角： 负 Gamma（2.47亿，历史分位 34%，中性区）｜负 Gamma 加深（7938万）｜现价位于 Flip 下方 0.55%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 700（Put Wall，弱结构）；上方 719（MaxPain，仅结算参考） / 750（Call Wall，弱结构）。
• Gamma 区域：切换参考 720（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 631.0P — Vol 30 | 最新价 $0.01 | OI 104→20323 (ΔOI +20219张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20219张（+19441.3% vs前日OI），连续性待观察（方向未知）
09-11 734.0C — Vol 1,356 | 最新价 $0.10 | OI 1117→9373 (ΔOI +8256张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8256张（+739.1% vs前日OI），连续性待观察（方向未知）
09-14 655.0P — Vol 3,877 | 最新价 $0.09 | OI 406→7872 (ΔOI +7466张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7466张（+1838.9% vs前日OI），连续性待观察（方向未知）
09-09 710.0P — Vol 67,829 | 最新价 $0.01 | OI 1404→7978 (ΔOI +6574张) | ΔOI/Volume 9.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6574张（+468.2% vs前日OI），连续性待观察（方向未知）
09-09 723.0C — Vol 34,657 | 最新价 $0.01 | OI 625→5751 (ΔOI +5126张) | ΔOI/Volume 14.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5126张（+820.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 47,641 张（Put 34,259 / Call 13,382），跨 3 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-10  C +0 / P +0 ｜ Activity LOW ｜ 1D
09-11  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-14  C +0 / P +0 ｜ Activity LOW ｜ 5D
09-15  C +0 / P +0 ｜ Activity LOW ｜ 6D

📆 09-10 Forward Structure
存量OI:      C 41.0k / P 70.9k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 2.93 / P 2.65
隐含波动率 ATM IV:  18.6%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 718（结算参考） ｜ Call Wall 725（+1.2%，弱）（OI 4.1k） ｜ Put Wall 656（-8.4%，弱）（OI 3.6k）
量化解读： 存量 Put 重｜ATM IV 18.6%｜历史 Rank 3%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-11（Activity LOW）仓位参考: Max Pain 716（结算参考） ｜ Call Wall 750（+4.7%，弱）（OI 12.1k） ｜ Put Wall 705（-1.6%，弱）（OI 24.8k）

09-14（Activity LOW）仓位参考: Max Pain 715（结算参考） ｜ Call Wall 725（+1.2%）（OI 3.1k） ｜ Put Wall 655（-8.6%）（OI 7.9k）

09-15（Activity LOW）仓位参考: Max Pain 715（结算参考） ｜ Call Wall 730（+1.9%，弱）（OI 1.9k） ｜ Put Wall 705（-1.6%）（OI 6.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-09/QQQ_evening.json