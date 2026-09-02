# 期权晚报 2026-09-02（快照 18:14 ET）

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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 218.79 → 收盘 224.41（+2.6%） ｜ 今日高 227.95 ｜ 低 218.48
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-09-09，窗口结束前不做对错判定）

Options: P/C成交量 0.66 | OI比 0.85 | ATM IV 62.2% | Skew -0.5pp | Term 0.52 | ExpMove ±2.1%（近端） | Rank 86%
量化视角： IV 历史高位（Rank 86%，期权偏贵）｜期限结构倒挂（Term 0.52，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.5pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.85）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.66×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.85×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-04（2D）±2.1% ｜ 09-09（7D）±3.2% ｜ 09-11（9D）±4.0% ｜ 09-14（12D）±4.3%
   ⇒ IV–VIX Spread: +47.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 568,717,428 | GEX Change vs 上次快照 -42,643,460 | Flip: Primary Flip: 212.11（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 641 / LOW 186 / INVALID 441
结构观察区: Primary Flip 212.11（全链重定价，覆盖 94%）
Call Wall 230（弱结构｜现价低于该位 2.4%）
最近结构参考: Call Wall 230（现价低于该位 2.4%）
量化视角： 正 Gamma（5.69亿，无历史分位）｜正 Gamma 减弱（4264万）｜现价位于 Flip 上方 5.80%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 212（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-02 222.5C — Vol 259,605 | 最新价 $1.81 | OI 11639→26057 (ΔOI +14418张) | ΔOI/Volume 5.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14418张（+123.9% vs前日OI），连续性待观察（方向未知）
09-02 220.0C — Vol 138,074 | 最新价 $4.35 | OI 15105→29039 (ΔOI +13934张) | ΔOI/Volume 10.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13934张（+92.2% vs前日OI），连续性待观察（方向未知）
09-04 220.0C — Vol 51,531 | 最新价 $5.40 | OI 27491→37743 (ΔOI +10252张) | ΔOI/Volume 19.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10252张（+37.3% vs前日OI），连续性待观察（方向未知）
09-04 222.5C — Vol 56,860 | 最新价 $3.54 | OI 26888→35759 (ΔOI +8871张) | ΔOI/Volume 15.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8871张（+33.0% vs前日OI），连续性待观察（方向未知）
09-04 225.0C — Vol 130,734 | 最新价 $2.13 | OI 38603→46403 (ΔOI +7800张) | ΔOI/Volume 6.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7800张（+20.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 55,275 张（Put 0 / Call 55,275），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-09  C +0 / P +0 ｜ Activity LOW ｜ 7D
09-11  C +0 / P +0 ｜ Activity LOW ｜ 9D
09-14  C +0 / P +0 ｜ Activity LOW ｜ 12D

📆 09-04 Forward Structure
存量OI:      C 566.5k / P 416.7k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 2.13 / P 2.70
隐含波动率 ATM IV:  35.7%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 35.7%｜历史 Rank 86%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

📅 事件差分（观察，非因果）: 09-04（2D）ATM IV 35.7% vs 09-09 28.9%（差 +6.9pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-02/NVDA_evening.json