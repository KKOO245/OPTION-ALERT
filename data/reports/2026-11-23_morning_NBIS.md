# 期权晨报 2026-11-23（快照 10:20 ET）

📊 市场环境

SPY $723.14 ｜ QQQ $655.71
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
🔴 **事件差分**: 11-27（4D）ATM IV 155.9% vs 12-04 137.0%（差 +18.8pp），覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-27 100C ΔOI +4,607（距现价 -1.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 81.31 → 今开 110.02（+35.3%） | 较昨收变动（含盘初走势） ｜ 今日高 110.03 ｜ 低 96.72

Options: P/C成交量 0.43 | OI比 0.41 | ATM IV 155.9% | Skew 16.4pp | Term 0.80 | ExpMove ±13.5%（近端） | Rank 92%
量化视角： IV 历史高位（Rank 92%，期权偏贵）｜期限结构倒挂（Term 0.80，近月 IV 高于远月）｜保护溢价显著（Skew 16.4pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.41）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.43×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.41×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（4D）±13.5% ｜ 12-04（11D）±19.1% ｜ 12-11（18D）±24.0% ｜ 12-18（25D）±25.4%
   ⇒ IV–VIX Spread: +128.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 4,493,302 | GEX Change vs 上次快照 8,205,716 | Flip: Primary Flip: 91.05（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 562 / LOW 70 / INVALID 322
结构观察区: Primary Flip 91.05（全链重定价，覆盖 100%）
最近结构参考: Flip 91（现价高于该位 11.7%）
量化视角： 正 Gamma（449万，无历史分位）｜由负转正（+821万）｜现价位于 Flip 上方 11.66%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 100（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 91（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 100.0C — Vol 11,984 | 最新价 $1.25 | OI 1266→5873 (ΔOI +4607张) | ΔOI/Volume 38.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4607张（+363.9% vs前日OI），连续性待观察（方向未知）
12-18 150.0C — Vol 3,027 | 最新价 $0.52 | OI 3256→5588 (ΔOI +2332张) | ΔOI/Volume 77.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2332张（+71.6% vs前日OI），连续性待观察（方向未知）
12-18 30.0P — Vol 1,847 | 最新价 $0.56 | OI 519→1985 (ΔOI +1466张) | ΔOI/Volume 79.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1466张（+282.5% vs前日OI），连续性待观察（方向未知）
11-27 80.0P — Vol 4,273 | 最新价 $6.40 | OI 2157→3603 (ΔOI +1446张) | ΔOI/Volume 33.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1446张（+67.0% vs前日OI），连续性待观察（方向未知）
12-18 50.0P — Vol 2,008 | 最新价 $2.25 | OI 1490→2729 (ΔOI +1239张) | ΔOI/Volume 61.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1239张（+83.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 11,090 张（Put 4,151 / Call 6,939），跨 2 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-27  C +9.1k / P +5.7k ｜ Activity HIGH ｜ 4D
12-04  C +3.4k / P +2.1k ｜ Activity HIGH ｜ 11D
12-11  C +1.0k / P +1.9k ｜ Activity HIGH ｜ 18D
12-18  C +5.3k / P +2.9k ｜ Activity HIGH ｜ 25D

📆 11-27 Forward Structure
存量OI: C 64.3k / P 26.2k，今日变化ΔOI: C +9.1k / P +5.7k，平值价格ATM: C $5.78 / P $7.97 ｜ ATM IV 155.9%，净 delta 敞口 736k shares
Top ΔOI: C 100 +4,607 ｜ C 110 -2,241 ｜ P 80 +1,446
仓位参考: Max Pain 100 ｜ Call Wall 100（-1.6%，弱）（OI 5.9k） ｜ Put Wall 95（-6.6%，弱）（OI 1.5k）
量化解读： 存量 Call 重｜ATM IV 155.9%｜历史 Rank 92%（近端代理）｜IV/RV 1.05×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 736,444 股

📆 12-04 Forward Structure
存量OI: C 22.4k / P 11.0k，今日变化ΔOI: C +3.4k / P +2.1k，平值价格ATM: C $9.00 / P $10.40 ｜ ATM IV 137.0%，净 delta 敞口 215k shares
Top ΔOI: C 95 +564 ｜ C 80 +549 ｜ P 84 +428
仓位参考: Max Pain 100 ｜ Call Wall 100（-1.6%，弱）（OI 0.7k） ｜ Put Wall 100（-1.6%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 137.0%｜历史 Rank 92%（近端代理）｜IV/RV 0.92×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 215,254 股

📆 12-11 Forward Structure
存量OI: C 8.4k / P 10.9k，今日变化ΔOI: C +1.0k / P +1.9k，平值价格ATM: C $12.70 / P $11.70 ｜ ATM IV 131.0%，净 delta 敞口 51k shares
Top ΔOI: P 55 +786 ｜ C 100 +347
仓位参考: Max Pain 120 ｜ Call Wall 100（-1.6%，弱）（OI 0.4k） ｜ Put Wall 100（-1.6%，弱）（OI 1.3k）
量化解读： 存量 Put 重｜ATM IV 131.0%｜历史 Rank 92%（近端代理）｜IV/RV 0.88×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 51,044 股

📆 12-18 Forward Structure
存量OI: C 137.3k / P 97.9k，今日变化ΔOI: C +5.3k / P +2.9k，平值价格ATM: C $13.50 / P $12.30 ｜ ATM IV 124.8%，净 delta 敞口 366k shares
Top ΔOI: C 150 +2,332 ｜ P 50 +1,239
仓位参考: Max Pain 150 ｜ Put Wall 100（-1.6%，弱）（OI 4.1k）
量化解读： 存量 Call 重｜ATM IV 124.8%｜历史 Rank 92%（近端代理）｜IV/RV 0.84×（近似）｜净 delta 敞口 正 366,108 股

📅 事件差分（观察，非因果）: 11-27（4D）ATM IV 155.9% vs 12-04 137.0%（差 +18.8pp）——覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-23/NBIS_morning.json