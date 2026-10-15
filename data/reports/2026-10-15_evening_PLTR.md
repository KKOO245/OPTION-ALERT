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
🟡 **近现价集中开仓**: 10-16 205P ΔOI -2,793（距现价 +2.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 196.58 → 收盘 200.50（+2.0%） ｜ 今日高 200.91 ｜ 低 192.60 ｜ 昨收 200.97 → 收盘 200.50（-0.2%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-22，窗口结束前不做对错判定）

Options: P/C成交量 0.66 | OI比 1.15 | ATM IV 54.9% | Skew 0.5pp | Term 1.12 | ExpMove ±2.3%（近端） | Rank 83%
量化视角： IV 历史高位（Rank 83%，期权偏贵）｜期限结构正常（Term 1.12）｜保护溢价薄（Skew 0.5pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.66×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.15×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（1D）±2.3% ｜ 10-23（8D）±5.3% ｜ 10-30（15D）±7.5% ｜ 11-06（22D）±12.9%
   ⇒ IV–VIX Spread: +38.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 39,328,438 | GEX Change vs 上次快照 30,662,865 | Flip: Primary Flip: 194.99（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 613 / LOW 71 / INVALID 228
结构观察区: Primary Flip 194.99（全链重定价，覆盖 98%）
Call Wall 220（弱结构｜现价低于该位 8.9%）
最近结构参考: Flip 195（现价高于该位 2.8%）
量化视角： 正 Gamma（3933万，无历史分位）｜正 Gamma 增强（+3066万）｜现价位于 Flip 上方 2.83%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 185（MaxPain，仅结算参考）；上方 220（Call Wall，弱结构）。
• Gamma 区域：切换参考 195（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C -1.7k / P -6.9k ｜ Activity MEDIUM △ ｜ 1D
10-23  C +4.2k / P +4.3k ｜ Activity HIGH ｜ 8D
10-30  C +1.7k / P +1.3k ｜ Activity MEDIUM △ ｜ 15D
11-06  C +1.0k / P +1.1k ｜ Activity HIGH ｜ 22D

📆 10-16 Forward Structure
存量OI: C 230.4k / P 263.8k，今日变化ΔOI: C -1.7k / P -6.9k，平值价格ATM: C $2.62 / P $2.05 ｜ ATM IV 54.9%，净 delta 敞口 179k shares
Top ΔOI: C 215 +2,821 ｜ P 205 -2,793
仓位参考: Max Pain 185 ｜ Call Wall 220（+9.7%，弱）（OI 17.2k） ｜ Put Wall 190（-5.2%，弱）（OI 10.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 54.9%｜历史 Rank 83%（近端代理）｜IV/RV 1.87×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 178,515 股

📆 10-23 Forward Structure
存量OI: C 46.9k / P 62.2k，今日变化ΔOI: C +4.2k / P +4.3k，平值价格ATM: C $5.70 / P $5.03 ｜ ATM IV 45.4%，净 delta 敞口 -109k shares
Top ΔOI: P 205 +2,098 ｜ P 197 +1,054
仓位参考: Max Pain 195 ｜ Call Wall 220（+9.7%，弱）（OI 4.4k） ｜ Put Wall 205（+2.2%，弱）（OI 3.4k）
量化解读： 存量 Put 重｜ATM IV 45.4%｜历史 Rank 83%（近端代理）｜IV/RV 1.54×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 108,654 股

10-30（MEDIUM △）Top ΔOI: 202P -1,930 ｜ 200P +1,285
10-30（MEDIUM △）仓位参考: Max Pain 192 ｜ Call Wall 205（+2.2%，弱）（OI 3.4k） ｜ Put Wall 190（-5.2%）（OI 4.4k）

📆 11-06 Forward Structure
存量OI: C 18.0k / P 17.3k，今日变化ΔOI: C +1.0k / P +1.1k，平值价格ATM: C $13.49 / P $12.40 ｜ ATM IV 65.9%，净 delta 敞口 34k shares
Top ΔOI: C 205 +535 ｜ P 172 +310 ｜ P 185 +263
仓位参考: Max Pain 192 ｜ Call Wall 215（+7.2%，弱）（OI 1.4k） ｜ Put Wall 190（-5.2%）（OI 3.0k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 65.9%｜历史 Rank 83%（近端代理）｜IV/RV 2.24×（近似）｜净 delta 敞口 正 33,853 股

📅 事件差分（观察，非因果）: 10-16（1D）ATM IV 54.9% vs 10-23 45.4%（差 +9.6pp）——覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-15/PLTR_evening.json