# 期权晚报 2026-09-02（快照 17:13 ET）

📊 市场环境

SPY $765.16 ｜ QQQ $709.24
VIX 15.20 ↓7.0%（5D -1.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 待公布 ｜ 前值 54.1
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 58 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **近现价集中开仓**: 09-04 93P ΔOI +4,863（距现价 -4.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 96.96 → 收盘 97.63（+0.7%） ｜ 今日高 98.76 ｜ 低 96.30
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-09-09，窗口结束前不做对错判定）

Options: P/C成交量 0.42 | OI比 0.89 | ATM IV 48.2% | Skew 2.8pp | Term 0.93 | ExpMove ±2.9%（近端） | Rank 79%
量化视角： IV 历史高位（Rank 79%，期权偏贵）｜期限结构正常（Term 0.93）｜保护溢价中性（Skew 2.8pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.42×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.89×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-04（2D）±2.9% ｜ 09-11（9D）±5.4% ｜ 09-18（16D）±7.6% ｜ 09-25（23D）±9.9%
   ⇒ IV–VIX Spread: +33.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -22,666,182 | GEX Change vs 上次快照 -7,134,493 | Flip: Primary Flip: 98.69（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 446 / LOW 182 / INVALID 348
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 98.69（全链重定价，覆盖 96%）
Call Wall 100（弱结构｜现价低于该位 2.4%）
最近结构参考: Flip 99（现价低于该位 1.1%）
量化视角： 负 Gamma（2267万，无历史分位）｜负 Gamma 加深（713万）｜现价位于 Flip 下方 1.07%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 99（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 93.0P — Vol 1,561 | 最新价 $0.13 | OI 4146→9009 (ΔOI +4863张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4863张（+117.3% vs前日OI），连续性待观察（方向未知）
09-11 90.0P — Vol 2,511 | 最新价 $0.39 | OI 2202→7043 (ΔOI +4841张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4841张（+219.8% vs前日OI），连续性待观察（方向未知）
09-04 103.0C — Vol 440 | 最新价 $0.05 | OI 1020→4632 (ΔOI +3612张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3612张（+354.1% vs前日OI），连续性待观察（方向未知）
09-11 100.0C — Vol 539 | 最新价 $1.69 | OI 587→4135 (ΔOI +3548张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3548张（+604.4% vs前日OI），连续性待观察（方向未知）
09-18 85.0P — Vol 1,612 | 最新价 $0.32 | OI 29012→31842 (ΔOI +2830张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增2830张（+9.8% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 19,694 张（Put 12,534 / Call 7,160），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C -2.4k / P +2.0k ｜ Activity MEDIUM △ ｜ 2D
09-11  C +4.2k / P +10.5k ｜ Activity HIGH ｜ 9D
09-18  C -3.9k / P +0.4k ｜ Activity HIGH ｜ 16D
09-25  C +0.7k / P +0.3k ｜ Activity HIGH ｜ 23D

📆 09-04 Forward Structure
存量OI:      C 95.1k / P 84.4k
今日变化ΔOI: C -2.4k / P +2.0k
平值价格ATM:  C 1.19 / P 1.64
隐含波动率 ATM IV:  48.2%
净 delta 敞口变化 ΔOI Δ Exposure*: 447k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 93 ｜ +4,863 ｜ $0.13 ｜ 名义 $63.2k* ｜ -4.7%
C 104 ｜ -4,351 ｜ $0.04 ｜ 名义 $-17.4k* ｜ +6.5%
C 103 ｜ +3,612 ｜ $0.05 ｜ 名义 $18.1k* ｜ +5.5%
结构参考：103（+5.5%） / 93（-4.7%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 48.2%｜历史 Rank 79%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 446,908 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-11 Forward Structure
存量OI:      C 20.1k / P 36.3k
今日变化ΔOI: C +4.2k / P +10.5k
平值价格ATM:  C 2.10 / P 3.15
隐含波动率 ATM IV:  43.1%
净 delta 敞口变化 ΔOI Δ Exposure*: 5k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 90 ｜ +4,841 ｜ $0.39 ｜ 名义 $188.8k* ｜ -7.8%
C 100 ｜ +3,548 ｜ $1.69 ｜ 名义 $599.6k* ｜ +2.4%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：100（+2.4%） / 90（-7.8%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜ATM IV 43.1%｜历史 Rank 79%（近端代理）｜净 delta 敞口 正 5,304 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 241.5k / P 399.5k
今日变化ΔOI: C -3.9k / P +0.4k
平值价格ATM:  C 3.48 / P 3.94
隐含波动率 ATM IV:  44.4%
净 delta 敞口变化 ΔOI Δ Exposure*: 123k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 110 ｜ -5,338 ｜ $0.48 ｜ 名义 $-256.2k* ｜ +12.7%
P 85 ｜ +2,830 ｜ $0.32 ｜ 名义 $90.6k* ｜ -12.9%
P 90 ｜ -1,705 ｜ $0.92 ｜ 名义 $-156.9k* ｜ -7.8%
结构参考：85（-12.9%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜ATM IV 44.4%｜历史 Rank 79%（近端代理）｜净 delta 敞口 正 123,268 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-25 Forward Structure
存量OI:      C 6.3k / P 6.7k
今日变化ΔOI: C +0.7k / P +0.3k
平值价格ATM:  C 3.86 / P 5.81
隐含波动率 ATM IV:  45.2%
净 delta 敞口变化 ΔOI Δ Exposure*: 10k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 92 ｜ +157 ｜ $2.21 ｜ 名义 $34.7k* ｜ -5.8%
C 105 ｜ +121 ｜ $1.86 ｜ 名义 $22.5k* ｜ +7.5%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：105（+7.5%） / 92（-5.8%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 45.2%｜历史 Rank 79%（近端代理）｜净 delta 敞口 正 9,601 股（方向不可观测）——方向不可观测，观察点，非方向信号

📅 事件差分（观察，非因果）: 09-04（2D）ATM IV 48.2% vs 09-11 43.1%（差 +5.0pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-02/GDX_evening.json