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
🟡 **近现价集中开仓**: 09-11 360C ΔOI +1,249（距现价 +1.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-11 360C ΔOI +1,249 占该期限总 OI 20.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 350.16 → 今开 350.21（+0.0%） | 较昨收变动（含盘初走势） ｜ 今日高 357.99 ｜ 低 349.86

Options: P/C成交量 0.51 | OI比 0.59 | ATM IV 48.3% | Skew -8.4pp | Term 0.73 | ExpMove ±3.6%（近端） | Rank — (历史不足)
量化视角： 期限结构倒挂（Term 0.73，近月 IV 高于远月）｜Put 保护异常便宜（Skew -8.4pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.59）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.51×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.59×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（2D）±3.6% ｜ 09-18（9D）±5.0% ｜ 09-25（16D）±5.9% ｜ 10-02（23D）±13.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -3,797,435 | GEX Change vs 上次快照 1,226,362 | Flip: Primary Flip: 370.60（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 271 / LOW 202 / INVALID 429
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 370.60（全链重定价，覆盖 91%）
最近结构参考: Flip 371（现价低于该位 4.7%）
量化视角： 负 Gamma（380万，无历史分位）｜负 Gamma 缓解（+123万）｜现价位于 Flip 下方 4.71%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 350（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 371（全链重定价，覆盖 91%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 360.0C — Vol 1,440 | 最新价 $2.58 | OI 8→1257 (ΔOI +1249张) | ΔOI/Volume 86.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1249张（+15612.5% vs前日OI），连续性待观察（方向未知）
09-11 350.0C — Vol 1,242 | 最新价 $6.38 | OI 1→1076 (ΔOI +1075张) | ΔOI/Volume 86.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1075张（+107500.0% vs前日OI），连续性待观察（方向未知）
09-18 345.0P — Vol 578 | 最新价 $5.60 | OI 163→695 (ΔOI +532张) | ΔOI/Volume 92.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增532张（+326.4% vs前日OI），连续性待观察（方向未知）
09-18 330.0P — Vol 580 | 最新价 $2.00 | OI 375→896 (ΔOI +521张) | ΔOI/Volume 89.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增521张（+138.9% vs前日OI），连续性待观察（方向未知）
09-11 342.5P — Vol 316 | 最新价 $2.75 | OI 31→325 (ΔOI +294张) | ΔOI/Volume 93.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增294张（+948.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,671 张（Put 1,347 / Call 2,324），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +2.9k / P +1.2k ｜ Activity HIGH ｜ 2D
09-18  C +89 / P +0.7k ｜ Activity HIGH ｜ 9D
09-25  C +0.3k / P +0.1k ｜ Activity HIGH ｜ 16D
10-02  C +87 / P +0.2k ｜ Activity HIGH ｜ 23D

📆 09-11 Forward Structure
存量OI:      C 3.9k / P 2.3k
今日变化ΔOI: C +2.9k / P +1.2k
平值价格ATM:  C 5.23 / P 7.43
隐含波动率 ATM IV:  48.3%
净 delta 敞口变化 ΔOI Δ Exposure*: 73k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 360 ｜ +1,249 ｜ $2.58 ｜ 名义 $322.2k* ｜ +1.9%
C 350 ｜ +1,075 ｜ $6.38 ｜ 名义 $685.9k* ｜ -0.9%
P 342 ｜ +294 ｜ $2.75 ｜ 名义 $80.8k* ｜ -3.0%
结构参考：360（+1.9%） / 350（-0.9%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 350（结算参考） ｜ Call Wall 360（+1.9%，弱）（OI 1.3k） ｜ Put Wall 342.5（-3.0%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 48.3%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 73,468 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 15.1k / P 16.4k
今日变化ΔOI: C +89 / P +0.7k
平值价格ATM:  C 8.80 / P 9.00
隐含波动率 ATM IV:  41.8%
净 delta 敞口变化 ΔOI Δ Exposure*: 19k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 345 ｜ +532 ｜ $5.60 ｜ 名义 $297.9k* ｜ -2.3%
P 330 ｜ +521 ｜ $2.00 ｜ 名义 $104.2k* ｜ -6.6%
P 410 ｜ -286 ｜ $51.86 ｜ 名义 $-1.48M* ｜ +16.1%
结构参考：345（-2.3%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 375（结算参考）
量化解读： 存量两侧均衡｜ATM IV 41.8%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 19,321 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-25 Forward Structure
存量OI:      C 1.3k / P 0.7k
今日变化ΔOI: C +0.3k / P +0.1k
平值价格ATM:  C 8.20 / P 12.50
隐含波动率 ATM IV:  38.5%
净 delta 敞口变化 ΔOI Δ Exposure*: 3k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 355 ｜ +153 ｜ $8.20 ｜ 名义 $125.5k* ｜ +0.5%
C 385 ｜ +54 ｜ $1.82 ｜ 名义 $9.8k* ｜ +9.0%
P 360 ｜ +41 ｜ $15.80 ｜ 名义 $64.8k* ｜ +1.9%
结构参考：355（+0.5%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 370（结算参考） ｜ Put Wall 360（+1.9%，弱）（OI 0.1k）
量化解读： 存量 Call 重｜ATM IV 38.5%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 3,288 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 10-02 Forward Structure
存量OI:      C 0.4k / P 2.8k
今日变化ΔOI: C +87 / P +0.2k
平值价格ATM:  C 32.70 / P 13.50
隐含波动率 ATM IV:  36.1%
净 delta 敞口变化 ΔOI Δ Exposure*: -2k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 355 ｜ +46 ｜ $13.50 ｜ 名义 $62.1k* ｜ +0.5%
P 335 ｜ +37 ｜ $5.60 ｜ 名义 $20.7k* ｜ -5.1%
P 350 ｜ +31 ｜ $11.75 ｜ 名义 $36.4k* ｜ -0.9%
结构参考：355（+0.5%） / 335（-5.1%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 365（结算参考） ｜ Put Wall 335（-5.1%）（OI 2.4k）
量化解读： 存量 Put 重｜ATM IV 36.1%｜净 delta 敞口 负 2,445 股（方向不可观测）——方向不可观测，观察点，非方向信号

📅 事件差分（观察，非因果）: 09-11（2D）ATM IV 48.3% vs 09-18 41.8%（差 +6.5pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-09/ISRG_morning.json