# 期权晚报 2026-11-12（快照 16:40 ET）

📊 市场环境

SPY $757.12 ｜ QQQ $688.17
VIX 18.70 ↑6.9%（5D -33.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 39.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-12

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 3.75 ｜ 前值 3.97　✅ 今日已公布
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🔴 **事件差分**: 11-13（1D）ATM IV 77.8% vs 11-20 59.5%（差 +18.3pp），覆盖 成屋销售、PPI 生产者物价 MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-13 160C ΔOI +4,665（距现价 +3.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SOXX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SOXX: 今开 150.26 → 收盘 154.99（+3.1%） ｜ 今日高 157.63 ｜ 低 150.04 ｜ 昨收 155.40 → 收盘 154.99（-0.3%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-19，窗口结束前不做对错判定）

Options: P/C成交量 3.67 | OI比 2.11 | ATM IV 77.8% | Skew 19.2pp | Term 0.66 | ExpMove ±2.8%（近端） | Rank 98%
量化视角： IV 历史高位（Rank 98%，期权偏贵）｜期限结构倒挂（Term 0.66，近月 IV 高于远月）｜保护溢价显著（Skew 19.2pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 3.67）——观察点，非方向信号
   ⇒ Put/Call Volume: 3.67×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 2.11×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-13（1D）±2.8% ｜ 11-20（8D）±7.3% ｜ 11-27（15D）±8.6% ｜ 12-04（22D）±9.9%
   ⇒ IV–VIX Spread: +59.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) -211,310 | GEX Change vs 上次快照 17,920,975 | Flip: Primary Flip: 155.01（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 581 / LOW 482 / INVALID 741
结构观察区: Primary Flip 155.01（全链重定价，覆盖 96%）
Call Wall 155（弱结构｜现价低于该位 0.0%）
最近结构参考: Call Wall 155（现价低于该位 0.0%）
量化视角： 负 Gamma（21万，无历史分位）｜负 Gamma 缓解（+1792万）｜现价位于 Flip 下方 0.01%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 153（MaxPain，仅结算参考）；上方 155（Call Wall，弱结构）。
• Gamma 区域：切换参考 155（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +6.0k / P +5.0k ｜ Activity HIGH ｜ 1D
11-20  C -7.7k / P -63.1k ｜ Activity HIGH ｜ 8D
11-27  C +3.0k / P +0.8k ｜ Activity HIGH ｜ 15D
12-04  C +3.6k / P +1.1k ｜ Activity HIGH ｜ 22D

📆 11-13 Forward Structure
存量OI: C 116.8k / P 246.6k，今日变化ΔOI: C +6.0k / P +5.0k，平值价格ATM: C $2.20 / P $2.15 ｜ ATM IV 77.8%，净 delta 敞口 -164k shares
Top ΔOI: C 160 +4,665 ｜ C 163 +1,702 ｜ P 150 +1,498
仓位参考: Max Pain 153 ｜ Call Wall 163.33（+5.4%）（OI 30.7k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 77.8%｜历史 Rank 98%（近端代理）｜IV/RV 0.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 163,698 股

📆 11-20 Forward Structure
存量OI: C 207.2k / P 251.8k，今日变化ΔOI: C -7.7k / P -63.1k，平值价格ATM: C $5.40 / P $5.85 ｜ ATM IV 59.5%，净 delta 敞口 343k shares
Top ΔOI: P 120 -17,615 ｜ P 105 -17,139 ｜ P 130 -8,867
仓位参考: Max Pain 158 ｜ Call Wall 155（+0.0%，弱）（OI 17.8k） ｜ Put Wall 150（-3.2%，弱）（OI 18.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 59.5%｜历史 Rank 98%（近端代理）｜IV/RV 0.13×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 343,187 股

📆 11-27 Forward Structure
存量OI: C 30.1k / P 25.3k，今日变化ΔOI: C +3.0k / P +0.8k，平值价格ATM: C $6.85 / P $6.50 ｜ ATM IV 53.4%，净 delta 敞口 87k shares
Top ΔOI: C 161 +1,009 ｜ C 162 +537 ｜ C 155 +428
仓位参考: Max Pain 162 ｜ Call Wall 161.67（+4.3%）（OI 11.1k） ｜ Put Wall 150（-3.2%，弱）（OI 3.3k）
量化解读： 存量 Call 重｜ATM IV 53.4%｜历史 Rank 98%（近端代理）｜IV/RV 0.12×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 87,230 股

📆 12-04 Forward Structure
存量OI: C 9.9k / P 9.3k，今日变化ΔOI: C +3.6k / P +1.1k，平值价格ATM: C $7.69 / P $7.61 ｜ ATM IV 50.9%，净 delta 敞口 53k shares
Top ΔOI: C 172 +1,450 ｜ C 165 +1,409 ｜ C 173 +513
仓位参考: Max Pain 160 ｜ Call Wall 165（+6.5%，弱）（OI 1.6k） ｜ Put Wall 150（-3.2%，弱）（OI 1.3k）
量化解读： 存量两侧均衡｜ATM IV 50.9%｜历史 Rank 98%（近端代理）｜IV/RV 0.12×（近似）｜净 delta 敞口 正 52,674 股

📅 事件差分（观察，非因果）: 11-13（1D）ATM IV 77.8% vs 11-20 59.5%（差 +18.3pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-12/SOXX_evening.json