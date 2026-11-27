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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 430.92 → 收盘 430.18（-0.2%） ｜ 今日高 431.34 ｜ 低 423.23 ｜ 昨收 427.18 → 收盘 430.18（+0.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.14 | OI比 0.60 | ATM IV 33.6% | Skew 3.6pp | Term 1.01 | ExpMove ±2.3%（近端） | Rank 13%
量化视角： IV 历史低位（Rank 13%，期权偏便宜）｜期限结构正常（Term 1.01）｜保护溢价中性（Skew 3.6pp）｜存量 Call 偏重（OI比 0.60）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.14×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.60×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 12-04（7D）±2.3% ｜ 12-11（14D）±3.6% ｜ 12-18（21D）±10.1% ｜ 12-24（27D）±14.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,989,164 | GEX Change vs 上次快照 336,022 | Flip: Primary Flip: 402.30（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 243 / LOW 170 / INVALID 571
结构观察区: Primary Flip 402.30（全链重定价，覆盖 95%）
Call Wall 400（弱结构｜现价高于该位 7.5%）
最近结构参考: Flip 402（现价高于该位 6.9%）
量化视角： 正 Gamma（199万，无历史分位）｜正 Gamma 增强（+34万）｜现价位于 Flip 上方 6.93%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 410（MaxPain，仅结算参考） / 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 402（全链重定价，覆盖 95%）。
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
存量OI: C 0.7k / P 0.3k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $3.20 / P $6.55 ｜ ATM IV 31.2%，净 delta 敞口 0 shares
仓位参考: Max Pain 420 ｜ Call Wall 450（+4.6%，弱）（OI 46） ｜ Put Wall 405（-5.9%，弱）（OI 29）
量化解读： 存量 Call 重｜ATM IV 31.2%｜历史 Rank 13%（近端代理）｜IV/RV 0.64×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

12-11（Activity LOW）仓位参考: Max Pain 435 ｜ Call Wall 450（+4.6%）（OI 0.1k） ｜ Put Wall 435（+1.1%）（OI 36）

12-18（Activity LOW）仓位参考: Max Pain 410 ｜ Call Wall 400（-7.0%，弱）（OI 1.5k） ｜ Put Wall 420（-2.4%，弱）（OI 0.6k）

12-24（Activity LOW）仓位参考: Max Pain 440 ｜ Call Wall 450（+4.6%）（OI 59） ｜ Put Wall 400（-7.0%，弱）（OI 36）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-27/ISRG_evening.json