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


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 18.65 → 收盘 17.61（-5.6%） ｜ 今日高 19.30 ｜ 低 17.25 ｜ 昨收 17.61 → 收盘 17.61（+0.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.53 | OI比 0.34 | ATM IV 67.2% | Skew -4.8pp | Term 1.19 | ExpMove ±7.8%（近端） | Rank 1%
量化视角： IV 历史低位（Rank 1%，期权偏便宜）｜期限结构正常偏陡（Term 1.19）｜Put 保护异常便宜（Skew -4.8pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.34）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.53×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.34×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（4D）±7.8% ｜ 09-18（11D）±12.1% ｜ 09-25（18D）±14.6% ｜ 10-02（25D）±18.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 4,968,379 | GEX Change vs 上次快照 1,145,554 | Flip: Primary Flip: 16.79（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 272 / LOW 78 / INVALID 126
结构观察区: Primary Flip 16.79（全链重定价，覆盖 100%）
最近结构参考: Flip 17（现价高于该位 4.9%）
量化视角： 正 Gamma（497万，无历史分位）｜正 Gamma 增强（+115万）｜现价位于 Flip 上方 4.91%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 18（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 17（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 22.0C — Vol 1,397 | 最新价 $0.12 | OI 14393→15456 (ΔOI +1063张) | ΔOI/Volume 76.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1063张（+7.4% vs前日OI），连续性待观察（方向未知）
09-18 21.5C — Vol 852 | 最新价 $0.14 | OI 1575→2389 (ΔOI +814张) | ΔOI/Volume 95.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增814张（+51.7% vs前日OI），连续性待观察（方向未知）
09-18 22.5C — Vol 1,228 | 最新价 $0.09 | OI 878→1538 (ΔOI +660张) | ΔOI/Volume 53.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增660张（+75.2% vs前日OI），连续性待观察（方向未知）
09-11 17.0P — Vol 1,030 | 最新价 $0.39 | OI 966→1565 (ΔOI +599张) | ΔOI/Volume 58.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增599张（+62.0% vs前日OI），连续性待观察（方向未知）
09-11 19.0C — Vol 1,264 | 最新价 $0.24 | OI 493→1043 (ΔOI +550张) | ΔOI/Volume 43.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增550张（+111.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,686 张（Put 599 / Call 3,087），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +0 / P +0 ｜ Activity LOW ｜ 4D
09-18  C +0 / P +0 ｜ Activity LOW ｜ 11D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 18D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 25D

📆 09-11 Forward Structure
存量OI:      C 19.0k / P 6.6k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 0.78 / P 0.60
隐含波动率 ATM IV:  67.2%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 18（结算参考） ｜ Put Wall 17（-3.5%）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 67.2%｜历史 Rank 1%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（Activity LOW）仓位参考: Max Pain 20（结算参考）

09-25（Activity LOW）仓位参考: Max Pain 18（结算参考）

10-02（Activity LOW）仓位参考: Max Pain 18（结算参考）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-07/USAR_evening.json