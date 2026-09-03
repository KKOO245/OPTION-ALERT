# 期权晨报 2026-09-03（快照 10:16 ET）

📊 市场环境

SPY $768.41 ｜ QQQ $712.44
VIX 15.00 ↓1.3%（5D -1.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 55.4 ｜ 前值 54.1　✅ 今日已公布
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 58 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **事件差分**: 09-04（1D）ATM IV 70.6% vs 09-09 43.9%（差 +26.7pp），覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **单日价格波动**: +4.1%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-04 372C ΔOI +5,804（距现价 +0.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 357.01 → 今开 365.92（+2.5%） | 较昨收变动（含盘初走势） ｜ 今日高 378.23 ｜ 低 365.91

Options: P/C成交量 0.42 | OI比 0.78 | ATM IV 70.6% | Skew -5.4pp | Term 0.62 | ExpMove ±3.4%（近端） | Rank 83%
量化视角： IV 历史高位（Rank 83%，期权偏贵）｜期限结构倒挂（Term 0.62，近月 IV 高于远月）｜Put 保护异常便宜（Skew -5.4pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.78）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.42×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.78×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（1D）±3.4% ｜ 09-09（6D）±4.6% ｜ 09-11（8D）±5.6% ｜ 09-14（11D）±6.0%
   ⇒ IV–VIX Spread: +55.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 171,067,936 | GEX Change vs 上次快照 89,649,118 | Flip: Primary Flip: 344.93（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1203 / LOW 100 / INVALID 475
结构观察区: Primary Flip 344.93（全链重定价，覆盖 100%）
Put Wall 340（弱结构｜现价高于该位 9.3%） | Call Wall 400（现价低于该位 7.1%）
最近结构参考: Call Wall 400（现价低于该位 7.1%）
量化视角： 正 Gamma（1.71亿，无历史分位）｜正 Gamma 增强（+8965万）｜现价位于 Flip 上方 7.73%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 340（Put Wall，弱结构）；上方 352（MaxPain，仅结算参考） / 400（Call Wall）。
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
平值价格ATM:  C 5.30 / P 7.20
隐含波动率 ATM IV:  70.6%
净 delta 敞口变化 ΔOI Δ Exposure*: 1.5M shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 372 ｜ +5,804 ｜ $5.30 ｜ 名义 $3.08M* ｜ +0.2%
P 352 ｜ +4,616 ｜ $0.83 ｜ 名义 $383.1k* ｜ -5.1%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：372（+0.2%） / 352（-5.1%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 70.6%｜历史 Rank 83%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,524,902 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-09 Forward Structure
存量OI:      C 58.7k / P 17.5k
今日变化ΔOI: C +16.9k / P +5.6k
平值价格ATM:  C 7.75 / P 9.47
隐含波动率 ATM IV:  43.9%
净 delta 敞口变化 ΔOI Δ Exposure*: 576k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 400 ｜ +2,763 ｜ $1.43 ｜ 名义 $395.1k* ｜ +7.6%
C 365 ｜ +2,167 ｜ $11.55 ｜ 名义 $2.50M* ｜ -1.8%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：400（+7.6%） / 365（-1.8%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 43.9%｜历史 Rank 83%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 576,409 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-11 Forward Structure
存量OI:      C 96.8k / P 75.6k
今日变化ΔOI: C +8.9k / P +8.8k
平值价格ATM:  C 9.60 / P 11.15
隐含波动率 ATM IV:  46.0%
净 delta 敞口变化 ΔOI Δ Exposure*: 249k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 400 ｜ +4,014 ｜ $2.38 ｜ 名义 $955.3k* ｜ +7.6%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：400（+7.6%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 46.0%｜历史 Rank 83%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 248,836 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-14 Forward Structure
存量OI:      C 4.9k / P 2.9k
今日变化ΔOI: C +1.4k / P +1.3k
平值价格ATM:  C 12.20 / P 10.20
隐含波动率 ATM IV:  42.9%
净 delta 敞口变化 ΔOI Δ Exposure*: 34k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 365 ｜ +481 ｜ $8.20 ｜ 名义 $394.4k* ｜ -1.8%
C 355 ｜ +340 ｜ $20.45 ｜ 名义 $695.3k* ｜ -4.5%
C 370 ｜ +143 ｜ $12.20 ｜ 名义 $174.5k* ｜ -0.4%
结构参考：365（-1.8%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 42.9%｜历史 Rank 83%（近端代理）｜净 delta 敞口 正 33,906 股（方向不可观测）——方向不可观测，观察点，非方向信号

📅 事件差分（观察，非因果）: 09-04（1D）ATM IV 70.6% vs 09-09 43.9%（差 +26.7pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-03/TSLA_morning.json