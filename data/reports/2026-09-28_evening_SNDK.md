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


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 1,735.14 → 收盘 1,712.89（-1.3%） ｜ 今日高 1762.00 ｜ 低 1659.02 ｜ 昨收 1,777.80 → 收盘 1,712.89（-3.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.64 | OI比 0.98 | ATM IV 76.9% | Skew -4.1pp | Term 0.91 | ExpMove ±6.4%（近端） | Rank 33%
量化视角： IV 中性（Rank 33%）｜期限结构正常（Term 0.91）｜Put 保护异常便宜（Skew -4.1pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.64×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.98×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-02（4D）±6.4% ｜ 10-09（11D）±9.4% ｜ 10-16（18D）±12.2% ｜ 10-23（25D）±14.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 267,142 | GEX Change vs 上次快照 -367,439 | Flip: Primary Flip: 1707.79（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1728 / LOW 416 / INVALID 1122
结构观察区: Primary Flip 1707.79（全链重定价，覆盖 100%）
最近结构参考: Flip 1708（现价高于该位 0.3%）
量化视角： 正 Gamma（27万，无历史分位）｜正 Gamma 减弱（37万）｜现价位于 Flip 上方 0.30%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 1,700（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1708（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 2000.0C — Vol 7,297 | 最新价 $3.80 | OI 2348→4068 (ΔOI +1720张) | ΔOI/Volume 23.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1720张（+73.2% vs前日OI），连续性待观察（方向未知）
10-02 900.0P — Vol 5 | 最新价 $0.03 | OI 45→1727 (ΔOI +1682张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1682张（+3737.8% vs前日OI），连续性待观察（方向未知）
10-02 1000.0P — Vol 309 | 最新价 $0.03 | OI 253→1165 (ΔOI +912张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增912张（+360.5% vs前日OI），连续性待观察（方向未知）
10-02 1700.0P — Vol 2,181 | 最新价 $48.12 | OI 688→1209 (ΔOI +521张) | ΔOI/Volume 23.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增521张（+75.7% vs前日OI），连续性待观察（方向未知）
10-16 700.0P — Vol 2 | 最新价 $0.10 | OI 1099→1583 (ΔOI +484张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增484张（+44.0% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,319 张（Put 3,599 / Call 1,720），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $3M，买/卖方向不可观测）｜远端彩票/名义（3 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +5.7k / P +7.2k ｜ Activity HIGH ｜ 4D
10-09  C +0.9k / P +0.6k ｜ Activity HIGH ｜ 11D
10-16  C +0.1k / P +1.8k ｜ Activity HIGH ｜ 18D
10-23  C +0.4k / P +0.2k ｜ Activity HIGH ｜ 25D

📆 10-02 Forward Structure
存量OI: C 31.2k / P 30.7k，今日变化ΔOI: C +5.7k / P +7.2k，平值价格ATM: C $54.00 / P $55.90 ｜ ATM IV 76.9%，净 delta 敞口 -65k shares
Top ΔOI: C 2000 +1,720
仓位参考: Max Pain 1,700 ｜ Call Wall 1600（-6.6%，弱）（OI 1.8k） ｜ Put Wall 1700（-0.8%，弱）（OI 1.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 76.9%｜历史 Rank 33%（近端代理）｜IV/RV 1.05×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 65,199 股

📆 10-09 Forward Structure
存量OI: C 9.9k / P 8.4k，今日变化ΔOI: C +0.9k / P +0.6k，平值价格ATM: C $80.77 / P $79.70 ｜ ATM IV 67.5%，净 delta 敞口 9k shares
Top ΔOI: C 1850 +113 ｜ C 1800 +78 ｜ C 1900 +59
仓位参考: Max Pain 1,590 ｜ Put Wall 1550（-9.5%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 67.5%｜历史 Rank 33%（近端代理）｜IV/RV 0.92×（近似）｜净 delta 敞口 正 9,433 股

📆 10-16 Forward Structure
存量OI: C 36.5k / P 46.5k，今日变化ΔOI: C +0.1k / P +1.8k，平值价格ATM: C $105.00 / P $104.01 ｜ ATM IV 67.5%，净 delta 敞口 -31k shares
仓位参考: Max Pain 1,650 ｜ Call Wall 1800（+5.1%，弱）（OI 1.2k） ｜ Put Wall 1600（-6.6%，弱）（OI 1.5k）
量化解读： 存量 Put 重｜ATM IV 67.5%｜历史 Rank 33%（近端代理）｜IV/RV 0.92×（近似）｜净 delta 敞口 负 30,911 股

📆 10-23 Forward Structure
存量OI: C 4.1k / P 6.1k，今日变化ΔOI: C +0.4k / P +0.2k，平值价格ATM: C $122.47 / P $120.40 ｜ ATM IV 67.7%，净 delta 敞口 -981 shares
Top ΔOI: C 2150 +84 ｜ P 1970 +59
仓位参考: Max Pain 1,755 ｜ Call Wall 1840（+7.4%，弱）（OI 0.2k） ｜ Put Wall 1650（-3.7%，弱）（OI 0.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 67.7%｜历史 Rank 33%（近端代理）｜IV/RV 0.92×（近似）｜净 delta 敞口 负 981 股

📅 事件差分（观察，非因果）: 10-02（4D）ATM IV 76.9% vs 10-09 67.5%（差 +9.4pp）——覆盖 职位空缺(JOLTS) Job Openings、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-28/SNDK_evening.json