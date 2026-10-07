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


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 87.72 → 收盘 88.22（+0.6%） ｜ 今日高 88.92 ｜ 低 86.66 ｜ 昨收 87.42 → 收盘 88.22（+0.9%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.31 | OI比 0.34 | ATM IV 38.9% | Skew -0.3pp | Term 1.02 | ExpMove ±2.9%（近端） | Rank 53%
量化视角： IV 中性（Rank 53%）｜期限结构正常（Term 1.02）｜Put 保护异常便宜（Skew -0.3pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.34）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.31×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.34×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（3D）±2.9% ｜ 10-16（10D）±5.1% ｜ 10-19（13D）±5.2% ｜ 10-21（15D）±3.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 58,144,602 | GEX Change vs 上次快照 33,741,947 | Flip: Primary Flip: 85.77（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 427 / LOW 119 / INVALID 414
结构观察区: Primary Flip 85.77（全链重定价，覆盖 97%）
Put Wall 85（弱结构｜现价高于该位 3.8%） | Call Wall 90（弱结构｜现价低于该位 2.0%）
最近结构参考: Call Wall 90（现价低于该位 2.0%）
量化视角： 正 Gamma（5814万，无历史分位）｜正 Gamma 增强（+3374万）｜现价位于 Flip 上方 2.86%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 85（Put Wall，弱结构） / 87（MaxPain，仅结算参考）；上方 90（Call Wall，弱结构）。
• Gamma 区域：切换参考 86（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +0 / P +0 ｜ Activity LOW ｜ 3D
10-16  C +0 / P +0 ｜ Activity LOW ｜ 10D
10-19  C +0 / P +0 ｜ Activity LOW ｜ 13D
10-21  C +0 / P +0 ｜ Activity LOW ｜ 15D

📆 10-09 Forward Structure
存量OI: C 91.0k / P 31.1k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $1.38 / P $1.13 ｜ ATM IV 38.9%，净 delta 敞口 0 shares
仓位参考: Max Pain 87 ｜ Call Wall 88（-0.2%，弱）（OI 16.3k） ｜ Put Wall 85（-3.6%，弱）（OI 6.1k）
量化解读： 存量 Call 重｜ATM IV 38.9%｜历史 Rank 53%（近端代理）｜IV/RV 1.12×（近似）｜净 delta 敞口 正 0 股

10-16（Activity LOW）仓位参考: Max Pain 91 ｜ Call Wall 90（+2.0%，弱）（OI 8.5k） ｜ Put Wall 90（+2.0%，弱）（OI 10.5k）

10-19（Activity LOW）仓位参考: Max Pain 90 ｜ Call Wall 93（+5.4%）（OI 62） ｜ Put Wall 87（-1.4%，弱）（OI 10）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-06/GDX_evening.json