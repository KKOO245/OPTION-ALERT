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
🟡 **事件差分**: 11-25 ATM IV 61.0% vs 11-27 47.9%（差 +13.1pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-25 70P ΔOI +274（距现价 -1.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-25 75C ΔOI +568 占该期限总 OI 11.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 71.91 → 收盘 71.37（-0.8%） ｜ 今日高 73.42 ｜ 低 70.96 ｜ 昨收 72.80 → 收盘 71.37（-2.0%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-12-01，窗口结束前不做对错判定）

Options: P/C成交量 0.81 | OI比 0.48 | ATM IV 61.0% | Skew 5.6pp | Term 0.80 | ExpMove ±2.9%（近端） | Rank 94%
量化视角： IV 历史高位（Rank 94%，期权偏贵）｜期限结构倒挂（Term 0.80，近月 IV 高于远月）｜保护溢价中性（Skew 5.6pp）｜存量 Call 偏重（OI比 0.48）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.81×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.48×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-25（1D）±2.9% ｜ 11-27（3D）±3.6% ｜ 11-30（6D）±5.0% ｜ 12-02（8D）±6.1%
   ⇒ IV–VIX Spread: +34.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -4,992,765 | GEX Change vs 上次快照 -1,499,898 | Flip: Primary Flip: 71.79（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 474 / LOW 224 / INVALID 592
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 71.79（全链重定价，覆盖 96%）
Put Wall 75（弱结构｜现价低于该位 4.8%）
最近结构参考: Flip 72（现价低于该位 0.6%）
量化视角： 负 Gamma（499万，无历史分位）｜负 Gamma 加深（150万）｜现价位于 Flip 下方 0.58%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 75（Put Wall，弱结构） / 73（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 72（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-25  C +1.2k / P +0.4k ｜ Activity HIGH ｜ 1D
11-27  C +1.1k / P +1.4k ｜ Activity HIGH ｜ 3D
11-30  C +1.0k / P +0.2k ｜ Activity HIGH ｜ 6D
12-02  C +0.2k / P +55 ｜ Activity HIGH ｜ 8D

📆 11-25 Forward Structure
存量OI: C 3.2k / P 1.6k，今日变化ΔOI: C +1.2k / P +0.4k，平值价格ATM: C $1.28 / P $0.82 ｜ ATM IV 61.0%，净 delta 敞口 -5k shares
Top ΔOI: C 75 +568 ｜ P 70 +274 ｜ C 76 +263
仓位参考: Max Pain 73 ｜ Call Wall 75（+5.1%）（OI 0.9k） ｜ Put Wall 70（-1.9%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 61.0%｜历史 Rank 94%（近端代理）｜IV/RV 0.99×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 5,043 股

📆 11-27 Forward Structure
存量OI: C 90.8k / P 13.6k，今日变化ΔOI: C +1.1k / P +1.4k，平值价格ATM: C $1.65 / P $0.91 ｜ ATM IV 47.9%，净 delta 敞口 -5k shares
Top ΔOI: C 77 +881 ｜ P 69 +619 ｜ C 75 +395
仓位参考: Max Pain 71 ｜ Call Wall 71（-0.5%，弱）（OI 15.0k） ｜ Put Wall 70（-1.9%，弱）（OI 2.0k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 47.9%｜历史 Rank 94%（近端代理）｜IV/RV 0.77×（近似）｜净 delta 敞口 负 5,347 股

📆 11-30 Forward Structure
存量OI: C 2.2k / P 1.7k，今日变化ΔOI: C +1.0k / P +0.2k，平值价格ATM: C $2.23 / P $1.30 ｜ ATM IV 43.7%，净 delta 敞口 12k shares
Top ΔOI: C 75 +565 ｜ P 65 +183
仓位参考: Max Pain 73 ｜ Call Wall 75（+5.1%，弱）（OI 0.8k） ｜ Put Wall 70（-1.9%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 43.7%｜历史 Rank 94%（近端代理）｜IV/RV 0.71×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 11,583 股

📆 12-02 Forward Structure
存量OI: C 0.9k / P 0.2k，今日变化ΔOI: C +0.2k / P +55，平值价格ATM: C $2.50 / P $1.86 ｜ ATM IV 50.0%，净 delta 敞口 -423 shares
Top ΔOI: P 76 +40
仓位参考: Max Pain 73 ｜ Call Wall 75（+5.1%，弱）（OI 0.2k） ｜ Put Wall 74（+3.7%，弱）（OI 55）
量化解读： 存量 Call 重｜ATM IV 50.0%｜历史 Rank 94%（近端代理）｜IV/RV 0.81×（近似）｜净 delta 敞口 负 423 股

📅 事件差分（观察，非因果）: 11-25（1D）ATM IV 61.0% vs 11-27 47.9%（差 +13.1pp）——覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-24/GDX_evening.json