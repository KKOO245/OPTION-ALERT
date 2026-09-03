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
🟡 **事件差分**: 09-04 ATM IV 49.4% vs 09-09 36.1%（差 +13.3pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 09-04 61C ΔOI +1,997（距现价 +0.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 60.02 → 收盘 60.55（+0.9%） ｜ 今日高 60.95 ｜ 低 59.60
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-09-10，窗口结束前不做对错判定）

Options: P/C成交量 0.68 | OI比 0.51 | ATM IV 49.4% | Skew -5.2pp | Term 0.91 | ExpMove ±2.1%（近端） | Rank 82%
量化视角： IV 历史高位（Rank 82%，期权偏贵）｜期限结构正常（Term 0.91）｜Put 保护异常便宜（Skew -5.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.51）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.68×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.51×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（1D）±2.1% ｜ 09-09（6D）±3.7% ｜ 09-11（8D）±4.8% ｜ 09-14（11D）±5.4%
   ⇒ IV–VIX Spread: +35.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 139,099,060 | GEX Change vs 上次快照 379,141 | Flip: Primary Flip: 56.00（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1062 / LOW 174 / INVALID 314
结构观察区: Primary Flip 56.00（全链重定价，覆盖 99%）
最近结构参考: Flip 56（现价高于该位 8.1%）
量化视角： 正 Gamma（1.39亿，无历史分位）｜正 Gamma 增强（+38万）｜现价位于 Flip 上方 8.12%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 56（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-30 52.5P — Vol 19 | 最新价 $0.40 | OI 1194→5981 (ΔOI +4787张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4787张（+400.9% vs前日OI），连续性待观察（方向未知）
10-02 68.0C — Vol 123 | 最新价 $1.05 | OI 54→4200 (ΔOI +4146张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4146张（+7677.8% vs前日OI），连续性待观察（方向未知）
10-02 66.0C — Vol 115 | 最新价 $1.40 | OI 119→4229 (ΔOI +4110张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4110张（+3453.8% vs前日OI），连续性待观察（方向未知）
09-04 61.0C — Vol 6,185 | 最新价 $0.45 | OI 10428→12425 (ΔOI +1997张) | ΔOI/Volume 32.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1997张（+19.1% vs前日OI），连续性待观察（方向未知）
09-18 64.0C — Vol 936 | 最新价 $0.99 | OI 6896→8235 (ΔOI +1339张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增1339张（+19.4% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 16,379 张（Put 4,787 / Call 11,592），跨 4 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C +5.0k / P +0.6k ｜ Activity HIGH ｜ 1D
09-09  C +1.4k / P +1.0k ｜ Activity HIGH ｜ 6D
09-11  C +3.5k / P +0.4k ｜ Activity HIGH ｜ 8D
09-14  C +0.3k / P +0.2k ｜ Activity HIGH ｜ 11D

📆 09-04 Forward Structure
存量OI:      C 100.3k / P 51.6k
今日变化ΔOI: C +5.0k / P +0.6k
平值价格ATM:  C 0.66 / P 0.61
隐含波动率 ATM IV:  49.4%
净 delta 敞口变化 ΔOI Δ Exposure*: 324k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 61 ｜ +1,997 ｜ $0.45 ｜ 名义 $89.9k* ｜ +0.7%
P 57 ｜ -1,977 ｜ $0.03 ｜ 名义 $-5.9k* ｜ -5.9%
P 58 ｜ +1,018 ｜ $0.06 ｜ 名义 $6.1k* ｜ -4.2%
结构参考：61（+0.7%） / 58（-4.2%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 49.4%｜历史 Rank 82%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 324,226 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-09 Forward Structure
存量OI:      C 11.4k / P 9.0k
今日变化ΔOI: C +1.4k / P +1.0k
平值价格ATM:  C 1.19 / P 1.07
隐含波动率 ATM IV:  36.1%
净 delta 敞口变化 ΔOI Δ Exposure*: 45k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 62 ｜ +559 ｜ $0.46 ｜ 名义 $25.7k* ｜ +3.2%
C 59 ｜ +322 ｜ $2.05 ｜ 名义 $66.0k* ｜ -2.6%
P 55 ｜ +266 ｜ $0.05 ｜ 名义 $1.3k* ｜ -9.2%
结构参考：62（+3.2%） / 59（-2.6%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 36.1%｜历史 Rank 82%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 44,600 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-11 Forward Structure
存量OI:      C 58.4k / P 20.8k
今日变化ΔOI: C +3.5k / P +0.4k
平值价格ATM:  C 1.51 / P 1.38
隐含波动率 ATM IV:  40.4%
净 delta 敞口变化 ΔOI Δ Exposure*: 90k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 60 ｜ -1,202 ｜ $1.75 ｜ 名义 $-210.3k* ｜ -0.9%
C 65 ｜ +1,141 ｜ $0.34 ｜ 名义 $38.8k* ｜ +7.3%
C 64 ｜ +1,129 ｜ $0.40 ｜ 名义 $45.2k* ｜ +6.5%
结构参考：65（+7.3%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 40.4%｜历史 Rank 82%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 89,561 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-14 Forward Structure
存量OI:      C 1.2k / P 1.0k
今日变化ΔOI: C +0.3k / P +0.2k
平值价格ATM:  C 1.45 / P 1.80
隐含波动率 ATM IV:  38.1%
净 delta 敞口变化 ΔOI Δ Exposure*: 12k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 64 ｜ +102 ｜ $0.55 ｜ 名义 $5.6k* ｜ +5.7%
C 58 ｜ +55 ｜ $3.14 ｜ 名义 $17.3k* ｜ -4.2%
P 59 ｜ +55 ｜ $0.83 ｜ 名义 $4.6k* ｜ -2.6%
结构参考：64（+5.7%） / 58（-4.2%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜ATM IV 38.1%｜历史 Rank 82%（近端代理）｜净 delta 敞口 正 11,787 股（方向不可观测）——方向不可观测，观察点，非方向信号

📅 事件差分（观察，非因果）: 09-04（1D）ATM IV 49.4% vs 09-09 36.1%（差 +13.3pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-03/SLV_evening.json