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
🟡 **近现价集中开仓**: 10-16 138C ΔOI +567（距现价 -2.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## NOW

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NOW: 今开 141.26 → 收盘 140.86（-0.3%） ｜ 今日高 142.47 ｜ 低 139.43 ｜ 昨收 139.75 → 收盘 140.86（+0.8%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.63 | OI比 0.70 | ATM IV 34.2% | Skew 6.3pp | Term 1.75 | ExpMove ±5.1%（近端） | Rank 0%
量化视角： IV 历史低位（Rank 0%，期权偏便宜）｜期限结构正常偏陡（Term 1.75）｜保护溢价显著（Skew 6.3pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.70）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.63×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.70×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（7D）±5.1% ｜ 10-23（14D）±7.2% ｜ 10-30（21D）±12.1% ｜ 11-06（28D）±6.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 26,972,013 | GEX Change vs 上次快照 2,668,500 | Flip: Primary Flip: 132.19（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 86%（带内） ｜ IV 有效性: VALID 472 / LOW 58 / INVALID 168
结构观察区: Primary Flip 132.19（全链重定价，覆盖 86%）
Call Wall 150（现价低于该位 6.1%）
最近结构参考: Call Wall 150（现价低于该位 6.1%）
量化视角： 正 Gamma（2697万，无历史分位）｜正 Gamma 增强（+267万）｜现价位于 Flip 上方 6.56%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 136（MaxPain，仅结算参考）；上方 150（Call Wall）。
• Gamma 区域：切换参考 132（全链重定价，覆盖 86%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +2.3k / P +0.9k ｜ Activity MEDIUM △ ｜ 7D
10-23  C +1.3k / P +1.2k ｜ Activity HIGH ｜ 14D
10-30  C +0.5k / P +0.4k ｜ Activity HIGH ｜ 21D
11-06  C +0.2k / P +0.3k ｜ Activity HIGH ｜ 28D

📆 10-16 Forward Structure
存量OI: C 85.3k / P 65.2k，今日变化ΔOI: C +2.3k / P +0.9k，平值价格ATM: C $3.49 / P $3.65 ｜ ATM IV 45.0%，净 delta 敞口 74k shares
Top ΔOI: C 150 +952 ｜ C 138 +567
仓位参考: Max Pain 130 ｜ Call Wall 150（+6.5%）（OI 15.9k） ｜ Put Wall 130（-7.7%，弱）（OI 4.5k）
量化解读： 存量 Call 重｜ATM IV 45.0%｜历史 Rank 0%（近端代理）｜IV/RV 1.56×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 74,003 股

📆 10-23 Forward Structure
存量OI: C 15.4k / P 18.2k，今日变化ΔOI: C +1.3k / P +1.2k，平值价格ATM: C $5.00 / P $5.10 ｜ ATM IV 46.3%，净 delta 敞口 17k shares
Top ΔOI: C 145 +485 ｜ P 142 +457 ｜ C 142 +413
仓位参考: Max Pain 135 ｜ Call Wall 140（-0.6%，弱）（OI 1.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 46.3%｜历史 Rank 0%（近端代理）｜IV/RV 1.60×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 17,276 股

📆 10-30 Forward Structure
存量OI: C 8.2k / P 10.2k，今日变化ΔOI: C +0.5k / P +0.4k，平值价格ATM: C $8.58 / P $8.51 ｜ ATM IV 62.8%，净 delta 敞口 17k shares
Top ΔOI: P 134 +83
仓位参考: Max Pain 134 ｜ Call Wall 150（+6.5%，弱）（OI 0.8k） ｜ Put Wall 130（-7.7%，弱）（OI 0.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 62.8%｜历史 Rank 0%（近端代理）｜IV/RV 2.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 16,700 股

📆 11-06 Forward Structure
存量OI: C 3.4k / P 2.3k，今日变化ΔOI: C +0.2k / P +0.3k，平值价格ATM: C $9.42 / P $0.00 ｜ ATM IV 60.0%，净 delta 敞口 -4k shares
Top ΔOI: P 139 +103 ｜ C 142 +39
仓位参考: Max Pain 137 ｜ Call Wall 140（-0.6%，弱）（OI 0.3k） ｜ Put Wall 130（-7.7%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 60.0%｜历史 Rank 0%（近端代理）｜IV/RV 2.08×（近似）｜净 delta 敞口 负 3,628 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-09/NOW_evening.json