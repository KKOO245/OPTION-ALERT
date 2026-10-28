# 期权晚报 2026-10-28（快照 16:40 ET）

📊 市场环境

SPY $772.31 ｜ QQQ $725.61
VIX 16.91 ↓3.5%（5D +1.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-28

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布　✅ 今日已公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 4 ｜ 前值 4　✅ 今日已公布
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布　✅ 今日已公布
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.9

🔍 重点速览
🟡 **近现价集中开仓**: 10-30 10C ΔOI +2,084（距现价 -4.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 10.41 → 收盘 10.48（+0.7%） ｜ 今日高 10.49 ｜ 低 9.85 ｜ 昨收 10.40 → 收盘 10.48（+0.8%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.39 | OI比 0.37 | ATM IV 94.7% | Skew 4.4pp | Term 0.94 | ExpMove ±5.1%（近端） | Rank 28%
量化视角： IV 中性（Rank 28%）｜期限结构正常（Term 0.94）｜保护溢价中性（Skew 4.4pp）｜存量 Call 偏重（OI比 0.37）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.39×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.37×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（2D）±5.1% ｜ 11-06（9D）±12.3% ｜ 11-13（16D）±17.8% ｜ 11-20（23D）±20.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 5,654,931 | GEX Change vs 上次快照 2,017,904 | Flip: Primary Flip: 9.32（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 219 / LOW 78 / INVALID 123
结构观察区: Primary Flip 9.32（全链重定价，覆盖 100%）
Put Wall 10（弱结构｜现价高于该位 4.8%） | Call Wall 11（弱结构｜现价低于该位 4.7%）
最近结构参考: Call Wall 11（现价低于该位 4.7%）
量化视角： 正 Gamma（565万，无历史分位）｜正 Gamma 增强（+202万）｜现价位于 Flip 上方 12.41%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 10（Put Wall，弱结构） / 10（MaxPain，仅结算参考）；上方 11（Call Wall，弱结构）。
• Gamma 区域：切换参考 9（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-30  C +5.5k / P +1.5k ｜ Activity HIGH ｜ 2D
11-06  C +1.6k / P +0.1k ｜ Activity HIGH ｜ 9D
11-13  C +1.0k / P +17 ｜ Activity HIGH ｜ 16D
11-20  C +3.9k / P +0.3k ｜ Activity MEDIUM △ ｜ 23D

📆 10-30 Forward Structure
存量OI: C 29.1k / P 10.8k，今日变化ΔOI: C +5.5k / P +1.5k，平值价格ATM: C $0.21 / P $0.32 ｜ ATM IV 94.7%，净 delta 敞口 256k shares
Top ΔOI: C 10 +2,084 ｜ C 11 +1,812 ｜ P 10 +1,359
仓位参考: Max Pain 10 ｜ Call Wall 10（-4.6%，弱）（OI 5.1k） ｜ Put Wall 10（-4.6%，弱）（OI 2.0k）
量化解读： 存量 Call 重｜ATM IV 94.7%｜历史 Rank 28%（近端代理）｜IV/RV 1.11×（近似）｜净 delta 敞口 正 255,619 股

📆 11-06 Forward Structure
存量OI: C 8.1k / P 4.3k，今日变化ΔOI: C +1.6k / P +0.1k，平值价格ATM: C $0.59 / P $0.70 ｜ ATM IV 85.4%，净 delta 敞口 62k shares
Top ΔOI: C 10 +486 ｜ C 11 +382 ｜ C 11 +314
仓位参考: Max Pain 10 ｜ Call Wall 11（+5.0%，弱）（OI 0.9k） ｜ Put Wall 10（-4.6%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 85.4%｜历史 Rank 28%（近端代理）｜IV/RV 1.00×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 62,099 股

📆 11-13 Forward Structure
存量OI: C 4.9k / P 2.7k，今日变化ΔOI: C +1.0k / P +17，平值价格ATM: C $0.82 / P $1.05 ｜ ATM IV 95.4%，净 delta 敞口 45k shares
Top ΔOI: C 11 +701 ｜ C 11 +77
仓位参考: Max Pain 10 ｜ Call Wall 11（+5.0%，弱）（OI 0.8k） ｜ Put Wall 11（+5.0%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 95.4%｜历史 Rank 28%（近端代理）｜IV/RV 1.12×（近似）｜净 delta 敞口 正 44,997 股

11-20（MEDIUM △）Top ΔOI: 11C +550
11-20（MEDIUM △）仓位参考: Max Pain 13 ｜ Call Wall 11（+5.0%，弱）（OI 1.8k） ｜ Put Wall 10（-4.6%，弱）（OI 6.3k）

📅 事件差分（观察，非因果）: 10-30（2D）ATM IV 94.7% vs 11-06 85.4%（差 +9.3pp）——覆盖 美联储议息会议 Statement、美联储利率决议 Decision、Fed Press Conference、GDP 增速 Rate QoQ Adv、PCE 物价 Price Index MoM、Personal Income MoM、Personal Spending MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-28/USAR_evening.json