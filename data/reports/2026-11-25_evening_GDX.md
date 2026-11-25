# 期权晚报 2026-11-25（快照 16:40 ET）

📊 市场环境

SPY $716.70 ｜ QQQ $633.93
VIX 28.29 ↑7.3%（5D +15.2%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 15.2（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-25

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-25 08:30　【高】Personal Spending MoM　预测 0.4 ｜ 实际 0.3 ｜ 前值 0.6　✅ 今日已公布
- 周三 11-25 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周三 11-25 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 0.7 ｜ 前值 0.3　✅ 今日已公布
- 周三 11-25 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 3.5 ｜ 实际 4.3 ｜ 前值 1.5　✅ 今日已公布
- 周三 11-25 08:30　【高】耐用品订单 Orders MoM　预测 0.6 ｜ 实际 0.2 ｜ 前值 1.8　✅ 今日已公布

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-27 77C ΔOI -3,749（距现价 +4.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-30 80C ΔOI +1,038 占该期限总 OI 18.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 68.76 → 收盘 73.89（+7.5%） ｜ 今日高 74.26 ｜ 低 67.93 ｜ 昨收 71.37 → 收盘 73.89（+3.5%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-12-02，窗口结束前不做对错判定）

Options: P/C成交量 0.52 | OI比 0.63 | ATM IV 89.6% | Skew 21.1pp | Term 0.61 | ExpMove ±3.3%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.61，近月 IV 高于远月）｜保护溢价显著（Skew 21.1pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.63）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.52×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.63×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（2D）±3.3% ｜ 11-30（5D）±5.2% ｜ 12-02（7D）±9.1% ｜ 12-04（9D）±7.0%
   ⇒ IV–VIX Spread: +61.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 11,012,749 | GEX Change vs 上次快照 42,199,162 | Flip: Primary Flip: 72.67（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 556 / LOW 206 / INVALID 550
结构观察区: Primary Flip 72.67（全链重定价，覆盖 96%）
Put Wall 75（弱结构｜现价低于该位 1.5%）
最近结构参考: Put Wall 75（现价低于该位 1.5%）
量化视角： 正 Gamma（1101万，无历史分位）｜由负转正（+4220万）｜现价位于 Flip 上方 1.67%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 72（MaxPain，仅结算参考）；上方 75（Put Wall，弱结构）。
• Gamma 区域：切换参考 73（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-27  C -5.7k / P +1.4k ｜ Activity HIGH ｜ 2D
11-30  C +1.1k / P +0.5k ｜ Activity HIGH ｜ 5D
12-02  C +0.1k / P +0.3k ｜ Activity HIGH ｜ 7D
12-04  C +0.4k / P -0.1k ｜ Activity LOW ｜ 9D

📆 11-27 Forward Structure
存量OI: C 85.0k / P 15.0k，今日变化ΔOI: C -5.7k / P +1.4k，平值价格ATM: C $1.23 / P $1.24 ｜ ATM IV 59.2%，净 delta 敞口 126k shares
Top ΔOI: C 77 -3,749 ｜ C 80 -2,265
仓位参考: Max Pain 71 ｜ Call Wall 71（-3.9%，弱）（OI 15.0k） ｜ Put Wall 70（-5.3%，弱）（OI 2.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 59.2%｜历史 Rank 100%（近端代理）｜IV/RV 0.97×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 125,977 股

📆 11-30 Forward Structure
存量OI: C 3.4k / P 2.2k，今日变化ΔOI: C +1.1k / P +0.5k，平值价格ATM: C $1.77 / P $2.09 ｜ ATM IV 55.1%，净 delta 敞口 10k shares
Top ΔOI: C 80 +1,038 ｜ P 70 +96
仓位参考: Max Pain 72 ｜ Call Wall 75（+1.5%，弱）（OI 0.8k） ｜ Put Wall 70（-5.3%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 55.1%｜历史 Rank 100%（近端代理）｜IV/RV 0.90×（近似）｜净 delta 敞口 正 10,241 股

📆 12-02 Forward Structure
存量OI: C 1.0k / P 0.5k，今日变化ΔOI: C +0.1k / P +0.3k，平值价格ATM: C $2.25 / P $4.48 ｜ ATM IV 53.8%，净 delta 敞口 -4k shares
Top ΔOI: P 71 +250 ｜ C 75 +55 ｜ P 69 +32
仓位参考: Max Pain 73 ｜ Call Wall 75（+1.5%）（OI 0.3k） ｜ Put Wall 71（-3.9%）（OI 0.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 53.8%｜历史 Rank 100%（近端代理）｜IV/RV 0.88×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 3,822 股

12-04（Activity LOW）仓位参考: Max Pain 76 ｜ Call Wall 76（+2.9%）（OI 3.0k） ｜ Put Wall 70（-5.3%）（OI 6.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_put_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-25/GDX_evening.json