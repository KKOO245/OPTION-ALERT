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
🟡 **事件差分**: 11-13 ATM IV 92.5% vs 11-20 81.8%（差 +10.6pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-20 120P ΔOI +3,235（距现价 -4.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-13 133C ΔOI +43,032 占该期限总 OI 12.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 124.58 → 收盘 125.59（+0.8%） ｜ 今日高 129.37 ｜ 低 122.48 ｜ 昨收 128.93 → 收盘 125.59（-2.6%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.70 | OI比 0.68 | ATM IV 92.5% | Skew 6.9pp | Term 0.80 | ExpMove ±7.8%（近端） | Rank 70%
量化视角： IV 中性（Rank 70%）｜期限结构倒挂（Term 0.80，近月 IV 高于远月）｜保护溢价显著（Skew 6.9pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.68）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.70×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.68×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（4D）±7.8% ｜ 11-20（11D）±11.7% ｜ 11-27（18D）±13.6% ｜ 12-04（25D）±15.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 34,463,708 | GEX Change vs 上次快照 2,851,605 | Flip: Primary Flip: 118.76（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 481 / LOW 160 / INVALID 341
结构观察区: Primary Flip 118.76（全链重定价，覆盖 100%）
Call Wall 135（弱结构｜现价低于该位 7.0%）
最近结构参考: Flip 119（现价高于该位 5.7%）
量化视角： 正 Gamma（3446万，无历史分位）｜正 Gamma 增强（+285万）｜现价位于 Flip 上方 5.75%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 132（MaxPain，仅结算参考） / 135（Call Wall，弱结构）。
• Gamma 区域：切换参考 119（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 133.0C — Vol 2,950 | 最新价 $2.05 | OI 132→43164 (ΔOI +43032张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增43032张（+32600.0% vs前日OI），连续性待观察（方向未知）
11-13 139.0C — Vol 1,078 | 最新价 $0.88 | OI 210→41153 (ΔOI +40943张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增40943张（+19496.7% vs前日OI），连续性待观察（方向未知）
11-13 80.0P — Vol 202 | 最新价 $0.07 | OI 5049→24055 (ΔOI +19006张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增19006张（+376.4% vs前日OI），连续性待观察（方向未知）
11-13 138.0C — Vol 1,414 | 最新价 $1.03 | OI 242→18425 (ΔOI +18183张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18183张（+7513.6% vs前日OI），连续性待观察（方向未知）
11-13 132.0C — Vol 3,097 | 最新价 $2.37 | OI 392→15768 (ΔOI +15376张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15376张（+3922.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 136,540 张（Put 19,006 / Call 117,534），跨 1 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +162.5k / P +54.1k ｜ Activity HIGH ｜ 4D
11-20  C +5.0k / P +6.9k ｜ Activity HIGH ｜ 11D
11-27  C +0.6k / P +2.3k ｜ Activity HIGH ｜ 18D
12-04  C +0.4k / P +2.4k ｜ Activity HIGH ｜ 25D

📆 11-13 Forward Structure
存量OI: C 213.8k / P 145.4k，今日变化ΔOI: C +162.5k / P +54.1k，平值价格ATM: C $4.78 / P $4.95 ｜ ATM IV 92.5%，净 delta 敞口 3.7M shares
Top ΔOI: C 133 +43,032 ｜ C 139 +40,943 ｜ P 80 +19,006
仓位参考: Max Pain 132 ｜ Call Wall 133（+5.9%，弱）（OI 43.2k） ｜ Put Wall 125（-0.5%，弱）（OI 5.8k）
量化解读： 存量 Call 重｜ATM IV 92.5%｜历史 Rank 70%（近端代理）｜IV/RV 1.24×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 3,658,712 股

📆 11-20 Forward Structure
存量OI: C 161.2k / P 147.1k，今日变化ΔOI: C +5.0k / P +6.9k，平值价格ATM: C $7.75 / P $6.95 ｜ ATM IV 81.8%，净 delta 敞口 12k shares
Top ΔOI: P 120 +3,235 ｜ C 145 +2,847 ｜ P 115 +931
仓位参考: Max Pain 135 ｜ Call Wall 135（+7.5%）（OI 43.1k） ｜ Put Wall 120（-4.5%，弱）（OI 10.5k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 81.8%｜历史 Rank 70%（近端代理）｜IV/RV 1.10×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 12,140 股

📆 11-27 Forward Structure
存量OI: C 14.4k / P 37.0k，今日变化ΔOI: C +0.6k / P +2.3k，平值价格ATM: C $9.41 / P $7.72 ｜ ATM IV 75.8%，净 delta 敞口 -50k shares
仓位参考: Max Pain 155 ｜ Call Wall 130（+3.5%，弱）（OI 0.9k） ｜ Put Wall 135（+7.5%，弱）（OI 2.6k）
量化解读： 存量 Put 重｜ATM IV 75.8%｜历史 Rank 70%（近端代理）｜IV/RV 1.02×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 50,128 股

📆 12-04 Forward Structure
存量OI: C 14.6k / P 19.4k，今日变化ΔOI: C +0.4k / P +2.4k，平值价格ATM: C $10.00 / P $9.04 ｜ ATM IV 75.3%，净 delta 敞口 -79k shares
Top ΔOI: P 85 +693 ｜ P 125 +190
仓位参考: Max Pain 150 ｜ Put Wall 135（+7.5%，弱）（OI 1.7k）
量化解读： 存量 Put 重｜ATM IV 75.3%｜历史 Rank 70%（近端代理）｜IV/RV 1.01×（近似）｜净 delta 敞口 负 78,890 股

📅 事件差分（观察，非因果）: 11-13（4D）ATM IV 92.5% vs 11-20 81.8%（差 +10.6pp）——覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-09/MSTR_evening.json