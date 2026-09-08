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

🔍 重点速览
🟡 **单日价格波动**: -3.0%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向


## NOW

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NOW: 今开 136.72 → 收盘 134.21（-1.8%） ｜ 今日高 136.77 ｜ 低 132.46 ｜ 昨收 141.26 → 收盘 134.21（-5.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.78 | OI比 0.96 | ATM IV 62.5% | Skew 0.7pp | Term 0.86 | ExpMove ±4.6%（近端） | Rank — (历史不足)
量化视角： 期限结构倒挂（Term 0.86，近月 IV 高于远月）｜保护溢价薄（Skew 0.7pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.78×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.96×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-11（3D）±4.6% ｜ 09-18（10D）±7.3% ｜ 09-25（17D）±9.2% ｜ 10-02（24D）±10.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 10,250,257 | GEX Change vs 上次快照 399,428 | Flip: Primary Flip: 122.36（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 612 / LOW 65 / INVALID 147
结构观察区: Primary Flip 122.36（全链重定价，覆盖 100%）
最近结构参考: Flip 122（现价高于该位 9.7%）
量化视角： 正 Gamma（1025万，无历史分位）｜正 Gamma 增强（+40万）｜现价位于 Flip 上方 9.68%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 140（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 122（全链重定价，覆盖 100%）。
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
存量OI:      C 18.2k / P 17.4k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 3.25 / P 2.88
隐含波动率 ATM IV:  62.5%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 140（结算参考） ｜ Put Wall 140（+4.3%，弱）（OI 1.8k）
量化解读： 存量两侧均衡｜ATM IV 62.5%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（Activity LOW）仓位参考: Max Pain 120（结算参考）

09-25（Activity LOW）仓位参考: Max Pain 131（结算参考）

10-02（Activity LOW）仓位参考: Max Pain 132（结算参考）

📅 事件差分（观察，非因果）: 09-11（3D）ATM IV 62.5% vs 09-18 55.8%（差 +6.8pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-08/NOW_evening.json