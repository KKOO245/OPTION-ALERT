# 期权晚报 2026-11-16（快照 21:00 ET）

📊 市场环境

SPY $739.95 ｜ QQQ $661.75
VIX 22.91 ↑18.7%（5D +15.0%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 31.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-17 08:30　【高】零售销售 MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.8
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 待公布 ｜ 前值 1.221
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 待公布 ｜ 前值 1.4

🔍 重点速览
🔴 **事件差分**: 11-18（2D）ATM IV 61.1% vs 11-20 5.3%（差 +55.8pp），覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 387.11 → 收盘 379.74（-1.9%） ｜ 今日高 389.80 ｜ 低 375.63 ｜ 昨收 390.22 → 收盘 379.74（-2.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.81 | OI比 1.13 | ATM IV 61.1% | Skew 8.3pp | Term 0.55 | ExpMove ±3.6%（近端） | Rank 72%
量化视角： IV 中性（Rank 72%）｜期限结构倒挂（Term 0.55，近月 IV 高于远月）｜保护溢价显著（Skew 8.3pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.81×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.13×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-18（2D）±3.6% ｜ 11-20（4D）±0.1% ｜ 11-23（7D）±5.7% ｜ 11-25（9D）±6.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 24,876,829 | GEX Change vs 上次快照 -4,436,519 | Flip: Primary Flip: 372.36（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1300 / LOW 207 / INVALID 903
结构观察区: Primary Flip 372.36（全链重定价，覆盖 100%）
Call Wall 400（弱结构｜现价低于该位 5.1%）
最近结构参考: Flip 372（现价高于该位 2.0%）
量化视角： 正 Gamma（2488万，无历史分位）｜正 Gamma 减弱（444万）｜现价位于 Flip 上方 1.98%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 390（MaxPain，仅结算参考） / 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 372（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-18  C +0 / P +0 ｜ Activity LOW ｜ 2D
11-20  C +0 / P +0 ｜ Activity LOW ｜ 4D
11-23  C +0 / P +0 ｜ Activity LOW ｜ 7D
11-25  C +0 / P +0 ｜ Activity LOW ｜ 9D

📆 11-18 Forward Structure
存量OI: C 19.6k / P 22.2k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $6.70 / P $6.90 ｜ ATM IV 61.1%，净 delta 敞口 0 shares
仓位参考: Max Pain 390 ｜ Call Wall 400（+5.3%，弱）（OI 1.8k） ｜ Put Wall 392.5（+3.4%，弱）（OI 2.4k）
量化解读： 存量两侧均衡｜ATM IV 61.1%｜历史 Rank 72%（近端代理）｜IV/RV 1.08×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-20（Activity LOW）仓位参考: Max Pain 375 ｜ Call Wall 400（+5.3%，弱）（OI 25.8k）

11-23（Activity LOW）仓位参考: Max Pain 390 ｜ Put Wall 360（-5.2%，弱）（OI 0.4k）

11-25（Activity LOW）仓位参考: Max Pain 390 ｜ Call Wall 400（+5.3%，弱）（OI 0.1k）

📅 事件差分（观察，非因果）: 11-18（2D）ATM IV 61.1% vs 11-20 5.3%（差 +55.8pp）——覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-16/TSLA_evening.json