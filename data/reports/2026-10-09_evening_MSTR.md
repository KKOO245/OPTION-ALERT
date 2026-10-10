# 期权晚报 2026-10-09（快照 21:00 ET）

📊 市场环境

SPY $778.57 ｜ QQQ $751.27
VIX 14.84 ↓3.7%（5D -3.1%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 45.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-09

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 46.3 ｜ 前值 48.1　✅ 今日已公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 154.37 → 收盘 154.34（-0.0%） ｜ 今日高 158.11 ｜ 低 150.50 ｜ 昨收 151.47 → 收盘 154.34（+1.9%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.28 | OI比 0.91 | ATM IV 57.7% | Skew -3.1pp | Term 1.09 | ExpMove ±6.4%（近端） | Rank 10%
量化视角： IV 历史低位（Rank 10%，期权偏便宜）｜期限结构正常（Term 1.09）｜Put 保护异常便宜（Skew -3.1pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.28×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.91×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（7D）±6.4% ｜ 10-23（14D）±9.0% ｜ 10-30（21D）±11.8% ｜ 11-06（28D）±14.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 17,446,719 | GEX Change vs 上次快照 -5,603,434 | Flip: Primary Flip: 147.00（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 554 / LOW 61 / INVALID 135
结构观察区: Primary Flip 147.00（全链重定价，覆盖 100%）
最近结构参考: Flip 147（现价高于该位 5.0%）
量化视角： 正 Gamma（1745万，无历史分位）｜正 Gamma 减弱（560万）｜现价位于 Flip 上方 4.99%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 140（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 147（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +0 / P +0 ｜ Activity LOW ｜ 7D
10-23  C +0 / P +0 ｜ Activity LOW ｜ 14D
10-30  C +0 / P +0 ｜ Activity LOW ｜ 21D
11-06  C +0 / P +0 ｜ Activity LOW ｜ 28D

📆 10-16 Forward Structure
存量OI: C 221.6k / P 201.8k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $4.64 / P $5.27 ｜ ATM IV 57.7%，净 delta 敞口 0 shares
仓位参考: Max Pain 140 ｜ Call Wall 155（+0.4%，弱）（OI 17.1k） ｜ Put Wall 142（-8.0%，弱）（OI 7.0k）
量化解读： 存量两侧均衡｜ATM IV 57.7%｜历史 Rank 10%（近端代理）｜IV/RV 0.78×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

10-23（Activity LOW）仓位参考: Max Pain 160 ｜ Call Wall 165（+6.9%，弱）（OI 2.4k） ｜ Put Wall 160（+3.7%）（OI 6.1k）

10-30（Activity LOW）仓位参考: Max Pain 160 ｜ Call Wall 162.5（+5.3%，弱）（OI 2.6k） ｜ Put Wall 160（+3.7%，弱）（OI 3.3k）

11-06（Activity LOW）仓位参考: Max Pain 160 ｜ Call Wall 160（+3.7%）（OI 1.2k） ｜ Put Wall 160（+3.7%，弱）（OI 2.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-09/MSTR_evening.json