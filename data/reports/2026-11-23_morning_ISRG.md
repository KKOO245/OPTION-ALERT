# 期权晨报 2026-11-23（快照 10:20 ET）

📊 市场环境

SPY $723.14 ｜ QQQ $656.34
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
🟡 **近现价集中开仓**: 11-27 410C ΔOI +163（距现价 -0.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 399.05 → 今开 410.89（+3.0%） | 较昨收变动（含盘初走势） ｜ 今日高 415.36 ｜ 低 407.34

Options: P/C成交量 0.14 | OI比 0.60 | ATM IV 43.8% | Skew 3.6pp | Term 0.87 | ExpMove ±2.7%（近端） | Rank 72%
量化视角： IV 中性（Rank 72%）｜期限结构倒挂（Term 0.87，近月 IV 高于远月）｜保护溢价中性（Skew 3.6pp）｜存量 Call 偏重（OI比 0.60）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.14×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.60×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（4D）±2.7% ｜ 12-04（11D）±6.0% ｜ 12-11（18D）±8.3% ｜ 12-18（25D）±8.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 722,353 | GEX Change vs 上次快照 620,742 | Flip: Primary Flip: 398.51（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 243 / LOW 170 / INVALID 571
结构观察区: Primary Flip 398.51（全链重定价，覆盖 96%）
Call Wall 400（弱结构｜现价高于该位 2.7%）
最近结构参考: Call Wall 400（现价高于该位 2.7%）
量化视角： 正 Gamma（72万，无历史分位）｜正 Gamma 增强（+62万）｜现价位于 Flip 上方 3.06%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 410（MaxPain，仅结算参考） / 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 399（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 410.0C — Vol 168 | 最新价 $4.80 | OI 14→177 (ΔOI +163张) | ΔOI/Volume 97.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增163张（+1164.3% vs前日OI），连续性待观察（方向未知）
11-27 407.5C — Vol 89 | 最新价 $8.12 | OI 0→89 (ΔOI +89张) | ΔOI/Volume 100.0% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增89张（前日OI缺失），值得跟踪（方向未知）
11-27 430.0C — Vol 71 | 最新价 $1.20 | OI 66→131 (ΔOI +65张) | ΔOI/Volume 91.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增65张（+98.5% vs前日OI），连续性待观察（方向未知）
12-18 405.0C — Vol 70 | 最新价 $14.80 | OI 97→159 (ΔOI +62张) | ΔOI/Volume 88.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增62张（+63.9% vs前日OI），连续性待观察（方向未知）
12-18 380.0P — Vol 82 | 最新价 $6.60 | OI 369→423 (ΔOI +54张) | ΔOI/Volume 65.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增54张（+14.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 433 张（Put 54 / Call 379），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-27  C +0.4k / P +25 ｜ Activity MEDIUM △ ｜ 4D
12-04  C +82 / P +70 ｜ Activity MEDIUM △ ｜ 11D
12-11  C +21 / P +29 ｜ Activity MEDIUM △ ｜ 18D
12-18  C +0.1k / P +32 ｜ Activity MEDIUM △ ｜ 25D

📆 11-27 Forward Structure
存量OI: C 1.3k / P 0.8k，今日变化ΔOI: C +0.4k / P +25，平值价格ATM: C $4.80 / P $6.47 ｜ ATM IV 43.8%，净 delta 敞口 19k shares
Top ΔOI: C 410 +163 ｜ C 407 +89 ｜ C 430 +65
仓位参考: Max Pain 410 ｜ Call Wall 410（-0.2%，弱）（OI 0.2k） ｜ Put Wall 395（-3.8%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 43.8%｜历史 Rank 72%（近端代理）｜IV/RV 0.96×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 18,861 股

12-04（MEDIUM △）Top ΔOI: 402C +24 ｜ 405C +22
12-04（MEDIUM △）仓位参考: Max Pain 420 ｜ Call Wall 450（+9.6%，弱）（OI 46） ｜ Put Wall 405（-1.4%，弱）（OI 29）

12-11（MEDIUM △）Top ΔOI: 435C +19 ｜ 405P +11
12-11（MEDIUM △）仓位参考: Max Pain 435 ｜ Call Wall 450（+9.6%）（OI 0.1k） ｜ Put Wall 435（+5.9%）（OI 36）

12-18（MEDIUM △）Top ΔOI: 405C +62 ｜ 380P +54
12-18（MEDIUM △）仓位参考: Max Pain 410 ｜ Call Wall 400（-2.6%，弱）（OI 1.5k） ｜ Put Wall 420（+2.3%，弱）（OI 0.6k）

📅 事件差分（观察，非因果）: 11-27（4D）ATM IV 43.8% vs 12-04 38.7%（差 +5.1pp）——覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-23/ISRG_morning.json