# 期权晚报 2026-09-10（快照 17:04 ET）

📊 市场环境

SPY $757.83 ｜ QQQ $708.69
VIX 17.84 ↑8.4%（5D +24.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-10 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 0.4 ｜ 前值 0.1　✅ 今日已公布
- 周四 09-10 10:00　【高】成屋销售　预测 3.98 ｜ 实际 3.98 ｜ 前值 4.06　✅ 今日已公布
- 周五 09-11 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.2
- 周五 09-11 08:30　【高】Inflation Rate MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.1
- 周五 09-11 08:30　【高】Inflation Rate YoY　预测 3.4 ｜ 实际 待公布 ｜ 前值 3.4
- 周五 09-11 08:30　【高】Core Inflation Rate YoY　预测 2.4 ｜ 实际 待公布 ｜ 前值 2.5
- 周五 09-11 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 51 ｜ 实际 待公布 ｜ 前值 51.7

🔍 重点速览
🟡 **单日价格波动**: -6.1%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **事件差分**: 09-11 ATM IV 90.8% vs 09-18 77.4%（差 +13.4pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 09-11 16P ΔOI +285（距现价 +2.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 16.95 → 收盘 16.04（-5.4%） ｜ 今日高 16.97 ｜ 低 16.00 ｜ 昨收 17.06 → 收盘 16.04（-6.0%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-09-15，窗口结束前不做对错判定）

Options: P/C成交量 0.99 | OI比 0.54 | ATM IV 90.8% | Skew -24.1pp | Term 0.87 | ExpMove ±3.7%（近端） | Rank 11%
量化视角： IV 历史低位（Rank 11%，期权偏便宜）｜期限结构倒挂（Term 0.87，近月 IV 高于远月）｜Put 保护异常便宜（Skew -24.1pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.54）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.99×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.54×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（1D）±3.7% ｜ 09-18（8D）±8.8% ｜ 09-25（15D）±12.7% ｜ 10-02（22D）±15.8%
   ⇒ IV–VIX Spread: +73.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -3,698,677 | GEX Change vs 上次快照 -33,897 | Flip: Primary Flip: 16.70（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 224 / LOW 94 / INVALID 166
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 16.70（全链重定价，覆盖 96%）
Put Wall 15（弱结构｜现价高于该位 6.9%）
最近结构参考: Flip 17（现价低于该位 3.9%）
量化视角： 负 Gamma（370万，无历史分位）｜负 Gamma 加深（3万）｜现价位于 Flip 下方 3.94%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall，弱结构）；上方 18（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 17（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 16.0P — Vol 45 | 最新价 $1.32 | OI 45→1112 (ΔOI +1067张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1067张（+2371.1% vs前日OI），连续性待观察（方向未知）
09-11 17.0P — Vol 1,331 | 最新价 $1.02 | OI 4020→4787 (ΔOI +767张) | ΔOI/Volume 57.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增767张（+19.1% vs前日OI），连续性待观察（方向未知）
09-18 16.0P — Vol 284 | 最新价 $0.67 | OI 2480→2792 (ΔOI +312张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增312张（+12.6% vs前日OI），值得跟踪（方向未知）
09-11 16.5P — Vol 791 | 最新价 $0.63 | OI 2227→2512 (ΔOI +285张) | ΔOI/Volume 36.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增285张（+12.8% vs前日OI），连续性待观察（方向未知）
09-11 16.0P — Vol 678 | 最新价 $0.28 | OI 757→989 (ΔOI +232张) | ΔOI/Volume 34.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增232张（+30.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,663 张（Put 2,663 / Call 0），跨 3 个期限｜近端保护（4 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C -52 / P +1.3k ｜ Activity HIGH ｜ 1D
09-18  C +0.3k / P +0.2k ｜ Activity LOW ｜ 8D
09-25  C +99 / P +0.2k ｜ Activity HIGH ｜ 15D
10-02  C +48 / P +0.2k ｜ Activity HIGH ｜ 22D

📆 09-11 Forward Structure
存量OI:      C 23.2k / P 12.5k
今日变化ΔOI: C -52 / P +1.3k
平值价格ATM:  C 0.31 / P 0.28
隐含波动率 ATM IV:  90.8%
净 delta 敞口变化 ΔOI Δ Exposure*: -88k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 17 ｜ +767 ｜ $1.02 ｜ 名义 $78.2k* ｜ +6.0%
P 16 ｜ +285 ｜ $0.63 ｜ 名义 $18.0k* ｜ +2.9%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：17（+6.0%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 18（结算参考） ｜ Put Wall 17（+6.0%）（OI 4.8k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 90.8%｜历史 Rank 11%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 88,048 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（Activity LOW）仓位参考: Max Pain 20（结算参考）

📆 09-25 Forward Structure
存量OI:      C 9.3k / P 3.5k
今日变化ΔOI: C +99 / P +0.2k
平值价格ATM:  C 1.08 / P 0.95
隐含波动率 ATM IV:  77.0%
净 delta 敞口变化 ΔOI Δ Exposure*: -7k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 15 ｜ +76 ｜ $0.49 ｜ 名义 $3.7k* ｜ -6.5%
P 15 ｜ +57 ｜ $0.76 ｜ 名义 $4.3k* ｜ -3.4%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：15（-6.5%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 18（结算参考） ｜ Put Wall 15（-6.5%，弱）（OI 0.7k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 77.0%｜历史 Rank 11%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 负 6,883 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 10-02 Forward Structure
存量OI:      C 7.4k / P 2.6k
今日变化ΔOI: C +48 / P +0.2k
平值价格ATM:  C 1.36 / P 1.18
隐含波动率 ATM IV:  81.0%
净 delta 敞口变化 ΔOI Δ Exposure*: -4k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 16 ｜ +63 ｜ $1.18 ｜ 名义 $7.4k* ｜ -0.2%
P 14 ｜ +56 ｜ $0.51 ｜ 名义 $2.9k* ｜ -9.6%
C 17 ｜ +25 ｜ $0.88 ｜ 名义 $2.2k* ｜ +6.0%
结构参考：17（+6.0%） / 16（-0.2%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 18（结算参考）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 81.0%｜历史 Rank 11%（近端代理）｜净 delta 敞口 负 4,464 股（方向不可观测）——方向不可观测，观察点，非方向信号

📅 事件差分（观察，非因果）: 09-11（1D）ATM IV 90.8% vs 09-18 77.4%（差 +13.4pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=14 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=14）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-10/USAR_evening.json