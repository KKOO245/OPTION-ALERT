# 期权晚报 2026-10-08（快照 16:40 ET）

📊 市场环境

SPY $773.93 ｜ QQQ $747.58
VIX 15.41 ↑2.2%（5D -6.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-08

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-12 785C ΔOI +2,202（距现价 +1.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 774.86 → 收盘 773.93（-0.1%） ｜ 今日高 777.09 ｜ 低 770.43 ｜ 昨收 777.22 → 收盘 773.93（-0.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.98 | OI比 1.82 | ATM IV 14.8% | Skew -0.1pp | Term 0.86 | ExpMove ±0.5%（近端） | Rank 65%
量化视角： IV 中性（Rank 65%）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.1pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.98×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.82×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 46% ｜ P/C OI(近端) 49%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 46%）｜近端持仓结构中性（P/C OI 分位 49%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-09（1D）±0.5% ｜ 10-12（4D）±0.7% ｜ 10-13（5D）±0.8% ｜ 10-14（6D）±1.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -438,209,773 | GEX Change vs 上次快照 -438,011,823 | Flip: Primary Flip: 775.42（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 2544 / LOW 392 / INVALID 1926
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 775.42（全链重定价，覆盖 93%）
Call Wall 785（弱结构｜现价低于该位 1.4%）
最近结构参考: Flip 775（现价低于该位 0.2%）
量化视角： 负 Gamma（4.38亿，历史分位 46%，中性区）｜负 Gamma 加深（4.38亿）｜现价位于 Flip 下方 0.19%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 776（MaxPain，仅结算参考） / 785（Call Wall，弱结构）。
• Gamma 区域：切换参考 775（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +37.9k / P +78.9k ｜ Activity HIGH ｜ 1D
10-12  C +17.3k / P +10.2k ｜ Activity HIGH ｜ 4D
10-13  C +17.8k / P +22.3k ｜ Activity HIGH ｜ 5D
10-14  C +18.7k / P +20.2k ｜ Activity HIGH ｜ 6D

📆 10-09 Forward Structure
存量OI: C 558.2k / P 707.9k，今日变化ΔOI: C +37.9k / P +78.9k，平值价格ATM: C $2.14 / P $1.47 ｜ ATM IV 10.9%，净 delta 敞口 -178k shares
Top ΔOI: P 710 +18,007 ｜ P 715 +17,223 ｜ P 725 -7,542
仓位参考: Max Pain 773 ｜ Call Wall 785（+1.4%）（OI 124.7k） ｜ Put Wall 767（-0.9%，弱）（OI 70.3k）
量化解读： 存量 Put 重｜ATM IV 10.9%｜历史 Rank 65%（近端代理）｜IV/RV 1.19×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 177,914 股

📆 10-12 Forward Structure
存量OI: C 65.1k / P 109.4k，今日变化ΔOI: C +17.3k / P +10.2k，平值价格ATM: C $2.98 / P $2.34 ｜ ATM IV 8.1%，净 delta 敞口 -82k shares
Top ΔOI: C 785 +2,202
仓位参考: Max Pain 775 ｜ Call Wall 785（+1.4%，弱）（OI 5.3k） ｜ Put Wall 770（-0.5%，弱）（OI 4.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 8.1%｜历史 Rank 65%（近端代理）｜IV/RV 0.89×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 82,159 股

📆 10-13 Forward Structure
存量OI: C 45.7k / P 74.5k，今日变化ΔOI: C +17.8k / P +22.3k，平值价格ATM: C $3.58 / P $2.84 ｜ ATM IV 8.8%，净 delta 敞口 -191k shares
Top ΔOI: P 705 +4,039 ｜ C 790 +2,912 ｜ P 774 +2,808
仓位参考: Max Pain 776 ｜ Call Wall 790（+2.1%，弱）（OI 4.1k） ｜ Put Wall 774（+0.0%，弱）（OI 3.1k）
量化解读： 存量 Put 重｜ATM IV 8.8%｜历史 Rank 65%（近端代理）｜IV/RV 0.96×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 190,608 股

📆 10-14 Forward Structure
存量OI: C 106.6k / P 70.3k，今日变化ΔOI: C +18.7k / P +20.2k，平值价格ATM: C $4.37 / P $3.54 ｜ ATM IV 9.9%，净 delta 敞口 -1k shares
Top ΔOI: P 700 +9,669 ｜ C 790 +8,628 ｜ P 778 +2,504
仓位参考: Max Pain 775 ｜ Call Wall 790（+2.1%）（OI 79.8k） ｜ Put Wall 755（-2.4%，弱）（OI 5.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 9.9%｜历史 Rank 65%（近端代理）｜IV/RV 1.08×（近似）｜净 delta 敞口 负 1,124 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-08/SPY_evening.json