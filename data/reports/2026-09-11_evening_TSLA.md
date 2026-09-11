# 期权晚报 2026-09-11（快照 16:40 ET）

📊 市场环境

SPY $764.29 ｜ QQQ $714.88
VIX 15.84 ↓11.2%（5D +9.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-11 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 0.3 ｜ 前值 0.2　✅ 今日已公布
- 周五 09-11 08:30　【高】Inflation Rate YoY　预测 3.4 ｜ 实际 3.4 ｜ 前值 3.4　✅ 今日已公布
- 周五 09-11 08:30　【高】Inflation Rate MoM　预测 0.4 ｜ 实际 0.4 ｜ 前值 0.1　✅ 今日已公布
- 周五 09-11 08:30　【高】Core Inflation Rate YoY　预测 2.4 ｜ 实际 2.4 ｜ 前值 2.5　✅ 今日已公布
- 周五 09-11 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 51 ｜ 实际 47.8 ｜ 前值 51.7　✅ 今日已公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 364.14 → 收盘 365.44（+0.4%） ｜ 今日高 368.66 ｜ 低 361.60 ｜ 昨收 363.56 → 收盘 365.44（+0.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.64 | OI比 0.90 | ATM IV 21.6% | Skew -2.9pp | Term 1.80 | ExpMove ±1.9%（近端） | Rank 10%
量化视角： IV 历史低位（Rank 10%，期权偏便宜）｜期限结构正常偏陡（Term 1.80）｜Put 保护异常便宜（Skew -2.9pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.64×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.90×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-14（3D）±1.9% ｜ 09-16（5D）±3.3% ｜ 09-18（7D）±4.2% ｜ 09-21（10D）±4.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 61,024,498 | GEX Change vs 上次快照 -6,246,157 | Flip: Primary Flip: 356.87（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 85%（带内） ｜ IV 有效性: VALID 1147 / LOW 204 / INVALID 647
结构观察区: Primary Flip 356.87（全链重定价，覆盖 85%）
Call Wall 400（现价低于该位 8.6%）
最近结构参考: Flip 357（现价高于该位 2.4%）
量化视角： 正 Gamma（6102万，无历史分位）｜正 Gamma 减弱（625万）｜现价位于 Flip 上方 2.40%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 360（MaxPain，仅结算参考）；上方 400（Call Wall）。
• Gamma 区域：切换参考 357（全链重定价，覆盖 85%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 130.0P — Vol 7,184 | 最新价 $0.01 | OI 1475→6737 (ΔOI +5262张) | ΔOI/Volume 73.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5262张（+356.8% vs前日OI），连续性待观察（方向未知）
09-11 380.0C — Vol 29,915 | 最新价 $0.01 | OI 12555→17032 (ΔOI +4477张) | ΔOI/Volume 15.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4477张（+35.7% vs前日OI），连续性待观察（方向未知）
09-14 400.0C — Vol 2,980 | 最新价 $0.04 | OI 2744→6963 (ΔOI +4219张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4219张（+153.8% vs前日OI），连续性待观察（方向未知）
09-11 375.0C — Vol 72,432 | 最新价 $0.01 | OI 9785→13224 (ΔOI +3439张) | ΔOI/Volume 4.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3439张（+35.1% vs前日OI），连续性待观察（方向未知）
09-18 375.0C — Vol 6,361 | 最新价 $4.03 | OI 7442→10587 (ΔOI +3145张) | ΔOI/Volume 49.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3145张（+42.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 20,542 张（Put 5,262 / Call 15,280），跨 4 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-14  C +11.3k / P +4.7k ｜ Activity HIGH ｜ 3D
09-16  C +5.1k / P +2.7k ｜ Activity HIGH ｜ 5D
09-18  C +25.0k / P -16.0k ｜ Activity HIGH ｜ 7D
09-21  C +1.0k / P +1.2k ｜ Activity HIGH ｜ 10D

📆 09-14 Forward Structure
存量OI:      C 34.8k / P 29.2k
今日变化ΔOI: C +11.3k / P +4.7k
平值价格ATM:  C 3.69 / P 3.24
隐含波动率 ATM IV:  25.9%
净 delta 敞口变化 ΔOI Δ Exposure*: 152k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 400 ｜ +4,219 ｜ $0.04 ｜ 名义 $16.9k* ｜ +9.5%
C 367 ｜ +1,172 ｜ $2.60 ｜ 名义 $304.7k* ｜ +0.6%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：400（+9.5%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 365（结算参考） ｜ Call Wall 400（+9.5%）（OI 7.0k）
量化解读： 存量 Call 重｜ATM IV 25.9%｜历史 Rank 10%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 152,248 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-16 Forward Structure
存量OI:      C 16.7k / P 10.7k
今日变化ΔOI: C +5.1k / P +2.7k
平值价格ATM:  C 6.30 / P 5.62
隐含波动率 ATM IV:  35.0%
净 delta 敞口变化 ΔOI Δ Exposure*: 12k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 400 ｜ +1,342 ｜ $0.22 ｜ 名义 $29.5k* ｜ +9.5%
P 340 ｜ +599 ｜ $0.45 ｜ 名义 $27.0k* ｜ -7.0%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：400（+9.5%） / 340（-7.0%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 362（结算参考） ｜ Call Wall 400（+9.5%，弱）（OI 2.3k） ｜ Put Wall 340（-7.0%，弱）（OI 1.3k）
量化解读： 存量 Call 重｜ATM IV 35.0%｜历史 Rank 10%（近端代理）｜净 delta 敞口 正 12,484 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 512.5k / P 400.2k
今日变化ΔOI: C +25.0k / P -16.0k
平值价格ATM:  C 7.95 / P 7.25
隐含波动率 ATM IV:  37.4%
净 delta 敞口变化 ΔOI Δ Exposure*: 2.0M shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 440 ｜ -6,194 ｜ $73.95 ｜ 名义 $-45.80M* ｜ +20.4%
P 340 ｜ -3,838 ｜ $0.88 ｜ 名义 $-337.7k* ｜ -7.0%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 360（结算参考）
量化解读： 存量 Call 重｜ATM IV 37.4%｜历史 Rank 10%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,963,080 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-21 Forward Structure
存量OI:      C 4.1k / P 3.7k
今日变化ΔOI: C +1.0k / P +1.2k
平值价格ATM:  C 9.10 / P 8.20
隐含波动率 ATM IV:  35.0%
净 delta 敞口变化 ΔOI Δ Exposure*: 6k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 345 ｜ +555 ｜ $1.80 ｜ 名义 $99.9k* ｜ -5.6%
C 380 ｜ +499 ｜ $3.55 ｜ 名义 $177.1k* ｜ +4.0%
C 390 ｜ -248 ｜ $1.73 ｜ 名义 $-42.9k* ｜ +6.7%
结构参考：380（+4.0%） / 345（-5.6%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 365（结算参考） ｜ Call Wall 380（+4.0%，弱）（OI 0.8k） ｜ Put Wall 345（-5.6%）（OI 0.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 35.0%｜历史 Rank 10%（近端代理）｜净 delta 敞口 正 5,871 股（方向不可观测）——方向不可观测，观察点，非方向信号

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-11/TSLA_evening.json