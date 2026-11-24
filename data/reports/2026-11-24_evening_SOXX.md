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
🟡 **近现价集中开仓**: 11-27 135C ΔOI -7,032（距现价 +5.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-27 145C ΔOI +14,663 占该期限总 OI 13.1%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SOXX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SOXX: 今开 133.79 → 收盘 128.62（-3.9%） ｜ 今日高 134.39 ｜ 低 126.00 ｜ 昨收 140.22 → 收盘 128.62（-8.3%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-27，窗口结束前不做对错判定）

Options: P/C成交量 0.77 | OI比 0.50 | ATM IV 77.9% | Skew 10.1pp | Term 0.89 | ExpMove ±6.2%（近端） | Rank 97%
量化视角： IV 历史高位（Rank 97%，期权偏贵）｜期限结构倒挂（Term 0.89，近月 IV 高于远月）｜保护溢价显著（Skew 10.1pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.50）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.77×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.50×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（3D）±6.2% ｜ 12-04（10D）±5.6% ｜ 12-11（17D）±12.1% ｜ 12-18（24D）±11.2%
   ⇒ IV–VIX Spread: +51.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -21,943,185 | GEX Change vs 上次快照 -6,928,991 | Flip: Primary Flip: 136.67（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 577 / LOW 311 / INVALID 628
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 136.67（全链重定价，覆盖 94%）
Put Wall 125（弱结构｜现价高于该位 2.9%）
最近结构参考: Put Wall 125（现价高于该位 2.9%）
量化视角： 负 Gamma（2194万，无历史分位）｜负 Gamma 加深（693万）｜现价位于 Flip 下方 5.89%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 125（Put Wall，弱结构）；上方 145（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 137（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-27  C +7.3k / P +1.6k ｜ Activity HIGH ｜ 3D
12-04  C +0.1k / P +25.5k ｜ Activity HIGH ｜ 10D
12-11  C +1.0k / P +0.4k ｜ Activity HIGH ｜ 17D
12-18  C +10.1k / P +6.7k ｜ Activity HIGH ｜ 24D

📆 11-27 Forward Structure
存量OI: C 74.2k / P 37.5k，今日变化ΔOI: C +7.3k / P +1.6k，平值价格ATM: C $4.55 / P $3.40 ｜ ATM IV 77.9%，净 delta 敞口 -550k shares
Top ΔOI: C 145 +14,663 ｜ C 135 -7,032 ｜ C 130 -6,782
仓位参考: Max Pain 145 ｜ Call Wall 130（+1.1%，弱）（OI 3.9k） ｜ Put Wall 130（+1.1%，弱）（OI 3.2k）
量化解读： 存量 Call 重｜ATM IV 77.9%｜历史 Rank 97%（近端代理）｜IV/RV 0.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 550,499 股

📆 12-04 Forward Structure
存量OI: C 14.0k / P 54.1k，今日变化ΔOI: C +0.1k / P +25.5k，平值价格ATM: C $0.00 / P $7.20 ｜ ATM IV 81.4%，净 delta 敞口 -871k shares
Top ΔOI: P 130 +11,363 ｜ P 110 +11,108 ｜ P 128 +903
仓位参考: Max Pain 150 ｜ Put Wall 130（+1.1%，弱）（OI 11.6k）
量化解读： 存量 Put 重｜ATM IV 81.4%｜历史 Rank 97%（近端代理）｜IV/RV 0.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 870,577 股

📆 12-11 Forward Structure
存量OI: C 5.2k / P 4.9k，今日变化ΔOI: C +1.0k / P +0.4k，平值价格ATM: C $8.97 / P $6.60 ｜ ATM IV 76.0%，净 delta 敞口 -4k shares
Top ΔOI: C 147 +799 ｜ P 140 +113
仓位参考: Max Pain 145
量化解读： 存量两侧均衡｜ATM IV 76.0%｜历史 Rank 97%（近端代理）｜IV/RV 0.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 4,064 股

📆 12-18 Forward Structure
存量OI: C 259.5k / P 204.7k，今日变化ΔOI: C +10.1k / P +6.7k，平值价格ATM: C $10.20 / P $4.20 ｜ ATM IV 74.4%，净 delta 敞口 -112k shares
Top ΔOI: C 155 +5,380 ｜ P 135 +2,527 ｜ P 125 +2,392
仓位参考: Max Pain 155 ｜ Put Wall 125（-2.8%）（OI 33.4k）
量化解读： 存量 Call 重｜ATM IV 74.4%｜历史 Rank 97%（近端代理）｜IV/RV 0.17×（近似）｜净 delta 敞口 负 111,648 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=107 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=107）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-24/SOXX_evening.json