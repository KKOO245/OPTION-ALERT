# 期权晨报 2026-11-25（快照 10:20 ET）

📊 市场环境

SPY $701.98 ｜ QQQ $610.90
VIX 31.62 ↑19.9%（5D +28.8%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 9.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-25

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-25 08:30　【高】Personal Spending MoM　预测 0.4 ｜ 实际 0.3 ｜ 前值 0.6　✅ 今日已公布
- 周三 11-25 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周三 11-25 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 0.7 ｜ 前值 0.3　✅ 今日已公布
- 周三 11-25 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 3.5 ｜ 实际 4.3 ｜ 前值 1.5　✅ 今日已公布
- 周三 11-25 08:30　【高】耐用品订单 Orders MoM　预测 0.6 ｜ 实际 0.2 ｜ 前值 1.8　✅ 今日已公布

🔍 重点速览
🔴 **事件差分**: 11-27（2D）ATM IV 112.1% vs 11-30 78.1%（差 +34.1pp），覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-30 145P ΔOI +3,275（距现价 -0.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 155.38 → 今开 144.02（-7.3%） | 较昨收变动（含盘初走势） ｜ 今日高 145.98 ｜ 低 141.17

Options: P/C成交量 1.03 | OI比 0.69 | ATM IV 142.8% | Skew 4.0pp | Term 0.52 | ExpMove ±0.0%（近端） | Rank 98%
量化视角： IV 历史高位（Rank 98%，期权偏贵）｜期限结构倒挂（Term 0.52，近月 IV 高于远月）｜保护溢价中性（Skew 4.0pp）｜存量 Call 偏重（OI比 0.69）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.03×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.69×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（2D）±0.0% ｜ 11-30（5D）±7.5% ｜ 12-02（7D）±9.7% ｜ 12-04（9D）±0.0%
   ⇒ IV–VIX Spread: +111.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 22,623,659 | GEX Change vs 上次快照 -57,015,237 | Flip: Primary Flip: 143.76（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1423 / LOW 273 / INVALID 926
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 143.76（全链重定价，覆盖 99%）
Put Wall 150（弱结构｜现价低于该位 3.1%）
最近结构参考: Flip 144（现价高于该位 1.1%）
量化视角： 正 Gamma（2262万，无历史分位）｜正 Gamma 减弱（5702万）｜现价位于 Flip 上方 1.05%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 150（Put Wall，弱结构） / 152（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 144（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-25 167.5C — Vol 52,276 | 最新价 $0.37 | OI 6756→31497 (ΔOI +24741张) | ΔOI/Volume 47.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增24741张（+366.2% vs前日OI），连续性待观察（方向未知）
11-25 160.0C — Vol 161,274 | 最新价 $1.62 | OI 8990→31565 (ΔOI +22575张) | ΔOI/Volume 14.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增22575张（+251.1% vs前日OI），连续性待观察（方向未知）
11-25 170.0C — Vol 100,888 | 最新价 $0.22 | OI 14463→32541 (ΔOI +18078张) | ΔOI/Volume 17.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18078张（+125.0% vs前日OI），连续性待观察（方向未知）
12-02 167.5C — Vol 19,223 | 最新价 $2.75 | OI 1554→16386 (ΔOI +14832张) | ΔOI/Volume 77.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14832张（+954.4% vs前日OI），连续性待观察（方向未知）
11-25 135.0P — Vol 33,672 | 最新价 $0.11 | OI 3545→17865 (ΔOI +14320张) | ΔOI/Volume 42.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14320张（+403.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 94,546 张（Put 14,320 / Call 80,226），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 368.1k / P 253.2k，今日成交量: C 284.8k / P 293.4k，平值价格ATM: C $2.23 / P $2.25 ｜ ATM IV 142.8%，预期波动 ±3.1%，Max Pain 152
Top ΔOI: C 167 +24,741 ｜ C 160 +22,575 ｜ C 170 +18,078

📆 Forward Expiration Structure

11-27  C +55.5k / P +38.0k ｜ Activity HIGH ｜ 2D
11-30  C +21.3k / P +20.7k ｜ Activity HIGH ｜ 5D
12-02  C +16.1k / P +4.0k ｜ Activity HIGH ｜ 7D
12-04  C +48.1k / P +8.6k ｜ Activity HIGH ｜ 9D

📆 11-27 Forward Structure
存量OI: C 616.5k / P 417.2k，今日变化ΔOI: C +55.5k / P +38.0k，平值价格ATM: C $0.00 / P $0.00 ｜ ATM IV 112.1%，净 delta 敞口 -452k shares
Top ΔOI: C 170 +11,792 ｜ C 160 +10,859 ｜ C 165 +8,314
仓位参考: Max Pain 150 ｜ Call Wall 157.5（+8.4%，弱）（OI 20.0k） ｜ Put Wall 150（+3.3%，弱）（OI 21.3k）
量化解读： 存量 Call 重｜ATM IV 112.1%｜历史 Rank 98%（近端代理）｜IV/RV 0.88×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 452,490 股

📆 11-30 Forward Structure
存量OI: C 106.4k / P 69.4k，今日变化ΔOI: C +21.3k / P +20.7k，平值价格ATM: C $5.55 / P $5.35 ｜ ATM IV 78.1%，净 delta 敞口 -289k shares
Top ΔOI: P 145 +3,275 ｜ C 165 +2,990 ｜ P 140 +2,549
仓位参考: Max Pain 150 ｜ Call Wall 150（+3.3%，弱）（OI 4.9k） ｜ Put Wall 140（-3.6%，弱）（OI 5.2k）
量化解读： 存量 Call 重｜ATM IV 78.1%｜历史 Rank 98%（近端代理）｜IV/RV 0.61×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 288,758 股

📆 12-02 Forward Structure
存量OI: C 67.3k / P 23.8k，今日变化ΔOI: C +16.1k / P +4.0k，平值价格ATM: C $7.15 / P $7.00 ｜ ATM IV 86.6%，净 delta 敞口 175k shares
Top ΔOI: C 167 +14,832 ｜ C 170 -1,441
仓位参考: Max Pain 155 ｜ Put Wall 155（+6.7%，弱）（OI 1.9k）
量化解读： 存量 Call 重｜ATM IV 86.6%｜历史 Rank 98%（近端代理）｜IV/RV 0.68×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 175,144 股

📆 12-04 Forward Structure
存量OI: C 274.0k / P 179.7k，今日变化ΔOI: C +48.1k / P +8.6k，平值价格ATM: C $0.00 / P $0.00 ｜ ATM IV 74.7%，净 delta 敞口 -297k shares
Top ΔOI: P 80 -19,474 ｜ C 165 +10,839 ｜ C 170 +9,417
仓位参考: Max Pain 160 ｜ Call Wall 155（+6.7%，弱）（OI 6.4k） ｜ Put Wall 145（-0.2%，弱）（OI 8.1k）
量化解读： 存量 Call 重｜ATM IV 74.7%｜历史 Rank 98%（近端代理）｜IV/RV 0.59×（近似）｜净 delta 敞口 负 296,833 股

📅 事件差分（观察，非因果）: 11-27（2D）ATM IV 112.1% vs 11-30 78.1%（差 +34.1pp）——覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-25/NVDA_morning.json