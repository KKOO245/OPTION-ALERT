# 期权晨报 2026-09-02（快照 11:19 ET）

📊 市场环境

SPY $764.45 ｜ QQQ $709.24
VIX 15.51 ↓5.1%（5D +0.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 待公布 ｜ 前值 54.1
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 58 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **单日价格波动**: +3.0%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-04 93P ΔOI +4,863（距现价 -4.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 94.67 → 今开 96.96（+2.4%） | 较昨收变动（含盘初走势） ｜ 今日高 98.76 ｜ 低 96.77

Options: P/C成交量 0.49 | OI比 0.89 | ATM IV 51.6% | Skew 3.4pp | Term 0.88 | ExpMove ±3.3%（近端） | Rank 86%
量化视角： IV 历史高位（Rank 86%，期权偏贵）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜保护溢价中性（Skew 3.4pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.49×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.89×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-04（2D）±3.3% ｜ 09-11（9D）±5.7% ｜ 09-18（16D）±7.8% ｜ 09-25（23D）±9.0%
   ⇒ IV–VIX Spread: +36.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -15,531,689 | GEX Change vs 上次快照 22,268,542 | Flip: Primary Flip: 98.34（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 581 / LOW 165 / INVALID 230
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 98.34（全链重定价，覆盖 99%）
Call Wall 100（弱结构｜现价低于该位 2.5%）
最近结构参考: Flip 98（现价低于该位 0.9%）
量化视角： 负 Gamma（1553万，无历史分位）｜负 Gamma 缓解（+2227万）｜现价位于 Flip 下方 0.88%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 98（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 93.0P — Vol 213 | 最新价 $0.29 | OI 4146→9009 (ΔOI +4863张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4863张（+117.3% vs前日OI），连续性待观察（方向未知）
09-11 90.0P — Vol 2,136 | 最新价 $0.48 | OI 2202→7043 (ΔOI +4841张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4841张（+219.8% vs前日OI），连续性待观察（方向未知）
09-04 103.0C — Vol 354 | 最新价 $0.21 | OI 1020→4632 (ΔOI +3612张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3612张（+354.1% vs前日OI），连续性待观察（方向未知）
09-11 100.0C — Vol 121 | 最新价 $1.73 | OI 587→4135 (ΔOI +3548张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3548张（+604.4% vs前日OI），连续性待观察（方向未知）
09-18 85.0P — Vol 100 | 最新价 $0.36 | OI 29012→31842 (ΔOI +2830张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增2830张（+9.8% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 19,694 张（Put 12,534 / Call 7,160），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C -2.4k / P +2.0k ｜ Activity HIGH ｜ 2D
09-11  C +4.2k / P +10.5k ｜ Activity HIGH ｜ 9D
09-18  C -3.9k / P +0.4k ｜ Activity MEDIUM △ ｜ 16D
09-25  C +0.7k / P +0.3k ｜ Activity HIGH ｜ 23D

📆 09-04 Forward Structure
存量OI:      C 95.1k / P 84.4k
今日变化ΔOI: C -2.4k / P +2.0k
平值价格ATM:  C 1.90 / P 1.30
隐含波动率 ATM IV:  51.6%
净 delta 敞口变化 ΔOI Δ Exposure*: 410k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 93 ｜ +4,863 ｜ $0.26 ｜ 名义 $126.4k* ｜ -4.6%
C 104 ｜ -4,351 ｜ $0.12 ｜ 名义 $-52.2k* ｜ +6.7%
C 103 ｜ +3,612 ｜ $0.18 ｜ 名义 $65.0k* ｜ +5.7%
结构参考：103（+5.7%） / 93（-4.6%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 51.6%｜历史 Rank 86%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 409,537 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-11 Forward Structure
存量OI:      C 20.1k / P 36.3k
今日变化ΔOI: C +4.2k / P +10.5k
平值价格ATM:  C 3.02 / P 2.51
隐含波动率 ATM IV:  44.8%
净 delta 敞口变化 ΔOI Δ Exposure*: -7k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 90 ｜ +4,841 ｜ $0.50 ｜ 名义 $242.1k* ｜ -7.7%
C 100 ｜ +3,548 ｜ $1.74 ｜ 名义 $617.4k* ｜ +2.6%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：100（+2.6%） / 90（-7.7%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜ATM IV 44.8%｜历史 Rank 86%（近端代理）｜净 delta 敞口 负 7,499 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（MEDIUM △）Top ΔOI: 110C -5,338 ｜ 85P +2,830

📆 09-25 Forward Structure
存量OI:      C 6.3k / P 6.7k
今日变化ΔOI: C +0.7k / P +0.3k
平值价格ATM:  C 4.60 / P 4.15
隐含波动率 ATM IV:  45.0%
净 delta 敞口变化 ΔOI Δ Exposure*: 10k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 110 ｜ +499 ｜ $1.06 ｜ 名义 $52.9k* ｜ +12.8%
P 92 ｜ +157 ｜ $2.05 ｜ 名义 $32.2k* ｜ -5.6%
C 105 ｜ +121 ｜ $2.04 ｜ 名义 $24.7k* ｜ +7.7%
结构参考：110（+12.8%） / 92（-5.6%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 45.0%｜历史 Rank 86%（近端代理）｜净 delta 敞口 正 9,940 股（方向不可观测）——方向不可观测，观察点，非方向信号

📅 事件差分（观察，非因果）: 09-04（2D）ATM IV 51.6% vs 09-11 44.8%（差 +6.8pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-02/GDX_morning.json