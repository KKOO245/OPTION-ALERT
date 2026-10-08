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
🟡 **近现价集中开仓**: 10-09 144C ΔOI +1,366（距现价 +3.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NOW

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NOW: 今开 139.25 → 收盘 139.75（+0.4%） ｜ 今日高 142.50 ｜ 低 135.58 ｜ 昨收 137.87 → 收盘 139.75（+1.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.33 | OI比 0.71 | ATM IV 52.3% | Skew -1.6pp | Term 1.18 | ExpMove ±2.3%（近端） | Rank 22%
量化视角： IV 历史低位（Rank 22%，期权偏便宜）｜期限结构正常偏陡（Term 1.18）｜Put 保护异常便宜（Skew -1.6pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.71）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.33×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.71×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（1D）±2.3% ｜ 10-16（8D）±5.9% ｜ 10-23（15D）±9.1% ｜ 10-30（22D）±12.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 23,204,103 | GEX Change vs 上次快照 4,623,314 | Flip: Primary Flip: 134.29（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 518 / LOW 58 / INVALID 122
结构观察区: Primary Flip 134.29（全链重定价，覆盖 98%）
Call Wall 150（现价低于该位 6.8%）
最近结构参考: Flip 134（现价高于该位 4.1%）
量化视角： 正 Gamma（2320万，无历史分位）｜正 Gamma 增强（+462万）｜现价位于 Flip 上方 4.06%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 136（MaxPain，仅结算参考）；上方 150（Call Wall）。
• Gamma 区域：切换参考 134（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +3.2k / P +0.7k ｜ Activity HIGH ｜ 1D
10-16  C +2.9k / P +1.0k ｜ Activity MEDIUM △ ｜ 8D
10-23  C +0.8k / P -52 ｜ Activity HIGH ｜ 15D
10-30  C +0.4k / P +0.3k ｜ Activity MEDIUM △ ｜ 22D

📆 10-09 Forward Structure
存量OI: C 27.9k / P 19.7k，今日变化ΔOI: C +3.2k / P +0.7k，平值价格ATM: C $1.47 / P $1.76 ｜ ATM IV 52.3%，净 delta 敞口 19k shares
Top ΔOI: C 144 +1,366 ｜ C 140 +887 ｜ C 147 +522
仓位参考: Max Pain 136 ｜ Call Wall 150（+7.3%，弱）（OI 5.2k） ｜ Put Wall 135（-3.4%，弱）（OI 1.5k）
量化解读： 存量 Call 重｜ATM IV 52.3%｜历史 Rank 22%（近端代理）｜IV/RV 1.81×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 18,931 股

10-16（MEDIUM △）Top ΔOI: 150C +725 ｜ 145C +608
10-16（MEDIUM △）仓位参考: Max Pain 130 ｜ Call Wall 150（+7.3%）（OI 14.9k） ｜ Put Wall 130（-7.0%，弱）（OI 4.5k）

📆 10-23 Forward Structure
存量OI: C 14.1k / P 17.0k，今日变化ΔOI: C +0.8k / P -52，平值价格ATM: C $5.80 / P $6.87 ｜ ATM IV 50.0%，净 delta 敞口 23k shares
Top ΔOI: C 150 +240 ｜ C 142 +183
仓位参考: Max Pain 134 ｜ Call Wall 140（+0.2%，弱）（OI 1.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 50.0%｜历史 Rank 22%（近端代理）｜IV/RV 1.73×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 23,325 股

10-30（MEDIUM △）仓位参考: Max Pain 135 ｜ Call Wall 150（+7.3%，弱）（OI 0.8k） ｜ Put Wall 130（-7.0%，弱）（OI 0.6k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-08/NOW_evening.json