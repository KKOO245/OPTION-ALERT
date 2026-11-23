# 期权晚报 2026-11-23（快照 16:40 ET）

📊 市场环境

SPY $722.29 ｜ QQQ $651.03
VIX 26.62 ↓25.8%（5D +16.2%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 17.0（extreme fear）
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
🟡 **近现价集中开仓**: 11-27 85C ΔOI +27,040（距现价 +0.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 91.22 → 收盘 84.40（-7.5%） ｜ 今日高 91.36 ｜ 低 83.95 ｜ 昨收 77.80 → 收盘 84.40（+8.5%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-30，窗口结束前不做对错判定）

Options: P/C成交量 0.86 | OI比 0.63 | ATM IV 110.5% | Skew 10.6pp | Term 0.87 | ExpMove ±9.1%（近端） | Rank 87%
量化视角： IV 历史高位（Rank 87%，期权偏贵）｜期限结构倒挂（Term 0.87，近月 IV 高于远月）｜保护溢价显著（Skew 10.6pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.63）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.86×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.63×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（4D）±9.1% ｜ 12-04（11D）±14.7% ｜ 12-11（18D）±8.1% ｜ 12-18（25D）±20.4%
   ⇒ IV–VIX Spread: +83.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 12,536,482 | GEX Change vs 上次快照 -8,454,470 | Flip: Primary Flip: 80.63（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 470 / LOW 192 / INVALID 366
结构观察区: Primary Flip 80.63（全链重定价，覆盖 100%）
Put Wall 90（弱结构｜现价低于该位 6.2%） | Call Wall 90（弱结构｜现价低于该位 6.2%）
最近结构参考: Flip 81（现价高于该位 4.7%）
量化视角： 正 Gamma（1254万，无历史分位）｜正 Gamma 减弱（845万）｜现价位于 Flip 上方 4.67%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 90（Put Wall，弱结构） / 86（MaxPain，仅结算参考） / 90（Call Wall，弱结构）。
• Gamma 区域：切换参考 81（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 90.0C — Vol 5,489 | 最新价 $1.64 | OI 1469→41493 (ΔOI +40024张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增40024张（+2724.6% vs前日OI），连续性待观察（方向未知）
11-27 85.0C — Vol 3,821 | 最新价 $3.57 | OI 74→27114 (ΔOI +27040张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增27040张（+36540.5% vs前日OI），连续性待观察（方向未知）
11-27 86.0C — Vol 1,600 | 最新价 $3.05 | OI 190→17963 (ΔOI +17773张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17773张（+9354.2% vs前日OI），连续性待观察（方向未知）
11-27 40.0P — Vol 1,016 | 最新价 $0.01 | OI 598→17297 (ΔOI +16699张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16699张（+2792.5% vs前日OI），连续性待观察（方向未知）
12-18 85.0C — Vol 611 | 最新价 $8.40 | OI 324→9337 (ΔOI +9013张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9013张（+2781.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 110,549 张（Put 16,699 / Call 93,850），跨 2 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-27  C +99.3k / P +37.6k ｜ Activity HIGH ｜ 4D
12-04  C +11.0k / P +5.6k ｜ Activity HIGH ｜ 11D
12-11  C +1.7k / P -3.4k ｜ Activity HIGH ｜ 18D
12-18  C +8.1k / P -9.4k ｜ Activity HIGH ｜ 25D

📆 11-27 Forward Structure
存量OI: C 246.1k / P 156.0k，今日变化ΔOI: C +99.3k / P +37.6k，平值价格ATM: C $4.05 / P $3.60 ｜ ATM IV 110.5%，净 delta 敞口 4.1M shares
Top ΔOI: C 90 +40,024 ｜ C 85 +27,040 ｜ C 86 +17,773
仓位参考: Max Pain 86 ｜ Call Wall 90（+6.6%）（OI 41.5k） ｜ Put Wall 90（+6.6%，弱）（OI 14.9k）
量化解读： 存量 Call 重｜ATM IV 110.5%｜历史 Rank 87%（近端代理）｜IV/RV 1.41×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 4,080,710 股

📆 12-04 Forward Structure
存量OI: C 37.4k / P 64.4k，今日变化ΔOI: C +11.0k / P +5.6k，平值价格ATM: C $6.55 / P $5.85 ｜ ATM IV 104.3%，净 delta 敞口 425k shares
Top ΔOI: P 65 +2,276 ｜ C 110 +2,033 ｜ C 100 +1,609
仓位参考: Max Pain 98 ｜ Put Wall 85（+0.7%，弱）（OI 6.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 104.3%｜历史 Rank 87%（近端代理）｜IV/RV 1.33×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 424,785 股

📆 12-11 Forward Structure
存量OI: C 10.7k / P 34.1k，今日变化ΔOI: C +1.7k / P -3.4k，平值价格ATM: C $0.00 / P $6.80 ｜ ATM IV 100.6%，净 delta 敞口 536k shares
Top ΔOI: P 135 -1,278 ｜ P 130 -1,097 ｜ P 140 -752
仓位参考: Max Pain 110 ｜ Call Wall 90（+6.6%，弱）（OI 0.9k） ｜ Put Wall 80（-5.2%，弱）（OI 3.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 100.6%｜历史 Rank 87%（近端代理）｜IV/RV 1.29×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 535,658 股

📆 12-18 Forward Structure
存量OI: C 239.5k / P 172.4k，今日变化ΔOI: C +8.1k / P -9.4k，平值价格ATM: C $9.00 / P $8.20 ｜ ATM IV 97.6%，净 delta 敞口 840k shares
Top ΔOI: C 85 +9,013 ｜ C 180 -4,367
仓位参考: Max Pain 125 ｜ Call Wall 85（+0.7%，弱）（OI 9.3k） ｜ Put Wall 80（-5.2%，弱）（OI 9.5k）
量化解读： 存量 Call 重｜ATM IV 97.6%｜历史 Rank 87%（近端代理）｜IV/RV 1.25×（近似）｜净 delta 敞口 正 840,055 股

📅 事件差分（观察，非因果）: 11-27（4D）ATM IV 110.5% vs 12-04 104.3%（差 +6.1pp）——覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-23/MSTR_evening.json