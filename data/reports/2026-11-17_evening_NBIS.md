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
🔴 **事件差分**: 11-20（3D）ATM IV 182.0% vs 11-27 132.4%（差 +49.7pp），覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Vol Regime 升档**: ELEVATED → STRESS（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-27 110C ΔOI +754（距现价 +3.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 108.93 → 收盘 106.04（-2.7%） ｜ 今日高 111.90 ｜ 低 102.25 ｜ 昨收 107.13 → 收盘 106.04（-1.0%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-20，窗口结束前不做对错判定）

Options: P/C成交量 0.64 | OI比 0.59 | ATM IV 182.0% | Skew 21.7pp | Term 0.64 | ExpMove ±13.2%（近端） | Rank 97%
量化视角： IV 历史高位（Rank 97%，期权偏贵）｜期限结构倒挂（Term 0.64，近月 IV 高于远月）｜保护溢价显著（Skew 21.7pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.59）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.64×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.59×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（3D）±13.2% ｜ 11-27（10D）±17.1% ｜ 12-04（17D）±21.4% ｜ 12-11（24D）±24.6%
   ⇒ IV–VIX Spread: +156.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -4,063,335 | GEX Change vs 上次快照 -259,609 | Flip: Primary Flip: 113.66（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 582 / LOW 81 / INVALID 143
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 113.66（全链重定价，覆盖 100%）
Put Wall 100（弱结构｜现价高于该位 6.0%）
最近结构参考: Put Wall 100（现价高于该位 6.0%）
量化视角： 负 Gamma（406万，无历史分位）｜负 Gamma 加深（26万）｜现价位于 Flip 下方 6.71%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 100（Put Wall，弱结构）；上方 130（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 114（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C +19.3k / P -3.9k ｜ Activity HIGH ｜ 3D
11-27  C +6.4k / P -0.3k ｜ Activity HIGH ｜ 10D
12-04  C +0.9k / P +0.1k ｜ Activity HIGH ｜ 17D
12-11  C +0.8k / P +0.5k ｜ Activity HIGH ｜ 24D

📆 11-20 Forward Structure
存量OI: C 187.7k / P 110.1k，今日变化ΔOI: C +19.3k / P -3.9k，平值价格ATM: C $7.05 / P $6.93 ｜ ATM IV 182.0%，净 delta 敞口 1.4M shares
Top ΔOI: C 115 +3,893 ｜ C 125 +3,435 ｜ P 107 +3,137
仓位参考: Max Pain 130 ｜ Call Wall 115（+8.5%，弱）（OI 5.2k） ｜ Put Wall 115（+8.5%，弱）（OI 9.9k）
量化解读： 存量 Call 重｜ATM IV 182.0%｜历史 Rank 97%（近端代理）｜IV/RV 1.27×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,382,115 股

📆 11-27 Forward Structure
存量OI: C 35.3k / P 18.7k，今日变化ΔOI: C +6.4k / P -0.3k，平值价格ATM: C $9.50 / P $8.65 ｜ ATM IV 132.4%，净 delta 敞口 208k shares
Top ΔOI: C 150 +1,967 ｜ C 107 +768 ｜ C 110 +754
仓位参考: Max Pain 132 ｜ Call Wall 110（+3.7%，弱）（OI 1.3k） ｜ Put Wall 100（-5.7%，弱）（OI 1.4k）
量化解读： 存量 Call 重｜ATM IV 132.4%｜历史 Rank 97%（近端代理）｜IV/RV 0.92×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 207,915 股

📆 12-04 Forward Structure
存量OI: C 10.9k / P 7.9k，今日变化ΔOI: C +0.9k / P +0.1k，平值价格ATM: C $12.00 / P $10.73 ｜ ATM IV 122.8%，净 delta 敞口 41k shares
Top ΔOI: C 120 +106
仓位参考: Max Pain 130 ｜ Put Wall 100（-5.7%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 122.8%｜历史 Rank 97%（近端代理）｜IV/RV 0.85×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 41,341 股

📆 12-11 Forward Structure
存量OI: C 5.6k / P 8.1k，今日变化ΔOI: C +0.8k / P +0.5k，平值价格ATM: C $14.20 / P $11.85 ｜ ATM IV 119.8%，净 delta 敞口 10k shares
Top ΔOI: C 120 +212 ｜ P 90 +196
仓位参考: Max Pain 135 ｜ Call Wall 115（+8.5%，弱）（OI 0.1k） ｜ Put Wall 100（-5.7%，弱）（OI 1.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 119.8%｜历史 Rank 97%（近端代理）｜IV/RV 0.83×（近似）｜净 delta 敞口 正 9,567 股

📅 事件差分（观察，非因果）: 11-20（3D）ATM IV 182.0% vs 11-27 132.4%（差 +49.7pp）——覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=98 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=98）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-17/NBIS_evening.json