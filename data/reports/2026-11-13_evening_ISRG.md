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

🔍 重点速览
🟡 **近现价集中开仓**: 12-04 430P ΔOI +3（距现价 -3.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 443.69 → 收盘 443.59（-0.0%） ｜ 今日高 448.77 ｜ 低 441.00 ｜ 昨收 439.89 → 收盘 443.59（+0.8%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-20，窗口结束前不做对错判定）

Options: P/C成交量 0.34 | OI比 0.78 | ATM IV 145.6% | Skew -30.4pp | Term 0.22 | ExpMove ±3.7%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.22，近月 IV 高于远月）｜Put 保护异常便宜（Skew -30.4pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.78）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.34×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.78×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（7D）±3.7% ｜ 11-27（14D）±5.8% ｜ 12-04（21D）±7.0% ｜ 12-11（28D）±7.0%
   ⇒ IV–VIX Spread: +126.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,784,564 | GEX Change N/A | Flip: Primary Flip: 419.33（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 87%（带内） ｜ IV 有效性: VALID 250 / LOW 197 / INVALID 563
结构观察区: Primary Flip 419.33（全链重定价，覆盖 87%）
Call Wall 480（弱结构｜现价低于该位 7.6%）
最近结构参考: Flip 419（现价高于该位 5.8%）
量化视角： 正 Gamma（278万，无历史分位）｜现价位于 Flip 上方 5.79%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 435（MaxPain，仅结算参考）；上方 480（Call Wall，弱结构）。
• Gamma 区域：切换参考 419（全链重定价，覆盖 87%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C +11 / P -11 ｜ Activity LOW ｜ 7D
11-27  C +23 / P +3 ｜ Activity MEDIUM △ ｜ 14D
12-04  C +6 / P +4 ｜ Activity LOW ｜ 21D
12-11  C +2 / P +7 ｜ Activity LOW ｜ 28D

📆 11-20 Forward Structure
存量OI: C 10.4k / P 10.4k，今日变化ΔOI: C +11 / P -11，平值价格ATM: C $10.31 / P $6.20 ｜ ATM IV 31.2%，净 delta 敞口 3k shares
Top ΔOI: C 460 +26 ｜ C 480 -26 ｜ P 460 -17
仓位参考: Max Pain 410 ｜ Call Wall 420（-5.3%，弱）（OI 0.8k） ｜ Put Wall 410（-7.6%，弱）（OI 0.5k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 31.2%｜历史 Rank 100%（近端代理）｜IV/RV 0.69×（近似）｜净 delta 敞口 正 2,949 股

11-27（MEDIUM △）Top ΔOI: 475C +9 ｜ 450C +6
11-27（MEDIUM △）仓位参考: Max Pain 430 ｜ Call Wall 430（-3.1%，弱）（OI 64） ｜ Put Wall 410（-7.6%，弱）（OI 42）

12-04（Activity LOW）仓位参考: Max Pain 450 ｜ Call Wall 475（+7.1%，弱）（OI 82） ｜ Put Wall 405（-8.7%，弱）（OI 25）

12-11（Activity LOW）仓位参考: Max Pain 440 ｜ Call Wall 450（+1.4%）（OI 0.1k） ｜ Put Wall 435（-1.9%）（OI 22）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-13/ISRG_evening.json