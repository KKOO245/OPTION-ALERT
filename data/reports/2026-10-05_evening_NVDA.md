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


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 236.07 → 收盘 238.90（+1.2%） ｜ 今日高 240.10 ｜ 低 235.15 ｜ 昨收 233.95 → 收盘 238.90（+2.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.01 | OI比 0.70 | ATM IV 29.6% | Skew 0.7pp | Term 0.97 | ExpMove ±1.8%（近端） | Rank 7%
量化视角： IV 历史低位（Rank 7%，期权偏便宜）｜期限结构正常（Term 0.97）｜保护溢价薄（Skew 0.7pp）｜存量 Call 偏重（OI比 0.70）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.01×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.70×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-07（2D）±1.8% ｜ 10-09（4D）±2.5% ｜ 10-12（7D）±2.9% ｜ 10-14（9D）±3.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 574,264,836 | GEX Change vs 上次快照 17,619,079 | Flip: Primary Flip: 221.80（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 619 / LOW 156 / INVALID 501
结构观察区: Primary Flip 221.80（全链重定价，覆盖 100%）
Put Wall 220（弱结构｜现价高于该位 8.6%） | Call Wall 240（弱结构｜现价低于该位 0.5%）
最近结构参考: Call Wall 240（现价低于该位 0.5%）
量化视角： 正 Gamma（5.74亿，无历史分位）｜正 Gamma 增强（+1762万）｜现价位于 Flip 上方 7.71%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 220（Put Wall，弱结构） / 230（MaxPain，仅结算参考）；上方 240（Call Wall，弱结构）。
• Gamma 区域：切换参考 222（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-07  C +0 / P +0 ｜ Activity LOW ｜ 2D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 4D
10-12  C +0 / P +0 ｜ Activity LOW ｜ 7D
10-14  C +0 / P +0 ｜ Activity LOW ｜ 9D

📆 10-07 Forward Structure
存量OI: C 59.5k / P 41.5k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $1.59 / P $2.69 ｜ ATM IV 29.6%，净 delta 敞口 0 shares
仓位参考: Max Pain 230 ｜ Call Wall 247.5（+3.6%，弱）（OI 9.9k） ｜ Put Wall 230（-3.7%）（OI 10.2k）
量化解读： 存量 Call 重｜ATM IV 29.6%｜历史 Rank 7%（近端代理）｜IV/RV 1.36×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-09（Activity LOW）仓位参考: Max Pain 230 ｜ Call Wall 240（+0.5%）（OI 78.3k） ｜ Put Wall 230（-3.7%，弱）（OI 26.5k）

10-12（Activity LOW）仓位参考: Max Pain 230 ｜ Call Wall 240（+0.5%）（OI 4.7k） ｜ Put Wall 222.5（-6.9%）（OI 1.7k）

10-14（Activity LOW）仓位参考: Max Pain 230 ｜ Call Wall 255（+6.7%，弱）（OI 1.0k） ｜ Put Wall 225（-5.8%，弱）（OI 0.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-05/NVDA_evening.json