# 期权晨报 2026-10-26（快照 09:08 ET）

📊 市场环境

SPY $765.37 ｜ QQQ $712.20
VIX 19.22 ↓1.2%（5D +4.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-26

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-27 08:30　【高】耐用品订单 Orders MoM　预测 1.5 ｜ 实际 待公布 ｜ 前值 0
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 4
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.9
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2

🔍 重点速览
🟡 **近现价集中开仓**: 10-30 9P ΔOI +576（距现价 +1.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 9.33 → 今开 9.52（+2.0%） | 较昨收变动（含盘初走势） ｜ 今日高 9.58 ｜ 低 9.26

Options: P/C成交量 0.80 | OI比 0.46 | ATM IV 73.2% | Skew -7.1pp | Term 1.17 | ExpMove ±8.3%（近端） | Rank 8%
量化视角： IV 历史低位（Rank 8%，期权偏便宜）｜期限结构正常偏陡（Term 1.17）｜Put 保护异常便宜（Skew -7.1pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.46）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.80×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.46×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（4D）±8.3% ｜ 11-06（11D）±13.2% ｜ 11-13（18D）±17.7% ｜ 11-20（25D）±19.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -2,760,165 | GEX Change vs 上次快照 -476,746 | Flip: Primary Flip: 10.17（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 189 / LOW 67 / INVALID 160
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 10.17（全链重定价，覆盖 100%）
Put Wall 10（弱结构｜现价低于该位 6.2%）
最近结构参考: Put Wall 10（现价低于该位 6.2%）
量化视角： 负 Gamma（276万，无历史分位）｜负 Gamma 加深（48万）｜现价位于 Flip 下方 7.79%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 10（Put Wall，弱结构） / 11（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 10（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 9.0P — Vol 1,063 | 最新价 $0.71 | OI 888→1747 (ΔOI +859张) | ΔOI/Volume 80.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增859张（+96.7% vs前日OI），连续性待观察（方向未知）
10-30 9.5P — Vol 611 | 最新价 $0.46 | OI 182→758 (ΔOI +576张) | ΔOI/Volume 94.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增576张（+316.5% vs前日OI），连续性待观察（方向未知）
11-20 9.0C — Vol 464 | 最新价 $1.14 | OI 55→501 (ΔOI +446张) | ΔOI/Volume 96.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增446张（+810.9% vs前日OI），连续性待观察（方向未知）
11-20 9.5C — Vol 427 | 最新价 $0.88 | OI 390→703 (ΔOI +313张) | ΔOI/Volume 73.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增313张（+80.3% vs前日OI），连续性待观察（方向未知）
11-13 10.0C — Vol 311 | 最新价 $0.54 | OI 94→365 (ΔOI +271张) | ΔOI/Volume 87.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增271张（+288.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,465 张（Put 1,435 / Call 1,030），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +0.6k / P +0.5k ｜ Activity HIGH ｜ 4D
11-06  C +0.5k / P -17 ｜ Activity HIGH ｜ 11D
11-13  C +0.4k / P +44 ｜ Activity HIGH ｜ 18D
11-20  C +1.4k / P +0.3k ｜ Activity HIGH ｜ 25D

📆 10-30 Forward Structure
存量OI: C 20.0k / P 9.3k，今日变化ΔOI: C +0.6k / P +0.5k，平值价格ATM: C $0.32 / P $0.46 ｜ ATM IV 73.2%，净 delta 敞口 21k shares
Top ΔOI: P 9 +576 ｜ C 10 +265 ｜ P 14 -234
仓位参考: Max Pain 11 ｜ Call Wall 10（+6.6%，弱）（OI 1.2k） ｜ Put Wall 9（-4.1%）（OI 3.8k）
量化解读： 存量 Call 重｜ATM IV 73.2%｜历史 Rank 8%（近端代理）｜IV/RV 1.29×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 21,242 股

📆 11-06 Forward Structure
存量OI: C 5.7k / P 4.2k，今日变化ΔOI: C +0.5k / P -17，平值价格ATM: C $0.56 / P $0.68 ｜ ATM IV 86.4%，净 delta 敞口 21k shares
Top ΔOI: C 10 +171
仓位参考: Max Pain 12 ｜ Call Wall 10（+6.6%，弱）（OI 0.3k） ｜ Put Wall 9（-4.1%）（OI 1.5k）
量化解读： 存量 Call 重｜ATM IV 86.4%｜历史 Rank 8%（近端代理）｜IV/RV 1.52×（近似）｜净 delta 敞口 正 20,786 股

📆 11-13 Forward Structure
存量OI: C 3.1k / P 2.7k，今日变化ΔOI: C +0.4k / P +44，平值价格ATM: C $0.77 / P $0.89 ｜ ATM IV 92.1%，净 delta 敞口 17k shares
Top ΔOI: C 10 +271 ｜ C 9 +106
仓位参考: Max Pain 12 ｜ Call Wall 10（+6.6%，弱）（OI 0.4k） ｜ Put Wall 9（-4.1%，弱）（OI 0.1k）
量化解读： 存量两侧均衡｜ATM IV 92.1%｜历史 Rank 8%（近端代理）｜IV/RV 1.62×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 16,907 股

📆 11-20 Forward Structure
存量OI: C 25.4k / P 26.6k，今日变化ΔOI: C +1.4k / P +0.3k，平值价格ATM: C $0.88 / P $0.93 ｜ ATM IV 87.4%，净 delta 敞口 57k shares
Top ΔOI: P 9 +859 ｜ P 10 -531 ｜ C 9 +446
仓位参考: Max Pain 14 ｜ Put Wall 10（+6.6%，弱）（OI 7.7k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 87.4%｜历史 Rank 8%（近端代理）｜IV/RV 1.54×（近似）｜净 delta 敞口 正 57,306 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-26/USAR_morning.json