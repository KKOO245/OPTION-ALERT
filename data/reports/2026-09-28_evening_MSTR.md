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

🔍 重点速览
🟡 **近现价集中开仓**: 10-02 162C ΔOI +29,297（距现价 +3.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 157.90 → 收盘 157.14（-0.5%） ｜ 今日高 161.72 ｜ 低 155.06 ｜ 昨收 158.61 → 收盘 157.14（-0.9%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.72 | OI比 0.82 | ATM IV 74.5% | Skew -6.4pp | Term 0.90 | ExpMove ±6.2%（近端） | Rank 36%
量化视角： IV 中性（Rank 36%）｜期限结构倒挂（Term 0.90，近月 IV 高于远月）｜Put 保护异常便宜（Skew -6.4pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.82）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.72×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.82×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-02（4D）±6.2% ｜ 10-09（11D）±9.2% ｜ 10-16（18D）±11.6% ｜ 10-23（25D）±13.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 51,346,502 | GEX Change vs 上次快照 -8,945,265 | Flip: Primary Flip: 142.73（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 796 / LOW 51 / INVALID 185
结构观察区: Primary Flip 142.73（全链重定价，覆盖 100%）
Call Wall 170（弱结构｜现价低于该位 7.6%）
最近结构参考: Call Wall 170（现价低于该位 7.6%）
量化视角： 正 Gamma（5135万，无历史分位）｜正 Gamma 减弱（895万）｜现价位于 Flip 上方 10.10%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 155（MaxPain，仅结算参考）；上方 170（Call Wall，弱结构）。
• Gamma 区域：切换参考 143（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 170.0C — Vol 6,791 | 最新价 $1.36 | OI 5891→44186 (ΔOI +38295张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增38295张（+650.1% vs前日OI），连续性待观察（方向未知）
10-02 162.5C — Vol 2,832 | 最新价 $2.90 | OI 663→29960 (ΔOI +29297张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增29297张（+4418.9% vs前日OI），连续性待观察（方向未知）
10-02 165.0C — Vol 7,025 | 最新价 $2.29 | OI 2079→30103 (ΔOI +28024张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增28024张（+1348.0% vs前日OI），连续性待观察（方向未知）
10-02 100.0P — Vol 172 | 最新价 $0.02 | OI 5279→28774 (ΔOI +23495张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增23495张（+445.1% vs前日OI），连续性待观察（方向未知）
10-02 172.5C — Vol 1,473 | 最新价 $1.10 | OI 4624→21572 (ΔOI +16948张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16948张（+366.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 136,059 张（Put 23,495 / Call 112,564），跨 1 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +131.2k / P +68.5k ｜ Activity HIGH ｜ 4D
10-09  C +6.4k / P +2.4k ｜ Activity HIGH ｜ 11D
10-16  C +7.6k / P -0.9k ｜ Activity HIGH ｜ 18D
10-23  C +0.9k / P +3.2k ｜ Activity HIGH ｜ 25D

📆 10-02 Forward Structure
存量OI: C 229.9k / P 187.6k，今日变化ΔOI: C +131.2k / P +68.5k，平值价格ATM: C $4.80 / P $5.00 ｜ ATM IV 74.5%，净 delta 敞口 3.3M shares
Top ΔOI: C 170 +38,295 ｜ C 162 +29,297 ｜ C 165 +28,024
仓位参考: Max Pain 155 ｜ Call Wall 170（+8.2%，弱）（OI 44.2k） ｜ Put Wall 150（-4.5%，弱）（OI 12.6k）
量化解读： 存量 Call 重｜ATM IV 74.5%｜历史 Rank 36%（近端代理）｜IV/RV 0.78×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 3,292,177 股

📆 10-09 Forward Structure
存量OI: C 37.8k / P 50.0k，今日变化ΔOI: C +6.4k / P +2.4k，平值价格ATM: C $7.20 / P $7.30 ｜ ATM IV 66.9%，净 delta 敞口 251k shares
Top ΔOI: C 165 +3,654 ｜ C 160 -2,062 ｜ C 144 +1,569
仓位参考: Max Pain 144 ｜ Call Wall 144（-8.4%，弱）（OI 5.4k） ｜ Put Wall 155（-1.4%，弱）（OI 1.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 66.9%｜历史 Rank 36%（近端代理）｜IV/RV 0.70×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 250,716 股

📆 10-16 Forward Structure
存量OI: C 171.8k / P 141.4k，今日变化ΔOI: C +7.6k / P -0.9k，平值价格ATM: C $9.08 / P $9.14 ｜ ATM IV 65.7%，净 delta 敞口 30k shares
Top ΔOI: P 115 -2,439 ｜ C 190 +811
仓位参考: Max Pain 120 ｜ Call Wall 155（-1.4%，弱）（OI 10.4k） ｜ Put Wall 160（+1.8%，弱）（OI 4.4k）
量化解读： 存量 Call 重｜ATM IV 65.7%｜历史 Rank 36%（近端代理）｜IV/RV 0.69×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 30,425 股

📆 10-23 Forward Structure
存量OI: C 14.3k / P 20.8k，今日变化ΔOI: C +0.9k / P +3.2k，平值价格ATM: C $10.50 / P $10.70 ｜ ATM IV 65.2%，净 delta 敞口 -29k shares
Top ΔOI: C 162 +380
仓位参考: Max Pain 155 ｜ Call Wall 170（+8.2%，弱）（OI 1.0k） ｜ Put Wall 155（-1.4%，弱）（OI 1.7k）
量化解读： 存量 Put 重｜ATM IV 65.2%｜历史 Rank 36%（近端代理）｜IV/RV 0.69×（近似）｜净 delta 敞口 负 29,248 股

📅 事件差分（观察，非因果）: 10-02（4D）ATM IV 74.5% vs 10-09 66.9%（差 +7.6pp）——覆盖 职位空缺(JOLTS) Job Openings、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-28/MSTR_evening.json