# 期权晨报 2026-11-24（快照 10:20 ET）

📊 市场环境

SPY $718.15 ｜ QQQ $638.10
VIX 27.25 ↑2.4%（5D +7.0%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 17.4（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-24

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-25 08:30　【高】Personal Spending MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.5
- 周三 11-25 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 11-25 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 11-25 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 3.5 ｜ 实际 待公布 ｜ 前值 1.5
- 周三 11-25 08:30　【高】耐用品订单 Orders MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 1.8

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 12-04 90P ΔOI +731（距现价 +0.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 97.80 → 今开 94.62（-3.3%） | 较昨收变动（含盘初走势） ｜ 今日高 95.28 ｜ 低 86.47

Options: P/C成交量 0.64 | OI比 0.40 | ATM IV 147.0% | Skew 17.0pp | Term 0.87 | ExpMove ±11.0%（近端） | Rank 88%
量化视角： IV 历史高位（Rank 88%，期权偏贵）｜期限结构倒挂（Term 0.87，近月 IV 高于远月）｜保护溢价显著（Skew 17.0pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.40）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.64×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.40×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（3D）±11.0% ｜ 12-04（10D）±18.4% ｜ 12-11（17D）±10.2% ｜ 12-18（24D）±26.5%
   ⇒ IV–VIX Spread: +119.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -2,841,818 | GEX Change vs 上次快照 -4,669,133 | Flip: Primary Flip: 92.89（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 639 / LOW 85 / INVALID 230
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 92.89（全链重定价，覆盖 100%）
最近结构参考: Flip 93（现价低于该位 3.9%）
量化视角： 负 Gamma（284万，无历史分位）｜由正转负（467万）｜现价位于 Flip 下方 3.87%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 100（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 93（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 110.0C — Vol 16,345 | 最新价 $1.62 | OI 3829→8146 (ΔOI +4317张) | ΔOI/Volume 26.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4317张（+112.7% vs前日OI），连续性待观察（方向未知）
11-27 120.0C — Vol 15,426 | 最新价 $0.51 | OI 1976→6039 (ΔOI +4063张) | ΔOI/Volume 26.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4063张（+205.6% vs前日OI），连续性待观察（方向未知）
12-18 150.0C — Vol 4,386 | 最新价 $1.33 | OI 5588→7685 (ΔOI +2097张) | ΔOI/Volume 47.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2097张（+37.5% vs前日OI），连续性待观察（方向未知）
11-27 102.0C — Vol 3,092 | 最新价 $3.90 | OI 271→2343 (ΔOI +2072张) | ΔOI/Volume 67.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2072张（+764.6% vs前日OI），连续性待观察（方向未知）
11-27 240.0C — Vol 1,875 | 最新价 $0.01 | OI 293→2073 (ΔOI +1780张) | ΔOI/Volume 94.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1780张（+607.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 14,329 张（Put 0 / Call 14,329），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-27  C +28.5k / P +11.2k ｜ Activity HIGH ｜ 3D
12-04  C +4.8k / P +4.2k ｜ Activity HIGH ｜ 10D
12-11  C +2.1k / P +2.1k ｜ Activity HIGH ｜ 17D
12-18  C +5.9k / P +11.7k ｜ Activity MEDIUM △ ｜ 24D

📆 11-27 Forward Structure
存量OI: C 92.8k / P 37.4k，今日变化ΔOI: C +28.5k / P +11.2k，平值价格ATM: C $5.05 / P $4.80 ｜ ATM IV 147.0%，净 delta 敞口 -555k shares
Top ΔOI: C 110 +4,317 ｜ C 102 +2,072
仓位参考: Max Pain 100 ｜ Put Wall 95（+6.4%，弱）（OI 2.8k）
量化解读： 存量 Call 重｜ATM IV 147.0%｜历史 Rank 88%（近端代理）｜IV/RV 0.91×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 554,965 股

📆 12-04 Forward Structure
存量OI: C 27.2k / P 15.2k，今日变化ΔOI: C +4.8k / P +4.2k，平值价格ATM: C $8.56 / P $7.85 ｜ ATM IV 137.6%，净 delta 敞口 -118k shares
Top ΔOI: C 100 +978 ｜ P 90 +731
仓位参考: Max Pain 100 ｜ Put Wall 90（+0.8%，弱）（OI 1.5k）
量化解读： 存量 Call 重｜ATM IV 137.6%｜历史 Rank 88%（近端代理）｜IV/RV 0.85×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 118,240 股

📆 12-11 Forward Structure
存量OI: C 10.5k / P 13.0k，今日变化ΔOI: C +2.1k / P +2.1k，平值价格ATM: C $0.00 / P $9.15 ｜ ATM IV 134.1%，净 delta 敞口 -52k shares
Top ΔOI: C 120 +404 ｜ C 110 +391 ｜ P 95 +349
仓位参考: Max Pain 115 ｜ Call Wall 90（+0.8%，弱）（OI 0.3k） ｜ Put Wall 85（-4.8%，弱）（OI 1.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 134.1%｜历史 Rank 88%（近端代理）｜IV/RV 0.83×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 51,823 股

12-18（MEDIUM △）Top ΔOI: 150C +2,097 ｜ 80P +1,272
12-18（MEDIUM △）仓位参考: Max Pain 145 ｜ Put Wall 90（+0.8%，弱）（OI 4.5k）

📅 事件差分（观察，非因果）: 11-27（3D）ATM IV 147.0% vs 12-04 137.6%（差 +9.4pp）——覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=107 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=107）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-24/NBIS_morning.json