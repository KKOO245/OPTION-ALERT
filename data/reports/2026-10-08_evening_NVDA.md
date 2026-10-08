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
🟡 **近现价集中开仓**: 10-09 237C ΔOI +4,921（距现价 +3.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 234.93 → 收盘 230.48（-1.9%） ｜ 今日高 237.07 ｜ 低 229.85 ｜ 昨收 237.47 → 收盘 230.48（-2.9%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.66 | OI比 1.14 | ATM IV 35.8% | Skew 4.8pp | Term 0.87 | ExpMove ±1.5%（近端） | Rank 24%
量化视角： IV 历史低位（Rank 24%，期权偏便宜）｜期限结构倒挂（Term 0.87，近月 IV 高于远月）｜保护溢价中性（Skew 4.8pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.66×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.14×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-09（1D）±1.5% ｜ 10-12（4D）±2.2% ｜ 10-14（6D）±3.2% ｜ 10-16（8D）±3.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 126,369,565 | GEX Change vs 上次快照 -193,812,322 | Flip: Primary Flip: 226.43（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 676 / LOW 194 / INVALID 570
结构观察区: Primary Flip 226.43（全链重定价，覆盖 96%）
Put Wall 220（弱结构｜现价高于该位 4.8%） | Call Wall 240（弱结构｜现价低于该位 4.0%）
最近结构参考: Flip 226（现价高于该位 1.8%）
量化视角： 正 Gamma（1.26亿，无历史分位）｜正 Gamma 减弱（1.94亿）｜现价位于 Flip 上方 1.79%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 220（Put Wall，弱结构）；上方 232（MaxPain，仅结算参考） / 240（Call Wall，弱结构）。
• Gamma 区域：切换参考 226（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +28.9k / P +45.2k ｜ Activity HIGH ｜ 1D
10-12  C +3.6k / P +7.5k ｜ Activity HIGH ｜ 4D
10-14  C +5.1k / P +2.2k ｜ Activity HIGH ｜ 6D
10-16  C +4.8k / P +16.3k ｜ Activity MEDIUM △ ｜ 8D

📆 10-09 Forward Structure
存量OI: C 427.5k / P 487.4k，今日变化ΔOI: C +28.9k / P +45.2k，平值价格ATM: C $2.12 / P $1.44 ｜ ATM IV 35.8%，净 delta 敞口 -795k shares
Top ΔOI: C 242 +8,274 ｜ C 245 +5,424 ｜ C 237 +4,921
仓位参考: Max Pain 232 ｜ Call Wall 240（+4.1%，弱）（OI 76.7k） ｜ Put Wall 230（-0.2%，弱）（OI 34.4k）
量化解读： 存量两侧均衡｜ATM IV 35.8%｜历史 Rank 24%（近端代理）｜IV/RV 2.11×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 795,106 股

📆 10-12 Forward Structure
存量OI: C 38.9k / P 33.3k，今日变化ΔOI: C +3.6k / P +7.5k，平值价格ATM: C $2.86 / P $2.32 ｜ ATM IV 27.2%，净 delta 敞口 -22k shares
Top ΔOI: P 215 +1,222 ｜ C 245 +1,133
仓位参考: Max Pain 238 ｜ Call Wall 240（+4.1%）（OI 7.0k） ｜ Put Wall 237.5（+3.0%，弱）（OI 3.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 27.2%｜历史 Rank 24%（近端代理）｜IV/RV 1.60×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 22,139 股

📆 10-14 Forward Structure
存量OI: C 19.0k / P 10.6k，今日变化ΔOI: C +5.1k / P +2.2k，平值价格ATM: C $3.96 / P $3.33 ｜ ATM IV 30.4%，净 delta 敞口 -16k shares
Top ΔOI: C 250 +1,134 ｜ C 237 +969 ｜ C 240 +722
仓位参考: Max Pain 235 ｜ Call Wall 250（+8.5%，弱）（OI 2.8k） ｜ Put Wall 237.5（+3.0%，弱）（OI 1.4k）
量化解读： 存量 Call 重｜ATM IV 30.4%｜历史 Rank 24%（近端代理）｜IV/RV 1.79×（近似）｜净 delta 敞口 负 16,429 股

10-16（MEDIUM △）Top ΔOI: 212P +5,720 ｜ 240C +4,994
10-16（MEDIUM △）仓位参考: Max Pain 212 ｜ Call Wall 220（-4.5%，弱）（OI 99.7k） ｜ Put Wall 220（-4.5%）（OI 52.8k）

📅 事件差分（观察，非因果）: 10-09（1D）ATM IV 35.8% vs 10-12 27.2%（差 +8.7pp）——覆盖 密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-08/NVDA_evening.json