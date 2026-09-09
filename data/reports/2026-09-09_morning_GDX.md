# 期权晨报 2026-09-09（快照 11:03 ET）

📊 市场环境

SPY $763.65 ｜ QQQ $717.17
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
🟡 **近现价集中开仓**: 09-11 100C ΔOI +1,188（距现价 +0.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 98.41 → 今开 100.46（+2.1%） | 较昨收变动（含盘初走势） ｜ 今日高 101.48 ｜ 低 99.36

Options: P/C成交量 0.55 | OI比 0.55 | ATM IV 58.5% | Skew -3.1pp | Term 0.79 | ExpMove ±3.7%（近端） | Rank 93%
量化视角： IV 历史高位（Rank 93%，期权偏贵）｜期限结构倒挂（Term 0.79，近月 IV 高于远月）｜Put 保护异常便宜（Skew -3.1pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.55）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.55×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.55×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（2D）±3.7% ｜ 09-18（9D）±6.4% ｜ 09-25（16D）±8.0% ｜ 10-02（23D）±10.1%
   ⇒ IV–VIX Spread: +42.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 54,258,711 | GEX Change vs 上次快照 28,091,369 | Flip: Primary Flip: 96.80（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 639 / LOW 142 / INVALID 169
结构观察区: Primary Flip 96.80（全链重定价，覆盖 100%）
Call Wall 100（弱结构｜现价低于该位 0.0%）
最近结构参考: Call Wall 100（现价低于该位 0.0%）
量化视角： 正 Gamma（5426万，无历史分位）｜正 Gamma 增强（+2809万）｜现价位于 Flip 上方 3.27%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 98（MaxPain，仅结算参考）；上方 100（Call Wall，弱结构）。
• Gamma 区域：切换参考 97（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 90.0P — Vol 3,517 | 最新价 $0.56 | OI 42261→44239 (ΔOI +1978张) | ΔOI/Volume 56.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1978张（+4.7% vs前日OI），连续性待观察（方向未知）
09-11 90.0P — Vol 1,848 | 最新价 $0.14 | OI 9781→11336 (ΔOI +1555张) | ΔOI/Volume 84.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1555张（+15.9% vs前日OI），连续性待观察（方向未知）
09-11 100.0C — Vol 1,847 | 最新价 $1.40 | OI 5483→6671 (ΔOI +1188张) | ΔOI/Volume 64.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1188张（+21.7% vs前日OI），连续性待观察（方向未知）
09-18 112.0C — Vol 1,036 | 最新价 $0.32 | OI 365→1314 (ΔOI +949张) | ΔOI/Volume 91.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增949张（+260.0% vs前日OI），连续性待观察（方向未知）
09-11 105.0C — Vol 1,574 | 最新价 $0.33 | OI 4910→5717 (ΔOI +807张) | ΔOI/Volume 51.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增807张（+16.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 6,477 张（Put 3,533 / Call 2,944），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +2.8k / P +4.7k ｜ Activity HIGH ｜ 2D
09-18  C +1.0k / P +2.1k ｜ Activity HIGH ｜ 9D
09-25  C +0.4k / P +0.6k ｜ Activity HIGH ｜ 16D
10-02  C +0.3k / P +39 ｜ Activity MEDIUM △ ｜ 23D

📆 09-11 Forward Structure
存量OI:      C 105.4k / P 57.5k
今日变化ΔOI: C +2.8k / P +4.7k
平值价格ATM:  C 1.73 / P 1.93
隐含波动率 ATM IV:  58.5%
净 delta 敞口变化 ΔOI Δ Exposure*: 67k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 90 ｜ +1,555 ｜ $0.07 ｜ 名义 $10.9k* ｜ -10.0%
C 100 ｜ +1,188 ｜ $1.73 ｜ 名义 $205.5k* ｜ +0.0%
C 107 ｜ -986 ｜ $0.24 ｜ 名义 $-23.7k* ｜ +7.0%
结构参考：90（-10.0%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 98（结算参考） ｜ Call Wall 104（+4.0%，弱）（OI 17.0k） ｜ Put Wall 90（-10.0%）（OI 11.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 58.5%｜历史 Rank 93%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 67,128 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 247.9k / P 418.7k
今日变化ΔOI: C +1.0k / P +2.1k
平值价格ATM:  C 3.18 / P 3.25
隐含波动率 ATM IV:  50.7%
净 delta 敞口变化 ΔOI Δ Exposure*: -18k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 90 ｜ +1,978 ｜ $0.43 ｜ 名义 $85.1k* ｜ -10.0%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：90（-10.0%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 90（结算参考） ｜ Call Wall 100（+0.0%，弱）（OI 23.8k）
量化解读： 存量 Put 重｜ATM IV 50.7%｜历史 Rank 93%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 18,489 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-25 Forward Structure
存量OI:      C 6.9k / P 7.9k
今日变化ΔOI: C +0.4k / P +0.6k
平值价格ATM:  C 4.17 / P 3.80
隐含波动率 ATM IV:  48.0%
净 delta 敞口变化 ΔOI Δ Exposure*: 7k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 105 ｜ +275 ｜ $2.13 ｜ 名义 $58.6k* ｜ +5.0%
P 90 ｜ +140 ｜ $0.77 ｜ 名义 $10.8k* ｜ -10.0%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：105（+5.0%） / 90（-10.0%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 96（结算参考） ｜ Call Wall 105（+5.0%）（OI 1.0k）
量化解读： 存量两侧均衡｜ATM IV 48.0%｜历史 Rank 93%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 6,873 股（方向不可观测）——方向不可观测，观察点，非方向信号

10-02（MEDIUM △）Top ΔOI: 110C +238 ｜ 97P -48
10-02（MEDIUM △）仓位参考: Max Pain 99（结算参考） ｜ Put Wall 97（-3.0%）（OI 15.1k）

📅 事件差分（观察，非因果）: 09-11（2D）ATM IV 58.5% vs 09-18 50.7%（差 +7.9pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-09/GDX_morning.json