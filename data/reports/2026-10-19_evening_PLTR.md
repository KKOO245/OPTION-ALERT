# 期权晚报 2026-10-19（快照 21:00 ET）

📊 市场环境

SPY $766.48 ｜ QQQ $718.36
VIX 18.44 ↓7.8%（5D +21.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 23.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.4 ｜ 实际 待公布 ｜ 前值 1.403
- 周二 10-20 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.275

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 187.00 → 收盘 194.15（+3.8%） ｜ 今日高 196.99 ｜ 低 186.15 ｜ 昨收 186.03 → 收盘 194.15（+4.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.48 | OI比 0.94 | ATM IV 52.3% | Skew 5.1pp | Term 1.19 | ExpMove ±4.4%（近端） | Rank 69%
量化视角： IV 中性（Rank 69%）｜期限结构正常偏陡（Term 1.19）｜保护溢价中性（Skew 5.1pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.48×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.94×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（4D）±4.4% ｜ 10-30（11D）±6.8% ｜ 11-06（18D）±12.8% ｜ 11-13（25D）±13.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 39,282,602 | GEX Change vs 上次快照 8,877,111 | Flip: Primary Flip: 181.69（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 658 / LOW 53 / INVALID 201
结构观察区: Primary Flip 181.69（全链重定价，覆盖 100%）
Call Wall 200（弱结构｜现价低于该位 2.9%）
最近结构参考: Call Wall 200（现价低于该位 2.9%）
量化视角： 正 Gamma（3928万，无历史分位）｜正 Gamma 增强（+888万）｜现价位于 Flip 上方 6.86%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 190（MaxPain，仅结算参考）；上方 200（Call Wall，弱结构）。
• Gamma 区域：切换参考 182（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +0 / P +0 ｜ Activity LOW ｜ 4D
10-30  C +0 / P +0 ｜ Activity LOW ｜ 11D
11-06  C +0 / P +0 ｜ Activity LOW ｜ 18D
11-13  C +0 / P +0 ｜ Activity LOW ｜ 25D

📆 10-23 Forward Structure
存量OI: C 107.3k / P 101.0k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $3.93 / P $4.68 ｜ ATM IV 52.3%，净 delta 敞口 0 shares
仓位参考: Max Pain 190 ｜ Call Wall 195（+0.4%，弱）（OI 13.6k） ｜ Put Wall 185（-4.7%，弱）（OI 4.1k）
量化解读： 存量两侧均衡｜ATM IV 52.3%｜历史 Rank 69%（近端代理）｜IV/RV 1.26×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

10-30（Activity LOW）仓位参考: Max Pain 190 ｜ Call Wall 205（+5.6%，弱）（OI 3.6k） ｜ Put Wall 190（-2.1%）（OI 6.1k）

11-06（Activity LOW）仓位参考: Max Pain 190 ｜ Call Wall 205（+5.6%，弱）（OI 1.6k） ｜ Put Wall 190（-2.1%）（OI 3.1k）

11-13（Activity LOW）仓位参考: Max Pain 192 ｜ Call Wall 210（+8.2%，弱）（OI 1.0k） ｜ Put Wall 180（-7.3%，弱）（OI 1.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-19/PLTR_evening.json