# 期权晚报 2026-11-06（快照 21:00 ET）

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

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 10.25 → 收盘 11.11（+8.4%） ｜ 今日高 11.28 ｜ 低 9.90 ｜ 昨收 9.64 → 收盘 11.11（+15.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.54 | OI比 0.83 | ATM IV 89.7% | Skew -4.4pp | Term 0.97 | ExpMove ±10.5%（近端） | Rank 24%
量化视角： IV 历史低位（Rank 24%，期权偏便宜）｜期限结构正常（Term 0.97）｜Put 保护异常便宜（Skew -4.4pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.83）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.54×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.83×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-13（7D）±10.5% ｜ 11-20（14D）±13.5% ｜ 11-27（21D）±24.5% ｜ 12-04（28D）±4.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 581,869 | GEX Change vs 上次快照 -199,068 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 132 / LOW 63 / INVALID 141
结构观察区: NO_CROSS
Put Wall 11（弱结构｜现价高于该位 1.0%）
最近结构参考: Put Wall 11（现价高于该位 1.0%）
量化视角： 正 Gamma（58万，无历史分位）｜正 Gamma 减弱（20万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 11（Put Wall，弱结构）；上方 12（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +0 / P +0 ｜ Activity LOW ｜ 7D
11-20  C +0 / P +0 ｜ Activity LOW ｜ 14D
11-27  C +0 / P +0 ｜ Activity LOW ｜ 21D
12-04  C +0 / P +0 ｜ Activity LOW ｜ 28D

📆 11-13 Forward Structure
存量OI: C 1.4k / P 1.2k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $0.62 / P $0.55 ｜ ATM IV 89.8%，净 delta 敞口 0 shares
仓位参考: Max Pain 12 ｜ Call Wall 12（+8.0%，弱）（OI 0.1k） ｜ Put Wall 11（-1.0%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 89.8%｜历史 Rank 24%（近端代理）｜IV/RV 1.22×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-20（Activity LOW）仓位参考: Max Pain 15 ｜ Put Wall 10（-10.0%，弱）（OI 0.3k）

11-27（Activity LOW）仓位参考: Max Pain 12

12-04（Activity LOW）仓位参考: Max Pain 14 ｜ Call Wall 10（-10.0%，弱）（OI 6）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-06/NNE_evening.json