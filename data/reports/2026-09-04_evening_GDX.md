# 期权晚报 2026-09-04（快照 16:40 ET）

📊 市场环境

SPY $770.19 ｜ QQQ $718.96
VIX 14.53 ↑1.5%（5D +0.7%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 41.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 56 ｜ 实际 162 ｜ 前值 21　✅ 今日已公布
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 4.1 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 09-11 102C ΔOI +5,300（距现价 +2.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 98.75 → 收盘 99.26（+0.5%） ｜ 今日高 100.10 ｜ 低 98.02
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-09-11，窗口结束前不做对错判定）

Options: P/C成交量 0.86 | OI比 0.98 | ATM IV 71.0% | Skew -4.0pp | Term 0.61 | ExpMove ±4.5%（近端） | Rank 98%
量化视角： IV 历史高位（Rank 98%，期权偏贵）｜期限结构倒挂（Term 0.61，近月 IV 高于远月）｜Put 保护异常便宜（Skew -4.0pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.86×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.98×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-11（7D）±4.5% ｜ 09-18（14D）±6.9% ｜ 09-25（21D）±8.2% ｜ 10-02（28D）±9.6%
   ⇒ IV–VIX Spread: +56.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 6,784,921 | GEX Change vs 上次快照 -14,988,154 | Flip: Primary Flip: 98.57（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 87%（带内） ｜ IV 有效性: VALID 519 / LOW 160 / INVALID 299
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 98.57（全链重定价，覆盖 87%）
Call Wall 100（弱结构｜现价低于该位 0.7%）
最近结构参考: Flip 99（现价高于该位 0.7%）
量化视角： 正 Gamma（678万，无历史分位）｜正 Gamma 减弱（1499万）｜现价位于 Flip 上方 0.70%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 99（全链重定价，覆盖 87%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 102.0C — Vol 9,329 | 最新价 $1.16 | OI 213→5513 (ΔOI +5300张) | ΔOI/Volume 56.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5300张（+2488.3% vs前日OI），连续性待观察（方向未知）
09-11 106.0C — Vol 7,885 | 最新价 $0.39 | OI 146→5226 (ΔOI +5080张) | ΔOI/Volume 64.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5080张（+3479.4% vs前日OI），连续性待观察（方向未知）
09-18 80.0P — Vol 21 | 最新价 $0.09 | OI 66246→71131 (ΔOI +4885张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增4885张（+7.4% vs前日OI），值得跟踪（方向未知）
09-04 98.0P — Vol 14,430 | 最新价 $0.01 | OI 3276→7510 (ΔOI +4234张) | ΔOI/Volume 29.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4234张（+129.2% vs前日OI），连续性待观察（方向未知）
09-18 95.0P — Vol 3,272 | 最新价 $1.55 | OI 11067→14922 (ΔOI +3855张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3855张（+34.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 23,354 张（Put 12,974 / Call 10,380），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +14.1k / P +0.5k ｜ Activity HIGH ｜ 7D
09-18  C +3.4k / P +11.5k ｜ Activity HIGH ｜ 14D
09-25  C +0.4k / P +0.5k ｜ Activity HIGH ｜ 21D
10-02  C +0.1k / P +0.6k ｜ Activity MEDIUM △ ｜ 28D

📆 09-11 Forward Structure
存量OI:      C 49.0k / P 36.0k
今日变化ΔOI: C +14.1k / P +0.5k
平值价格ATM:  C 2.39 / P 2.10
隐含波动率 ATM IV:  40.8%
净 delta 敞口变化 ΔOI Δ Exposure*: 234k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 102 ｜ +5,300 ｜ $1.16 ｜ 名义 $614.8k* ｜ +2.8%
C 106 ｜ +5,080 ｜ $0.39 ｜ 名义 $198.1k* ｜ +6.8%
C 107 ｜ +3,036 ｜ $0.27 ｜ 名义 $82.0k* ｜ +7.8%
结构参考：102（+2.8%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 40.8%｜历史 Rank 98%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 233,720 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 245.8k / P 411.9k
今日变化ΔOI: C +3.4k / P +11.5k
平值价格ATM:  C 3.70 / P 3.13
隐含波动率 ATM IV:  43.4%
净 delta 敞口变化 ΔOI Δ Exposure*: -163k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 95 ｜ +3,855 ｜ $1.55 ｜ 名义 $597.5k* ｜ -4.3%
C 110 ｜ +3,173 ｜ $0.60 ｜ 名义 $190.4k* ｜ +10.8%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：110（+10.8%） / 95（-4.3%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜ATM IV 43.4%｜历史 Rank 98%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 163,030 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-25 Forward Structure
存量OI:      C 6.5k / P 7.3k
今日变化ΔOI: C +0.4k / P +0.5k
平值价格ATM:  C 4.38 / P 3.75
隐含波动率 ATM IV:  44.0%
净 delta 敞口变化 ΔOI Δ Exposure*: 2k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 102 ｜ +125 ｜ $3.27 ｜ 名义 $40.9k* ｜ +2.8%
P 95 ｜ +112 ｜ $2.15 ｜ 名义 $24.1k* ｜ -4.3%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：102（+2.8%） / 95（-4.3%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜ATM IV 44.0%｜历史 Rank 98%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,348 股（方向不可观测）——方向不可观测，观察点，非方向信号

10-02（MEDIUM △）Top ΔOI: 90P +97 ｜ 99P +94

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location near_call_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-04/GDX_evening.json