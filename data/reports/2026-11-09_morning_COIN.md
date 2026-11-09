# 期权晨报 2026-11-09（快照 10:20 ET）

📊 市场环境

SPY $748.41 ｜ QQQ $674.60
VIX 21.34 ↓16.8%（5D +0.9%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 31.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-09

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-10 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周二 11-10 08:30　【高】Core Inflation Rate YoY　预测 2.8 ｜ 实际 待公布 ｜ 前值 2.6
- 周二 11-10 08:30　【高】Inflation Rate MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.6
- 周二 11-10 08:30　【高】Inflation Rate YoY　预测 3.9 ｜ 实际 待公布 ｜ 前值 3.7
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-13 141C ΔOI +8,272（距现价 +3.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 134.76 → 今开 131.36（-2.5%） | 较昨收变动（含盘初走势） ｜ 今日高 137.39 ｜ 低 131.12

Options: P/C成交量 0.29 | OI比 0.56 | ATM IV 86.3% | Skew 6.3pp | Term 0.80 | ExpMove ±7.5%（近端） | Rank 75%
量化视角： IV 中性（Rank 75%）｜期限结构倒挂（Term 0.80，近月 IV 高于远月）｜保护溢价显著（Skew 6.3pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.56）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.29×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.56×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（4D）±7.5% ｜ 11-20（11D）±5.5% ｜ 11-27（18D）±6.3% ｜ 12-04（25D）±15.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 7,619,243 | GEX Change vs 上次快照 13,193,902 | Flip: Primary Flip: 130.17（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 406 / LOW 203 / INVALID 379
结构观察区: Primary Flip 130.17（全链重定价，覆盖 100%）
最近结构参考: Flip 130（现价高于该位 4.3%）
量化视角： 正 Gamma（762万，无历史分位）｜由负转正（+1319万）｜现价位于 Flip 上方 4.25%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 137（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 130（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 147.0C — Vol 8,544 | 最新价 $1.44 | OI 142→8496 (ΔOI +8354张) | ΔOI/Volume 97.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8354张（+5883.1% vs前日OI），连续性待观察（方向未知）
11-13 141.0C — Vol 8,422 | 最新价 $2.93 | OI 135→8407 (ΔOI +8272张) | ΔOI/Volume 98.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8272张（+6127.4% vs前日OI），连续性待观察（方向未知）
11-13 143.0C — Vol 7,179 | 最新价 $2.42 | OI 75→7060 (ΔOI +6985张) | ΔOI/Volume 97.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6985张（+9313.3% vs前日OI），连续性待观察（方向未知）
11-13 137.0C — Vol 7,602 | 最新价 $4.55 | OI 128→7098 (ΔOI +6970张) | ΔOI/Volume 91.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6970张（+5445.3% vs前日OI），连续性待观察（方向未知）
11-13 140.0C — Vol 3,601 | 最新价 $3.25 | OI 473→3330 (ΔOI +2857张) | ΔOI/Volume 79.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2857张（+604.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 33,438 张（Put 0 / Call 33,438），跨 1 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +45.6k / P +8.2k ｜ Activity HIGH ｜ 4D
11-20  C +1.4k / P +3.1k ｜ Activity HIGH ｜ 11D
11-27  C +0.5k / P +0.5k ｜ Activity MEDIUM △ ｜ 18D
12-04  C +0.1k / P +1.1k ｜ Activity MEDIUM △ ｜ 25D

📆 11-13 Forward Structure
存量OI: C 63.5k / P 35.3k，今日变化ΔOI: C +45.6k / P +8.2k，平值价格ATM: C $5.02 / P $5.10 ｜ ATM IV 86.3%，净 delta 敞口 1.4M shares
Top ΔOI: C 147 +8,354 ｜ C 141 +8,272 ｜ C 143 +6,985
仓位参考: Max Pain 137 ｜ Call Wall 147（+8.3%，弱）（OI 8.5k） ｜ Put Wall 135（-0.5%，弱）（OI 2.2k）
量化解读： 存量 Call 重｜ATM IV 86.3%｜历史 Rank 75%（近端代理）｜IV/RV 1.29×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,358,952 股

📆 11-20 Forward Structure
存量OI: C 78.1k / P 62.4k，今日变化ΔOI: C +1.4k / P +3.1k，平值价格ATM: C $7.40 / P $0.00 ｜ ATM IV 77.5%，净 delta 敞口 63k shares
Top ΔOI: P 75 +2,543 ｜ P 120 +645 ｜ C 140 +466
仓位参考: Max Pain 165 ｜ Put Wall 140（+3.2%，弱）（OI 3.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 77.5%｜历史 Rank 75%（近端代理）｜IV/RV 1.16×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 62,788 股

11-27（MEDIUM △）仓位参考: Max Pain 150 ｜ Call Wall 140（+3.2%，弱）（OI 0.1k） ｜ Put Wall 130（-4.2%，弱）（OI 0.4k）

12-04（MEDIUM △）Top ΔOI: 135P +208
12-04（MEDIUM △）仓位参考: Max Pain 140 ｜ Call Wall 140（+3.2%）（OI 1.3k） ｜ Put Wall 135（-0.5%）（OI 1.7k）

📅 事件差分（观察，非因果）: 11-13（4D）ATM IV 86.3% vs 11-20 77.5%（差 +8.8pp）——覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-09/COIN_morning.json