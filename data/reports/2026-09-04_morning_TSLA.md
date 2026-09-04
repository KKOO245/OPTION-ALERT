# 期权晨报 2026-09-04（快照 10:52 ET）

📊 市场环境

SPY $769.49 ｜ QQQ $718.96
VIX 14.12 ↓1.4%（5D -2.1%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 41.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 56 ｜ 实际 162 ｜ 前值 21　✅ 今日已公布
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 4.1 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **单日价格波动**: -5.9%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-09 360P ΔOI +12,815（距现价 +1.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 376.36 → 今开 362.18（-3.8%） | 较昨收变动（含盘初走势） ｜ 今日高 364.69 ｜ 低 352.42

Options: P/C成交量 1.10 | OI比 0.95 | ATM IV 67.3% | Skew -7.8pp | Term 0.59 | ExpMove ±3.4%（近端） | Rank 81%
量化视角： IV 历史高位（Rank 81%，期权偏贵）｜期限结构倒挂（Term 0.59，近月 IV 高于远月）｜Put 保护异常便宜（Skew -7.8pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.10×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.95×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-09（5D）±3.4% ｜ 09-11（7D）±4.3% ｜ 09-14（10D）±4.8% ｜ 09-16（12D）±5.5%
   ⇒ IV–VIX Spread: +53.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 3,071,340 | GEX Change vs 上次快照 -176,303,727 | Flip: Primary Flip: 353.52（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 1130 / LOW 141 / INVALID 507
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 353.52（全链重定价，覆盖 97%）
Put Wall 360（弱结构｜现价低于该位 1.7%）
最近结构参考: Flip 354（现价高于该位 0.1%）
量化视角： 正 Gamma（307万，无历史分位）｜正 Gamma 减弱（1.76亿）｜现价位于 Flip 上方 0.15%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 360（Put Wall，弱结构）；上方 362（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 354（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-09 360.0P — Vol 8,980 | 最新价 $7.45 | OI 348→13163 (ΔOI +12815张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12815张（+3682.5% vs前日OI），连续性待观察（方向未知）
09-09 400.0C — Vol 12,217 | 最新价 $0.22 | OI 7750→18850 (ΔOI +11100张) | ΔOI/Volume 90.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11100张（+143.2% vs前日OI），连续性待观察（方向未知）
09-04 400.0C — Vol 11,451 | 最新价 $0.02 | OI 18760→28420 (ΔOI +9660张) | ΔOI/Volume 84.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9660张（+51.5% vs前日OI），连续性待观察（方向未知）
09-04 365.0P — Vol 12,519 | 最新价 $8.60 | OI 2070→10903 (ΔOI +8833张) | ΔOI/Volume 70.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8833张（+426.7% vs前日OI），连续性待观察（方向未知）
09-04 370.0P — Vol 11,605 | 最新价 $13.20 | OI 2486→11235 (ΔOI +8749张) | ΔOI/Volume 75.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8749张（+351.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 51,157 张（Put 30,397 / Call 20,760），跨 2 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $29M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-09  C +25.5k / P +32.6k ｜ Activity HIGH ｜ 5D
09-11  C +20.8k / P +32.7k ｜ Activity HIGH ｜ 7D
09-14  C +2.9k / P +2.5k ｜ Activity HIGH ｜ 10D
09-16  C +1.1k / P +1.5k ｜ Activity HIGH ｜ 12D

📆 09-09 Forward Structure
存量OI:      C 84.1k / P 50.0k
今日变化ΔOI: C +25.5k / P +32.6k
平值价格ATM:  C 5.19 / P 6.70
隐含波动率 ATM IV:  34.7%
净 delta 敞口变化 ΔOI Δ Exposure*: -1.9M shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 360 ｜ +12,815 ｜ $9.88 ｜ 名义 $12.66M* ｜ +1.7%
C 400 ｜ +11,100 ｜ $0.18 ｜ 名义 $199.8k* ｜ +13.0%
P 310 ｜ +5,073 ｜ $0.10 ｜ 名义 $50.7k* ｜ -12.4%
结构参考：360（+1.7%） / 310（-12.4%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 34.7%｜历史 Rank 81%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 负 1,855,399 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-11 Forward Structure
存量OI:      C 117.6k / P 108.3k
今日变化ΔOI: C +20.8k / P +32.7k
平值价格ATM:  C 7.00 / P 8.37
隐含波动率 ATM IV:  38.3%
净 delta 敞口变化 ΔOI Δ Exposure*: -1.5M shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 407 ｜ +6,284 ｜ $0.31 ｜ 名义 $194.8k* ｜ +15.1%
C 392 ｜ +5,928 ｜ $0.58 ｜ 名义 $343.8k* ｜ +10.9%
C 400 ｜ -4,636 ｜ $0.39 ｜ 名义 $-180.8k* ｜ +13.0%
结构参考：407（+15.1%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 38.3%｜历史 Rank 81%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,508,608 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-14 Forward Structure
存量OI:      C 7.8k / P 5.4k
今日变化ΔOI: C +2.9k / P +2.5k
平值价格ATM:  C 7.90 / P 9.15
隐含波动率 ATM IV:  35.7%
净 delta 敞口变化 ΔOI Δ Exposure*: -137k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 370 ｜ +619 ｜ $18.89 ｜ 名义 $1.17M* ｜ +4.5%
C 380 ｜ +482 ｜ $1.73 ｜ 名义 $83.4k* ｜ +7.3%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：370（+4.5%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 35.7%｜历史 Rank 81%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 负 136,527 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-16 Forward Structure
存量OI:      C 3.7k / P 2.4k
今日变化ΔOI: C +1.1k / P +1.5k
平值价格ATM:  C 9.40 / P 10.20
隐含波动率 ATM IV:  37.9%
净 delta 敞口变化 ΔOI Δ Exposure*: -76k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 360 ｜ +522 ｜ $13.10 ｜ 名义 $683.8k* ｜ +1.7%
P 370 ｜ +170 ｜ $19.75 ｜ 名义 $335.8k* ｜ +4.5%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：360（+1.7%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 37.9%｜历史 Rank 81%（近端代理）｜净 delta 敞口 负 75,880 股（方向不可观测）——方向不可观测，观察点，非方向信号

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=11 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=11）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-04/TSLA_morning.json