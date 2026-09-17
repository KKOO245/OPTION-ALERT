# 期权晚报 2026-09-16（快照 21:12 ET）

📊 市场环境

SPY $754.05 ｜ QQQ $704.72
VIX 17.71 ↑3.0%（5D +7.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 26.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.8 ｜ 实际 1.2 ｜ 前值 -0.5　✅ 今日已公布
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 4 ｜ 前值 3.75　✅ 今日已公布
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布　✅ 今日已公布
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布　✅ 今日已公布
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 357.71 → 收盘 358.08（+0.1%） ｜ 今日高 365.10 ｜ 低 354.89 ｜ 昨收 356.58 → 收盘 358.08（+0.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.78 | OI比 0.82 | ATM IV 46.9% | Skew -0.2pp | Term 0.89 | ExpMove ±2.8%（近端） | Rank 28%
量化视角： IV 中性（Rank 28%）｜期限结构倒挂（Term 0.89，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.82）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.78×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.82×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（2D）±2.8% ｜ 09-21（5D）±3.6% ｜ 09-23（7D）±4.5% ｜ 09-25（9D）±5.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 14,069,640 | GEX Change vs 上次快照 -92,328,605 | Flip: Primary Flip: 356.72（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 1116 / LOW 176 / INVALID 630
结构观察区: Primary Flip 356.72（全链重定价，覆盖 97%）
最近结构参考: Flip 357（现价高于该位 0.4%）
量化视角： 正 Gamma（1407万，无历史分位）｜正 Gamma 减弱（9233万）｜现价位于 Flip 上方 0.38%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 360（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 357（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-18  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-21  C +0 / P +0 ｜ Activity LOW ｜ 5D
09-23  C +0 / P +0 ｜ Activity LOW ｜ 7D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 9D

📆 09-18 Forward Structure
存量OI: C 588.9k / P 485.5k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $5.50 / P $4.57 ｜ ATM IV 46.9%，净 delta 敞口 0 shares
仓位参考: Max Pain 360 ｜ Call Wall 370（+3.3%，弱）（OI 22.3k） ｜ Put Wall 350（-2.3%，弱）（OI 17.7k）
量化解读： 存量 Call 重｜ATM IV 46.9%｜历史 Rank 28%（近端代理）｜IV/RV 0.96×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-21（Activity LOW）仓位参考: Max Pain 360 ｜ Call Wall 380（+6.1%，弱）（OI 1.7k） ｜ Put Wall 360（+0.5%，弱）（OI 1.8k）

09-23（Activity LOW）仓位参考: Max Pain 362 ｜ Call Wall 375（+4.7%，弱）（OI 0.9k） ｜ Put Wall 330（-7.8%）（OI 1.5k）

09-25（Activity LOW）仓位参考: Max Pain 358 ｜ Call Wall 385（+7.5%，弱）（OI 5.8k） ｜ Put Wall 350（-2.3%，弱）（OI 3.5k）

📅 事件差分（观察，非因果）: 09-18（2D）ATM IV 46.9% vs 09-21 37.7%（差 +9.2pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-16/TSLA_evening.json