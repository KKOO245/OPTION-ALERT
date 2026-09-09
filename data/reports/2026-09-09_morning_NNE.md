# 期权晨报 2026-09-09（快照 11:03 ET）

📊 市场环境

SPY $763.65 ｜ QQQ $717.17
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
🟡 **单日价格波动**: -3.7%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-18 19C ΔOI +434（距现价 +1.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 19.35 → 今开 19.03（-1.7%） | 较昨收变动（含盘初走势） ｜ 今日高 19.33 ｜ 低 18.40

Options: P/C成交量 0.88 | OI比 0.60 | ATM IV 90.7% | Skew 1.8pp | Term 0.86 | ExpMove ±7.8%（近端） | Rank 18%
量化视角： IV 历史低位（Rank 18%，期权偏便宜）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜保护溢价薄（Skew 1.8pp）｜存量 Call 偏重（OI比 0.60）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.88×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.60×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（2D）±7.8% ｜ 09-18（9D）±8.4% ｜ 09-25（16D）±17.0% ｜ 10-02（23D）±16.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,994,204 | GEX Change vs 上次快照 328,226 | Flip: Primary Flip: 16.46（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 227 / LOW 87 / INVALID 126
结构观察区: Primary Flip 16.46（全链重定价，覆盖 95%）
Put Wall 20（弱结构｜现价低于该位 6.8%）
最近结构参考: Put Wall 20（现价低于该位 6.8%）
量化视角： 正 Gamma（299万，无历史分位）｜正 Gamma 增强（+33万）｜现价位于 Flip 上方 13.24%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 20（Put Wall，弱结构） / 19（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 16（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 30.0C — Vol 750 | 最新价 $0.15 | OI 9→753 (ΔOI +744张) | ΔOI/Volume 99.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增744张（+8266.7% vs前日OI），连续性待观察（方向未知）
09-11 20.0C — Vol 941 | 最新价 $0.30 | OI 224→870 (ΔOI +646张) | ΔOI/Volume 68.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增646张（+288.4% vs前日OI），连续性待观察（方向未知）
09-18 19.0C — Vol 674 | 最新价 $1.15 | OI 241→675 (ΔOI +434张) | ΔOI/Volume 64.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增434张（+180.1% vs前日OI），连续性待观察（方向未知）
09-11 21.0C — Vol 455 | 最新价 $0.11 | OI 165→587 (ΔOI +422张) | ΔOI/Volume 92.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增422张（+255.8% vs前日OI），连续性待观察（方向未知）
09-18 21.0C — Vol 468 | 最新价 $0.55 | OI 252→658 (ΔOI +406张) | ΔOI/Volume 86.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增406张（+161.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,652 张（Put 0 / Call 2,652），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +2.4k / P +0.4k ｜ Activity HIGH ｜ 2D
09-18  C +1.6k / P +23 ｜ Activity HIGH ｜ 9D
09-25  C +0.3k / P +43 ｜ Activity MEDIUM △ ｜ 16D
10-02  C +45 / P -65 ｜ Activity MEDIUM △ ｜ 23D

📆 09-11 Forward Structure
存量OI:      C 5.4k / P 3.2k
今日变化ΔOI: C +2.4k / P +0.4k
平值价格ATM:  C 1.03 / P 0.42
隐含波动率 ATM IV:  90.7%
净 delta 敞口变化 ΔOI Δ Exposure*: 42k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 20 ｜ +646 ｜ $0.18 ｜ 名义 $11.6k* ｜ +7.3%
C 19 ｜ +285 ｜ $0.50 ｜ 名义 $14.2k* ｜ +1.9%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：20（+7.3%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 19（结算参考）
量化解读： 存量 Call 重｜ATM IV 90.7%｜历史 Rank 18%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 41,576 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 6.7k / P 3.2k
今日变化ΔOI: C +1.6k / P +23
平值价格ATM:  C 0.97 / P 0.60
隐含波动率 ATM IV:  80.9%
净 delta 敞口变化 ΔOI Δ Exposure*: 41k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 19 ｜ +434 ｜ $0.87 ｜ 名义 $37.8k* ｜ +1.9%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：19（+1.9%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 19（结算参考） ｜ Put Wall 18（-3.4%）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 80.9%｜历史 Rank 18%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 41,130 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-25（MEDIUM △）仓位参考: Max Pain 18（结算参考）

10-02（MEDIUM △）Top ΔOI: 17P -68 ｜ 20C +16
10-02（MEDIUM △）仓位参考: Max Pain 19（结算参考） ｜ Put Wall 18.5（-0.8%）（OI 0.1k）

📅 事件差分（观察，非因果）: 09-11（2D）ATM IV 90.7% vs 09-18 80.9%（差 +9.9pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-09/NNE_morning.json