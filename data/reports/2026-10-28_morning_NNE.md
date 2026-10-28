# 期权晨报 2026-10-28（快照 10:20 ET）

📊 市场环境

SPY $770.58 ｜ QQQ $721.71
VIX 17.36 ↓0.9%（5D +4.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-28

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布　⏰ 今日
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 4　⏰ 今日
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布　⏰ 今日
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.9

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-30 12C ΔOI +118（距现价 +2.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 12.34 → 今开 12.50（+1.3%） | 较昨收变动（含盘初走势） ｜ 今日高 12.50 ｜ 低 12.09

Options: P/C成交量 0.50 | OI比 0.19 | ATM IV 88.7% | Skew 16.5pp | Term 0.88 | ExpMove ±6.9%（近端） | Rank 23%
量化视角： IV 历史低位（Rank 23%，期权偏便宜）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜保护溢价显著（Skew 16.5pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.19）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.50×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.19×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（2D）±6.9% ｜ 11-06（9D）±13.1% ｜ 11-13（16D）±14.3% ｜ 11-20（23D）±16.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 488,553 | GEX Change vs 上次快照 305,894 | Flip: Primary Flip: 11.63（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 182 / LOW 80 / INVALID 146
结构观察区: Primary Flip 11.63（全链重定价，覆盖 95%）
最近结构参考: Flip 12（现价高于该位 5.2%）
量化视角： 正 Gamma（49万，无历史分位）｜正 Gamma 增强（+31万）｜现价位于 Flip 上方 5.21%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 13（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 12（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 13.0C — Vol 437 | 最新价 $0.10 | OI 442→751 (ΔOI +309张) | ΔOI/Volume 70.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增309张（+69.9% vs前日OI），连续性待观察（方向未知）
11-06 11.5P — Vol 208 | 最新价 $0.32 | OI 64→271 (ΔOI +207张) | ΔOI/Volume 99.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增207张（+323.4% vs前日OI），连续性待观察（方向未知）
10-30 13.5C — Vol 153 | 最新价 $0.04 | OI 298→428 (ΔOI +130张) | ΔOI/Volume 85.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增130张（+43.6% vs前日OI），连续性待观察（方向未知）
10-30 12.5C — Vol 189 | 最新价 $0.25 | OI 223→341 (ΔOI +118张) | ΔOI/Volume 62.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增118张（+52.9% vs前日OI），连续性待观察（方向未知）
11-06 13.0C — Vol 80 | 最新价 $0.33 | OI 16→90 (ΔOI +74张) | ΔOI/Volume 92.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增74张（+462.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 838 张（Put 207 / Call 631），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +0.6k / P -97 ｜ Activity HIGH ｜ 2D
11-06  C +0.2k / P +0.2k ｜ Activity HIGH ｜ 9D
11-13  C +50 / P +6 ｜ Activity HIGH ｜ 16D
11-20  C +0.2k / P -16 ｜ Activity MEDIUM △ ｜ 23D

📆 10-30 Forward Structure
存量OI: C 8.4k / P 1.6k，今日变化ΔOI: C +0.6k / P -97，平值价格ATM: C $0.55 / P $0.30 ｜ ATM IV 88.7%，净 delta 敞口 21k shares
Top ΔOI: C 13 +309 ｜ C 12 +118
仓位参考: Max Pain 13 ｜ Put Wall 13（+6.2%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 88.7%｜历史 Rank 23%（近端代理）｜IV/RV 1.36×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 21,367 股

📆 11-06 Forward Structure
存量OI: C 1.9k / P 1.0k，今日变化ΔOI: C +0.2k / P +0.2k，平值价格ATM: C $0.95 / P $0.65 ｜ ATM IV 83.5%，净 delta 敞口 3k shares
Top ΔOI: P 11 +207 ｜ C 13 +74
仓位参考: Max Pain 14 ｜ Put Wall 11.5（-6.0%）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 83.5%｜历史 Rank 23%（近端代理）｜IV/RV 1.28×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,909 股

📆 11-13 Forward Structure
存量OI: C 0.8k / P 0.4k，今日变化ΔOI: C +50 / P +6，平值价格ATM: C $1.10 / P $0.65 ｜ ATM IV 77.6%，净 delta 敞口 2k shares
Top ΔOI: C 12 +25
仓位参考: Max Pain 14 ｜ Put Wall 13（+6.2%，弱）（OI 68）
量化解读： 存量 Call 重｜ATM IV 77.6%｜历史 Rank 23%（近端代理）｜IV/RV 1.19×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,945 股

11-20（MEDIUM △）仓位参考: Max Pain 15 ｜ Put Wall 12（-2.0%，弱）（OI 0.3k）

📅 事件差分（观察，非因果）: 10-30（2D）ATM IV 88.7% vs 11-06 83.5%（差 +5.2pp）——覆盖 美联储议息会议 Statement、美联储利率决议 Decision、Fed Press Conference、GDP 增速 Rate QoQ Adv、PCE 物价 Price Index MoM、Personal Income MoM、Personal Spending MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-28/NNE_morning.json