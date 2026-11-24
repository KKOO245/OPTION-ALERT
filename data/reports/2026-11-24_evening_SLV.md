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
🟡 **事件差分**: 11-25 ATM IV 68.0% vs 11-27 57.7%（差 +10.3pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-27 35P ΔOI +754（距现价 -5.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-25 43C ΔOI +11,309 占该期限总 OI 16.1%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 38.17 → 收盘 36.84（-3.5%） ｜ 今日高 38.31 ｜ 低 36.71 ｜ 昨收 38.91 → 收盘 36.84（-5.3%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-27，窗口结束前不做对错判定）

Options: P/C成交量 0.95 | OI比 0.39 | ATM IV 68.0% | Skew 9.6pp | Term 0.78 | ExpMove ±3.0%（近端） | Rank 94%
量化视角： IV 历史高位（Rank 94%，期权偏贵）｜期限结构倒挂（Term 0.78，近月 IV 高于远月）｜保护溢价显著（Skew 9.6pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.39）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.95×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.39×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-25（1D）±3.0% ｜ 11-27（3D）±4.1% ｜ 11-30（6D）±5.1% ｜ 12-02（8D）±6.2%
   ⇒ IV–VIX Spread: +41.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -17,660,723 | GEX Change vs 上次快照 -12,500,467 | Flip: Primary Flip: 37.90（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 681 / LOW 238 / INVALID 701
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 37.90（全链重定价，覆盖 96%）
Put Wall 40（弱结构｜现价低于该位 7.9%）
最近结构参考: Flip 38（现价低于该位 2.8%）
量化视角： 负 Gamma（1766万，无历史分位）｜负 Gamma 加深（1250万）｜现价位于 Flip 下方 2.81%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 40（Put Wall，弱结构） / 39（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 38（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-25  C +21.9k / P +6.5k ｜ Activity HIGH ｜ 1D
11-27  C +5.7k / P +2.6k ｜ Activity HIGH ｜ 3D
11-30  C +2.2k / P +0.9k ｜ Activity HIGH ｜ 6D
12-02  C +0.5k / P +0.7k ｜ Activity HIGH ｜ 8D

📆 11-25 Forward Structure
存量OI: C 50.5k / P 19.7k，今日变化ΔOI: C +21.9k / P +6.5k，平值价格ATM: C $0.48 / P $0.61 ｜ ATM IV 68.0%，净 delta 敞口 -189k shares
仓位参考: Max Pain 39 ｜ Call Wall 40.5（+9.9%，弱）（OI 5.7k） ｜ Put Wall 39（+5.9%，弱）（OI 2.9k）
量化解读： 存量 Call 重｜ATM IV 68.0%｜历史 Rank 94%（近端代理）｜IV/RV 1.39×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 188,880 股

📆 11-27 Forward Structure
存量OI: C 114.8k / P 43.8k，今日变化ΔOI: C +5.7k / P +2.6k，平值价格ATM: C $0.70 / P $0.82 ｜ ATM IV 57.7%，净 delta 敞口 -16k shares
Top ΔOI: C 39 +1,705 ｜ P 35 +754
仓位参考: Max Pain 41 ｜ Call Wall 40（+8.6%，弱）（OI 6.3k） ｜ Put Wall 40（+8.6%）（OI 9.2k）
量化解读： 存量 Call 重｜ATM IV 57.7%｜历史 Rank 94%（近端代理）｜IV/RV 1.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 16,362 股

📆 11-30 Forward Structure
存量OI: C 27.6k / P 10.9k，今日变化ΔOI: C +2.2k / P +0.9k，平值价格ATM: C $0.87 / P $1.01 ｜ ATM IV 49.5%，净 delta 敞口 -41k shares
Top ΔOI: C 40 +714 ｜ C 39 +363
仓位参考: Max Pain 40 ｜ Put Wall 39（+5.9%）（OI 4.1k）
量化解读： 存量 Call 重｜ATM IV 49.5%｜历史 Rank 94%（近端代理）｜IV/RV 1.01×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 41,021 股

📆 12-02 Forward Structure
存量OI: C 8.5k / P 3.6k，今日变化ΔOI: C +0.5k / P +0.7k，平值价格ATM: C $1.12 / P $1.17 ｜ ATM IV 52.6%，净 delta 敞口 -29k shares
Top ΔOI: P 37 +474 ｜ C 40 +349
仓位参考: Max Pain 40 ｜ Put Wall 39（+5.9%，弱）（OI 0.7k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 52.6%｜历史 Rank 94%（近端代理）｜IV/RV 1.08×（近似）｜净 delta 敞口 负 28,924 股

📅 事件差分（观察，非因果）: 11-25（1D）ATM IV 68.0% vs 11-27 57.7%（差 +10.3pp）——覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=107 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=107）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-24/SLV_evening.json