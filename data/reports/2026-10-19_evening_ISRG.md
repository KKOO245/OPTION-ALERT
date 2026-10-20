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

🔍 重点速览
🔴 **事件差分**: 10-23（4D）ATM IV 92.7% vs 10-30 64.0%（差 +28.7pp），覆盖 建筑许可 Prel、新屋开工
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 427.34 → 收盘 433.18（+1.4%） ｜ 今日高 434.62 ｜ 低 426.70 ｜ 昨收 426.70 → 收盘 433.18（+1.5%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-26，窗口结束前不做对错判定）

Options: P/C成交量 1.15 | OI比 0.71 | ATM IV 92.7% | Skew 11.0pp | Term 0.50 | ExpMove ±7.9%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.50，近月 IV 高于远月）｜保护溢价显著（Skew 11.0pp，Put 明显贵于 Call）｜⚠️ 重点观察：存量 Call 重（OI比 0.71）+ 当日成交偏 Put（P/C量 1.15）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.15×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.71×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（4D）±7.9% ｜ 10-30（11D）±8.8% ｜ 11-06（18D）±0.0% ｜ 11-13（25D）±4.9%
   ⇒ IV–VIX Spread: +74.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,599,468 | GEX Change vs 上次快照 187,273 | Flip: Primary Flip: 395.72（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 360 / LOW 83 / INVALID 463
结构观察区: Primary Flip 395.72（全链重定价，覆盖 100%）
Call Wall 420（弱结构｜现价高于该位 3.1%）
最近结构参考: Call Wall 420（现价高于该位 3.1%）
量化视角： 正 Gamma（160万，无历史分位）｜正 Gamma 增强（+19万）｜现价位于 Flip 上方 9.47%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 415（MaxPain，仅结算参考） / 420（Call Wall，弱结构）。
• Gamma 区域：切换参考 396（全链重定价，覆盖 100%）。
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
存量OI: C 3.0k / P 2.2k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $18.20 / P $16.20 ｜ ATM IV 92.7%，净 delta 敞口 0 shares
仓位参考: Max Pain 415 ｜ Call Wall 425（-1.9%，弱）（OI 0.5k） ｜ Put Wall 415（-4.2%）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 92.7%｜历史 Rank 100%（近端代理）｜IV/RV 3.79×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-30（Activity LOW）仓位参考: Max Pain 400 ｜ Call Wall 460（+6.2%，弱）（OI 0.1k） ｜ Put Wall 410（-5.4%，弱）（OI 61）

11-06（Activity LOW）仓位参考: Max Pain 420 ｜ Call Wall 455（+5.0%，弱）（OI 54） ｜ Put Wall 450（+3.9%，弱）（OI 64）

11-13（Activity LOW）仓位参考: Max Pain 410 ｜ Call Wall 475（+9.7%，弱）（OI 32）

📅 事件差分（观察，非因果）: 10-23（4D）ATM IV 92.7% vs 10-30 64.0%（差 +28.7pp）——覆盖 建筑许可 Prel、新屋开工
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-19/ISRG_evening.json