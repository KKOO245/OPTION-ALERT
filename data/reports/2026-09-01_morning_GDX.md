# 期权晨报 2026-09-01（快照 10:20 ET）

📊 市场环境

SPY $763.56 ｜ QQQ $709.15
VIX 15.71 ↑5.3%（5D +1.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 46.4（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-01 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.3 ｜ 实际 7.271 ｜ 前值 7.182　✅ 今日已公布
- 周二 09-01 10:00　【高】ISM 制造业 PMI　预测 55.2 ｜ 实际 54.6 ｜ 前值 55.6　✅ 今日已公布
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 待公布 ｜ 前值 54.1
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 58 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🔴 **Vol Regime 升档**: LOW → NORMAL（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **单日价格波动**: -2.1%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 98.51 → 今开 95.15（-3.4%） | 较昨收变动（含盘初走势） ｜ 今日高 98.07 ｜ 低 94.58

Options: P/C成交量 0.53 | OI比 0.85 | ATM IV 50.6% | Skew -0.2pp | Term 0.87 | ExpMove ±3.9%（近端） | Rank 84%
量化视角： IV 历史高位（Rank 84%，期权偏贵）｜期限结构倒挂（Term 0.87，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.85）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.53×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.85×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-04（3D）±3.9% ｜ 09-11（10D）±5.7% ｜ 09-18（17D）±7.9% ｜ 09-25（24D）±8.7%
   ⇒ IV–VIX Spread: +34.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -25,158,522 | GEX Change vs 上次快照 -29,452,528 | Flip: Primary Flip: 98.28（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 451 / LOW 185 / INVALID 340
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 98.28（全链重定价，覆盖 98%）
最近结构参考: Flip 98（现价低于该位 1.9%）
量化视角： 负 Gamma（2516万，无历史分位）｜由正转负（2945万）｜现价位于 Flip 下方 1.85%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 98（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 90.0P — Vol 861 | 最新价 $1.22 | OI 38031→41924 (ΔOI +3893张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增3893张（+10.2% vs前日OI），值得跟踪（方向未知）
09-18 92.0P — Vol 1,329 | 最新价 $1.76 | OI 1911→5398 (ΔOI +3487张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3487张（+182.5% vs前日OI），连续性待观察（方向未知）
09-18 108.0C — Vol 8 | 最新价 $0.62 | OI 3058→6118 (ΔOI +3060张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3060张（+100.1% vs前日OI），连续性待观察（方向未知）
09-04 93.0P — Vol 393 | 最新价 $0.63 | OI 1214→4146 (ΔOI +2932张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2932张（+241.5% vs前日OI），连续性待观察（方向未知）
09-04 96.0P — Vol 392 | 最新价 $1.63 | OI 11210→12625 (ΔOI +1415张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增1415张（+12.6% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 14,787 张（Put 11,727 / Call 3,060），跨 2 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C +6.1k / P +5.8k ｜ Activity HIGH ｜ 3D
09-11  C +1.7k / P +2.6k ｜ Activity HIGH ｜ 10D
09-18  C +4.0k / P +8.5k ｜ Activity MEDIUM △ ｜ 17D
09-25  C +0.4k / P +0.4k ｜ Activity HIGH ｜ 24D

📆 09-04 Forward Structure
存量OI:      C 97.5k / P 82.4k
今日变化ΔOI: C +6.1k / P +5.8k
平值价格ATM:  C 2.12 / P 1.63
隐含波动率 ATM IV:  50.6%
净 delta 敞口变化 ΔOI Δ Exposure*: -47k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 93 ｜ +2,932 ｜ $0.63 ｜ 名义 $184.7k* ｜ -3.6%
P 96 ｜ +1,415 ｜ $1.63 ｜ 名义 $230.6k* ｜ -0.5%
C 106 ｜ +1,212 ｜ $0.05 ｜ 名义 $6.1k* ｜ +9.9%
结构参考：106（+9.9%） / 93（-3.6%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 50.6%｜历史 Rank 84%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 47,316 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-11 Forward Structure
存量OI:      C 15.9k / P 25.9k
今日变化ΔOI: C +1.7k / P +2.6k
平值价格ATM:  C 2.80 / P 2.72
隐含波动率 ATM IV:  43.1%
净 delta 敞口变化 ΔOI Δ Exposure*: -12k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 90 ｜ +1,141 ｜ $0.75 ｜ 名义 $85.6k* ｜ -6.7%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：90（-6.7%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜ATM IV 43.1%｜历史 Rank 84%（近端代理）｜净 delta 敞口 负 11,836 股（方向不可观测）——方向不可观测，观察点，非方向信号

   Top ΔOI: 90P +3,893 ｜ 92P +3,487

📆 09-25 Forward Structure
存量OI:      C 5.6k / P 6.5k
今日变化ΔOI: C +0.4k / P +0.4k
平值价格ATM:  C 4.42 / P 4.00
隐含波动率 ATM IV:  43.6%
净 delta 敞口变化 ΔOI Δ Exposure*: -3k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 93 ｜ +512 ｜ $2.94 ｜ 名义 $150.5k* ｜ -3.6%
P 95 ｜ -120 ｜ $3.50 ｜ 名义 $-42.0k* ｜ -1.5%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：93（-3.6%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 43.6%｜历史 Rank 84%（近端代理）｜净 delta 敞口 负 2,593 股（方向不可观测）——方向不可观测，观察点，非方向信号

📅 事件差分（观察，非因果）: 09-04（3D）ATM IV 50.6% vs 09-11 43.1%（差 +7.4pp）——覆盖 职位空缺(JOLTS) Job Openings、ISM 制造业 PMI 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=4 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=4）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-01/GDX_morning.json