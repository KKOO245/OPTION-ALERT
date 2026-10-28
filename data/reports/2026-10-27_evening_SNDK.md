# 期权晚报 2026-10-27（快照 21:00 ET）

📊 市场环境

SPY $769.66 ｜ QQQ $nan
VIX 17.52 ↓4.7%（5D +1.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-27

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-27 08:30　【高】耐用品订单 Orders MoM　预测 1.5 ｜ 实际 1.8 ｜ 前值 0.1　✅ 今日已公布
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 4
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.9
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2

🔍 重点速览
🔴 **事件差分**: 10-30（3D）ATM IV 128.3% vs 11-06 91.4%（差 +36.8pp），覆盖 耐用品订单 Orders MoM、美联储议息会议 Statement 等
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 1,267.08 → 收盘 1,304.84（+3.0%） ｜ 今日高 1315.98 ｜ 低 1259.00 ｜ 昨收 1,255.58 → 收盘 1,304.84（+3.9%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-03，窗口结束前不做对错判定）

Options: P/C成交量 0.54 | OI比 0.78 | ATM IV 128.3% | Skew -1.7pp | Term 0.57 | ExpMove ±9.3%（近端） | Rank 86%
量化视角： IV 历史高位（Rank 86%，期权偏贵）｜期限结构倒挂（Term 0.57，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.7pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.78）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.54×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.78×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（3D）±9.3% ｜ 11-06（10D）±12.2% ｜ 11-13（17D）±14.2% ｜ 11-20（24D）±17.1%
   ⇒ IV–VIX Spread: +110.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -835,414 | GEX Change vs 上次快照 194,207 | Flip: Primary Flip: 1324.48（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1841 / LOW 426 / INVALID 1127
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 1324.48（全链重定价，覆盖 100%）
最近结构参考: Flip 1324（现价低于该位 1.5%）
量化视角： 负 Gamma（84万，无历史分位）｜负 Gamma 缓解（+19万）｜现价位于 Flip 下方 1.48%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 1,370（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1324（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-30  C +0 / P +0 ｜ Activity LOW ｜ 3D
11-06  C +0 / P +0 ｜ Activity LOW ｜ 10D
11-13  C +0 / P +0 ｜ Activity LOW ｜ 17D
11-20  C +0 / P +0 ｜ Activity LOW ｜ 24D

📆 10-30 Forward Structure
存量OI: C 44.7k / P 34.7k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $61.20 / P $60.15 ｜ ATM IV 128.3%，净 delta 敞口 0 shares
仓位参考: Max Pain 1,370 ｜ Call Wall 1400（+7.3%，弱）（OI 1.6k） ｜ Put Wall 1200（-8.0%，弱）（OI 1.2k）
量化解读： 存量 Call 重｜ATM IV 128.3%｜历史 Rank 86%（近端代理）｜IV/RV 2.33×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-06（Activity LOW）仓位参考: Max Pain 1,400 ｜ Call Wall 1400（+7.3%，弱）（OI 0.8k） ｜ Put Wall 1200（-8.0%，弱）（OI 0.8k）

11-13（Activity LOW）仓位参考: Max Pain 1,495 ｜ Call Wall 1420（+8.8%，弱）（OI 0.2k） ｜ Put Wall 1300（-0.4%，弱）（OI 0.2k）

11-20（Activity LOW）仓位参考: Max Pain 1,490 ｜ Call Wall 1400（+7.3%，弱）（OI 1.7k） ｜ Put Wall 1200（-8.0%，弱）（OI 1.5k）

📅 事件差分（观察，非因果）: 10-30（3D）ATM IV 128.3% vs 11-06 91.4%（差 +36.8pp）——覆盖 耐用品订单 Orders MoM、美联储议息会议 Statement 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-27/SNDK_evening.json