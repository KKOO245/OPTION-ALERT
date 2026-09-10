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
🔴 **事件差分**: 09-11（1D）ATM IV 115.1% vs 09-18 85.7%（差 +29.4pp），覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **单日价格波动**: -4.6%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-11 18P ΔOI +108（距现价 +3.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 17.84 → 收盘 17.36（-2.7%） ｜ 今日高 17.89 ｜ 低 17.23 ｜ 昨收 18.17 → 收盘 17.36（-4.5%）
Target 等待验证: 3D_mdd >= 0.03（3D） — PENDING（评估日 ≈ 2026-09-15，窗口结束前不做对错判定）

Options: P/C成交量 0.98 | OI比 0.64 | ATM IV 115.1% | Skew -31.1pp | Term 0.66 | ExpMove ±9.8%（近端） | Rank 58%
量化视角： IV 中性（Rank 58%）｜期限结构倒挂（Term 0.66，近月 IV 高于远月）｜Put 保护异常便宜（Skew -31.1pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.64）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.98×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.64×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（1D）±9.8% ｜ 09-18（8D）±14.1% ｜ 09-25（15D）±11.4% ｜ 10-02（22D）±14.9%
   ⇒ IV–VIX Spread: +97.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 610,088 | GEX Change vs 上次快照 -839,918 | Flip: Primary Flip: 16.95（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 208 / LOW 88 / INVALID 154
结构观察区: Primary Flip 16.95（全链重定价，覆盖 94%）
Put Wall 16（弱结构｜现价高于该位 8.5%）
最近结构参考: Flip 17（现价高于该位 2.4%）
量化视角： 正 Gamma（61万，无历史分位）｜正 Gamma 减弱（84万）｜现价位于 Flip 上方 2.41%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 16（Put Wall，弱结构）；上方 19（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 17（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 19.0C — Vol 1,490 | 最新价 $0.65 | OI 675→1497 (ΔOI +822张) | ΔOI/Volume 55.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增822张（+121.8% vs前日OI），连续性待观察（方向未知）
09-18 16.0P — Vol 142 | 最新价 $0.15 | OI 389→513 (ΔOI +124张) | ΔOI/Volume 87.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增124张（+31.9% vs前日OI），连续性待观察（方向未知）
09-11 18.0P — Vol 131 | 最新价 $0.29 | OI 342→450 (ΔOI +108张) | ΔOI/Volume 82.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增108张（+31.6% vs前日OI），连续性待观察（方向未知）
09-11 17.5P — Vol 120 | 最新价 $0.15 | OI 116→209 (ΔOI +93张) | ΔOI/Volume 77.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增93张（+80.2% vs前日OI），连续性待观察（方向未知）
09-25 16.0P — Vol 81 | 最新价 $0.35 | OI 23→96 (ΔOI +73张) | ΔOI/Volume 90.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增73张（+317.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,220 张（Put 398 / Call 822），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +74 / P +0.2k ｜ Activity HIGH ｜ 1D
09-18  C +0.9k / P +0.3k ｜ Activity HIGH ｜ 8D
09-25  C +9 / P +91 ｜ Activity HIGH ｜ 15D
10-02  C +13 / P +14 ｜ Activity MEDIUM △ ｜ 22D

📆 09-11 Forward Structure
存量OI:      C 5.4k / P 3.5k
今日变化ΔOI: C +74 / P +0.2k
平值价格ATM:  C 1.55 / P 0.15
隐含波动率 ATM IV:  115.1%
净 delta 敞口变化 ΔOI Δ Exposure*: -5k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 18 ｜ +108 ｜ $0.29 ｜ 名义 $3.1k* ｜ +3.7%
P 17 ｜ +93 ｜ $0.15 ｜ 名义 $1.4k* ｜ +0.8%
C 19 ｜ +65 ｜ $0.31 ｜ 名义 $2.0k* ｜ +9.4%
结构参考：18（+3.7%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 19（结算参考） ｜ Put Wall 16（-7.8%）（OI 0.8k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 115.1%｜历史 Rank 58%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 5,135 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 7.6k / P 3.5k
今日变化ΔOI: C +0.9k / P +0.3k
平值价格ATM:  C 1.90 / P 0.55
隐含波动率 ATM IV:  85.7%
净 delta 敞口变化 ΔOI Δ Exposure*: 29k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 19 ｜ +822 ｜ $0.65 ｜ 名义 $53.4k* ｜ +9.4%
P 16 ｜ +124 ｜ $0.15 ｜ 名义 $1.9k* ｜ -7.8%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：19（+9.4%） / 16（-7.8%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 19（结算参考） ｜ Call Wall 19（+9.4%，弱）（OI 1.5k） ｜ Put Wall 18（+3.7%，弱）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 85.7%｜历史 Rank 58%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 28,743 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-25 Forward Structure
存量OI:      C 4.7k / P 1.0k
今日变化ΔOI: C +9 / P +91
平值价格ATM:  C 1.20 / P 0.78
隐含波动率 ATM IV:  79.0%
净 delta 敞口变化 ΔOI Δ Exposure*: -2k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 16 ｜ +73 ｜ $0.35 ｜ 名义 $2.6k* ｜ -7.8%
C 18 ｜ -30 ｜ $1.35 ｜ 名义 $-4.0k* ｜ +6.6%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：16（-7.8%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 19（结算参考）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 79.0%｜历史 Rank 58%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 负 2,340 股（方向不可观测）——方向不可观测，观察点，非方向信号

10-02（MEDIUM △）Top ΔOI: 16P +6
10-02（MEDIUM △）仓位参考: Max Pain 19（结算参考） ｜ Put Wall 18.5（+6.6%）（OI 0.1k）

📅 事件差分（观察，非因果）: 09-11（1D）ATM IV 115.1% vs 09-18 85.7%（差 +29.4pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-10/NNE_evening.json