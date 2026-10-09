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
🟡 **近现价集中开仓**: 10-16 210C ΔOI +1,929（距现价 +0.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 201.06 → 收盘 209.05（+4.0%） ｜ 今日高 209.31 ｜ 低 198.30 ｜ 昨收 198.78 → 收盘 209.05（+5.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.51 | OI比 0.56 | ATM IV 37.5% | Skew 10.0pp | Term 1.52 | ExpMove ±4.6%（近端） | Rank 2%
量化视角： IV 历史低位（Rank 2%，期权偏便宜）｜期限结构正常偏陡（Term 1.52）｜保护溢价显著（Skew 10.0pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.56）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.51×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.56×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（7D）±4.6% ｜ 10-23（14D）±6.5% ｜ 10-30（21D）±8.2% ｜ 11-06（28D）±12.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 102,460,577 | GEX Change vs 上次快照 -31,527,835 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 546 / LOW 86 / INVALID 186
结构观察区: NO_CROSS
Call Wall 205（弱结构｜现价高于该位 2.0%）
最近结构参考: Call Wall 205（现价高于该位 2.0%）
量化视角： 正 Gamma（1.02亿，无历史分位）｜正 Gamma 减弱（3153万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 190（MaxPain，仅结算参考） / 205（Call Wall，弱结构）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +7.1k / P +15.0k ｜ Activity HIGH ｜ 7D
10-23  C +3.7k / P +7.3k ｜ Activity HIGH ｜ 14D
10-30  C +1.6k / P +2.3k ｜ Activity HIGH ｜ 21D
11-06  C +2.6k / P +1.5k ｜ Activity HIGH ｜ 28D

📆 10-16 Forward Structure
存量OI: C 169.0k / P 212.1k，今日变化ΔOI: C +7.1k / P +15.0k，平值价格ATM: C $4.40 / P $5.23 ｜ ATM IV 41.7%，净 delta 敞口 61k shares
Top ΔOI: P 197 +2,714 ｜ C 210 +1,929
仓位参考: Max Pain 170 ｜ Call Wall 200（-4.3%，弱）（OI 16.9k） ｜ Put Wall 190（-9.1%，弱）（OI 6.1k）
量化解读： 存量 Put 重｜ATM IV 41.7%｜历史 Rank 2%（近端代理）｜IV/RV 2.02×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 60,589 股

📆 10-23 Forward Structure
存量OI: C 29.9k / P 27.6k，今日变化ΔOI: C +3.7k / P +7.3k，平值价格ATM: C $6.42 / P $7.10 ｜ ATM IV 41.5%，净 delta 敞口 94k shares
Top ΔOI: C 220 +672 ｜ P 195 +594
仓位参考: Max Pain 180 ｜ Call Wall 200（-4.3%，弱）（OI 3.5k） ｜ Put Wall 190（-9.1%，弱）（OI 1.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 41.5%｜历史 Rank 2%（近端代理）｜IV/RV 2.01×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 94,022 股

📆 10-30 Forward Structure
存量OI: C 29.8k / P 22.4k，今日变化ΔOI: C +1.6k / P +2.3k，平值价格ATM: C $8.30 / P $8.80 ｜ ATM IV 42.7%，净 delta 敞口 -20k shares
Top ΔOI: P 190 +783 ｜ C 235 +466 ｜ C 200 -458
仓位参考: Max Pain 185 ｜ Call Wall 192.5（-7.9%，弱）（OI 2.7k） ｜ Put Wall 190（-9.1%，弱）（OI 2.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 42.7%｜历史 Rank 2%（近端代理）｜IV/RV 2.06×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 20,195 股

📆 11-06 Forward Structure
存量OI: C 11.1k / P 12.4k，今日变化ΔOI: C +2.6k / P +1.5k，平值价格ATM: C $13.00 / P $13.55 ｜ ATM IV 57.1%，净 delta 敞口 76k shares
Top ΔOI: C 215 +502 ｜ C 205 +416 ｜ P 200 +377
仓位参考: Max Pain 190 ｜ Call Wall 215（+2.8%，弱）（OI 1.0k） ｜ Put Wall 190（-9.1%）（OI 3.0k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 57.1%｜历史 Rank 2%（近端代理）｜IV/RV 2.77×（近似）｜净 delta 敞口 正 76,026 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-09/PLTR_evening.json