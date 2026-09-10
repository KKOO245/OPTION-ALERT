# 期权晚报 2026-09-10（快照 17:04 ET）

📊 市场环境

SPY $757.83 ｜ QQQ $708.69
VIX 17.84 ↑8.4%（5D +24.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-10 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 0.4 ｜ 前值 0.1　✅ 今日已公布
- 周四 09-10 10:00　【高】成屋销售　预测 3.98 ｜ 实际 3.98 ｜ 前值 4.06　✅ 今日已公布
- 周五 09-11 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.2
- 周五 09-11 08:30　【高】Inflation Rate MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.1
- 周五 09-11 08:30　【高】Inflation Rate YoY　预测 3.4 ｜ 实际 待公布 ｜ 前值 3.4
- 周五 09-11 08:30　【高】Core Inflation Rate YoY　预测 2.4 ｜ 实际 待公布 ｜ 前值 2.5
- 周五 09-11 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 51 ｜ 实际 待公布 ｜ 前值 51.7

🔍 重点速览
🟡 **单日价格波动**: -4.0%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-18 1750C ΔOI -340（距现价 +3.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 1,724.60 → 收盘 1,692.59（-1.9%） ｜ 今日高 1733.95 ｜ 低 1674.00 ｜ 昨收 1,764.17 → 收盘 1,692.59（-4.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.72 | OI比 0.90 | ATM IV 76.5% | Skew -2.1pp | Term 0.96 | ExpMove ±3.2%（近端） | Rank 30%
量化视角： IV 中性（Rank 30%）｜期限结构正常（Term 0.96）｜Put 保护异常便宜（Skew -2.1pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.72×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.90×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-11（1D）±3.2% ｜ 09-18（8D）±8.3% ｜ 09-25（15D）±11.8% ｜ 10-02（22D）±13.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,852,241 | GEX Change vs 上次快照 -1,974,069 | Flip: Primary Flip: 1677.09（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 2043 / LOW 499 / INVALID 920
结构观察区: Primary Flip 1677.09（全链重定价，覆盖 99%）
最近结构参考: Flip 1677（现价高于该位 0.9%）
量化视角： 正 Gamma（185万，无历史分位）｜正 Gamma 减弱（197万）｜现价位于 Flip 上方 0.92%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 1,695（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1677（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 2000.0C — Vol 4,390 | 最新价 $0.15 | OI 4613→6359 (ΔOI +1746张) | ΔOI/Volume 39.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1746张（+37.9% vs前日OI），连续性待观察（方向未知）
09-11 1900.0C — Vol 3,938 | 最新价 $0.48 | OI 2230→2937 (ΔOI +707张) | ΔOI/Volume 17.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增707张（+31.7% vs前日OI），连续性待观察（方向未知）
09-11 1800.0C — Vol 10,998 | 最新价 $2.95 | OI 2524→2970 (ΔOI +446张) | ΔOI/Volume 4.1% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增446张（+17.7% vs前日OI），值得跟踪（方向未知）
09-11 1950.0C — Vol 1,047 | 最新价 $0.26 | OI 777→1222 (ΔOI +445张) | ΔOI/Volume 42.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增445张（+57.3% vs前日OI），连续性待观察（方向未知）
09-18 1800.0C — Vol 1,369 | 最新价 $32.60 | OI 1755→2183 (ΔOI +428张) | ΔOI/Volume 31.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增428张（+24.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,772 张（Put 0 / Call 3,772），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +7.6k / P +4.0k ｜ Activity HIGH ｜ 1D
09-18  C +1.8k / P +1.3k ｜ Activity MEDIUM △ ｜ 8D
09-25  C +0.4k / P +0.6k ｜ Activity HIGH ｜ 15D
10-02  C +0.1k / P +0.2k ｜ Activity MEDIUM △ ｜ 22D

📆 09-11 Forward Structure
存量OI:      C 47.0k / P 42.5k
今日变化ΔOI: C +7.6k / P +4.0k
平值价格ATM:  C 26.30 / P 28.30
隐含波动率 ATM IV:  76.5%
净 delta 敞口变化 ΔOI Δ Exposure*: -133k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 1800 ｜ +446 ｜ $2.95 ｜ 名义 $131.6k* ｜ +6.3%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：1800（+6.3%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 1,695（结算参考） ｜ Put Wall 1600（-5.5%，弱）（OI 2.3k）
量化解读： 存量两侧均衡｜ATM IV 76.5%｜历史 Rank 30%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 133,069 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（MEDIUM △）Top ΔOI: 1800C +428 ｜ 1750C -340
09-18（MEDIUM △）仓位参考: Max Pain 1,470（结算参考）

📆 09-25 Forward Structure
存量OI:      C 8.1k / P 15.4k
今日变化ΔOI: C +0.4k / P +0.6k
平值价格ATM:  C 107.00 / P 91.80
隐含波动率 ATM IV:  70.8%
净 delta 敞口变化 ΔOI Δ Exposure*: -11k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 1780 ｜ +109 ｜ $69.69 ｜ 名义 $759.6k* ｜ +5.2%
P 1575 ｜ +93 ｜ $43.13 ｜ 名义 $401.1k* ｜ -6.9%
P 1590 ｜ +78 ｜ $47.40 ｜ 名义 $369.7k* ｜ -6.1%
结构参考：1780（+5.2%） / 1575（-6.9%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 1,600（结算参考）
量化解读： 存量 Put 重｜ATM IV 70.8%｜历史 Rank 30%（近端代理）｜净 delta 敞口 负 11,458 股（方向不可观测）——方向不可观测，观察点，非方向信号

10-02（MEDIUM △）Top ΔOI: 1900C +41 ｜ 1700C +33
10-02（MEDIUM △）仓位参考: Max Pain 1,565（结算参考） ｜ Call Wall 1800（+6.3%，弱）（OI 0.3k）

📅 事件差分（观察，非因果）: 09-11（1D）ATM IV 76.5% vs 09-18 69.9%（差 +6.6pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-10/SNDK_evening.json