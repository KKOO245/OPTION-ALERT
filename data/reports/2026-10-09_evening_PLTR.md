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


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 201.06 → 收盘 209.05（+4.0%） ｜ 今日高 209.31 ｜ 低 198.30 ｜ 昨收 198.78 → 收盘 209.05（+5.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.61 | OI比 1.26 | ATM IV 41.7% | Skew -0.4pp | Term 1.37 | ExpMove ±4.6%（近端） | Rank 10%
量化视角： IV 历史低位（Rank 10%，期权偏便宜）｜期限结构正常偏陡（Term 1.37）｜Put 保护异常便宜（Skew -0.4pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.61×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.26×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-16（7D）±4.6% ｜ 10-23（14D）±6.5% ｜ 10-30（21D）±8.2% ｜ 11-06（28D）±12.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 47,079,392 | GEX Change vs 上次快照 -86,909,020 | Flip: Primary Flip: 182.25（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 530 / LOW 62 / INVALID 80
结构观察区: Primary Flip 182.25（全链重定价，覆盖 100%）
Call Wall 200（弱结构｜现价高于该位 4.5%）
最近结构参考: Call Wall 200（现价高于该位 4.5%）
量化视角： 正 Gamma（4708万，无历史分位）｜正 Gamma 减弱（8691万）｜现价位于 Flip 上方 14.70%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 170（MaxPain，仅结算参考） / 200（Call Wall，弱结构）。
• Gamma 区域：切换参考 182（全链重定价，覆盖 100%）。
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
存量OI: C 169.0k / P 212.1k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $4.40 / P $5.23 ｜ ATM IV 41.7%，净 delta 敞口 0 shares
仓位参考: Max Pain 170 ｜ Call Wall 200（-4.3%，弱）（OI 16.9k） ｜ Put Wall 190（-9.1%，弱）（OI 6.1k）
量化解读： 存量 Put 重｜ATM IV 41.7%｜历史 Rank 10%（近端代理）｜IV/RV 2.02×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

10-23（Activity LOW）仓位参考: Max Pain 180 ｜ Call Wall 200（-4.3%，弱）（OI 3.5k） ｜ Put Wall 190（-9.1%，弱）（OI 1.2k）

10-30（Activity LOW）仓位参考: Max Pain 185 ｜ Call Wall 192.5（-7.9%，弱）（OI 2.7k） ｜ Put Wall 190（-9.1%，弱）（OI 2.1k）

11-06（Activity LOW）仓位参考: Max Pain 190 ｜ Call Wall 215（+2.8%，弱）（OI 1.0k） ｜ Put Wall 190（-9.1%）（OI 3.0k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-09/PLTR_evening.json