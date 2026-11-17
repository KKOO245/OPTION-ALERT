# 期权晚报 2026-11-16（快照 21:00 ET）

📊 市场环境

SPY $739.95 ｜ QQQ $661.75
VIX 22.91 ↑18.7%（5D +15.0%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 31.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-17 08:30　【高】零售销售 MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.8
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 待公布 ｜ 前值 1.221
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 待公布 ｜ 前值 1.4

🔍 重点速览
🔴 **事件差分**: 11-20（4D）ATM IV 147.3% vs 11-27 117.6%（差 +29.7pp），覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 106.74 → 收盘 107.13（+0.4%） ｜ 今日高 111.55 ｜ 低 104.75 ｜ 昨收 115.88 → 收盘 107.13（-7.6%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-23，窗口结束前不做对错判定）

Options: P/C成交量 0.51 | OI比 0.68 | ATM IV 147.3% | Skew 12.6pp | Term 0.75 | ExpMove ±12.3%（近端） | Rank 90%
量化视角： IV 历史高位（Rank 90%，期权偏贵）｜期限结构倒挂（Term 0.75，近月 IV 高于远月）｜保护溢价显著（Skew 12.6pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.68）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.51×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.68×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（4D）±12.3% ｜ 11-27（11D）±16.2% ｜ 12-04（18D）±19.9% ｜ 12-11（25D）±22.2%
   ⇒ IV–VIX Spread: +124.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -7,860,172 | GEX Change vs 上次快照 -1,922,233 | Flip: Primary Flip: 122.51（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 512 / LOW 69 / INVALID 225
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 122.51（全链重定价，覆盖 100%）
Put Wall 100（弱结构｜现价高于该位 7.1%）
最近结构参考: Put Wall 100（现价高于该位 7.1%）
量化视角： 负 Gamma（786万，无历史分位）｜负 Gamma 加深（192万）｜现价位于 Flip 下方 12.55%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 100（Put Wall，弱结构）；上方 145（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 123（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C +0 / P +0 ｜ Activity LOW ｜ 4D
11-27  C +0 / P +0 ｜ Activity LOW ｜ 11D
12-04  C +0 / P +0 ｜ Activity LOW ｜ 18D
12-11  C +0 / P +0 ｜ Activity LOW ｜ 25D

📆 11-20 Forward Structure
存量OI: C 168.4k / P 114.0k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $6.70 / P $6.50 ｜ ATM IV 147.3%，净 delta 敞口 0 shares
仓位参考: Max Pain 145 ｜ Call Wall 110（+2.7%，弱）（OI 2.3k） ｜ Put Wall 115（+7.3%，弱）（OI 9.9k）
量化解读： 存量 Call 重｜ATM IV 147.3%｜历史 Rank 90%（近端代理）｜IV/RV 1.02×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-27（Activity LOW）仓位参考: Max Pain 145 ｜ Call Wall 116（+8.3%，弱）（OI 1.2k） ｜ Put Wall 110（+2.7%，弱）（OI 0.9k）

12-04（Activity LOW）仓位参考: Max Pain 130 ｜ Put Wall 100（-6.7%，弱）（OI 0.9k）

12-11（Activity LOW）仓位参考: Max Pain 140 ｜ Call Wall 115（+7.3%，弱）（OI 0.1k） ｜ Put Wall 100（-6.7%，弱）（OI 1.2k）

📅 事件差分（观察，非因果）: 11-20（4D）ATM IV 147.3% vs 11-27 117.6%（差 +29.7pp）——覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-16/NBIS_evening.json