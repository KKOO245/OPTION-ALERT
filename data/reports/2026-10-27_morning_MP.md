# 期权晨报 2026-10-27（快照 10:20 ET）

📊 市场环境

SPY $766.09 ｜ QQQ $715.24
VIX 18.02 ↓2.0%（5D +4.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-27

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-27 08:30　【高】耐用品订单 Orders MoM　预测 1.5 ｜ 实际 1.8 ｜ 前值 0.1　✅ 今日已公布
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 4
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.9

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-30 40C ΔOI +924（距现价 +2.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 37.47 → 今开 38.28（+2.1%） | 较昨收变动（含盘初走势） ｜ 今日高 39.58 ｜ 低 38.00

Options: P/C成交量 0.31 | OI比 0.62 | ATM IV 70.3% | Skew 8.3pp | Term 0.88 | ExpMove ±5.8%（近端） | Rank 56%
量化视角： IV 中性（Rank 56%）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜保护溢价显著（Skew 8.3pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.62）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.31×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.62×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（3D）±5.8% ｜ 11-06（10D）±11.8% ｜ 11-13（17D）±13.2% ｜ 11-20（24D）±13.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 339,711 | GEX Change vs 上次快照 2,428,866 | Flip: Primary Flip: 38.77（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 315 / LOW 58 / INVALID 153
结构观察区: Primary Flip 38.77（全链重定价，覆盖 100%）
最近结构参考: Flip 39（现价高于该位 0.9%）
量化视角： 正 Gamma（34万，无历史分位）｜由负转正（+243万）｜现价位于 Flip 上方 0.85%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 42（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 39（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 44.0C — Vol 1,000 | 最新价 $1.00 | OI 4→1004 (ΔOI +1000张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1000张（+25000.0% vs前日OI），连续性待观察（方向未知）
10-30 40.0C — Vol 1,058 | 最新价 $0.30 | OI 182→1106 (ΔOI +924张) | ΔOI/Volume 87.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增924张（+507.7% vs前日OI），连续性待观察（方向未知）
11-27 48.0C — Vol 605 | 最新价 $0.47 | OI 19→603 (ΔOI +584张) | ΔOI/Volume 96.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增584张（+3073.7% vs前日OI），连续性待观察（方向未知）
11-20 33.0P — Vol 491 | 最新价 $0.74 | OI 90→442 (ΔOI +352张) | ΔOI/Volume 71.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增352张（+391.1% vs前日OI），连续性待观察（方向未知）
11-20 45.0C — Vol 334 | 最新价 $0.59 | OI 1179→1479 (ΔOI +300张) | ΔOI/Volume 89.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增300张（+25.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,160 张（Put 352 / Call 2,808），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +2.4k / P -0.2k ｜ Activity HIGH ｜ 3D
11-06  C +0.6k / P +0.4k ｜ Activity MEDIUM △ ｜ 10D
11-13  C +0.2k / P +0.3k ｜ Activity MEDIUM △ ｜ 17D
11-20  C +1.0k / P +0.7k ｜ Activity MEDIUM △ ｜ 24D

📆 10-30 Forward Structure
存量OI: C 12.1k / P 7.5k，今日变化ΔOI: C +2.4k / P -0.2k，平值价格ATM: C $1.10 / P $1.15 ｜ ATM IV 70.3%，净 delta 敞口 139k shares
Top ΔOI: C 40 +924 ｜ C 41 +273 ｜ P 42 -223
仓位参考: Max Pain 42 ｜ Call Wall 40（+2.3%，弱）（OI 1.1k） ｜ Put Wall 38（-2.8%，弱）（OI 1.2k）
量化解读： 存量 Call 重｜ATM IV 70.3%｜历史 Rank 56%（近端代理）｜IV/RV 1.64×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 139,472 股

11-06（MEDIUM △）Top ΔOI: 42P +190 ｜ 37P +59
11-06（MEDIUM △）仓位参考: Max Pain 42 ｜ Call Wall 43（+10.0%，弱）（OI 0.9k） ｜ Put Wall 38（-2.8%）（OI 0.9k）

11-13（MEDIUM △）Top ΔOI: 42P +129 ｜ 39P +98
11-13（MEDIUM △）仓位参考: Max Pain 42 ｜ Put Wall 39（-0.3%）（OI 0.8k）

11-20（MEDIUM △）Top ΔOI: 36C +170
11-20（MEDIUM △）仓位参考: Max Pain 45 ｜ Call Wall 40（+2.3%，弱）（OI 0.9k） ｜ Put Wall 40（+2.3%，弱）（OI 1.6k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-27/MP_morning.json