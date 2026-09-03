# 期权晨报 2026-09-03（快照 11:17 ET）

📊 市场环境

SPY $769.44 ｜ QQQ $716.16
VIX 14.85 ↓2.3%（5D -2.4%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 35.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 55.4 ｜ 前值 54.1　✅ 今日已公布
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 56 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **事件差分**: 09-04（1D）ATM IV 71.4% vs 09-09 44.5%（差 +26.9pp），覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **单日价格波动**: +6.4%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-04 372C ΔOI +5,804（距现价 -2.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 357.01 → 今开 365.92（+2.5%） | 较昨收变动（含盘初走势） ｜ 今日高 381.64 ｜ 低 365.91

Options: P/C成交量 0.47 | OI比 0.78 | ATM IV 71.4% | Skew -2.8pp | Term 0.62 | ExpMove ±3.3%（近端） | Rank 85%
量化视角： IV 历史高位（Rank 85%，期权偏贵）｜期限结构倒挂（Term 0.62，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.8pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.78）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.47×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.78×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（1D）±3.3% ｜ 09-09（6D）±4.6% ｜ 09-11（8D）±5.6% ｜ 09-14（11D）±6.0%
   ⇒ IV–VIX Spread: +56.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 182,364,556 | GEX Change vs 上次快照 100,945,738 | Flip: Primary Flip: 345.39（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1193 / LOW 89 / INVALID 496
结构观察区: Primary Flip 345.39（全链重定价，覆盖 100%）
Call Wall 400（现价低于该位 5.0%）
最近结构参考: Call Wall 400（现价低于该位 5.0%）
量化视角： 正 Gamma（1.82亿，无历史分位）｜正 Gamma 增强（+1.01亿）｜现价位于 Flip 上方 10.00%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 345（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 372.5C — Vol 26,101 | 最新价 $5.30 | OI 9763→15567 (ΔOI +5804张) | ΔOI/Volume 22.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5804张（+59.5% vs前日OI），连续性待观察（方向未知）
09-04 327.5P — Vol 6,373 | 最新价 $0.06 | OI 1028→6739 (ΔOI +5711张) | ΔOI/Volume 89.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5711张（+555.5% vs前日OI），连续性待观察（方向未知）
09-04 352.5P — Vol 3,382 | 最新价 $0.83 | OI 2846→7462 (ΔOI +4616张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4616张（+162.2% vs前日OI），连续性待观察（方向未知）
09-11 400.0C — Vol 4,831 | 最新价 $2.38 | OI 15916→19930 (ΔOI +4014张) | ΔOI/Volume 83.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4014张（+25.2% vs前日OI），连续性待观察（方向未知）
09-09 290.0P — Vol 8 | 最新价 $0.10 | OI 37→3022 (ΔOI +2985张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2985张（+8067.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 23,130 张（Put 13,312 / Call 9,818），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C +36.5k / P +31.1k ｜ Activity HIGH ｜ 1D
09-09  C +16.9k / P +5.6k ｜ Activity HIGH ｜ 6D
09-11  C +8.9k / P +8.8k ｜ Activity HIGH ｜ 8D
09-14  C +1.4k / P +1.3k ｜ Activity HIGH ｜ 11D

📆 09-04 Forward Structure
存量OI:      C 269.4k / P 209.3k
今日变化ΔOI: C +36.5k / P +31.1k
平值价格ATM:  C 6.05 / P 6.45
隐含波动率 ATM IV:  71.4%
净 delta 敞口变化 ΔOI Δ Exposure*: 2.1M shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 372 ｜ +5,804 ｜ $10.40 ｜ 名义 $6.04M* ｜ -2.0%
P 352 ｜ +4,616 ｜ $0.34 ｜ 名义 $156.9k* ｜ -7.2%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：372（-2.0%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 71.4%｜历史 Rank 85%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,105,532 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-09 Forward Structure
存量OI:      C 58.7k / P 17.5k
今日变化ΔOI: C +16.9k / P +5.6k
平值价格ATM:  C 8.59 / P 8.95
隐含波动率 ATM IV:  44.5%
净 delta 敞口变化 ΔOI Δ Exposure*: 737k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 400 ｜ +2,763 ｜ $2.66 ｜ 名义 $735.0k* ｜ +5.3%
C 365 ｜ +2,167 ｜ $18.27 ｜ 名义 $3.96M* ｜ -3.9%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：400（+5.3%） / 365（-3.9%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 44.5%｜历史 Rank 85%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 737,021 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-11 Forward Structure
存量OI:      C 96.8k / P 75.6k
今日变化ΔOI: C +8.9k / P +8.8k
平值价格ATM:  C 10.51 / P 10.65
隐含波动率 ATM IV:  46.6%
净 delta 敞口变化 ΔOI Δ Exposure*: 347k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 400 ｜ +4,014 ｜ $4.03 ｜ 名义 $1.62M* ｜ +5.3%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：400（+5.3%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 46.6%｜历史 Rank 85%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 346,718 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-14 Forward Structure
存量OI:      C 4.9k / P 2.9k
今日变化ΔOI: C +1.4k / P +1.3k
平值价格ATM:  C 11.30 / P 11.65
隐含波动率 ATM IV:  43.2%
净 delta 敞口变化 ΔOI Δ Exposure*: 58k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 365 ｜ +481 ｜ $5.09 ｜ 名义 $244.8k* ｜ -3.9%
C 355 ｜ +340 ｜ $29.00 ｜ 名义 $986.0k* ｜ -6.6%
C 370 ｜ +143 ｜ $17.15 ｜ 名义 $245.2k* ｜ -2.6%
结构参考：365（-3.9%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 43.2%｜历史 Rank 85%（近端代理）｜净 delta 敞口 正 58,084 股（方向不可观测）——方向不可观测，观察点，非方向信号

📅 事件差分（观察，非因果）: 09-04（1D）ATM IV 71.4% vs 09-09 44.5%（差 +26.9pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-03/TSLA_morning.json