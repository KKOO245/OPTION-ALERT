# 期权晚报 2026-11-04（快照 16:40 ET）

📊 市场环境

SPY $766.81 ｜ QQQ $691.95
VIX 16.61 ↓20.3%（5D -1.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-04

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 54.5 ｜ 前值 54.9　✅ 今日已公布
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🟡 **事件差分**: 11-06 ATM IV 56.5% vs 11-09 43.6%（差 +12.9pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-06 385P ΔOI +1,243（距现价 -0.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 379.80 → 收盘 385.19（+1.4%） ｜ 今日高 392.04 ｜ 低 375.50 ｜ 昨收 398.50 → 收盘 385.19（-3.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.97 | OI比 1.18 | ATM IV 29.6% | Skew 0.8pp | Term 1.47 | ExpMove ±3.4%（近端） | Rank 4%
量化视角： IV 历史低位（Rank 4%，期权偏便宜）｜期限结构正常偏陡（Term 1.47）｜保护溢价薄（Skew 0.8pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.97×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.18×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-06（2D）±3.4% ｜ 11-09（5D）±4.1% ｜ 11-11（7D）±5.1% ｜ 11-13（9D）±5.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 805,603 | GEX Change vs 上次快照 11,190,510 | Flip: Primary Flip: 385.00（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 1298 / LOW 183 / INVALID 873
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 385.00（全链重定价，覆盖 90%）
Call Wall 400（弱结构｜现价低于该位 3.7%）
最近结构参考: Flip 385（现价高于该位 0.0%）
量化视角： 正 Gamma（81万，无历史分位）｜由负转正（+1119万）｜现价位于 Flip 上方 0.05%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 400（MaxPain，仅结算参考） / 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 385（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-06  C +12.0k / P +6.3k ｜ Activity MEDIUM △ ｜ 2D
11-09  C +6.5k / P +5.7k ｜ Activity HIGH ｜ 5D
11-11  C +2.4k / P +1.3k ｜ Activity HIGH ｜ 7D
11-13  C +4.4k / P +4.4k ｜ Activity HIGH ｜ 9D

📆 11-06 Forward Structure
存量OI: C 170.3k / P 258.9k，今日变化ΔOI: C +12.0k / P +6.3k，平值价格ATM: C $6.70 / P $6.20 ｜ ATM IV 56.5%，净 delta 敞口 -53k shares
Top ΔOI: P 385 +1,243 ｜ C 400 +1,066
仓位参考: Max Pain 395 ｜ Call Wall 410（+6.4%，弱）（OI 10.8k） ｜ Put Wall 380（-1.3%，弱）（OI 10.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 56.5%｜历史 Rank 4%（近端代理）｜IV/RV 1.73×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 53,070 股

📆 11-09 Forward Structure
存量OI: C 20.1k / P 15.3k，今日变化ΔOI: C +6.5k / P +5.7k，平值价格ATM: C $8.11 / P $7.55 ｜ ATM IV 43.6%，净 delta 敞口 -33k shares
Top ΔOI: C 420 +609
仓位参考: Max Pain 400 ｜ Call Wall 420（+9.0%）（OI 2.4k） ｜ Put Wall 380（-1.3%，弱）（OI 1.4k）
量化解读： 存量 Call 重｜ATM IV 43.6%｜历史 Rank 4%（近端代理）｜IV/RV 1.33×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 32,511 股

📆 11-11 Forward Structure
存量OI: C 10.0k / P 5.5k，今日变化ΔOI: C +2.4k / P +1.3k，平值价格ATM: C $10.15 / P $9.60 ｜ ATM IV 46.1%，净 delta 敞口 -11k shares
Top ΔOI: C 410 +484 ｜ P 355 +435
仓位参考: Max Pain 400 ｜ Call Wall 410（+6.4%，弱）（OI 1.1k） ｜ Put Wall 405（+5.1%，弱）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 46.1%｜历史 Rank 4%（近端代理）｜IV/RV 1.41×（近似）｜净 delta 敞口 负 11,139 股

📆 11-13 Forward Structure
存量OI: C 51.2k / P 37.1k，今日变化ΔOI: C +4.4k / P +4.4k，平值价格ATM: C $11.74 / P $10.98 ｜ ATM IV 46.9%，净 delta 敞口 -47k shares
Top ΔOI: C 407 +1,310
仓位参考: Max Pain 380 ｜ Call Wall 420（+9.0%，弱）（OI 2.1k） ｜ Put Wall 350（-9.1%，弱）（OI 2.1k）
量化解读： 存量 Call 重｜ATM IV 46.9%｜历史 Rank 4%（近端代理）｜IV/RV 1.44×（近似）｜净 delta 敞口 负 47,423 股

📅 事件差分（观察，非因果）: 11-06（2D）ATM IV 56.5% vs 11-09 43.6%（差 +12.9pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-04/TSLA_evening.json