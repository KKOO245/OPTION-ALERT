# 期权晨报 2026-09-10（快照 10:56 ET）

📊 市场环境

SPY $758.27 ｜ QQQ $708.69
VIX 17.34 ↑5.3%（5D +21.1%） ｜ Vol Regime: NORMAL
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
🟡 **单日价格波动**: -2.2%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **事件差分**: 09-11 ATM IV 74.4% vs 09-18 61.9%（差 +12.4pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 09-11 53P ΔOI +277（距现价 -0.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 54.30 → 今开 53.33（-1.8%） | 较昨收变动（含盘初走势） ｜ 今日高 53.73 ｜ 低 52.21

Options: P/C成交量 1.05 | OI比 0.82 | ATM IV 74.4% | Skew -4.0pp | Term 0.95 | ExpMove ±5.2%（近端） | Rank 60%
量化视角： IV 中性（Rank 60%）｜期限结构正常（Term 0.95）｜Put 保护异常便宜（Skew -4.0pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.82）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.05×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.82×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-11（1D）±5.2% ｜ 09-18（8D）±8.5% ｜ 09-25（15D）±12.4% ｜ 10-02（22D）±17.0%
   ⇒ IV–VIX Spread: +57.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -4,121,408 | GEX Change vs 上次快照 -4,092,358 | Flip: Primary Flip: 54.91（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 272 / LOW 61 / INVALID 99
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 54.91（全链重定价，覆盖 99%）
最近结构参考: Flip 55（现价低于该位 3.3%）
量化视角： 负 Gamma（412万，无历史分位）｜负 Gamma 加深（409万）｜现价位于 Flip 下方 3.30%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 55（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 55（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 53.0P — Vol 318 | 最新价 $0.58 | OI 697→974 (ΔOI +277张) | ΔOI/Volume 87.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增277张（+39.7% vs前日OI），连续性待观察（方向未知）
09-11 54.0P — Vol 457 | 最新价 $0.80 | OI 957→1182 (ΔOI +225张) | ΔOI/Volume 49.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增225张（+23.5% vs前日OI），连续性待观察（方向未知）
09-25 50.0P — Vol 164 | 最新价 $1.06 | OI 291→450 (ΔOI +159张) | ΔOI/Volume 97.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增159张（+54.6% vs前日OI），连续性待观察（方向未知）
10-09 50.0P — Vol 159 | 最新价 $1.77 | OI 37→195 (ΔOI +158张) | ΔOI/Volume 99.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增158张（+427.0% vs前日OI），连续性待观察（方向未知）
09-11 38.0P — Vol 116 | 最新价 $0.02 | OI 9→125 (ΔOI +116张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增116张（+1288.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 935 张（Put 935 / Call 0），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +0.2k / P +0.8k ｜ Activity HIGH ｜ 1D
09-18  C -0.7k / P +0.1k ｜ Activity HIGH ｜ 8D
09-25  C +0.1k / P +0.2k ｜ Activity HIGH ｜ 15D
10-02  C +34 / P +27 ｜ Activity MEDIUM △ ｜ 22D

📆 09-11 Forward Structure
存量OI:      C 9.8k / P 8.0k
今日变化ΔOI: C +0.2k / P +0.8k
平值价格ATM:  C 2.18 / P 0.58
隐含波动率 ATM IV:  74.4%
净 delta 敞口变化 ΔOI Δ Exposure*: -14k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 53 ｜ +277 ｜ $0.58 ｜ 名义 $16.1k* ｜ -0.2%
P 54 ｜ +225 ｜ $0.80 ｜ 名义 $18.0k* ｜ +1.7%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：54（+1.7%） / 53（-0.2%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 55（结算参考）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 74.4%｜历史 Rank 60%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 14,277 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 50.5k / P 44.6k
今日变化ΔOI: C -0.7k / P +0.1k
平值价格ATM:  C 3.00 / P 1.50
隐含波动率 ATM IV:  61.9%
净 delta 敞口变化 ΔOI Δ Exposure*: -24k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 56 ｜ -533 ｜ $1.79 ｜ 名义 $-95.4k* ｜ +5.5%
P 52 ｜ +66 ｜ $1.18 ｜ 名义 $7.8k* ｜ -2.1%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：52（-2.1%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 55（结算参考） ｜ Put Wall 55（+3.6%，弱）（OI 9.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 61.9%｜历史 Rank 60%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 负 23,687 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-25 Forward Structure
存量OI:      C 4.3k / P 4.1k
今日变化ΔOI: C +0.1k / P +0.2k
平值价格ATM:  C 4.53 / P 2.07
隐含波动率 ATM IV:  69.0%
净 delta 敞口变化 ΔOI Δ Exposure*: -693 shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 50 ｜ +159 ｜ $1.06 ｜ 名义 $16.9k* ｜ -5.8%
P 53 ｜ +39 ｜ $2.07 ｜ 名义 $8.1k* ｜ -0.2%
C 54 ｜ +38 ｜ $3.44 ｜ 名义 $13.1k* ｜ +1.7%
结构参考：54（+1.7%） / 50（-5.8%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 52（结算参考）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 69.0%｜历史 Rank 60%（近端代理）｜净 delta 敞口 负 693 股（方向不可观测）——方向不可观测，观察点，非方向信号

10-02（MEDIUM △）Top ΔOI: 51C +19 ｜ 58C +16
10-02（MEDIUM △）仓位参考: Max Pain 59（结算参考） ｜ Put Wall 50（-5.8%）（OI 1.2k）

📅 事件差分（观察，非因果）: 09-11（1D）ATM IV 74.4% vs 09-18 61.9%（差 +12.4pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=14 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=14）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-10/MP_morning.json