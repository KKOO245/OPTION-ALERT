# 期权晚报 2026-10-30（快照 21:00 ET）

📊 市场环境

SPY $755.72 ｜ QQQ $690.49
VIX 19.42 ↑12.9%（5D -0.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 26.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-30

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 453.60 → 收盘 432.01（-4.8%） ｜ 今日高 453.60 ｜ 低 431.19 ｜ 昨收 448.76 → 收盘 432.01（-3.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.46 | OI比 0.73 | ATM IV 32.8% | Skew 12.6pp | Term 0.97 | ExpMove ±3.5%（近端） | Rank 13%
量化视角： IV 历史低位（Rank 13%，期权偏便宜）｜期限结构正常（Term 0.97）｜保护溢价显著（Skew 12.6pp，Put 明显贵于 Call）｜⚠️ 重点观察：存量 Call 重（OI比 0.73）+ 当日成交偏 Put（P/C量 1.46）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.46×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.73×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（7D）±3.5% ｜ 11-13（14D）±2.9% ｜ 11-20（21D）±7.4% ｜ 11-27（28D）±6.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,228,712 | GEX Change vs 上次快照 -808,418 | Flip: Primary Flip: 413.49（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 224 / LOW 134 / INVALID 436
结构观察区: Primary Flip 413.49（全链重定价，覆盖 95%）
Call Wall 420（弱结构｜现价高于该位 2.9%）
最近结构参考: Call Wall 420（现价高于该位 2.9%）
量化视角： 正 Gamma（123万，无历史分位）｜正 Gamma 减弱（81万）｜现价位于 Flip 上方 4.48%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 428（MaxPain，仅结算参考） / 420（Call Wall，弱结构）。
• Gamma 区域：切换参考 413（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-06  C +0 / P +0 ｜ Activity LOW ｜ 7D
11-13  C +0 / P +0 ｜ Activity LOW ｜ 14D
11-20  C +0 / P +0 ｜ Activity LOW ｜ 21D
11-27  C +0 / P +0 ｜ Activity LOW ｜ 28D

📆 11-06 Forward Structure
存量OI: C 1.4k / P 1.0k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $7.82 / P $7.17 ｜ ATM IV 32.8%，净 delta 敞口 0 shares
仓位参考: Max Pain 428 ｜ Call Wall 430（-0.5%，弱）（OI 0.1k） ｜ Put Wall 420（-2.8%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 32.8%｜历史 Rank 13%（近端代理）｜IV/RV 1.45×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-13（Activity LOW）仓位参考: Max Pain 425 ｜ Call Wall 440（+1.8%，弱）（OI 0.1k） ｜ Put Wall 420（-2.8%，弱）（OI 81）

11-20（Activity LOW）仓位参考: Max Pain 400 ｜ Call Wall 420（-2.8%，弱）（OI 0.8k） ｜ Put Wall 390（-9.7%，弱）（OI 0.6k）

11-27（Activity LOW）仓位参考: Max Pain 420 ｜ Call Wall 460（+6.5%，弱）（OI 39） ｜ Put Wall 395（-8.6%，弱）（OI 0.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-30/ISRG_evening.json