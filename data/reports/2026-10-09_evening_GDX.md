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


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 88.64 → 收盘 89.28（+0.7%） ｜ 今日高 89.63 ｜ 低 88.25 ｜ 昨收 86.72 → 收盘 89.28（+3.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.29 | OI比 0.82 | ATM IV 37.3% | Skew 0.5pp | Term 1.09 | ExpMove ±4.2%（近端） | Rank 45%
量化视角： IV 中性（Rank 45%）｜期限结构正常（Term 1.09）｜保护溢价薄（Skew 0.5pp）｜存量 Call 偏重（OI比 0.82）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.29×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.82×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（7D）±4.2% ｜ 10-19（10D）±4.7% ｜ 10-21（12D）±5.6% ｜ 10-23（14D）±5.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 14,351,955 | GEX Change vs 上次快照 -88,329,663 | Flip: Primary Flip: 87.15（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 424 / LOW 99 / INVALID 299
结构观察区: Primary Flip 87.15（全链重定价，覆盖 97%）
最近结构参考: Flip 87（现价高于该位 2.4%）
量化视角： 正 Gamma（1435万，无历史分位）｜正 Gamma 减弱（8833万）｜现价位于 Flip 上方 2.44%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 89（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 87（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +0 / P +0 ｜ Activity LOW ｜ 7D
10-19  C +0 / P +0 ｜ Activity LOW ｜ 10D
10-21  C +0 / P +0 ｜ Activity LOW ｜ 12D
10-23  C +0 / P +0 ｜ Activity LOW ｜ 14D

📆 10-16 Forward Structure
存量OI: C 139.0k / P 114.5k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $1.79 / P $1.95 ｜ ATM IV 37.3%，净 delta 敞口 0 shares
仓位参考: Max Pain 89 ｜ Call Wall 88.5（-0.9%，弱）（OI 11.2k） ｜ Put Wall 90（+0.8%，弱）（OI 10.4k）
量化解读： 存量 Call 重｜ATM IV 37.3%｜历史 Rank 45%（近端代理）｜IV/RV 1.05×（近似）｜净 delta 敞口 正 0 股

10-19（Activity LOW）仓位参考: Max Pain 86 ｜ Call Wall 92（+3.0%）（OI 0.4k） ｜ Put Wall 90（+0.8%，弱）（OI 23）

10-21（Activity LOW）仓位参考: Max Pain 84 ｜ Call Wall 95（+6.4%）（OI 0.4k）

10-23（Activity LOW）仓位参考: Max Pain 92 ｜ Call Wall 90（+0.8%，弱）（OI 0.6k） ｜ Put Wall 90（+0.8%，弱）（OI 1.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-09/GDX_evening.json