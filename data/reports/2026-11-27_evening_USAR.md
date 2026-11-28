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

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 6.91 → 收盘 6.70（-3.0%） ｜ 今日高 6.91 ｜ 低 6.41 ｜ 昨收 6.59 → 收盘 6.70（+1.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.06 | OI比 0.56 | ATM IV 115.7% | Skew 15.0pp | Term 0.93 | ExpMove ±18.3%（近端） | Rank 50%
量化视角： IV 中性（Rank 50%）｜期限结构正常（Term 0.93）｜保护溢价显著（Skew 15.0pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.56）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.06×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.56×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 12-04（7D）±18.3% ｜ 12-11（14D）±23.1% ｜ 12-18（21D）±24.5% ｜ 12-24（27D）±27.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -957,742 | GEX Change vs 上次快照 8,647 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 183 / LOW 67 / INVALID 88
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: NO_CROSS
量化视角： 负 Gamma（96万，无历史分位）｜负 Gamma 缓解（+1万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 8（MaxPain，仅结算参考）。
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
存量OI: C 4.1k / P 2.3k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $0.83 / P $0.40 ｜ ATM IV 115.7%，净 delta 敞口 0 shares
仓位参考: Max Pain 8 ｜ Call Wall 7（+4.4%，弱）（OI 0.3k） ｜ Put Wall 7（+4.4%）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 115.7%｜历史 Rank 50%（近端代理）｜IV/RV 1.08×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

12-11（Activity LOW）仓位参考: Max Pain 8 ｜ Put Wall 7（+4.4%，弱）（OI 0.1k）

12-18（Activity LOW）仓位参考: Max Pain 10 ｜ Put Wall 7（+4.4%，弱）（OI 4.6k）

12-24（Activity LOW）仓位参考: Max Pain 8 ｜ Put Wall 7（+4.4%，弱）（OI 80）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-27/USAR_evening.json