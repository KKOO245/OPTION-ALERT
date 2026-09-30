# 期权晚报 2026-09-29（快照 21:00 ET）

📊 市场环境

SPY $764.20 ｜ QQQ $nan
VIX 16.04 ↓0.2%（5D +12.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-29

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-29 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.23 ｜ 实际 7.079 ｜ 前值 7.335　✅ 今日已公布
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 待公布 ｜ 前值 2.1
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 230.99 → 收盘 227.21（-1.6%） ｜ 今日高 232.82 ｜ 低 227.02 ｜ 昨收 228.86 → 收盘 227.21（-0.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.50 | OI比 0.76 | ATM IV 32.6% | Skew 1.8pp | Term 0.97 | ExpMove ±1.4%（近端） | Rank 12%
量化视角： IV 历史低位（Rank 12%，期权偏便宜）｜期限结构正常（Term 0.97）｜保护溢价薄（Skew 1.8pp）｜存量 Call 偏重（OI比 0.76）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.50×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.76×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-30（1D）±1.4% ｜ 10-02（3D）±2.5% ｜ 10-05（6D）±2.9% ｜ 10-07（8D）±3.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 449,884,060 | GEX Change vs 上次快照 -77,920,413 | Flip: Primary Flip: 218.22（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 644 / LOW 205 / INVALID 537
结构观察区: Primary Flip 218.22（全链重定价，覆盖 99%）
最近结构参考: Flip 218（现价高于该位 4.1%）
量化视角： 正 Gamma（4.50亿，无历史分位）｜正 Gamma 减弱（7792万）｜现价位于 Flip 上方 4.12%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 225（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 218（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-30  C +0 / P +0 ｜ Activity LOW ｜ 1D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 3D
10-05  C +0 / P +0 ｜ Activity LOW ｜ 6D
10-07  C +0 / P +0 ｜ Activity LOW ｜ 8D

📆 09-30 Forward Structure
存量OI: C 106.2k / P 80.5k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $1.44 / P $1.63 ｜ ATM IV 32.6%，净 delta 敞口 0 shares
仓位参考: Max Pain 225 ｜ Call Wall 235（+3.4%，弱）（OI 18.1k） ｜ Put Wall 220（-3.2%，弱）（OI 7.5k）
量化解读： 存量 Call 重｜ATM IV 32.6%｜历史 Rank 12%（近端代理）｜IV/RV 1.36×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-02（Activity LOW）仓位参考: Max Pain 225 ｜ Call Wall 227.5（+0.1%，弱）（OI 76.5k） ｜ Put Wall 215（-5.4%，弱）（OI 25.1k）

10-05（Activity LOW）仓位参考: Max Pain 225 ｜ Call Wall 230（+1.2%，弱）（OI 5.8k） ｜ Put Wall 205（-9.8%，弱）（OI 2.2k）

10-07（Activity LOW）仓位参考: Max Pain 228 ｜ Call Wall 247.5（+8.9%）（OI 4.3k） ｜ Put Wall 215（-5.4%，弱）（OI 0.8k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-29/NVDA_evening.json