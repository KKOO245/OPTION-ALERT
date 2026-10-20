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


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 51.91 → 收盘 51.54（-0.7%） ｜ 今日高 51.94 ｜ 低 51.51 ｜ 昨收 51.51 → 收盘 51.54（+0.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.55 | OI比 0.57 | ATM IV 31.8% | Skew 3.7pp | Term 1.06 | ExpMove ±1.9%（近端） | Rank 46%
量化视角： IV 中性（Rank 46%）｜期限结构正常（Term 1.06）｜保护溢价中性（Skew 3.7pp）｜存量 Call 偏重（OI比 0.57）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.55×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.57×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-21（2D）±1.9% ｜ 10-23（4D）±2.7% ｜ 10-26（7D）±3.2% ｜ 10-28（9D）±4.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 23,297,741 | GEX Change vs 上次快照 -13,230,561 | Flip: Primary Flip: 50.79（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 673 / LOW 112 / INVALID 353
结构观察区: Primary Flip 50.79（全链重定价，覆盖 99%）
Put Wall 50（弱结构｜现价高于该位 3.1%）
最近结构参考: Flip 51（现价高于该位 1.5%）
量化视角： 正 Gamma（2330万，无历史分位）｜正 Gamma 减弱（1323万）｜现价位于 Flip 上方 1.48%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 50（Put Wall，弱结构） / 52（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 51（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-21  C +0 / P +0 ｜ Activity LOW ｜ 2D
10-23  C +0 / P +0 ｜ Activity LOW ｜ 4D
10-26  C +0 / P +0 ｜ Activity LOW ｜ 7D
10-28  C +0 / P +0 ｜ Activity LOW ｜ 9D

📆 10-21 Forward Structure
存量OI: C 24.2k / P 13.8k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $0.51 / P $0.48 ｜ ATM IV 31.8%，净 delta 敞口 0 shares
仓位参考: Max Pain 52 ｜ Call Wall 54（+4.8%）（OI 4.9k） ｜ Put Wall 48（-6.9%，弱）（OI 2.8k）
量化解读： 存量 Call 重｜ATM IV 31.8%｜历史 Rank 46%（近端代理）｜IV/RV 0.86×（近似）｜净 delta 敞口 正 0 股

10-23（Activity LOW）仓位参考: Max Pain 54 ｜ Call Wall 55（+6.7%，弱）（OI 5.3k） ｜ Put Wall 50（-3.0%，弱）（OI 4.6k）

10-26（Activity LOW）仓位参考: Max Pain 50 ｜ Call Wall 50.5（-2.0%）（OI 1.4k） ｜ Put Wall 50（-3.0%，弱）（OI 0.6k）

10-28（Activity LOW）仓位参考: Max Pain 52 ｜ Call Wall 55（+6.7%，弱）（OI 0.3k） ｜ Put Wall 48（-6.9%，弱）（OI 0.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-19/SLV_evening.json