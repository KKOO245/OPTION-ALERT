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

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 752.55 → 收盘 751.27（-0.2%） ｜ 今日高 752.86 ｜ 低 748.36 ｜ 昨收 747.58 → 收盘 751.27（+0.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.27 | OI比 2.24 | ATM IV 8.6% | Skew 1.1pp | Term 2.09 | ExpMove ±0.6%（近端） | Rank 5%
量化视角： IV 历史低位（Rank 5%，期权偏便宜）｜期限结构正常偏陡（Term 2.09）｜保护溢价薄（Skew 1.1pp）｜当日成交偏 Put（P/C量 1.27）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.27×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 2.24×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 60% ｜ P/C OI(近端) 86%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 60%）｜近端持仓结构中性（P/C OI 分位 86%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-12（3D）±0.6% ｜ 10-13（4D）±0.9% ｜ 10-14（5D）±1.2% ｜ 10-15（6D）±1.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 87,739,264 | GEX Change vs 上次快照 237,333,743 | Flip: Primary Flip: 750.04（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 2896 / LOW 240 / INVALID 1374
结构观察区: Primary Flip 750.04（全链重定价，覆盖 99%）
Call Wall 760（弱结构｜现价低于该位 1.1%）
最近结构参考: Flip 750（现价高于该位 0.2%）
量化视角： 正 Gamma（8774万，历史分位 60%，中性区）｜由负转正（+2.37亿）｜现价位于 Flip 上方 0.16%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 750（MaxPain，仅结算参考）；上方 760（Call Wall，弱结构）。
• Gamma 区域：切换参考 750（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-12  C +0 / P +0 ｜ Activity LOW ｜ 3D
10-13  C +0 / P +0 ｜ Activity LOW ｜ 4D
10-14  C +0 / P +0 ｜ Activity LOW ｜ 5D
10-15  C +0 / P +0 ｜ Activity LOW ｜ 6D

📆 10-12 Forward Structure
存量OI: C 70.1k / P 157.0k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $2.49 / P $2.23 ｜ ATM IV 8.6%，净 delta 敞口 0 shares
仓位参考: Max Pain 750 ｜ Call Wall 755（+0.5%，弱）（OI 5.2k） ｜ Put Wall 738（-1.8%，弱）（OI 13.2k）
量化解读： 存量 Put 重｜ATM IV 8.6%｜历史 Rank 5%（近端代理）｜IV/RV 0.59×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

10-13（Activity LOW）仓位参考: Max Pain 751 ｜ Call Wall 770（+2.5%，弱）（OI 1.8k） ｜ Put Wall 740（-1.5%，弱）（OI 11.2k）

10-14（Activity LOW）仓位参考: Max Pain 752 ｜ Call Wall 770（+2.5%，弱）（OI 2.3k） ｜ Put Wall 730（-2.8%，弱）（OI 2.5k）

10-15（Activity LOW）仓位参考: Max Pain 750 ｜ Call Wall 763（+1.6%，弱）（OI 1.5k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-09/QQQ_evening.json