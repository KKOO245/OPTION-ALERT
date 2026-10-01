# 期权晚报 2026-09-30（快照 21:00 ET）

📊 市场环境

SPY $762.63 ｜ QQQ $nan
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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 410.45 → 收盘 406.63（-0.9%） ｜ 今日高 410.74 ｜ 低 405.51 ｜ 昨收 412.18 → 收盘 406.63（-1.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.32 | OI比 1.57 | ATM IV 40.3% | Skew -2.8pp | Term 1.05 | ExpMove ±2.0%（近端） | Rank 51%
量化视角： IV 中性（Rank 51%）｜期限结构正常（Term 1.05）｜Put 保护异常便宜（Skew -2.8pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.32×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.57×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-02（2D）±2.0% ｜ 10-09（9D）±3.6% ｜ 10-16（16D）±5.5% ｜ 10-23（23D）±10.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,778,317 | GEX Change vs 上次快照 -381,567 | Flip: Primary Flip: 390.77（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 293 / LOW 165 / INVALID 404
结构观察区: Primary Flip 390.77（全链重定价，覆盖 97%）
Call Wall 420（弱结构｜现价低于该位 3.2%）
最近结构参考: Call Wall 420（现价低于该位 3.2%）
量化视角： 正 Gamma（278万，无历史分位）｜正 Gamma 减弱（38万）｜现价位于 Flip 上方 4.06%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 392（MaxPain，仅结算参考）；上方 420（Call Wall，弱结构）。
• Gamma 区域：切换参考 391（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C +0 / P +0 ｜ Activity LOW ｜ 2D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 9D
10-16  C +0 / P +0 ｜ Activity LOW ｜ 16D
10-23  C +0 / P +0 ｜ Activity LOW ｜ 23D

📆 10-02 Forward Structure
存量OI: C 2.2k / P 3.5k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $4.50 / P $3.74 ｜ ATM IV 40.3%，净 delta 敞口 0 shares
仓位参考: Max Pain 392 ｜ Call Wall 410（+0.8%，弱）（OI 0.3k）
量化解读： 存量 Put 重｜ATM IV 40.3%｜历史 Rank 51%（近端代理）｜IV/RV 1.53×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

10-09（Activity LOW）仓位参考: Max Pain 375 ｜ Call Wall 420（+3.3%，弱）（OI 0.1k） ｜ Put Wall 370（-9.0%，弱）（OI 17）

10-16（Activity LOW）仓位参考: Max Pain 390 ｜ Call Wall 400（-1.6%，弱）（OI 0.9k） ｜ Put Wall 380（-6.5%，弱）（OI 0.6k）

10-23（Activity LOW）仓位参考: Max Pain 415 ｜ Call Wall 425（+4.5%）（OI 0.5k） ｜ Put Wall 415（+2.1%）（OI 0.5k）

📅 事件差分（观察，非因果）: 10-02（2D）ATM IV 40.3% vs 10-09 31.0%（差 +9.3pp）——覆盖 PCE 物价 Price Index MoM、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-30/ISRG_evening.json