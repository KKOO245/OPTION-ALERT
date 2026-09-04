# 期权晚报 2026-09-04（快照 17:18 ET）

📊 市场环境

SPY $770.19 ｜ QQQ $718.96
VIX 14.53 ↑1.5%（5D +0.7%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 41.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 56 ｜ 实际 162 ｜ 前值 21　✅ 今日已公布
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 4.1 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 137.22 → 收盘 142.80（+4.1%） ｜ 今日高 144.40 ｜ 低 137.07 ｜ 昨收 144.82 → 收盘 142.80（-1.4%）
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
• 支撑/压力参考：下方 130（MaxPain，仅结算参考）。
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

09-11  C +0 / P +0 ｜ Activity LOW ｜ 7D
09-18  C +0 / P +0 ｜ Activity LOW ｜ 14D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 21D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 28D

📆 09-11 Forward Structure
存量OI:      C 156.9k / P 110.0k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 5.45 / P 5.72
隐含波动率 ATM IV:  70.8%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 130（结算参考） ｜ Call Wall 145（+1.5%，弱）（OI 17.5k）
量化解读： 存量 Call 重｜ATM IV 70.8%｜历史 Rank 20%（近端代理）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（Activity LOW）仓位参考: Max Pain 105（结算参考）

09-25（Activity LOW）仓位参考: Max Pain 125（结算参考） ｜ Call Wall 140（-2.0%，弱）（OI 1.4k）

10-02（Activity LOW）仓位参考: Max Pain 125（结算参考）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-04/MSTR_evening.json