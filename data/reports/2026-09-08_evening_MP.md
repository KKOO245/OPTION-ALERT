# 期权晚报 2026-09-08（快照 16:40 ET）

📊 市场环境

SPY $765.96 ｜ QQQ $718.36
VIX 15.72 ↑2.8%（5D -3.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 40.8（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-10 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0
- 周四 09-10 10:00　【高】成屋销售　预测 3.99 ｜ 实际 待公布 ｜ 前值 4.06
- 周五 09-11 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.2
- 周五 09-11 08:30　【高】Inflation Rate MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.1
- 周五 09-11 08:30　【高】Inflation Rate YoY　预测 3.4 ｜ 实际 待公布 ｜ 前值 3.4
- 周五 09-11 08:30　【高】Core Inflation Rate YoY　预测 2.4 ｜ 实际 待公布 ｜ 前值 2.5
- 周五 09-11 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 51 ｜ 实际 待公布 ｜ 前值 51.7

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 54.81 → 收盘 55.37（+1.0%） ｜ 今日高 57.31 ｜ 低 54.56 ｜ 昨收 54.53 → 收盘 55.37（+1.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.47 | OI比 0.81 | ATM IV 71.2% | Skew -6.5pp | Term 0.98 | ExpMove ±5.5%（近端） | Rank 55%
量化视角： IV 中性（Rank 55%）｜期限结构正常（Term 0.98）｜Put 保护异常便宜（Skew -6.5pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.81）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.47×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.81×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-11（3D）±5.5% ｜ 09-18（10D）±8.9% ｜ 09-25（17D）±12.2% ｜ 10-02（24D）±14.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,242,425 | GEX Change vs 上次快照 -1,676,985 | Flip: Primary Flip: 54.53（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 266 / LOW 55 / INVALID 89
结构观察区: Primary Flip 54.53（全链重定价，覆盖 100%）
Call Wall 60（弱结构｜现价低于该位 7.7%）
最近结构参考: Flip 55（现价高于该位 1.5%）
量化视角： 正 Gamma（124万，无历史分位）｜正 Gamma 减弱（168万）｜现价位于 Flip 上方 1.54%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 54（MaxPain，仅结算参考）；上方 60（Call Wall，弱结构）。
• Gamma 区域：切换参考 55（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-11  C +0 / P +0 ｜ Activity LOW ｜ 3D
09-18  C +0 / P +0 ｜ Activity LOW ｜ 10D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 17D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 24D

📆 09-11 Forward Structure
存量OI:      C 7.3k / P 5.9k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 1.73 / P 1.29
隐含波动率 ATM IV:  71.2%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 54（结算参考）
量化解读： 存量 Call 重｜ATM IV 71.2%｜历史 Rank 55%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（Activity LOW）仓位参考: Max Pain 55（结算参考） ｜ Put Wall 55（-0.7%，弱）（OI 9.1k）

09-25（Activity LOW）仓位参考: Max Pain 52（结算参考） ｜ Call Wall 60（+8.4%，弱）（OI 0.7k）

10-02（Activity LOW）仓位参考: Max Pain 59（结算参考） ｜ Put Wall 50（-9.7%）（OI 1.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-08/MP_evening.json