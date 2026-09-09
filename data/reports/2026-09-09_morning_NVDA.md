# 期权晨报 2026-09-09（快照 11:03 ET）

📊 市场环境

SPY $762.70 ｜ QQQ $716.31
VIX 16.06 ↑2.2%（5D +5.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 39.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-10 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0
- 周四 09-10 10:00　【高】成屋销售　预测 3.98 ｜ 实际 待公布 ｜ 前值 4.06
- 周五 09-11 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.2
- 周五 09-11 08:30　【高】Inflation Rate MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.1
- 周五 09-11 08:30　【高】Inflation Rate YoY　预测 3.4 ｜ 实际 待公布 ｜ 前值 3.4
- 周五 09-11 08:30　【高】Core Inflation Rate YoY　预测 2.4 ｜ 实际 待公布 ｜ 前值 2.5
- 周五 09-11 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 51 ｜ 实际 待公布 ｜ 前值 51.7

🔍 重点速览
🟡 **近现价集中开仓**: 09-11 235C ΔOI +24,245（距现价 +4.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-14 235C ΔOI +8,137 占该期限总 OI 13.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 225.73 → 今开 225.27（-0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 226.18 ｜ 低 223.55

Options: P/C成交量 0.53 | OI比 0.76 | ATM IV 36.3% | Skew -1.7pp | Term 0.95 | ExpMove ±2.4%（近端） | Rank 22%
量化视角： IV 历史低位（Rank 22%，期权偏便宜）｜期限结构正常（Term 0.95）｜Put 保护异常便宜（Skew -1.7pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.76）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.53×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.76×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（2D）±2.4% ｜ 09-14（5D）±2.9% ｜ 09-16（7D）±3.8% ｜ 09-18（9D）±4.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 454,955,292 | GEX Change vs 上次快照 46,749,954 | Flip: Primary Flip: 215.13（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 690 / LOW 195 / INVALID 567
结构观察区: Primary Flip 215.13（全链重定价，覆盖 96%）
最近结构参考: Flip 215（现价高于该位 4.3%）
量化视角： 正 Gamma（4.55亿，无历史分位）｜正 Gamma 增强（+4675万）｜现价位于 Flip 上方 4.35%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 225（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 215（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 235.0C — Vol 54,222 | 最新价 $0.48 | OI 32767→57012 (ΔOI +24245张) | ΔOI/Volume 44.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增24245张（+74.0% vs前日OI），连续性待观察（方向未知）
09-11 227.5C — Vol 54,493 | 最新价 $2.19 | OI 24169→47467 (ΔOI +23298张) | ΔOI/Volume 42.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增23298张（+96.4% vs前日OI），连续性待观察（方向未知）
09-09 230.0C — Vol 164,032 | 最新价 $0.38 | OI 16990→39880 (ΔOI +22890张) | ΔOI/Volume 13.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增22890张（+134.7% vs前日OI），连续性待观察（方向未知）
09-09 235.0C — Vol 111,873 | 最新价 $0.09 | OI 19009→37014 (ΔOI +18005张) | ΔOI/Volume 16.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18005张（+94.7% vs前日OI），连续性待观察（方向未知）
09-11 315.0C — Vol 15,083 | 最新价 $0.01 | OI 111→15142 (ΔOI +15031张) | ΔOI/Volume 99.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15031张（+13541.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 103,469 张（Put 0 / Call 103,469），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +107.4k / P +39.9k ｜ Activity HIGH ｜ 2D
09-14  C +18.4k / P +9.6k ｜ Activity HIGH ｜ 5D
09-16  C +10.2k / P +2.0k ｜ Activity HIGH ｜ 7D
09-18  C +9.3k / P +6.2k ｜ Activity HIGH ｜ 9D

📆 09-11 Forward Structure
存量OI:      C 519.8k / P 307.0k
今日变化ΔOI: C +107.4k / P +39.9k
平值价格ATM:  C 2.30 / P 3.02
隐含波动率 ATM IV:  37.7%
净 delta 敞口变化 ΔOI Δ Exposure*: 293k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 235 ｜ +24,245 ｜ $0.25 ｜ 名义 $606.1k* ｜ +4.7%
C 227 ｜ +23,298 ｜ $1.35 ｜ 名义 $3.15M* ｜ +1.3%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：235（+4.7%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 225（结算参考） ｜ Call Wall 235（+4.7%，弱）（OI 57.0k） ｜ Put Wall 220（-2.0%）（OI 31.2k）
量化解读： 存量 Call 重｜ATM IV 37.7%｜历史 Rank 22%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 292,661 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-14 Forward Structure
存量OI:      C 42.2k / P 16.9k
今日变化ΔOI: C +18.4k / P +9.6k
平值价格ATM:  C 2.97 / P 3.60
隐含波动率 ATM IV:  30.5%
净 delta 敞口变化 ΔOI Δ Exposure*: 64k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 235 ｜ +8,137 ｜ $0.44 ｜ 名义 $358.0k* ｜ +4.7%
C 245 ｜ +4,420 ｜ $0.08 ｜ 名义 $35.4k* ｜ +9.1%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：235（+4.7%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 225（结算参考） ｜ Call Wall 235（+4.7%，弱）（OI 13.1k）
量化解读： 存量 Call 重｜ATM IV 30.5%｜历史 Rank 22%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 63,754 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-16 Forward Structure
存量OI:      C 26.2k / P 7.8k
今日变化ΔOI: C +10.2k / P +2.0k
平值价格ATM:  C 3.90 / P 4.51
隐含波动率 ATM IV:  33.4%
净 delta 敞口变化 ΔOI Δ Exposure*: 144k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 235 ｜ +2,725 ｜ $0.96 ｜ 名义 $261.6k* ｜ +4.7%
C 240 ｜ +1,652 ｜ $0.46 ｜ 名义 $76.0k* ｜ +6.9%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：235（+4.7%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 225（结算参考） ｜ Call Wall 235（+4.7%）（OI 8.9k） ｜ Put Wall 205（-8.7%）（OI 2.2k）
量化解读： 存量 Call 重｜ATM IV 33.4%｜历史 Rank 22%（近端代理）｜净 delta 敞口 正 143,749 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 1195.1k / P 1004.0k
今日变化ΔOI: C +9.3k / P +6.2k
平值价格ATM:  C 4.65 / P 5.25
隐含波动率 ATM IV:  34.6%
净 delta 敞口变化 ΔOI Δ Exposure*: -14k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 235 ｜ +3,132 ｜ $1.45 ｜ 名义 $454.1k* ｜ +4.7%
C 230 ｜ +2,961 ｜ $2.71 ｜ 名义 $802.4k* ｜ +2.5%
P 200 ｜ -2,268 ｜ $0.39 ｜ 名义 $-88.5k* ｜ -10.9%
结构参考：235（+4.7%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 195（结算参考）
量化解读： 存量 Call 重｜ATM IV 34.6%｜历史 Rank 22%（近端代理）｜净 delta 敞口 负 14,391 股（方向不可观测）——方向不可观测，观察点，非方向信号

📅 事件差分（观察，非因果）: 09-11（2D）ATM IV 37.7% vs 09-14 30.5%（差 +7.2pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-09/NVDA_morning.json