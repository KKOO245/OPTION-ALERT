# 期权晚报 2026-09-29（快照 16:40 ET）

📊 市场环境

SPY $764.20 ｜ QQQ $737.93
VIX 16.04 ↓0.2%（5D +12.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-29

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-29 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.23 ｜ 实际 7.079 ｜ 前值 7.335　✅ 今日已公布
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 待公布 ｜ 前值 2.1
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 09-30 370C ΔOI +4,871（距现价 +4.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-05 390C ΔOI +8,946 占该期限总 OI 20.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 358.42 → 收盘 352.84（-1.6%） ｜ 今日高 358.74 ｜ 低 351.67 ｜ 昨收 357.45 → 收盘 352.84（-1.3%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-02，窗口结束前不做对错判定）

Options: P/C成交量 0.78 | OI比 0.59 | ATM IV 39.7% | Skew -1.0pp | Term 1.12 | ExpMove ±1.7%（近端） | Rank 9%
量化视角： IV 历史低位（Rank 9%，期权偏便宜）｜期限结构正常（Term 1.12）｜Put 保护异常便宜（Skew -1.0pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.59）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.78×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.59×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-30（1D）±1.7% ｜ 10-02（3D）±3.4% ｜ 10-05（6D）±3.9% ｜ 10-07（8D）±4.6%
   ⇒ IV–VIX Spread: +23.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -129,956 | GEX Change vs 上次快照 4,167,132 | Flip: Primary Flip: 352.86（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 1155 / LOW 96 / INVALID 673
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 352.86（全链重定价，覆盖 98%）
最近结构参考: Flip 353（现价低于该位 0.0%）
量化视角： 负 Gamma（13万，无历史分位）｜负 Gamma 缓解（+417万）｜现价位于 Flip 下方 0.00%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 362（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 353（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-30  C +50.7k / P +25.3k ｜ Activity HIGH ｜ 1D
10-02  C +45.5k / P +24.2k ｜ Activity HIGH ｜ 3D
10-05  C +17.1k / P +6.9k ｜ Activity HIGH ｜ 6D
10-07  C +4.6k / P +1.3k ｜ Activity HIGH ｜ 8D

📆 09-30 Forward Structure
存量OI: C 89.5k / P 52.6k，今日变化ΔOI: C +50.7k / P +25.3k，平值价格ATM: C $3.20 / P $2.71 ｜ ATM IV 39.7%，净 delta 敞口 -514k shares
Top ΔOI: C 385 +5,373 ｜ C 370 +4,871
仓位参考: Max Pain 362 ｜ Call Wall 385（+9.1%，弱）（OI 7.1k） ｜ Put Wall 355（+0.6%，弱）（OI 4.4k）
量化解读： 存量 Call 重｜ATM IV 39.7%｜历史 Rank 9%（近端代理）｜IV/RV 1.15×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 513,657 股

📆 10-02 Forward Structure
存量OI: C 214.9k / P 242.2k，今日变化ΔOI: C +45.5k / P +24.2k，平值价格ATM: C $6.25 / P $5.70 ｜ ATM IV 46.4%，净 delta 敞口 -32k shares
Top ΔOI: C 365 +4,011 ｜ C 385 +3,981 ｜ C 370 +3,901
仓位参考: Max Pain 362 ｜ Call Wall 385（+9.1%，弱）（OI 14.2k） ｜ Put Wall 350（-0.8%，弱）（OI 6.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 46.4%｜历史 Rank 9%（近端代理）｜IV/RV 1.34×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 32,200 股

📆 10-05 Forward Structure
存量OI: C 28.5k / P 14.5k，今日变化ΔOI: C +17.1k / P +6.9k，平值价格ATM: C $7.25 / P $6.38 ｜ ATM IV 38.0%，净 delta 敞口 127k shares
Top ΔOI: C 390 +8,946 ｜ C 370 +1,338
仓位参考: Max Pain 365 ｜ Put Wall 325（-7.9%，弱）（OI 1.3k）
量化解读： 存量 Call 重｜ATM IV 38.0%｜历史 Rank 9%（近端代理）｜IV/RV 1.10×（近似）｜净 delta 敞口 正 127,365 股

📆 10-07 Forward Structure
存量OI: C 6.3k / P 2.0k，今日变化ΔOI: C +4.6k / P +1.3k，平值价格ATM: C $8.70 / P $7.68 ｜ ATM IV 38.9%，净 delta 敞口 42k shares
Top ΔOI: C 375 +762 ｜ C 367 +676 ｜ C 377 +444
仓位参考: Max Pain 360 ｜ Call Wall 375（+6.3%，弱）（OI 0.9k） ｜ Put Wall 360（+2.0%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 38.9%｜历史 Rank 9%（近端代理）｜IV/RV 1.12×（近似）｜净 delta 敞口 正 42,129 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=35 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=35）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-29/TSLA_evening.json