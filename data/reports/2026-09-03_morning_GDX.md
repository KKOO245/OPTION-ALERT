# 期权晨报 2026-09-03（快照 11:17 ET）

📊 市场环境

SPY $769.44 ｜ QQQ $716.22
VIX 14.85 ↓2.3%（5D -2.4%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 35.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 55.4 ｜ 前值 54.1　✅ 今日已公布
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 56 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **单日价格波动**: +3.0%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **事件差分**: 09-04 ATM IV 55.6% vs 09-11 43.7%（差 +11.9pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 97.63 → 今开 100.68（+3.1%） | 较昨收变动（含盘初走势） ｜ 今日高 101.06 ｜ 低 99.07

Options: P/C成交量 0.66 | OI比 0.93 | ATM IV 55.6% | Skew 2.1pp | Term 0.80 | ExpMove ±2.9%（近端） | Rank 90%
量化视角： IV 历史高位（Rank 90%，期权偏贵）｜期限结构倒挂（Term 0.80，近月 IV 高于远月）｜保护溢价中性（Skew 2.1pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.66×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.93×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-04（1D）±2.9% ｜ 09-11（8D）±7.0% ｜ 09-18（15D）±7.8% ｜ 09-25（22D）±8.8%
   ⇒ IV–VIX Spread: +40.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 46,951,502 | GEX Change vs 上次快照 69,617,684 | Flip: Primary Flip: 98.80（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 423 / LOW 190 / INVALID 365
结构观察区: Primary Flip 98.80（全链重定价，覆盖 96%）
Call Wall 100（弱结构｜现价高于该位 0.6%）
最近结构参考: Call Wall 100（现价高于该位 0.6%）
量化视角： 正 Gamma（4695万，无历史分位）｜由负转正（+6962万）｜现价位于 Flip 上方 1.82%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 99（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 103.0C — Vol 83 | 最新价 $1.33 | OI 424→5437 (ΔOI +5013张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5013张（+1182.3% vs前日OI），连续性待观察（方向未知）
09-11 99.0C — Vol 101 | 最新价 $2.94 | OI 2154→7090 (ΔOI +4936张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4936张（+229.2% vs前日OI），连续性待观察（方向未知）
09-04 95.0P — Vol 260 | 最新价 $0.09 | OI 5432→9171 (ΔOI +3739张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3739张（+68.8% vs前日OI），连续性待观察（方向未知）
09-18 93.0P — Vol 32 | 最新价 $1.25 | OI 4340→7141 (ΔOI +2801张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2801张（+64.5% vs前日OI），连续性待观察（方向未知）
10-02 110.0C — Vol 9 | 最新价 $1.80 | OI 506→3032 (ΔOI +2526张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2526张（+499.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 19,015 张（Put 6,540 / Call 12,475），跨 4 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C +0.2k / P +4.5k ｜ Activity HIGH ｜ 1D
09-11  C +14.8k / P -0.8k ｜ Activity HIGH ｜ 8D
09-18  C +1.0k / P +0.8k ｜ Activity MEDIUM △ ｜ 15D
09-25  C -0.3k / P +49 ｜ Activity MEDIUM △ ｜ 22D

📆 09-04 Forward Structure
存量OI:      C 95.3k / P 88.9k
今日变化ΔOI: C +0.2k / P +4.5k
平值价格ATM:  C 1.18 / P 1.78
隐含波动率 ATM IV:  55.6%
净 delta 敞口变化 ΔOI Δ Exposure*: 282k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 95 ｜ +3,739 ｜ $0.06 ｜ 名义 $22.4k* ｜ -5.6%
P 97 ｜ +2,318 ｜ $0.22 ｜ 名义 $51.0k* ｜ -3.6%
C 106 ｜ -2,054 ｜ $0.08 ｜ 名义 $-16.4k* ｜ +5.4%
结构参考：95（-5.6%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 55.6%｜历史 Rank 90%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 281,506 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-11 Forward Structure
存量OI:      C 34.9k / P 35.5k
今日变化ΔOI: C +14.8k / P -0.8k
平值价格ATM:  C 2.19 / P 4.90
隐含波动率 ATM IV:  43.7%
净 delta 敞口变化 ΔOI Δ Exposure*: 731k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 103 ｜ +5,013 ｜ $1.68 ｜ 名义 $842.2k* ｜ +2.4%
C 99 ｜ +4,936 ｜ $3.10 ｜ 名义 $1.53M* ｜ -1.6%
C 98 ｜ +1,908 ｜ $4.00 ｜ 名义 $763.2k* ｜ -2.6%
结构参考：103（+2.4%） / 99（-1.6%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 43.7%｜历史 Rank 90%（近端代理）｜净 delta 敞口 正 730,778 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（MEDIUM △）Top ΔOI: 93P +2,801 ｜ 89P -1,521

09-25（MEDIUM △）Top ΔOI: 110C -446 ｜ 105C +121

📅 事件差分（观察，非因果）: 09-04（1D）ATM IV 55.6% vs 09-11 43.7%（差 +11.9pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-03/GDX_morning.json