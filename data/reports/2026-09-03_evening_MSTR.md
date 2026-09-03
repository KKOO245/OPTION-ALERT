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
🔴 **事件差分**: 09-04（1D）ATM IV 104.7% vs 09-11 80.2%（差 +24.4pp），覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **单日价格波动**: +9.7%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-04 146C ΔOI -14,575（距现价 +0.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 128.04 → 收盘 144.82（+13.1%） ｜ 今日高 144.92 ｜ 低 127.59
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-09-10，窗口结束前不做对错判定）

Options: P/C成交量 0.62 | OI比 0.74 | ATM IV 104.7% | Skew -8.5pp | Term 0.73 | ExpMove ±4.3%（近端） | Rank 83%
量化视角： IV 历史高位（Rank 83%，期权偏贵）｜期限结构倒挂（Term 0.73，近月 IV 高于远月）｜Put 保护异常便宜（Skew -8.5pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.74）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.62×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.74×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（1D）±4.3% ｜ 09-11（8D）±9.4% ｜ 09-18（15D）±12.8% ｜ 09-25（22D）±15.2%
   ⇒ IV–VIX Spread: +90.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 96,613,410 | GEX Change vs 上次快照 -22,752,515 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 871 / LOW 142 / INVALID 319
结构观察区: NO_CROSS
量化视角： 正 Gamma（9661万，无历史分位）｜正 Gamma 减弱（2275万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 150.0C — Vol 28,368 | 最新价 $1.49 | OI 6749→9056 (ΔOI +2307张) | ΔOI/Volume 8.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2307张（+34.2% vs前日OI），连续性待观察（方向未知）
09-11 123.0C — Vol 205 | 最新价 $20.85 | OI 128→2090 (ΔOI +1962张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1962张（+1532.8% vs前日OI），连续性待观察（方向未知）
09-04 125.0C — Vol 2,191 | 最新价 $19.90 | OI 2272→3727 (ΔOI +1455张) | ΔOI/Volume 66.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1455张（+64.0% vs前日OI），连续性待观察（方向未知）
09-04 130.0C — Vol 11,207 | 最新价 $15.00 | OI 11841→13204 (ΔOI +1363张) | ΔOI/Volume 12.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1363张（+11.5% vs前日OI），连续性待观察（方向未知）
09-04 126.0C — Vol 2,314 | 最新价 $18.73 | OI 1565→2810 (ΔOI +1245张) | ΔOI/Volume 53.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1245张（+79.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 8,332 张（Put 0 / Call 8,332），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C -21.1k / P -0.4k ｜ Activity HIGH ｜ 1D
09-11  C +6.4k / P +2.6k ｜ Activity MEDIUM △ ｜ 8D
09-18  C +1.6k / P +0.9k ｜ Activity MEDIUM △ ｜ 15D
09-25  C +0.5k / P +1.7k ｜ Activity HIGH ｜ 22D

📆 09-04 Forward Structure
存量OI:      C 239.3k / P 177.6k
今日变化ΔOI: C -21.1k / P -0.4k
平值价格ATM:  C 3.10 / P 3.20
隐含波动率 ATM IV:  104.7%
净 delta 敞口变化 ΔOI Δ Exposure*: -1.0M shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 146 ｜ -14,575 ｜ $2.63 ｜ 名义 $-3.83M* ｜ +0.8%
C 140 ｜ -11,638 ｜ $6.10 ｜ 名义 $-7.10M* ｜ -3.3%
C 147 ｜ -2,721 ｜ $2.30 ｜ 名义 $-625.8k* ｜ +1.5%
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 104.7%｜历史 Rank 83%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,008,743 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-11（MEDIUM △）Top ΔOI: 123C +1,962 ｜ 170C +860

09-18（MEDIUM △）Top ΔOI: 170C +314

📆 09-25 Forward Structure
存量OI:      C 17.0k / P 24.9k
今日变化ΔOI: C +0.5k / P +1.7k
平值价格ATM:  C 11.00 / P 11.00
隐含波动率 ATM IV:  77.0%
净 delta 敞口变化 ΔOI Δ Exposure*: 29k shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜ATM IV 77.0%｜历史 Rank 83%（近端代理）｜净 delta 敞口 正 29,132 股（方向不可观测）——方向不可观测，观察点，非方向信号

📅 事件差分（观察，非因果）: 09-04（1D）ATM IV 104.7% vs 09-11 80.2%（差 +24.4pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location ? | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-03/MSTR_evening.json