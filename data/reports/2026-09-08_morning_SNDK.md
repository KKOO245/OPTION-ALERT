# 期权晨报 2026-09-08（快照 10:49 ET）

📊 市场环境

SPY $765.75 ｜ QQQ $718.36
VIX 15.51 ↑1.4%（5D -5.1%） ｜ Vol Regime: NORMAL
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
🟡 **单日价格波动**: +2.2%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 1,740.00 → 今开 1,769.43（+1.7%） | 较昨收变动（含盘初走势） ｜ 今日高 1794.95 ｜ 低 1741.00

Options: P/C成交量 0.67 | OI比 0.99 | ATM IV 89.1% | Skew -5.4pp | Term 0.89 | ExpMove ±6.7%（近端） | Rank 38%
量化视角： IV 中性（Rank 38%）｜期限结构倒挂（Term 0.89，近月 IV 高于远月）｜Put 保护异常便宜（Skew -5.4pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.67×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.99×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-11（3D）±6.7% ｜ 09-18（10D）±11.3% ｜ 09-25（17D）±13.5% ｜ 10-02（24D）±15.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 8,403,901 | GEX Change vs 上次快照 877,863 | Flip: Primary Flip: 1607.11（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1982 / LOW 388 / INVALID 1030
结构观察区: Primary Flip 1607.11（全链重定价，覆盖 100%）
最近结构参考: Flip 1607（现价高于该位 10.6%）
量化视角： 正 Gamma（840万，无历史分位）｜正 Gamma 增强（+88万）｜现价位于 Flip 上方 10.61%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 1,595（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1607（全链重定价，覆盖 100%）。
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
存量OI:      C 28.7k / P 28.5k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 58.86 / P 61.00
隐含波动率 ATM IV:  89.1%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 1,595（结算参考）
量化解读： 存量两侧均衡｜ATM IV 89.1%｜历史 Rank 38%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（Activity LOW）仓位参考: Max Pain 1,450（结算参考）

09-25（Activity LOW）仓位参考: Max Pain 1,555（结算参考） ｜ Call Wall 1800（+1.3%）（OI 0.4k）

10-02（Activity LOW）仓位参考: Max Pain 1,550（结算参考） ｜ Call Wall 1800（+1.3%，弱）（OI 0.4k）

📅 事件差分（观察，非因果）: 09-11（3D）ATM IV 89.1% vs 09-18 80.4%（差 +8.7pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-08/SNDK_morning.json