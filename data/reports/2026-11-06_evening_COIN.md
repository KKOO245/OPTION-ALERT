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
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🔴 **Vol Regime 升档**: ELEVATED → STRESS（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-13 135P ΔOI +639（距现价 +0.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 136.51 → 收盘 134.76（-1.3%） ｜ 今日高 139.28 ｜ 低 131.55 ｜ 昨收 136.82 → 收盘 134.76（-1.5%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-11，窗口结束前不做对错判定）

Options: P/C成交量 0.34 | OI比 0.69 | ATM IV 62.6% | Skew -0.5pp | Term 1.11 | ExpMove ±8.2%（近端） | Rank 15%
量化视角： IV 历史低位（Rank 15%，期权偏便宜）｜期限结构正常（Term 1.11）｜Put 保护异常便宜（Skew -0.5pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.69）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.34×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.69×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（7D）±8.2% ｜ 11-20（14D）±11.3% ｜ 11-27（21D）±13.3% ｜ 12-04（28D）±15.5%
   ⇒ IV–VIX Spread: +37.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,941,370 | GEX Change vs 上次快照 -11,858,543 | Flip: Candidates 136.95 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 70%（带内） ｜ IV 有效性: VALID 342 / LOW 155 / INVALID 371
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: ≈137（全链重定价，覆盖 70%，CONDITIONAL）
最近结构参考: Flip 137（现价低于该位 1.6%）
量化视角： 负 Gamma（194万，无历史分位）｜由正转负（1186万）｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 141（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 137（全链重定价，覆盖 70%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +3.3k / P +2.7k ｜ Activity HIGH ｜ 7D
11-20  C +3.0k / P -1.5k ｜ Activity HIGH ｜ 14D
11-27  C +0.3k / P -0.8k ｜ Activity HIGH ｜ 21D
12-04  C +98 / P +1.2k ｜ Activity HIGH ｜ 28D

📆 11-13 Forward Structure
存量OI: C 17.9k / P 27.1k，今日变化ΔOI: C +3.3k / P +2.7k，平值价格ATM: C $5.44 / P $5.55 ｜ ATM IV 73.3%，净 delta 敞口 -1k shares
Top ΔOI: C 144 +751 ｜ P 135 +639
仓位参考: Max Pain 150 ｜ Call Wall 144（+6.9%，弱）（OI 0.9k） ｜ Put Wall 130（-3.5%，弱）（OI 1.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 73.3%｜历史 Rank 15%（近端代理）｜IV/RV 0.99×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,158 股

📆 11-20 Forward Structure
存量OI: C 76.7k / P 59.3k，今日变化ΔOI: C +3.0k / P -1.5k，平值价格ATM: C $7.54 / P $7.68 ｜ ATM IV 72.0%，净 delta 敞口 317k shares
Top ΔOI: P 200 -1,768 ｜ P 110 +1,702
仓位参考: Max Pain 165 ｜ Put Wall 140（+3.9%，弱）（OI 3.4k）
量化解读： 存量 Call 重｜ATM IV 72.0%｜历史 Rank 15%（近端代理）｜IV/RV 0.98×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 316,956 股

📆 11-27 Forward Structure
存量OI: C 4.0k / P 6.9k，今日变化ΔOI: C +0.3k / P -0.8k，平值价格ATM: C $9.05 / P $8.85 ｜ ATM IV 68.5%，净 delta 敞口 10k shares
仓位参考: Max Pain 155 ｜ Call Wall 140（+3.9%，弱）（OI 95） ｜ Put Wall 140（+3.9%，弱）（OI 0.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 68.5%｜历史 Rank 15%（近端代理）｜IV/RV 0.93×（近似）｜净 delta 敞口 正 9,683 股

📆 12-04 Forward Structure
存量OI: C 4.2k / P 5.6k，今日变化ΔOI: C +98 / P +1.2k，平值价格ATM: C $10.66 / P $10.17 ｜ ATM IV 69.7%，净 delta 敞口 -60k shares
Top ΔOI: P 135 +1,285
仓位参考: Max Pain 140 ｜ Call Wall 140（+3.9%）（OI 1.3k） ｜ Put Wall 135（+0.2%）（OI 1.5k）
量化解读： 存量 Put 重｜ATM IV 69.7%｜历史 Rank 15%（近端代理）｜IV/RV 0.94×（近似）｜净 delta 敞口 负 59,705 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=85 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=85）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-06/COIN_evening.json