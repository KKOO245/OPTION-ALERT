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


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 416.39 → 收盘 423.96（+1.8%） ｜ 今日高 427.53 ｜ 低 415.86 ｜ 昨收 415.41 → 收盘 423.96（+2.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.31 | OI比 0.98 | ATM IV 29.7% | Skew 2.8pp | Term 1.58 | ExpMove ±3.4%（近端） | Rank 0%
量化视角： IV 历史低位（Rank 0%，期权偏便宜）｜期限结构正常偏陡（Term 1.58）｜保护溢价中性（Skew 2.8pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.31×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.98×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（7D）±3.4% ｜ 10-23（14D）±8.6% ｜ 10-30（21D）±9.5% ｜ 11-06（28D）±10.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,392,875 | GEX Change vs 上次快照 -1,766,112 | Flip: Primary Flip: 401.30（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 246 / LOW 110 / INVALID 354
结构观察区: Primary Flip 401.30（全链重定价，覆盖 91%）
Call Wall 400（弱结构｜现价高于该位 6.0%）
最近结构参考: Flip 401（现价高于该位 5.6%）
量化视角： 正 Gamma（239万，无历史分位）｜正 Gamma 减弱（177万）｜现价位于 Flip 上方 5.65%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 390（MaxPain，仅结算参考） / 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 401（全链重定价，覆盖 91%）。
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
存量OI: C 10.8k / P 10.6k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $7.23 / P $7.30 ｜ ATM IV 29.7%，净 delta 敞口 0 shares
仓位参考: Max Pain 390 ｜ Call Wall 400（-5.7%，弱）（OI 0.9k） ｜ Put Wall 400（-5.7%，弱）（OI 0.5k）
量化解读： 存量两侧均衡｜ATM IV 29.7%｜历史 Rank 0%（近端代理）｜IV/RV 1.22×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

10-23（Activity LOW）仓位参考: Max Pain 415 ｜ Call Wall 425（+0.2%）（OI 0.5k） ｜ Put Wall 415（-2.1%）（OI 0.5k）

10-30（Activity LOW）仓位参考: Max Pain 395 ｜ Call Wall 460（+8.5%，弱）（OI 94） ｜ Put Wall 400（-5.7%，弱）（OI 45）

11-06（Activity LOW）仓位参考: Max Pain 400 ｜ Call Wall 455（+7.3%，弱）（OI 49） ｜ Put Wall 400（-5.7%，弱）（OI 35）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-09/ISRG_evening.json