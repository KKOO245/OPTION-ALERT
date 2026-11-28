# 期权晚报 2026-11-27（快照 21:00 ET）

📊 市场环境

SPY $728.32 ｜ QQQ $650.99
VIX 23.81 ↓11.2%（5D -33.7%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 24.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-27

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 108.44 → 收盘 107.04（-1.3%） ｜ 今日高 108.90 ｜ 低 104.44 ｜ 昨收 103.72 → 收盘 107.04（+3.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.54 | OI比 0.60 | ATM IV 77.4% | Skew 8.0pp | Term 0.95 | ExpMove ±8.6%（近端） | Rank 54%
量化视角： IV 中性（Rank 54%）｜期限结构正常（Term 0.95）｜保护溢价显著（Skew 8.0pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.60）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.54×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.60×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 12-04（7D）±8.6% ｜ 12-11（14D）±12.0% ｜ 12-18（21D）±14.9% ｜ 12-24（27D）±16.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 6,593,686 | GEX Change vs 上次快照 -4,714,889 | Flip: Primary Flip: 95.36（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 387 / LOW 162 / INVALID 311
结构观察区: Primary Flip 95.36（全链重定价，覆盖 100%）
Put Wall 110（弱结构｜现价低于该位 2.7%）
最近结构参考: Put Wall 110（现价低于该位 2.7%）
量化视角： 正 Gamma（659万，无历史分位）｜正 Gamma 减弱（471万）｜现价位于 Flip 上方 12.25%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 101（MaxPain，仅结算参考）；上方 110（Put Wall，弱结构）。
• Gamma 区域：切换参考 95（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

12-04  C +0 / P +0 ｜ Activity LOW ｜ 7D
12-11  C +0 / P +0 ｜ Activity LOW ｜ 14D
12-18  C +0 / P +0 ｜ Activity LOW ｜ 21D
12-24  C +0 / P +0 ｜ Activity LOW ｜ 27D

📆 12-04 Forward Structure
存量OI: C 44.2k / P 26.4k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $4.50 / P $4.69 ｜ ATM IV 77.4%，净 delta 敞口 0 shares
仓位参考: Max Pain 101 ｜ Call Wall 105（-1.9%，弱）（OI 7.4k） ｜ Put Wall 100（-6.6%，弱）（OI 3.7k）
量化解读： 存量 Call 重｜ATM IV 77.4%｜历史 Rank 54%（近端代理）｜IV/RV 1.21×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

12-11（Activity LOW）仓位参考: Max Pain 120 ｜ Call Wall 110（+2.8%，弱）（OI 0.3k） ｜ Put Wall 100（-6.6%，弱）（OI 0.7k）

12-18（Activity LOW）仓位参考: Max Pain 130 ｜ Put Wall 110（+2.8%）（OI 7.9k）

12-24（Activity LOW）仓位参考: Max Pain 105 ｜ Call Wall 105（-1.9%，弱）（OI 0.5k） ｜ Put Wall 105（-1.9%，弱）（OI 0.6k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-27/COIN_evening.json