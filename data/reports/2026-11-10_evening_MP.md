# 期权晚报 2026-11-10（快照 16:40 ET）

📊 市场环境

SPY $749.92 ｜ QQQ $674.76
VIX 19.46 ↓2.3%（5D -6.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-10

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-10 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周二 11-10 08:30　【高】Inflation Rate MoM　预测 0.3 ｜ 实际 0.4 ｜ 前值 0.6　✅ 今日已公布
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-13 37C ΔOI -446（距现价 +1.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 36.36 → 收盘 36.46（+0.3%） ｜ 今日高 37.27 ｜ 低 35.60 ｜ 昨收 37.75 → 收盘 36.46（-3.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.50 | OI比 0.36 | ATM IV 74.2% | Skew 1.2pp | Term 0.90 | ExpMove ±5.9%（近端） | Rank 62%
量化视角： IV 中性（Rank 62%）｜期限结构倒挂（Term 0.90，近月 IV 高于远月）｜保护溢价薄（Skew 1.2pp）｜存量 Call 偏重（OI比 0.36）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.50×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.36×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（3D）±5.9% ｜ 11-20（10D）±9.7% ｜ 11-27（17D）±9.5% ｜ 12-04（24D）±13.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,138,593 | GEX Change vs 上次快照 -1,114,833 | Flip: Primary Flip: 35.14（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 300 / LOW 76 / INVALID 116
结构观察区: Primary Flip 35.14（全链重定价，覆盖 100%）
Put Wall 35（现价高于该位 4.2%）
最近结构参考: Flip 35（现价高于该位 3.7%）
量化视角： 正 Gamma（214万，无历史分位）｜正 Gamma 减弱（111万）｜现价位于 Flip 上方 3.74%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 35（Put Wall）；上方 37（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 35（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +2.3k / P +0.2k ｜ Activity HIGH ｜ 3D
11-20  C +3.8k / P +0.1k ｜ Activity MEDIUM △ ｜ 10D
11-27  C +0.2k / P +25 ｜ Activity LOW ｜ 17D
12-04  C +0.1k / P +17 ｜ Activity HIGH ｜ 24D

📆 11-13 Forward Structure
存量OI: C 13.8k / P 4.9k，今日变化ΔOI: C +2.3k / P +0.2k，平值价格ATM: C $0.84 / P $1.30 ｜ ATM IV 74.2%，净 delta 敞口 50k shares
Top ΔOI: C 40 +718 ｜ C 39 +609 ｜ C 37 -446
仓位参考: Max Pain 37 ｜ Call Wall 40（+9.7%，弱）（OI 2.2k） ｜ Put Wall 34（-6.7%）（OI 1.0k）
量化解读： 存量 Call 重｜ATM IV 74.2%｜历史 Rank 62%（近端代理）｜IV/RV 1.25×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 50,420 股

11-20（MEDIUM △）Top ΔOI: 39C +1,443
11-20（MEDIUM △）仓位参考: Max Pain 40 ｜ Call Wall 39.5（+8.3%，弱）（OI 1.5k） ｜ Put Wall 35（-4.0%）（OI 3.8k）

11-27（Activity LOW）仓位参考: Max Pain 42 ｜ Put Wall 38（+4.2%，弱）（OI 88）

📆 12-04 Forward Structure
存量OI: C 2.0k / P 0.8k，今日变化ΔOI: C +0.1k / P +17，平值价格ATM: C $2.66 / P $2.34 ｜ ATM IV 66.5%，净 delta 敞口 1k shares
仓位参考: Max Pain 35 ｜ Call Wall 35（-4.0%）（OI 0.5k） ｜ Put Wall 34（-6.7%）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 66.5%｜历史 Rank 62%（近端代理）｜IV/RV 1.12×（近似）｜净 delta 敞口 正 1,177 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-10/MP_evening.json