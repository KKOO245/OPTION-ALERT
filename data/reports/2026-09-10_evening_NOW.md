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
🔴 **事件差分**: 09-11（1D）ATM IV 72.7% vs 09-18 55.0%（差 +17.6pp），覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 09-11 132P ΔOI +906（距现价 +0.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NOW

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NOW: 今开 130.64 → 收盘 131.17（+0.4%） ｜ 今日高 134.65 ｜ 低 130.64 ｜ 昨收 131.11 → 收盘 131.17（+0.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.48 | OI比 0.92 | ATM IV 72.7% | Skew 1.0pp | Term 0.74 | ExpMove ±3.1%（近端） | Rank — (历史不足)
量化视角： 期限结构倒挂（Term 0.74，近月 IV 高于远月）｜保护溢价薄（Skew 1.0pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.48×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.92×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-11（1D）±3.1% ｜ 09-18（8D）±6.6% ｜ 09-25（15D）±8.7% ｜ 10-02（22D）±10.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 5,575,461 | GEX Change vs 上次快照 -2,676,791 | Flip: Primary Flip: 128.24（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 587 / LOW 89 / INVALID 164
结构观察区: Primary Flip 128.24（全链重定价，覆盖 100%）
最近结构参考: Flip 128（现价高于该位 2.3%）
量化视角： 正 Gamma（558万，无历史分位）｜正 Gamma 减弱（268万）｜现价位于 Flip 上方 2.29%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 135（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 128（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 132.0P — Vol 1,460 | 最新价 $2.50 | OI 683→1589 (ΔOI +906张) | ΔOI/Volume 62.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增906张（+132.7% vs前日OI），连续性待观察（方向未知）
09-11 140.0C — Vol 4,110 | 最新价 $0.13 | OI 3094→3720 (ΔOI +626张) | ΔOI/Volume 15.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增626张（+20.2% vs前日OI），连续性待观察（方向未知）
09-18 141.0C — Vol 100 | 最新价 $1.25 | OI 864→1371 (ΔOI +507张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增507张（+58.7% vs前日OI），连续性待观察（方向未知）
09-18 142.0C — Vol 178 | 最新价 $1.03 | OI 263→672 (ΔOI +409张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增409张（+155.5% vs前日OI），值得跟踪（方向未知）
09-25 145.0C — Vol 446 | 最新价 $1.53 | OI 1006→1412 (ΔOI +406张) | ΔOI/Volume 91.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增406张（+40.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,854 张（Put 906 / Call 1,948），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +2.5k / P +1.5k ｜ Activity HIGH ｜ 1D
09-18  C +0.7k / P +1.0k ｜ Activity MEDIUM △ ｜ 8D
09-25  C +0.5k / P +0.2k ｜ Activity HIGH ｜ 15D
10-02  C +0.2k / P +0.3k ｜ Activity MEDIUM △ ｜ 22D

📆 09-11 Forward Structure
存量OI:      C 26.6k / P 24.5k
今日变化ΔOI: C +2.5k / P +1.5k
平值价格ATM:  C 2.10 / P 1.96
隐含波动率 ATM IV:  72.7%
净 delta 敞口变化 ΔOI Δ Exposure*: 44k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 132 ｜ +906 ｜ $2.50 ｜ 名义 $226.5k* ｜ +0.6%
C 140 ｜ +626 ｜ $0.13 ｜ 名义 $8.1k* ｜ +6.7%
C 136 ｜ +368 ｜ $0.51 ｜ 名义 $18.8k* ｜ +3.7%
结构参考：132（+0.6%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 135（结算参考） ｜ Call Wall 140（+6.7%，弱）（OI 3.7k） ｜ Put Wall 130（-0.9%，弱）（OI 2.1k）
量化解读： 存量两侧均衡｜ATM IV 72.7%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 43,673 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（MEDIUM △）Top ΔOI: 141C +507 ｜ 142C +409
09-18（MEDIUM △）仓位参考: Max Pain 120（结算参考） ｜ Call Wall 120（-8.5%，弱）（OI 9.9k）

📆 09-25 Forward Structure
存量OI:      C 7.4k / P 8.1k
今日变化ΔOI: C +0.5k / P +0.2k
平值价格ATM:  C 5.91 / P 5.44
隐含波动率 ATM IV:  53.5%
净 delta 敞口变化 ΔOI Δ Exposure*: 11k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 145 ｜ +406 ｜ $1.53 ｜ 名义 $62.1k* ｜ +10.5%
C 137 ｜ +49 ｜ $3.55 ｜ 名义 $17.4k* ｜ +4.4%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：145（+10.5%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 131（结算参考）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 53.5%｜净 delta 敞口 正 11,192 股（方向不可观测）——方向不可观测，观察点，非方向信号

10-02（MEDIUM △）Top ΔOI: 122P +50 ｜ 123P +41
10-02（MEDIUM △）仓位参考: Max Pain 132（结算参考）

📅 事件差分（观察，非因果）: 09-11（1D）ATM IV 72.7% vs 09-18 55.0%（差 +17.6pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-10/NOW_evening.json