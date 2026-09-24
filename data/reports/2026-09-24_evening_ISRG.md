# 期权晚报 2026-09-24（快照 16:40 ET）

📊 市场环境

SPY $767.18 ｜ QQQ $741.10
VIX 15.67 ↑3.2%（5D -11.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 36.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-24

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🔴 **事件差分**: 09-25（1D）ATM IV 57.9% vs 10-02 37.5%（差 +20.5pp），覆盖 耐用品订单 Orders MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 09-25 415C ΔOI +58（距现价 +3.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-09 460C ΔOI +156 占该期限总 OI 12.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 396.17 → 收盘 399.52（+0.8%） ｜ 今日高 404.19 ｜ 低 395.18 ｜ 昨收 398.30 → 收盘 399.52（+0.3%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-01，窗口结束前不做对错判定）

Options: P/C成交量 0.68 | OI比 0.61 | ATM IV 57.9% | Skew 1.9pp | Term 0.71 | ExpMove ±1.8%（近端） | Rank 94%
量化视角： IV 历史高位（Rank 94%，期权偏贵）｜期限结构倒挂（Term 0.71，近月 IV 高于远月）｜保护溢价薄（Skew 1.9pp）｜存量 Call 偏重（OI比 0.61）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.68×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.61×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（1D）±1.8% ｜ 10-02（8D）±4.0% ｜ 10-09（15D）±5.4% ｜ 10-16（22D）±6.2%
   ⇒ IV–VIX Spread: +42.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,421,846 | GEX Change vs 上次快照 -130,732 | Flip: Primary Flip: 383.89（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 276 / LOW 190 / INVALID 430
结构观察区: Primary Flip 383.89（全链重定价，覆盖 90%）
Call Wall 400（弱结构｜现价低于该位 0.1%）
最近结构参考: Call Wall 400（现价低于该位 0.1%）
量化视角： 正 Gamma（242万，无历史分位）｜正 Gamma 减弱（13万）｜现价位于 Flip 上方 4.07%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 385（MaxPain，仅结算参考）；上方 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 384（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +99 / P +0.1k ｜ Activity HIGH ｜ 1D
10-02  C +46 / P +0.1k ｜ Activity MEDIUM △ ｜ 8D
10-09  C +0.5k / P -0.1k ｜ Activity MEDIUM △ ｜ 15D
10-16  C +0.2k / P -97 ｜ Activity MEDIUM △ ｜ 22D

📆 09-25 Forward Structure
存量OI: C 2.5k / P 1.5k，今日变化ΔOI: C +99 / P +0.1k，平值价格ATM: C $4.20 / P $2.85 ｜ ATM IV 57.9%，净 delta 敞口 -4k shares
Top ΔOI: C 415 +58 ｜ P 392 +57 ｜ P 380 -47
仓位参考: Max Pain 385 ｜ Call Wall 430（+7.6%，弱）（OI 0.3k） ｜ Put Wall 380（-4.9%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 57.9%｜历史 Rank 94%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 4,093 股

10-02（MEDIUM △）Top ΔOI: 367P +64 ｜ 410C +31
10-02（MEDIUM △）仓位参考: Max Pain 375 ｜ Call Wall 410（+2.6%）（OI 0.3k）

10-09（MEDIUM △）Top ΔOI: 385P -147 ｜ 425C +102
10-09（MEDIUM △）仓位参考: Max Pain 370 ｜ Call Wall 420（+5.1%，弱）（OI 0.1k） ｜ Put Wall 370（-7.4%，弱）（OI 15）

10-16（MEDIUM △）Top ΔOI: 420C +168 ｜ 385P -155
10-16（MEDIUM △）仓位参考: Max Pain 380 ｜ Call Wall 400（+0.1%，弱）（OI 1.0k） ｜ Put Wall 380（-4.9%，弱）（OI 0.6k）

📅 事件差分（观察，非因果）: 09-25（1D）ATM IV 57.9% vs 10-02 37.5%（差 +20.5pp）——覆盖 耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-24/ISRG_evening.json