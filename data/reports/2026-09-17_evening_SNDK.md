# 期权晚报 2026-09-17（快照 21:08 ET）

📊 市场环境

SPY $762.60 ｜ QQQ $nan
VIX 15.44 ↓12.8%（5D -13.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-17

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 1.275 ｜ 前值 1.309　✅ 今日已公布
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 1.394 ｜ 前值 1.433　✅ 今日已公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 1,564.50 → 收盘 1,614.39（+3.2%） ｜ 今日高 1625.35 ｜ 低 1564.50 ｜ 昨收 1,519.97 → 收盘 1,614.39（+6.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.56 | OI比 1.09 | ATM IV 75.2% | Skew -2.3pp | Term 0.91 | ExpMove ±3.1%（近端） | Rank 29%
量化视角： IV 中性（Rank 29%）｜期限结构正常（Term 0.91）｜Put 保护异常便宜（Skew -2.3pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.56×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.09×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（1D）±3.1% ｜ 09-25（8D）±8.1% ｜ 10-02（15D）±11.6% ｜ 10-09（22D）±13.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 6,248,065 | GEX Change vs 上次快照 -382,940 | Flip: Primary Flip: 1579.53（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 1867 / LOW 548 / INVALID 961
结构观察区: Primary Flip 1579.53（全链重定价，覆盖 98%）
最近结构参考: Flip 1580（现价高于该位 2.2%）
量化视角： 正 Gamma（625万，无历史分位）｜正 Gamma 减弱（38万）｜现价位于 Flip 上方 2.21%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 1,500（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1580（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-18  C +0 / P +0 ｜ Activity LOW ｜ 1D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 8D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 15D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 22D

📆 09-18 Forward Structure
存量OI: C 94.4k / P 103.2k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $25.20 / P $25.50 ｜ ATM IV 75.2%，净 delta 敞口 0 shares
仓位参考: Max Pain 1,500 ｜ Call Wall 1750（+8.4%，弱）（OI 3.7k） ｜ Put Wall 1500（-7.1%，弱）（OI 3.9k）
量化解读： 存量两侧均衡｜ATM IV 75.2%｜历史 Rank 29%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-25（Activity LOW）仓位参考: Max Pain 1,575 ｜ Call Wall 1700（+5.3%，弱）（OI 0.7k） ｜ Put Wall 1500（-7.1%，弱）（OI 1.8k）

10-02（Activity LOW）仓位参考: Max Pain 1,580 ｜ Call Wall 1600（-0.9%，弱）（OI 0.5k） ｜ Put Wall 1500（-7.1%，弱）（OI 0.4k）

10-09（Activity LOW）仓位参考: Max Pain 1,610 ｜ Call Wall 1750（+8.4%，弱）（OI 0.1k） ｜ Put Wall 1500（-7.1%，弱）（OI 0.2k）

📅 事件差分（观察，非因果）: 09-18（1D）ATM IV 75.2% vs 09-25 65.4%（差 +9.8pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-17/SNDK_evening.json