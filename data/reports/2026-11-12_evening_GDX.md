# 期权晚报 2026-11-12（快照 16:40 ET）

📊 市场环境

SPY $757.12 ｜ QQQ $688.17
VIX 18.70 ↑6.9%（5D -33.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 39.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-12

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 3.75 ｜ 前值 3.97　✅ 今日已公布
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **事件差分**: 11-13 ATM IV 53.6% vs 11-16 39.2%（差 +14.4pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-13 83P ΔOI +441（距现价 +2.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 82.52 → 收盘 81.84（-0.8%） ｜ 今日高 83.74 ｜ 低 81.66 ｜ 昨收 85.21 → 收盘 81.84（-4.0%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-17，窗口结束前不做对错判定）

Options: P/C成交量 0.28 | OI比 0.46 | ATM IV 53.6% | Skew -2.0pp | Term 0.79 | ExpMove ±2.5%（近端） | Rank 86%
量化视角： IV 历史高位（Rank 86%，期权偏贵）｜期限结构倒挂（Term 0.79，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.0pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.46）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.28×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.46×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（1D）±2.5% ｜ 11-16（4D）±3.1% ｜ 11-18（6D）±4.4% ｜ 11-20（8D）±5.2%
   ⇒ IV–VIX Spread: +34.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -46,206,027 | GEX Change vs 上次快照 -1,187,676 | Flip: Primary Flip: 84.14（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 86%（带内） ｜ IV 有效性: VALID 585 / LOW 207 / INVALID 466
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 84.14（全链重定价，覆盖 86%）
最近结构参考: Flip 84（现价低于该位 2.7%）
量化视角： 负 Gamma（4621万，无历史分位）｜负 Gamma 加深（119万）｜现价位于 Flip 下方 2.73%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 85（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 84（全链重定价，覆盖 86%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C -0.3k / P +0.8k ｜ Activity MEDIUM △ ｜ 1D
11-16  C +0.6k / P +0.6k ｜ Activity HIGH ｜ 4D
11-18  C +0.2k / P +0.1k ｜ Activity HIGH ｜ 6D
11-20  C -1.1k / P +2.3k ｜ Activity MEDIUM △ ｜ 8D

📆 11-13 Forward Structure
存量OI: C 83.0k / P 37.9k，今日变化ΔOI: C -0.3k / P +0.8k，平值价格ATM: C $0.90 / P $1.12 ｜ ATM IV 53.6%，净 delta 敞口 -49k shares
Top ΔOI: P 83 +441 ｜ C 88 -163 ｜ P 79 +158
仓位参考: Max Pain 85 ｜ Put Wall 79（-3.5%，弱）（OI 6.8k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 53.6%｜历史 Rank 86%（近端代理）｜IV/RV 0.97×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 48,960 股

📆 11-16 Forward Structure
存量OI: C 2.5k / P 2.0k，今日变化ΔOI: C +0.6k / P +0.6k，平值价格ATM: C $1.50 / P $1.07 ｜ ATM IV 39.2%，净 delta 敞口 -22k shares
Top ΔOI: P 79 +305 ｜ C 87 +217 ｜ C 89 +215
仓位参考: Max Pain 86 ｜ Call Wall 87（+6.3%，弱）（OI 0.4k） ｜ Put Wall 84（+2.6%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 39.2%｜历史 Rank 86%（近端代理）｜IV/RV 0.71×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 21,950 股

📆 11-18 Forward Structure
存量OI: C 0.8k / P 0.8k，今日变化ΔOI: C +0.2k / P +0.1k，平值价格ATM: C $1.99 / P $1.62 ｜ ATM IV 42.1%，净 delta 敞口 -4k shares
Top ΔOI: C 86 +106 ｜ P 81 +43
仓位参考: Max Pain 85 ｜ Call Wall 86（+5.1%，弱）（OI 0.1k） ｜ Put Wall 84（+2.6%）（OI 0.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 42.1%｜历史 Rank 86%（近端代理）｜IV/RV 0.76×（近似）｜净 delta 敞口 负 4,083 股

11-20（MEDIUM △）Top ΔOI: 83P +1,953 ｜ 80P +983
11-20（MEDIUM △）仓位参考: Max Pain 87 ｜ Call Wall 84（+2.6%，弱）（OI 8.5k） ｜ Put Wall 80（-2.2%，弱）（OI 24.8k）

📅 事件差分（观察，非因果）: 11-13（1D）ATM IV 53.6% vs 11-16 39.2%（差 +14.4pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=94 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=94）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-12/GDX_evening.json