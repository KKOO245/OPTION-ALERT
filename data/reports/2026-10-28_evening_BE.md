# 期权晚报 2026-10-28（快照 21:00 ET）

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
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.9

🔍 重点速览
🟡 **事件差分**: 10-30 ATM IV 97.1% vs 11-06 85.3%（差 +11.8pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 225.97 → 收盘 228.08（+0.9%） ｜ 今日高 231.67 ｜ 低 217.90 ｜ 昨收 218.50 → 收盘 228.08（+4.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.64 | OI比 0.74 | ATM IV 97.1% | Skew -2.1pp | Term 0.81 | ExpMove ±5.8%（近端） | Rank 59%
量化视角： IV 中性（Rank 59%）｜期限结构倒挂（Term 0.81，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.1pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.74）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.64×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.74×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（2D）±5.8% ｜ 11-06（9D）±10.7% ｜ 11-13（16D）±7.4% ｜ 11-20（23D）±16.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 9,247,478 | GEX Change vs 上次快照 5,318,479 | Flip: Primary Flip: 212.56（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 598 / LOW 112 / INVALID 228
结构观察区: Primary Flip 212.56（全链重定价，覆盖 99%）
最近结构参考: Flip 213（现价高于该位 7.3%）
量化视角： 正 Gamma（925万，无历史分位）｜正 Gamma 增强（+532万）｜现价位于 Flip 上方 7.30%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 212（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 213（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-30  C +0 / P +0 ｜ Activity LOW ｜ 2D
11-06  C +0 / P +0 ｜ Activity LOW ｜ 9D
11-13  C +0 / P +0 ｜ Activity LOW ｜ 16D
11-20  C +0 / P +0 ｜ Activity LOW ｜ 23D

📆 10-30 Forward Structure
存量OI: C 65.6k / P 48.4k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $6.90 / P $6.40 ｜ ATM IV 97.1%，净 delta 敞口 0 shares
仓位参考: Max Pain 212 ｜ Call Wall 240（+5.2%，弱）（OI 4.1k） ｜ Put Wall 210（-7.9%，弱）（OI 2.3k）
量化解读： 存量 Call 重｜ATM IV 97.1%｜历史 Rank 59%（近端代理）｜IV/RV 1.14×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-06（Activity LOW）仓位参考: Max Pain 230 ｜ Call Wall 225（-1.4%，弱）（OI 1.4k） ｜ Put Wall 235（+3.0%，弱）（OI 2.0k）

11-13（Activity LOW）仓位参考: Max Pain 242 ｜ Call Wall 250（+9.6%，弱）（OI 0.7k） ｜ Put Wall 240（+5.2%，弱）（OI 0.5k）

11-20（Activity LOW）仓位参考: Max Pain 230 ｜ Call Wall 240（+5.2%，弱）（OI 2.7k） ｜ Put Wall 220（-3.5%，弱）（OI 3.7k）

📅 事件差分（观察，非因果）: 10-30（2D）ATM IV 97.1% vs 11-06 85.3%（差 +11.8pp）——覆盖 美联储议息会议 Statement、美联储利率决议 Decision、Fed Press Conference、PCE 物价 Price Index MoM、GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-28/BE_evening.json