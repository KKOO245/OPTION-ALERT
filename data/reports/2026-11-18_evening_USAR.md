# 期权晚报 2026-11-18（快照 16:40 ET）

📊 市场环境

SPY $730.20 ｜ QQQ $nan
VIX 24.56 ↓3.5%（5D +40.4%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 24.6（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 1.309 ｜ 前值 1.191　✅ 今日已公布
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 1.295 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🔴 **事件差分**: 11-20（2D）ATM IV 140.6% vs 11-27 106.8%（差 +33.7pp），覆盖 新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 12-04 6C ΔOI +42（距现价 -0.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 6.66 → 收盘 6.56（-1.5%） ｜ 今日高 7.52 ｜ 低 6.51 ｜ 昨收 6.64 → 收盘 6.56（-1.1%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-25，窗口结束前不做对错判定）

Options: P/C成交量 0.25 | OI比 0.48 | ATM IV 140.6% | Skew -18.6pp | Term 0.78 | ExpMove ±8.1%（近端） | Rank 77%
量化视角： IV 历史高位（Rank 77%，期权偏贵）｜期限结构倒挂（Term 0.78，近月 IV 高于远月）｜Put 保护异常便宜（Skew -18.6pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.48）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.25×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.48×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（2D）±8.1% ｜ 11-27（9D）±13.4% ｜ 12-04（16D）±19.1% ｜ 12-11（23D）±23.9%
   ⇒ IV–VIX Spread: +116.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 987,776 | GEX Change vs 上次快照 840,957 | Flip: Primary Flip: 5.84（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 133 / LOW 100 / INVALID 199
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 5.84（全链重定价，覆盖 95%）
最近结构参考: Flip 6（现价高于该位 12.2%）
量化视角： 正 Gamma（99万，无历史分位）｜正 Gamma 增强（+84万）｜现价位于 Flip 上方 12.24%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 10（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 6（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C +1.0k / P -2.7k ｜ Activity MEDIUM △ ｜ 2D
11-27  C +0.7k / P -22 ｜ Activity HIGH ｜ 9D
12-04  C +0.2k / P +73 ｜ Activity MEDIUM △ ｜ 16D
12-11  C +0.1k / P -30 ｜ Activity MEDIUM △ ｜ 23D

📆 11-20 Forward Structure
存量OI: C 56.7k / P 27.3k，今日变化ΔOI: C +1.0k / P -2.7k，平值价格ATM: C $0.30 / P $0.23 ｜ ATM IV 140.6%，净 delta 敞口 338k shares
Top ΔOI: P 8 -1,121 ｜ P 10 -614 ｜ P 8 -531
仓位参考: Max Pain 10 ｜ Put Wall 7（+6.7%，弱）（OI 3.1k）
量化解读： 存量 Call 重｜ATM IV 140.6%｜历史 Rank 77%（近端代理）｜IV/RV 1.22×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 338,167 股

📆 11-27 Forward Structure
存量OI: C 17.4k / P 3.2k，今日变化ΔOI: C +0.7k / P -22，平值价格ATM: C $0.55 / P $0.33 ｜ ATM IV 106.8%，净 delta 敞口 29k shares
Top ΔOI: C 7 +149
仓位参考: Max Pain 8 ｜ Put Wall 7（+6.7%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 106.8%｜历史 Rank 77%（近端代理）｜IV/RV 0.93×（近似）｜净 delta 敞口 正 28,809 股

12-04（MEDIUM △）Top ΔOI: 6P +61 ｜ 6C +42
12-04（MEDIUM △）仓位参考: Max Pain 9 ｜ Put Wall 7（+6.7%，弱）（OI 0.1k）

12-11（MEDIUM △）Top ΔOI: 7C +63
12-11（MEDIUM △）仓位参考: Max Pain 9 ｜ Call Wall 7（+6.7%，弱）（OI 85） ｜ Put Wall 7（+6.7%，弱）（OI 76）

📅 事件差分（观察，非因果）: 11-20（2D）ATM IV 140.6% vs 11-27 106.8%（差 +33.7pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-18/USAR_evening.json