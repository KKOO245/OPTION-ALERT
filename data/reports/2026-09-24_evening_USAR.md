# 期权晚报 2026-09-24（快照 16:40 ET）

📊 市场环境

SPY $767.18 ｜ QQQ $741.10
VIX 15.67 ↑3.2%（5D -11.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 36.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-24

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 09-25 15P ΔOI +1,812（距现价 +0.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 15.47 → 收盘 15.38（-0.6%） ｜ 今日高 15.56 ｜ 低 15.06 ｜ 昨收 15.83 → 收盘 15.38（-2.8%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-09-29，窗口结束前不做对错判定）

Options: P/C成交量 0.83 | OI比 0.55 | ATM IV 73.9% | Skew -8.6pp | Term 0.97 | ExpMove ±3.1%（近端） | Rank 3%
量化视角： IV 历史低位（Rank 3%，期权偏便宜）｜期限结构正常（Term 0.97）｜Put 保护异常便宜（Skew -8.6pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.55）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.83×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.55×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（1D）±3.1% ｜ 10-02（8D）±7.8% ｜ 10-09（15D）±11.2% ｜ 10-16（22D）±13.9%
   ⇒ IV–VIX Spread: +58.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -5,684,599 | GEX Change vs 上次快照 -13,809,914 | Flip: Primary Flip: 16.00（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 225 / LOW 77 / INVALID 140
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 16.00（全链重定价，覆盖 99%）
Put Wall 15（弱结构｜现价高于该位 2.5%）
最近结构参考: Put Wall 15（现价高于该位 2.5%）
量化视角： 负 Gamma（568万，无历史分位）｜由正转负（1381万）｜现价位于 Flip 下方 3.89%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall，弱结构）；上方 16（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 16（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +2.3k / P +2.5k ｜ Activity HIGH ｜ 1D
10-02  C +2.3k / P +3.2k ｜ Activity HIGH ｜ 8D
10-09  C +0.9k / P +0.3k ｜ Activity HIGH ｜ 15D
10-16  C +1.9k / P +0.3k ｜ Activity HIGH ｜ 22D

📆 09-25 Forward Structure
存量OI: C 29.3k / P 16.2k，今日变化ΔOI: C +2.3k / P +2.5k，平值价格ATM: C $0.20 / P $0.27 ｜ ATM IV 73.9%，净 delta 敞口 -126k shares
Top ΔOI: P 15 +1,812 ｜ P 16 +786
仓位参考: Max Pain 16 ｜ Call Wall 16.5（+7.3%，弱）（OI 1.4k） ｜ Put Wall 15.5（+0.8%）（OI 4.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 73.9%｜历史 Rank 3%（近端代理）｜IV/RV 1.35×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 125,623 股

📆 10-02 Forward Structure
存量OI: C 19.2k / P 9.2k，今日变化ΔOI: C +2.3k / P +3.2k，平值价格ATM: C $0.53 / P $0.67 ｜ ATM IV 66.6%，净 delta 敞口 -154k shares
Top ΔOI: P 16 +1,417 ｜ P 15 +789
仓位参考: Max Pain 17 ｜ Put Wall 16（+4.0%，弱）（OI 2.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 66.6%｜历史 Rank 3%（近端代理）｜IV/RV 1.22×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 154,425 股

📆 10-09 Forward Structure
存量OI: C 6.4k / P 3.3k，今日变化ΔOI: C +0.9k / P +0.3k，平值价格ATM: C $0.81 / P $0.92 ｜ ATM IV 68.5%，净 delta 敞口 3k shares
Top ΔOI: C 16 +114 ｜ P 14 +93
仓位参考: Max Pain 16 ｜ Put Wall 16（+4.0%）（OI 1.2k）
量化解读： 存量 Call 重｜ATM IV 68.5%｜历史 Rank 3%（近端代理）｜IV/RV 1.25×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 3,218 股

📆 10-16 Forward Structure
存量OI: C 37.4k / P 13.2k，今日变化ΔOI: C +1.9k / P +0.3k，平值价格ATM: C $1.01 / P $1.13 ｜ ATM IV 77.6%，净 delta 敞口 -3k shares
Top ΔOI: C 16 -443
仓位参考: Max Pain 17 ｜ Put Wall 15（-2.5%）（OI 5.4k）
量化解读： 存量 Call 重｜ATM IV 77.6%｜历史 Rank 3%（近端代理）｜IV/RV 1.42×（近似）｜净 delta 敞口 负 2,687 股

📅 事件差分（观察，非因果）: 09-25（1D）ATM IV 73.9% vs 10-02 66.6%（差 +7.3pp）——覆盖 耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=28 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=28）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-24/USAR_evening.json