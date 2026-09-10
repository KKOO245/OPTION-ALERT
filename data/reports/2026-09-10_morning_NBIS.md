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
🔴 **事件差分**: 09-11（1D）ATM IV 95.9% vs 09-18 79.8%（差 +16.1pp），覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **单日价格波动**: -3.2%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-11 232P ΔOI +642（距现价 -0.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 240.35 → 今开 231.99（-3.5%） | 较昨收变动（含盘初走势） ｜ 今日高 238.33 ｜ 低 228.27

Options: P/C成交量 0.76 | OI比 0.75 | ATM IV 95.9% | Skew 0.3pp | Term 0.86 | ExpMove ±4.5%（近端） | Rank 32%
量化视角： IV 中性（Rank 32%）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜保护溢价薄（Skew 0.3pp）｜存量 Call 偏重（OI比 0.75）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.76×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.75×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（1D）±4.5% ｜ 09-18（8D）±9.6% ｜ 09-25（15D）±13.2% ｜ 10-02（22D）±16.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 3,687,945 | GEX Change vs 上次快照 -6,194,252 | Flip: Primary Flip: 227.12（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 569 / LOW 59 / INVALID 206
结构观察区: Primary Flip 227.12（全链重定价，覆盖 100%）
最近结构参考: Flip 227（现价高于该位 2.5%）
量化视角： 正 Gamma（369万，无历史分位）｜正 Gamma 减弱（619万）｜现价位于 Flip 上方 2.46%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 225（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 227（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 235.0P — Vol 1,494 | 最新价 $9.83 | OI 296→1249 (ΔOI +953张) | ΔOI/Volume 63.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增953张（+322.0% vs前日OI），连续性待观察（方向未知）
09-11 270.0C — Vol 2,399 | 最新价 $0.60 | OI 3213→3993 (ΔOI +780张) | ΔOI/Volume 32.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增780张（+24.3% vs前日OI），连续性待观察（方向未知）
09-18 242.5P — Vol 1,071 | 最新价 $13.40 | OI 56→802 (ΔOI +746张) | ΔOI/Volume 69.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增746张（+1332.1% vs前日OI），连续性待观察（方向未知）
09-11 232.5P — Vol 905 | 最新价 $3.44 | OI 211→853 (ΔOI +642张) | ΔOI/Volume 70.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增642张（+304.3% vs前日OI），连续性待观察（方向未知）
09-11 225.0P — Vol 1,148 | 最新价 $1.55 | OI 863→1335 (ΔOI +472张) | ΔOI/Volume 41.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增472张（+54.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,593 张（Put 2,813 / Call 780），跨 2 个期限｜近端保护（4 档，距现价 ≤5%，权利金合计约 $2M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +2.8k / P +3.0k ｜ Activity HIGH ｜ 1D
09-18  C +0.7k / P +3.6k ｜ Activity HIGH ｜ 8D
09-25  C -0.1k / P +0.4k ｜ Activity MEDIUM △ ｜ 15D
10-02  C +0.5k / P +0.4k ｜ Activity MEDIUM △ ｜ 22D

📆 09-11 Forward Structure
存量OI:      C 60.7k / P 45.8k
今日变化ΔOI: C +2.8k / P +3.0k
平值价格ATM:  C 4.80 / P 5.55
隐含波动率 ATM IV:  95.9%
净 delta 敞口变化 ΔOI Δ Exposure*: -154k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 232 ｜ +642 ｜ $5.55 ｜ 名义 $356.3k* ｜ -0.1%
P 225 ｜ +472 ｜ $2.51 ｜ 名义 $118.5k* ｜ -3.3%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：232（-0.1%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 225（结算参考） ｜ Call Wall 225（-3.3%，弱）（OI 4.9k） ｜ Put Wall 210（-9.8%，弱）（OI 2.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 95.9%｜历史 Rank 32%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 154,259 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 119.2k / P 165.6k
今日变化ΔOI: C +0.7k / P +3.6k
平值价格ATM:  C 10.85 / P 11.50
隐含波动率 ATM IV:  79.8%
净 delta 敞口变化 ΔOI Δ Exposure*: -143k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 235 ｜ +953 ｜ $12.70 ｜ 名义 $1.21M* ｜ +1.0%
P 242 ｜ +746 ｜ $17.47 ｜ 名义 $1.30M* ｜ +4.2%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：235（+1.0%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 220（结算参考）
量化解读： 存量 Put 重｜ATM IV 79.8%｜历史 Rank 32%（近端代理）｜净 delta 敞口 负 142,696 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-25（MEDIUM △）Top ΔOI: 300C -305 ｜ 215P +204
09-25（MEDIUM △）仓位参考: Max Pain 220（结算参考）

10-02（MEDIUM △）Top ΔOI: 250C +332 ｜ 235P +81
10-02（MEDIUM △）仓位参考: Max Pain 220（结算参考）

📅 事件差分（观察，非因果）: 09-11（1D）ATM IV 95.9% vs 09-18 79.8%（差 +16.1pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-10/NBIS_morning.json