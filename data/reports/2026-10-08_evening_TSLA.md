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
🟡 **近现价集中开仓**: 10-09 380C ΔOI +3,559（距现价 +1.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 374.12 → 收盘 375.00（+0.2%） ｜ 今日高 375.96 ｜ 低 368.03 ｜ 昨收 377.81 → 收盘 375.00（-0.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.91 | OI比 1.05 | ATM IV 35.6% | Skew 0.6pp | Term 1.22 | ExpMove ±1.5%（近端） | Rank 6%
量化视角： IV 历史低位（Rank 6%，期权偏便宜）｜期限结构正常偏陡（Term 1.22）｜保护溢价薄（Skew 0.6pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.91×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.05×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-09（1D）±1.5% ｜ 10-12（4D）±2.3% ｜ 10-14（6D）±3.4% ｜ 10-16（8D）±4.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 104,053,367 | GEX Change vs 上次快照 36,461,717 | Flip: Primary Flip: 365.66（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1074 / LOW 124 / INVALID 526
结构观察区: Primary Flip 365.66（全链重定价，覆盖 99%）
Call Wall 400（现价低于该位 6.2%）
最近结构参考: Flip 366（现价高于该位 2.6%）
量化视角： 正 Gamma（1.04亿，无历史分位）｜正 Gamma 增强（+3646万）｜现价位于 Flip 上方 2.55%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 370（MaxPain，仅结算参考）；上方 400（Call Wall）。
• Gamma 区域：切换参考 366（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +20.5k / P +13.5k ｜ Activity MEDIUM △ ｜ 1D
10-12  C +5.1k / P +6.5k ｜ Activity HIGH ｜ 4D
10-14  C +1.8k / P +1.4k ｜ Activity HIGH ｜ 6D
10-16  C +9.6k / P +7.0k ｜ Activity MEDIUM △ ｜ 8D

📆 10-09 Forward Structure
存量OI: C 214.8k / P 225.3k，今日变化ΔOI: C +20.5k / P +13.5k，平值价格ATM: C $2.90 / P $2.72 ｜ ATM IV 35.6%，净 delta 敞口 -136k shares
Top ΔOI: C 380 +3,559 ｜ P 377 +2,987 ｜ C 385 +2,615
仓位参考: Max Pain 370 ｜ Call Wall 400（+6.7%）（OI 23.8k） ｜ Put Wall 370（-1.3%，弱）（OI 8.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 35.6%｜历史 Rank 6%（近端代理）｜IV/RV 1.25×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 136,092 股

📆 10-12 Forward Structure
存量OI: C 22.9k / P 22.7k，今日变化ΔOI: C +5.1k / P +6.5k，平值价格ATM: C $4.39 / P $4.30 ｜ ATM IV 27.8%，净 delta 敞口 -16k shares
Top ΔOI: C 405 +1,071 ｜ C 400 +735
仓位参考: Max Pain 372 ｜ Call Wall 400（+6.7%，弱）（OI 2.4k） ｜ Put Wall 370（-1.3%，弱）（OI 1.4k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 27.8%｜历史 Rank 6%（近端代理）｜IV/RV 0.98×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 15,891 股

📆 10-14 Forward Structure
存量OI: C 8.3k / P 6.7k，今日变化ΔOI: C +1.8k / P +1.4k，平值价格ATM: C $6.45 / P $6.10 ｜ ATM IV 32.9%，净 delta 敞口 13k shares
Top ΔOI: C 400 +380 ｜ C 405 +174 ｜ C 377 +162
仓位参考: Max Pain 370 ｜ Call Wall 400（+6.7%）（OI 1.4k） ｜ Put Wall 370（-1.3%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 32.9%｜历史 Rank 6%（近端代理）｜IV/RV 1.16×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 13,189 股

10-16（MEDIUM △）Top ΔOI: 385C +2,003 ｜ 340P +1,785
10-16（MEDIUM △）仓位参考: Max Pain 370 ｜ Call Wall 400（+6.7%）（OI 23.3k） ｜ Put Wall 380（+1.3%，弱）（OI 14.7k）

📅 事件差分（观察，非因果）: 10-09（1D）ATM IV 35.6% vs 10-12 27.8%（差 +7.8pp）——覆盖 密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-08/TSLA_evening.json