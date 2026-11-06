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
🟡 **近现价集中开仓**: 11-13 135C ΔOI +5,954（距现价 +4.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 127.83 → 收盘 128.93（+0.9%） ｜ 今日高 130.64 ｜ 低 125.59 ｜ 昨收 129.30 → 收盘 128.93（-0.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.29 | OI比 0.58 | ATM IV 49.5% | Skew 0.4pp | Term 1.51 | ExpMove ±9.3%（近端） | Rank 2%
量化视角： IV 历史低位（Rank 2%，期权偏便宜）｜期限结构正常偏陡（Term 1.51）｜保护溢价薄（Skew 0.4pp）｜存量 Call 偏重（OI比 0.58）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.29×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.58×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（7D）±9.3% ｜ 11-20（14D）±12.4% ｜ 11-27（21D）±14.5% ｜ 12-04（28D）±16.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 28,711,320 | GEX Change vs 上次快照 -9,128,602 | Flip: Candidates 114.29 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 73%（带内） ｜ IV 有效性: VALID 418 / LOW 114 / INVALID 312
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: ≈114（全链重定价，覆盖 73%，CONDITIONAL）
Call Wall 135（现价低于该位 4.5%）
最近结构参考: Call Wall 135（现价低于该位 4.5%）
量化视角： 正 Gamma（2871万，无历史分位）｜正 Gamma 减弱（913万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 131（MaxPain，仅结算参考） / 135（Call Wall）。
• Gamma 区域：切换参考 114（全链重定价，覆盖 73%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +16.1k / P +8.8k ｜ Activity HIGH ｜ 7D
11-20  C +1.4k / P +0.6k ｜ Activity MEDIUM △ ｜ 14D
11-27  C +1.5k / P +3.6k ｜ Activity HIGH ｜ 21D
12-04  C +0.8k / P +2.4k ｜ Activity HIGH ｜ 28D

📆 11-13 Forward Structure
存量OI: C 51.4k / P 91.3k，今日变化ΔOI: C +16.1k / P +8.8k，平值价格ATM: C $6.20 / P $5.80 ｜ ATM IV 83.0%，净 delta 敞口 283k shares
Top ΔOI: C 135 +5,954 ｜ C 141 +2,558 ｜ C 142 +2,550
仓位参考: Max Pain 142 ｜ Call Wall 135（+4.7%）（OI 6.3k） ｜ Put Wall 125（-3.0%，弱）（OI 3.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 83.0%｜历史 Rank 2%（近端代理）｜IV/RV 1.04×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 282,589 股

11-20（MEDIUM △）Top ΔOI: 135P -1,199 ｜ 95P +962
11-20（MEDIUM △）仓位参考: Max Pain 135 ｜ Call Wall 135（+4.7%）（OI 43.0k） ｜ Put Wall 120（-6.9%，弱）（OI 7.3k）

📆 11-27 Forward Structure
存量OI: C 13.8k / P 34.7k，今日变化ΔOI: C +1.5k / P +3.6k，平值价格ATM: C $8.90 / P $9.82 ｜ ATM IV 75.1%，净 delta 敞口 -80k shares
Top ΔOI: P 120 +1,535 ｜ P 100 +1,456 ｜ C 165 +583
仓位参考: Max Pain 155 ｜ Call Wall 140（+8.6%，弱）（OI 0.6k） ｜ Put Wall 140（+8.6%，弱）（OI 2.8k）
量化解读： 存量 Put 重｜ATM IV 75.1%｜历史 Rank 2%（近端代理）｜IV/RV 0.94×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 79,788 股

📆 12-04 Forward Structure
存量OI: C 14.2k / P 16.9k，今日变化ΔOI: C +0.8k / P +2.4k，平值价格ATM: C $10.25 / P $11.13 ｜ ATM IV 75.0%，净 delta 敞口 -81k shares
Top ΔOI: P 95 +419
仓位参考: Max Pain 150 ｜ Call Wall 140（+8.6%，弱）（OI 3.0k） ｜ Put Wall 140（+8.6%，弱）（OI 1.6k）
量化解读： 存量 Put 重｜ATM IV 75.0%｜历史 Rank 2%（近端代理）｜IV/RV 0.94×（近似）｜净 delta 敞口 负 80,985 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-06/MSTR_evening.json