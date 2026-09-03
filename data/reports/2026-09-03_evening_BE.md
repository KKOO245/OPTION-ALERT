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
🔴 **事件差分**: 09-04（1D）ATM IV 162.9% vs 09-11 94.8%（差 +68.1pp），覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **单日价格波动**: +7.6%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-04 230C ΔOI +1,053（距现价 -2.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 219.00 → 收盘 235.55（+7.6%） ｜ 今日高 238.41 ｜ 低 212.12
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-09-10，窗口结束前不做对错判定）

Options: P/C成交量 0.81 | OI比 1.03 | ATM IV 162.9% | Skew -18.6pp | Term 0.52 | ExpMove ±6.9%（近端） | Rank 94%
量化视角： IV 历史高位（Rank 94%，期权偏贵）｜期限结构倒挂（Term 0.52，近月 IV 高于远月）｜Put 保护异常便宜（Skew -18.6pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.81×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.03×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-04（1D）±6.9% ｜ 09-11（8D）±11.2% ｜ 09-18（15D）±14.4% ｜ 09-25（22D）±16.9%
   ⇒ IV–VIX Spread: +148.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 21,845,346 | GEX Change vs 上次快照 339,449 | Flip: Primary Flip: 205.56（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 562 / LOW 71 / INVALID 165
结构观察区: Primary Flip 205.56（全链重定价，覆盖 100%）
Call Wall 250（现价低于该位 5.8%）
最近结构参考: Call Wall 250（现价低于该位 5.8%）
量化视角： 正 Gamma（2185万，无历史分位）｜正 Gamma 增强（+34万）｜现价位于 Flip 上方 14.59%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 206（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 220.0C — Vol 962 | 最新价 $21.28 | OI 712→1826 (ΔOI +1114张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1114张（+156.5% vs前日OI），连续性待观察（方向未知）
09-04 182.5P — Vol 318 | 最新价 $0.12 | OI 2373→3470 (ΔOI +1097张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1097张（+46.2% vs前日OI），连续性待观察（方向未知）
09-04 230.0C — Vol 4,562 | 最新价 $10.80 | OI 2459→3512 (ΔOI +1053张) | ΔOI/Volume 23.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1053张（+42.8% vs前日OI），连续性待观察（方向未知）
09-18 270.0C — Vol 1,203 | 最新价 $6.45 | OI 3294→4298 (ΔOI +1004张) | ΔOI/Volume 83.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1004张（+30.5% vs前日OI），连续性待观察（方向未知）
09-04 220.0C — Vol 2,213 | 最新价 $17.40 | OI 2449→3401 (ΔOI +952张) | ΔOI/Volume 43.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增952张（+38.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,220 张（Put 1,097 / Call 4,123），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C +6.8k / P +3.3k ｜ Activity HIGH ｜ 1D
09-11  C +2.8k / P +2.1k ｜ Activity HIGH ｜ 8D
09-18  C +2.5k / P +1.8k ｜ Activity MEDIUM △ ｜ 15D
09-25  C +0.3k / P +0.6k ｜ Activity HIGH ｜ 22D

📆 09-04 Forward Structure
存量OI:      C 47.9k / P 49.5k
今日变化ΔOI: C +6.8k / P +3.3k
平值价格ATM:  C 8.42 / P 7.80
隐含波动率 ATM IV:  162.9%
净 delta 敞口变化 ΔOI Δ Exposure*: 404k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 230 ｜ +1,053 ｜ $10.80 ｜ 名义 $1.14M* ｜ -2.4%
C 220 ｜ +952 ｜ $17.40 ｜ 名义 $1.66M* ｜ -6.6%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：230（-2.4%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 162.9%｜历史 Rank 94%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 403,695 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-11 Forward Structure
存量OI:      C 19.4k / P 20.7k
今日变化ΔOI: C +2.8k / P +2.1k
平值价格ATM:  C 13.50 / P 12.80
隐含波动率 ATM IV:  94.8%
净 delta 敞口变化 ΔOI Δ Exposure*: 144k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 220 ｜ +1,114 ｜ $21.28 ｜ 名义 $2.37M* ｜ -6.6%
C 250 ｜ +529 ｜ $7.95 ｜ 名义 $420.6k* ｜ +6.1%
C 230 ｜ +321 ｜ $16.03 ｜ 名义 $514.6k* ｜ -2.4%
结构参考：250（+6.1%） / 220（-6.6%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 94.8%｜历史 Rank 94%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 144,171 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（MEDIUM △）Top ΔOI: 270C +1,004 ｜ 180P +821

📆 09-25 Forward Structure
存量OI:      C 8.1k / P 8.7k
今日变化ΔOI: C +0.3k / P +0.6k
平值价格ATM:  C 20.30 / P 19.39
隐含波动率 ATM IV:  85.9%
净 delta 敞口变化 ΔOI Δ Exposure*: 8k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 250 ｜ +130 ｜ $14.37 ｜ 名义 $186.8k* ｜ +6.1%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：250（+6.1%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜ATM IV 85.9%｜历史 Rank 94%（近端代理）｜净 delta 敞口 正 7,663 股（方向不可观测）——方向不可观测，观察点，非方向信号

📅 事件差分（观察，非因果）: 09-04（1D）ATM IV 162.9% vs 09-11 94.8%（差 +68.1pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-03/BE_evening.json