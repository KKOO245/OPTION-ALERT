# 期权晨报 2026-09-01（快照 10:20 ET）

📊 市场环境

SPY $763.56 ｜ QQQ $709.23
VIX 15.71 ↑5.3%（5D +1.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 46.4（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-01 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.3 ｜ 实际 7.271 ｜ 前值 7.182　✅ 今日已公布
- 周二 09-01 10:00　【高】ISM 制造业 PMI　预测 55.2 ｜ 实际 54.6 ｜ 前值 55.6　✅ 今日已公布
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 待公布 ｜ 前值 54.1
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 58 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **Vol Regime 升档**: LOW → NORMAL（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **单日价格波动**: -2.8%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **事件差分**: 09-04 ATM IV 84.0% vs 09-11 73.1%（差 +11.0pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 17.82 → 今开 17.12（-3.9%） | 较昨收变动（含盘初走势） ｜ 今日高 17.80 ｜ 低 16.96

Options: P/C成交量 0.44 | OI比 0.30 | ATM IV 84.0% | Skew -7.4pp | Term 0.97 | ExpMove ±7.2%（近端） | Rank 3%
量化视角： IV 历史低位（Rank 3%，期权偏便宜）｜期限结构正常（Term 0.97）｜Put 保护异常便宜（Skew -7.4pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.30）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.44×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.30×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（3D）±7.2% ｜ 09-11（10D）±10.6% ｜ 09-18（17D）±15.4% ｜ 09-25（24D）±17.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,610,796 | GEX Change vs 上次快照 -3,407,131 | Flip: Primary Flip: 17.05（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 265 / LOW 100 / INVALID 163
结构观察区: Primary Flip 17.05（全链重定价，覆盖 100%）
最近结构参考: Flip 17（现价高于该位 1.6%）
量化视角： 正 Gamma（161万，无历史分位）｜正 Gamma 减弱（341万）｜现价位于 Flip 上方 1.62%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 17（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 18.0P — Vol 3,670 | 最新价 $1.34 | OI 5178→6452 (ΔOI +1274张) | ΔOI/Volume 34.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1274张（+24.6% vs前日OI），连续性待观察（方向未知）
09-11 20.5C — Vol 843 | 最新价 $0.22 | OI 243→1052 (ΔOI +809张) | ΔOI/Volume 96.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增809张（+332.9% vs前日OI），连续性待观察（方向未知）
09-11 21.5C — Vol 804 | 最新价 $0.14 | OI 74→849 (ΔOI +775张) | ΔOI/Volume 96.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增775张（+1047.3% vs前日OI），连续性待观察（方向未知）
09-18 21.5C — Vol 814 | 最新价 $0.28 | OI 771→1492 (ΔOI +721张) | ΔOI/Volume 88.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增721张（+93.5% vs前日OI），连续性待观察（方向未知）
09-18 22.5C — Vol 808 | 最新价 $0.16 | OI 139→838 (ΔOI +699张) | ΔOI/Volume 86.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增699张（+502.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,278 张（Put 1,274 / Call 3,004），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C +3.5k / P +1.6k ｜ Activity HIGH ｜ 3D
09-11  C +2.0k / P +0.7k ｜ Activity HIGH ｜ 10D
09-18  C +2.4k / P +1.6k ｜ Activity HIGH ｜ 17D
09-25  C +1.0k / P +0.3k ｜ Activity HIGH ｜ 24D

📆 09-04 Forward Structure
存量OI:      C 32.0k / P 9.7k
今日变化ΔOI: C +3.5k / P +1.6k
平值价格ATM:  C 0.80 / P 0.45
隐含波动率 ATM IV:  84.0%
净 delta 敞口变化 ΔOI Δ Exposure*: 26k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 16 ｜ +530 ｜ $0.17 ｜ 名义 $9.0k* ｜ -4.8%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：16（-4.8%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 84.0%｜历史 Rank 3%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 25,536 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-11 Forward Structure
存量OI:      C 11.9k / P 2.9k
今日变化ΔOI: C +2.0k / P +0.7k
平值价格ATM:  C 1.03 / P 0.81
隐含波动率 ATM IV:  73.1%
净 delta 敞口变化 ΔOI Δ Exposure*: 11k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 19 ｜ +285 ｜ $1.75 ｜ 名义 $49.9k* ｜ +9.7%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：19（+9.7%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 73.1%｜历史 Rank 3%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 10,679 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 111.4k / P 65.5k
今日变化ΔOI: C +2.4k / P +1.6k
平值价格ATM:  C 1.60 / P 1.07
隐含波动率 ATM IV:  81.5%
净 delta 敞口变化 ΔOI Δ Exposure*: -16k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 18 ｜ +1,274 ｜ $1.34 ｜ 名义 $170.7k* ｜ +3.9%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：18（+3.9%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 81.5%｜历史 Rank 3%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 15,788 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-25 Forward Structure
存量OI:      C 8.6k / P 3.0k
今日变化ΔOI: C +1.0k / P +0.3k
平值价格ATM:  C 1.70 / P 1.35
隐含波动率 ATM IV:  78.7%
净 delta 敞口变化 ΔOI Δ Exposure*: 18k shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 78.7%｜历史 Rank 3%（近端代理）｜净 delta 敞口 正 17,828 股（方向不可观测）——方向不可观测，观察点，非方向信号

📅 事件差分（观察，非因果）: 09-04（3D）ATM IV 84.0% vs 09-11 73.1%（差 +11.0pp）——覆盖 职位空缺(JOLTS) Job Openings、ISM 制造业 PMI 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-01/USAR_morning.json