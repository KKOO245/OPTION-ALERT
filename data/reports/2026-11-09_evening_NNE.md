# 期权晚报 2026-11-09（快照 16:40 ET）

📊 市场环境

SPY $752.69 ｜ QQQ $679.35
VIX 19.92 ↓22.3%（5D -5.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.7（fear）
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
🟡 **近现价集中开仓**: 11-13 12C ΔOI +121（距现价 -3.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 12-04 13C ΔOI +101 占该期限总 OI 16.4%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 11.20 → 收盘 12.48（+11.4%） ｜ 今日高 12.86 ｜ 低 10.96 ｜ 昨收 11.11 → 收盘 12.48（+12.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.35 | OI比 0.80 | ATM IV 90.7% | Skew 14.9pp | Term 0.91 | ExpMove ±8.4%（近端） | Rank 26%
量化视角： IV 中性（Rank 26%）｜期限结构正常（Term 0.91）｜保护溢价显著（Skew 14.9pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.80）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.35×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.80×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（4D）±8.4% ｜ 11-20（11D）±11.7% ｜ 11-27（18D）±31.4% ｜ 12-04（25D）±17.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,423,003 | GEX Change vs 上次快照 423,549 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 163 / LOW 65 / INVALID 158
结构观察区: NO_CROSS
Call Wall 12（现价低于该位 0.2%）
最近结构参考: Call Wall 12（现价低于该位 0.2%）
量化视角： 正 Gamma（142万，无历史分位）｜正 Gamma 增强（+42万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 12（MaxPain，仅结算参考）；上方 12（Call Wall）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 12.0C — Vol 25 | 最新价 $1.25 | OI 10→680 (ΔOI +670张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增670张（+6700.0% vs前日OI），连续性待观察（方向未知）
11-20 10.0C — Vol 5 | 最新价 $2.29 | OI 59→224 (ΔOI +165张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增165张（+279.7% vs前日OI），值得跟踪（方向未知）
11-13 12.0C — Vol 275 | 最新价 $1.00 | OI 135→256 (ΔOI +121张) | ΔOI/Volume 44.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增121张（+89.6% vs前日OI），连续性待观察（方向未知）
12-04 13.5C — Vol 5 | 最新价 $0.51 | OI 25→126 (ΔOI +101张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增101张（+404.0% vs前日OI），值得跟踪（方向未知）
11-13 11.0P — Vol 212 | 最新价 $0.08 | OI 239→308 (ΔOI +69张) | ΔOI/Volume 32.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增69张（+28.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,126 张（Put 69 / Call 1,057），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +0.2k / P +0.1k ｜ Activity MEDIUM △ ｜ 4D
11-20  C +1.0k / P +44 ｜ Activity HIGH ｜ 11D
11-27  C +22 / P +9 ｜ Activity MEDIUM △ ｜ 18D
12-04  C +0.1k / P +3 ｜ Activity HIGH ｜ 25D

📆 11-13 Forward Structure
存量OI: C 1.7k / P 1.3k，今日变化ΔOI: C +0.2k / P +0.1k，平值价格ATM: C $0.60 / P $0.45 ｜ ATM IV 90.7%，净 delta 敞口 15k shares
Top ΔOI: C 12 +121
仓位参考: Max Pain 12 ｜ Call Wall 12（-3.8%，弱）（OI 0.3k） ｜ Put Wall 13（+4.2%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 90.7%｜历史 Rank 26%（近端代理）｜IV/RV 1.06×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 15,307 股

📆 11-20 Forward Structure
存量OI: C 5.3k / P 1.9k，今日变化ΔOI: C +1.0k / P +44，平值价格ATM: C $0.71 / P $0.75 ｜ ATM IV 88.2%，净 delta 敞口 67k shares
Top ΔOI: C 12 +670
仓位参考: Max Pain 12 ｜ Call Wall 12（-3.8%，弱）（OI 0.7k） ｜ Put Wall 12（-3.8%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 88.2%｜历史 Rank 26%（近端代理）｜IV/RV 1.03×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 67,425 股

11-27（MEDIUM △）Top ΔOI: 12C +12 ｜ 11C +5
11-27（MEDIUM △）仓位参考: Max Pain 12 ｜ Call Wall 12.5（+0.2%）（OI 4.0k） ｜ Put Wall 12.5（+0.2%）（OI 0.3k）

📆 12-04 Forward Structure
存量OI: C 0.3k / P 0.4k，今日变化ΔOI: C +0.1k / P +3，平值价格ATM: C $1.15 / P $1.05 ｜ ATM IV 78.8%，净 delta 敞口 5k shares
Top ΔOI: C 13 +101 ｜ C 11 +11
仓位参考: Max Pain 14 ｜ Call Wall 13.5（+8.2%）（OI 0.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 78.8%｜历史 Rank 26%（近端代理）｜IV/RV 0.92×（近似）｜净 delta 敞口 正 5,428 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-09/NNE_evening.json