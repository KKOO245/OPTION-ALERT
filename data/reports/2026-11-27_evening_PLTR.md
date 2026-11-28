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


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 169.76 → 收盘 172.17（+1.4%） ｜ 今日高 173.22 ｜ 低 164.80 ｜ 昨收 163.59 → 收盘 172.17（+5.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.42 | OI比 0.88 | ATM IV 57.6% | Skew 8.0pp | Term 0.92 | ExpMove ±6.6%（近端） | Rank 62%
量化视角： IV 中性（Rank 62%）｜期限结构正常（Term 0.92）｜保护溢价显著（Skew 8.0pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.42×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.88×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 12-04（7D）±6.6% ｜ 12-11（14D）±8.9% ｜ 12-18（21D）±10.9% ｜ 12-24（27D）±11.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 25,835,057 | GEX Change vs 上次快照 -20,374,917 | Flip: Primary Flip: 158.18（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 390 / LOW 117 / INVALID 245
结构观察区: Primary Flip 158.18（全链重定价，覆盖 100%）
最近结构参考: Flip 158（现价高于该位 8.8%）
量化视角： 正 Gamma（2584万，无历史分位）｜正 Gamma 减弱（2037万）｜现价位于 Flip 上方 8.84%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 160（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 158（全链重定价，覆盖 100%）。
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
存量OI: C 54.3k / P 48.0k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $5.85 / P $5.55 ｜ ATM IV 57.6%，净 delta 敞口 0 shares
仓位参考: Max Pain 160 ｜ Call Wall 175（+1.6%，弱）（OI 9.4k） ｜ Put Wall 155（-10.0%，弱）（OI 3.2k）
量化解读： 存量两侧均衡｜ATM IV 57.6%｜历史 Rank 62%（近端代理）｜IV/RV 0.85×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

12-11（Activity LOW）仓位参考: Max Pain 160 ｜ Call Wall 175（+1.6%，弱）（OI 1.3k） ｜ Put Wall 160（-7.1%，弱）（OI 0.8k）

12-18（Activity LOW）仓位参考: Max Pain 140 ｜ Call Wall 185（+7.5%，弱）（OI 16.0k） ｜ Put Wall 160（-7.1%，弱）（OI 18.5k）

12-24（Activity LOW）仓位参考: Max Pain 160 ｜ Call Wall 180（+4.5%，弱）（OI 0.7k） ｜ Put Wall 155（-10.0%，弱）（OI 0.5k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-27/PLTR_evening.json