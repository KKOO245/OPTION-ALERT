# 期权晚报 2026-11-13（快照 16:40 ET）

📊 市场环境

SPY $754.37 ｜ QQQ $679.89
VIX 19.30 ↑3.2%（5D -24.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-13

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 0.3 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-20 195P ΔOI +560（距现价 +1.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 200.45 → 收盘 191.99（-4.2%） ｜ 今日高 205.92 ｜ 低 183.89 ｜ 昨收 201.93 → 收盘 191.99（-4.9%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-18，窗口结束前不做对错判定）

Options: P/C成交量 0.64 | OI比 1.08 | ATM IV 113.3% | Skew 15.1pp | Term 0.81 | ExpMove ±11.2%（近端） | Rank 72%
量化视角： IV 中性（Rank 72%）｜期限结构倒挂（Term 0.81，近月 IV 高于远月）｜保护溢价显著（Skew 15.1pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.64×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.08×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-20（7D）±11.2% ｜ 11-27（14D）±14.4% ｜ 12-04（21D）±17.1% ｜ 12-11（28D）±19.6%
   ⇒ IV–VIX Spread: +94.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -9,012,431 | GEX Change vs 上次快照 4,643,459 | Flip: Primary Flip: 213.43（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 88%（带内） ｜ IV 有效性: VALID 492 / LOW 116 / INVALID 336
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 213.43（全链重定价，覆盖 88%）
Put Wall 200（弱结构｜现价低于该位 4.0%）
最近结构参考: Put Wall 200（现价低于该位 4.0%）
量化视角： 负 Gamma（901万，无历史分位）｜负 Gamma 缓解（+464万）｜现价位于 Flip 下方 10.05%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 200（Put Wall，弱结构） / 195（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 213（全链重定价，覆盖 88%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C +2.0k / P +3.8k ｜ Activity MEDIUM △ ｜ 7D
11-27  C +1.0k / P +93 ｜ Activity HIGH ｜ 14D
12-04  C +0.3k / P +0.3k ｜ Activity MEDIUM △ ｜ 21D
12-11  C +0.4k / P +0.3k ｜ Activity HIGH ｜ 28D

📆 11-20 Forward Structure
存量OI: C 83.8k / P 89.0k，今日变化ΔOI: C +2.0k / P +3.8k，平值价格ATM: C $10.25 / P $11.20 ｜ ATM IV 99.9%，净 delta 敞口 -18k shares
Top ΔOI: C 215 +739 ｜ P 195 +560
仓位参考: Max Pain 215 ｜ Call Wall 200（+4.2%，弱）（OI 3.1k） ｜ Put Wall 200（+4.2%，弱）（OI 5.2k）
量化解读： 存量两侧均衡｜ATM IV 99.9%｜历史 Rank 72%（近端代理）｜IV/RV 0.79×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 18,201 股

📆 11-27 Forward Structure
存量OI: C 10.8k / P 11.4k，今日变化ΔOI: C +1.0k / P +93，平值价格ATM: C $13.35 / P $14.35 ｜ ATM IV 90.4%，净 delta 敞口 26k shares
Top ΔOI: C 210 +168 ｜ C 215 +157
仓位参考: Max Pain 215 ｜ Call Wall 200（+4.2%，弱）（OI 0.7k） ｜ Put Wall 200（+4.2%，弱）（OI 1.4k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 90.4%｜历史 Rank 72%（近端代理）｜IV/RV 0.71×（近似）｜净 delta 敞口 正 26,127 股

12-04（MEDIUM △）Top ΔOI: 140P +278 ｜ 210C +109
12-04（MEDIUM △）仓位参考: Max Pain 200 ｜ Call Wall 200（+4.2%，弱）（OI 0.6k） ｜ Put Wall 200（+4.2%）（OI 1.8k）

📆 12-11 Forward Structure
存量OI: C 2.9k / P 4.6k，今日变化ΔOI: C +0.4k / P +0.3k，平值价格ATM: C $20.31 / P $17.30 ｜ ATM IV 92.0%，净 delta 敞口 -1k shares
Top ΔOI: C 230 +205 ｜ P 190 +67
仓位参考: Max Pain 210 ｜ Call Wall 195（+1.6%，弱）（OI 0.2k） ｜ Put Wall 175（-8.8%）（OI 2.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 92.0%｜历史 Rank 72%（近端代理）｜IV/RV 0.73×（近似）｜净 delta 敞口 负 1,298 股

📅 事件差分（观察，非因果）: 11-20（7D）ATM IV 99.9% vs 11-27 90.4%（差 +9.5pp）——覆盖 PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=94 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=94）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-13/BE_evening.json