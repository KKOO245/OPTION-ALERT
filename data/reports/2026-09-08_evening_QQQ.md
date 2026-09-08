# 期权晚报 2026-09-08（快照 17:30 ET）

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


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 720.97 → 收盘 718.36（-0.4%） ｜ 今日高 721.89 ｜ 低 715.57 ｜ 昨收 718.96 → 收盘 718.36（-0.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.04 | OI比 1.79 | ATM IV 11.5% | Skew 1.0pp | Term 1.61 | ExpMove ±0.7%（近端） | Rank 14%
量化视角： IV 历史低位（Rank 14%，期权偏便宜）｜期限结构正常偏陡（Term 1.61）｜保护溢价薄（Skew 1.0pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.04×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.79×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 41% ｜ P/C OI(近端) 63%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 41%）｜近端持仓结构中性（P/C OI 分位 63%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-09（1D）±0.7% ｜ 09-10（2D）±1.0% ｜ 09-11（3D）±1.4% ｜ 09-14（6D）±1.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -143,700,430 | GEX Change vs 上次快照 66,116,773 | Flip: Primary Flip: 720.74（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 2441 / LOW 595 / INVALID 1744
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 720.74（全链重定价，覆盖 94%）
Put Wall 700（弱结构｜现价高于该位 2.6%） | Call Wall 750（弱结构｜现价低于该位 4.2%）
最近结构参考: Flip 721（现价低于该位 0.3%）
量化视角： 负 Gamma（1.44亿，历史分位 41%，中性区）｜负 Gamma 缓解（+6612万）｜现价位于 Flip 下方 0.33%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 700（Put Wall，弱结构） / 718（MaxPain，仅结算参考）；上方 750（Call Wall，弱结构）。
• Gamma 区域：切换参考 721（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-09  C +0 / P +0 ｜ Activity LOW ｜ 1D
09-10  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-11  C +0 / P +0 ｜ Activity LOW ｜ 3D
09-14  C +0 / P +0 ｜ Activity LOW ｜ 6D

📆 09-09 Forward Structure
存量OI:      C 46.3k / P 107.2k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 2.49 / P 2.45
隐含波动率 ATM IV:  16.5%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 717（结算参考） ｜ Call Wall 722（+0.5%，弱）（OI 4.9k）
量化解读： 存量 Put 重｜ATM IV 16.5%｜历史 Rank 14%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-10（Activity LOW）仓位参考: Max Pain 715（结算参考） ｜ Call Wall 725（+0.9%）（OI 2.8k） ｜ Put Wall 656（-8.7%，弱）（OI 3.6k）

09-11（Activity LOW）仓位参考: Max Pain 715（结算参考） ｜ Call Wall 750（+4.4%，弱）（OI 12.0k） ｜ Put Wall 705（-1.9%，弱）（OI 21.9k）

09-14（Activity LOW）仓位参考: Max Pain 715（结算参考） ｜ Call Wall 725（+0.9%，弱）（OI 1.7k） ｜ Put Wall 690（-3.9%，弱）（OI 1.5k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-08/QQQ_evening.json