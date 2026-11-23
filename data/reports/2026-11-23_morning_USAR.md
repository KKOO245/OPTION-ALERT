# 期权晨报 2026-11-23（快照 10:20 ET）

📊 市场环境

SPY $723.14 ｜ QQQ $656.24
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
🟡 **事件差分**: 11-27 ATM IV 132.0% vs 12-04 118.9%（差 +13.1pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-27 7C ΔOI +769（距现价 +3.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 6.27 → 今开 7.12（+13.6%） | 较昨收变动（含盘初走势） ｜ 今日高 7.15 ｜ 低 6.60

Options: P/C成交量 0.38 | OI比 0.23 | ATM IV 132.0% | Skew 21.6pp | Term 0.82 | ExpMove ±10.2%（近端） | Rank 71%
量化视角： IV 中性（Rank 71%）｜期限结构倒挂（Term 0.82，近月 IV 高于远月）｜保护溢价显著（Skew 21.6pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.23）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.38×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.23×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（4D）±10.2% ｜ 12-04（11D）±21.6% ｜ 12-11（18D）±27.2% ｜ 12-18（25D）±20.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,436,605 | GEX Change vs 上次快照 1,338,520 | Flip: Primary Flip: 6.30（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 155 / LOW 99 / INVALID 162
结构观察区: Primary Flip 6.30（全链重定价，覆盖 100%）
最近结构参考: Flip 6（现价高于该位 7.5%）
量化视角： 正 Gamma（144万，无历史分位）｜正 Gamma 增强（+134万）｜现价位于 Flip 上方 7.51%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 8（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 6（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 10.0C — Vol 16,654 | 最新价 $0.13 | OI 4105→20412 (ΔOI +16307张) | ΔOI/Volume 97.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16307张（+397.2% vs前日OI），连续性待观察（方向未知）
12-18 10.0P — Vol 16,352 | 最新价 $3.78 | OI 3387→19658 (ΔOI +16271张) | ΔOI/Volume 99.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16271张（+480.4% vs前日OI），连续性待观察（方向未知）
11-27 7.5C — Vol 3,281 | 最新价 $0.08 | OI 778→3620 (ΔOI +2842张) | ΔOI/Volume 86.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2842张（+365.3% vs前日OI），连续性待观察（方向未知）
11-27 7.0C — Vol 1,179 | 最新价 $0.14 | OI 894→1663 (ΔOI +769张) | ΔOI/Volume 65.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增769张（+86.0% vs前日OI），连续性待观察（方向未知）
11-27 6.5P — Vol 1,075 | 最新价 $0.54 | OI 264→868 (ΔOI +604张) | ΔOI/Volume 56.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增604张（+228.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 36,793 张（Put 16,875 / Call 19,918），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $6M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-27  C +3.9k / P +1.1k ｜ Activity HIGH ｜ 4D
12-04  C +0.2k / P +0.1k ｜ Activity MEDIUM △ ｜ 11D
12-11  C -1 / P +84 ｜ Activity MEDIUM △ ｜ 18D
12-18  C +16.6k / P +16.4k ｜ Activity HIGH ｜ 25D

📆 11-27 Forward Structure
存量OI: C 22.7k / P 5.2k，今日变化ΔOI: C +3.9k / P +1.1k，平值价格ATM: C $0.27 / P $0.42 ｜ ATM IV 132.0%，净 delta 敞口 100k shares
Top ΔOI: C 7 +769 ｜ P 6 +604
仓位参考: Max Pain 8 ｜ Call Wall 7（+3.4%，弱）（OI 1.7k） ｜ Put Wall 6.5（-4.0%，弱）（OI 0.9k）
量化解读： 存量 Call 重｜ATM IV 132.0%｜历史 Rank 71%（近端代理）｜IV/RV 1.25×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 100,303 股

12-04（MEDIUM △）Top ΔOI: 6P +62
12-04（MEDIUM △）仓位参考: Max Pain 8 ｜ Call Wall 7（+3.4%，弱）（OI 0.3k） ｜ Put Wall 7（+3.4%）（OI 0.6k）

12-11（MEDIUM △）仓位参考: Max Pain 8 ｜ Put Wall 7（+3.4%，弱）（OI 0.1k）

📆 12-18 Forward Structure
存量OI: C 106.3k / P 77.7k，今日变化ΔOI: C +16.6k / P +16.4k，平值价格ATM: C $0.73 / P $0.66 ｜ ATM IV 114.8%，净 delta 敞口 -1.2M shares
Top ΔOI: C 10 +16,307 ｜ P 10 +16,271 ｜ C 7 +178
仓位参考: Max Pain 10 ｜ Put Wall 7（+3.4%，弱）（OI 4.6k）
量化解读： 存量 Call 重｜ATM IV 114.8%｜历史 Rank 71%（近端代理）｜IV/RV 1.09×（近似）｜净 delta 敞口 负 1,173,475 股

📅 事件差分（观察，非因果）: 11-27（4D）ATM IV 132.0% vs 12-04 118.9%（差 +13.1pp）——覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-23/USAR_morning.json