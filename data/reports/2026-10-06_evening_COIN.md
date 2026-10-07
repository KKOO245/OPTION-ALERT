# 期权晚报 2026-10-06（快照 21:00 ET）

📊 市场环境

SPY $779.09 ｜ QQQ $759.66
VIX 15.01 ↓3.3%（5D -6.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 47.4（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-06

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 188.26 → 收盘 185.74（-1.3%） ｜ 今日高 192.80 ｜ 低 184.82 ｜ 昨收 188.22 → 收盘 185.74（-1.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.46 | OI比 0.55 | ATM IV 64.5% | Skew -3.6pp | Term 1.05 | ExpMove ±4.7%（近端） | Rank 19%
量化视角： IV 历史低位（Rank 19%，期权偏便宜）｜期限结构正常（Term 1.05）｜Put 保护异常便宜（Skew -3.6pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.55）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.46×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.55×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（3D）±4.7% ｜ 10-16（10D）±7.8% ｜ 10-23（17D）±10.0% ｜ 10-30（24D）±13.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 23,182,480 | GEX Change vs 上次快照 -7,893,433 | Flip: Primary Flip: 176.78（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 473 / LOW 116 / INVALID 249
结构观察区: Primary Flip 176.78（全链重定价，覆盖 100%）
Call Wall 200（弱结构｜现价低于该位 7.1%）
最近结构参考: Flip 177（现价高于该位 5.1%）
量化视角： 正 Gamma（2318万，无历史分位）｜正 Gamma 减弱（789万）｜现价位于 Flip 上方 5.07%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 188（MaxPain，仅结算参考） / 200（Call Wall，弱结构）。
• Gamma 区域：切换参考 177（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +0 / P +0 ｜ Activity LOW ｜ 3D
10-16  C +0 / P +0 ｜ Activity LOW ｜ 10D
10-23  C +0 / P +0 ｜ Activity LOW ｜ 17D
10-30  C +0 / P +0 ｜ Activity LOW ｜ 24D

📆 10-09 Forward Structure
存量OI: C 65.2k / P 36.2k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $4.80 / P $3.91 ｜ ATM IV 64.5%，净 delta 敞口 0 shares
仓位参考: Max Pain 188 ｜ Call Wall 195（+5.0%）（OI 12.8k） ｜ Put Wall 170（-8.5%，弱）（OI 2.0k）
量化解读： 存量 Call 重｜ATM IV 64.5%｜历史 Rank 19%（近端代理）｜IV/RV 0.87×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-16（Activity LOW）仓位参考: Max Pain 180 ｜ Call Wall 200（+7.7%，弱）（OI 7.0k） ｜ Put Wall 200（+7.7%，弱）（OI 3.9k）

10-23（Activity LOW）仓位参考: Max Pain 190 ｜ Call Wall 190（+2.3%，弱）（OI 0.8k） ｜ Put Wall 170（-8.5%，弱）（OI 0.4k）

10-30（Activity LOW）仓位参考: Max Pain 185 ｜ Call Wall 185（-0.4%，弱）（OI 1.2k） ｜ Put Wall 170（-8.5%，弱）（OI 0.7k）

📅 事件差分（观察，非因果）: 10-09（3D）ATM IV 64.5% vs 10-16 58.9%（差 +5.6pp）——覆盖 美联储议息会议 Minutes、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-06/COIN_evening.json