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
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **事件差分**: 10-09 ATM IV 52.0% vs 10-12 37.8%（差 +14.1pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-09 167P ΔOI +3,203（距现价 +4.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPCX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPCX: 今开 167.50 → 收盘 160.57（-4.1%） ｜ 今日高 167.60 ｜ 低 160.29 ｜ 昨收 167.60 → 收盘 160.57（-4.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.05 | OI比 1.09 | ATM IV 52.0% | Skew 1.7pp | Term 0.94 | ExpMove ±2.2%（近端） | Rank 40%
量化视角： IV 中性（Rank 40%）｜期限结构正常（Term 0.94）｜保护溢价薄（Skew 1.7pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.05×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.09×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-09（1D）±2.2% ｜ 10-12（4D）±3.2% ｜ 10-14（6D）±4.4% ｜ 10-16（8D）±5.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 1,682,574 | GEX Change vs 上次快照 -61,553,412 | Flip: Primary Flip: 160.43（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 698 / LOW 155 / INVALID 447
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 160.43（全链重定价，覆盖 98%）
最近结构参考: Flip 160（现价高于该位 0.1%）
量化视角： 正 Gamma（168万，无历史分位）｜正 Gamma 减弱（6155万）｜现价位于 Flip 上方 0.09%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 165（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 160（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +6.9k / P -5.4k ｜ Activity MEDIUM △ ｜ 1D
10-12  C +7.3k / P +3.8k ｜ Activity HIGH ｜ 4D
10-14  C +2.8k / P +1.1k ｜ Activity HIGH ｜ 6D
10-16  C +0.6k / P +4.6k ｜ Activity MEDIUM △ ｜ 8D

📆 10-09 Forward Structure
存量OI: C 198.3k / P 216.5k，今日变化ΔOI: C +6.9k / P -5.4k，平值价格ATM: C $2.14 / P $1.44 ｜ ATM IV 52.0%，净 delta 敞口 -45k shares
Top ΔOI: P 170 -4,221 ｜ P 167 +3,203 ｜ C 170 +2,399
仓位参考: Max Pain 165 ｜ Call Wall 175（+9.0%，弱）（OI 21.8k） ｜ Put Wall 160（-0.4%，弱）（OI 18.4k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 52.0%｜历史 Rank 40%（近端代理）｜IV/RV 1.09×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 45,468 股

📆 10-12 Forward Structure
存量OI: C 36.1k / P 19.1k，今日变化ΔOI: C +7.3k / P +3.8k，平值价格ATM: C $2.86 / P $2.21 ｜ ATM IV 37.8%，净 delta 敞口 -97k shares
Top ΔOI: C 170 +2,225 ｜ P 148 +1,322
仓位参考: Max Pain 170 ｜ Call Wall 170（+5.9%，弱）（OI 5.7k） ｜ Put Wall 165（+2.8%，弱）（OI 2.9k）
量化解读： 存量 Call 重｜ATM IV 37.8%｜历史 Rank 40%（近端代理）｜IV/RV 0.80×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 97,258 股

📆 10-14 Forward Structure
存量OI: C 7.2k / P 3.8k，今日变化ΔOI: C +2.8k / P +1.1k，平值价格ATM: C $3.83 / P $3.18 ｜ ATM IV 43.1%，净 delta 敞口 -8k shares
Top ΔOI: C 170 +546 ｜ C 175 +452 ｜ P 160 +366
仓位参考: Max Pain 170 ｜ Call Wall 175（+9.0%，弱）（OI 1.2k） ｜ Put Wall 165（+2.8%，弱）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 43.1%｜历史 Rank 40%（近端代理）｜IV/RV 0.91×（近似）｜净 delta 敞口 负 7,799 股

10-16（MEDIUM △）Top ΔOI: 160C -6,328 ｜ 165P +2,463
10-16（MEDIUM △）仓位参考: Max Pain 150 ｜ Call Wall 160（-0.4%，弱）（OI 26.6k） ｜ Put Wall 150（-6.6%，弱）（OI 24.1k）

📅 事件差分（观察，非因果）: 10-09（1D）ATM IV 52.0% vs 10-12 37.8%（差 +14.1pp）——覆盖 密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-08/SPCX_evening.json