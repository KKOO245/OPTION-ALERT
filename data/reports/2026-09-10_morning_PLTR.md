# 期权晨报 2026-09-10（快照 10:56 ET）

📊 市场环境

SPY $758.27 ｜ QQQ $708.69
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
🟡 **近现价集中开仓**: 09-11 175C ΔOI +2,587（距现价 +4.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 169.53 → 今开 167.36（-1.3%） | 较昨收变动（含盘初走势） ｜ 今日高 169.00 ｜ 低 164.55

Options: P/C成交量 0.71 | OI比 0.74 | ATM IV 56.5% | Skew -1.9pp | Term 0.84 | ExpMove ±2.7%（近端） | Rank — (历史不足)
量化视角： 期限结构倒挂（Term 0.84，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.9pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.74）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.71×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.74×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（1D）±2.7% ｜ 09-18（8D）±5.8% ｜ 09-25（15D）±7.3% ｜ 10-02（22D）±9.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 11,287,147 | GEX Change vs 上次快照 -18,342,560 | Flip: Primary Flip: 166.74（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 584 / LOW 106 / INVALID 188
结构观察区: Primary Flip 166.74（全链重定价，覆盖 100%）
Put Wall 170（弱结构｜现价低于该位 1.3%） | Call Wall 180（弱结构｜现价低于该位 6.8%）
最近结构参考: Flip 167（现价高于该位 0.7%）
量化视角： 正 Gamma（1129万，无历史分位）｜正 Gamma 减弱（1834万）｜现价位于 Flip 上方 0.66%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 170（Put Wall，弱结构） / 170（MaxPain，仅结算参考） / 180（Call Wall，弱结构）。
• Gamma 区域：切换参考 167（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 180.0C — Vol 16,626 | 最新价 $0.29 | OI 15238→18621 (ΔOI +3383张) | ΔOI/Volume 20.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3383张（+22.2% vs前日OI），连续性待观察（方向未知）
09-11 175.0C — Vol 15,136 | 最新价 $0.86 | OI 12306→14893 (ΔOI +2587张) | ΔOI/Volume 17.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2587张（+21.0% vs前日OI），连续性待观察（方向未知）
09-18 177.5C — Vol 3,769 | 最新价 $2.30 | OI 890→3306 (ΔOI +2416张) | ΔOI/Volume 64.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2416张（+271.5% vs前日OI），连续性待观察（方向未知）
09-18 180.0C — Vol 7,719 | 最新价 $1.68 | OI 13666→16041 (ΔOI +2375张) | ΔOI/Volume 30.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2375张（+17.4% vs前日OI），连续性待观察（方向未知）
09-11 167.5P — Vol 13,020 | 最新价 $1.74 | OI 3640→5754 (ΔOI +2114张) | ΔOI/Volume 16.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2114张（+58.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 12,875 张（Put 2,114 / Call 10,761），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +3.9k / P +4.5k ｜ Activity MEDIUM △ ｜ 1D
09-18  C +4.6k / P +1.7k ｜ Activity MEDIUM △ ｜ 8D
09-25  C +1.6k / P +2.2k ｜ Activity HIGH ｜ 15D
10-02  C +0.4k / P +0.4k ｜ Activity MEDIUM △ ｜ 22D

📆 09-11 Forward Structure
存量OI:      C 151.5k / P 111.4k
今日变化ΔOI: C +3.9k / P +4.5k
平值价格ATM:  C 2.91 / P 1.55
隐含波动率 ATM IV:  56.5%
净 delta 敞口变化 ΔOI Δ Exposure*: 51k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 180 ｜ +3,383 ｜ $0.14 ｜ 名义 $47.4k* ｜ +7.2%
C 175 ｜ +2,587 ｜ $0.46 ｜ 名义 $119.0k* ｜ +4.3%
P 167 ｜ +2,114 ｜ $1.55 ｜ 名义 $327.7k* ｜ -0.2%
结构参考：180（+7.2%） / 167（-0.2%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 170（结算参考） ｜ Call Wall 180（+7.2%，弱）（OI 18.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 56.5%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 51,122 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（MEDIUM △）Top ΔOI: 135C -5,651 ｜ 177C +2,416
09-18（MEDIUM △）仓位参考: Max Pain 150（结算参考）

📆 09-25 Forward Structure
存量OI:      C 22.6k / P 33.3k
今日变化ΔOI: C +1.6k / P +2.2k
平值价格ATM:  C 6.55 / P 5.70
隐含波动率 ATM IV:  47.3%
净 delta 敞口变化 ΔOI Δ Exposure*: -4k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 155 ｜ +1,447 ｜ $1.71 ｜ 名义 $247.4k* ｜ -7.7%
P 152 ｜ +594 ｜ $1.41 ｜ 名义 $83.8k* ｜ -9.1%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：155（-7.7%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 175（结算参考） ｜ Put Wall 170（+1.3%）（OI 7.3k）
量化解读： 存量 Put 重｜ATM IV 47.3%｜净 delta 敞口 负 3,724 股（方向不可观测）——方向不可观测，观察点，非方向信号

10-02（MEDIUM △）Top ΔOI: 155P +180 ｜ 150C +102
10-02（MEDIUM △）仓位参考: Max Pain 175（结算参考） ｜ Call Wall 180（+7.2%，弱）（OI 2.5k） ｜ Put Wall 160（-4.7%，弱）（OI 2.7k）

📅 事件差分（观察，非因果）: 09-11（1D）ATM IV 56.5% vs 09-18 48.0%（差 +8.5pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-10/PLTR_morning.json