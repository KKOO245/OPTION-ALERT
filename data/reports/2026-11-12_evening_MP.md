# 期权晚报 2026-11-12（快照 16:40 ET）

📊 市场环境

SPY $757.12 ｜ QQQ $688.17
VIX 18.70 ↑6.9%（5D -33.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 39.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-12

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 3.75 ｜ 前值 3.97　✅ 今日已公布
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 37.81 → 收盘 37.45（-1.0%） ｜ 今日高 38.63 ｜ 低 35.93 ｜ 昨收 36.73 → 收盘 37.45（+2.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.47 | OI比 0.34 | ATM IV 74.9% | Skew -21.0pp | Term 0.90 | ExpMove ±2.9%（近端） | Rank 63%
量化视角： IV 中性（Rank 63%）｜期限结构倒挂（Term 0.90，近月 IV 高于远月）｜Put 保护异常便宜（Skew -21.0pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.34）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.47×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.34×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（1D）±2.9% ｜ 11-20（8D）±7.9% ｜ 11-27（15D）±13.0% ｜ 12-04（22D）±13.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 5,829,178 | GEX Change vs 上次快照 3,196,423 | Flip: Primary Flip: 35.50（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 264 / LOW 84 / INVALID 144
结构观察区: Primary Flip 35.50（全链重定价，覆盖 98%）
Put Wall 35（现价高于该位 7.0%）
最近结构参考: Flip 36（现价高于该位 5.5%）
量化视角： 正 Gamma（583万，无历史分位）｜正 Gamma 增强（+320万）｜现价位于 Flip 上方 5.48%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 35（Put Wall） / 37（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 36（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +0.5k / P +15 ｜ Activity MEDIUM △ ｜ 1D
11-20  C +0.7k / P +0.8k ｜ Activity HIGH ｜ 8D
11-27  C +0.1k / P +0.1k ｜ Activity MEDIUM △ ｜ 15D
12-04  C +86 / P +13 ｜ Activity MEDIUM △ ｜ 22D

📆 11-13 Forward Structure
存量OI: C 15.1k / P 5.1k，今日变化ΔOI: C +0.5k / P +15，平值价格ATM: C $0.60 / P $0.50 ｜ ATM IV 74.9%，净 delta 敞口 14k shares
Top ΔOI: C 39 +323 ｜ P 34 -272 ｜ P 35 +127
仓位参考: Max Pain 37 ｜ Call Wall 40（+6.8%，弱）（OI 2.1k） ｜ Put Wall 34（-9.2%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 74.9%｜历史 Rank 63%（近端代理）｜IV/RV 1.25×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 13,914 股

📆 11-20 Forward Structure
存量OI: C 25.7k / P 13.2k，今日变化ΔOI: C +0.7k / P +0.8k，平值价格ATM: C $1.70 / P $1.26 ｜ ATM IV 71.3%，净 delta 敞口 25k shares
Top ΔOI: P 34 +805 ｜ C 39 +697 ｜ P 35 +151
仓位参考: Max Pain 40 ｜ Call Wall 39.5（+5.5%，弱）（OI 2.2k） ｜ Put Wall 35（-6.5%）（OI 3.9k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 71.3%｜历史 Rank 63%（近端代理）｜IV/RV 1.19×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 24,581 股

11-27（MEDIUM △）Top ΔOI: 35P +37
11-27（MEDIUM △）仓位参考: Max Pain 42 ｜ Put Wall 38（+1.5%，弱）（OI 82）

12-04（MEDIUM △）Top ΔOI: 36P +7
12-04（MEDIUM △）仓位参考: Max Pain 35 ｜ Call Wall 35（-6.5%）（OI 0.5k） ｜ Put Wall 34（-9.2%）（OI 0.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-12/MP_evening.json