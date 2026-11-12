# 期权晚报 2026-11-12（快照 16:40 ET）

📊 市场环境

SPY $757.12 ｜ QQQ $688.17
VIX 18.70 ↑6.9%（5D -33.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 39.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-12

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 3.75 ｜ 前值 3.97　✅ 今日已公布
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **事件差分**: 11-13 ATM IV 113.0% vs 11-20 98.2%（差 +14.8pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-13 205P ΔOI +4,515（距现价 +1.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 195.89 → 收盘 201.93（+3.1%） ｜ 今日高 208.90 ｜ 低 193.44 ｜ 昨收 209.47 → 收盘 201.93（-3.6%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.02 | OI比 1.16 | ATM IV 113.0% | Skew 2.9pp | Term 0.78 | ExpMove ±4.8%（近端） | Rank 72%
量化视角： IV 中性（Rank 72%）｜期限结构倒挂（Term 0.78，近月 IV 高于远月）｜保护溢价中性（Skew 2.9pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.02×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.16×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-13（1D）±4.8% ｜ 11-20（8D）±11.6% ｜ 11-27（15D）±13.2% ｜ 12-04（22D）±17.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -5,615,266 | GEX Change vs 上次快照 3,700,442 | Flip: Primary Flip: 207.89（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 611 / LOW 150 / INVALID 183
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 207.89（全链重定价，覆盖 99%）
Put Wall 200（弱结构｜现价高于该位 1.0%） | Call Wall 220（弱结构｜现价低于该位 8.2%）
最近结构参考: Put Wall 200（现价高于该位 1.0%）
量化视角： 负 Gamma（562万，无历史分位）｜负 Gamma 缓解（+370万）｜现价位于 Flip 下方 2.87%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall，弱结构） / 198（MaxPain，仅结算参考）；上方 220（Call Wall，弱结构）。
• Gamma 区域：切换参考 208（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +2.8k / P +17.8k ｜ Activity HIGH ｜ 1D
11-20  C +1.6k / P +4.1k ｜ Activity HIGH ｜ 8D
11-27  C +0.7k / P +0.4k ｜ Activity HIGH ｜ 15D
12-04  C +0.3k / P +77 ｜ Activity MEDIUM △ ｜ 22D

📆 11-13 Forward Structure
存量OI: C 46.2k / P 53.5k，今日变化ΔOI: C +2.8k / P +17.8k，平值价格ATM: C $4.52 / P $5.10 ｜ ATM IV 113.0%，净 delta 敞口 -520k shares
Top ΔOI: P 185 +8,638 ｜ P 205 +4,515
仓位参考: Max Pain 198 ｜ Call Wall 220（+8.9%，弱）（OI 2.9k） ｜ Put Wall 185（-8.4%）（OI 9.5k）
量化解读： 存量两侧均衡｜ATM IV 113.0%｜历史 Rank 72%（近端代理）｜IV/RV 0.90×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 519,785 股

📆 11-20 Forward Structure
存量OI: C 81.8k / P 85.2k，今日变化ΔOI: C +1.6k / P +4.1k，平值价格ATM: C $11.50 / P $11.95 ｜ ATM IV 98.2%，净 delta 敞口 -61k shares
Top ΔOI: C 230 +774 ｜ C 222 -433
仓位参考: Max Pain 215 ｜ Call Wall 220（+8.9%，弱）（OI 4.8k） ｜ Put Wall 200（-1.0%，弱）（OI 5.5k）
量化解读： 存量两侧均衡｜ATM IV 98.2%｜历史 Rank 72%（近端代理）｜IV/RV 0.78×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 60,870 股

📆 11-27 Forward Structure
存量OI: C 9.8k / P 11.3k，今日变化ΔOI: C +0.7k / P +0.4k，平值价格ATM: C $14.21 / P $12.50 ｜ ATM IV 88.4%，净 delta 敞口 -17k shares
Top ΔOI: P 200 +531 ｜ C 230 +184 ｜ C 240 +184
仓位参考: Max Pain 215 ｜ Call Wall 200（-1.0%，弱）（OI 0.6k） ｜ Put Wall 200（-1.0%，弱）（OI 1.5k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 88.4%｜历史 Rank 72%（近端代理）｜IV/RV 0.70×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 17,000 股

12-04（MEDIUM △）Top ΔOI: 175P +87 ｜ 240C +84
12-04（MEDIUM △）仓位参考: Max Pain 205 ｜ Call Wall 200（-1.0%，弱）（OI 0.6k） ｜ Put Wall 200（-1.0%）（OI 1.8k）

📅 事件差分（观察，非因果）: 11-13（1D）ATM IV 113.0% vs 11-20 98.2%（差 +14.8pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-12/BE_evening.json