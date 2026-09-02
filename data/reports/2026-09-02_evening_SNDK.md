# 期权晚报 2026-09-02（快照 18:14 ET）

📊 市场环境

SPY $765.16 ｜ QQQ $709.24
VIX 15.20 ↓7.0%（5D -1.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 待公布 ｜ 前值 54.1
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 58 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **事件差分**: 09-04 ATM IV 76.5% vs 09-11 66.3%（差 +10.2pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 1,531.62 → 收盘 1,553.40（+1.4%） ｜ 今日高 1587.86 ｜ 低 1509.24
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.79 | OI比 1.27 | ATM IV 76.5% | Skew -2.4pp | Term 0.91 | ExpMove ±4.5%（近端） | Rank 29%
量化视角： IV 中性（Rank 29%）｜期限结构正常（Term 0.91）｜Put 保护异常便宜（Skew -2.4pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.79×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.27×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-04（2D）±4.5% ｜ 09-11（9D）±8.1% ｜ 09-18（16D）±11.3% ｜ 09-25（23D）±17.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 3,220,771 | GEX Change vs 上次快照 3,953,132 | Flip: Primary Flip: 1527.62（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 2005 / LOW 523 / INVALID 982
结构观察区: Primary Flip 1527.62（全链重定价，覆盖 100%）
最近结构参考: Flip 1528（现价高于该位 1.7%）
量化视角： 正 Gamma（322万，无历史分位）｜由负转正（+395万）｜现价位于 Flip 上方 1.69%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 1528（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 1240.0P — Vol 3,796 | 最新价 $0.15 | OI 174→5404 (ΔOI +5230张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5230张（+3005.8% vs前日OI），连续性待观察（方向未知）
09-04 700.0P — Vol 34 | 最新价 $0.03 | OI 104→1058 (ΔOI +954张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增954张（+917.3% vs前日OI），连续性待观察（方向未知）
09-04 1100.0P — Vol 167 | 最新价 $0.11 | OI 673→1504 (ΔOI +831张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增831张（+123.5% vs前日OI），连续性待观察（方向未知）
09-04 1500.0P — Vol 2,968 | 最新价 $14.10 | OI 1346→1968 (ΔOI +622张) | ΔOI/Volume 21.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增622张（+46.2% vs前日OI），连续性待观察（方向未知）
09-04 1095.0P — Vol 15 | 最新价 $0.17 | OI 21→630 (ΔOI +609张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增609张（+2900.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 8,246 张（Put 8,246 / Call 0），跨 1 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜远端彩票/名义（4 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-11  C +0 / P +0 ｜ Activity LOW ｜ 9D
09-18  C +0 / P +0 ｜ Activity LOW ｜ 16D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 23D

📆 09-04 Forward Structure
存量OI:      C 45.7k / P 57.9k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 35.14 / P 35.40
隐含波动率 ATM IV:  76.5%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜ATM IV 76.5%｜历史 Rank 29%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

📅 事件差分（观察，非因果）: 09-04（2D）ATM IV 76.5% vs 09-11 66.3%（差 +10.2pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-02/SNDK_evening.json