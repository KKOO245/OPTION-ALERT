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


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 367.81 → 收盘 366.70（-0.3%） ｜ 今日高 369.55 ｜ 低 363.23 ｜ 昨收 366.70 → 收盘 366.70（+0.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.84 | OI比 1.15 | ATM IV 33.2% | Skew -5.9pp | Term 0.93 | ExpMove ±3.5%（近端） | Rank — (历史不足)
量化视角： 期限结构正常（Term 0.93）｜Put 保护异常便宜（Skew -5.9pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 1.84）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.84×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.15×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-11（4D）±3.5% ｜ 09-18（11D）±6.6% ｜ 09-25（18D）±5.8% ｜ 10-02（25D）±8.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -3,588,455 | GEX Change vs 上次快照 110,845 | Flip: Primary Flip: 381.24（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 293 / LOW 188 / INVALID 421
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 381.24（全链重定价，覆盖 98%）
Call Wall 400（弱结构｜现价低于该位 8.3%）
最近结构参考: Flip 381（现价低于该位 3.8%）
量化视角： 负 Gamma（359万，无历史分位）｜负 Gamma 缓解（+11万）｜现价位于 Flip 下方 3.81%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 375（MaxPain，仅结算参考） / 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 381（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 365.0P — Vol 111 | 最新价 $5.38 | OI 30→128 (ΔOI +98张) | ΔOI/Volume 88.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增98张（+326.7% vs前日OI），连续性待观察（方向未知）
09-11 350.0P — Vol 99 | 最新价 $1.05 | OI 123→203 (ΔOI +80张) | ΔOI/Volume 80.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增80张（+65.0% vs前日OI），连续性待观察（方向未知）
09-11 357.5P — Vol 61 | 最新价 $2.29 | OI 23→78 (ΔOI +55张) | ΔOI/Volume 90.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增55张（+239.1% vs前日OI），连续性待观察（方向未知）
09-11 365.0C — Vol 76 | 最新价 $6.66 | OI 20→64 (ΔOI +44张) | ΔOI/Volume 57.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增44张（+220.0% vs前日OI），连续性待观察（方向未知）
09-11 337.5P — Vol 34 | 最新价 $0.19 | OI 0→34 (ΔOI +34张) | ΔOI/Volume 100.0% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增34张（前日OI缺失），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 311 张（Put 267 / Call 44），跨 1 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +0 / P +0 ｜ Activity LOW ｜ 4D
09-18  C +0 / P +0 ｜ Activity LOW ｜ 11D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 18D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 25D

📆 09-11 Forward Structure
存量OI:      C 1.0k / P 1.1k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 6.00 / P 6.80
隐含波动率 ATM IV:  33.2%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 375（结算参考） ｜ Call Wall 400（+9.1%，弱）（OI 0.1k） ｜ Put Wall 350（-4.6%）（OI 0.2k）
量化解读： 存量两侧均衡｜ATM IV 33.2%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（Activity LOW）仓位参考: Max Pain 378（结算参考） ｜ Call Wall 400（+9.1%，弱）（OI 1.1k）

09-25（Activity LOW）仓位参考: Max Pain 380（结算参考） ｜ Put Wall 370（+0.9%，弱）（OI 0.1k）

10-02（Activity LOW）仓位参考: Max Pain 370（结算参考） ｜ Put Wall 335（-8.6%）（OI 2.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-07/ISRG_evening.json