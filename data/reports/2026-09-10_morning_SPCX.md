# 期权晨报 2026-09-10（快照 10:56 ET）

📊 市场环境

SPY $758.49 ｜ QQQ $708.69
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
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **事件差分**: 09-11 ATM IV 66.9% vs 09-18 55.3%（差 +11.7pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 09-11 152P ΔOI -6,941（距现价 +1.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 147.55 → 今开 145.10（-1.7%） | 较昨收变动（含盘初走势） ｜ 今日高 154.70 ｜ 低 144.89

Options: P/C成交量 0.52 | OI比 1.43 | ATM IV 66.9% | Skew -1.2pp | Term 0.78 | ExpMove ±3.1%（近端） | Rank 68%
量化视角： IV 中性（Rank 68%）｜期限结构倒挂（Term 0.78，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.2pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.52×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.43×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-11（1D）±3.1% ｜ 09-18（8D）±6.6% ｜ 09-25（15D）±8.7% ｜ 10-02（22D）±10.3%
   ⇒ IV–VIX Spread: +49.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 62,908,887 | GEX Change vs 上次快照 77,548,335 | Flip: Primary Flip: 146.23（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 653 / LOW 148 / INVALID 303
结构观察区: Primary Flip 146.23（全链重定价，覆盖 100%）
Call Wall 150（弱结构｜现价高于该位 0.0%）
最近结构参考: Call Wall 150（现价高于该位 0.0%）
量化视角： 正 Gamma（6291万，无历史分位）｜由负转正（+7755万）｜现价位于 Flip 上方 2.62%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 147（MaxPain，仅结算参考） / 150（Call Wall，弱结构）。
• Gamma 区域：切换参考 146（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 155.0C — Vol 59,847 | 最新价 $2.36 | OI 17299→55470 (ΔOI +38171张) | ΔOI/Volume 63.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增38171张（+220.7% vs前日OI），连续性待观察（方向未知）
09-18 150.0C — Vol 20,433 | 最新价 $4.02 | OI 44286→50058 (ΔOI +5772张) | ΔOI/Volume 28.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5772张（+13.0% vs前日OI），连续性待观察（方向未知）
09-18 165.0C — Vol 15,569 | 最新价 $0.74 | OI 23215→28808 (ΔOI +5593张) | ΔOI/Volume 35.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5593张（+24.1% vs前日OI），连续性待观察（方向未知）
09-11 147.0C — Vol 18,790 | 最新价 $2.93 | OI 1498→5016 (ΔOI +3518张) | ΔOI/Volume 18.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3518张（+234.8% vs前日OI），连续性待观察（方向未知）
09-11 152.5C — Vol 21,908 | 最新价 $0.92 | OI 6572→8898 (ΔOI +2326张) | ΔOI/Volume 10.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2326张（+35.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 55,380 张（Put 0 / Call 55,380），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +16.2k / P -15.1k ｜ Activity HIGH ｜ 1D
09-18  C +57.3k / P +2.6k ｜ Activity HIGH ｜ 8D
09-25  C +4.4k / P +1.4k ｜ Activity HIGH ｜ 15D
10-02  C +2.1k / P +3.4k ｜ Activity HIGH ｜ 22D

📆 09-11 Forward Structure
存量OI:      C 162.7k / P 231.8k
今日变化ΔOI: C +16.2k / P -15.1k
平值价格ATM:  C 2.40 / P 2.26
隐含波动率 ATM IV:  66.9%
净 delta 敞口变化 ΔOI Δ Exposure*: 1.4M shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 152 ｜ -6,941 ｜ $3.90 ｜ 名义 $-2.71M* ｜ +1.6%
P 150 ｜ -5,798 ｜ $2.26 ｜ 名义 $-1.31M* ｜ -0.0%
P 145 ｜ -4,713 ｜ $0.66 ｜ 名义 $-311.1k* ｜ -3.4%
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 147（结算参考） ｜ Call Wall 160（+6.6%）（OI 26.4k） ｜ Put Wall 140（-6.7%，弱）（OI 28.9k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 66.9%｜历史 Rank 68%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,394,608 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 590.1k / P 478.2k
今日变化ΔOI: C +57.3k / P +2.6k
平值价格ATM:  C 5.07 / P 4.90
隐含波动率 ATM IV:  55.3%
净 delta 敞口变化 ΔOI Δ Exposure*: 1.9M shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 155 ｜ +38,171 ｜ $2.98 ｜ 名义 $11.37M* ｜ +3.3%
C 150 ｜ +5,772 ｜ $5.07 ｜ 名义 $2.93M* ｜ -0.0%
C 165 ｜ +5,593 ｜ $0.98 ｜ 名义 $548.1k* ｜ +10.0%
结构参考：155（+3.3%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 145（结算参考） ｜ Call Wall 155（+3.3%，弱）（OI 55.5k） ｜ Put Wall 150（-0.0%，弱）（OI 45.8k）
量化解读： 存量 Call 重｜ATM IV 55.3%｜历史 Rank 68%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,939,495 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-25 Forward Structure
存量OI:      C 47.9k / P 65.7k
今日变化ΔOI: C +4.4k / P +1.4k
平值价格ATM:  C 6.63 / P 6.40
隐含波动率 ATM IV:  53.2%
净 delta 敞口变化 ΔOI Δ Exposure*: 109k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 170 ｜ +1,662 ｜ $1.33 ｜ 名义 $221.0k* ｜ +13.3%
C 160 ｜ +779 ｜ $3.10 ｜ 名义 $241.5k* ｜ +6.6%
C 148 ｜ +756 ｜ $7.74 ｜ 名义 $585.1k* ｜ -1.4%
结构参考：170（+13.3%） / 148（-1.4%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 144（结算参考）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 53.2%｜历史 Rank 68%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 108,653 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 10-02 Forward Structure
存量OI:      C 23.5k / P 35.3k
今日变化ΔOI: C +2.1k / P +3.4k
平值价格ATM:  C 7.95 / P 7.55
隐含波动率 ATM IV:  52.5%
净 delta 敞口变化 ΔOI Δ Exposure*: 258 shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 130 ｜ +861 ｜ $1.53 ｜ 名义 $131.7k* ｜ -13.4%
C 170 ｜ +756 ｜ $2.05 ｜ 名义 $155.0k* ｜ +13.3%
P 147 ｜ +485 ｜ $5.85 ｜ 名义 $283.7k* ｜ -2.0%
结构参考：170（+13.3%） / 130（-13.4%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 145（结算参考）
量化解读： 存量 Put 重｜ATM IV 52.5%｜历史 Rank 68%（近端代理）｜净 delta 敞口 正 258 股（方向不可观测）——方向不可观测，观察点，非方向信号

📅 事件差分（观察，非因果）: 09-11（1D）ATM IV 66.9% vs 09-18 55.3%（差 +11.7pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-10/SPCX_morning.json