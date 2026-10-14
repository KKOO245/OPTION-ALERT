# 期权晚报 2026-10-14（快照 16:42 ET）

📊 市场环境

SPY $769.60 ｜ QQQ $728.95
VIX 16.87 ↑10.5%（5D +11.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 32.4（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-14

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 2.6 ｜ 前值 2.4　✅ 今日已公布
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.6 ｜ 实际 3.7 ｜ 前值 3.4　✅ 今日已公布
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 0.6 ｜ 前值 0.4　✅ 今日已公布
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览
🟡 **事件差分**: 10-16 ATM IV 49.7% vs 10-19 37.7%（差 +12.0pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-16 80P ΔOI +1,404（距现价 -4.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 84.95 → 收盘 83.40（-1.8%） ｜ 今日高 85.62 ｜ 低 82.46 ｜ 昨收 87.24 → 收盘 83.40（-4.4%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-19，窗口结束前不做对错判定）

Options: P/C成交量 0.34 | OI比 0.67 | ATM IV 49.7% | Skew 4.7pp | Term 0.87 | ExpMove ±3.0%（近端） | Rank 82%
量化视角： IV 历史高位（Rank 82%，期权偏贵）｜期限结构倒挂（Term 0.87，近月 IV 高于远月）｜保护溢价中性（Skew 4.7pp）｜存量 Call 偏重（OI比 0.67）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.34×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.67×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（2D）±3.0% ｜ 10-19（5D）±3.5% ｜ 10-21（7D）±4.3% ｜ 10-23（9D）±5.0%
   ⇒ IV–VIX Spread: +32.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -59,332,073 | GEX Change vs 上次快照 -5,375,087 | Flip: Primary Flip: 86.74（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 549 / LOW 170 / INVALID 425
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 86.74（全链重定价，覆盖 91%）
Put Wall 80（弱结构｜现价高于该位 4.3%）
最近结构参考: Flip 87（现价低于该位 3.8%）
量化视角： 负 Gamma（5933万，无历史分位）｜负 Gamma 加深（538万）｜现价位于 Flip 下方 3.85%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 80（Put Wall，弱结构）；上方 89（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 87（全链重定价，覆盖 91%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +0.5k / P -1.2k ｜ Activity MEDIUM △ ｜ 2D
10-19  C +27 / P +0.2k ｜ Activity HIGH ｜ 5D
10-21  C +0.1k / P +22 ｜ Activity MEDIUM △ ｜ 7D
10-23  C +1.5k / P +0.6k ｜ Activity HIGH ｜ 9D

📆 10-16 Forward Structure
存量OI: C 192.2k / P 128.3k，今日变化ΔOI: C +0.5k / P -1.2k，平值价格ATM: C $1.19 / P $1.33 ｜ ATM IV 49.7%，净 delta 敞口 338k shares
Top ΔOI: P 98 -1,589 ｜ P 80 +1,404 ｜ P 97 -738
仓位参考: Max Pain 89 ｜ Call Wall 88.5（+6.1%，弱）（OI 11.2k） ｜ Put Wall 85（+1.9%，弱）（OI 10.8k）
量化解读： 存量 Call 重｜ATM IV 49.7%｜历史 Rank 82%（近端代理）｜IV/RV 1.41×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 337,762 股

📆 10-19 Forward Structure
存量OI: C 1.7k / P 0.6k，今日变化ΔOI: C +27 / P +0.2k，平值价格ATM: C $1.47 / P $1.44 ｜ ATM IV 37.7%，净 delta 敞口 -15k shares
Top ΔOI: P 89 +188 ｜ P 88 -30 ｜ C 85 +12
仓位参考: Max Pain 89 ｜ Put Wall 85（+1.9%，弱）（OI 81）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 37.7%｜历史 Rank 82%（近端代理）｜IV/RV 1.07×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 14,509 股

10-21（MEDIUM △）Top ΔOI: 90C +94 ｜ 80P +15
10-21（MEDIUM △）仓位参考: Max Pain 85 ｜ Put Wall 79（-5.3%）（OI 2.4k）

📆 10-23 Forward Structure
存量OI: C 10.9k / P 14.0k，今日变化ΔOI: C +1.5k / P +0.6k，平值价格ATM: C $2.05 / P $2.16 ｜ ATM IV 41.6%，净 delta 敞口 -20k shares
Top ΔOI: C 90 +560 ｜ C 91 +348
仓位参考: Max Pain 90 ｜ Call Wall 87（+4.3%，弱）（OI 0.3k） ｜ Put Wall 85（+1.9%，弱）（OI 1.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 41.6%｜历史 Rank 82%（近端代理）｜IV/RV 1.18×（近似）｜净 delta 敞口 负 19,823 股

📅 事件差分（观察，非因果）: 10-16（2D）ATM IV 49.7% vs 10-19 37.7%（差 +12.0pp）——覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY、Inflation Rate YoY、Inflation Rate MoM、PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-14/GDX_evening.json