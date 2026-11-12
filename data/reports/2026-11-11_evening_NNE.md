# 期权晚报 2026-11-11（快照 16:40 ET）

📊 市场环境

SPY $759.81 ｜ QQQ $nan
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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 12.20 → 收盘 11.59（-5.0%） ｜ 今日高 12.23 ｜ 低 11.55 ｜ 昨收 11.58 → 收盘 11.59（+0.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.35 | OI比 0.40 | ATM IV 97.4% | Skew 6.7pp | Term 0.86 | ExpMove ±5.7%（近端） | Rank 40%
量化视角： IV 中性（Rank 40%）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜保护溢价显著（Skew 6.7pp，Put 明显贵于 Call）｜⚠️ 重点观察：存量 Call 重（OI比 0.40）+ 当日成交偏 Put（P/C量 1.35）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.35×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.40×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（2D）±5.7% ｜ 11-20（9D）±12.1% ｜ 11-27（16D）±12.1% ｜ 12-04（23D）±23.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,569,716 | GEX Change vs 上次快照 -404,077 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 162 / LOW 73 / INVALID 151
结构观察区: NO_CROSS
Put Wall 11（现价高于该位 5.4%） | Call Wall 12（现价低于该位 7.3%）
最近结构参考: Put Wall 11（现价高于该位 5.4%）
量化视角： 正 Gamma（157万，无历史分位）｜正 Gamma 减弱（40万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 11（Put Wall）；上方 12（MaxPain，仅结算参考） / 12（Call Wall）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +0.2k / P +70 ｜ Activity HIGH ｜ 2D
11-20  C +37 / P -6 ｜ Activity MEDIUM △ ｜ 9D
11-27  C -1 / P +16 ｜ Activity LOW ｜ 16D
12-04  C +7 / P +1 ｜ Activity MEDIUM △ ｜ 23D

📆 11-13 Forward Structure
存量OI: C 3.0k / P 1.2k，今日变化ΔOI: C +0.2k / P +70，平值价格ATM: C $0.46 / P $0.20 ｜ ATM IV 97.4%，净 delta 敞口 4k shares
Top ΔOI: C 12 +117 ｜ C 11 +37
仓位参考: Max Pain 12 ｜ Call Wall 12.5（+7.9%，弱）（OI 0.5k） ｜ Put Wall 11（-5.1%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 97.4%｜历史 Rank 40%（近端代理）｜IV/RV 0.99×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 3,614 股

11-20（MEDIUM △）Top ΔOI: 12C +31 ｜ 12P -10
11-20（MEDIUM △）仓位参考: Max Pain 12 ｜ Call Wall 12（+3.5%，弱）（OI 0.7k） ｜ Put Wall 11（-5.1%，弱）（OI 0.5k）

11-27（Activity LOW）仓位参考: Max Pain 12 ｜ Call Wall 12.5（+7.9%）（OI 4.0k） ｜ Put Wall 12.5（+7.9%）（OI 0.3k）

12-04（MEDIUM △）Top ΔOI: 11P +1
12-04（MEDIUM △）仓位参考: Max Pain 13 ｜ Call Wall 12.5（+7.9%，弱）（OI 48）

📅 事件差分（观察，非因果）: 11-13（2D）ATM IV 97.4% vs 11-20 88.3%（差 +9.2pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-11/NNE_evening.json