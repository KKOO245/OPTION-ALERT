# 期权晚报 2026-11-10（快照 16:40 ET）

📊 市场环境

SPY $749.92 ｜ QQQ $674.76
VIX 19.46 ↓2.3%（5D -6.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-10

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-10 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周二 11-10 08:30　【高】Inflation Rate MoM　预测 0.3 ｜ 实际 0.4 ｜ 前值 0.6　✅ 今日已公布
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 132.31 → 收盘 132.13（-0.1%） ｜ 今日高 136.25 ｜ 低 129.41 ｜ 昨收 136.10 → 收盘 132.13（-2.9%）
Target 等待验证: 3D_mdd >= 0.03（3D） — PENDING（评估日 ≈ 2026-11-13，窗口结束前不做对错判定）

Options: P/C成交量 0.63 | OI比 0.52 | ATM IV 83.4% | Skew 3.7pp | Term 0.83 | ExpMove ±6.1%（近端） | Rank 69%
量化视角： IV 中性（Rank 69%）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜保护溢价中性（Skew 3.7pp）｜存量 Call 偏重（OI比 0.52）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.63×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.52×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（3D）±6.1% ｜ 11-20（10D）±9.7% ｜ 11-27（17D）±12.2% ｜ 12-04（24D）±14.0%
   ⇒ IV–VIX Spread: +63.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 6,214,609 | GEX Change vs 上次快照 -6,316,241 | Flip: Primary Flip: 129.23（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 441 / LOW 213 / INVALID 334
结构观察区: Primary Flip 129.23（全链重定价，覆盖 100%）
Call Wall 140（弱结构｜现价低于该位 5.6%）
最近结构参考: Flip 129（现价高于该位 2.2%）
量化视角： 正 Gamma（621万，无历史分位）｜正 Gamma 减弱（632万）｜现价位于 Flip 上方 2.24%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 137（MaxPain，仅结算参考） / 140（Call Wall，弱结构）。
• Gamma 区域：切换参考 129（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +6.3k / P +1.3k ｜ Activity HIGH ｜ 3D
11-20  C +1.4k / P -1.2k ｜ Activity HIGH ｜ 10D
11-27  C +0.7k / P +0.6k ｜ Activity HIGH ｜ 17D
12-04  C +0.6k / P +0.8k ｜ Activity HIGH ｜ 24D

📆 11-13 Forward Structure
存量OI: C 69.8k / P 36.6k，今日变化ΔOI: C +6.3k / P +1.3k，平值价格ATM: C $4.15 / P $3.87 ｜ ATM IV 83.4%，净 delta 敞口 119k shares
Top ΔOI: C 145 +1,141
仓位参考: Max Pain 137 ｜ Call Wall 141（+6.7%，弱）（OI 8.6k） ｜ Put Wall 135（+2.2%，弱）（OI 2.3k）
量化解读： 存量 Call 重｜ATM IV 83.4%｜历史 Rank 69%（近端代理）｜IV/RV 1.27×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 119,035 股

📆 11-20 Forward Structure
存量OI: C 79.5k / P 61.2k，今日变化ΔOI: C +1.4k / P -1.2k，平值价格ATM: C $6.99 / P $5.79 ｜ ATM IV 73.9%，净 delta 敞口 189k shares
Top ΔOI: C 170 -5,074 ｜ C 165 +4,204 ｜ P 195 -774
仓位参考: Max Pain 162 ｜ Put Wall 120（-9.2%）（OI 7.0k）
量化解读： 存量 Call 重｜ATM IV 73.9%｜历史 Rank 69%（近端代理）｜IV/RV 1.12×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 188,516 股

📆 11-27 Forward Structure
存量OI: C 5.2k / P 8.1k，今日变化ΔOI: C +0.7k / P +0.6k，平值价格ATM: C $8.00 / P $8.10 ｜ ATM IV 69.0%，净 delta 敞口 18k shares
仓位参考: Max Pain 145 ｜ Call Wall 140（+6.0%，弱）（OI 0.2k） ｜ Put Wall 120（-9.2%，弱）（OI 0.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 69.0%｜历史 Rank 69%（近端代理）｜IV/RV 1.05×（近似）｜净 delta 敞口 正 17,583 股

📆 12-04 Forward Structure
存量OI: C 4.8k / P 7.5k，今日变化ΔOI: C +0.6k / P +0.8k，平值价格ATM: C $9.68 / P $8.80 ｜ ATM IV 69.5%，净 delta 敞口 -5k shares
Top ΔOI: P 125 +460 ｜ C 140 +99
仓位参考: Max Pain 140 ｜ Call Wall 140（+6.0%）（OI 1.4k） ｜ Put Wall 135（+2.2%）（OI 1.8k）
量化解读： 存量 Put 重｜ATM IV 69.5%｜历史 Rank 69%（近端代理）｜IV/RV 1.06×（近似）｜净 delta 敞口 负 4,712 股

📅 事件差分（观察，非因果）: 11-13（3D）ATM IV 83.4% vs 11-20 73.9%（差 +9.5pp）——覆盖 Core Inflation Rate MoM、Inflation Rate MoM 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime RANGE | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-10/COIN_evening.json