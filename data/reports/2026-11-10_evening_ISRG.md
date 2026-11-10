# 期权晚报 2026-11-10（快照 16:40 ET）

📊 市场环境

SPY $749.92 ｜ QQQ $674.76
VIX 19.46 ↓2.3%（5D -6.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-10

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-10 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周二 11-10 08:30　【高】Inflation Rate MoM　预测 0.3 ｜ 实际 0.4 ｜ 前值 0.6　✅ 今日已公布
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-20 447P ΔOI +23（距现价 -0.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 458.00 → 收盘 450.04（-1.7%） ｜ 今日高 458.80 ｜ 低 444.16 ｜ 昨收 460.56 → 收盘 450.04（-2.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.70 | OI比 0.96 | ATM IV 38.6% | Skew 7.1pp | Term 0.86 | ExpMove ±3.1%（近端） | Rank 41%
量化视角： IV 中性（Rank 41%）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜保护溢价显著（Skew 7.1pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.70×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.96×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-13（3D）±3.1% ｜ 11-20（10D）±3.8% ｜ 11-27（17D）±7.4% ｜ 12-04（24D）±7.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 3,339,203 | GEX Change vs 上次快照 113,435 | Flip: Primary Flip: 415.34（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 326 / LOW 209 / INVALID 469
结构观察区: Primary Flip 415.34（全链重定价，覆盖 92%）
Call Wall 480（弱结构｜现价低于该位 6.2%）
最近结构参考: Call Wall 480（现价低于该位 6.2%）
量化视角： 正 Gamma（334万，无历史分位）｜正 Gamma 增强（+11万）｜现价位于 Flip 上方 8.35%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 440（MaxPain，仅结算参考）；上方 480（Call Wall，弱结构）。
• Gamma 区域：切换参考 415（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +0.3k / P +56 ｜ Activity MEDIUM △ ｜ 3D
11-20  C +1 / P +52 ｜ Activity MEDIUM △ ｜ 10D
11-27  C +6 / P +12 ｜ Activity LOW ｜ 17D
12-04  C -8 / P +28 ｜ Activity MEDIUM △ ｜ 24D

📆 11-13 Forward Structure
存量OI: C 1.5k / P 1.5k，今日变化ΔOI: C +0.3k / P +56，平值价格ATM: C $6.00 / P $8.15 ｜ ATM IV 38.6%，净 delta 敞口 2k shares
Top ΔOI: C 480 +135 ｜ C 467 +68 ｜ C 470 +17
仓位参考: Max Pain 440 ｜ Call Wall 480（+6.7%，弱）（OI 0.2k） ｜ Put Wall 462.5（+2.8%，弱）（OI 0.1k）
量化解读： 存量两侧均衡｜ATM IV 38.6%｜历史 Rank 41%（近端代理）｜IV/RV 0.88×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,693 股

11-20（MEDIUM △）Top ΔOI: 450C -24 ｜ 410P +23
11-20（MEDIUM △）仓位参考: Max Pain 410 ｜ Call Wall 420（-6.7%，弱）（OI 0.8k） ｜ Put Wall 410（-8.9%，弱）（OI 0.5k）

11-27（Activity LOW）仓位参考: Max Pain 430 ｜ Call Wall 430（-4.5%，弱）（OI 64） ｜ Put Wall 410（-8.9%，弱）（OI 42）

12-04（MEDIUM △）Top ΔOI: 405P +14 ｜ 460P +10
12-04（MEDIUM △）仓位参考: Max Pain 450 ｜ Call Wall 475（+5.5%，弱）（OI 82） ｜ Put Wall 410（-8.9%，弱）（OI 20）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-10/ISRG_evening.json