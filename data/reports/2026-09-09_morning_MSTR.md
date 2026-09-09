# 期权晨报 2026-09-09（快照 11:03 ET）

📊 市场环境

SPY $763.65 ｜ QQQ $717.21
VIX 16.06 ↑2.2%（5D +5.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 40.9（fear）
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
🔴 **事件差分**: 09-11（2D）ATM IV 95.3% vs 09-18 78.7%（差 +16.6pp），覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 09-11 140C ΔOI +3,909（距现价 +2.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 136.52 → 今开 141.98（+4.0%） | 较昨收变动（含盘初走势） ｜ 今日高 141.98 ｜ 低 134.66

Options: P/C成交量 0.47 | OI比 0.65 | ATM IV 95.3% | Skew -10.0pp | Term 0.79 | ExpMove ±5.9%（近端） | Rank 73%
量化视角： IV 中性（Rank 73%）｜期限结构倒挂（Term 0.79，近月 IV 高于远月）｜Put 保护异常便宜（Skew -10.0pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.65）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.47×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.65×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（2D）±5.9% ｜ 09-18（9D）±10.2% ｜ 09-25（16D）±12.3% ｜ 10-02（23D）±15.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 74,077,033 | GEX Change vs 上次快照 7,314,262 | Flip: Primary Flip: 118.81（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 886 / LOW 108 / INVALID 200
结构观察区: Primary Flip 118.81（全链重定价，覆盖 100%）
Call Wall 150（弱结构｜现价低于该位 8.9%）
最近结构参考: Call Wall 150（现价低于该位 8.9%）
量化视角： 正 Gamma（7408万，无历史分位）｜正 Gamma 增强（+731万）｜现价位于 Flip 上方 15.03%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 131（MaxPain，仅结算参考）；上方 150（Call Wall，弱结构）。
• Gamma 区域：切换参考 119（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 150.0C — Vol 5,419 | 最新价 $0.98 | OI 24102→28991 (ΔOI +4889张) | ΔOI/Volume 90.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4889张（+20.3% vs前日OI），连续性待观察（方向未知）
09-11 140.0C — Vol 9,849 | 最新价 $3.00 | OI 3855→7764 (ΔOI +3909张) | ΔOI/Volume 39.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3909张（+101.4% vs前日OI），连续性待观察（方向未知）
09-11 138.0C — Vol 6,634 | 最新价 $3.75 | OI 7870→10749 (ΔOI +2879张) | ΔOI/Volume 43.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2879张（+36.6% vs前日OI），连续性待观察（方向未知）
09-18 210.0C — Vol 2,029 | 最新价 $0.13 | OI 1187→2868 (ΔOI +1681张) | ΔOI/Volume 82.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1681张（+141.6% vs前日OI），连续性待观察（方向未知）
09-18 60.0P — Vol 1,641 | 最新价 $0.03 | OI 11937→13536 (ΔOI +1599张) | ΔOI/Volume 97.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1599张（+13.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 14,957 张（Put 1,599 / Call 13,358），跨 2 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +17.2k / P +4.1k ｜ Activity HIGH ｜ 2D
09-18  C +1.7k / P +3.9k ｜ Activity HIGH ｜ 9D
09-25  C +1.2k / P +3.1k ｜ Activity HIGH ｜ 16D
10-02  C -45 / P +2.6k ｜ Activity MEDIUM △ ｜ 23D

📆 09-11 Forward Structure
存量OI:      C 244.4k / P 159.3k
今日变化ΔOI: C +17.2k / P +4.1k
平值价格ATM:  C 3.90 / P 4.15
隐含波动率 ATM IV:  95.3%
净 delta 敞口变化 ΔOI Δ Exposure*: 302k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 150 ｜ +4,889 ｜ $0.75 ｜ 名义 $366.7k* ｜ +9.8%
C 140 ｜ +3,909 ｜ $2.70 ｜ 名义 $1.06M* ｜ +2.4%
C 144 ｜ -3,234 ｜ $1.70 ｜ 名义 $-549.8k* ｜ +5.4%
结构参考：150（+9.8%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 131（结算参考） ｜ Call Wall 150（+9.8%，弱）（OI 29.0k）
量化解读： 存量 Call 重｜ATM IV 95.3%｜历史 Rank 73%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 302,177 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 274.0k / P 203.8k
今日变化ΔOI: C +1.7k / P +3.9k
平值价格ATM:  C 7.85 / P 6.05
隐含波动率 ATM IV:  78.7%
净 delta 敞口变化 ΔOI Δ Exposure*: -262k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 100 ｜ -2,722 ｜ $36.43 ｜ 名义 $-9.92M* ｜ -26.8%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 110（结算参考）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 78.7%｜历史 Rank 73%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 261,589 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-25 Forward Structure
存量OI:      C 20.4k / P 33.3k
今日变化ΔOI: C +1.2k / P +3.1k
平值价格ATM:  C 8.65 / P 8.23
隐含波动率 ATM IV:  76.0%
净 delta 敞口变化 ΔOI Δ Exposure*: 4k shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 125（结算参考）
量化解读： 存量 Put 重｜ATM IV 76.0%｜历史 Rank 73%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 3,505 股（方向不可观测）——方向不可观测，观察点，非方向信号

10-02（MEDIUM △）仓位参考: Max Pain 130（结算参考） ｜ Call Wall 145（+6.1%，弱）（OI 2.6k）

📅 事件差分（观察，非因果）: 09-11（2D）ATM IV 95.3% vs 09-18 78.7%（差 +16.6pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-09/MSTR_morning.json