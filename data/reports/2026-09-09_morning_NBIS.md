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
🟡 **事件差分**: 09-11 ATM IV 99.0% vs 09-18 88.0%（差 +11.0pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 243.88 → 今开 247.21（+1.4%） | 较昨收变动（含盘初走势） ｜ 今日高 250.27 ｜ 低 241.27

Options: P/C成交量 0.66 | OI比 0.74 | ATM IV 99.0% | Skew -0.7pp | Term 0.87 | ExpMove ±6.2%（近端） | Rank 39%
量化视角： IV 中性（Rank 39%）｜期限结构倒挂（Term 0.87，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.7pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.74）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.66×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.74×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（2D）±6.2% ｜ 09-18（9D）±11.1% ｜ 09-25（16D）±14.5% ｜ 10-02（23D）±17.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 11,191,209 | GEX Change vs 上次快照 2,346,880 | Flip: Primary Flip: 226.45（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 535 / LOW 53 / INVALID 130
结构观察区: Primary Flip 226.45（全链重定价，覆盖 100%）
最近结构参考: Flip 226（现价高于该位 8.3%）
量化视角： 正 Gamma（1119万，无历史分位）｜正 Gamma 增强（+235万）｜现价位于 Flip 上方 8.31%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 220（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 226（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 380.0C — Vol 13,329 | 最新价 $0.17 | OI 1262→13290 (ΔOI +12028张) | ΔOI/Volume 90.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12028张（+953.1% vs前日OI），连续性待观察（方向未知）
09-18 220.0P — Vol 4,636 | 最新价 $5.12 | OI 3425→5909 (ΔOI +2484张) | ΔOI/Volume 53.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2484张（+72.5% vs前日OI），连续性待观察（方向未知）
09-18 140.0P — Vol 2,726 | 最新价 $0.08 | OI 1967→4390 (ΔOI +2423张) | ΔOI/Volume 88.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2423张（+123.2% vs前日OI），连续性待观察（方向未知）
09-11 280.0C — Vol 5,199 | 最新价 $1.02 | OI 885→3200 (ΔOI +2315张) | ΔOI/Volume 44.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2315张（+261.6% vs前日OI），连续性待观察（方向未知）
09-11 260.0C — Vol 6,490 | 最新价 $3.56 | OI 1554→3307 (ΔOI +1753张) | ΔOI/Volume 27.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1753张（+112.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 21,003 张（Put 4,907 / Call 16,096），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +14.0k / P +7.0k ｜ Activity HIGH ｜ 2D
09-18  C +15.0k / P +5.9k ｜ Activity MEDIUM △ ｜ 9D
09-25  C +3.0k / P +1.8k ｜ Activity HIGH ｜ 16D
10-02  C +0.7k / P +1.0k ｜ Activity HIGH ｜ 23D

📆 09-11 Forward Structure
存量OI:      C 57.9k / P 42.8k
今日变化ΔOI: C +14.0k / P +7.0k
平值价格ATM:  C 8.00 / P 7.30
隐含波动率 ATM IV:  99.0%
净 delta 敞口变化 ΔOI Δ Exposure*: -86k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 280 ｜ +2,315 ｜ $0.61 ｜ 名义 $141.2k* ｜ +14.2%
P 220 ｜ -1,793 ｜ $0.83 ｜ 名义 $-148.8k* ｜ -10.3%
C 260 ｜ +1,753 ｜ $2.79 ｜ 名义 $489.1k* ｜ +6.0%
结构参考：280（+14.2%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 220（结算参考） ｜ Call Wall 225（-8.3%，弱）（OI 4.9k）
量化解读： 存量 Call 重｜ATM IV 99.0%｜历史 Rank 39%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 85,920 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（MEDIUM △）Top ΔOI: 380C +12,028 ｜ 220P +2,484
09-18（MEDIUM △）仓位参考: Max Pain 220（结算参考）

📆 09-25 Forward Structure
存量OI:      C 12.8k / P 15.2k
今日变化ΔOI: C +3.0k / P +1.8k
平值价格ATM:  C 18.02 / P 17.50
隐含波动率 ATM IV:  85.5%
净 delta 敞口变化 ΔOI Δ Exposure*: 30k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 270 ｜ +1,171 ｜ $9.25 ｜ 名义 $1.08M* ｜ +10.1%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：270（+10.1%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 220（结算参考）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 85.5%｜历史 Rank 39%（近端代理）｜净 delta 敞口 正 30,299 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 10-02 Forward Structure
存量OI:      C 6.2k / P 8.5k
今日变化ΔOI: C +0.7k / P +1.0k
平值价格ATM:  C 22.26 / P 19.90
隐含波动率 ATM IV:  86.7%
净 delta 敞口变化 ΔOI Δ Exposure*: 2k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 300 ｜ -366 ｜ $6.38 ｜ 名义 $-233.5k* ｜ +22.3%
P 190 ｜ +295 ｜ $3.30 ｜ 名义 $97.3k* ｜ -22.5%
C 260 ｜ +283 ｜ $16.35 ｜ 名义 $462.7k* ｜ +6.0%
结构参考：260（+6.0%） / 190（-22.5%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 220（结算参考）
量化解读： 存量 Put 重｜ATM IV 86.7%｜历史 Rank 39%（近端代理）｜净 delta 敞口 正 2,356 股（方向不可观测）——方向不可观测，观察点，非方向信号

📅 事件差分（观察，非因果）: 09-11（2D）ATM IV 99.0% vs 09-18 88.0%（差 +11.0pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-09/NBIS_morning.json