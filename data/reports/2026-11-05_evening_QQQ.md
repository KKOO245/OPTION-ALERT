# 期权晚报 2026-11-05（快照 16:40 ET）

📊 市场环境

SPY $733.00 ｜ QQQ $647.05
VIX 28.18 ↑69.7%（5D +63.8%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 19.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-05

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🔴 **事件差分**: 11-06（1D）ATM IV 58.5% vs 11-09 42.6%（差 +15.9pp），覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Vol Regime 升档**: ELEVATED → STRESS（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-09 635P ΔOI +8,539（距现价 -1.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 683.17 → 收盘 647.05（-5.3%） ｜ 今日高 683.64 ｜ 低 647.05 ｜ 昨收 691.95 → 收盘 647.05（-6.5%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-10，窗口结束前不做对错判定）

Options: P/C成交量 0.93 | OI比 1.12 | ATM IV 55.5% | Skew -5.8pp | Term 0.62 | ExpMove ±2.5%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.62，近月 IV 高于远月）｜Put 保护异常便宜（Skew -5.8pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.93×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.12×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 18% ｜ P/C OI(近端) 11%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 18%）｜近端持仓结构中性（P/C OI 分位 11%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-06（1D）±2.5% ｜ 11-09（4D）±3.6% ｜ 11-10（5D）±4.1% ｜ 11-11（6D）±4.6%
   ⇒ IV–VIX Spread: +27.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -556,987,532 | GEX Change vs 上次快照 321,380,614 | Flip: Primary Flip: 691.21（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 81%（带内） ｜ IV 有效性: VALID 2583 / LOW 169 / INVALID 1814
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 691.21（全链重定价，覆盖 81%）
最近结构参考: Flip 691（现价低于该位 6.4%）
量化视角： 负 Gamma（5.57亿，历史分位偏负区，比 82% 的交易日更负）｜负 Gamma 缓解（+3.21亿）｜现价位于 Flip 下方 6.39%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 694（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 691（全链重定价，覆盖 81%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-06  C +53.3k / P +15.7k ｜ Activity HIGH ｜ 1D
11-09  C +13.5k / P +44.5k ｜ Activity HIGH ｜ 4D
11-10  C +5.8k / P +5.3k ｜ Activity HIGH ｜ 5D
11-11  C +6.1k / P +8.3k ｜ Activity HIGH ｜ 6D

📆 11-06 Forward Structure
存量OI: C 468.0k / P 619.0k，今日变化ΔOI: C +53.3k / P +15.7k，平值价格ATM: C $9.01 / P $6.97 ｜ ATM IV 58.5%，净 delta 敞口 171k shares
Top ΔOI: C 705 +22,966 ｜ P 691 +14,339
仓位参考: Max Pain 710 ｜ Put Wall 660（+2.0%，弱）（OI 12.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 58.5%｜历史 Rank 100%（近端代理）｜IV/RV 2.58×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 170,586 股

📆 11-09 Forward Structure
存量OI: C 41.3k / P 87.5k，今日变化ΔOI: C +13.5k / P +44.5k，平值价格ATM: C $12.74 / P $10.51 ｜ ATM IV 42.6%，净 delta 敞口 -1.1M shares
Top ΔOI: P 635 +8,539 ｜ P 560 +5,845 ｜ C 700 +5,713
仓位参考: Max Pain 695 ｜ Put Wall 635（-1.9%，弱）（OI 9.4k）
量化解读： 存量 Put 重｜ATM IV 42.6%｜历史 Rank 100%（近端代理）｜IV/RV 1.88×（近似）｜净 delta 敞口 负 1,104,760 股

📆 11-10 Forward Structure
存量OI: C 40.2k / P 20.3k，今日变化ΔOI: C +5.8k / P +5.3k，平值价格ATM: C $13.62 / P $13.20 ｜ ATM IV 44.0%，净 delta 敞口 -281k shares
Top ΔOI: P 575 +938 ｜ C 708 +752 ｜ P 635 -530
仓位参考: Max Pain 695 ｜ Put Wall 635（-1.9%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 44.0%｜历史 Rank 100%（近端代理）｜IV/RV 1.93×（近似）｜净 delta 敞口 负 280,691 股

📆 11-11 Forward Structure
存量OI: C 21.9k / P 17.4k，今日变化ΔOI: C +6.1k / P +8.3k，平值价格ATM: C $16.09 / P $13.64 ｜ ATM IV 44.4%，净 delta 敞口 -510k shares
Top ΔOI: P 570 +998 ｜ P 674 +787
仓位参考: Max Pain 695 ｜ Put Wall 645（-0.3%，弱）（OI 1.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 44.4%｜历史 Rank 100%（近端代理）｜IV/RV 1.95×（近似）｜净 delta 敞口 负 510,415 股

📅 事件差分（观察，非因果）: 11-06（1D）ATM IV 58.5% vs 11-09 42.6%（差 +15.9pp）——覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=85 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=85）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-05/QQQ_evening.json