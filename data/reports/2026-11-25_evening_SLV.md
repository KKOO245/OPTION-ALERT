# 期权晚报 2026-11-25（快照 21:00 ET）

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
🟡 **事件差分**: 11-27 ATM IV 64.9% vs 11-30 54.9%（差 +10.0pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 35.24 → 收盘 37.10（+5.3%） ｜ 今日高 37.19 ｜ 低 34.49 ｜ 昨收 36.84 → 收盘 37.10（+0.7%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-12-02，窗口结束前不做对错判定）

Options: P/C成交量 0.53 | OI比 0.30 | ATM IV 64.9% | Skew 5.3pp | Term 0.89 | ExpMove ±3.7%（近端） | Rank 92%
量化视角： IV 历史高位（Rank 92%，期权偏贵）｜期限结构倒挂（Term 0.89，近月 IV 高于远月）｜保护溢价中性（Skew 5.3pp）｜存量 Call 偏重（OI比 0.30）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.53×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.30×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（2D）±3.7% ｜ 11-30（5D）±5.3% ｜ 12-02（7D）±6.5% ｜ 12-04（9D）±7.8%
   ⇒ IV–VIX Spread: +36.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -8,072,825 | GEX Change vs 上次快照 9,307,445 | Flip: Primary Flip: 37.63（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 833 / LOW 194 / INVALID 527
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 37.63（全链重定价，覆盖 99%）
Put Wall 40（弱结构｜现价低于该位 7.3%）
最近结构参考: Flip 38（现价低于该位 1.4%）
量化视角： 负 Gamma（807万，无历史分位）｜负 Gamma 缓解（+931万）｜现价位于 Flip 下方 1.40%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 40（Put Wall，弱结构） / 40（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 38（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-27  C +0 / P +0 ｜ Activity LOW ｜ 2D
11-30  C +0 / P +0 ｜ Activity LOW ｜ 5D
12-02  C +0 / P +0 ｜ Activity LOW ｜ 7D
12-04  C +0 / P +0 ｜ Activity LOW ｜ 9D

📆 11-27 Forward Structure
存量OI: C 124.1k / P 37.1k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $0.74 / P $0.63 ｜ ATM IV 64.9%，净 delta 敞口 0 shares
仓位参考: Max Pain 40 ｜ Call Wall 40（+7.8%，弱）（OI 8.5k） ｜ Put Wall 40（+7.8%）（OI 9.2k）
量化解读： 存量 Call 重｜ATM IV 64.9%｜历史 Rank 92%（近端代理）｜IV/RV 1.29×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-30（Activity LOW）仓位参考: Max Pain 39 ｜ Put Wall 39（+5.1%）（OI 4.1k）

12-02（Activity LOW）仓位参考: Max Pain 38 ｜ Call Wall 40（+7.8%，弱）（OI 1.0k） ｜ Put Wall 39（+5.1%，弱）（OI 0.7k）

12-04（Activity LOW）仓位参考: Max Pain 40 ｜ Put Wall 40（+7.8%）（OI 4.4k）

📅 事件差分（观察，非因果）: 11-27（2D）ATM IV 64.9% vs 11-30 54.9%（差 +10.0pp）——覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-25/SLV_evening.json