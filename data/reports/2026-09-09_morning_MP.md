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
🟡 **事件差分**: 09-11 ATM IV 80.5% vs 09-18 70.0%（差 +10.5pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 09-11 54P ΔOI +642（距现价 -2.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 55.37 → 今开 55.11（-0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 56.33 ｜ 低 54.66

Options: P/C成交量 0.62 | OI比 0.74 | ATM IV 80.5% | Skew -5.8pp | Term 0.83 | ExpMove ±4.4%（近端） | Rank 70%
量化视角： IV 中性（Rank 70%）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜Put 保护异常便宜（Skew -5.8pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.74）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.62×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.74×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（2D）±4.4% ｜ 09-18（9D）±9.1% ｜ 09-25（16D）±11.8% ｜ 10-02（23D）±14.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,081,237 | GEX Change vs 上次快照 838,812 | Flip: Primary Flip: 54.26（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 271 / LOW 60 / INVALID 79
结构观察区: Primary Flip 54.26（全链重定价，覆盖 100%）
Call Wall 60（弱结构｜现价低于该位 7.8%）
最近结构参考: Flip 54（现价高于该位 2.0%）
量化视角： 正 Gamma（208万，无历史分位）｜正 Gamma 增强（+84万）｜现价位于 Flip 上方 2.00%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 55（MaxPain，仅结算参考）；上方 60（Call Wall，弱结构）。
• Gamma 区域：切换参考 54（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 54.0P — Vol 740 | 最新价 $0.78 | OI 315→957 (ΔOI +642张) | ΔOI/Volume 86.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增642张（+203.8% vs前日OI），连续性待观察（方向未知）
09-11 60.0C — Vol 1,405 | 最新价 $0.35 | OI 1021→1597 (ΔOI +576张) | ΔOI/Volume 41.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增576张（+56.4% vs前日OI），连续性待观察（方向未知）
09-18 55.0C — Vol 2,037 | 最新价 $2.71 | OI 3487→3945 (ΔOI +458张) | ΔOI/Volume 22.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增458张（+13.1% vs前日OI），连续性待观察（方向未知）
09-11 58.0C — Vol 661 | 最新价 $0.65 | OI 384→742 (ΔOI +358张) | ΔOI/Volume 54.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增358张（+93.2% vs前日OI），连续性待观察（方向未知）
09-18 60.0C — Vol 818 | 最新价 $1.16 | OI 6347→6703 (ΔOI +356张) | ΔOI/Volume 43.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增356张（+5.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,390 张（Put 642 / Call 1,748），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +2.3k / P +1.2k ｜ Activity HIGH ｜ 2D
09-18  C +1.5k / P +0.2k ｜ Activity MEDIUM △ ｜ 9D
09-25  C +0.3k / P +0.2k ｜ Activity MEDIUM △ ｜ 16D
10-02  C +0.2k / P +0.1k ｜ Activity MEDIUM △ ｜ 23D

📆 09-11 Forward Structure
存量OI:      C 9.6k / P 7.1k
今日变化ΔOI: C +2.3k / P +1.2k
平值价格ATM:  C 1.40 / P 1.03
隐含波动率 ATM IV:  80.5%
净 delta 敞口变化 ΔOI Δ Exposure*: -6k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 54 ｜ +642 ｜ $0.78 ｜ 名义 $50.1k* ｜ -2.4%
C 60 ｜ +576 ｜ $0.23 ｜ 名义 $13.2k* ｜ +8.4%
C 58 ｜ +358 ｜ $0.40 ｜ 名义 $14.3k* ｜ +4.8%
结构参考：60（+8.4%） / 54（-2.4%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 55（结算参考） ｜ Call Wall 60（+8.4%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 80.5%｜历史 Rank 70%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 5,856 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（MEDIUM △）Top ΔOI: 55C +458 ｜ 60C +356
09-18（MEDIUM △）仓位参考: Max Pain 55（结算参考） ｜ Put Wall 55（-0.6%，弱）（OI 9.1k）

09-25（MEDIUM △）Top ΔOI: 52P +57
09-25（MEDIUM △）仓位参考: Max Pain 52（结算参考） ｜ Call Wall 60（+8.4%，弱）（OI 0.7k）

10-02（MEDIUM △）Top ΔOI: 58P +95 ｜ 52P -83
10-02（MEDIUM △）仓位参考: Max Pain 59（结算参考） ｜ Put Wall 50（-9.7%）（OI 1.2k）

📅 事件差分（观察，非因果）: 09-11（2D）ATM IV 80.5% vs 09-18 70.0%（差 +10.5pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-09/MP_morning.json