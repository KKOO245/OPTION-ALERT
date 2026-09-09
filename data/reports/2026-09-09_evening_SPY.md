# 期权晚报 2026-09-09（快照 18:23 ET）

📊 市场环境

SPY $762.40 ｜ QQQ $716.31
VIX 16.46 ↑4.7%（5D +8.3%） ｜ Vol Regime: NORMAL
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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 764.08 → 收盘 762.40（-0.2%） ｜ 今日高 764.47 ｜ 低 760.94 ｜ 昨收 765.96 → 收盘 762.40（-0.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.30 | OI比 1.94 | ATM IV 11.9% | Skew -1.1pp | Term 1.12 | ExpMove ±0.6%（近端） | Rank 42%
量化视角： IV 中性（Rank 42%）｜期限结构正常（Term 1.12）｜Put 保护异常便宜（Skew -1.1pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 1.30）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.30×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.94×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 27% ｜ P/C OI(近端) 58%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 27%）｜近端持仓结构中性（P/C OI 分位 58%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-10（1D）±0.6% ｜ 09-11（2D）±0.9% ｜ 09-14（5D）±1.2% ｜ 09-15（6D）±1.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,332,478,752 | GEX Change vs 上次快照 -65,877,536 | Flip: Primary Flip: 770.18（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 2665 / LOW 391 / INVALID 1162
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 770.18（全链重定价，覆盖 95%）
Call Wall 800（弱结构｜现价低于该位 4.7%）
最近结构参考: Flip 770（现价低于该位 1.0%）
量化视角： 负 Gamma（13.32亿，历史分位 27%，中性区）｜负 Gamma 加深（6588万）｜现价位于 Flip 下方 1.01%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 767（MaxPain，仅结算参考） / 800（Call Wall，弱结构）。
• Gamma 区域：切换参考 770（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 604.0P — Vol 1,200 | 最新价 $0.05 | OI 1339→22328 (ΔOI +20989张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20989张（+1567.5% vs前日OI），连续性待观察（方向未知）
09-18 740.0P — Vol 11,906 | 最新价 $1.65 | OI 49818→69892 (ΔOI +20074张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20074张（+40.3% vs前日OI），连续性待观察（方向未知）
09-18 605.0P — Vol 145 | 最新价 $0.05 | OI 52294→71508 (ΔOI +19214张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增19214张（+36.7% vs前日OI），连续性待观察（方向未知）
09-11 763.0P — Vol 24,576 | 最新价 $3.37 | OI 10791→29118 (ΔOI +18327张) | ΔOI/Volume 74.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18327张（+169.8% vs前日OI），连续性待观察（方向未知）
09-14 700.0P — Vol 8,334 | 最新价 $0.06 | OI 501→16336 (ΔOI +15835张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15835张（+3160.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 94,439 张（Put 94,439 / Call 0），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $9M，买/卖方向不可观测）｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-10  C +0 / P +0 ｜ Activity LOW ｜ 1D
09-11  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-14  C +0 / P +0 ｜ Activity LOW ｜ 5D
09-15  C +0 / P +0 ｜ Activity LOW ｜ 6D

📆 09-10 Forward Structure
存量OI:      C 70.6k / P 74.1k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 2.50 / P 1.80
隐含波动率 ATM IV:  13.3%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 766（结算参考） ｜ Call Wall 770（+1.0%）（OI 7.1k） ｜ Put Wall 695（-8.8%，弱）（OI 8.0k）
量化解读： 存量两侧均衡｜ATM IV 13.3%｜历史 Rank 42%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-11（Activity LOW）仓位参考: Max Pain 768（结算参考） ｜ Call Wall 777（+1.9%，弱）（OI 20.4k） ｜ Put Wall 760（-0.3%）（OI 52.2k）

09-14（Activity LOW）仓位参考: Max Pain 765（结算参考） ｜ Call Wall 800（+4.9%，弱）（OI 5.5k） ｜ Put Wall 700（-8.2%）（OI 16.3k）

09-15（Activity LOW）仓位参考: Max Pain 765（结算参考） ｜ Call Wall 795（+4.3%，弱）（OI 2.8k） ｜ Put Wall 755（-1.0%）（OI 27.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-09/SPY_evening.json