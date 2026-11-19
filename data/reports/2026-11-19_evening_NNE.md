# 期权晚报 2026-11-19（快照 16:40 ET）

📊 市场环境

SPY $715.87 ｜ QQQ $645.04
VIX 28.44 ↑15.8%（5D +52.1%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 18.7（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🔴 **Vol Regime 升档**: ELEVATED → STRESS（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 10.66 → 收盘 9.97（-6.5%） ｜ 今日高 10.86 ｜ 低 9.93 ｜ 昨收 10.35 → 收盘 9.97（-3.7%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-26，窗口结束前不做对错判定）

Options: P/C成交量 0.43 | OI比 0.28 | ATM IV 160.7% | Skew 32.1pp | Term 0.55 | ExpMove ±5.5%（近端） | Rank 93%
量化视角： IV 历史高位（Rank 93%，期权偏贵）｜期限结构倒挂（Term 0.55，近月 IV 高于远月）｜保护溢价显著（Skew 32.1pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.28）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.43×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.28×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（1D）±5.5% ｜ 11-27（8D）±11.3% ｜ 12-04（15D）±19.6% ｜ 12-11（22D）±16.6%
   ⇒ IV–VIX Spread: +132.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 508,212 | GEX Change vs 上次快照 -539,616 | Flip: Primary Flip: 8.60（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 104 / LOW 72 / INVALID 190
结构观察区: Primary Flip 8.60（全链重定价，覆盖 92%）
Put Wall 10（弱结构｜现价低于该位 0.3%）
最近结构参考: Put Wall 10（现价低于该位 0.3%）
量化视角： 正 Gamma（51万，无历史分位）｜正 Gamma 减弱（54万）｜现价位于 Flip 上方 15.97%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 10（Put Wall，弱结构） / 12（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 9（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C +0.2k / P -88 ｜ Activity LOW ｜ 1D
11-27  C +23 / P +26 ｜ Activity MEDIUM △ ｜ 8D
12-04  C +12 / P +87 ｜ Activity MEDIUM △ ｜ 15D
12-11  C +4 / P +2 ｜ Activity LOW ｜ 22D

📆 11-20 Forward Structure
存量OI: C 7.2k / P 2.0k，今日变化ΔOI: C +0.2k / P -88，平值价格ATM: C $0.40 / P $0.15 ｜ ATM IV 160.7%，净 delta 敞口 18k shares
Top ΔOI: C 10 +38
仓位参考: Max Pain 12 ｜ Call Wall 10（+0.3%，弱）（OI 0.2k） ｜ Put Wall 10（+0.3%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 160.7%｜历史 Rank 93%（近端代理）｜IV/RV 1.67×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 17,598 股

11-27（MEDIUM △）Top ΔOI: 9P +26
11-27（MEDIUM △）仓位参考: Max Pain 12 ｜ Put Wall 10（+0.3%，弱）（OI 0.1k）

12-04（MEDIUM △）Top ΔOI: 10P +78
12-04（MEDIUM △）仓位参考: Max Pain 12 ｜ Put Wall 9.5（-4.7%）（OI 0.2k）

12-11（Activity LOW）仓位参考: Max Pain 11 ｜ Call Wall 10（+0.3%，弱）（OI 34） ｜ Put Wall 9（-9.7%，弱）（OI 8）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-19/NNE_evening.json