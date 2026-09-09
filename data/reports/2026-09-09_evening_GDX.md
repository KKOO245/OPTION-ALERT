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


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 100.46 → 收盘 99.47（-1.0%） ｜ 今日高 101.48 ｜ 低 98.69 ｜ 昨收 98.41 → 收盘 99.47（+1.1%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-09-16，窗口结束前不做对错判定）

Options: P/C成交量 1.32 | OI比 0.55 | ATM IV 51.5% | Skew 1.0pp | Term 0.87 | ExpMove ±3.1%（近端） | Rank 84%
量化视角： IV 历史高位（Rank 84%，期权偏贵）｜期限结构倒挂（Term 0.87，近月 IV 高于远月）｜保护溢价薄（Skew 1.0pp）｜⚠️ 重点观察：存量 Call 重（OI比 0.55）+ 当日成交偏 Put（P/C量 1.32）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.32×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.55×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（2D）±3.1% ｜ 09-18（9D）±6.4% ｜ 09-25（16D）±7.5% ｜ 10-02（23D）±9.5%
   ⇒ IV–VIX Spread: +35.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 51,599,896 | GEX Change vs 上次快照 -2,658,815 | Flip: Primary Flip: 96.98（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 631 / LOW 147 / INVALID 172
结构观察区: Primary Flip 96.98（全链重定价，覆盖 97%）
Call Wall 100（弱结构｜现价低于该位 0.5%）
最近结构参考: Call Wall 100（现价低于该位 0.5%）
量化视角： 正 Gamma（5160万，无历史分位）｜正 Gamma 减弱（266万）｜现价位于 Flip 上方 2.57%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 98（MaxPain，仅结算参考）；上方 100（Call Wall，弱结构）。
• Gamma 区域：切换参考 97（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 90.0P — Vol 798 | 最新价 $0.31 | OI 42261→44239 (ΔOI +1978张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增1978张（+4.7% vs前日OI），值得跟踪（方向未知）
09-11 90.0P — Vol 379 | 最新价 $0.04 | OI 9781→11336 (ΔOI +1555张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增1555张（+15.9% vs前日OI），值得跟踪（方向未知）
09-11 100.0C — Vol 870 | 最新价 $1.26 | OI 5483→6671 (ΔOI +1188张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1188张（+21.7% vs前日OI），连续性待观察（方向未知）
09-18 112.0C — Vol 123 | 最新价 $0.32 | OI 365→1314 (ΔOI +949张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增949张（+260.0% vs前日OI），连续性待观察（方向未知）
09-11 105.0C — Vol 2,278 | 最新价 $0.19 | OI 4910→5717 (ΔOI +807张) | ΔOI/Volume 35.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增807张（+16.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 6,477 张（Put 3,533 / Call 2,944），跨 2 个期限｜彩票/名义 1 档（价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-18  C +0 / P +0 ｜ Activity LOW ｜ 9D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 16D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 23D

📆 09-11 Forward Structure
存量OI:      C 105.4k / P 57.5k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 1.72 / P 1.37
隐含波动率 ATM IV:  51.5%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 98（结算参考） ｜ Call Wall 104（+4.6%，弱）（OI 17.0k） ｜ Put Wall 90（-9.5%）（OI 11.3k）
量化解读： 存量 Call 重｜ATM IV 51.5%｜历史 Rank 84%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（Activity LOW）仓位参考: Max Pain 90（结算参考） ｜ Call Wall 100（+0.5%，弱）（OI 23.8k）

09-25（Activity LOW）仓位参考: Max Pain 96（结算参考） ｜ Call Wall 105（+5.6%）（OI 1.0k）

10-02（Activity LOW）仓位参考: Max Pain 99（结算参考） ｜ Put Wall 97（-2.5%）（OI 15.1k）

📅 事件差分（观察，非因果）: 09-11（2D）ATM IV 51.5% vs 09-18 46.5%（差 +5.0pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-09/GDX_evening.json