# 期权晨报 2026-09-03（快照 12:15 ET）

📊 市场环境

SPY $772.61 ｜ QQQ $717.67
VIX 14.69 ↓3.4%（5D +1.2%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 35.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 55.4 ｜ 前值 54.1　✅ 今日已公布
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 56 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **事件差分**: 09-04（1D）ATM IV 94.3% vs 09-11 74.4%（差 +19.8pp），覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 09-04 18C ΔOI +244（距现价 +1.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-11 19C ΔOI +2,061 占该期限总 OI 10.6%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 17.85 → 今开 18.05（+1.1%） | 较昨收变动（含盘初走势） ｜ 今日高 18.17 ｜ 低 17.60

Options: P/C成交量 0.24 | OI比 0.30 | ATM IV 94.3% | Skew -1.3pp | Term 0.85 | ExpMove ±4.9%（近端） | Rank 12%
量化视角： IV 历史低位（Rank 12%，期权偏便宜）｜期限结构倒挂（Term 0.85，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.3pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.30）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.24×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.30×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（1D）±4.9% ｜ 09-11（8D）±9.1% ｜ 09-18（15D）±12.6% ｜ 09-25（22D）±15.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 4,829,277 | GEX Change vs 上次快照 -1,263,893 | Flip: Primary Flip: 17.25（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 262 / LOW 114 / INVALID 152
结构观察区: Primary Flip 17.25（全链重定价，覆盖 100%）
最近结构参考: Flip 17（现价高于该位 3.0%）
量化视角： 正 Gamma（483万，无历史分位）｜正 Gamma 减弱（126万）｜现价位于 Flip 上方 3.04%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 17（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 19.5C — Vol 2,305 | 最新价 $0.28 | OI 348→2409 (ΔOI +2061张) | ΔOI/Volume 89.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2061张（+592.2% vs前日OI），连续性待观察（方向未知）
09-11 20.5C — Vol 1,935 | 最新价 $0.14 | OI 1099→2492 (ΔOI +1393张) | ΔOI/Volume 72.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1393张（+126.8% vs前日OI），连续性待观察（方向未知）
09-04 19.0C — Vol 728 | 最新价 $0.11 | OI 1218→1683 (ΔOI +465张) | ΔOI/Volume 63.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增465张（+38.2% vs前日OI），连续性待观察（方向未知）
09-18 20.0C — Vol 1,141 | 最新价 $0.45 | OI 13817→14259 (ΔOI +442张) | ΔOI/Volume 38.7% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增442张（+3.2% vs前日OI），值得跟踪（方向未知）
09-18 21.0C — Vol 444 | 最新价 $0.25 | OI 1118→1406 (ΔOI +288张) | ΔOI/Volume 64.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增288张（+25.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,649 张（Put 0 / Call 4,649），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C +0.7k / P -0.1k ｜ Activity HIGH ｜ 1D
09-11  C +3.8k / P +0.1k ｜ Activity HIGH ｜ 8D
09-18  C +0.7k / P -25 ｜ Activity MEDIUM △ ｜ 15D
09-25  C +95 / P -77 ｜ Activity LOW ｜ 22D

📆 09-04 Forward Structure
存量OI:      C 33.1k / P 9.9k
今日变化ΔOI: C +0.7k / P -0.1k
平值价格ATM:  C 0.39 / P 0.48
隐含波动率 ATM IV:  94.3%
净 delta 敞口变化 ΔOI Δ Exposure*: 26k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 19 ｜ +465 ｜ $0.09 ｜ 名义 $4.2k* ｜ +6.9%
C 18 ｜ +244 ｜ $0.39 ｜ 名义 $9.5k* ｜ +1.3%
P 16 ｜ -95 ｜ $0.04 ｜ 名义 $-380* ｜ -7.1%
结构参考：19（+6.9%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 94.3%｜历史 Rank 12%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 26,205 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-11 Forward Structure
存量OI:      C 15.9k / P 3.6k
今日变化ΔOI: C +3.8k / P +0.1k
平值价格ATM:  C 0.78 / P 0.83
隐含波动率 ATM IV:  74.4%
净 delta 敞口变化 ΔOI Δ Exposure*: 80k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 19 ｜ +2,061 ｜ $0.30 ｜ 名义 $61.8k* ｜ +9.7%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：19（+9.7%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 74.4%｜历史 Rank 12%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 80,167 股（方向不可观测）——方向不可观测，观察点，非方向信号

📅 事件差分（观察，非因果）: 09-04（1D）ATM IV 94.3% vs 09-11 74.4%（差 +19.8pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-03/USAR_morning.json