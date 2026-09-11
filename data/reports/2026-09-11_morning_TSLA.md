# 期权晨报 2026-09-11（快照 10:40 ET）

📊 市场环境

SPY $764.35 ｜ QQQ $714.15
VIX 15.78 ↓11.6%（5D +8.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.1（fear）
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

🔍 重点速览
🟡 **近现价集中开仓**: 09-21 345P ΔOI +555（距现价 -5.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 363.56 → 今开 364.14（+0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 368.66 ｜ 低 361.60

Options: P/C成交量 0.52 | OI比 0.90 | ATM IV 56.0% | Skew -3.0pp | Term 0.71 | ExpMove ±2.4%（近端） | Rank 61%
量化视角： IV 中性（Rank 61%）｜期限结构倒挂（Term 0.71，近月 IV 高于远月）｜Put 保护异常便宜（Skew -3.0pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.52×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.90×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-14（3D）±2.4% ｜ 09-16（5D）±3.6% ｜ 09-18（7D）±4.4% ｜ 09-21（10D）±4.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 67,270,655 | GEX Change vs 上次快照 21,726,109 | Flip: Primary Flip: 356.75（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1302 / LOW 149 / INVALID 547
结构观察区: Primary Flip 356.75（全链重定价，覆盖 99%）
最近结构参考: Flip 357（现价高于该位 1.8%）
量化视角： 正 Gamma（6727万，无历史分位）｜正 Gamma 增强（+2173万）｜现价位于 Flip 上方 1.79%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 360（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 357（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 130.0P — Vol 5,262 | 最新价 $0.01 | OI 1475→6737 (ΔOI +5262张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5262张（+356.8% vs前日OI），连续性待观察（方向未知）
09-11 380.0C — Vol 53,377 | 最新价 $0.29 | OI 12555→17032 (ΔOI +4477张) | ΔOI/Volume 8.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4477张（+35.7% vs前日OI），连续性待观察（方向未知）
09-14 400.0C — Vol 8,592 | 最新价 $0.13 | OI 2744→6963 (ΔOI +4219张) | ΔOI/Volume 49.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4219张（+153.8% vs前日OI），连续性待观察（方向未知）
09-11 375.0C — Vol 64,329 | 最新价 $0.65 | OI 9785→13224 (ΔOI +3439张) | ΔOI/Volume 5.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3439张（+35.1% vs前日OI），连续性待观察（方向未知）
09-18 375.0C — Vol 8,227 | 最新价 $4.65 | OI 7442→10587 (ΔOI +3145张) | ΔOI/Volume 38.2% | Magnitude: HIGH | 完整度: HIGH
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
平值价格ATM:  C 5.00 / P 3.87
隐含波动率 ATM IV:  31.3%
净 delta 敞口变化 ΔOI Δ Exposure*: 124k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 367 ｜ +1,172 ｜ $2.60 ｜ 名义 $304.7k* ｜ +1.2%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：367（+1.2%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 365（结算参考）
量化解读： 存量 Call 重｜ATM IV 31.3%｜历史 Rank 61%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 123,824 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-16 Forward Structure
存量OI:      C 16.7k / P 10.7k
今日变化ΔOI: C +5.1k / P +2.7k
平值价格ATM:  C 7.05 / P 6.01
隐含波动率 ATM IV:  37.9%
净 delta 敞口变化 ΔOI Δ Exposure*: 2k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 340 ｜ +599 ｜ $0.68 ｜ 名义 $40.7k* ｜ -6.4%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：340（-6.4%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 362（结算参考） ｜ Put Wall 340（-6.4%，弱）（OI 1.3k）
量化解读： 存量 Call 重｜ATM IV 37.9%｜历史 Rank 61%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,204 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 512.5k / P 400.2k
今日变化ΔOI: C +25.0k / P -16.0k
平值价格ATM:  C 8.75 / P 7.38
隐含波动率 ATM IV:  39.6%
净 delta 敞口变化 ΔOI Δ Exposure*: 1.9M shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 440 ｜ -6,194 ｜ $74.19 ｜ 名义 $-45.95M* ｜ +21.2%
P 340 ｜ -3,838 ｜ $1.24 ｜ 名义 $-475.9k* ｜ -6.4%
P 290 ｜ -3,421 ｜ $0.15 ｜ 名义 $-51.3k* ｜ -20.1%
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 360（结算参考）
量化解读： 存量 Call 重｜ATM IV 39.6%｜历史 Rank 61%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,941,507 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-21 Forward Structure
存量OI:      C 4.1k / P 3.7k
今日变化ΔOI: C +1.0k / P +1.2k
平值价格ATM:  C 9.62 / P 8.15
隐含波动率 ATM IV:  36.6%
净 delta 敞口变化 ΔOI Δ Exposure*: 706 shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 345 ｜ +555 ｜ $2.36 ｜ 名义 $131.0k* ｜ -5.0%
C 380 ｜ +499 ｜ $3.45 ｜ 名义 $172.2k* ｜ +4.6%
C 390 ｜ -248 ｜ $1.83 ｜ 名义 $-45.4k* ｜ +7.4%
结构参考：380（+4.6%） / 345（-5.0%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 365（结算参考） ｜ Call Wall 380（+4.6%，弱）（OI 0.8k） ｜ Put Wall 345（-5.0%）（OI 0.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 36.6%｜历史 Rank 61%（近端代理）｜净 delta 敞口 正 706 股（方向不可观测）——方向不可观测，观察点，非方向信号

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-11/TSLA_morning.json