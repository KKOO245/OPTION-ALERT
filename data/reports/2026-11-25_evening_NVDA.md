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
🟡 **近现价集中开仓**: 11-30 145P ΔOI +3,275（距现价 -2.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 12-02 167C ΔOI +14,832 占该期限总 OI 16.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 144.02 → 收盘 149.30（+3.7%） ｜ 今日高 150.37 ｜ 低 141.17 ｜ 昨收 155.38 → 收盘 149.30（-3.9%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-12-02，窗口结束前不做对错判定）

Options: P/C成交量 0.86 | OI比 0.69 | ATM IV 64.8% | Skew -8.6pp | Term 1.21 | ExpMove ±4.3%（近端） | Rank 86%
量化视角： IV 历史高位（Rank 86%，期权偏贵）｜期限结构正常偏陡（Term 1.21）｜Put 保护异常便宜（Skew -8.6pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.69）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.86×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.69×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（2D）±4.3% ｜ 11-30（5D）±6.8% ｜ 12-02（7D）±9.2% ｜ 12-04（9D）±11.1%
   ⇒ IV–VIX Spread: +36.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 60,770,315 | GEX Change vs 上次快照 38,146,656 | Flip: Primary Flip: 143.78（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 1383 / LOW 235 / INVALID 1004
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 143.78（全链重定价，覆盖 91%）
Put Wall 150（弱结构｜现价低于该位 0.5%）
最近结构参考: Put Wall 150（现价低于该位 0.5%）
量化视角： 正 Gamma（6077万，无历史分位）｜正 Gamma 增强（+3815万）｜现价位于 Flip 上方 3.84%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 150（Put Wall，弱结构） / 152（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 144（全链重定价，覆盖 91%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-27  C +55.5k / P +38.0k ｜ Activity HIGH ｜ 2D
11-30  C +21.3k / P +20.7k ｜ Activity HIGH ｜ 5D
12-02  C +16.1k / P +4.0k ｜ Activity HIGH ｜ 7D
12-04  C +48.1k / P +8.6k ｜ Activity HIGH ｜ 9D

📆 11-27 Forward Structure
存量OI: C 616.5k / P 417.2k，今日变化ΔOI: C +55.5k / P +38.0k，平值价格ATM: C $3.45 / P $3.05 ｜ ATM IV 74.5%，净 delta 敞口 53k shares
Top ΔOI: C 170 +11,792 ｜ C 160 +10,859 ｜ C 165 +8,314
仓位参考: Max Pain 150 ｜ Call Wall 160（+7.2%，弱）（OI 36.1k） ｜ Put Wall 150（+0.5%，弱）（OI 21.3k）
量化解读： 存量 Call 重｜ATM IV 74.5%｜历史 Rank 86%（近端代理）｜IV/RV 0.59×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 52,946 股

📆 11-30 Forward Structure
存量OI: C 106.4k / P 69.4k，今日变化ΔOI: C +21.3k / P +20.7k，平值价格ATM: C $5.30 / P $4.85 ｜ ATM IV 72.0%，净 delta 敞口 -45k shares
Top ΔOI: P 145 +3,275 ｜ C 165 +2,990 ｜ P 140 +2,549
仓位参考: Max Pain 150 ｜ Call Wall 160（+7.2%，弱）（OI 5.2k） ｜ Put Wall 140（-6.2%，弱）（OI 5.2k）
量化解读： 存量 Call 重｜ATM IV 72.0%｜历史 Rank 86%（近端代理）｜IV/RV 0.57×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 45,330 股

📆 12-02 Forward Structure
存量OI: C 67.3k / P 23.8k，今日变化ΔOI: C +16.1k / P +4.0k，平值价格ATM: C $7.05 / P $6.75 ｜ ATM IV 82.8%，净 delta 敞口 292k shares
Top ΔOI: C 167 +14,832 ｜ C 200 -5,004 ｜ C 170 -1,441
仓位参考: Max Pain 155 ｜ Call Wall 160（+7.2%，弱）（OI 3.4k） ｜ Put Wall 155（+3.8%，弱）（OI 1.9k）
量化解读： 存量 Call 重｜ATM IV 82.8%｜历史 Rank 86%（近端代理）｜IV/RV 0.65×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 292,175 股

📆 12-04 Forward Structure
存量OI: C 274.0k / P 179.7k，今日变化ΔOI: C +48.1k / P +8.6k，平值价格ATM: C $8.40 / P $8.10 ｜ ATM IV 88.4%，净 delta 敞口 35k shares
Top ΔOI: P 80 -19,474 ｜ C 165 +10,839 ｜ C 170 +9,417
仓位参考: Max Pain 160 ｜ Call Wall 160（+7.2%，弱）（OI 16.1k） ｜ Put Wall 160（+7.2%，弱）（OI 10.5k）
量化解读： 存量 Call 重｜ATM IV 88.4%｜历史 Rank 86%（近端代理）｜IV/RV 0.70×（近似）｜净 delta 敞口 正 35,426 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-25/NVDA_evening.json