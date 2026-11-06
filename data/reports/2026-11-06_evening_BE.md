# 期权晚报 2026-11-06（快照 16:40 ET）

📊 市场环境

SPY $735.29 ｜ QQQ $656.10
VIX 25.64 ↓9.0%（5D +32.0%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 22.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-06

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 165 ｜ 前值 60　✅ 今日已公布
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 4.1 ｜ 前值 4.2　✅ 今日已公布
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 51 ｜ 前值 46.3　✅ 今日已公布

🔍 重点速览
🔴 **Vol Regime 升档**: ELEVATED → STRESS（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-13 180C ΔOI +2,116（距现价 +3.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 12-04 140P ΔOI -1,283 占该期限总 OI 11.9%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 183.31 → 收盘 173.24（-5.5%） ｜ 今日高 186.33 ｜ 低 168.84 ｜ 昨收 167.52 → 收盘 173.24（+3.4%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-11，窗口结束前不做对错判定）

Options: P/C成交量 0.78 | OI比 0.45 | ATM IV 126.6% | Skew 12.6pp | Term 0.78 | ExpMove ±13.3%（近端） | Rank 81%
量化视角： IV 历史高位（Rank 81%，期权偏贵）｜期限结构倒挂（Term 0.78，近月 IV 高于远月）｜保护溢价显著（Skew 12.6pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.45）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.78×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.45×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（7D）±13.3% ｜ 11-20（14D）±17.3% ｜ 11-27（21D）±19.4% ｜ 12-04（28D）±21.6%
   ⇒ IV–VIX Spread: +100.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -3,330,992 | GEX Change vs 上次快照 -2,977,049 | Flip: Primary Flip: 194.96（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 80%（带内） ｜ IV 有效性: VALID 453 / LOW 107 / INVALID 402
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 194.96（全链重定价，覆盖 80%）
最近结构参考: Flip 195（现价低于该位 11.1%）
量化视角： 负 Gamma（333万，无历史分位）｜负 Gamma 加深（298万）｜现价位于 Flip 下方 11.14%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 188（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 195（全链重定价，覆盖 80%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +9.4k / P +2.9k ｜ Activity HIGH ｜ 7D
11-20  C +6.7k / P +2.5k ｜ Activity HIGH ｜ 14D
11-27  C +1.3k / P -0.5k ｜ Activity HIGH ｜ 21D
12-04  C +0.3k / P -0.9k ｜ Activity MEDIUM △ ｜ 28D

📆 11-13 Forward Structure
存量OI: C 24.4k / P 17.2k，今日变化ΔOI: C +9.4k / P +2.9k，平值价格ATM: C $12.05 / P $11.00 ｜ ATM IV 120.7%，净 delta 敞口 581k shares
Top ΔOI: C 180 +2,116 ｜ C 130 +1,350 ｜ C 140 +1,262
仓位参考: Max Pain 185 ｜ Call Wall 180（+3.9%）（OI 2.2k） ｜ Put Wall 165（-4.8%，弱）（OI 1.2k）
量化解读： 存量 Call 重｜ATM IV 120.7%｜历史 Rank 81%（近端代理）｜IV/RV 1.08×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 581,028 股

📆 11-20 Forward Structure
存量OI: C 71.9k / P 78.0k，今日变化ΔOI: C +6.7k / P +2.5k，平值价格ATM: C $15.55 / P $14.37 ｜ ATM IV 110.8%，净 delta 敞口 401k shares
Top ΔOI: P 145 +2,768 ｜ P 140 +1,932 ｜ C 190 +1,308
仓位参考: Max Pain 220 ｜ Call Wall 190（+9.7%，弱）（OI 2.2k） ｜ Put Wall 170（-1.9%，弱）（OI 4.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 110.8%｜历史 Rank 81%（近端代理）｜IV/RV 1.00×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 401,347 股

📆 11-27 Forward Structure
存量OI: C 8.0k / P 8.9k，今日变化ΔOI: C +1.3k / P -0.5k，平值价格ATM: C $16.95 / P $16.74 ｜ ATM IV 101.9%，净 delta 敞口 89k shares
Top ΔOI: P 200 -774 ｜ C 200 +355 ｜ C 220 +275
仓位参考: Max Pain 220 ｜ Put Wall 190（+9.7%，弱）（OI 1.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 101.9%｜历史 Rank 81%（近端代理）｜IV/RV 0.92×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 89,413 股

12-04（MEDIUM △）Top ΔOI: 140P -1,283 ｜ 150P +121
12-04（MEDIUM △）仓位参考: Max Pain 210 ｜ Put Wall 190（+9.7%，弱）（OI 0.3k）

📅 事件差分（观察，非因果）: 11-13（7D）ATM IV 120.7% vs 11-20 110.8%（差 +9.9pp）——覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=85 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=85）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-06/BE_evening.json