# 期权晚报 2026-11-17（快照 16:40 ET）

📊 市场环境

SPY $732.44 ｜ QQQ $656.95
VIX 25.46 ↑11.1%（5D +30.8%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 25.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-17

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-17 08:30　【高】零售销售 MoM　预测 0.2 ｜ 实际 0.2 ｜ 前值 0.8　✅ 今日已公布
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 待公布 ｜ 前值 1.221
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 待公布 ｜ 前值 1.4

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🔴 **Vol Regime 升档**: ELEVATED → STRESS（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-18 43C ΔOI +2,585（距现价 +0.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 42.88 → 收盘 42.64（-0.6%） ｜ 今日高 43.30 ｜ 低 42.47 ｜ 昨收 42.39 → 收盘 42.64（+0.6%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-24，窗口结束前不做对错判定）

Options: P/C成交量 0.51 | OI比 0.46 | ATM IV 55.3% | Skew 6.0pp | Term 0.78 | ExpMove ±2.4%（近端） | Rank 88%
量化视角： IV 历史高位（Rank 88%，期权偏贵）｜期限结构倒挂（Term 0.78，近月 IV 高于远月）｜保护溢价显著（Skew 6.0pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.46）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.51×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.46×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-18（1D）±2.4% ｜ 11-20（3D）±3.8% ｜ 11-23（6D）±4.5% ｜ 11-25（8D）±5.5%
   ⇒ IV–VIX Spread: +29.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 3,453,838 | GEX Change vs 上次快照 -9,380,006 | Flip: Primary Flip: 42.53（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 650 / LOW 147 / INVALID 405
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 42.53（全链重定价，覆盖 94%）
Put Wall 40（弱结构｜现价高于该位 6.6%）
最近结构参考: Flip 43（现价高于该位 0.3%）
量化视角： 正 Gamma（345万，无历史分位）｜正 Gamma 减弱（938万）｜现价位于 Flip 上方 0.26%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 40（Put Wall，弱结构）；上方 44（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 43（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-18  C +11.4k / P +3.4k ｜ Activity HIGH ｜ 1D
11-20  C +21.6k / P +0.7k ｜ Activity MEDIUM △ ｜ 3D
11-23  C +5.8k / P +2.3k ｜ Activity HIGH ｜ 6D
11-25  C +1.2k / P +0.4k ｜ Activity HIGH ｜ 8D

📆 11-18 Forward Structure
存量OI: C 33.5k / P 15.4k，今日变化ΔOI: C +11.4k / P +3.4k，平值价格ATM: C $0.58 / P $0.42 ｜ ATM IV 55.3%，净 delta 敞口 260k shares
Top ΔOI: C 43 +2,585 ｜ C 44 +2,134 ｜ C 43 +1,465
仓位参考: Max Pain 44 ｜ Call Wall 43（+0.8%，弱）（OI 2.6k） ｜ Put Wall 40（-6.2%，弱）（OI 2.2k）
量化解读： 存量 Call 重｜ATM IV 55.3%｜历史 Rank 88%（近端代理）｜IV/RV 1.36×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 260,499 股

11-20（MEDIUM △）Top ΔOI: 44C +13,451 ｜ 45C +3,779
11-20（MEDIUM △）仓位参考: Max Pain 48 ｜ Put Wall 45（+5.5%，弱）（OI 14.4k）

📆 11-23 Forward Structure
存量OI: C 13.1k / P 3.6k，今日变化ΔOI: C +5.8k / P +2.3k，平值价格ATM: C $1.02 / P $0.89 ｜ ATM IV 44.1%，净 delta 敞口 49k shares
Top ΔOI: C 45 +3,917 ｜ P 39 +656 ｜ C 46 +352
仓位参考: Max Pain 43 ｜ Call Wall 45.5（+6.7%，弱）（OI 4.0k） ｜ Put Wall 39（-8.5%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 44.1%｜历史 Rank 88%（近端代理）｜IV/RV 1.09×（近似）｜净 delta 敞口 正 49,388 股

📆 11-25 Forward Structure
存量OI: C 2.5k / P 1.4k，今日变化ΔOI: C +1.2k / P +0.4k，平值价格ATM: C $1.25 / P $1.08 ｜ ATM IV 45.4%，净 delta 敞口 19k shares
Top ΔOI: C 46 +417 ｜ P 42 +204 ｜ C 43 +145
仓位参考: Max Pain 44 ｜ Call Wall 46（+7.9%）（OI 0.5k） ｜ Put Wall 42（-1.5%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 45.4%｜历史 Rank 88%（近端代理）｜IV/RV 1.12×（近似）｜净 delta 敞口 正 19,414 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location above_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-17/SLV_evening.json