# 期权晚报 2026-10-07（快照 16:40 ET）

📊 市场环境

SPY $777.22 ｜ QQQ $757.73
VIX 15.08 ↑0.5%（5D -7.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 44.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-07

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布　✅ 今日已公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-09 85P ΔOI +351（距现价 -0.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-19 80P ΔOI +23 占该期限总 OI 10.1%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 85.32 → 收盘 85.46（+0.2%） ｜ 今日高 86.39 ｜ 低 84.36 ｜ 昨收 88.22 → 收盘 85.46（-3.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.58 | OI比 0.33 | ATM IV 40.2% | Skew -1.9pp | Term 1.00 | ExpMove ±2.6%（近端） | Rank 57%
量化视角： IV 中性（Rank 57%）｜期限结构正常（Term 1.00）｜Put 保护异常便宜（Skew -1.9pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.33）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.58×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.33×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（2D）±2.6% ｜ 10-16（9D）±5.0% ｜ 10-19（12D）±5.1% ｜ 10-21（14D）±5.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,128,297 | GEX Change vs 上次快照 4,108,412 | Flip: Primary Flip: 85.36（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 429 / LOW 137 / INVALID 402
结构观察区: Primary Flip 85.36（全链重定价，覆盖 94%）
Put Wall 85（弱结构｜现价高于该位 0.5%） | Call Wall 90（弱结构｜现价低于该位 5.0%）
最近结构参考: Flip 85（现价高于该位 0.1%）
量化视角： 正 Gamma（213万，无历史分位）｜由负转正（+411万）｜现价位于 Flip 上方 0.12%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 85（Put Wall，弱结构）；上方 87（MaxPain，仅结算参考） / 90（Call Wall，弱结构）。
• Gamma 区域：切换参考 85（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +5.7k / P +0.9k ｜ Activity HIGH ｜ 2D
10-16  C +3.8k / P +4.6k ｜ Activity MEDIUM △ ｜ 9D
10-19  C +37 / P +83 ｜ Activity MEDIUM △ ｜ 12D
10-21  C +28 / P +13 ｜ Activity LOW ｜ 14D

📆 10-09 Forward Structure
存量OI: C 96.8k / P 32.0k，今日变化ΔOI: C +5.7k / P +0.9k，平值价格ATM: C $1.45 / P $0.80 ｜ ATM IV 40.2%，净 delta 敞口 -23k shares
Top ΔOI: C 91 +3,977 ｜ P 85 +351
仓位参考: Max Pain 87 ｜ Call Wall 88（+3.0%，弱）（OI 16.4k） ｜ Put Wall 82（-4.0%，弱）（OI 6.8k）
量化解读： 存量 Call 重｜ATM IV 40.2%｜历史 Rank 57%（近端代理）｜IV/RV 1.20×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 22,829 股

10-16（MEDIUM △）Top ΔOI: 84P +1,537 ｜ 94C +1,298
10-16（MEDIUM △）仓位参考: Max Pain 90 ｜ Call Wall 90（+5.3%，弱）（OI 9.0k） ｜ Put Wall 90（+5.3%，弱）（OI 10.5k）

10-19（MEDIUM △）Top ΔOI: 80P +23 ｜ 90P +22
10-19（MEDIUM △）仓位参考: Max Pain 90 ｜ Call Wall 90（+5.3%，弱）（OI 13） ｜ Put Wall 80（-6.4%，弱）（OI 24）

10-21（Activity LOW）仓位参考: Max Pain 85 ｜ Call Wall 90（+5.3%，弱）（OI 10） ｜ Put Wall 85（-0.5%）（OI 10）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-07/GDX_evening.json