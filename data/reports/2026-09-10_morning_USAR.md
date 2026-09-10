# 期权晨报 2026-09-10（快照 10:56 ET）

📊 市场环境

SPY $759.44 ｜ QQQ $711.34
VIX 17.34 ↑5.3%（5D +21.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-10 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 0.4 ｜ 前值 0.1　✅ 今日已公布
- 周四 09-10 10:00　【高】成屋销售　预测 3.98 ｜ 实际 3.98 ｜ 前值 4.06　✅ 今日已公布
- 周五 09-11 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.2
- 周五 09-11 08:30　【高】Inflation Rate YoY　预测 3.4 ｜ 实际 待公布 ｜ 前值 3.4
- 周五 09-11 08:30　【高】Inflation Rate MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.1
- 周五 09-11 08:30　【高】Core Inflation Rate YoY　预测 2.4 ｜ 实际 待公布 ｜ 前值 2.5
- 周五 09-11 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 51 ｜ 实际 待公布 ｜ 前值 51.7

🔍 重点速览
🔴 **事件差分**: 09-11（1D）ATM IV 106.4% vs 09-18 80.0%（差 +26.4pp），覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate YoY、Inflation Rate MoM、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **单日价格波动**: -2.7%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 17.06 → 今开 16.95（-0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 16.97 ｜ 低 16.33

Options: P/C成交量 0.69 | OI比 0.54 | ATM IV 106.4% | Skew -3.4pp | Term 0.76 | ExpMove ±5.2%（近端） | Rank 26%
量化视角： IV 中性（Rank 26%）｜期限结构倒挂（Term 0.76，近月 IV 高于远月）｜Put 保护异常便宜（Skew -3.4pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.54）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.69×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.54×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（1D）±5.2% ｜ 09-18（8D）±10.4% ｜ 09-25（15D）±16.6% ｜ 10-02（22D）±17.2%
   ⇒ IV–VIX Spread: +89.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -3,664,781 | GEX Change vs 上次快照 -4,517,701 | Flip: Primary Flip: 17.09（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 226 / LOW 96 / INVALID 162
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 17.09（全链重定价，覆盖 99%）
Put Wall 15（弱结构｜现价高于该位 10.7%）
最近结构参考: Flip 17（现价低于该位 2.9%）
量化视角： 负 Gamma（366万，无历史分位）｜由正转负（452万）｜现价位于 Flip 下方 2.89%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall，弱结构）；上方 18（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 17（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 16.0P — Vol 1,067 | 最新价 $0.99 | OI 45→1112 (ΔOI +1067张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1067张（+2371.1% vs前日OI），连续性待观察（方向未知）
09-11 17.0P — Vol 1,352 | 最新价 $0.40 | OI 4020→4787 (ΔOI +767张) | ΔOI/Volume 56.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增767张（+19.1% vs前日OI），连续性待观察（方向未知）
09-18 16.0P — Vol 430 | 最新价 $0.36 | OI 2480→2792 (ΔOI +312张) | ΔOI/Volume 72.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增312张（+12.6% vs前日OI），连续性待观察（方向未知）
09-11 16.5P — Vol 503 | 最新价 $0.19 | OI 2227→2512 (ΔOI +285张) | ΔOI/Volume 56.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增285张（+12.8% vs前日OI），连续性待观察（方向未知）
09-11 16.0P — Vol 273 | 最新价 $0.06 | OI 757→989 (ΔOI +232张) | ΔOI/Volume 85.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增232张（+30.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,663 张（Put 2,663 / Call 0），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C -52 / P +1.3k ｜ Activity MEDIUM △ ｜ 1D
09-18  C +0.3k / P +0.2k ｜ Activity MEDIUM △ ｜ 8D
09-25  C +99 / P +0.2k ｜ Activity MEDIUM △ ｜ 15D
10-02  C +48 / P +0.2k ｜ Activity MEDIUM △ ｜ 22D

📆 09-11 Forward Structure
存量OI:      C 23.2k / P 12.5k
今日变化ΔOI: C -52 / P +1.3k
平值价格ATM:  C 0.44 / P 0.42
隐含波动率 ATM IV:  106.4%
净 delta 敞口变化 ΔOI Δ Exposure*: -65k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 17 ｜ +767 ｜ $0.74 ｜ 名义 $56.8k* ｜ +2.4%
P 16 ｜ +285 ｜ $0.42 ｜ 名义 $12.0k* ｜ -0.6%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：17（+2.4%） / 16（-0.6%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 18（结算参考） ｜ Put Wall 17（+2.4%）（OI 4.8k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 106.4%｜历史 Rank 26%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 65,408 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（MEDIUM △）Top ΔOI: 19P -319 ｜ 16P +312
09-18（MEDIUM △）仓位参考: Max Pain 20（结算参考）

09-25（MEDIUM △）Top ΔOI: 15P +76 ｜ 15P +57
09-25（MEDIUM △）仓位参考: Max Pain 18（结算参考） ｜ Put Wall 15（-9.6%，弱）（OI 0.7k）

10-02（MEDIUM △）Top ΔOI: 16P +63 ｜ 17C +25
10-02（MEDIUM △）仓位参考: Max Pain 18（结算参考）

📅 事件差分（观察，非因果）: 09-11（1D）ATM IV 106.4% vs 09-18 80.0%（差 +26.4pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate YoY、Inflation Rate MoM、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=14 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=14）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-10/USAR_morning.json