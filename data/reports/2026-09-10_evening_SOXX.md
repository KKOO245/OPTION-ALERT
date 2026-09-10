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
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **单日价格波动**: -2.6%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **事件差分**: 09-11 ATM IV 52.2% vs 09-18 37.8%（差 +14.4pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## SOXX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SOXX: 今开 518.32 → 收盘 517.43（-0.2%） ｜ 今日高 522.50 ｜ 低 514.31 ｜ 昨收 532.00 → 收盘 517.43（-2.7%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-09-15，窗口结束前不做对错判定）

Options: P/C成交量 1.39 | OI比 1.65 | ATM IV 52.2% | Skew 9.9pp | Term 0.73 | ExpMove ±2.1%（近端） | Rank 88%
量化视角： IV 历史高位（Rank 88%，期权偏贵）｜期限结构倒挂（Term 0.73，近月 IV 高于远月）｜保护溢价显著（Skew 9.9pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 1.39）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.39×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.65×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-11（1D）±2.1% ｜ 09-18（8D）±4.3% ｜ 09-25（15D）±6.2% ｜ 10-02（22D）±8.5%
   ⇒ IV–VIX Spread: +34.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -13,908,996 | GEX Change vs 上次快照 -4,916,238 | Flip: Primary Flip: 523.88（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 563 / LOW 378 / INVALID 719
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 523.88（全链重定价，覆盖 98%）
最近结构参考: Flip 524（现价低于该位 1.2%）
量化视角： 负 Gamma（1391万，无历史分位）｜负 Gamma 加深（492万）｜现价位于 Flip 下方 1.23%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 518（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 524（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 497.5P — Vol 305 | 最新价 $0.45 | OI 518→2238 (ΔOI +1720张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1720张（+332.1% vs前日OI），连续性待观察（方向未知）
09-18 525.0P — Vol 40 | 最新价 $15.50 | OI 379→1807 (ΔOI +1428张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1428张（+376.8% vs前日OI），连续性待观察（方向未知）
09-11 495.0P — Vol 25 | 最新价 $0.46 | OI 62→1461 (ΔOI +1399张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1399张（+2256.4% vs前日OI），连续性待观察（方向未知）
09-11 520.0P — Vol 103 | 最新价 $5.30 | OI 94→753 (ΔOI +659张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增659张（+701.1% vs前日OI），连续性待观察（方向未知）
09-18 600.0C — Vol 10 | 最新价 $0.10 | OI 2034→2690 (ΔOI +656张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增656张（+32.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,862 张（Put 5,206 / Call 656），跨 2 个期限｜近端保护（4 档，距现价 ≤5%，权利金合计约 $3M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +0.1k / P +3.7k ｜ Activity HIGH ｜ 1D
09-18  C -1.3k / P -1.6k ｜ Activity HIGH ｜ 8D
09-25  C -0.3k / P +98 ｜ Activity MEDIUM △ ｜ 15D
10-02  C -0.2k / P +0.5k ｜ Activity HIGH ｜ 22D

📆 09-11 Forward Structure
存量OI:      C 13.7k / P 22.6k
今日变化ΔOI: C +0.1k / P +3.7k
平值价格ATM:  C 6.54 / P 4.35
隐含波动率 ATM IV:  52.2%
净 delta 敞口变化 ΔOI Δ Exposure*: -96k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 497 ｜ +1,720 ｜ $0.45 ｜ 名义 $77.4k* ｜ -3.9%
P 495 ｜ +1,399 ｜ $0.46 ｜ 名义 $64.4k* ｜ -4.3%
P 520 ｜ +659 ｜ $5.30 ｜ 名义 $349.3k* ｜ +0.5%
结构参考：520（+0.5%） / 497（-3.9%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 518（结算参考） ｜ Call Wall 530（+2.4%）（OI 3.2k） ｜ Put Wall 500（-3.4%，弱）（OI 3.1k）
量化解读： 存量 Put 重｜ATM IV 52.2%｜历史 Rank 88%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 95,931 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 99.4k / P 91.6k
今日变化ΔOI: C -1.3k / P -1.6k
平值价格ATM:  C 11.90 / P 10.50
隐含波动率 ATM IV:  37.8%
净 delta 敞口变化 ΔOI Δ Exposure*: -65k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 485 ｜ -1,430 ｜ $2.40 ｜ 名义 $-343.2k* ｜ -6.3%
P 525 ｜ +1,428 ｜ $15.50 ｜ 名义 $2.21M* ｜ +1.5%
P 500 ｜ -1,117 ｜ $5.64 ｜ 名义 $-630.0k* ｜ -3.4%
结构参考：525（+1.5%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 530（结算参考）
量化解读： 存量两侧均衡｜ATM IV 37.8%｜历史 Rank 88%（近端代理）｜净 delta 敞口 负 65,415 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-25（MEDIUM △）Top ΔOI: 490P -120
09-25（MEDIUM △）仓位参考: Max Pain 530（结算参考） ｜ Put Wall 480（-7.2%，弱）（OI 1.9k）

📆 10-02 Forward Structure
存量OI:      C 10.4k / P 8.7k
今日变化ΔOI: C -0.2k / P +0.5k
平值价格ATM:  C 29.00 / P 15.00
隐含波动率 ATM IV:  38.8%
净 delta 敞口变化 ΔOI Δ Exposure*: -4k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 425 ｜ +603 ｜ $1.18 ｜ 名义 $71.2k* ｜ -17.9%
P 485 ｜ -79 ｜ $7.30 ｜ 名义 $-57.7k* ｜ -6.3%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：425（-17.9%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 525（结算参考） ｜ Call Wall 542.5（+4.8%，弱）（OI 2.8k） ｜ Put Wall 470（-9.2%）（OI 2.8k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 38.8%｜历史 Rank 88%（近端代理）｜净 delta 敞口 负 4,088 股（方向不可观测）——方向不可观测，观察点，非方向信号

📅 事件差分（观察，非因果）: 09-11（1D）ATM IV 52.2% vs 09-18 37.8%（差 +14.4pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=14 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=14）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-10/SOXX_evening.json