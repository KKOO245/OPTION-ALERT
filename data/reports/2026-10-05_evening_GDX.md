# 期权晚报 2026-10-05（快照 21:00 ET）

📊 市场环境

SPY $774.83 ｜ QQQ $nan
VIX 15.52 ↑1.4%（5D -3.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 43.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-05

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周一 10-05 10:00　【高】ISM 非制造业 PMI　预测 55 ｜ 实际 54.9 ｜ 前值 55.4　✅ 今日已公布
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 87.84 → 收盘 87.42（-0.5%） ｜ 今日高 88.18 ｜ 低 85.99 ｜ 昨收 87.78 → 收盘 87.42（-0.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.38 | OI比 0.35 | ATM IV 41.2% | Skew -2.2pp | Term 0.94 | ExpMove ±3.7%（近端） | Rank 61%
量化视角： IV 中性（Rank 61%）｜期限结构正常（Term 0.94）｜Put 保护异常便宜（Skew -2.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.35）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.38×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.35×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（4D）±3.7% ｜ 10-16（11D）±5.6% ｜ 10-19（14D）±5.8% ｜ 10-23（18D）±7.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 31,702,290 | GEX Change vs 上次快照 11,626,792 | Flip: Primary Flip: 85.45（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 397 / LOW 105 / INVALID 398
结构观察区: Primary Flip 85.45（全链重定价，覆盖 96%）
Put Wall 85（弱结构｜现价高于该位 2.8%） | Call Wall 90（弱结构｜现价低于该位 2.9%）
最近结构参考: Flip 85（现价高于该位 2.3%）
量化视角： 正 Gamma（3170万，无历史分位）｜正 Gamma 增强（+1163万）｜现价位于 Flip 上方 2.30%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 85（Put Wall，弱结构） / 87（MaxPain，仅结算参考）；上方 90（Call Wall，弱结构）。
• Gamma 区域：切换参考 85（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +0 / P +0 ｜ Activity LOW ｜ 4D
10-16  C +0 / P +0 ｜ Activity LOW ｜ 11D
10-19  C +0 / P +0 ｜ Activity LOW ｜ 14D
10-23  C +0 / P +0 ｜ Activity LOW ｜ 18D

📆 10-09 Forward Structure
存量OI: C 88.8k / P 30.7k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $2.04 / P $1.21 ｜ ATM IV 41.2%，净 delta 敞口 0 shares
仓位参考: Max Pain 87 ｜ Call Wall 88（+0.7%，弱）（OI 16.3k） ｜ Put Wall 82（-6.2%，弱）（OI 6.7k）
量化解读： 存量 Call 重｜ATM IV 41.2%｜历史 Rank 61%（近端代理）｜IV/RV 1.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-16（Activity LOW）仓位参考: Max Pain 92 ｜ Call Wall 90（+3.0%，弱）（OI 8.5k） ｜ Put Wall 90（+3.0%，弱）（OI 10.5k）

10-23（Activity LOW）仓位参考: Max Pain 94 ｜ Call Wall 90（+3.0%，弱）（OI 0.4k） ｜ Put Wall 93（+6.4%，弱）（OI 1.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-05/GDX_evening.json