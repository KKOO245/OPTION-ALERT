# 期权晚报 2026-09-28（快照 16:40 ET）

📊 市场环境

SPY $765.61 ｜ QQQ $736.53
VIX 16.07 ↑8.1%（5D +8.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-28

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-29 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.24 ｜ 实际 待公布 ｜ 前值 7.271
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 待公布 ｜ 前值 2.1
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 54.9 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 84 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 282.51 → 收盘 262.87（-7.0%） ｜ 今日高 286.26 ｜ 低 259.46 ｜ 昨收 288.70 → 收盘 262.87（-8.9%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.73 | OI比 0.98 | ATM IV 83.7% | Skew -2.1pp | Term 1.00 | ExpMove ±7.0%（近端） | Rank 42%
量化视角： IV 中性（Rank 42%）｜期限结构正常（Term 1.00）｜Put 保护异常便宜（Skew -2.1pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.73×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.98×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-02（4D）±7.0% ｜ 10-09（11D）±10.0% ｜ 10-16（18D）±13.0% ｜ 10-23（25D）±15.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,483,411 | GEX Change vs 上次快照 -2,563,123 | Flip: Primary Flip: 257.61（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 570 / LOW 76 / INVALID 202
结构观察区: Primary Flip 257.61（全链重定价，覆盖 100%）
Call Wall 270（弱结构｜现价低于该位 2.6%）
最近结构参考: Flip 258（现价高于该位 2.0%）
量化视角： 正 Gamma（248万，无历史分位）｜正 Gamma 减弱（256万）｜现价位于 Flip 上方 2.04%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 270（MaxPain，仅结算参考） / 270（Call Wall，弱结构）。
• Gamma 区域：切换参考 258（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 150.0P — Vol 23 | 最新价 $0.07 | OI 1632→3922 (ΔOI +2290张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2290张（+140.3% vs前日OI），连续性待观察（方向未知）
10-02 290.0C — Vol 4,275 | 最新价 $1.82 | OI 1231→2416 (ΔOI +1185张) | ΔOI/Volume 27.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1185张（+96.3% vs前日OI），连续性待观察（方向未知）
10-02 280.0P — Vol 354 | 最新价 $20.41 | OI 182→1337 (ΔOI +1155张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1155张（+634.6% vs前日OI），连续性待观察（方向未知）
10-02 210.0P — Vol 311 | 最新价 $0.11 | OI 812→1926 (ΔOI +1114张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1114张（+137.2% vs前日OI），连续性待观察（方向未知）
10-09 350.0C — Vol 940 | 最新价 $0.44 | OI 124→1077 (ΔOI +953张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增953张（+768.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 6,697 张（Put 4,559 / Call 2,138），跨 3 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +9.1k / P +6.3k ｜ Activity HIGH ｜ 4D
10-09  C +2.1k / P +0.5k ｜ Activity HIGH ｜ 11D
10-16  C +0.3k / P +1.6k ｜ Activity HIGH ｜ 18D
10-23  C +27 / P -0.2k ｜ Activity MEDIUM △ ｜ 25D

📆 10-02 Forward Structure
存量OI: C 34.4k / P 33.7k，今日变化ΔOI: C +9.1k / P +6.3k，平值价格ATM: C $9.60 / P $8.90 ｜ ATM IV 83.7%，净 delta 敞口 -240k shares
Top ΔOI: C 290 +1,185 ｜ P 280 +1,155
仓位参考: Max Pain 270 ｜ Call Wall 270（+2.7%，弱）（OI 3.0k） ｜ Put Wall 260（-1.1%，弱）（OI 2.2k）
量化解读： 存量两侧均衡｜ATM IV 83.7%｜历史 Rank 42%（近端代理）｜IV/RV 1.10×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 239,890 股

📆 10-09 Forward Structure
存量OI: C 7.6k / P 11.0k，今日变化ΔOI: C +2.1k / P +0.5k，平值价格ATM: C $13.60 / P $12.65 ｜ ATM IV 77.0%，净 delta 敞口 -14k shares
Top ΔOI: P 240 -180
仓位参考: Max Pain 265 ｜ Call Wall 275（+4.6%，弱）（OI 0.3k） ｜ Put Wall 240（-8.7%）（OI 1.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 77.0%｜历史 Rank 42%（近端代理）｜IV/RV 1.01×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 13,505 股

📆 10-16 Forward Structure
存量OI: C 68.1k / P 74.5k，今日变化ΔOI: C +0.3k / P +1.6k，平值价格ATM: C $17.95 / P $16.17 ｜ ATM IV 74.8%，净 delta 敞口 -67k shares
Top ΔOI: C 300 -564 ｜ C 315 +522
仓位参考: Max Pain 258 ｜ Call Wall 280（+6.5%，弱）（OI 8.3k） ｜ Put Wall 260（-1.1%，弱）（OI 3.8k）
量化解读： 存量两侧均衡｜ATM IV 74.8%｜历史 Rank 42%（近端代理）｜IV/RV 0.99×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 67,309 股

10-23（MEDIUM △）Top ΔOI: 300C -466
10-23（MEDIUM △）仓位参考: Max Pain 250 ｜ Call Wall 270（+2.7%，弱）（OI 0.7k） ｜ Put Wall 240（-8.7%，弱）（OI 1.4k）

📅 事件差分（观察，非因果）: 10-02（4D）ATM IV 83.7% vs 10-09 77.0%（差 +6.7pp）——覆盖 职位空缺(JOLTS) Job Openings、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-28/BE_evening.json