# 期权晚报 2026-09-03（快照 17:36 ET）

📊 市场环境

SPY $773.17 ｜ QQQ $717.67
VIX 14.32 ↓5.8%（5D -1.3%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 35.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 55.4 ｜ 前值 54.1　✅ 今日已公布
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 56 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **事件差分**: 09-04（1D）ATM IV 89.5% vs 09-11 66.4%（差 +23.0pp），覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **单日价格波动**: +3.6%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-04 195C ΔOI -3,697（距现价 +1.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 181.48 → 收盘 192.70（+6.2%） ｜ 今日高 195.85 ｜ 低 181.00
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.41 | OI比 0.54 | ATM IV 89.5% | Skew -10.3pp | Term 0.76 | ExpMove ±3.8%（近端） | Rank 78%
量化视角： IV 历史高位（Rank 78%，期权偏贵）｜期限结构倒挂（Term 0.76，近月 IV 高于远月）｜Put 保护异常便宜（Skew -10.3pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.54）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.41×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.54×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（1D）±3.8% ｜ 09-11（8D）±7.9% ｜ 09-18（15D）±11.2% ｜ 09-25（22D）±13.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 45,622,085 | GEX Change vs 上次快照 -1,823,006 | Flip: Primary Flip: 169.11（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 548 / LOW 187 / INVALID 325
结构观察区: Primary Flip 169.11（全链重定价，覆盖 99%）
Call Wall 200（弱结构｜现价低于该位 3.7%）
最近结构参考: Call Wall 200（现价低于该位 3.7%）
量化视角： 正 Gamma（4562万，无历史分位）｜正 Gamma 减弱（182万）｜现价位于 Flip 上方 13.95%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 169（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 180.0C — Vol 1,122 | 最新价 $15.20 | OI 535→5673 (ΔOI +5138张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5138张（+960.4% vs前日OI），连续性待观察（方向未知）
09-11 187.5C — Vol 346 | 最新价 $10.45 | OI 338→5111 (ΔOI +4773张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4773张（+1412.1% vs前日OI），连续性待观察（方向未知）
09-04 190.0C — Vol 9,739 | 最新价 $5.05 | OI 6530→7099 (ΔOI +569张) | ΔOI/Volume 5.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增569张（+8.7% vs前日OI），连续性待观察（方向未知）
09-18 190.0C — Vol 521 | 最新价 $12.16 | OI 3086→3589 (ΔOI +503张) | ΔOI/Volume 96.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增503张（+16.3% vs前日OI），连续性待观察（方向未知）
09-04 155.0P — Vol 317 | 最新价 $0.02 | OI 998→1428 (ΔOI +430张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增430张（+43.1% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 11,413 张（Put 430 / Call 10,983），跨 3 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C -5.2k / P +1.8k ｜ Activity HIGH ｜ 1D
09-11  C +10.9k / P +0.4k ｜ Activity HIGH ｜ 8D
09-18  C +0.8k / P +0.2k ｜ Activity MEDIUM △ ｜ 15D
09-25  C +87 / P +0.1k ｜ Activity MEDIUM △ ｜ 22D

📆 09-04 Forward Structure
存量OI:      C 75.6k / P 40.8k
今日变化ΔOI: C -5.2k / P +1.8k
平值价格ATM:  C 3.78 / P 3.46
隐含波动率 ATM IV:  89.5%
净 delta 敞口变化 ΔOI Δ Exposure*: -66k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 202 ｜ -4,027 ｜ $1.00 ｜ 名义 $-402.7k* ｜ +5.1%
C 195 ｜ -3,697 ｜ $2.71 ｜ 名义 $-1.00M* ｜ +1.2%
C 190 ｜ +569 ｜ $5.05 ｜ 名义 $287.3k* ｜ -1.4%
结构参考：190（-1.4%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 89.5%｜历史 Rank 78%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 65,996 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-11 Forward Structure
存量OI:      C 30.5k / P 15.1k
今日变化ΔOI: C +10.9k / P +0.4k
平值价格ATM:  C 7.80 / P 7.41
隐含波动率 ATM IV:  66.4%
净 delta 敞口变化 ΔOI Δ Exposure*: 748k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 180 ｜ +5,138 ｜ $15.20 ｜ 名义 $7.81M* ｜ -6.6%
C 187 ｜ +4,773 ｜ $10.45 ｜ 名义 $4.99M* ｜ -2.7%
C 177 ｜ +419 ｜ $16.40 ｜ 名义 $687.2k* ｜ -7.9%
结构参考：180（-6.6%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 66.4%｜历史 Rank 78%（近端代理）｜净 delta 敞口 正 748,161 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（MEDIUM △）Top ΔOI: 190C +503 ｜ 180P -352

09-25（MEDIUM △）Top ΔOI: 180C +15

📅 事件差分（观察，非因果）: 09-04（1D）ATM IV 89.5% vs 09-11 66.4%（差 +23.0pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-03/COIN_evening.json