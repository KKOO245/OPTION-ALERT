# 期权晚报 2026-11-27（快照 16:40 ET）

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

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 12-04 105C ΔOI +7,279（距现价 -1.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 12-04 105C ΔOI +7,279 占该期限总 OI 10.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 108.44 → 收盘 107.04（-1.3%） ｜ 今日高 108.90 ｜ 低 104.44 ｜ 昨收 103.72 → 收盘 107.04（+3.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.01 | OI比 0.64 | ATM IV 75.8% | Skew 9.3pp | Term 1.01 | ExpMove ±8.6%（近端） | Rank 50%
量化视角： IV 中性（Rank 50%）｜期限结构正常（Term 1.01）｜保护溢价显著（Skew 9.3pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.64）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.01×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.64×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 12-04（7D）±8.6% ｜ 12-11（14D）±12.0% ｜ 12-18（21D）±14.9% ｜ 12-24（27D）±16.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 9,383,839 | GEX Change vs 上次快照 -1,924,736 | Flip: Candidates 94.60 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 76%（带内） ｜ IV 有效性: VALID 395 / LOW 188 / INVALID 499
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: ≈95（全链重定价，覆盖 76%，CONDITIONAL）
Put Wall 100（弱结构｜现价高于该位 7.0%）
最近结构参考: Put Wall 100（现价高于该位 7.0%）
量化视角： 正 Gamma（938万，无历史分位）｜正 Gamma 减弱（192万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 100（Put Wall，弱结构）；上方 108（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 95（全链重定价，覆盖 76%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

12-04  C +29.1k / P +7.5k ｜ Activity HIGH ｜ 7D
12-11  C +0.5k / P -0.2k ｜ Activity HIGH ｜ 14D
12-18  C +1.6k / P +0.9k ｜ Activity HIGH ｜ 21D
12-24  C +0.1k / P +0.5k ｜ Activity HIGH ｜ 27D

📆 12-04 Forward Structure
存量OI: C 44.2k / P 26.4k，今日变化ΔOI: C +29.1k / P +7.5k，平值价格ATM: C $4.50 / P $4.69 ｜ ATM IV 77.4%，净 delta 敞口 1.6M shares
Top ΔOI: C 105 +7,279 ｜ C 101 +7,261 ｜ C 107 +3,257
仓位参考: Max Pain 101 ｜ Call Wall 105（-1.9%，弱）（OI 7.4k） ｜ Put Wall 100（-6.6%，弱）（OI 3.7k）
量化解读： 存量 Call 重｜ATM IV 77.4%｜历史 Rank 50%（近端代理）｜IV/RV 1.21×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,574,268 股

📆 12-11 Forward Structure
存量OI: C 5.5k / P 6.7k，今日变化ΔOI: C +0.5k / P -0.2k，平值价格ATM: C $6.50 / P $6.35 ｜ ATM IV 78.4%，净 delta 敞口 23k shares
仓位参考: Max Pain 120 ｜ Call Wall 110（+2.8%，弱）（OI 0.3k） ｜ Put Wall 100（-6.6%，弱）（OI 0.7k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 78.4%｜历史 Rank 50%（近端代理）｜IV/RV 1.23×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 22,940 股

📆 12-18 Forward Structure
存量OI: C 146.9k / P 54.7k，今日变化ΔOI: C +1.6k / P +0.9k，平值价格ATM: C $8.01 / P $7.95 ｜ ATM IV 77.9%，净 delta 敞口 49k shares
Top ΔOI: P 80 +1,099
仓位参考: Max Pain 130 ｜ Put Wall 110（+2.8%）（OI 7.9k）
量化解读： 存量 Call 重｜ATM IV 77.9%｜历史 Rank 50%（近端代理）｜IV/RV 1.22×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 49,131 股

📆 12-24 Forward Structure
存量OI: C 4.3k / P 2.5k，今日变化ΔOI: C +0.1k / P +0.5k，平值价格ATM: C $10.35 / P $7.30 ｜ ATM IV 76.7%，净 delta 敞口 -31 shares
仓位参考: Max Pain 105 ｜ Call Wall 105（-1.9%，弱）（OI 0.5k） ｜ Put Wall 105（-1.9%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 76.7%｜历史 Rank 50%（近端代理）｜IV/RV 1.20×（近似）｜净 delta 敞口 负 31 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-27/COIN_evening.json