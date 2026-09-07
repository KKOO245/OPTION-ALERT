# 期权晚报 2026-09-07（快照 19:08 ET）

📊 市场环境

SPY $770.19 ｜ QQQ $718.96
VIX 15.30 ↑5.3%（5D +2.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 41.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-10 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0
- 周四 09-10 10:00　【高】成屋销售　预测 3.99 ｜ 实际 待公布 ｜ 前值 4.06
- 周五 09-11 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.2
- 周五 09-11 08:30　【高】Inflation Rate YoY　预测 3.4 ｜ 实际 待公布 ｜ 前值 3.4
- 周五 09-11 08:30　【高】Inflation Rate MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.1
- 周五 09-11 08:30　【高】Core Inflation Rate YoY　预测 2.4 ｜ 实际 待公布 ｜ 前值 2.5
- 周五 09-11 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 51 ｜ 实际 待公布 ｜ 前值 51.7

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## XBI

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
XBI: 今开 162.74 → 收盘 163.81（+0.7%） ｜ 今日高 164.35 ｜ 低 162.51 ｜ 昨收 163.81 → 收盘 163.81（+0.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.11 | OI比 1.80 | ATM IV 26.5% | Skew 2.6pp | Term 1.13 | ExpMove ±2.9%（近端） | Rank 13%
量化视角： IV 历史低位（Rank 13%，期权偏便宜）｜期限结构正常（Term 1.13）｜保护溢价中性（Skew 2.6pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.11×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.80×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-11（4D）±2.9% ｜ 09-18（11D）±4.4% ｜ 09-25（18D）±6.7% ｜ 10-02（25D）±7.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -9,825,539 | GEX Change vs 上次快照 0 | Flip: Primary Flip: 165.43（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 380 / LOW 110 / INVALID 362
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 165.43（全链重定价，覆盖 94%）
Put Wall 158（弱结构｜现价高于该位 3.7%） | Call Wall 170（弱结构｜现价低于该位 3.6%）
最近结构参考: Flip 165（现价低于该位 1.0%）
量化视角： 负 Gamma（983万，无历史分位）｜负 Gamma 加深（0万）｜现价位于 Flip 下方 0.98%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 158（Put Wall，弱结构） / 163（MaxPain，仅结算参考）；上方 170（Call Wall，弱结构）。
• Gamma 区域：切换参考 165（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 162.0P — Vol 2,786 | 最新价 $1.66 | OI 1127→3799 (ΔOI +2672张) | ΔOI/Volume 95.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2672张（+237.1% vs前日OI），连续性待观察（方向未知）
09-11 163.0P — Vol 1,819 | 最新价 $2.02 | OI 31→1799 (ΔOI +1768张) | ΔOI/Volume 97.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1768张（+5703.2% vs前日OI），连续性待观察（方向未知）
09-11 170.0C — Vol 1,767 | 最新价 $0.45 | OI 121→1862 (ΔOI +1741张) | ΔOI/Volume 98.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1741张（+1438.8% vs前日OI），连续性待观察（方向未知）
09-11 164.0C — Vol 1,740 | 最新价 $2.26 | OI 237→1960 (ΔOI +1723张) | ΔOI/Volume 99.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1723张（+727.0% vs前日OI），连续性待观察（方向未知）
09-11 155.0P — Vol 1,924 | 最新价 $0.22 | OI 1879→3470 (ΔOI +1591张) | ΔOI/Volume 82.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1591张（+84.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 9,495 张（Put 6,031 / Call 3,464），跨 1 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +0 / P +0 ｜ Activity LOW ｜ 4D
09-18  C +0 / P +0 ｜ Activity LOW ｜ 11D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 18D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 25D

📆 09-11 Forward Structure
存量OI:      C 8.5k / P 15.4k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 2.26 / P 2.47
隐含波动率 ATM IV:  26.5%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 163（结算参考） ｜ Call Wall 164（+0.1%，弱）（OI 2.0k） ｜ Put Wall 162（-1.1%，弱）（OI 3.8k）
量化解读： 存量 Put 重｜ATM IV 26.5%｜历史 Rank 13%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（Activity LOW）仓位参考: Max Pain 158（结算参考） ｜ Call Wall 155（-5.4%，弱）（OI 10.8k） ｜ Put Wall 158（-3.5%，弱）（OI 16.9k）

09-25（Activity LOW）仓位参考: Max Pain 160（结算参考） ｜ Call Wall 167（+1.9%）（OI 1.4k）

10-02（Activity LOW）仓位参考: Max Pain 164（结算参考） ｜ Call Wall 165（+0.7%）（OI 0.2k） ｜ Put Wall 150（-8.4%，弱）（OI 0.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-07/XBI_evening.json