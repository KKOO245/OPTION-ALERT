# 期权晚报 2026-11-03（快照 16:41 ET）

📊 市场环境

SPY $754.35 ｜ QQQ $685.28
VIX 20.83 ↓1.5%（5D +18.9%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 19.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-03

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-03 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.1 ｜ 实际 7.523 ｜ 前值 7.19　✅ 今日已公布
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 待公布 ｜ 前值 54.9
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🔴 **事件差分**: 11-06（3D）ATM IV 111.3% vs 11-13 78.2%（差 +33.0pp），覆盖 职位空缺(JOLTS) Job Openings、ISM 非制造业 PMI 等
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 39.23 → 收盘 37.83（-3.6%） ｜ 今日高 39.29 ｜ 低 37.35 ｜ 昨收 38.35 → 收盘 37.83（-1.4%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-10，窗口结束前不做对错判定）

Options: P/C成交量 0.90 | OI比 0.41 | ATM IV 111.3% | Skew 0.4pp | Term 0.61 | ExpMove ±8.0%（近端） | Rank 96%
量化视角： IV 历史高位（Rank 96%，期权偏贵）｜期限结构倒挂（Term 0.61，近月 IV 高于远月）｜保护溢价薄（Skew 0.4pp）｜存量 Call 偏重（OI比 0.41）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.90×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.41×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（3D）±8.0% ｜ 11-13（10D）±10.8% ｜ 11-20（17D）±13.1% ｜ 11-27（24D）±13.5%
   ⇒ IV–VIX Spread: +90.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,173,177 | GEX Change vs 上次快照 -382,406 | Flip: Primary Flip: 36.06（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 312 / LOW 43 / INVALID 113
结构观察区: Primary Flip 36.06（全链重定价，覆盖 100%）
Put Wall 35（弱结构｜现价高于该位 8.1%）
最近结构参考: Flip 36（现价高于该位 4.9%）
量化视角： 正 Gamma（117万，无历史分位）｜正 Gamma 减弱（38万）｜现价位于 Flip 上方 4.91%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 35（Put Wall，弱结构）；上方 41（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 36（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-06  C +2.0k / P -0.1k ｜ Activity HIGH ｜ 3D
11-13  C +1.0k / P +0.4k ｜ Activity HIGH ｜ 10D
11-20  C +20 / P +0.4k ｜ Activity MEDIUM △ ｜ 17D
11-27  C -0.2k / P +48 ｜ Activity MEDIUM △ ｜ 24D

📆 11-06 Forward Structure
存量OI: C 13.0k / P 5.4k，今日变化ΔOI: C +2.0k / P -0.1k，平值价格ATM: C $1.37 / P $1.65 ｜ ATM IV 111.3%，净 delta 敞口 58k shares
Top ΔOI: C 41 +465
仓位参考: Max Pain 41 ｜ Call Wall 41.5（+9.7%，弱）（OI 0.6k） ｜ Put Wall 38（+0.4%）（OI 1.4k）
量化解读： 存量 Call 重｜ATM IV 111.3%｜历史 Rank 96%（近端代理）｜IV/RV 2.03×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 57,800 股

📆 11-13 Forward Structure
存量OI: C 5.8k / P 2.8k，今日变化ΔOI: C +1.0k / P +0.4k，平值价格ATM: C $1.81 / P $2.27 ｜ ATM IV 78.2%，净 delta 敞口 -20k shares
Top ΔOI: C 41 +300 ｜ P 42 +224
仓位参考: Max Pain 40 ｜ Call Wall 40（+5.7%，弱）（OI 0.8k） ｜ Put Wall 39（+3.1%，弱）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 78.2%｜历史 Rank 96%（近端代理）｜IV/RV 1.43×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 19,633 股

11-20（MEDIUM △）仓位参考: Max Pain 45 ｜ Call Wall 40（+5.7%，弱）（OI 0.9k） ｜ Put Wall 35（-7.5%，弱）（OI 1.7k）

11-27（MEDIUM △）仓位参考: Max Pain 44 ｜ Put Wall 38（+0.4%，弱）（OI 71）

📅 事件差分（观察，非因果）: 11-06（3D）ATM IV 111.3% vs 11-13 78.2%（差 +33.0pp）——覆盖 职位空缺(JOLTS) Job Openings、ISM 非制造业 PMI 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-03/MP_evening.json