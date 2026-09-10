# 期权晨报 2026-09-10（快照 10:56 ET）

📊 市场环境

SPY $758.49 ｜ QQQ $708.69
VIX 17.34 ↑5.3%（5D +21.1%） ｜ Vol Regime: NORMAL
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
🔴 **事件差分**: 09-11（1D）ATM IV 100.0% vs 09-18 82.5%（差 +17.6pp），覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 09-11 272C ΔOI -764（距现价 +0.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 269.28 → 今开 260.71（-3.2%） | 较昨收变动（含盘初走势） ｜ 今日高 271.50 ｜ 低 257.01

Options: P/C成交量 1.22 | OI比 1.19 | ATM IV 100.0% | Skew -2.9pp | Term 0.82 | ExpMove ±4.7%（近端） | Rank 60%
量化视角： IV 中性（Rank 60%）｜期限结构倒挂（Term 0.82，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.9pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 1.22）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.22×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.19×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-11（1D）±4.7% ｜ 09-18（8D）±9.8% ｜ 09-25（15D）±13.3% ｜ 10-02（22D）±16.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 22,850,399 | GEX Change vs 上次快照 -690,608 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 639 / LOW 98 / INVALID 295
结构观察区: NO_CROSS
Call Wall 250（弱结构｜现价高于该位 8.2%）
最近结构参考: Call Wall 250（现价高于该位 8.2%）
量化视角： 正 Gamma（2285万，无历史分位）｜正 Gamma 减弱（69万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 250（MaxPain，仅结算参考） / 250（Call Wall，弱结构）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 275.0C — Vol 2,258 | 最新价 $11.70 | OI 0→1960 (ΔOI +1960张) | ΔOI/Volume 86.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1960张（前日OI缺失），连续性待观察（方向未知）
09-25 250.0P — Vol 1,919 | 最新价 $9.00 | OI 287→2169 (ΔOI +1882张) | ΔOI/Volume 98.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1882张（+655.8% vs前日OI），连续性待观察（方向未知）
09-18 290.0C — Vol 2,642 | 最新价 $6.80 | OI 2797→4655 (ΔOI +1858张) | ΔOI/Volume 70.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1858张（+66.4% vs前日OI），连续性待观察（方向未知）
10-02 275.0C — Vol 1,662 | 最新价 $19.75 | OI 181→1726 (ΔOI +1545张) | ΔOI/Volume 93.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1545张（+853.6% vs前日OI），连续性待观察（方向未知）
10-02 270.0C — Vol 1,585 | 最新价 $23.16 | OI 219→1749 (ΔOI +1530张) | ΔOI/Volume 96.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1530张（+698.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 8,775 张（Put 1,882 / Call 6,893），跨 3 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +0.4k / P +5.9k ｜ Activity HIGH ｜ 1D
09-18  C +6.9k / P +3.1k ｜ Activity HIGH ｜ 8D
09-25  C +0.7k / P +3.6k ｜ Activity HIGH ｜ 15D
10-02  C +3.8k / P +0.7k ｜ Activity HIGH ｜ 22D

📆 09-11 Forward Structure
存量OI:      C 50.2k / P 60.0k
今日变化ΔOI: C +0.4k / P +5.9k
平值价格ATM:  C 6.45 / P 6.18
隐含波动率 ATM IV:  100.0%
净 delta 敞口变化 ΔOI Δ Exposure*: -143k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 250 ｜ +1,015 ｜ $0.67 ｜ 名义 $68.0k* ｜ -7.6%
C 272 ｜ -764 ｜ $5.10 ｜ 名义 $-389.6k* ｜ +0.7%
P 260 ｜ +695 ｜ $2.35 ｜ 名义 $163.3k* ｜ -3.9%
结构参考：250（-7.6%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 250（结算参考） ｜ Call Wall 275（+1.6%，弱）（OI 4.3k） ｜ Put Wall 250（-7.6%，弱）（OI 2.8k）
量化解读： 存量 Put 重｜ATM IV 100.0%｜历史 Rank 60%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 143,108 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 127.8k / P 107.8k
今日变化ΔOI: C +6.9k / P +3.1k
平值价格ATM:  C 13.40 / P 13.20
隐含波动率 ATM IV:  82.5%
净 delta 敞口变化 ΔOI Δ Exposure*: 127k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 275 ｜ +1,960 ｜ $11.40 ｜ 名义 $2.23M* ｜ +1.6%
C 290 ｜ +1,858 ｜ $6.40 ｜ 名义 $1.19M* ｜ +7.2%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：275（+1.6%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 230（结算参考） ｜ Call Wall 250（-7.6%）（OI 20.8k）
量化解读： 存量 Call 重｜ATM IV 82.5%｜历史 Rank 60%（近端代理）｜净 delta 敞口 正 126,978 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-25 Forward Structure
存量OI:      C 10.4k / P 15.6k
今日变化ΔOI: C +0.7k / P +3.6k
平值价格ATM:  C 18.15 / P 17.75
隐含波动率 ATM IV:  81.2%
净 delta 敞口变化 ΔOI Δ Exposure*: -71k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 250 ｜ +1,882 ｜ $9.20 ｜ 名义 $1.73M* ｜ -7.6%
P 245 ｜ +1,242 ｜ $7.64 ｜ 名义 $948.9k* ｜ -9.5%
C 280 ｜ +255 ｜ $14.27 ｜ 名义 $363.9k* ｜ +3.5%
结构参考：280（+3.5%） / 250（-7.6%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 245（结算参考） ｜ Put Wall 250（-7.6%，弱）（OI 2.2k）
量化解读： 存量 Put 重｜ATM IV 81.2%｜历史 Rank 60%（近端代理）｜净 delta 敞口 负 71,461 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 10-02 Forward Structure
存量OI:      C 11.1k / P 9.9k
今日变化ΔOI: C +3.8k / P +0.7k
平值价格ATM:  C 22.44 / P 22.10
隐含波动率 ATM IV:  82.7%
净 delta 敞口变化 ΔOI Δ Exposure*: 172k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 275 ｜ +1,545 ｜ $19.65 ｜ 名义 $3.04M* ｜ +1.6%
C 270 ｜ +1,530 ｜ $22.44 ｜ 名义 $3.43M* ｜ -0.2%
P 245 ｜ +304 ｜ $11.20 ｜ 名义 $340.5k* ｜ -9.5%
结构参考：275（+1.6%） / 270（-0.2%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 245（结算参考） ｜ Put Wall 245（-9.5%，弱）（OI 1.0k）
量化解读： 存量两侧均衡｜ATM IV 82.7%｜历史 Rank 60%（近端代理）｜净 delta 敞口 正 172,466 股（方向不可观测）——方向不可观测，观察点，非方向信号

📅 事件差分（观察，非因果）: 09-11（1D）ATM IV 100.0% vs 09-18 82.5%（差 +17.6pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-10/BE_morning.json