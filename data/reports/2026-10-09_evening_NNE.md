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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 15.40 → 收盘 15.34（-0.4%） ｜ 今日高 15.46 ｜ 低 14.92 ｜ 昨收 15.26 → 收盘 15.34（+0.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 6.12 | OI比 0.34 | ATM IV 109.9% | Skew 2.1pp | Term 0.64 | ExpMove ±7.8%（近端） | Rank 55%
量化视角： IV 中性（Rank 55%）｜期限结构倒挂（Term 0.64，近月 IV 高于远月）｜保护溢价中性（Skew 2.1pp）｜⚠️ 重点观察：存量 Call 重（OI比 0.34）+ 当日成交偏 Put（P/C量 6.12）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 6.12×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.34×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（7D）±7.8% ｜ 10-23（14D）±13.8% ｜ 10-30（21D）±13.7% ｜ 11-06（28D）±14.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 1,516,491 | GEX Change vs 上次快照 245,911 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 78%（带内） ｜ IV 有效性: VALID 142 / LOW 104 / INVALID 182
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: NO_CROSS
Put Wall 15（现价高于该位 2.3%）
最近结构参考: Put Wall 15（现价高于该位 2.3%）
量化视角： 正 Gamma（152万，无历史分位）｜正 Gamma 增强（+25万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall）；上方 16（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +15 / P -0.2k ｜ Activity MEDIUM △ ｜ 7D
10-23  C +63 / P +63 ｜ Activity HIGH ｜ 14D
10-30  C +81 / P +52 ｜ Activity MEDIUM △ ｜ 21D
11-06  C +46 / P +55 ｜ Activity MEDIUM △ ｜ 28D

📆 10-16 Forward Structure
存量OI: C 21.8k / P 5.4k，今日变化ΔOI: C +15 / P -0.2k，平值价格ATM: C $0.39 / P $0.80 ｜ ATM IV 65.2%，净 delta 敞口 47k shares
Top ΔOI: P 14 +345 ｜ P 29 -337 ｜ P 25 -145
仓位参考: Max Pain 18 ｜ Put Wall 15（-2.2%，弱）（OI 1.0k）
量化解读： 存量 Call 重｜ATM IV 65.2%｜历史 Rank 55%（近端代理）｜IV/RV 1.03×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 46,772 股

📆 10-23 Forward Structure
存量OI: C 5.1k / P 1.1k，今日变化ΔOI: C +63 / P +63，平值价格ATM: C $1.05 / P $1.07 ｜ ATM IV 72.3%，净 delta 敞口 -2k shares
Top ΔOI: P 14 +66 ｜ P 14 -58
仓位参考: Max Pain 17 ｜ Put Wall 14（-8.7%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 72.3%｜历史 Rank 55%（近端代理）｜IV/RV 1.15×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,717 股

10-30（MEDIUM △）Top ΔOI: 14C +93 ｜ 16P +30
10-30（MEDIUM △）仓位参考: Max Pain 16 ｜ Put Wall 14（-8.7%）（OI 0.3k）

11-06（MEDIUM △）Top ΔOI: 15P +41 ｜ 14C +21
11-06（MEDIUM △）仓位参考: Max Pain 16 ｜ Put Wall 15.5（+1.0%，弱）（OI 62）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-09/NNE_evening.json