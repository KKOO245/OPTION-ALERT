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
🔴 **事件差分**: 10-30（3D）ATM IV 114.6% vs 11-06 82.3%（差 +32.4pp），覆盖 耐用品订单 Orders MoM、美联储议息会议 Statement 等
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 160.33 → 收盘 161.09（+0.5%） ｜ 今日高 161.87 ｜ 低 157.75 ｜ 昨收 159.60 → 收盘 161.09（+0.9%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-03，窗口结束前不做对错判定）

Options: P/C成交量 0.50 | OI比 0.50 | ATM IV 114.6% | Skew -1.5pp | Term 0.59 | ExpMove ±8.3%（近端） | Rank 92%
量化视角： IV 历史高位（Rank 92%，期权偏贵）｜期限结构倒挂（Term 0.59，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.5pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.50）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.50×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.50×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（3D）±8.3% ｜ 11-06（10D）±11.2% ｜ 11-13（17D）±13.0% ｜ 11-20（24D）±14.7%
   ⇒ IV–VIX Spread: +97.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 9,453,681 | GEX Change vs 上次快照 1,345,545 | Flip: Primary Flip: 153.60（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 452 / LOW 120 / INVALID 318
结构观察区: Primary Flip 153.60（全链重定价，覆盖 100%）
Call Wall 170（弱结构｜现价低于该位 5.2%）
最近结构参考: Flip 154（现价高于该位 4.9%）
量化视角： 正 Gamma（945万，无历史分位）｜正 Gamma 增强（+135万）｜现价位于 Flip 上方 4.88%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 170（MaxPain，仅结算参考） / 170（Call Wall，弱结构）。
• Gamma 区域：切换参考 154（全链重定价，覆盖 100%）。
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
存量OI: C 70.6k / P 35.1k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $7.25 / P $6.10 ｜ ATM IV 114.6%，净 delta 敞口 0 shares
仓位参考: Max Pain 170 ｜ Call Wall 172.5（+7.1%，弱）（OI 11.9k） ｜ Put Wall 150（-6.9%，弱）（OI 2.2k）
量化解读： 存量 Call 重｜ATM IV 114.6%｜历史 Rank 92%（近端代理）｜IV/RV 2.20×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-06（Activity LOW）仓位参考: Max Pain 170 ｜ Call Wall 175（+8.6%，弱）（OI 0.5k）

11-13（Activity LOW）仓位参考: Max Pain 175 ｜ Call Wall 170（+5.5%，弱）（OI 0.3k） ｜ Put Wall 155（-3.8%，弱）（OI 1.0k）

11-20（Activity LOW）仓位参考: Max Pain 170 ｜ Call Wall 170（+5.5%）（OI 13.6k） ｜ Put Wall 150（-6.9%，弱）（OI 3.2k）

📅 事件差分（观察，非因果）: 10-30（3D）ATM IV 114.6% vs 11-06 82.3%（差 +32.4pp）——覆盖 耐用品订单 Orders MoM、美联储议息会议 Statement 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-27/COIN_evening.json