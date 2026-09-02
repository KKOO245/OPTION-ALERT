# 期权晨报 2026-09-02（快照 11:19 ET）

📊 市场环境

SPY $764.45 ｜ QQQ $709.24
VIX 15.51 ↓5.1%（5D +0.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 待公布 ｜ 前值 54.1
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 58 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **单日价格波动**: -2.1%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **事件差分**: 09-04 ATM IV 79.9% vs 09-11 65.6%（差 +14.3pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 09-04 128C ΔOI +1,413（距现价 +4.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 124.88 → 今开 123.35（-1.2%） | 较昨收变动（含盘初走势） ｜ 今日高 124.66 ｜ 低 121.38

Options: P/C成交量 0.47 | OI比 0.68 | ATM IV 79.9% | Skew -4.9pp | Term 0.85 | ExpMove ±5.0%（近端） | Rank 49%
量化视角： IV 中性（Rank 49%）｜期限结构倒挂（Term 0.85，近月 IV 高于远月）｜Put 保护异常便宜（Skew -4.9pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.68）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.47×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.68×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（2D）±5.0% ｜ 09-11（9D）±8.1% ｜ 09-18（16D）±11.6% ｜ 09-25（23D）±13.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 26,107,615 | GEX Change vs 上次快照 -19,891,785 | Flip: Primary Flip: 116.70（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 932 / LOW 130 / INVALID 268
结构观察区: Primary Flip 116.70（全链重定价，覆盖 100%）
最近结构参考: Flip 117（现价高于该位 4.8%）
量化视角： 正 Gamma（2611万，无历史分位）｜正 Gamma 减弱（1989万）｜现价位于 Flip 上方 4.75%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 117（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 131.0C — Vol 344 | 最新价 $0.90 | OI 10146→12725 (ΔOI +2579张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2579张（+25.4% vs前日OI），连续性待观察（方向未知）
09-04 128.0C — Vol 568 | 最新价 $1.41 | OI 1242→2655 (ΔOI +1413张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1413张（+113.8% vs前日OI），连续性待观察（方向未知）
09-04 129.0C — Vol 368 | 最新价 $1.27 | OI 976→2290 (ΔOI +1314张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1314张（+134.6% vs前日OI），连续性待观察（方向未知）
09-04 134.0C — Vol 308 | 最新价 $0.54 | OI 4491→5691 (ΔOI +1200张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1200张（+26.7% vs前日OI），连续性待观察（方向未知）
09-11 155.0C — Vol 36 | 最新价 $0.31 | OI 464→1339 (ΔOI +875张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增875张（+188.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 7,381 张（Put 0 / Call 7,381），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C +6.8k / P +3.4k ｜ Activity HIGH ｜ 2D
09-11  C +2.8k / P +2.5k ｜ Activity HIGH ｜ 9D
09-18  C -0.4k / P +3.8k ｜ Activity MEDIUM △ ｜ 16D
09-25  C +0.9k / P +1.6k ｜ Activity HIGH ｜ 23D

📆 09-04 Forward Structure
存量OI:      C 260.3k / P 178.0k
今日变化ΔOI: C +6.8k / P +3.4k
平值价格ATM:  C 3.45 / P 2.62
隐含波动率 ATM IV:  79.9%
净 delta 敞口变化 ΔOI Δ Exposure*: 95k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 131 ｜ +2,579 ｜ $0.73 ｜ 名义 $188.3k* ｜ +7.2%
C 128 ｜ +1,413 ｜ $1.28 ｜ 名义 $180.9k* ｜ +4.7%
C 129 ｜ +1,314 ｜ $0.97 ｜ 名义 $127.5k* ｜ +5.5%
结构参考：131（+7.2%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 79.9%｜历史 Rank 49%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 94,712 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-11 Forward Structure
存量OI:      C 39.2k / P 74.2k
今日变化ΔOI: C +2.8k / P +2.5k
平值价格ATM:  C 5.44 / P 4.45
隐含波动率 ATM IV:  65.6%
净 delta 敞口变化 ΔOI Δ Exposure*: -46k shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 65.6%｜历史 Rank 49%（近端代理）｜净 delta 敞口 负 45,931 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（MEDIUM △）Top ΔOI: 110P +853

📆 09-25 Forward Structure
存量OI:      C 16.5k / P 23.2k
今日变化ΔOI: C +0.9k / P +1.6k
平值价格ATM:  C 8.57 / P 7.86
隐含波动率 ATM IV:  67.7%
净 delta 敞口变化 ΔOI Δ Exposure*: -5k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 133 ｜ +694 ｜ $5.20 ｜ 名义 $360.9k* ｜ +8.8%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：133（+8.8%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜ATM IV 67.7%｜历史 Rank 49%（近端代理）｜净 delta 敞口 负 5,062 股（方向不可观测）——方向不可观测，观察点，非方向信号

📅 事件差分（观察，非因果）: 09-04（2D）ATM IV 79.9% vs 09-11 65.6%（差 +14.3pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-02/MSTR_morning.json