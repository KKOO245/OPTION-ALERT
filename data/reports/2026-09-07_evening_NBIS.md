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


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 210.19 → 收盘 226.39（+7.7%） ｜ 今日高 226.58 ｜ 低 209.40 ｜ 昨收 226.39 → 收盘 226.39（+0.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.52 | OI比 0.81 | ATM IV 78.0% | Skew -5.4pp | Term 1.08 | ExpMove ±8.7%（近端） | Rank 8%
量化视角： IV 历史低位（Rank 8%，期权偏便宜）｜期限结构正常（Term 1.08）｜Put 保护异常便宜（Skew -5.4pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.81）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.52×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.81×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-11（4D）±8.7% ｜ 09-18（11D）±14.2% ｜ 09-25（18D）±15.9% ｜ 10-02（25D）±17.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 3,789,074 | GEX Change vs 上次快照 634,807 | Flip: Primary Flip: 219.23（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 538 / LOW 44 / INVALID 128
结构观察区: Primary Flip 219.23（全链重定价，覆盖 100%）
最近结构参考: Flip 219（现价高于该位 3.3%）
量化视角： 正 Gamma（379万，无历史分位）｜正 Gamma 增强（+63万）｜现价位于 Flip 上方 3.27%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 220（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 219（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 225.0C — Vol 5,180 | 最新价 $10.44 | OI 1359→5226 (ΔOI +3867张) | ΔOI/Volume 74.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3867张（+284.6% vs前日OI），连续性待观察（方向未知）
09-11 220.0P — Vol 2,389 | 最新价 $6.55 | OI 2268→4113 (ΔOI +1845张) | ΔOI/Volume 77.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1845张（+81.3% vs前日OI），连续性待观察（方向未知）
09-11 240.0C — Vol 2,791 | 最新价 $5.00 | OI 1149→2827 (ΔOI +1678张) | ΔOI/Volume 60.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1678张（+146.0% vs前日OI），连续性待观察（方向未知）
09-18 100.0P — Vol 2,162 | 最新价 $0.07 | OI 9943→11200 (ΔOI +1257张) | ΔOI/Volume 58.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1257张（+12.6% vs前日OI），连续性待观察（方向未知）
09-11 235.0C — Vol 2,216 | 最新价 $6.37 | OI 669→1897 (ΔOI +1228张) | ΔOI/Volume 55.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1228张（+183.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 9,875 张（Put 3,102 / Call 6,773），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +0 / P +0 ｜ Activity LOW ｜ 4D
09-18  C +0 / P +0 ｜ Activity LOW ｜ 11D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 18D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 25D

📆 09-11 Forward Structure
存量OI:      C 43.9k / P 35.8k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 9.41 / P 10.30
隐含波动率 ATM IV:  78.0%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 220（结算参考） ｜ Call Wall 225（-0.6%，弱）（OI 5.2k） ｜ Put Wall 220（-2.8%，弱）（OI 4.1k）
量化解读： 存量 Call 重｜ATM IV 78.0%｜历史 Rank 8%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（Activity LOW）仓位参考: Max Pain 210（结算参考）

09-25（Activity LOW）仓位参考: Max Pain 220（结算参考）

10-02（Activity LOW）仓位参考: Max Pain 210（结算参考）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-07/NBIS_evening.json