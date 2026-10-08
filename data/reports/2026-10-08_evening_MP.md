# 期权晚报 2026-10-08（快照 16:40 ET）

📊 市场环境

SPY $773.93 ｜ QQQ $747.58
VIX 15.41 ↑2.2%（5D -6.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-08

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 48C ΔOI +455（距现价 +4.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 45.37 → 收盘 46.14（+1.7%） ｜ 今日高 46.75 ｜ 低 45.28 ｜ 昨收 46.31 → 收盘 46.14（-0.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.02 | OI比 0.79 | ATM IV 57.7% | Skew -7.2pp | Term 1.01 | ExpMove ±2.2%（近端） | Rank 32%
量化视角： IV 中性（Rank 32%）｜期限结构正常（Term 1.01）｜Put 保护异常便宜（Skew -7.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.79）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.02×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.79×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（1D）±2.2% ｜ 10-16（8D）±6.5% ｜ 10-23（15D）±8.7% ｜ 10-30（22D）±10.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -6,788,167 | GEX Change vs 上次快照 -618,300 | Flip: Primary Flip: 47.73（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 284 / LOW 66 / INVALID 102
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 47.73（全链重定价，覆盖 96%）
Put Wall 45（现价高于该位 2.5%） | Call Wall 50（弱结构｜现价低于该位 7.7%）
最近结构参考: Put Wall 45（现价高于该位 2.5%）
量化视角： 负 Gamma（679万，无历史分位）｜负 Gamma 加深（62万）｜现价位于 Flip 下方 3.33%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 45（Put Wall）；上方 48（MaxPain，仅结算参考） / 50（Call Wall，弱结构）。
• Gamma 区域：切换参考 48（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +0.3k / P +0.4k ｜ Activity MEDIUM △ ｜ 1D
10-16  C +0.6k / P +0.6k ｜ Activity HIGH ｜ 8D
10-23  C +0.2k / P +0.1k ｜ Activity HIGH ｜ 15D
10-30  C +0.2k / P +0.3k ｜ Activity MEDIUM △ ｜ 22D

📆 10-09 Forward Structure
存量OI: C 12.0k / P 9.5k，今日变化ΔOI: C +0.3k / P +0.4k，平值价格ATM: C $0.54 / P $0.50 ｜ ATM IV 57.7%，净 delta 敞口 20k shares
Top ΔOI: C 48 +455 ｜ C 50 -256
仓位参考: Max Pain 48 ｜ Call Wall 50（+8.4%，弱）（OI 1.9k） ｜ Put Wall 47（+1.9%）（OI 2.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 57.7%｜历史 Rank 32%（近端代理）｜IV/RV 1.23×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 20,476 股

📆 10-16 Forward Structure
存量OI: C 20.9k / P 17.2k，今日变化ΔOI: C +0.6k / P +0.6k，平值价格ATM: C $1.53 / P $1.45 ｜ ATM IV 52.4%，净 delta 敞口 20k shares
Top ΔOI: C 50 +356
仓位参考: Max Pain 50 ｜ Call Wall 50（+8.4%）（OI 4.5k） ｜ Put Wall 45（-2.5%，弱）（OI 4.4k）
量化解读： 存量 Call 重｜ATM IV 52.4%｜历史 Rank 32%（近端代理）｜IV/RV 1.12×（近似）｜净 delta 敞口 正 19,502 股

📆 10-23 Forward Structure
存量OI: C 3.3k / P 1.9k，今日变化ΔOI: C +0.2k / P +0.1k，平值价格ATM: C $1.91 / P $2.12 ｜ ATM IV 52.7%，净 delta 敞口 -3k shares
Top ΔOI: C 50 +58
仓位参考: Max Pain 50 ｜ Call Wall 50（+8.4%，弱）（OI 0.2k） ｜ Put Wall 45（-2.5%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 52.7%｜历史 Rank 32%（近端代理）｜IV/RV 1.13×（近似）｜净 delta 敞口 负 2,930 股

10-30（MEDIUM △）Top ΔOI: 48P +59
10-30（MEDIUM △）仓位参考: Max Pain 48 ｜ Call Wall 50（+8.4%，弱）（OI 0.3k） ｜ Put Wall 44（-4.6%）（OI 1.6k）

📅 事件差分（观察，非因果）: 10-09（1D）ATM IV 57.7% vs 10-16 52.4%（差 +5.3pp）——覆盖 密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-08/MP_evening.json