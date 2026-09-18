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

🔍 重点速览
🟡 **事件差分**: 09-18 ATM IV 44.0% vs 09-21 32.7%（差 +11.3pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 367.59 → 收盘 366.20（-0.4%） ｜ 今日高 374.12 ｜ 低 363.22 ｜ 昨收 358.08 → 收盘 366.20（+2.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.65 | OI比 0.80 | ATM IV 44.0% | Skew -0.7pp | Term 0.93 | ExpMove ±1.9%（近端） | Rank 18%
量化视角： IV 历史低位（Rank 18%，期权偏便宜）｜期限结构正常（Term 0.93）｜Put 保护异常便宜（Skew -0.7pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.80）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.65×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.80×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（1D）±1.9% ｜ 09-21（4D）±2.7% ｜ 09-23（6D）±3.8% ｜ 09-25（8D）±4.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 125,426,022 | GEX Change vs 上次快照 18,119,567 | Flip: Primary Flip: 357.32（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 1191 / LOW 212 / INVALID 521
结构观察区: Primary Flip 357.32（全链重定价，覆盖 98%）
Call Wall 400（弱结构｜现价低于该位 8.4%）
最近结构参考: Flip 357（现价高于该位 2.5%）
量化视角： 正 Gamma（1.25亿，无历史分位）｜正 Gamma 增强（+1812万）｜现价位于 Flip 上方 2.49%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 358（MaxPain，仅结算参考）；上方 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 357（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-18  C +0 / P +0 ｜ Activity LOW ｜ 1D
09-21  C +0 / P +0 ｜ Activity LOW ｜ 4D
09-23  C +0 / P +0 ｜ Activity LOW ｜ 6D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 8D

📆 09-18 Forward Structure
存量OI: C 603.9k / P 481.3k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $4.00 / P $2.83 ｜ ATM IV 44.0%，净 delta 敞口 0 shares
仓位参考: Max Pain 358 ｜ Call Wall 400（+9.2%，弱）（OI 24.0k） ｜ Put Wall 350（-4.4%，弱）（OI 18.1k）
量化解读： 存量 Call 重｜ATM IV 44.0%｜历史 Rank 18%（近端代理）｜IV/RV 0.99×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-21（Activity LOW）仓位参考: Max Pain 360 ｜ Call Wall 400（+9.2%）（OI 5.1k） ｜ Put Wall 360（-1.7%，弱）（OI 1.8k）

09-23（Activity LOW）仓位参考: Max Pain 362 ｜ Call Wall 400（+9.2%，弱）（OI 1.2k） ｜ Put Wall 330（-9.9%）（OI 1.5k）

09-25（Activity LOW）仓位参考: Max Pain 358 ｜ Call Wall 385（+5.1%，弱）（OI 6.4k） ｜ Put Wall 350（-4.4%，弱）（OI 4.2k）

📅 事件差分（观察，非因果）: 09-18（1D）ATM IV 44.0% vs 09-21 32.7%（差 +11.3pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-17/TSLA_evening.json