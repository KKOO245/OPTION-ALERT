# 期权晚报 2026-11-09（快照 16:40 ET）

📊 市场环境

SPY $752.69 ｜ QQQ $679.35
VIX 19.92 ↓22.3%（5D -5.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-09

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-10 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周二 11-10 08:30　【高】Core Inflation Rate YoY　预测 2.8 ｜ 实际 待公布 ｜ 前值 2.6
- 周二 11-10 08:30　【高】Inflation Rate MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.6
- 周二 11-10 08:30　【高】Inflation Rate YoY　预测 3.9 ｜ 实际 待公布 ｜ 前值 3.7
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-20 153C ΔOI +626（距现价 -2.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-13 147P ΔOI +1,730 占该期限总 OI 15.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## XBI

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
XBI: 今开 153.21 → 收盘 156.90（+2.4%） ｜ 今日高 157.92 ｜ 低 151.00 ｜ 昨收 152.21 → 收盘 156.90（+3.1%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-16，窗口结束前不做对错判定）

Options: P/C成交量 0.99 | OI比 1.27 | ATM IV 40.6% | Skew 1.7pp | Term 0.83 | ExpMove ±3.6%（近端） | Rank 85%
量化视角： IV 历史高位（Rank 85%，期权偏贵）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜保护溢价薄（Skew 1.7pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.99×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.27×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-13（4D）±3.6% ｜ 11-20（11D）±5.1% ｜ 11-27（18D）±7.3% ｜ 12-04（25D）±3.7%
   ⇒ IV–VIX Spread: +20.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 14,812,196 | GEX Change vs 上次快照 6,678,525 | Flip: Primary Flip: 151.91（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 466 / LOW 140 / INVALID 316
结构观察区: Primary Flip 151.91（全链重定价，覆盖 99%）
最近结构参考: Flip 152（现价高于该位 3.3%）
量化视角： 正 Gamma（1481万，无历史分位）｜正 Gamma 增强（+668万）｜现价位于 Flip 上方 3.28%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 148（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 152（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 140.0P — Vol 38 | 最新价 $0.26 | OI 1192→9661 (ΔOI +8469张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8469张（+710.5% vs前日OI），连续性待观察（方向未知）
11-13 147.0P — Vol 323 | 最新价 $0.26 | OI 68→1798 (ΔOI +1730张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1730张（+2544.1% vs前日OI），连续性待观察（方向未知）
11-13 142.0C — Vol 500 | 最新价 $15.24 | OI 0→1000 (ΔOI +1000张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增1000张（前日OI缺失），值得跟踪（方向未知）
11-20 153.0C — Vol 5 | 最新价 $6.18 | OI 332→958 (ΔOI +626张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增626张（+188.6% vs前日OI），连续性待观察（方向未知）
11-20 163.0C — Vol 7 | 最新价 $1.80 | OI 252→738 (ΔOI +486张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增486张（+192.9% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 12,311 张（Put 10,199 / Call 2,112），跨 2 个期限｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +1.9k / P +1.6k ｜ Activity HIGH ｜ 4D
11-20  C +0.8k / P +7.6k ｜ Activity HIGH ｜ 11D
11-27  C +21 / P +78 ｜ Activity MEDIUM △ ｜ 18D
12-04  C +8 / P -3 ｜ Activity MEDIUM △ ｜ 25D

📆 11-13 Forward Structure
存量OI: C 5.0k / P 6.4k，今日变化ΔOI: C +1.9k / P +1.6k，平值价格ATM: C $2.73 / P $2.99 ｜ ATM IV 40.6%，净 delta 敞口 129k shares
Top ΔOI: P 147 +1,730 ｜ C 142 +1,000 ｜ P 142 -654
仓位参考: Max Pain 148 ｜ Call Wall 160（+2.0%，弱）（OI 0.8k） ｜ Put Wall 147（-6.3%，弱）（OI 1.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 40.6%｜历史 Rank 85%（近端代理）｜IV/RV 1.02×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 128,634 股

📆 11-20 Forward Structure
存量OI: C 23.5k / P 52.6k，今日变化ΔOI: C +0.8k / P +7.6k，平值价格ATM: C $3.98 / P $3.96 ｜ ATM IV 36.1%，净 delta 敞口 9k shares
Top ΔOI: P 140 +8,469 ｜ P 145 -1,020 ｜ C 153 +626
仓位参考: Max Pain 153 ｜ Call Wall 165（+5.2%）（OI 5.6k） ｜ Put Wall 147（-6.3%，弱）（OI 5.7k）
量化解读： 存量 Put 重｜ATM IV 36.1%｜历史 Rank 85%（近端代理）｜IV/RV 0.90×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 9,371 股

11-27（MEDIUM △）Top ΔOI: 148P +72 ｜ 156C +23
11-27（MEDIUM △）仓位参考: Max Pain 158 ｜ Call Wall 152.5（-2.8%，弱）（OI 0.1k） ｜ Put Wall 156（-0.6%）（OI 0.2k）

12-04（MEDIUM △）Top ΔOI: 152C +3 ｜ 167P -3
12-04（MEDIUM △）仓位参考: Max Pain 161 ｜ Call Wall 162（+3.3%，弱）（OI 44） ｜ Put Wall 147（-6.3%，弱）（OI 45）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-09/XBI_evening.json