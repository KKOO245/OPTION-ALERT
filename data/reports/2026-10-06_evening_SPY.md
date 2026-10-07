# 期权晚报 2026-10-06（快照 21:00 ET）

📊 市场环境

SPY $779.09 ｜ QQQ $759.66
VIX 15.01 ↓3.3%（5D -6.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 47.4（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-06

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 778.15 → 收盘 779.09（+0.1%） ｜ 今日高 781.62 ｜ 低 777.96 ｜ 昨收 774.83 → 收盘 779.09（+0.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.12 | OI比 1.17 | ATM IV 9.4% | Skew 0.8pp | Term 1.34 | ExpMove ±0.4%（近端） | Rank 20%
量化视角： IV 历史低位（Rank 20%，期权偏便宜）｜期限结构正常偏陡（Term 1.34）｜保护溢价薄（Skew 0.8pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.12×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.17×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 81% ｜ P/C OI(近端) 6%
量化视角的组合解读： Gamma 异常偏正（GEX 分位 81%）｜近端持仓极端 Call 重（P/C OI 分位 6%，历史极低区）｜⚠️ 需重点观察：持仓极端 + Gamma 异常侧组合——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-07（1D）±0.4% ｜ 10-08（2D）±0.6% ｜ 10-09（3D）±0.8% ｜ 10-12（6D）±0.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,277,789,731 | GEX Change vs 上次快照 -201,774,283 | Flip: Primary Flip: 774.12（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 2413 / LOW 317 / INVALID 1888
结构观察区: Primary Flip 774.12（全链重定价，覆盖 97%）
Call Wall 785（现价低于该位 0.8%）
最近结构参考: Flip 774（现价高于该位 0.6%）
量化视角： 正 Gamma（12.78亿，历史分位偏正区，比 81% 的交易日更正）｜正 Gamma 减弱（2.02亿）｜现价位于 Flip 上方 0.64%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 771（MaxPain，仅结算参考）；上方 785（Call Wall）。
• Gamma 区域：切换参考 774（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-07  C +0 / P +0 ｜ Activity LOW ｜ 1D
10-08  C +0 / P +0 ｜ Activity LOW ｜ 2D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 3D
10-12  C +0 / P +0 ｜ Activity LOW ｜ 6D

📆 10-07 Forward Structure
存量OI: C 146.6k / P 171.3k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $1.80 / P $1.29 ｜ ATM IV 9.4%，净 delta 敞口 0 shares
仓位参考: Max Pain 771 ｜ Call Wall 802（+2.9%，弱）（OI 16.9k） ｜ Put Wall 760（-2.5%，弱）（OI 6.9k）
量化解读： 存量两侧均衡｜ATM IV 9.4%｜历史 Rank 20%（近端代理）｜IV/RV 1.00×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-08（Activity LOW）仓位参考: Max Pain 770 ｜ Call Wall 795（+2.0%，弱）（OI 6.5k） ｜ Put Wall 756（-3.0%，弱）（OI 2.9k）

10-09（Activity LOW）仓位参考: Max Pain 770 ｜ Call Wall 785（+0.8%）（OI 125.9k） ｜ Put Wall 767（-1.6%，弱）（OI 64.6k）

10-12（Activity LOW）仓位参考: Max Pain 770 ｜ Call Wall 785（+0.8%）（OI 3.1k） ｜ Put Wall 770（-1.2%，弱）（OI 2.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-06/SPY_evening.json