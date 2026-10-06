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


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 47.27 → 收盘 46.84（-0.9%） ｜ 今日高 47.80 ｜ 低 46.46 ｜ 昨收 46.97 → 收盘 46.84（-0.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.05 | OI比 0.82 | ATM IV 57.2% | Skew -7.2pp | Term 1.02 | ExpMove ±4.8%（近端） | Rank 31%
量化视角： IV 中性（Rank 31%）｜期限结构正常（Term 1.02）｜Put 保护异常便宜（Skew -7.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.82）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.05×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.82×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-09（4D）±4.8% ｜ 10-16（11D）±7.5% ｜ 10-23（18D）±10.2% ｜ 10-30（25D）±11.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -3,066,275 | GEX Change vs 上次快照 -908,752 | Flip: Primary Flip: 48.80（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 260 / LOW 49 / INVALID 127
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 48.80（全链重定价，覆盖 98%）
Put Wall 45（弱结构｜现价高于该位 4.1%） | Call Wall 50（弱结构｜现价低于该位 6.3%）
最近结构参考: Flip 49（现价低于该位 4.0%）
量化视角： 负 Gamma（307万，无历史分位）｜负 Gamma 加深（91万）｜现价位于 Flip 下方 4.02%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 45（Put Wall，弱结构）；上方 48（MaxPain，仅结算参考） / 50（Call Wall，弱结构）。
• Gamma 区域：切换参考 49（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +0 / P +0 ｜ Activity LOW ｜ 4D
10-16  C +0 / P +0 ｜ Activity LOW ｜ 11D
10-23  C +0 / P +0 ｜ Activity LOW ｜ 18D
10-30  C +0 / P +0 ｜ Activity LOW ｜ 25D

📆 10-09 Forward Structure
存量OI: C 8.5k / P 7.0k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $1.19 / P $1.06 ｜ ATM IV 57.2%，净 delta 敞口 0 shares
仓位参考: Max Pain 48 ｜ Call Wall 50（+6.7%，弱）（OI 1.0k） ｜ Put Wall 47（+0.3%）（OI 2.3k）
量化解读： 存量 Call 重｜ATM IV 57.2%｜历史 Rank 31%（近端代理）｜IV/RV 1.33×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-16（Activity LOW）仓位参考: Max Pain 50 ｜ Call Wall 50（+6.7%，弱）（OI 4.0k） ｜ Put Wall 45（-3.9%，弱）（OI 4.4k）

10-23（Activity LOW）仓位参考: Max Pain 50 ｜ Call Wall 50（+6.7%，弱）（OI 0.2k） ｜ Put Wall 45（-3.9%，弱）（OI 0.2k）

10-30（Activity LOW）仓位参考: Max Pain 49 ｜ Call Wall 50（+6.7%，弱）（OI 0.3k） ｜ Put Wall 43（-8.2%，弱）（OI 0.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-05/MP_evening.json