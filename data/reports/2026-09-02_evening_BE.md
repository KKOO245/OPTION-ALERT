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
🔴 **事件差分**: 09-04（2D）ATM IV 121.8% vs 09-11 90.1%（差 +31.7pp），覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **单日价格波动**: +3.8%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-04 220C ΔOI +659（距现价 +1.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 210.00 → 收盘 217.28（+3.5%） ｜ 今日高 217.30 ｜ 低 204.30
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-09-09，窗口结束前不做对错判定）

Options: P/C成交量 0.78 | OI比 1.12 | ATM IV 121.8% | Skew -9.9pp | Term 0.68 | ExpMove ±7.2%（近端） | Rank 78%
量化视角： IV 历史高位（Rank 78%，期权偏贵）｜期限结构倒挂（Term 0.68，近月 IV 高于远月）｜Put 保护异常便宜（Skew -9.9pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.78×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.12×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-04（2D）±7.2% ｜ 09-11（9D）±11.4% ｜ 09-18（16D）±14.8% ｜ 09-25（23D）±17.3%
   ⇒ IV–VIX Spread: +106.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 9,993,361 | GEX Change vs 上次快照 9,424,353 | Flip: Primary Flip: 205.47（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 545 / LOW 73 / INVALID 180
结构观察区: Primary Flip 205.47（全链重定价，覆盖 100%）
最近结构参考: Flip 205（现价高于该位 5.8%）
量化视角： 正 Gamma（999万，无历史分位）｜正 Gamma 增强（+942万）｜现价位于 Flip 上方 5.75%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 205（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 125.0P — Vol 71 | 最新价 $0.09 | OI 34→2543 (ΔOI +2509张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2509张（+7379.4% vs前日OI），连续性待观察（方向未知）
09-04 220.0C — Vol 2,338 | 最新价 $6.70 | OI 1790→2449 (ΔOI +659张) | ΔOI/Volume 28.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增659张（+36.8% vs前日OI），连续性待观察（方向未知）
09-04 237.5C — Vol 1,769 | 最新价 $2.05 | OI 302→954 (ΔOI +652张) | ΔOI/Volume 36.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增652张（+215.9% vs前日OI），连续性待观察（方向未知）
09-04 210.0C — Vol 2,392 | 最新价 $11.70 | OI 1588→2192 (ΔOI +604张) | ΔOI/Volume 25.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增604张（+38.0% vs前日OI），连续性待观察（方向未知）
09-04 190.0P — Vol 1,171 | 最新价 $0.45 | OI 3105→3671 (ΔOI +566张) | ΔOI/Volume 48.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增566张（+18.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,990 张（Put 3,075 / Call 1,915），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C +3.6k / P +2.4k ｜ Activity HIGH ｜ 2D
09-11  C +2.1k / P +3.8k ｜ Activity HIGH ｜ 9D
09-18  C +0.3k / P +1.4k ｜ Activity HIGH ｜ 16D
09-25  C +0.2k / P +1.1k ｜ Activity HIGH ｜ 23D

📆 09-04 Forward Structure
存量OI:      C 41.2k / P 46.2k
今日变化ΔOI: C +3.6k / P +2.4k
平值价格ATM:  C 7.70 / P 7.95
隐含波动率 ATM IV:  121.8%
净 delta 敞口变化 ΔOI Δ Exposure*: 155k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 220 ｜ +659 ｜ $6.70 ｜ 名义 $441.5k* ｜ +1.3%
C 237 ｜ +652 ｜ $2.05 ｜ 名义 $133.7k* ｜ +9.3%
C 210 ｜ +604 ｜ $11.70 ｜ 名义 $706.7k* ｜ -3.4%
结构参考：220（+1.3%） / 210（-3.4%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 121.8%｜历史 Rank 78%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 155,484 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-11 Forward Structure
存量OI:      C 16.5k / P 18.5k
今日变化ΔOI: C +2.1k / P +3.8k
平值价格ATM:  C 12.16 / P 12.70
隐含波动率 ATM IV:  90.1%
净 delta 敞口变化 ΔOI Δ Exposure*: 67k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 260 ｜ +312 ｜ $1.95 ｜ 名义 $60.8k* ｜ +19.7%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：260（+19.7%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜ATM IV 90.1%｜历史 Rank 78%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 67,205 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 116.1k / P 95.9k
今日变化ΔOI: C +0.3k / P +1.4k
平值价格ATM:  C 15.55 / P 16.52
隐含波动率 ATM IV:  85.3%
净 delta 敞口变化 ΔOI Δ Exposure*: -15k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 280 ｜ +493 ｜ $2.12 ｜ 名义 $104.5k* ｜ +28.9%
C 250 ｜ -356 ｜ $5.80 ｜ 名义 $-206.5k* ｜ +15.1%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：280（+28.9%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 85.3%｜历史 Rank 78%（近端代理）｜净 delta 敞口 负 14,745 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-25 Forward Structure
存量OI:      C 7.8k / P 8.1k
今日变化ΔOI: C +0.2k / P +1.1k
平值价格ATM:  C 19.50 / P 18.14
隐含波动率 ATM IV:  85.6%
净 delta 敞口变化 ΔOI Δ Exposure*: -2k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 215 ｜ +88 ｜ $18.14 ｜ 名义 $159.6k* ｜ -1.0%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：215（-1.0%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜ATM IV 85.6%｜历史 Rank 78%（近端代理）｜净 delta 敞口 负 1,848 股（方向不可观测）——方向不可观测，观察点，非方向信号

📅 事件差分（观察，非因果）: 09-04（2D）ATM IV 121.8% vs 09-11 90.1%（差 +31.7pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-02/BE_evening.json