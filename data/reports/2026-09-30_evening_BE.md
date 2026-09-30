# 期权晚报 2026-09-30（快照 16:40 ET）

📊 市场环境

SPY $762.63 ｜ QQQ $739.77
VIX 16.34 ↑1.9%（5D +7.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 30.8（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-30

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.2 ｜ 前值 0.1　✅ 今日已公布
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 2.2 ｜ 前值 2.5　✅ 今日已公布
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 0.9 ｜ 前值 0.1　✅ 今日已公布
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **事件差分**: 10-02 ATM IV 86.5% vs 10-09 74.2%（差 +12.3pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-02 290P ΔOI +1,375（距现价 +4.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 296.06 → 收盘 276.98（-6.4%） ｜ 今日高 300.35 ｜ 低 276.90 ｜ 昨收 291.25 → 收盘 276.98（-4.9%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.89 | OI比 1.08 | ATM IV 86.5% | Skew -6.6pp | Term 0.95 | ExpMove ±5.1%（近端） | Rank 49%
量化视角： IV 中性（Rank 49%）｜期限结构正常（Term 0.95）｜Put 保护异常便宜（Skew -6.6pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.89×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.08×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-02（2D）±5.1% ｜ 10-09（9D）±9.3% ｜ 10-16（16D）±12.7% ｜ 10-23（23D）±14.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,897,885 | GEX Change vs 上次快照 -6,218,922 | Flip: Primary Flip: 272.69（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 648 / LOW 86 / INVALID 156
结构观察区: Primary Flip 272.69（全链重定价，覆盖 100%）
Call Wall 300（弱结构｜现价低于该位 7.7%）
最近结构参考: Flip 273（现价高于该位 1.6%）
量化视角： 正 Gamma（290万，无历史分位）｜正 Gamma 减弱（622万）｜现价位于 Flip 上方 1.57%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 280（MaxPain，仅结算参考） / 300（Call Wall，弱结构）。
• Gamma 区域：切换参考 273（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C +12.6k / P +6.9k ｜ Activity HIGH ｜ 2D
10-09  C +2.7k / P +1.3k ｜ Activity HIGH ｜ 9D
10-16  C +1.6k / P +2.4k ｜ Activity HIGH ｜ 16D
10-23  C +1.3k / P +0.9k ｜ Activity HIGH ｜ 23D

📆 10-02 Forward Structure
存量OI: C 49.5k / P 53.5k，今日变化ΔOI: C +12.6k / P +6.9k，平值价格ATM: C $6.99 / P $7.20 ｜ ATM IV 86.5%，净 delta 敞口 -504k shares
Top ΔOI: P 290 +1,375 ｜ C 300 +1,218
仓位参考: Max Pain 280 ｜ Call Wall 300（+8.3%）（OI 5.2k） ｜ Put Wall 250（-9.7%，弱）（OI 3.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 86.5%｜历史 Rank 49%（近端代理）｜IV/RV 1.03×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 504,201 股

📆 10-09 Forward Structure
存量OI: C 12.6k / P 16.3k，今日变化ΔOI: C +2.7k / P +1.3k，平值价格ATM: C $13.09 / P $12.75 ｜ ATM IV 74.2%，净 delta 敞口 -55k shares
Top ΔOI: P 240 -780 ｜ P 290 +690
仓位参考: Max Pain 270 ｜ Call Wall 300（+8.3%，弱）（OI 0.9k） ｜ Put Wall 250（-9.7%，弱）（OI 1.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 74.2%｜历史 Rank 49%（近端代理）｜IV/RV 0.89×（近似）｜净 delta 敞口 负 54,946 股

📆 10-16 Forward Structure
存量OI: C 71.2k / P 78.6k，今日变化ΔOI: C +1.6k / P +2.4k，平值价格ATM: C $18.18 / P $17.05 ｜ ATM IV 74.2%，净 delta 敞口 -250k shares
Top ΔOI: C 270 -934 ｜ P 230 -915 ｜ P 277 +857
仓位参考: Max Pain 260 ｜ Call Wall 270（-2.5%，弱）（OI 8.2k） ｜ Put Wall 260（-6.1%，弱）（OI 3.7k）
量化解读： 存量两侧均衡｜ATM IV 74.2%｜历史 Rank 49%（近端代理）｜IV/RV 0.89×（近似）｜净 delta 敞口 负 249,848 股

📆 10-23 Forward Structure
存量OI: C 10.2k / P 14.2k，今日变化ΔOI: C +1.3k / P +0.9k，平值价格ATM: C $22.20 / P $18.51 ｜ ATM IV 75.8%，净 delta 敞口 -28k shares
Top ΔOI: P 220 +540 ｜ P 275 +481 ｜ C 325 +470
仓位参考: Max Pain 265 ｜ Call Wall 300（+8.3%，弱）（OI 0.8k） ｜ Put Wall 250（-9.7%，弱）（OI 0.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 75.8%｜历史 Rank 49%（近端代理）｜IV/RV 0.90×（近似）｜净 delta 敞口 负 27,822 股

📅 事件差分（观察，非因果）: 10-02（2D）ATM IV 86.5% vs 10-09 74.2%（差 +12.3pp）——覆盖 PCE 物价 Price Index MoM、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-30/BE_evening.json