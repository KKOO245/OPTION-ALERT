# 期权晚报 2026-11-11（快照 16:40 ET）

📊 市场环境

SPY $759.81 ｜ QQQ $690.38
VIX 17.49 ↓10.1%（5D +5.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 37.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-11

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-13 38C ΔOI +220（距现价 +3.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 37.20 → 收盘 36.73（-1.3%） ｜ 今日高 38.25 ｜ 低 36.71 ｜ 昨收 36.46 → 收盘 36.73（+0.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.85 | OI比 0.35 | ATM IV 69.9% | Skew -1.4pp | Term 0.91 | ExpMove ±5.2%（近端） | Rank 54%
量化视角： IV 中性（Rank 54%）｜期限结构正常（Term 0.91）｜Put 保护异常便宜（Skew -1.4pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.35）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.85×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.35×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（2D）±5.2% ｜ 11-20（9D）±8.3% ｜ 11-27（16D）±9.5% ｜ 12-04（23D）±14.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 3,287,936 | GEX Change vs 上次快照 -1,075,701 | Flip: Primary Flip: 35.36（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 254 / LOW 89 / INVALID 149
结构观察区: Primary Flip 35.36（全链重定价，覆盖 98%）
Put Wall 35（现价高于该位 4.9%）
最近结构参考: Flip 35（现价高于该位 3.9%）
量化视角： 正 Gamma（329万，无历史分位）｜正 Gamma 减弱（108万）｜现价位于 Flip 上方 3.87%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 35（Put Wall）；上方 37（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 35（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +0.7k / P +0.2k ｜ Activity HIGH ｜ 2D
11-20  C +97 / P -0.6k ｜ Activity HIGH ｜ 9D
11-27  C +39 / P +50 ｜ Activity MEDIUM △ ｜ 16D
12-04  C +0.1k / P +40 ｜ Activity MEDIUM △ ｜ 23D

📆 11-13 Forward Structure
存量OI: C 14.5k / P 5.1k，今日变化ΔOI: C +0.7k / P +0.2k，平值价格ATM: C $1.30 / P $0.63 ｜ ATM IV 69.9%，净 delta 敞口 25k shares
Top ΔOI: C 38 +220 ｜ C 39 +148
仓位参考: Max Pain 37 ｜ Call Wall 40（+8.9%，弱）（OI 2.1k） ｜ Put Wall 34（-7.4%）（OI 1.1k）
量化解读： 存量 Call 重｜ATM IV 69.9%｜历史 Rank 54%（近端代理）｜IV/RV 1.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 24,976 股

📆 11-20 Forward Structure
存量OI: C 24.9k / P 12.4k，今日变化ΔOI: C +97 / P -0.6k，平值价格ATM: C $2.04 / P $1.01 ｜ ATM IV 66.4%，净 delta 敞口 69k shares
Top ΔOI: P 50 -287 ｜ P 55 -265
仓位参考: Max Pain 40 ｜ Call Wall 39.5（+7.5%，弱）（OI 1.5k） ｜ Put Wall 35（-4.7%）（OI 3.8k）
量化解读： 存量 Call 重｜ATM IV 66.4%｜历史 Rank 54%（近端代理）｜IV/RV 1.11×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 69,441 股

11-27（MEDIUM △）Top ΔOI: 39C +19
11-27（MEDIUM △）仓位参考: Max Pain 42 ｜ Put Wall 38（+3.5%，弱）（OI 82）

12-04（MEDIUM △）仓位参考: Max Pain 35 ｜ Call Wall 35（-4.7%）（OI 0.5k） ｜ Put Wall 34（-7.4%）（OI 0.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-11/MP_evening.json