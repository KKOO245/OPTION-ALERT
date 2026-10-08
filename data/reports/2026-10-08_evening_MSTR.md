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
🟡 **近现价集中开仓**: 10-16 150P ΔOI -4,932（距现价 -1.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 150.18 → 收盘 151.47（+0.9%） ｜ 今日高 153.63 ｜ 低 147.41 ｜ 昨收 153.37 → 收盘 151.47（-1.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.44 | OI比 0.77 | ATM IV 70.9% | Skew -7.1pp | Term 0.93 | ExpMove ±3.1%（近端） | Rank 30%
量化视角： IV 中性（Rank 30%）｜期限结构正常（Term 0.93）｜Put 保护异常便宜（Skew -7.1pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.77）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.44×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.77×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（1D）±3.1% ｜ 10-16（8D）±7.2% ｜ 10-23（15D）±9.7% ｜ 10-30（22D）±12.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 6,121,352 | GEX Change vs 上次快照 14,319,563 | Flip: Primary Flip: 150.45（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 660 / LOW 110 / INVALID 172
结构观察区: Primary Flip 150.45（全链重定价，覆盖 99%）
最近结构参考: Flip 150（现价高于该位 0.7%）
量化视角： 正 Gamma（612万，无历史分位）｜由负转正（+1432万）｜现价位于 Flip 上方 0.68%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 155（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 150（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +2.0k / P +10.2k ｜ Activity HIGH ｜ 1D
10-16  C +18.2k / P +4.1k ｜ Activity HIGH ｜ 8D
10-23  C +5.2k / P +7.3k ｜ Activity HIGH ｜ 15D
10-30  C +4.5k / P +3.4k ｜ Activity HIGH ｜ 22D

📆 10-09 Forward Structure
存量OI: C 216.8k / P 167.1k，今日变化ΔOI: C +2.0k / P +10.2k，平值价格ATM: C $1.82 / P $2.81 ｜ ATM IV 70.9%，净 delta 敞口 111k shares
仓位参考: Max Pain 155 ｜ Call Wall 165（+8.9%，弱）（OI 26.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 70.9%｜历史 Rank 30%（近端代理）｜IV/RV 0.94×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 110,997 股

📆 10-16 Forward Structure
存量OI: C 202.1k / P 188.1k，今日变化ΔOI: C +18.2k / P +4.1k，平值价格ATM: C $5.05 / P $5.90 ｜ ATM IV 61.3%，净 delta 敞口 421k shares
Top ΔOI: P 142 +6,394 ｜ C 170 +6,100 ｜ P 150 -4,932
仓位参考: Max Pain 130 ｜ Call Wall 160（+5.6%，弱）（OI 12.2k） ｜ Put Wall 142（-6.3%，弱）（OI 6.9k）
量化解读： 存量两侧均衡｜ATM IV 61.3%｜历史 Rank 30%（近端代理）｜IV/RV 0.82×（近似）｜净 delta 敞口 正 420,573 股

📆 10-23 Forward Structure
存量OI: C 31.8k / P 47.4k，今日变化ΔOI: C +5.2k / P +7.3k，平值价格ATM: C $7.22 / P $7.47 ｜ ATM IV 60.4%，净 delta 敞口 -170k shares
Top ΔOI: P 138 +2,461 ｜ P 160 +2,407 ｜ C 190 +2,382
仓位参考: Max Pain 160 ｜ Call Wall 165（+8.9%，弱）（OI 2.1k） ｜ Put Wall 160（+5.6%）（OI 6.2k）
量化解读： 存量 Put 重｜ATM IV 60.4%｜历史 Rank 30%（近端代理）｜IV/RV 0.80×（近似）｜净 delta 敞口 负 169,530 股

📆 10-30 Forward Structure
存量OI: C 26.7k / P 35.1k，今日变化ΔOI: C +4.5k / P +3.4k，平值价格ATM: C $9.52 / P $9.73 ｜ ATM IV 63.0%，净 delta 敞口 -19k shares
Top ΔOI: C 210 +3,318 ｜ P 130 +1,063 ｜ P 140 +862
仓位参考: Max Pain 160 ｜ Call Wall 162.5（+7.3%，弱）（OI 2.6k） ｜ Put Wall 160（+5.6%，弱）（OI 3.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 63.0%｜历史 Rank 30%（近端代理）｜IV/RV 0.84×（近似）｜净 delta 敞口 负 18,589 股

📅 事件差分（观察，非因果）: 10-09（1D）ATM IV 70.9% vs 10-16 61.3%（差 +9.6pp）——覆盖 密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-08/MSTR_evening.json