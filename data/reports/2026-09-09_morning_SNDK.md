# 期权晨报 2026-09-09（快照 11:03 ET）

📊 市场环境

SPY $763.57 ｜ QQQ $717.17
VIX 16.06 ↑2.2%（5D +5.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 40.9（fear）
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
🟡 **单日价格波动**: +3.1%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 1,737.99 → 今开 1,749.72（+0.7%） | 较昨收变动（含盘初走势） ｜ 今日高 1807.00 ｜ 低 1728.02

Options: P/C成交量 0.56 | OI比 0.98 | ATM IV 86.9% | Skew -5.8pp | Term 0.91 | ExpMove ±5.4%（近端） | Rank 37%
量化视角： IV 中性（Rank 37%）｜期限结构正常（Term 0.91）｜Put 保护异常便宜（Skew -5.8pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.56×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.98×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-11（2D）±5.4% ｜ 09-18（9D）±9.9% ｜ 09-25（16D）±13.1% ｜ 10-02（23D）±16.5%
   ⇒ IV–VIX Spread: +70.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 9,266,027 | GEX Change vs 上次快照 2,169,705 | Flip: Primary Flip: 1665.41（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 2229 / LOW 422 / INVALID 749
结构观察区: Primary Flip 1665.41（全链重定价，覆盖 100%）
最近结构参考: Flip 1665（现价高于该位 7.6%）
量化视角： 正 Gamma（927万，无历史分位）｜正 Gamma 增强（+217万）｜现价位于 Flip 上方 7.60%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 1,670（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1665（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 2000.0C — Vol 10,608 | 最新价 $4.00 | OI 2121→4613 (ΔOI +2492张) | ΔOI/Volume 23.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2492张（+117.5% vs前日OI），连续性待观察（方向未知）
09-11 1600.0P — Vol 3,260 | 最新价 $8.97 | OI 1095→2027 (ΔOI +932张) | ΔOI/Volume 28.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增932张（+85.1% vs前日OI），连续性待观察（方向未知）
09-11 1950.0P — Vol 726 | 最新价 $214.60 | OI 2→718 (ΔOI +716张) | ΔOI/Volume 98.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增716张（+35800.0% vs前日OI），连续性待观察（方向未知）
09-11 1750.0P — Vol 3,302 | 最新价 $59.50 | OI 215→838 (ΔOI +623张) | ΔOI/Volume 18.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增623张（+289.8% vs前日OI），连续性待观察（方向未知）
09-18 1510.0P — Vol 696 | 最新价 $14.20 | OI 87→694 (ΔOI +607张) | ΔOI/Volume 87.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增607张（+697.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,370 张（Put 2,878 / Call 2,492），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $21M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +10.7k / P +10.1k ｜ Activity HIGH ｜ 2D
09-18  C +1.9k / P +3.4k ｜ Activity HIGH ｜ 9D
09-25  C +0.9k / P +1.1k ｜ Activity HIGH ｜ 16D
10-02  C +0.3k / P +0.4k ｜ Activity MEDIUM △ ｜ 23D

📆 09-11 Forward Structure
存量OI:      C 39.4k / P 38.5k
今日变化ΔOI: C +10.7k / P +10.1k
平值价格ATM:  C 49.85 / P 47.06
隐含波动率 ATM IV:  86.9%
净 delta 敞口变化 ΔOI Δ Exposure*: -57k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 2000 ｜ +2,492 ｜ $5.00 ｜ 名义 $1.25M* ｜ +11.6%
P 1600 ｜ +932 ｜ $2.77 ｜ 名义 $258.2k* ｜ -10.7%
P 1950 ｜ +716 ｜ $170.00 ｜ 名义 $12.17M* ｜ +8.8%
结构参考：2000（+11.6%） / 1600（-10.7%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 1,670（结算参考）
量化解读： 存量两侧均衡｜ATM IV 86.9%｜历史 Rank 37%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 57,029 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 65.1k / P 79.2k
今日变化ΔOI: C +1.9k / P +3.4k
平值价格ATM:  C 90.21 / P 86.70
隐含波动率 ATM IV:  78.5%
净 delta 敞口变化 ΔOI Δ Exposure*: -71k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 1510 ｜ +607 ｜ $8.30 ｜ 名义 $503.8k* ｜ -15.7%
C 2000 ｜ +409 ｜ $28.60 ｜ 名义 $1.17M* ｜ +11.6%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：2000（+11.6%） / 1510（-15.7%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 1,450（结算参考）
量化解读： 存量 Put 重｜ATM IV 78.5%｜历史 Rank 37%（近端代理）｜净 delta 敞口 负 70,543 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-25 Forward Structure
存量OI:      C 7.7k / P 14.8k
今日变化ΔOI: C +0.9k / P +1.1k
平值价格ATM:  C 119.50 / P 114.70
隐含波动率 ATM IV:  77.6%
净 delta 敞口变化 ΔOI Δ Exposure*: 9k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 1500 ｜ +240 ｜ $18.00 ｜ 名义 $432.0k* ｜ -16.3%
C 2000 ｜ +140 ｜ $49.55 ｜ 名义 $693.7k* ｜ +11.6%
C 1815 ｜ +121 ｜ $105.30 ｜ 名义 $1.27M* ｜ +1.3%
结构参考：2000（+11.6%） / 1500（-16.3%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 1,590（结算参考） ｜ Call Wall 1800（+0.4%，弱）（OI 0.4k）
量化解读： 存量 Put 重｜ATM IV 77.6%｜历史 Rank 37%（近端代理）｜净 delta 敞口 正 9,220 股（方向不可观测）——方向不可观测，观察点，非方向信号

10-02（MEDIUM △）Top ΔOI: 1900C +104 ｜ 1800C -83
10-02（MEDIUM △）仓位参考: Max Pain 1,560（结算参考） ｜ Call Wall 1800（+0.4%，弱）（OI 0.3k）

📅 事件差分（观察，非因果）: 09-11（2D）ATM IV 86.9% vs 09-18 78.5%（差 +8.4pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-09/SNDK_morning.json