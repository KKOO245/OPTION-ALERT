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

🔍 重点速览
🔴 **事件差分**: 11-13（3D）ATM IV 240.7% vs 11-20 158.7%（差 +82.0pp），覆盖 Core Inflation Rate MoM、Inflation Rate MoM 等
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 11-13 140C ΔOI +4,463（距现价 +4.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 137.42 → 收盘 134.00（-2.5%） ｜ 今日高 146.23 ｜ 低 130.90 ｜ 昨收 141.45 → 收盘 134.00（-5.3%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-13，窗口结束前不做对错判定）

Options: P/C成交量 0.67 | OI比 0.54 | ATM IV 240.7% | Skew 12.6pp | Term 0.49 | ExpMove ±17.4%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.49，近月 IV 高于远月）｜保护溢价显著（Skew 12.6pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.54）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.67×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.54×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（3D）±17.4% ｜ 11-20（10D）±20.9% ｜ 11-27（17D）±23.4% ｜ 12-04（24D）±25.9%
   ⇒ IV–VIX Spread: +221.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -2,471,240 | GEX Change vs 上次快照 -3,852,964 | Flip: Primary Flip: 140.27（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 735 / LOW 47 / INVALID 98
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 140.27（全链重定价，覆盖 100%）
最近结构参考: Flip 140（现价低于该位 4.5%）
量化视角： 负 Gamma（247万，无历史分位）｜由正转负（385万）｜现价位于 Flip 下方 4.47%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 145（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 140（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +15.9k / P +6.6k ｜ Activity HIGH ｜ 3D
11-20  C +2.1k / P -0.7k ｜ Activity MEDIUM △ ｜ 10D
11-27  C +0.6k / P +1.3k ｜ Activity HIGH ｜ 17D
12-04  C +0.4k / P +0.2k ｜ Activity HIGH ｜ 24D

📆 11-13 Forward Structure
存量OI: C 75.8k / P 41.1k，今日变化ΔOI: C +15.9k / P +6.6k，平值价格ATM: C $11.62 / P $11.66 ｜ ATM IV 240.7%，净 delta 敞口 366k shares
Top ΔOI: C 140 +4,463 ｜ C 187 +1,473 ｜ C 144 +936
仓位参考: Max Pain 145 ｜ Call Wall 140（+4.5%，弱）（OI 5.8k） ｜ Put Wall 130（-3.0%）（OI 3.2k）
量化解读： 存量 Call 重｜ATM IV 240.7%｜历史 Rank 100%（近端代理）｜IV/RV 2.15×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 365,621 股

11-20（MEDIUM △）Top ΔOI: 115P -967 ｜ 170C +423
11-20（MEDIUM △）仓位参考: Max Pain 175 ｜ Put Wall 140（+4.5%，弱）（OI 5.1k）

📆 11-27 Forward Structure
存量OI: C 13.3k / P 16.8k，今日变化ΔOI: C +0.6k / P +1.3k，平值价格ATM: C $15.51 / P $15.80 ｜ ATM IV 132.7%，净 delta 敞口 3k shares
Top ΔOI: P 90 +530 ｜ P 95 +414
仓位参考: Max Pain 190 ｜ Call Wall 145（+8.2%，弱）（OI 0.3k） ｜ Put Wall 140（+4.5%，弱）（OI 0.7k）
量化解读： 存量 Put 重｜ATM IV 132.7%｜历史 Rank 100%（近端代理）｜IV/RV 1.19×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 3,328 股

📆 12-04 Forward Structure
存量OI: C 3.8k / P 4.9k，今日变化ΔOI: C +0.4k / P +0.2k，平值价格ATM: C $16.50 / P $18.20 ｜ ATM IV 120.3%，净 delta 敞口 -512 shares
Top ΔOI: P 205 +43
仓位参考: Max Pain 155 ｜ Call Wall 140（+4.5%，弱）（OI 0.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 120.3%｜历史 Rank 100%（近端代理）｜IV/RV 1.08×（近似）｜净 delta 敞口 负 512 股

📅 事件差分（观察，非因果）: 11-13（3D）ATM IV 240.7% vs 11-20 158.7%（差 +82.0pp）——覆盖 Core Inflation Rate MoM、Inflation Rate MoM 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=93 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=93）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-10/NBIS_evening.json