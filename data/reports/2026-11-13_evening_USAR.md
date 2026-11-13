# 期权晚报 2026-11-13（快照 16:40 ET）

📊 市场环境

SPY $754.37 ｜ QQQ $679.89
VIX 19.30 ↑3.2%（5D -24.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-13

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 0.3 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-20 8C ΔOI +1,591（距现价 +4.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 8.09 → 收盘 8.16（+0.9%） ｜ 今日高 8.36 ｜ 低 7.76 ｜ 昨收 8.07 → 收盘 8.16（+1.1%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-18，窗口结束前不做对错判定）

Options: P/C成交量 0.36 | OI比 0.29 | ATM IV 268.2% | Skew -4.8pp | Term 0.38 | ExpMove ±10.9%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.38，近月 IV 高于远月）｜Put 保护异常便宜（Skew -4.8pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.29）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.36×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.29×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（7D）±10.9% ｜ 11-27（14D）±14.9% ｜ 12-04（21D）±18.8% ｜ 12-11（28D）±21.2%
   ⇒ IV–VIX Spread: +248.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 1,686,959 | GEX Change vs 上次快照 -2,651,817 | Flip: Primary Flip: 7.67（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 185 / LOW 86 / INVALID 153
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 7.67（全链重定价，覆盖 91%）
Put Wall 8（弱结构｜现价高于该位 2.0%）
最近结构参考: Put Wall 8（现价高于该位 2.0%）
量化视角： 正 Gamma（169万，无历史分位）｜正 Gamma 减弱（265万）｜现价位于 Flip 上方 6.37%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 8（Put Wall，弱结构）；上方 8（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 8（全链重定价，覆盖 91%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C +2.9k / P +0.3k ｜ Activity HIGH ｜ 7D
11-27  C +1.5k / P +38 ｜ Activity MEDIUM △ ｜ 14D
12-04  C +30 / P +41 ｜ Activity MEDIUM △ ｜ 21D
12-11  C +95 / P +84 ｜ Activity HIGH ｜ 28D

📆 11-20 Forward Structure
存量OI: C 50.9k / P 32.9k，今日变化ΔOI: C +2.9k / P +0.3k，平值价格ATM: C $0.52 / P $0.37 ｜ ATM IV 97.6%，净 delta 敞口 57k shares
Top ΔOI: C 8 +1,591 ｜ P 7 +510
仓位参考: Max Pain 10 ｜ Call Wall 8.5（+4.2%，弱）（OI 2.5k） ｜ Put Wall 8（-2.0%，弱）（OI 6.9k）
量化解读： 存量 Call 重｜ATM IV 97.6%｜历史 Rank 100%（近端代理）｜IV/RV 0.92×（近似）｜净 delta 敞口 正 57,429 股

11-27（MEDIUM △）Top ΔOI: 8C +1,411
11-27（MEDIUM △）仓位参考: Max Pain 8 ｜ Call Wall 8（-2.0%，弱）（OI 2.7k） ｜ Put Wall 8（-2.0%，弱）（OI 0.5k）

12-04（MEDIUM △）Top ΔOI: 8C +11 ｜ 8P +10
12-04（MEDIUM △）仓位参考: Max Pain 10 ｜ Call Wall 8（-2.0%，弱）（OI 0.1k） ｜ Put Wall 8.5（+4.2%）（OI 0.3k）

📆 12-11 Forward Structure
存量OI: C 1.3k / P 1.1k，今日变化ΔOI: C +95 / P +84，平值价格ATM: C $0.97 / P $0.76 ｜ ATM IV 100.6%，净 delta 敞口 210 shares
Top ΔOI: C 8 +55 ｜ P 8 +44
仓位参考: Max Pain 10 ｜ Call Wall 7.5（-8.1%，弱）（OI 97） ｜ Put Wall 8（-2.0%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 100.6%｜历史 Rank 100%（近端代理）｜IV/RV 0.95×（近似）｜净 delta 敞口 正 210 股

📅 事件差分（观察，非因果）: 11-20（7D）ATM IV 97.6% vs 11-27 90.2%（差 +7.4pp）——覆盖 PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=94 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=94）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-13/USAR_evening.json