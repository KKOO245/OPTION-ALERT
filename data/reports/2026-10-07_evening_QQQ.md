# 期权晚报 2026-10-07（快照 16:40 ET）

📊 市场环境

SPY $777.22 ｜ QQQ $757.73
VIX 15.08 ↑0.5%（5D -7.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 44.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-07

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布　✅ 今日已公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-08 755P ΔOI +18,346（距现价 -0.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-08 755P ΔOI +18,346 占该期限总 OI 10.9%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 753.87 → 收盘 757.73（+0.5%） ｜ 今日高 758.15 ｜ 低 751.76 ｜ 昨收 759.66 → 收盘 757.73（-0.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.05 | OI比 2.15 | ATM IV 11.6% | Skew 0.7pp | Term 1.60 | ExpMove ±0.6%（近端） | Rank 14%
量化视角： IV 历史低位（Rank 14%，期权偏便宜）｜期限结构正常偏陡（Term 1.60）｜保护溢价薄（Skew 0.7pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.05×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 2.15×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 66% ｜ P/C OI(近端) 83%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 66%）｜近端持仓结构中性（P/C OI 分位 83%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-08（1D）±0.6% ｜ 10-09（2D）±0.9% ｜ 10-12（5D）±1.2% ｜ 10-13（6D）±1.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 149,053,159 | GEX Change vs 上次快照 288,964,868 | Flip: Primary Flip: 755.43（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 2761 / LOW 322 / INVALID 2019
结构观察区: Primary Flip 755.43（全链重定价，覆盖 94%）
Call Wall 760（现价低于该位 0.3%）
最近结构参考: Call Wall 760（现价低于该位 0.3%）
量化视角： 正 Gamma（1.49亿，历史分位 66%，中性区）｜由负转正（+2.89亿）｜现价位于 Flip 上方 0.30%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 758（MaxPain，仅结算参考） / 760（Call Wall）。
• Gamma 区域：切换参考 755（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-08  C +11.0k / P +44.8k ｜ Activity HIGH ｜ 1D
10-09  C +15.5k / P +47.0k ｜ Activity HIGH ｜ 2D
10-12  C +9.6k / P +13.6k ｜ Activity HIGH ｜ 5D
10-13  C +5.1k / P +25.3k ｜ Activity HIGH ｜ 6D

📆 10-08 Forward Structure
存量OI: C 37.5k / P 130.6k，今日变化ΔOI: C +11.0k / P +44.8k，平值价格ATM: C $2.16 / P $2.27 ｜ ATM IV 13.9%，净 delta 敞口 -1.3M shares
Top ΔOI: P 755 +18,346 ｜ P 760 +3,877 ｜ P 758 +1,755
仓位参考: Max Pain 756 ｜ Call Wall 770（+1.6%，弱）（OI 2.2k） ｜ Put Wall 755（-0.4%，弱）（OI 19.3k）
量化解读： 存量 Put 重｜ATM IV 13.9%｜历史 Rank 14%（近端代理）｜IV/RV 1.03×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,283,300 股

📆 10-09 Forward Structure
存量OI: C 186.6k / P 355.3k，今日变化ΔOI: C +15.5k / P +47.0k，平值价格ATM: C $3.39 / P $3.20 ｜ ATM IV 14.7%，净 delta 敞口 -1.6M shares
Top ΔOI: P 754 +19,719 ｜ C 765 +4,392 ｜ P 760 +2,908
仓位参考: Max Pain 750 ｜ Call Wall 754（-0.5%）（OI 21.1k） ｜ Put Wall 754（-0.5%，弱）（OI 23.1k）
量化解读： 存量 Put 重｜ATM IV 14.7%｜历史 Rank 14%（近端代理）｜IV/RV 1.08×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,628,079 股

📆 10-12 Forward Structure
存量OI: C 26.2k / P 94.1k，今日变化ΔOI: C +9.6k / P +13.6k，平值价格ATM: C $4.53 / P $4.30 ｜ ATM IV 12.5%，净 delta 敞口 -70k shares
Top ΔOI: C 780 +4,828 ｜ P 742 +3,883 ｜ P 731 +1,979
仓位参考: Max Pain 752 ｜ Call Wall 780（+2.9%）（OI 5.2k） ｜ Put Wall 738（-2.6%）（OI 12.6k）
量化解读： 存量 Put 重｜ATM IV 12.5%｜历史 Rank 14%（近端代理）｜IV/RV 0.92×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 69,708 股

📆 10-13 Forward Structure
存量OI: C 14.4k / P 69.0k，今日变化ΔOI: C +5.1k / P +25.3k，平值价格ATM: C $5.33 / P $5.04 ｜ ATM IV 13.3%，净 delta 敞口 -370k shares
Top ΔOI: P 750 +10,519 ｜ P 692 +4,573 ｜ P 727 +1,487
仓位参考: Max Pain 752 ｜ Call Wall 780（+2.9%，弱）（OI 1.1k） ｜ Put Wall 740（-2.3%，弱）（OI 10.9k）
量化解读： 存量 Put 重｜ATM IV 13.3%｜历史 Rank 14%（近端代理）｜IV/RV 0.98×（近似）｜净 delta 敞口 负 370,259 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-07/QQQ_evening.json