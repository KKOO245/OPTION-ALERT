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
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🔴 **Vol Regime 升档**: ELEVATED → STRESS（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-13 8C ΔOI +893（距现价 -2.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 7.77 → 收盘 8.23（+5.9%） ｜ 今日高 8.29 ｜ 低 7.47 ｜ 昨收 7.42 → 收盘 8.23（+10.8%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-13，窗口结束前不做对错判定）

Options: P/C成交量 0.17 | OI比 0.32 | ATM IV 259.8% | Skew 0.4pp | Term 0.42 | ExpMove ±14.3%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.42，近月 IV 高于远月）｜保护溢价薄（Skew 0.4pp）｜存量 Call 偏重（OI比 0.32）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.17×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.32×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（7D）±14.3% ｜ 11-20（14D）±19.0% ｜ 11-27（21D）±21.2% ｜ 12-04（28D）±24.1%
   ⇒ IV–VIX Spread: +234.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 352,423 | GEX Change vs 上次快照 -822,367 | Flip: Candidates 7.92 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 80%（带内） ｜ IV 有效性: VALID 213 / LOW 51 / INVALID 150
结构观察区: ≈8（全链重定价，覆盖 80%，CONDITIONAL）
Put Wall 8（弱结构｜现价高于该位 2.8%）
最近结构参考: Put Wall 8（现价高于该位 2.8%）
量化视角： 正 Gamma（35万，无历史分位）｜正 Gamma 减弱（82万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 8（Put Wall，弱结构）；上方 8（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 8（全链重定价，覆盖 80%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +2.7k / P +0.2k ｜ Activity HIGH ｜ 7D
11-20  C +1.6k / P +1.8k ｜ Activity HIGH ｜ 14D
11-27  C +0.1k / P +66 ｜ Activity MEDIUM △ ｜ 21D
12-04  C +0.1k / P +0.1k ｜ Activity HIGH ｜ 28D

📆 11-13 Forward Structure
存量OI: C 13.9k / P 3.6k，今日变化ΔOI: C +2.7k / P +0.2k，平值价格ATM: C $0.70 / P $0.48 ｜ ATM IV 130.5%，净 delta 敞口 209k shares
Top ΔOI: C 7 +1,187 ｜ C 8 +893
仓位参考: Max Pain 8 ｜ Call Wall 8（-2.7%，弱）（OI 0.9k） ｜ Put Wall 9（+9.4%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 130.5%｜历史 Rank 100%（近端代理）｜IV/RV 1.36×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 208,638 股

📆 11-20 Forward Structure
存量OI: C 38.8k / P 32.1k，今日变化ΔOI: C +1.6k / P +1.8k，平值价格ATM: C $0.91 / P $0.65 ｜ ATM IV 120.9%，净 delta 敞口 183k shares
Top ΔOI: P 8 +4,090 ｜ P 10 -2,571 ｜ C 8 +1,459
仓位参考: Max Pain 11 ｜ Call Wall 9（+9.4%，弱）（OI 2.9k） ｜ Put Wall 8（-2.7%，弱）（OI 6.7k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 120.9%｜历史 Rank 100%（近端代理）｜IV/RV 1.26×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 182,759 股

11-27（MEDIUM △）Top ΔOI: 9P +261 ｜ 15P -202
11-27（MEDIUM △）仓位参考: Max Pain 10 ｜ Put Wall 9（+9.4%，弱）（OI 0.4k）

📆 12-04 Forward Structure
存量OI: C 1.7k / P 1.3k，今日变化ΔOI: C +0.1k / P +0.1k，平值价格ATM: C $1.08 / P $0.90 ｜ ATM IV 108.7%，净 delta 敞口 9k shares
Top ΔOI: C 7 +47
仓位参考: Max Pain 10 ｜ Put Wall 8.5（+3.3%，弱）（OI 0.1k）
量化解读： 存量 Call 重｜ATM IV 108.7%｜历史 Rank 100%（近端代理）｜IV/RV 1.13×（近似）｜净 delta 敞口 正 9,109 股

📅 事件差分（观察，非因果）: 11-13（7D）ATM IV 130.5% vs 11-20 120.9%（差 +9.6pp）——覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-06/USAR_evening.json