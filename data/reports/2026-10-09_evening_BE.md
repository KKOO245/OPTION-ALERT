# 期权晚报 2026-10-09（快照 16:40 ET）

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

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-16 275C ΔOI +827（距现价 -2.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 275.85 → 收盘 280.50（+1.7%） ｜ 今日高 280.50 ｜ 低 271.03 ｜ 昨收 272.82 → 收盘 280.50（+2.8%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.75 | OI比 1.03 | ATM IV 71.5% | Skew -3.7pp | Term 1.12 | ExpMove ±6.9%（近端） | Rank 28%
量化视角： IV 中性（Rank 28%）｜期限结构正常（Term 1.12）｜Put 保护异常便宜（Skew -3.7pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.75×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.03×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（7D）±6.9% ｜ 10-23（14D）±10.0% ｜ 10-30（21D）±14.7% ｜ 11-06（28D）±17.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 5,023,877 | GEX Change vs 上次快照 4,759,312 | Flip: Primary Flip: 272.61（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 85%（带内） ｜ IV 有效性: VALID 484 / LOW 99 / INVALID 287
结构观察区: Primary Flip 272.61（全链重定价，覆盖 85%）
Call Wall 300（弱结构｜现价低于该位 6.5%）
最近结构参考: Flip 273（现价高于该位 2.9%）
量化视角： 正 Gamma（502万，无历史分位）｜正 Gamma 增强（+476万）｜现价位于 Flip 上方 2.90%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 280（MaxPain，仅结算参考）；上方 300（Call Wall，弱结构）。
• Gamma 区域：切换参考 273（全链重定价，覆盖 85%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +5.4k / P +3.5k ｜ Activity HIGH ｜ 7D
10-23  C +0.7k / P +1.4k ｜ Activity HIGH ｜ 14D
10-30  C +0.9k / P +0.2k ｜ Activity HIGH ｜ 21D
11-06  C +1.0k / P +1.3k ｜ Activity HIGH ｜ 28D

📆 10-16 Forward Structure
存量OI: C 86.7k / P 96.8k，今日变化ΔOI: C +5.4k / P +3.5k，平值价格ATM: C $9.90 / P $9.50 ｜ ATM IV 62.8%，净 delta 敞口 338k shares
Top ΔOI: P 360 -1,205 ｜ C 275 +827 ｜ C 285 +689
仓位参考: Max Pain 270 ｜ Call Wall 270（-3.7%，弱）（OI 7.0k） ｜ Put Wall 260（-7.3%，弱）（OI 4.7k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 62.8%｜历史 Rank 28%（近端代理）｜IV/RV 0.84×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 338,133 股

📆 10-23 Forward Structure
存量OI: C 15.2k / P 18.1k，今日变化ΔOI: C +0.7k / P +1.4k，平值价格ATM: C $13.78 / P $14.24 ｜ ATM IV 62.4%，净 delta 敞口 20k shares
Top ΔOI: P 250 +490
仓位参考: Max Pain 270 ｜ Call Wall 300（+7.0%，弱）（OI 1.2k） ｜ Put Wall 280（-0.2%，弱）（OI 0.7k）
量化解读： 存量 Put 重｜ATM IV 62.4%｜历史 Rank 28%（近端代理）｜IV/RV 0.84×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 20,186 股

📆 10-30 Forward Structure
存量OI: C 10.8k / P 19.9k，今日变化ΔOI: C +0.9k / P +0.2k，平值价格ATM: C $20.50 / P $20.63 ｜ ATM IV 76.8%，净 delta 敞口 41k shares
Top ΔOI: C 320 +463 ｜ P 210 -341
仓位参考: Max Pain 280 ｜ Call Wall 300（+7.0%，弱）（OI 1.5k） ｜ Put Wall 285（+1.6%，弱）（OI 1.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 76.8%｜历史 Rank 28%（近端代理）｜IV/RV 1.03×（近似）｜净 delta 敞口 正 40,825 股

📆 11-06 Forward Structure
存量OI: C 4.0k / P 10.2k，今日变化ΔOI: C +1.0k / P +1.3k，平值价格ATM: C $25.00 / P $24.88 ｜ ATM IV 80.3%，净 delta 敞口 8k shares
Top ΔOI: C 355 +332 ｜ P 215 +186 ｜ P 220 +174
仓位参考: Max Pain 275 ｜ Call Wall 300（+7.0%，弱）（OI 0.2k）
量化解读： 存量 Put 重｜ATM IV 80.3%｜历史 Rank 28%（近端代理）｜IV/RV 1.08×（近似）｜净 delta 敞口 正 7,563 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-09/BE_evening.json