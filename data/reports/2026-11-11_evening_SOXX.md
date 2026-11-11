# 期权晚报 2026-11-11（快照 16:40 ET）

📊 市场环境

SPY $759.81 ｜ QQQ $690.38
VIX 17.49 ↓10.1%（5D +5.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 37.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-11

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-20 155C ΔOI +15,158（距现价 -0.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SOXX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SOXX: 今开 153.69 → 收盘 155.40（+1.1%） ｜ 今日高 158.57 ｜ 低 150.88 ｜ 昨收 146.59 → 收盘 155.40（+6.0%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-18，窗口结束前不做对错判定）

Options: P/C成交量 0.79 | OI比 2.18 | ATM IV 52.3% | Skew 5.7pp | Term 0.95 | ExpMove ±3.0%（近端） | Rank 86%
量化视角： IV 历史高位（Rank 86%，期权偏贵）｜期限结构正常（Term 0.95）｜保护溢价中性（Skew 5.7pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.79×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 2.18×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-13（2D）±3.0% ｜ 11-20（9D）±7.2% ｜ 11-27（16D）±8.2% ｜ 12-04（23D）±9.4%
   ⇒ IV–VIX Spread: +34.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 1,022,853 | GEX Change vs 上次快照 13,583,834 | Flip: Primary Flip: 155.29（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 539 / LOW 499 / INVALID 766
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 155.29（全链重定价，覆盖 96%）
Call Wall 155（弱结构｜现价高于该位 0.3%）
最近结构参考: Flip 155（现价高于该位 0.1%）
量化视角： 正 Gamma（102万，无历史分位）｜由负转正（+1358万）｜现价位于 Flip 上方 0.07%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 153（MaxPain，仅结算参考） / 155（Call Wall，弱结构）。
• Gamma 区域：切换参考 155（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +0.7k / P +3.6k ｜ Activity HIGH ｜ 2D
11-20  C +15.4k / P +1.3k ｜ Activity HIGH ｜ 9D
11-27  C +0.2k / P +0.4k ｜ Activity MEDIUM △ ｜ 16D
12-04  C +0.4k / P +0.3k ｜ Activity MEDIUM △ ｜ 23D

📆 11-13 Forward Structure
存量OI: C 110.8k / P 241.6k，今日变化ΔOI: C +0.7k / P +3.6k，平值价格ATM: C $2.30 / P $2.35 ｜ ATM IV 52.3%，净 delta 敞口 54k shares
Top ΔOI: P 140 +1,756
仓位参考: Max Pain 153 ｜ Call Wall 163.33（+5.1%）（OI 29.0k）
量化解读： 存量 Put 重｜ATM IV 52.3%｜历史 Rank 86%（近端代理）｜IV/RV 0.12×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 53,666 股

📆 11-20 Forward Structure
存量OI: C 214.9k / P 314.9k，今日变化ΔOI: C +15.4k / P +1.3k，平值价格ATM: C $5.83 / P $5.30 ｜ ATM IV 55.3%，净 delta 敞口 871k shares
Top ΔOI: C 155 +15,158 ｜ C 171 -1,000 ｜ P 135 +876
仓位参考: Max Pain 158 ｜ Call Wall 155（-0.3%，弱）（OI 16.5k） ｜ Put Wall 150（-3.5%，弱）（OI 21.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 55.3%｜历史 Rank 86%（近端代理）｜IV/RV 0.13×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 871,130 股

11-27（MEDIUM △）Top ΔOI: 153C +297 ｜ 161C -295
11-27（MEDIUM △）仓位参考: Max Pain 162 ｜ Call Wall 161.67（+4.0%）（OI 10.0k） ｜ Put Wall 163.33（+5.1%，弱）（OI 3.3k）

12-04（MEDIUM △）Top ΔOI: 160C +103
12-04（MEDIUM △）仓位参考: Max Pain 160 ｜ Call Wall 160（+3.0%）（OI 1.0k） ｜ Put Wall 148.33（-4.5%，弱）（OI 0.9k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_call_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-11/SOXX_evening.json