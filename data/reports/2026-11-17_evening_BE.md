# 期权晚报 2026-11-17（快照 21:00 ET）

📊 市场环境

SPY $732.44 ｜ QQQ $nan
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
🔴 **事件差分**: 11-20（3D）ATM IV 145.2% vs 11-27 110.9%（差 +34.3pp），覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Vol Regime 升档**: ELEVATED → STRESS（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 181.00 → 收盘 173.46（-4.2%） ｜ 今日高 181.16 ｜ 低 162.93 ｜ 昨收 177.28 → 收盘 173.46（-2.2%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-24，窗口结束前不做对错判定）

Options: P/C成交量 0.63 | OI比 0.92 | ATM IV 145.2% | Skew 15.3pp | Term 0.70 | ExpMove ±10.6%（近端） | Rank 90%
量化视角： IV 历史高位（Rank 90%，期权偏贵）｜期限结构倒挂（Term 0.70，近月 IV 高于远月）｜保护溢价显著（Skew 15.3pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.63×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.92×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-20（3D）±10.6% ｜ 11-27（10D）±13.9% ｜ 12-04（17D）±18.4% ｜ 12-11（24D）±21.0%
   ⇒ IV–VIX Spread: +119.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -11,536,500 | GEX Change vs 上次快照 -1,894,648 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 549 / LOW 106 / INVALID 143
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: NO_CROSS
量化视角： 负 Gamma（1154万，无历史分位）｜负 Gamma 加深（189万）｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 200（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C +0 / P +0 ｜ Activity LOW ｜ 3D
11-27  C +0 / P +0 ｜ Activity LOW ｜ 10D
12-04  C +0 / P +0 ｜ Activity LOW ｜ 17D
12-11  C +0 / P +0 ｜ Activity LOW ｜ 24D

📆 11-20 Forward Structure
存量OI: C 99.8k / P 91.7k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $9.75 / P $8.57 ｜ ATM IV 145.2%，净 delta 敞口 0 shares
仓位参考: Max Pain 200 ｜ Call Wall 190（+9.5%，弱）（OI 3.6k） ｜ Put Wall 170（-2.0%，弱）（OI 4.9k）
量化解读： 存量两侧均衡｜ATM IV 145.2%｜历史 Rank 90%（近端代理）｜IV/RV 1.25×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-27（Activity LOW）仓位参考: Max Pain 200 ｜ Call Wall 185（+6.7%，弱）（OI 0.7k） ｜ Put Wall 190（+9.5%，弱）（OI 1.3k）

12-04（Activity LOW）仓位参考: Max Pain 200 ｜ Call Wall 190（+9.5%，弱）（OI 0.3k） ｜ Put Wall 185（+6.7%，弱）（OI 0.4k）

12-11（Activity LOW）仓位参考: Max Pain 210 ｜ Put Wall 175（+0.9%）（OI 2.1k）

📅 事件差分（观察，非因果）: 11-20（3D）ATM IV 145.2% vs 11-27 110.9%（差 +34.3pp）——覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location ? | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-17/BE_evening.json