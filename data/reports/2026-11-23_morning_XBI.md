# 期权晨报 2026-11-23（快照 10:20 ET）

📊 市场环境

SPY $723.14 ｜ QQQ $655.57
VIX 27.37 ↓23.7%（5D +19.5%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 19.0（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-23

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-25 08:30　【高】Personal Spending MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.5
- 周三 11-25 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 11-25 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 11-25 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 3.4 ｜ 实际 待公布 ｜ 前值 1.5
- 周三 11-25 08:30　【高】耐用品订单 Orders MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.8

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 12-18 140P ΔOI +3,126（距现价 -3.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-27 130C ΔOI +1,600 占该期限总 OI 13.1%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 140.18 → 今开 145.57（+3.8%） | 较昨收变动（含盘初走势） ｜ 今日高 146.84 ｜ 低 144.61

Options: P/C成交量 0.27 | OI比 1.17 | ATM IV 45.0% | Skew 12.1pp | Term 0.84 | ExpMove ±3.6%（近端） | Rank 91%
量化视角： IV 历史高位（Rank 91%，期权偏贵）｜期限结构倒挂（Term 0.84，近月 IV 高于远月）｜保护溢价显著（Skew 12.1pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.27×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.17×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-27（4D）±3.6% ｜ 12-04（11D）±6.3% ｜ 12-11（18D）±7.5% ｜ 12-18（25D）±8.3%
   ⇒ IV–VIX Spread: +17.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) -1,627,152 | GEX Change vs 上次快照 -1,307,389 | Flip: Primary Flip: 146.47（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 348 / LOW 160 / INVALID 404
结构观察区: Primary Flip 146.47（全链重定价，覆盖 95%）
最近结构参考: Flip 146（现价低于该位 0.7%）
量化视角： 负 Gamma（163万，无历史分位）｜负 Gamma 加深（131万）｜现价位于 Flip 下方 0.67%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 145（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 146（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 140.0P — Vol 3,354 | 最新价 $6.32 | OI 1063→4189 (ΔOI +3126张) | ΔOI/Volume 93.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3126张（+294.1% vs前日OI），连续性待观察（方向未知）
12-04 136.0P — Vol 2,003 | 最新价 $2.76 | OI 2→2005 (ΔOI +2003张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2003张（+100150.0% vs前日OI），连续性待观察（方向未知）
12-04 126.0P — Vol 2,000 | 最新价 $0.75 | OI 0→2000 (ΔOI +2000张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2000张（前日OI缺失），连续性待观察（方向未知）
12-04 128.0P — Vol 2,000 | 最新价 $0.29 | OI 0→2000 (ΔOI +2000张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2000张（前日OI缺失），连续性待观察（方向未知）
12-04 138.0P — Vol 2,002 | 最新价 $2.77 | OI 24→2023 (ΔOI +1999张) | ΔOI/Volume 99.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1999张（+8329.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 11,128 张（Put 11,128 / Call 0），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $3M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-27  C +2.4k / P +1.1k ｜ Activity HIGH ｜ 4D
12-04  C +0.3k / P +10.4k ｜ Activity HIGH ｜ 11D
12-11  C +0.4k / P +56 ｜ Activity MEDIUM △ ｜ 18D
12-18  C +1.3k / P +6.4k ｜ Activity MEDIUM △ ｜ 25D

📆 11-27 Forward Structure
存量OI: C 5.6k / P 6.6k，今日变化ΔOI: C +2.4k / P +1.1k，平值价格ATM: C $2.84 / P $2.36 ｜ ATM IV 45.0%，净 delta 敞口 213k shares
Top ΔOI: C 130 +1,600 ｜ P 135 +765
仓位参考: Max Pain 145 ｜ Call Wall 146（+0.4%，弱）（OI 0.5k） ｜ Put Wall 146（+0.4%，弱）（OI 0.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 45.0%｜历史 Rank 91%（近端代理）｜IV/RV 1.15×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 213,043 股

📆 12-04 Forward Structure
存量OI: C 0.9k / P 13.9k，今日变化ΔOI: C +0.3k / P +10.4k，平值价格ATM: C $3.20 / P $5.92 ｜ ATM IV 38.5%，净 delta 敞口 -147k shares
Top ΔOI: P 136 +2,003 ｜ P 126 +2,000 ｜ P 128 +2,000
仓位参考: Max Pain 154 ｜ Call Wall 154（+5.8%，弱）（OI 0.2k） ｜ Put Wall 141（-3.1%，弱）（OI 2.2k）
量化解读： 存量 Put 重｜ATM IV 38.5%｜历史 Rank 91%（近端代理）｜IV/RV 0.99×（近似）｜净 delta 敞口 负 147,162 股

12-11（MEDIUM △）Top ΔOI: 147C +351 ｜ 135P +58
12-11（MEDIUM △）仓位参考: Max Pain 147 ｜ Call Wall 147（+1.0%）（OI 0.8k） ｜ Put Wall 143（-1.7%，弱）（OI 0.3k）

12-18（MEDIUM △）Top ΔOI: 140P +3,126 ｜ 148P -869
12-18（MEDIUM △）仓位参考: Max Pain 137 ｜ Call Wall 145（-0.3%，弱）（OI 6.6k）

📅 事件差分（观察，非因果）: 11-27（4D）ATM IV 45.0% vs 12-04 38.5%（差 +6.4pp）——覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-23/XBI_morning.json