# 期权晚报 2026-10-27（快照 16:40 ET）

📊 市场环境

SPY $769.66 ｜ QQQ $721.25
VIX 17.52 ↓4.7%（5D +1.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 32.7（fear）
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
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.9
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2

🔍 重点速览
🟡 **事件差分**: 10-30 ATM IV 106.3% vs 11-06 94.2%（差 +12.1pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-30 10C ΔOI +1,864（距现价 -3.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 9.12 → 收盘 10.40（+14.0%） ｜ 今日高 10.48 ｜ 低 9.02 ｜ 昨收 8.91 → 收盘 10.40（+16.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.21 | OI比 0.40 | ATM IV 106.3% | Skew -5.2pp | Term 0.83 | ExpMove ±7.6%（近端） | Rank 38%
量化视角： IV 中性（Rank 38%）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜Put 保护异常便宜（Skew -5.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.40）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.21×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.40×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（3D）±7.6% ｜ 11-06（10D）±13.9% ｜ 11-13（17D）±16.4% ｜ 11-20（24D）±21.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,151,862 | GEX Change vs 上次快照 2,148,541 | Flip: Primary Flip: 9.69（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 219 / LOW 76 / INVALID 125
结构观察区: Primary Flip 9.69（全链重定价，覆盖 100%）
Call Wall 10（弱结构｜现价高于该位 4.0%）
最近结构参考: Call Wall 10（现价高于该位 4.0%）
量化视角： 正 Gamma（215万，无历史分位）｜正 Gamma 增强（+215万）｜现价位于 Flip 上方 7.28%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 10（MaxPain，仅结算参考） / 10（Call Wall，弱结构）。
• Gamma 区域：切换参考 10（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 9.0P — Vol 1,562 | 最新价 $0.89 | OI 888→1747 (ΔOI +859张) | ΔOI/Volume 55.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增859张（+96.7% vs前日OI），连续性待观察（方向未知）
10-30 9.5P — Vol 525 | 最新价 $0.63 | OI 182→758 (ΔOI +576张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增576张（+316.5% vs前日OI），连续性待观察（方向未知）
11-20 9.0C — Vol 854 | 最新价 $0.89 | OI 55→501 (ΔOI +446张) | ΔOI/Volume 52.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增446张（+810.9% vs前日OI），连续性待观察（方向未知）
11-20 9.5C — Vol 871 | 最新价 $0.66 | OI 390→703 (ΔOI +313张) | ΔOI/Volume 35.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增313张（+80.3% vs前日OI），连续性待观察（方向未知）
11-13 10.0C — Vol 74 | 最新价 $0.43 | OI 94→365 (ΔOI +271张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增271张（+288.3% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,465 张（Put 1,435 / Call 1,030），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +3.6k / P +96 ｜ Activity HIGH ｜ 3D
11-06  C +0.8k / P -45 ｜ Activity HIGH ｜ 10D
11-13  C +0.8k / P -27 ｜ Activity HIGH ｜ 17D
11-20  C +2.2k / P -0.4k ｜ Activity HIGH ｜ 24D

📆 10-30 Forward Structure
存量OI: C 23.6k / P 9.4k，今日变化ΔOI: C +3.6k / P +96，平值价格ATM: C $0.34 / P $0.45 ｜ ATM IV 106.3%，净 delta 敞口 278k shares
Top ΔOI: C 10 +1,864 ｜ C 9 +718 ｜ C 10 +514
仓位参考: Max Pain 10 ｜ Call Wall 10（-3.8%，弱）（OI 3.0k）
量化解读： 存量 Call 重｜ATM IV 106.3%｜历史 Rank 38%（近端代理）｜IV/RV 1.82×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 278,378 股

📆 11-06 Forward Structure
存量OI: C 6.5k / P 4.2k，今日变化ΔOI: C +0.8k / P -45，平值价格ATM: C $0.64 / P $0.81 ｜ ATM IV 94.2%，净 delta 敞口 63k shares
Top ΔOI: C 10 +310 ｜ C 10 +188
仓位参考: Max Pain 11 ｜ Call Wall 10（-3.8%，弱）（OI 0.6k） ｜ Put Wall 10（-3.8%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 94.2%｜历史 Rank 38%（近端代理）｜IV/RV 1.61×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 62,986 股

📆 11-13 Forward Structure
存量OI: C 3.9k / P 2.7k，今日变化ΔOI: C +0.8k / P -27，平值价格ATM: C $0.83 / P $0.88 ｜ ATM IV 96.7%，净 delta 敞口 84k shares
Top ΔOI: C 9 +585 ｜ P 15 -209
仓位参考: Max Pain 10 ｜ Call Wall 10（-3.8%，弱）（OI 0.4k） ｜ Put Wall 11（+5.8%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 96.7%｜历史 Rank 38%（近端代理）｜IV/RV 1.65×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 83,540 股

📆 11-20 Forward Structure
存量OI: C 27.5k / P 26.2k，今日变化ΔOI: C +2.2k / P -0.4k，平值价格ATM: C $0.96 / P $1.23 ｜ ATM IV 93.5%，净 delta 敞口 185k shares
Top ΔOI: P 10 -1,553 ｜ P 9 +1,310 ｜ C 9 +735
仓位参考: Max Pain 13 ｜ Call Wall 11（+5.8%，弱）（OI 1.4k） ｜ Put Wall 10（-3.8%，弱）（OI 6.2k）
量化解读： 存量两侧均衡｜ATM IV 93.5%｜历史 Rank 38%（近端代理）｜IV/RV 1.60×（近似）｜净 delta 敞口 正 184,835 股

📅 事件差分（观察，非因果）: 10-30（3D）ATM IV 106.3% vs 11-06 94.2%（差 +12.1pp）——覆盖 耐用品订单 Orders MoM、美联储议息会议 Statement 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-27/USAR_evening.json