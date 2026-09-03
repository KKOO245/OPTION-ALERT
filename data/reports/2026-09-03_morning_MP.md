# 期权晨报 2026-09-03（快照 12:15 ET）

📊 市场环境

SPY $773.21 ｜ QQQ $717.30
VIX 14.69 ↓3.4%（5D +1.2%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 35.8（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 55.4 ｜ 前值 54.1　✅ 今日已公布
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 56 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **事件差分**: 09-04 ATM IV 72.3% vs 09-11 59.2%（差 +13.1pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 09-04 55C ΔOI -170（距现价 +1.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 54.70 → 今开 55.20（+0.9%） | 较昨收变动（含盘初走势） ｜ 今日高 55.63 ｜ 低 53.37

Options: P/C成交量 0.24 | OI比 0.79 | ATM IV 72.3% | Skew -5.0pp | Term 0.88 | ExpMove ±3.4%（近端） | Rank 57%
量化视角： IV 中性（Rank 57%）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜Put 保护异常便宜（Skew -5.0pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.79）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.24×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.79×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（1D）±3.4% ｜ 09-11（8D）±6.9% ｜ 09-18（15D）±10.4% ｜ 09-25（22D）±13.6%
   ⇒ IV–VIX Spread: +57.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,736,233 | GEX Change vs 上次快照 -960,529 | Flip: Primary Flip: 54.68（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 304 / LOW 73 / INVALID 117
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 54.68（全链重定价，覆盖 98%）
Put Wall 55（弱结构｜现价低于该位 1.9%）
最近结构参考: Flip 55（现价低于该位 1.3%）
量化视角： 负 Gamma（174万，无历史分位）｜负 Gamma 加深（96万）｜现价位于 Flip 下方 1.31%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 55（Put Wall，弱结构）；上方 55（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 55（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 55.0C — Vol 7 | 最新价 $1.98 | OI 119→645 (ΔOI +526张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增526张（+442.0% vs前日OI），连续性待观察（方向未知）
09-04 44.5P — Vol 2 | 最新价 $0.01 | OI 44→246 (ΔOI +202张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增202张（+459.1% vs前日OI），值得跟踪（方向未知）
09-04 56.0C — Vol 227 | 最新价 $0.42 | OI 523→674 (ΔOI +151张) | ΔOI/Volume 66.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增151张（+28.9% vs前日OI），连续性待观察（方向未知）
09-04 31.0P — Vol 0 | 最新价 $0.08 | OI 2→138 (ΔOI +136张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增136张（+6800.0% vs前日OI），值得跟踪（方向未知）
09-04 58.0C — Vol 7 | 最新价 $0.14 | OI 864→974 (ΔOI +110张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增110张（+12.7% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,125 张（Put 338 / Call 787），跨 2 个期限｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C +0.2k / P +0.7k ｜ Activity MEDIUM △ ｜ 1D
09-11  C +0.8k / P +44 ｜ Activity HIGH ｜ 8D
09-18  C +71 / P -0.2k ｜ Activity MEDIUM △ ｜ 15D
09-25  C +81 / P +19 ｜ Activity MEDIUM △ ｜ 22D

📆 09-04 Forward Structure
存量OI:      C 12.6k / P 9.9k
今日变化ΔOI: C +0.2k / P +0.7k
平值价格ATM:  C 0.95 / P 0.86
隐含波动率 ATM IV:  72.3%
净 delta 敞口变化 ΔOI Δ Exposure*: 823 shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 55 ｜ -170 ｜ $0.50 ｜ 名义 $-8.5k* ｜ +1.9%
C 56 ｜ +151 ｜ $0.26 ｜ 名义 $3.9k* ｜ +3.8%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：56（+3.8%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 72.3%｜历史 Rank 57%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 823 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-11 Forward Structure
存量OI:      C 4.4k / P 3.9k
今日变化ΔOI: C +0.8k / P +44
平值价格ATM:  C 1.98 / P 1.76
隐含波动率 ATM IV:  59.2%
净 delta 敞口变化 ΔOI Δ Exposure*: 27k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 55 ｜ +526 ｜ $1.60 ｜ 名义 $84.2k* ｜ +1.9%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：55（+1.9%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜ATM IV 59.2%｜历史 Rank 57%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 27,431 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（MEDIUM △）Top ΔOI: 50P -260 ｜ 52P +32

📅 事件差分（观察，非因果）: 09-04（1D）ATM IV 72.3% vs 09-11 59.2%（差 +13.1pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=10 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=10）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-03/MP_morning.json