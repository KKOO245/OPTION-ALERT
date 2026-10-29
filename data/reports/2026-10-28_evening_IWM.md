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
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）


## IWM

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
IWM: 今开 280.35 → 收盘 281.29（+0.3%） ｜ 今日高 281.47 ｜ 低 279.05 ｜ 昨收 280.18 → 收盘 281.29（+0.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.56 | OI比 0.33 | ATM IV 19.6% | Skew 2.1pp | Term 0.92 | ExpMove ±0.8%（近端） | Rank 50%
量化视角： IV 中性（Rank 50%）｜期限结构正常（Term 0.92）｜保护溢价中性（Skew 2.1pp）｜存量 Call 偏重（OI比 0.33）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.56×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.33×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-29（1D）±0.8% ｜ 10-30（2D）±1.2% ｜ 11-02（5D）±1.5% ｜ 11-03（6D）±1.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 60,583,687 | GEX Change vs 上次快照 109,702,727 | Flip: Primary Flip: 280.84（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 1175 / LOW 164 / INVALID 1009
结构观察区: Primary Flip 280.84（全链重定价，覆盖 98%）
Put Wall 260（弱结构｜现价高于该位 8.2%） | Call Wall 290（弱结构｜现价低于该位 3.0%）
最近结构参考: Flip 281（现价高于该位 0.2%）
量化视角： 正 Gamma（6058万，无历史分位）｜由负转正（+1.10亿）｜现价位于 Flip 上方 0.16%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 260（Put Wall，弱结构） / 276（MaxPain，仅结算参考）；上方 290（Call Wall，弱结构）。
• Gamma 区域：切换参考 281（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-29  C +0 / P +0 ｜ Activity LOW ｜ 1D
10-30  C +0 / P +0 ｜ Activity LOW ｜ 2D
11-02  C +0 / P +0 ｜ Activity LOW ｜ 5D
11-03  C +0 / P +0 ｜ Activity LOW ｜ 6D

📆 10-29 Forward Structure
存量OI: C 80.0k / P 26.0k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $1.46 / P $0.89 ｜ ATM IV 19.6%，净 delta 敞口 0 shares
仓位参考: Max Pain 276 ｜ Call Wall 282（+0.3%，弱）（OI 18.3k） ｜ Put Wall 265（-5.8%，弱）（OI 4.5k）
量化解读： 存量 Call 重｜ATM IV 19.6%｜历史 Rank 50%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-30（Activity LOW）仓位参考: Max Pain 278 ｜ Call Wall 278（-1.2%，弱）（OI 20.9k） ｜ Put Wall 260（-7.6%）（OI 86.1k）

11-02（Activity LOW）仓位参考: Max Pain 276 ｜ Call Wall 287（+2.0%，弱）（OI 1.3k） ｜ Put Wall 270（-4.0%，弱）（OI 1.6k）

11-03（Activity LOW）仓位参考: Max Pain 277 ｜ Call Wall 282（+0.3%，弱）（OI 1.2k） ｜ Put Wall 270（-4.0%）（OI 2.5k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-28/IWM_evening.json