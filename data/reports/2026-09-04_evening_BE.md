# 期权晚报 2026-09-04（快照 16:40 ET）

📊 市场环境

SPY $770.19 ｜ QQQ $718.96
VIX 14.53 ↑1.5%（5D +0.7%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 41.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 56 ｜ 实际 162 ｜ 前值 21　✅ 今日已公布
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 4.1 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览
🟡 **单日价格波动**: +3.6%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **事件差分**: 09-11 ATM IV 106.0% vs 09-18 95.4%（差 +10.5pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 09-18 250C ΔOI -986（距现价 -1.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 236.82 → 收盘 252.87（+6.8%） ｜ 今日高 253.30 ｜ 低 235.74
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.02 | OI比 1.28 | ATM IV N/A | Skew -5.7pp | Term N/A | ExpMove ±11.7%（近端） | Rank — (历史不足)
量化视角： Put 保护异常便宜（Skew -5.7pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.02×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.28×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-11（7D）±11.7% ｜ 09-18（14D）±14.8% ｜ 09-25（21D）±18.1% ｜ 10-02（28D）±19.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 15,927,476 | GEX Change vs 上次快照 -3,333,695 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 78%（带内） ｜ IV 有效性: VALID 487 / LOW 50 / INVALID 261
结构观察区: NO_CROSS
Call Wall 250（现价高于该位 1.1%）
最近结构参考: Call Wall 250（现价高于该位 1.1%）
量化视角： 正 Gamma（1593万，无历史分位）｜正 Gamma 减弱（333万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 275.0C — Vol 3,860 | 最新价 $7.50 | OI 213→2451 (ΔOI +2238张) | ΔOI/Volume 58.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2238张（+1050.7% vs前日OI），连续性待观察（方向未知）
09-11 235.0C — Vol 2,513 | 最新价 $24.40 | OI 405→2390 (ΔOI +1985张) | ΔOI/Volume 79.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1985张（+490.1% vs前日OI），连续性待观察（方向未知）
09-04 145.0P — Vol 13 | 最新价 $0.01 | OI 1235→3194 (ΔOI +1959张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1959张（+158.6% vs前日OI），连续性待观察（方向未知）
09-11 272.5C — Vol 235 | 最新价 $8.19 | OI 16→1640 (ΔOI +1624张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1624张（+10150.0% vs前日OI），连续性待观察（方向未知）
09-11 135.0P — Vol 20 | 最新价 $0.06 | OI 131→1325 (ΔOI +1194张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1194张（+911.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 9,000 张（Put 3,153 / Call 5,847），跨 2 个期限｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +11.0k / P +5.0k ｜ Activity HIGH ｜ 7D
09-18  C -0.3k / P +1.4k ｜ Activity MEDIUM △ ｜ 14D
09-25  C -68 / P +0.4k ｜ Activity MEDIUM △ ｜ 21D
10-02  C +1.8k / P +0.9k ｜ Activity HIGH ｜ 28D

📆 09-11 Forward Structure
存量OI:      C 30.4k / P 25.7k
今日变化ΔOI: C +11.0k / P +5.0k
平值价格ATM:  C 15.15 / P 14.50
隐含波动率 ATM IV:  106.0%
净 delta 敞口变化 ΔOI Δ Exposure*: 432k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 275 ｜ +2,238 ｜ $7.50 ｜ 名义 $1.68M* ｜ +8.8%
C 235 ｜ +1,985 ｜ $24.40 ｜ 名义 $4.84M* ｜ -7.1%
C 225 ｜ -1,754 ｜ $31.48 ｜ 名义 $-5.52M* ｜ -11.0%
结构参考：275（+8.8%） / 235（-7.1%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 106.0%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 431,855 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（MEDIUM △）Top ΔOI: 300C -2,302 ｜ 225C +1,061

09-25（MEDIUM △）Top ΔOI: 195P +423

📆 10-02 Forward Structure
存量OI:      C 5.4k / P 6.4k
今日变化ΔOI: C +1.8k / P +0.9k
平值价格ATM:  C 23.92 / P 26.50
隐含波动率 ATM IV:  89.0%
净 delta 敞口变化 ΔOI Δ Exposure*: 45k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 300 ｜ +926 ｜ $11.03 ｜ 名义 $1.02M* ｜ +18.6%
P 190 ｜ +478 ｜ $2.86 ｜ 名义 $136.7k* ｜ -24.9%
C 260 ｜ +316 ｜ $22.25 ｜ 名义 $703.1k* ｜ +2.8%
结构参考：300（+18.6%） / 190（-24.9%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 89.0%｜净 delta 敞口 正 45,418 股（方向不可观测）——方向不可观测，观察点，非方向信号

📅 事件差分（观察，非因果）: 09-11（7D）ATM IV 106.0% vs 09-18 95.4%（差 +10.5pp）——覆盖 Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-04/BE_evening.json