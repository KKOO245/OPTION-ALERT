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


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 410.89 → 收盘 416.23（+1.3%） ｜ 今日高 418.10 ｜ 低 407.34 ｜ 昨收 399.05 → 收盘 416.23（+4.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.14 | OI比 0.60 | ATM IV 40.9% | Skew 3.6pp | Term 0.90 | ExpMove ±3.4%（近端） | Rank 53%
量化视角： IV 中性（Rank 53%）｜期限结构正常（Term 0.90）｜保护溢价中性（Skew 3.6pp）｜存量 Call 偏重（OI比 0.60）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.14×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.60×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（4D）±3.4% ｜ 12-04（11D）±4.5% ｜ 12-11（18D）±7.4% ｜ 12-18（25D）±8.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,069,198 | GEX Change vs 上次快照 346,845 | Flip: Primary Flip: 398.51（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 243 / LOW 170 / INVALID 571
结构观察区: Primary Flip 398.51（全链重定价，覆盖 96%）
Call Wall 400（弱结构｜现价高于该位 4.1%）
最近结构参考: Call Wall 400（现价高于该位 4.1%）
量化视角： 正 Gamma（107万，无历史分位）｜正 Gamma 增强（+35万）｜现价位于 Flip 上方 4.45%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 410（MaxPain，仅结算参考） / 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 399（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 410.0C — Vol 2（Yahoo补） | 最新价 $4.80 | OI 14→177 (ΔOI +163张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增163张（+1164.3% vs前日OI），值得跟踪（方向未知）
11-27 407.5C — Vol 89（Yahoo补） | 最新价 $8.12 | OI 0→89 (ΔOI +89张) | ΔOI/Volume 100.0% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增89张（前日OI缺失），值得跟踪（方向未知）
11-27 430.0C — Vol 23 | 最新价 $1.35 | OI 66→131 (ΔOI +65张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增65张（+98.5% vs前日OI），值得跟踪（方向未知）
12-18 405.0C — Vol 5（Yahoo补） | 最新价 $14.80 | OI 97→159 (ΔOI +62张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增62张（+63.9% vs前日OI），值得跟踪（方向未知）
12-18 380.0P — Vol 17（Yahoo补） | 最新价 $6.60 | OI 369→423 (ΔOI +54张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增54张（+14.6% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 433 张（Put 54 / Call 379），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-27  C +0.4k / P +25 ｜ Activity MEDIUM △ ｜ 4D
12-04  C +82 / P +70 ｜ Activity MEDIUM △ ｜ 11D
12-11  C +21 / P +29 ｜ Activity MEDIUM △ ｜ 18D
12-18  C +0.1k / P +32 ｜ Activity LOW ｜ 25D

📆 11-27 Forward Structure
存量OI: C 1.3k / P 0.8k，今日变化ΔOI: C +0.4k / P +25，平值价格ATM: C $4.67 / P $9.63 ｜ ATM IV 40.9%，净 delta 敞口 19k shares
Top ΔOI: C 410 +163 ｜ C 407 +89 ｜ C 430 +65
仓位参考: Max Pain 410 ｜ Call Wall 410（-1.5%，弱）（OI 0.2k） ｜ Put Wall 395（-5.1%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 40.9%｜历史 Rank 53%（近端代理）｜IV/RV 0.90×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 18,861 股

12-04（MEDIUM △）Top ΔOI: 402C +24 ｜ 405C +22
12-04（MEDIUM △）仓位参考: Max Pain 420 ｜ Call Wall 450（+8.1%，弱）（OI 46） ｜ Put Wall 405（-2.7%，弱）（OI 29）

12-11（MEDIUM △）Top ΔOI: 435C +19 ｜ 405P +11
12-11（MEDIUM △）仓位参考: Max Pain 435 ｜ Call Wall 450（+8.1%）（OI 0.1k） ｜ Put Wall 435（+4.5%）（OI 36）

12-18（Activity LOW）仓位参考: Max Pain 410 ｜ Call Wall 400（-3.9%，弱）（OI 1.5k） ｜ Put Wall 420（+0.9%，弱）（OI 0.6k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-23/ISRG_evening.json