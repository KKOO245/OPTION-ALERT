# 期权晚报 2026-10-15（快照 16:40 ET）

📊 市场环境

SPY $771.79 ｜ QQQ $728.00
VIX 16.46 ↓2.4%（5D +6.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-15

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 1.3 ｜ 前值 0.5　✅ 今日已公布
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 0.8 ｜ 前值 1.3　✅ 今日已公布
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布　⏰ 今日

🔍 重点速览
🔴 **事件差分**: 10-16（1D）ATM IV 62.2% vs 10-19 44.4%（差 +17.8pp），覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 10-16 155C ΔOI +4,555（距现价 +4.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-19 148P ΔOI +7,866 占该期限总 OI 13.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SPCX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPCX: 今开 146.90 → 收盘 148.62（+1.2%） ｜ 今日高 149.04 ｜ 低 140.66 ｜ 昨收 152.16 → 收盘 148.62（-2.3%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-22，窗口结束前不做对错判定）

Options: P/C成交量 0.78 | OI比 0.95 | ATM IV 62.2% | Skew -0.4pp | Term 0.90 | ExpMove ±2.7%（近端） | Rank 76%
量化视角： IV 历史高位（Rank 76%，期权偏贵）｜期限结构倒挂（Term 0.90，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.4pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.78×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.95×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（1D）±2.7% ｜ 10-19（4D）±3.6% ｜ 10-21（6D）±5.0% ｜ 10-23（8D）±6.1%
   ⇒ IV–VIX Spread: +45.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -37,499,420 | GEX Change vs 上次快照 39,969,309 | Flip: Primary Flip: 151.47（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 746 / LOW 152 / INVALID 518
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 151.47（全链重定价，覆盖 95%）
最近结构参考: Flip 151（现价低于该位 1.9%）
量化视角： 负 Gamma（3750万，无历史分位）｜负 Gamma 缓解（+3997万）｜现价位于 Flip 下方 1.88%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 150（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 151（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +26.9k / P +0.4k ｜ Activity HIGH ｜ 1D
10-19  C +10.3k / P +13.5k ｜ Activity HIGH ｜ 4D
10-21  C +3.2k / P +1.6k ｜ Activity HIGH ｜ 6D
10-23  C +10.2k / P +5.5k ｜ Activity HIGH ｜ 8D

📆 10-16 Forward Structure
存量OI: C 436.3k / P 415.0k，今日变化ΔOI: C +26.9k / P +0.4k，平值价格ATM: C $1.79 / P $2.16 ｜ ATM IV 62.2%，净 delta 敞口 275k shares
Top ΔOI: C 162 +13,228 ｜ C 155 +4,555
仓位参考: Max Pain 150 ｜ Call Wall 160（+7.7%，弱）（OI 27.6k） ｜ Put Wall 135（-9.2%，弱）（OI 30.3k）
量化解读： 存量两侧均衡｜ATM IV 62.2%｜历史 Rank 76%（近端代理）｜IV/RV 1.22×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 275,123 股

📆 10-19 Forward Structure
存量OI: C 36.6k / P 22.7k，今日变化ΔOI: C +10.3k / P +13.5k，平值价格ATM: C $2.60 / P $2.78 ｜ ATM IV 44.4%，净 delta 敞口 -486k shares
Top ΔOI: P 148 +7,866 ｜ P 155 +2,410 ｜ C 157 +2,035
仓位参考: Max Pain 158 ｜ Call Wall 157.5（+6.0%，弱）（OI 4.7k） ｜ Put Wall 148（-0.4%）（OI 8.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 44.4%｜历史 Rank 76%（近端代理）｜IV/RV 0.87×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 485,923 股

📆 10-21 Forward Structure
存量OI: C 13.4k / P 7.1k，今日变化ΔOI: C +3.2k / P +1.6k，平值价格ATM: C $3.65 / P $3.80 ｜ ATM IV 49.5%，净 delta 敞口 -26k shares
Top ΔOI: C 160 +414 ｜ P 155 +328
仓位参考: Max Pain 158 ｜ Call Wall 162.5（+9.3%，弱）（OI 2.0k） ｜ Put Wall 147（-1.1%，弱）（OI 1.4k）
量化解读： 存量 Call 重｜ATM IV 49.5%｜历史 Rank 76%（近端代理）｜IV/RV 0.97×（近似）｜净 delta 敞口 负 26,369 股

📆 10-23 Forward Structure
存量OI: C 66.9k / P 71.2k，今日变化ΔOI: C +10.2k / P +5.5k，平值价格ATM: C $4.40 / P $4.68 ｜ ATM IV 51.3%，净 delta 敞口 69k shares
Top ΔOI: C 155 +3,409 ｜ C 165 +2,264 ｜ C 160 +1,209
仓位参考: Max Pain 155 ｜ Call Wall 155（+4.3%，弱）（OI 6.6k） ｜ Put Wall 140（-5.8%，弱）（OI 6.7k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 51.3%｜历史 Rank 76%（近端代理）｜IV/RV 1.01×（近似）｜净 delta 敞口 正 68,917 股

📅 事件差分（观察，非因果）: 10-16（1D）ATM IV 62.2% vs 10-19 44.4%（差 +17.8pp）——覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-15/SPCX_evening.json