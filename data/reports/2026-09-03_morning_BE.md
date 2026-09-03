# 期权晨报 2026-09-03（快照 10:16 ET）

📊 市场环境

SPY $768.41 ｜ QQQ $712.45
VIX 15.00 ↓1.3%（5D -1.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 55.4 ｜ 前值 54.1　✅ 今日已公布
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 58 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **事件差分**: 09-04（1D）ATM IV 145.5% vs 09-11 90.1%（差 +55.5pp），覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 09-04 220C ΔOI +952（距现价 +0.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 217.28 → 今开 219.00（+0.8%） | 较昨收变动（含盘初走势） ｜ 今日高 224.80 ｜ 低 212.12

Options: P/C成交量 1.19 | OI比 1.03 | ATM IV 145.5% | Skew -13.4pp | Term 0.58 | ExpMove ±6.8%（近端） | Rank 90%
量化视角： IV 历史高位（Rank 90%，期权偏贵）｜期限结构倒挂（Term 0.58，近月 IV 高于远月）｜Put 保护异常便宜（Skew -13.4pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 1.19）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.19×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.03×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-04（1D）±6.8% ｜ 09-11（8D）±10.9% ｜ 09-18（15D）±14.4% ｜ 09-25（22D）±16.0%
   ⇒ IV–VIX Spread: +130.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 14,578,729 | GEX Change vs 上次快照 4,585,368 | Flip: Primary Flip: 204.89（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 575 / LOW 82 / INVALID 141
结构观察区: Primary Flip 204.89（全链重定价，覆盖 100%）
最近结构参考: Flip 205（现价高于该位 6.8%）
量化视角： 正 Gamma（1458万，无历史分位）｜正 Gamma 增强（+459万）｜现价位于 Flip 上方 6.82%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 205（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 220.0C — Vol 194 | 最新价 $11.15 | OI 712→1826 (ΔOI +1114张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1114张（+156.5% vs前日OI），连续性待观察（方向未知）
09-04 182.5P — Vol 82 | 最新价 $0.15 | OI 2373→3470 (ΔOI +1097张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1097张（+46.2% vs前日OI），连续性待观察（方向未知）
09-04 230.0C — Vol 856 | 最新价 $3.36 | OI 2459→3512 (ΔOI +1053张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1053张（+42.8% vs前日OI），连续性待观察（方向未知）
09-18 270.0C — Vol 12 | 最新价 $3.20 | OI 3294→4298 (ΔOI +1004张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1004张（+30.5% vs前日OI），连续性待观察（方向未知）
09-04 220.0C — Vol 807 | 最新价 $6.25 | OI 2449→3401 (ΔOI +952张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增952张（+38.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,220 张（Put 1,097 / Call 4,123），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C +6.8k / P +3.3k ｜ Activity HIGH ｜ 1D
09-11  C +2.8k / P +2.1k ｜ Activity MEDIUM △ ｜ 8D
09-18  C +2.5k / P +1.8k ｜ Activity MEDIUM △ ｜ 15D
09-25  C +0.3k / P +0.6k ｜ Activity MEDIUM △ ｜ 22D

📆 09-04 Forward Structure
存量OI:      C 47.9k / P 49.5k
今日变化ΔOI: C +6.8k / P +3.3k
平值价格ATM:  C 6.25 / P 8.55
隐含波动率 ATM IV:  145.5%
净 delta 敞口变化 ΔOI Δ Exposure*: 186k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 230 ｜ +1,053 ｜ $3.36 ｜ 名义 $353.8k* ｜ +5.1%
C 220 ｜ +952 ｜ $6.25 ｜ 名义 $595.0k* ｜ +0.5%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：230（+5.1%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 145.5%｜历史 Rank 90%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 186,123 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-11（MEDIUM △）Top ΔOI: 220C +1,114 ｜ 250C +529

09-18（MEDIUM △）Top ΔOI: 270C +1,004 ｜ 180P +821

09-25（MEDIUM △）Top ΔOI: 250C +130

📅 事件差分（观察，非因果）: 09-04（1D）ATM IV 145.5% vs 09-11 90.1%（差 +55.5pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-03/BE_morning.json