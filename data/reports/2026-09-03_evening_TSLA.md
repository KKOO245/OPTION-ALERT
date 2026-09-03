# 期权晚报 2026-09-03（快照 17:36 ET）

📊 市场环境

SPY $773.17 ｜ QQQ $717.67
VIX 14.32 ↓5.8%（5D -1.3%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 35.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 55.4 ｜ 前值 54.1　✅ 今日已公布
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 56 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **事件差分**: 09-04（1D）ATM IV 73.4% vs 09-09 43.4%（差 +30.0pp），覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 09-04 372C ΔOI +5,804（距现价 -1.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 365.92 → 收盘 376.36（+2.9%） ｜ 今日高 384.04 ｜ 低 365.91
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-09-10，窗口结束前不做对错判定）

Options: P/C成交量 0.60 | OI比 0.78 | ATM IV 73.4% | Skew -2.7pp | Term 0.59 | ExpMove ±3.1%（近端） | Rank 86%
量化视角： IV 历史高位（Rank 86%，期权偏贵）｜期限结构倒挂（Term 0.59，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.7pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.78）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.60×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.78×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（1D）±3.1% ｜ 09-09（6D）±4.4% ｜ 09-11（8D）±5.4% ｜ 09-14（11D）±5.8%
   ⇒ IV–VIX Spread: +59.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 179,375,066 | GEX Change vs 上次快照 -4,470,433 | Flip: Primary Flip: 345.21（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1184 / LOW 122 / INVALID 472
结构观察区: Primary Flip 345.21（全链重定价，覆盖 100%）
Put Wall 340（弱结构｜现价高于该位 10.7%） | Call Wall 400（现价低于该位 5.9%）
最近结构参考: Call Wall 400（现价低于该位 5.9%）
量化视角： 正 Gamma（1.79亿，无历史分位）｜正 Gamma 减弱（447万）｜现价位于 Flip 上方 9.02%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 340（Put Wall，弱结构）；上方 352（MaxPain，仅结算参考） / 400（Call Wall）。
• Gamma 区域：切换参考 345（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 372.5C — Vol 40,736 | 最新价 $8.05 | OI 9763→15567 (ΔOI +5804张) | ΔOI/Volume 14.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5804张（+59.5% vs前日OI），连续性待观察（方向未知）
09-04 327.5P — Vol 9,210 | 最新价 $0.08 | OI 1028→6739 (ΔOI +5711张) | ΔOI/Volume 62.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5711张（+555.5% vs前日OI），连续性待观察（方向未知）
09-04 352.5P — Vol 9,168 | 最新价 $0.45 | OI 2846→7462 (ΔOI +4616张) | ΔOI/Volume 50.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4616张（+162.2% vs前日OI），连续性待观察（方向未知）
09-11 400.0C — Vol 19,121 | 最新价 $2.94 | OI 15916→19930 (ΔOI +4014张) | ΔOI/Volume 21.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4014张（+25.2% vs前日OI），连续性待观察（方向未知）
09-09 290.0P — Vol 69 | 最新价 $0.09 | OI 37→3022 (ΔOI +2985张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2985张（+8067.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 23,130 张（Put 13,312 / Call 9,818），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C +36.5k / P +31.1k ｜ Activity MEDIUM △ ｜ 1D
09-09  C +16.9k / P +5.6k ｜ Activity HIGH ｜ 6D
09-11  C +8.9k / P +8.8k ｜ Activity HIGH ｜ 8D
09-14  C +1.4k / P +1.3k ｜ Activity HIGH ｜ 11D

📆 09-04 Forward Structure
存量OI:      C 269.4k / P 209.3k
今日变化ΔOI: C +36.5k / P +31.1k
平值价格ATM:  C 5.35 / P 6.43
隐含波动率 ATM IV:  73.4%
净 delta 敞口变化 ΔOI Δ Exposure*: 1.9M shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 372 ｜ +5,804 ｜ $8.05 ｜ 名义 $4.67M* ｜ -1.0%
P 352 ｜ +4,616 ｜ $0.45 ｜ 名义 $207.7k* ｜ -6.3%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：372（-1.0%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 73.4%｜历史 Rank 86%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,920,942 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-09 Forward Structure
存量OI:      C 58.7k / P 17.5k
今日变化ΔOI: C +16.9k / P +5.6k
平值价格ATM:  C 7.90 / P 8.80
隐含波动率 ATM IV:  43.4%
净 delta 敞口变化 ΔOI Δ Exposure*: 678k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 400 ｜ +2,763 ｜ $1.88 ｜ 名义 $519.4k* ｜ +6.3%
C 365 ｜ +2,167 ｜ $15.50 ｜ 名义 $3.36M* ｜ -3.0%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：400（+6.3%） / 365（-3.0%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 43.4%｜历史 Rank 86%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 677,767 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-11 Forward Structure
存量OI:      C 96.8k / P 75.6k
今日变化ΔOI: C +8.9k / P +8.8k
平值价格ATM:  C 9.75 / P 10.45
隐含波动率 ATM IV:  45.2%
净 delta 敞口变化 ΔOI Δ Exposure*: 310k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 400 ｜ +4,014 ｜ $2.94 ｜ 名义 $1.18M* ｜ +6.3%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：400（+6.3%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 45.2%｜历史 Rank 86%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 310,050 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-14 Forward Structure
存量OI:      C 4.9k / P 2.9k
今日变化ΔOI: C +1.4k / P +1.3k
平值价格ATM:  C 11.54 / P 10.10
隐含波动率 ATM IV:  41.8%
净 delta 敞口变化 ΔOI Δ Exposure*: 50k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 365 ｜ +481 ｜ $5.80 ｜ 名义 $279.0k* ｜ -3.0%
C 355 ｜ +340 ｜ $27.05 ｜ 名义 $919.7k* ｜ -5.7%
C 370 ｜ +143 ｜ $17.60 ｜ 名义 $251.7k* ｜ -1.7%
结构参考：365（-3.0%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 41.8%｜历史 Rank 86%（近端代理）｜净 delta 敞口 正 50,408 股（方向不可观测）——方向不可观测，观察点，非方向信号

📅 事件差分（观察，非因果）: 09-04（1D）ATM IV 73.4% vs 09-09 43.4%（差 +30.0pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-03/TSLA_evening.json