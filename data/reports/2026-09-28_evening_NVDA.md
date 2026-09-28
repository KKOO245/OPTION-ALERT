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
🟡 **近现价集中开仓**: 09-30 232C ΔOI +6,682（距现价 +1.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 229.70 → 收盘 228.86（-0.4%） ｜ 今日高 233.21 ｜ 低 228.04 ｜ 昨收 225.07 → 收盘 228.86（+1.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.39 | OI比 0.75 | ATM IV 34.1% | Skew -10.9pp | Term 0.92 | ExpMove ±2.0%（近端） | Rank 17%
量化视角： IV 历史低位（Rank 17%，期权偏便宜）｜期限结构正常（Term 0.92）｜Put 保护异常便宜（Skew -10.9pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.75）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.39×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.75×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-30（2D）±2.0% ｜ 10-02（4D）±2.9% ｜ 10-05（7D）±3.2% ｜ 10-07（9D）±3.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 504,115,122 | GEX Change vs 上次快照 -79,414,959 | Flip: Primary Flip: 215.41（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 619 / LOW 201 / INVALID 562
结构观察区: Primary Flip 215.41（全链重定价，覆盖 95%）
Call Wall 230（弱结构｜现价低于该位 0.5%）
最近结构参考: Call Wall 230（现价低于该位 0.5%）
量化视角： 正 Gamma（5.04亿，无历史分位）｜正 Gamma 减弱（7941万）｜现价位于 Flip 上方 6.24%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 222（MaxPain，仅结算参考）；上方 230（Call Wall，弱结构）。
• Gamma 区域：切换参考 215（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 227.5C — Vol 8,295 | 最新价 $4.10 | OI 6052→75663 (ΔOI +69611张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增69611张（+1150.2% vs前日OI），连续性待观察（方向未知）
10-02 232.5C — Vol 65,737 | 最新价 $1.80 | OI 6132→45334 (ΔOI +39202张) | ΔOI/Volume 59.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增39202张（+639.3% vs前日OI），连续性待观察（方向未知）
10-02 235.0C — Vol 65,844 | 最新价 $1.10 | OI 26904→51138 (ΔOI +24234张) | ΔOI/Volume 36.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增24234张（+90.1% vs前日OI），连续性待观察（方向未知）
10-02 215.0P — Vol 11,238 | 最新价 $0.35 | OI 11328→25950 (ΔOI +14622张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14622张（+129.1% vs前日OI），连续性待观察（方向未知）
10-02 115.0P — Vol 1,000 | 最新价 $0.01 | OI 954→14626 (ΔOI +13672张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13672张（+1433.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 161,341 张（Put 28,294 / Call 133,047），跨 1 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-30  C +18.1k / P +16.2k ｜ Activity HIGH ｜ 2D
10-02  C +158.1k / P +88.0k ｜ Activity HIGH ｜ 4D
10-05  C +4.1k / P +2.5k ｜ Activity HIGH ｜ 7D
10-07  C +0.8k / P +0.5k ｜ Activity HIGH ｜ 9D

📆 09-30 Forward Structure
存量OI: C 55.3k / P 41.4k，今日变化ΔOI: C +18.1k / P +16.2k，平值价格ATM: C $1.77 / P $2.85 ｜ ATM IV 33.3%，净 delta 敞口 552k shares
Top ΔOI: C 232 +6,682 ｜ C 235 +3,346
仓位参考: Max Pain 222 ｜ Call Wall 230（+0.5%，弱）（OI 11.2k） ｜ Put Wall 212.5（-7.1%，弱）（OI 5.3k）
量化解读： 存量 Call 重｜ATM IV 33.3%｜历史 Rank 17%（近端代理）｜IV/RV 1.34×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 552,239 股

📆 10-02 Forward Structure
存量OI: C 377.8k / P 337.0k，今日变化ΔOI: C +158.1k / P +88.0k，平值价格ATM: C $2.84 / P $3.85 ｜ ATM IV 34.1%，净 delta 敞口 6.3M shares
Top ΔOI: C 227 +69,611 ｜ C 232 +39,202 ｜ C 235 +24,234
仓位参考: Max Pain 222 ｜ Call Wall 227.5（-0.6%，弱）（OI 75.7k） ｜ Put Wall 215（-6.1%，弱）（OI 25.9k）
量化解读： 存量两侧均衡｜ATM IV 34.1%｜历史 Rank 17%（近端代理）｜IV/RV 1.37×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 6,296,331 股

📆 10-05 Forward Structure
存量OI: C 19.2k / P 8.3k，今日变化ΔOI: C +4.1k / P +2.5k，平值价格ATM: C $3.30 / P $4.05 ｜ ATM IV 29.1%，净 delta 敞口 144k shares
Top ΔOI: C 225 +762 ｜ P 220 +736 ｜ P 215 +734
仓位参考: Max Pain 222 ｜ Call Wall 230（+0.5%）（OI 4.3k） ｜ Put Wall 222.5（-2.8%，弱）（OI 1.7k）
量化解读： 存量 Call 重｜ATM IV 29.1%｜历史 Rank 17%（近端代理）｜IV/RV 1.17×（近似）｜净 delta 敞口 正 144,171 股

📆 10-07 Forward Structure
存量OI: C 1.4k / P 0.8k，今日变化ΔOI: C +0.8k / P +0.5k，平值价格ATM: C $4.05 / P $4.90 ｜ ATM IV 30.3%，净 delta 敞口 27k shares
Top ΔOI: P 215 +160 ｜ C 225 +146 ｜ C 230 +107
仓位参考: Max Pain 220 ｜ Call Wall 225（-1.7%，弱）（OI 0.3k） ｜ Put Wall 215（-6.1%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 30.3%｜历史 Rank 17%（近端代理）｜IV/RV 1.22×（近似）｜净 delta 敞口 正 26,894 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-28/NVDA_evening.json