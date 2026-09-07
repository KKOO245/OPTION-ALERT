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


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 362.07 → 收盘 354.08（-2.2%） ｜ 今日高 364.69 ｜ 低 351.32 ｜ 昨收 354.08 → 收盘 354.08（+0.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.55 | OI比 0.34 | ATM IV 32.0% | Skew -1.8pp | Term 1.24 | ExpMove ±3.0%（近端） | Rank 3%
量化视角： IV 历史低位（Rank 3%，期权偏便宜）｜期限结构正常偏陡（Term 1.24）｜Put 保护异常便宜（Skew -1.8pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.34）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.55×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.34×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-09（2D）±3.0% ｜ 09-11（4D）±4.1% ｜ 09-14（7D）±4.5% ｜ 09-16（9D）±5.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 37,904,308 | GEX Change vs 上次快照 9,742,784 | Flip: Primary Flip: 349.44（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1216 / LOW 91 / INVALID 595
结构观察区: Primary Flip 349.44（全链重定价，覆盖 100%）
Put Wall 340（弱结构｜现价高于该位 4.1%）
最近结构参考: Flip 349（现价高于该位 1.3%）
量化视角： 正 Gamma（3790万，无历史分位）｜正 Gamma 增强（+974万）｜现价位于 Flip 上方 1.33%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 340（Put Wall，弱结构）；上方 358（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 349（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 130.0P — Vol 23,002 | 最新价 $0.01 | OI 789→23790 (ΔOI +23001张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增23001张（+2915.2% vs前日OI），连续性待观察（方向未知）
09-18 200.0P — Vol 10,008 | 最新价 $0.07 | OI 18445→28449 (ΔOI +10004张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10004张（+54.2% vs前日OI），连续性待观察（方向未知）
09-11 370.0C — Vol 29,933 | 最新价 $2.15 | OI 4831→14235 (ΔOI +9404张) | ΔOI/Volume 31.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9404张（+194.7% vs前日OI），连续性待观察（方向未知）
09-09 397.5C — Vol 7,527 | 最新价 $0.26 | OI 282→7298 (ΔOI +7016张) | ΔOI/Volume 93.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7016张（+2487.9% vs前日OI），连续性待观察（方向未知）
09-09 360.0C — Vol 44,099 | 最新价 $2.99 | OI 1917→8915 (ΔOI +6998张) | ΔOI/Volume 15.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6998张（+365.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 56,423 张（Put 33,005 / Call 23,418），跨 3 个期限｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-09  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-11  C +0 / P +0 ｜ Activity LOW ｜ 4D
09-14  C +0 / P +0 ｜ Activity LOW ｜ 7D
09-16  C +0 / P +0 ｜ Activity LOW ｜ 9D

📆 09-09 Forward Structure
存量OI:      C 168.0k / P 56.8k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 4.80 / P 5.80
隐含波动率 ATM IV:  32.0%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 358（结算参考）
量化解读： 存量 Call 重｜ATM IV 32.0%｜历史 Rank 3%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-11（Activity LOW）仓位参考: Max Pain 355（结算参考） ｜ Call Wall 370（+4.5%，弱）（OI 14.2k）

09-14（Activity LOW）仓位参考: Max Pain 360（结算参考） ｜ Put Wall 345（-2.6%，弱）（OI 0.6k）

09-16（Activity LOW）仓位参考: Max Pain 355（结算参考） ｜ Put Wall 355（+0.3%）（OI 0.9k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-07/TSLA_evening.json