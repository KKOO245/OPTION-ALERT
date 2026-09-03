# 期权晨报 2026-09-03（快照 10:16 ET）

📊 市场环境

SPY $768.40 ｜ QQQ $712.31
VIX 15.00 ↓1.3%（5D -1.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 55.4 ｜ 前值 54.1　✅ 今日已公布
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 58 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **单日价格波动**: +2.4%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **事件差分**: 09-04 ATM IV 78.7% vs 09-11 65.6%（差 +13.1pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 09-04 18C ΔOI +247（距现价 -0.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 17.59 → 今开 17.75（+0.9%） | 较昨收变动（含盘初走势） ｜ 今日高 18.24 ｜ 低 17.60

Options: P/C成交量 0.29 | OI比 0.68 | ATM IV 78.7% | Skew -9.1pp | Term 0.96 | ExpMove ±5.8%（近端） | Rank 5%
量化视角： IV 历史低位（Rank 5%，期权偏便宜）｜期限结构正常（Term 0.96）｜Put 保护异常便宜（Skew -9.1pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.68）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.29×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.68×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（1D）±5.8% ｜ 09-11（8D）±9.1% ｜ 09-18（15D）±11.7% ｜ 09-25（22D）±13.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,185,321 | GEX Change vs 上次快照 589,582 | Flip: Primary Flip: 17.42（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 89%（带内） ｜ IV 有效性: VALID 197 / LOW 92 / INVALID 177
结构观察区: Primary Flip 17.42（全链重定价，覆盖 89%）
最近结构参考: Flip 17（现价高于该位 3.4%）
量化视角： 正 Gamma（119万，无历史分位）｜正 Gamma 增强（+59万）｜现价位于 Flip 上方 3.39%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 17（全链重定价，覆盖 89%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 18.0C — Vol 340 | 最新价 $0.30 | OI 109→356 (ΔOI +247张) | ΔOI/Volume 72.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增247张（+226.6% vs前日OI），连续性待观察（方向未知）
09-11 15.5P — Vol 173 | 最新价 $0.15 | OI 17→180 (ΔOI +163张) | ΔOI/Volume 94.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增163张（+958.8% vs前日OI），连续性待观察（方向未知）
09-04 17.0P — Vol 66 | 最新价 $0.15 | OI 519→570 (ΔOI +51张) | ΔOI/Volume 77.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增51张（+9.8% vs前日OI），连续性待观察（方向未知）
09-18 16.0P — Vol 40 | 最新价 $0.40 | OI 346→386 (ΔOI +40张) | ΔOI/Volume 100.0% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增40张（+11.6% vs前日OI），值得跟踪（方向未知）
09-11 19.0C — Vol 24 | 最新价 $0.35 | OI 79→98 (ΔOI +19张) | ΔOI/Volume 79.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增19张（+24.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 520 张（Put 254 / Call 266），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C +0.1k / P +22 ｜ Activity MEDIUM △ ｜ 1D
09-11  C +75 / P +0.2k ｜ Activity HIGH ｜ 8D
09-18  C +50 / P +26 ｜ Activity MEDIUM △ ｜ 15D
09-25  C +45 / P +5 ｜ Activity MEDIUM △ ｜ 22D

📆 09-04 Forward Structure
存量OI:      C 3.5k / P 2.4k
今日变化ΔOI: C +0.1k / P +22
平值价格ATM:  C 0.30 / P 0.75
隐含波动率 ATM IV:  78.7%
净 delta 敞口变化 ΔOI Δ Exposure*: 11k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 18 ｜ +247 ｜ $0.30 ｜ 名义 $7.4k* ｜ -0.1%
C 19 ｜ -121 ｜ $0.06 ｜ 名义 $-726* ｜ +5.5%
P 17 ｜ +51 ｜ $0.15 ｜ 名义 $765* ｜ -5.6%
结构参考：18（-0.1%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 78.7%｜历史 Rank 5%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 10,965 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-11 Forward Structure
存量OI:      C 2.6k / P 2.0k
今日变化ΔOI: C +75 / P +0.2k
平值价格ATM:  C 0.63 / P 1.00
隐含波动率 ATM IV:  65.6%
净 delta 敞口变化 ΔOI Δ Exposure*: -4k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 19 ｜ +19 ｜ $0.35 ｜ 名义 $665* ｜ +5.5%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：19（+5.5%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 65.6%｜历史 Rank 5%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 负 3,914 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-25（MEDIUM △）Top ΔOI: 18C +18 ｜ 19C +16

📅 事件差分（观察，非因果）: 09-04（1D）ATM IV 78.7% vs 09-11 65.6%（差 +13.1pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-03/NNE_morning.json