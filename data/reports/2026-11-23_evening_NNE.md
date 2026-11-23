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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 10.23 → 收盘 9.47（-7.4%） ｜ 今日高 10.38 ｜ 低 9.41 ｜ 昨收 9.10 → 收盘 9.47（+4.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.40 | OI比 0.15 | ATM IV 110.2% | Skew 17.0pp | Term 0.89 | ExpMove ±8.8%（近端） | Rank 59%
量化视角： IV 中性（Rank 59%）｜期限结构倒挂（Term 0.89，近月 IV 高于远月）｜保护溢价显著（Skew 17.0pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.15）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.40×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.15×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（4D）±8.8% ｜ 12-04（11D）±15.6% ｜ 12-11（18D）±23.0% ｜ 12-18（25D）±0.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 183,439 | GEX Change vs 上次快照 -179,059 | Flip: Primary Flip: 8.61（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 102 / LOW 61 / INVALID 217
结构观察区: Primary Flip 8.61（全链重定价，覆盖 100%）
Put Wall 10（弱结构｜现价低于该位 5.3%）
最近结构参考: Put Wall 10（现价低于该位 5.3%）
量化视角： 正 Gamma（18万，无历史分位）｜正 Gamma 减弱（18万）｜现价位于 Flip 上方 9.95%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 10（Put Wall，弱结构） / 12（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 9（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 12.0P — Vol 30（Yahoo补） | 最新价 $2.20 | OI 48→78 (ΔOI +30张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增30张（+62.5% vs前日OI），连续性待观察（方向未知）
11-27 10.0C — Vol 30 | 最新价 $0.39 | OI 19→48 (ΔOI +29张) | ΔOI/Volume 96.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增29张（+152.6% vs前日OI），连续性待观察（方向未知）
12-24 11.5P — Vol 2（Yahoo补） | 最新价 $2.66 | OI 1→27 (ΔOI +26张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增26张（+2600.0% vs前日OI），值得跟踪（方向未知）
12-18 12.0P — Vol 21（Yahoo补） | 最新价 $3.06 | OI 47→68 (ΔOI +21张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21张（+44.7% vs前日OI），连续性待观察（方向未知）
12-11 11.0P — Vol 10（Yahoo补） | 最新价 $2.17 | OI 14→31 (ΔOI +17张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增17张（+121.4% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 123 张（Put 94 / Call 29），跨 4 个期限｜有实质成本保护 4 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-27  C +56 / P -4 ｜ Activity MEDIUM △ ｜ 4D
12-04  C +9 / P -68 ｜ Activity HIGH ｜ 11D
12-11  C -7 / P +18 ｜ Activity MEDIUM △ ｜ 18D
12-18  C +3 / P +22 ｜ Activity MEDIUM △ ｜ 25D

📆 11-27 Forward Structure
存量OI: C 5.1k / P 0.8k，今日变化ΔOI: C +56 / P -4，平值价格ATM: C $0.60 / P $0.23 ｜ ATM IV 110.2%，净 delta 敞口 4k shares
Top ΔOI: C 10 +29
仓位参考: Max Pain 12 ｜ Put Wall 10（+5.6%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 110.2%｜历史 Rank 59%（近端代理）｜IV/RV 1.07×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 4,221 股

📆 12-04 Forward Structure
存量OI: C 0.8k / P 0.5k，今日变化ΔOI: C +9 / P -68，平值价格ATM: C $1.05 / P $0.43 ｜ ATM IV 108.8%，净 delta 敞口 5k shares
Top ΔOI: P 10 -49 ｜ C 9 +10
仓位参考: Max Pain 11 ｜ Put Wall 9.5（+0.3%）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 108.8%｜历史 Rank 59%（近端代理）｜IV/RV 1.05×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 4,963 股

12-11（MEDIUM △）仓位参考: Max Pain 11 ｜ Call Wall 10（+5.6%，弱）（OI 34） ｜ Put Wall 9（-5.0%，弱）（OI 8）

12-18（MEDIUM △）Top ΔOI: 9C +5 ｜ 10C +5
12-18（MEDIUM △）仓位参考: Max Pain 11 ｜ Call Wall 10（+5.6%，弱）（OI 65） ｜ Put Wall 9（-5.0%，弱）（OI 0.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-23/NNE_evening.json