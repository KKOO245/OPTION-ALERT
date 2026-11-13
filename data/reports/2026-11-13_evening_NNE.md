# 期权晚报 2026-11-13（快照 16:40 ET）

📊 市场环境

SPY $754.37 ｜ QQQ $679.89
VIX 19.30 ↑3.2%（5D -24.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-13

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 0.3 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 11.10 → 收盘 11.11（+0.1%） ｜ 今日高 11.25 ｜ 低 10.77 ｜ 昨收 11.09 → 收盘 11.11（+0.2%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-20，窗口结束前不做对错判定）

Options: P/C成交量 0.30 | OI比 0.35 | ATM IV 160.1% | Skew -98.0pp | Term 0.52 | ExpMove ±9.7%（近端） | Rank 92%
量化视角： IV 历史高位（Rank 92%，期权偏贵）｜期限结构倒挂（Term 0.52，近月 IV 高于远月）｜Put 保护异常便宜（Skew -98.0pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.35）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.30×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.35×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（7D）±9.7% ｜ 11-27（14D）±11.8% ｜ 12-04（21D）±5.0% ｜ 12-11（28D）±15.8%
   ⇒ IV–VIX Spread: +140.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,360,270 | GEX Change vs 上次快照 311,374 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 155 / LOW 68 / INVALID 163
结构观察区: NO_CROSS
Put Wall 11（现价高于该位 1.0%）
最近结构参考: Put Wall 11（现价高于该位 1.0%）
量化视角： 正 Gamma（136万，无历史分位）｜正 Gamma 增强（+31万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 11（Put Wall）；上方 12（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C +62 / P -35 ｜ Activity MEDIUM △ ｜ 7D
11-27  C +8 / P +78 ｜ Activity MEDIUM △ ｜ 14D
12-04  C -1 / P +24 ｜ Activity MEDIUM △ ｜ 21D
12-11  C -12 / P +2 ｜ Activity MEDIUM △ ｜ 28D

📆 11-20 Forward Structure
存量OI: C 6.3k / P 2.0k，今日变化ΔOI: C +62 / P -35，平值价格ATM: C $0.55 / P $0.53 ｜ ATM IV 83.0%，净 delta 敞口 5k shares
Top ΔOI: C 12 +23
仓位参考: Max Pain 12 ｜ Call Wall 12（+8.0%，弱）（OI 0.7k） ｜ Put Wall 11（-1.0%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 83.0%｜历史 Rank 92%（近端代理）｜IV/RV 0.84×（近似）｜净 delta 敞口 正 5,339 股

11-27（MEDIUM △）Top ΔOI: 10P +75 ｜ 11P +2
11-27（MEDIUM △）仓位参考: Max Pain 12 ｜ Put Wall 10（-10.0%，弱）（OI 94）

12-04（MEDIUM △）Top ΔOI: 12P +20 ｜ 11P +2
12-04（MEDIUM △）仓位参考: Max Pain 13

12-11（MEDIUM △）Top ΔOI: 12C -12 ｜ 11C -1
12-11（MEDIUM △）仓位参考: Max Pain 12 ｜ Call Wall 10（-10.0%，弱）（OI 33） ｜ Put Wall 12（+8.0%）（OI 23）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location near_put_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-13/NNE_evening.json