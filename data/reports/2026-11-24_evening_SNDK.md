# 期权晚报 2026-11-24（快照 16:40 ET）

📊 市场环境

SPY $718.78 ｜ QQQ $638.10
VIX 26.36 ↓1.0%（5D +3.5%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 17.4（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-24

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-25 08:30　【高】Personal Spending MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.5
- 周三 11-25 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 11-25 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 11-25 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 3.5 ｜ 实际 待公布 ｜ 前值 1.5
- 周三 11-25 08:30　【高】耐用品订单 Orders MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 1.8

🔍 重点速览
🟡 **近现价集中开仓**: 12-18 75P ΔOI -25,030（距现价 -3.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 82.74 → 收盘 77.95（-5.8%） ｜ 今日高 83.82 ｜ 低 74.87 ｜ 昨收 87.71 → 收盘 77.95（-11.1%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-27，窗口结束前不做对错判定）

Options: P/C成交量 1.04 | OI比 0.44 | ATM IV 128.9% | Skew 15.4pp | Term 0.89 | ExpMove ±9.1%（近端） | Rank 83%
量化视角： IV 历史高位（Rank 83%，期权偏贵）｜期限结构倒挂（Term 0.89，近月 IV 高于远月）｜保护溢价显著（Skew 15.4pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.44）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.04×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.44×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（3D）±9.1% ｜ 12-04（10D）±16.6% ｜ 12-11（17D）±22.2% ｜ 12-18（24D）±24.2%
   ⇒ IV–VIX Spread: +102.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -29,652,398 | GEX Change vs 上次快照 -9,518,106 | Flip: Primary Flip: 89.03（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1158 / LOW 962 / INVALID 3784
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 89.03（全链重定价，覆盖 100%）
Put Wall 75（弱结构｜现价高于该位 3.9%）
最近结构参考: Put Wall 75（现价高于该位 3.9%）
量化视角： 负 Gamma（2965万，无历史分位）｜负 Gamma 加深（952万）｜现价位于 Flip 下方 12.45%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 75（Put Wall，弱结构）；上方 98（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 89（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-27  C +12.7k / P +12.1k ｜ Activity HIGH ｜ 3D
12-04  C +0.4k / P +1.3k ｜ Activity MEDIUM △ ｜ 10D
12-11  C +1.2k / P +0.5k ｜ Activity MEDIUM △ ｜ 17D
12-18  C +4.3k / P -19.8k ｜ Activity HIGH ｜ 24D

📆 11-27 Forward Structure
存量OI: C 297.4k / P 131.6k，今日变化ΔOI: C +12.7k / P +12.1k，平值价格ATM: C $3.57 / P $3.50 ｜ ATM IV 128.9%，净 delta 敞口 -572k shares
Top ΔOI: P 100 -1,971
仓位参考: Max Pain 98 ｜ Put Wall 80（+2.6%，弱）（OI 4.9k）
量化解读： 存量 Call 重｜ATM IV 128.9%｜历史 Rank 83%（近端代理）｜IV/RV 0.16×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 572,455 股

12-04（MEDIUM △）Top ΔOI: 100C +1,642 ｜ 85C -1,524
12-04（MEDIUM △）仓位参考: Max Pain 102 ｜ Call Wall 85（+9.0%，弱）（OI 1.8k） ｜ Put Wall 71.25（-8.6%，弱）（OI 2.7k）

12-11（MEDIUM △）Top ΔOI: 82P +293 ｜ 95C +190
12-11（MEDIUM △）仓位参考: Max Pain 105 ｜ Call Wall 80（+2.6%，弱）（OI 2.0k） ｜ Put Wall 80（+2.6%）（OI 10.6k）

📆 12-18 Forward Structure
存量OI: C 564.8k / P 532.5k，今日变化ΔOI: C +4.3k / P -19.8k，平值价格ATM: C $9.88 / P $9.00 ｜ ATM IV 119.2%，净 delta 敞口 911k shares
Top ΔOI: P 75 -25,030 ｜ C 95 +2,343 ｜ P 80 +1,312
仓位参考: Max Pain 116 ｜ Put Wall 75（-3.8%，弱）（OI 44.0k）
量化解读： 存量两侧均衡｜ATM IV 119.2%｜历史 Rank 83%（近端代理）｜IV/RV 0.15×（近似）｜净 delta 敞口 正 910,838 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=107 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=107）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-24/SNDK_evening.json