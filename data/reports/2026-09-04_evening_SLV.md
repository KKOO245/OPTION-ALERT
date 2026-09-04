# 期权晚报 2026-09-04（快照 16:40 ET）

📊 市场环境

SPY $770.19 ｜ QQQ $718.96
VIX 14.53 ↑1.5%（5D +0.7%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 41.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 56 ｜ 实际 162 ｜ 前值 21　✅ 今日已公布
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 4.1 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 09-09 60P ΔOI +2,272（距现价 +1.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 59.15 → 收盘 59.82（+1.1%） ｜ 今日高 59.97 ｜ 低 59.13
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-09-11，窗口结束前不做对错判定）

Options: P/C成交量 0.63 | OI比 0.52 | ATM IV 58.7% | Skew -19.9pp | Term 0.70 | ExpMove ±2.6%（近端） | Rank 89%
量化视角： IV 历史高位（Rank 89%，期权偏贵）｜期限结构倒挂（Term 0.70，近月 IV 高于远月）｜Put 保护异常便宜（Skew -19.9pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.52）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.63×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.52×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-09（5D）±2.6% ｜ 09-11（7D）±3.8% ｜ 09-14（10D）±4.3% ｜ 09-16（12D）±5.2%
   ⇒ IV–VIX Spread: +44.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 97,377,480 | GEX Change vs 上次快照 -20,133,075 | Flip: Primary Flip: 55.17（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 986 / LOW 170 / INVALID 394
结构观察区: Primary Flip 55.17（全链重定价，覆盖 91%）
最近结构参考: Flip 55（现价高于该位 8.4%）
量化视角： 正 Gamma（9738万，无历史分位）｜正 Gamma 减弱（2013万）｜现价位于 Flip 上方 8.42%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 55（全链重定价，覆盖 91%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 68.0C — Vol 70 | 最新价 $0.25 | OI 3472→8525 (ΔOI +5053张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5053张（+145.5% vs前日OI），连续性待观察（方向未知）
09-18 67.5C — Vol 32 | 最新价 $0.27 | OI 2666→6373 (ΔOI +3707张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3707张（+139.1% vs前日OI），连续性待观察（方向未知）
09-30 70.0C — Vol 159 | 最新价 $0.46 | OI 27065→29682 (ΔOI +2617张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增2617张（+9.7% vs前日OI），值得跟踪（方向未知）
09-04 58.0P — Vol 1,313 | 最新价 $0.01 | OI 2227→4681 (ΔOI +2454张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2454张（+110.2% vs前日OI），连续性待观察（方向未知）
09-09 60.5P — Vol 792 | 最新价 $1.18 | OI 304→2576 (ΔOI +2272张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2272张（+747.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 16,103 张（Put 4,726 / Call 11,377），跨 4 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜彩票/名义 1 档（价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-09  C +4.1k / P +3.6k ｜ Activity HIGH ｜ 5D
09-11  C +5.2k / P +1.3k ｜ Activity HIGH ｜ 7D
09-14  C +0.5k / P +0.3k ｜ Activity HIGH ｜ 10D
09-16  C +0.5k / P +0.5k ｜ Activity HIGH ｜ 12D

📆 09-09 Forward Structure
存量OI:      C 15.5k / P 12.5k
今日变化ΔOI: C +4.1k / P +3.6k
平值价格ATM:  C 0.68 / P 0.87
隐含波动率 ATM IV:  28.0%
净 delta 敞口变化 ΔOI Δ Exposure*: -103k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 60 ｜ +2,272 ｜ $1.18 ｜ 名义 $268.1k* ｜ +1.1%
C 62 ｜ +552 ｜ $0.15 ｜ 名义 $8.3k* ｜ +4.5%
C 64 ｜ +462 ｜ $0.07 ｜ 名义 $3.2k* ｜ +7.0%
结构参考：60（+1.1%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 28.0%｜历史 Rank 89%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 负 103,196 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-11 Forward Structure
存量OI:      C 63.5k / P 22.1k
今日变化ΔOI: C +5.2k / P +1.3k
平值价格ATM:  C 1.08 / P 1.19
隐含波动率 ATM IV:  35.2%
净 delta 敞口变化 ΔOI Δ Exposure*: 57k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 62 ｜ +1,185 ｜ $0.45 ｜ 名义 $53.3k* ｜ +3.6%
C 61 ｜ +850 ｜ $0.69 ｜ 名义 $58.6k* ｜ +2.0%
C 60 ｜ +845 ｜ $1.08 ｜ 名义 $91.3k* ｜ +0.3%
结构参考：62（+3.6%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 35.2%｜历史 Rank 89%（近端代理）｜净 delta 敞口 正 57,126 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-14 Forward Structure
存量OI:      C 1.8k / P 1.4k
今日变化ΔOI: C +0.5k / P +0.3k
平值价格ATM:  C 1.22 / P 1.35
隐含波动率 ATM IV:  32.9%
净 delta 敞口变化 ΔOI Δ Exposure*: 7k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 61 ｜ +215 ｜ $0.84 ｜ 名义 $18.1k* ｜ +2.0%
P 58 ｜ +97 ｜ $0.54 ｜ 名义 $5.2k* ｜ -3.0%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：61（+2.0%） / 58（-3.0%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 32.9%｜历史 Rank 89%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 6,655 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-16 Forward Structure
存量OI:      C 1.5k / P 1.0k
今日变化ΔOI: C +0.5k / P +0.5k
平值价格ATM:  C 1.50 / P 1.64
隐含波动率 ATM IV:  36.7%
净 delta 敞口变化 ΔOI Δ Exposure*: -2k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 59 ｜ +212 ｜ $1.22 ｜ 名义 $25.9k* ｜ -1.4%
P 58 ｜ +201 ｜ $0.82 ｜ 名义 $16.5k* ｜ -3.0%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：59（-1.4%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 36.7%｜历史 Rank 89%（近端代理）｜净 delta 敞口 负 1,655 股（方向不可观测）——方向不可观测，观察点，非方向信号

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-04/SLV_evening.json