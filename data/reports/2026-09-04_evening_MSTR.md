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
🟡 **近现价集中开仓**: 09-11 145C ΔOI +15,957（距现价 +1.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 137.22 → 收盘 142.80（+4.1%） ｜ 今日高 144.40 ｜ 低 137.07
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.52 | OI比 1.04 | ATM IV 65.1% | Skew -10.4pp | Term 1.12 | ExpMove ±7.8%（近端） | Rank 20%
量化视角： IV 历史低位（Rank 20%，期权偏便宜）｜期限结构正常（Term 1.12）｜Put 保护异常便宜（Skew -10.4pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.52×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.04×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-11（7D）±7.8% ｜ 09-18（14D）±11.5% ｜ 09-25（21D）±14.2% ｜ 10-02（28D）±16.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 85,375,244 | GEX Change vs 上次快照 -15,339,013 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 87%（带内） ｜ IV 有效性: VALID 838 / LOW 123 / INVALID 371
结构观察区: NO_CROSS
量化视角： 正 Gamma（8538万，无历史分位）｜正 Gamma 减弱（1534万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 145.0C — Vol 13,460 | 最新价 $4.75 | OI 1589→17546 (ΔOI +15957张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15957张（+1004.2% vs前日OI），连续性待观察（方向未知）
09-11 152.5C — Vol 9,223 | 最新价 $2.55 | OI 211→13965 (ΔOI +13754张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13754张（+6518.5% vs前日OI），连续性待观察（方向未知）
09-11 147.0C — Vol 6,177 | 最新价 $4.00 | OI 70→13633 (ΔOI +13563张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13563张（+19375.7% vs前日OI），连续性待观察（方向未知）
09-04 135.0P — Vol 13,335 | 最新价 $0.03 | OI 1178→13145 (ΔOI +11967张) | ΔOI/Volume 89.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11967张（+1015.9% vs前日OI），连续性待观察（方向未知）
09-11 150.0C — Vol 19,791 | 最新价 $3.10 | OI 2334→12012 (ΔOI +9678张) | ΔOI/Volume 48.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9678张（+414.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 64,919 张（Put 11,967 / Call 52,952），跨 2 个期限｜彩票/名义 1 档（价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +111.4k / P +33.2k ｜ Activity HIGH ｜ 7D
09-18  C -3.2k / P +5.7k ｜ Activity HIGH ｜ 14D
09-25  C +69 / P +2.9k ｜ Activity HIGH ｜ 21D
10-02  C +3.8k / P +2.5k ｜ Activity HIGH ｜ 28D

📆 09-11 Forward Structure
存量OI:      C 156.9k / P 110.0k
今日变化ΔOI: C +111.4k / P +33.2k
平值价格ATM:  C 5.45 / P 5.72
隐含波动率 ATM IV:  70.8%
净 delta 敞口变化 ΔOI Δ Exposure*: 3.9M shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 145 ｜ +15,957 ｜ $4.75 ｜ 名义 $7.58M* ｜ +1.5%
C 152 ｜ +13,754 ｜ $2.55 ｜ 名义 $3.51M* ｜ +6.8%
C 147 ｜ +13,563 ｜ $4.00 ｜ 名义 $5.43M* ｜ +2.9%
结构参考：145（+1.5%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 70.8%｜历史 Rank 20%（近端代理）｜净 delta 敞口 正 3,945,881 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 266.1k / P 193.5k
今日变化ΔOI: C -3.2k / P +5.7k
平值价格ATM:  C 7.20 / P 9.20
隐含波动率 ATM IV:  73.5%
净 delta 敞口变化 ΔOI Δ Exposure*: -281k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 160 ｜ -787 ｜ $3.25 ｜ 名义 $-255.8k* ｜ +12.0%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 73.5%｜历史 Rank 20%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 280,677 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-25 Forward Structure
存量OI:      C 17.1k / P 27.8k
今日变化ΔOI: C +69 / P +2.9k
平值价格ATM:  C 10.15 / P 10.06
隐含波动率 ATM IV:  72.7%
净 delta 敞口变化 ΔOI Δ Exposure*: -107k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 133 ｜ -973 ｜ $14.64 ｜ 名义 $-1.42M* ｜ -6.9%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜ATM IV 72.7%｜历史 Rank 20%（近端代理）｜净 delta 敞口 负 107,447 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 10-02 Forward Structure
存量OI:      C 15.6k / P 21.0k
今日变化ΔOI: C +3.8k / P +2.5k
平值价格ATM:  C 12.05 / P 11.30
隐含波动率 ATM IV:  72.9%
净 delta 敞口变化 ΔOI Δ Exposure*: 28k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 180 ｜ +1,967 ｜ $3.05 ｜ 名义 $599.9k* ｜ +26.1%
C 230 ｜ +1,060 ｜ $0.70 ｜ 名义 $74.2k* ｜ +61.1%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：180（+26.1%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 72.9%｜历史 Rank 20%（近端代理）｜净 delta 敞口 正 27,956 股（方向不可观测）——方向不可观测，观察点，非方向信号

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-04/MSTR_evening.json