# 期权晨报 2026-09-04（快照 10:52 ET）

📊 市场环境

SPY $771.00 ｜ QQQ $717.87
VIX 14.12 ↓1.4%（5D -2.1%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 41.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 56 ｜ 实际 162 ｜ 前值 21　✅ 今日已公布
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 4.1 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览
🟡 **单日价格波动**: -2.9%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-11 145C ΔOI +15,957（距现价 +3.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 144.82 → 今开 137.22（-5.2%） | 较昨收变动（含盘初走势） ｜ 今日高 141.12 ｜ 低 137.07

Options: P/C成交量 0.62 | OI比 1.04 | ATM IV 102.0% | Skew -9.9pp | Term 0.71 | ExpMove ±7.8%（近端） | Rank 80%
量化视角： IV 历史高位（Rank 80%，期权偏贵）｜期限结构倒挂（Term 0.71，近月 IV 高于远月）｜Put 保护异常便宜（Skew -9.9pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.62×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.04×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-11（7D）±7.8% ｜ 09-18（14D）±11.1% ｜ 09-25（21D）±13.3% ｜ 10-02（28D）±15.9%
   ⇒ IV–VIX Spread: +87.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 100,714,257 | GEX Change vs 上次快照 4,100,848 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 919 / LOW 145 / INVALID 268
结构观察区: NO_CROSS
量化视角： 正 Gamma（1.01亿，无历史分位）｜正 Gamma 增强（+410万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 145.0C — Vol 1,136 | 最新价 $4.05 | OI 1589→17546 (ΔOI +15957张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15957张（+1004.2% vs前日OI），连续性待观察（方向未知）
09-11 152.5C — Vol 464 | 最新价 $2.22 | OI 211→13965 (ΔOI +13754张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13754张（+6518.5% vs前日OI），连续性待观察（方向未知）
09-11 147.0C — Vol 55 | 最新价 $3.32 | OI 70→13633 (ΔOI +13563张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13563张（+19375.7% vs前日OI），连续性待观察（方向未知）
09-04 135.0P — Vol 5,737 | 最新价 $0.19 | OI 1178→13145 (ΔOI +11967张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11967张（+1015.9% vs前日OI），连续性待观察（方向未知）
09-11 150.0C — Vol 1,060 | 最新价 $2.67 | OI 2334→12012 (ΔOI +9678张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9678张（+414.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 64,919 张（Put 11,967 / Call 52,952），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +111.4k / P +33.2k ｜ Activity HIGH ｜ 7D
09-18  C -3.2k / P +5.7k ｜ Activity HIGH ｜ 14D
09-25  C +69 / P +2.9k ｜ Activity MEDIUM △ ｜ 21D
10-02  C +3.8k / P +2.5k ｜ Activity HIGH ｜ 28D

📆 09-11 Forward Structure
存量OI:      C 156.9k / P 110.0k
今日变化ΔOI: C +111.4k / P +33.2k
平值价格ATM:  C 5.18 / P 5.85
隐含波动率 ATM IV:  68.8%
净 delta 敞口变化 ΔOI Δ Exposure*: 3.2M shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 145 ｜ +15,957 ｜ $3.70 ｜ 名义 $5.90M* ｜ +3.1%
C 152 ｜ +13,754 ｜ $1.98 ｜ 名义 $2.72M* ｜ +8.5%
C 147 ｜ +13,563 ｜ $3.10 ｜ 名义 $4.20M* ｜ +4.5%
结构参考：145（+3.1%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 68.8%｜历史 Rank 80%（近端代理）｜净 delta 敞口 正 3,177,899 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 266.1k / P 193.5k
今日变化ΔOI: C -3.2k / P +5.7k
平值价格ATM:  C 8.20 / P 7.45
隐含波动率 ATM IV:  70.7%
净 delta 敞口变化 ΔOI Δ Exposure*: -276k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 160 ｜ -787 ｜ $2.61 ｜ 名义 $-205.4k* ｜ +13.8%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 70.7%｜历史 Rank 80%（近端代理）｜净 delta 敞口 负 275,987 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-25（MEDIUM △）Top ΔOI: 133C -973

📆 10-02 Forward Structure
存量OI:      C 15.6k / P 21.0k
今日变化ΔOI: C +3.8k / P +2.5k
平值价格ATM:  C 10.60 / P 11.81
隐含波动率 ATM IV:  72.1%
净 delta 敞口变化 ΔOI Δ Exposure*: 17k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 180 ｜ +1,967 ｜ $2.45 ｜ 名义 $481.9k* ｜ +28.0%
C 230 ｜ +1,060 ｜ $0.53 ｜ 名义 $56.2k* ｜ +63.6%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：180（+28.0%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 72.1%｜历史 Rank 80%（近端代理）｜净 delta 敞口 正 16,650 股（方向不可观测）——方向不可观测，观察点，非方向信号

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location ? | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-04/MSTR_morning.json