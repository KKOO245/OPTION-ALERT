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
🔴 **事件差分**: 09-04（1D）ATM IV 89.2% vs 09-11 73.0%（差 +16.2pp），覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **单日价格波动**: +4.9%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 202.79 → 收盘 210.63（+3.9%） ｜ 今日高 211.67 ｜ 低 196.63
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.46 | OI比 0.92 | ATM IV 89.2% | Skew 1.1pp | Term 0.86 | ExpMove ±3.8%（近端） | Rank 21%
量化视角： IV 历史低位（Rank 21%，期权偏便宜）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜保护溢价薄（Skew 1.1pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.46×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.92×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-04（1D）±3.8% ｜ 09-11（8D）±8.9% ｜ 09-18（15D）±12.4% ｜ 09-25（22D）±15.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,200,180 | GEX Change vs 上次快照 1,870,804 | Flip: Primary Flip: 209.68（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 532 / LOW 103 / INVALID 169
结构观察区: Primary Flip 209.68（全链重定价，覆盖 99%）
Put Wall 200（弱结构｜现价高于该位 5.3%）
最近结构参考: Flip 210（现价高于该位 0.5%）
量化视角： 正 Gamma（120万，无历史分位）｜由负转正（+187万）｜现价位于 Flip 上方 0.46%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall，弱结构）；上方 208（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 210（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 157.5P — Vol 2 | 最新价 $0.02 | OI 171→1802 (ΔOI +1631张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1631张（+953.8% vs前日OI），连续性待观察（方向未知）
09-11 125.0P — Vol 8 | 最新价 $0.05 | OI 243→1242 (ΔOI +999张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增999张（+411.1% vs前日OI），连续性待观察（方向未知）
09-11 315.0C — Vol 8 | 最新价 $0.07 | OI 74→907 (ΔOI +833张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增833张（+1125.7% vs前日OI），连续性待观察（方向未知）
09-18 200.0C — Vol 144 | 最新价 $19.10 | OI 5619→6284 (ΔOI +665张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增665张（+11.8% vs前日OI），值得跟踪（方向未知）
09-04 200.0C — Vol 732 | 最新价 $11.50 | OI 1739→2319 (ΔOI +580张) | ΔOI/Volume 79.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增580张（+33.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,708 张（Put 2,630 / Call 2,078），跨 3 个期限｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C +1.6k / P +0.6k ｜ Activity MEDIUM △ ｜ 1D
09-11  C +3.4k / P +2.9k ｜ Activity HIGH ｜ 8D
09-18  C +0.8k / P +0.6k ｜ Activity MEDIUM △ ｜ 15D
09-25  C +0.4k / P +0.6k ｜ Activity HIGH ｜ 22D

📆 09-04 Forward Structure
存量OI:      C 58.5k / P 53.5k
今日变化ΔOI: C +1.6k / P +0.6k
平值价格ATM:  C 4.40 / P 3.50
隐含波动率 ATM IV:  89.2%
净 delta 敞口变化 ΔOI Δ Exposure*: 282k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 200 ｜ +580 ｜ $11.50 ｜ 名义 $667.0k* ｜ -5.0%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：200（-5.0%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜ATM IV 89.2%｜历史 Rank 21%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 281,574 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-11 Forward Structure
存量OI:      C 24.1k / P 20.9k
今日变化ΔOI: C +3.4k / P +2.9k
平值价格ATM:  C 9.95 / P 8.80
隐含波动率 ATM IV:  73.0%
净 delta 敞口变化 ΔOI Δ Exposure*: 24k shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜ATM IV 73.0%｜历史 Rank 21%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 24,012 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（MEDIUM △）Top ΔOI: 200C +665

📆 09-25 Forward Structure
存量OI:      C 7.8k / P 13.5k
今日变化ΔOI: C +0.4k / P +0.6k
平值价格ATM:  C 16.87 / P 15.64
隐含波动率 ATM IV:  77.4%
净 delta 敞口变化 ΔOI Δ Exposure*: 12k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 205 ｜ +100 ｜ $18.95 ｜ 名义 $189.5k* ｜ -2.7%
C 220 ｜ +74 ｜ $12.30 ｜ 名义 $91.0k* ｜ +4.4%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：220（+4.4%） / 205（-2.7%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜ATM IV 77.4%｜历史 Rank 21%（近端代理）｜净 delta 敞口 正 12,246 股（方向不可观测）——方向不可观测，观察点，非方向信号

📅 事件差分（观察，非因果）: 09-04（1D）ATM IV 89.2% vs 09-11 73.0%（差 +16.2pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-03/NBIS_evening.json