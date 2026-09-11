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

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 09-14 58P ΔOI +1,578（距现价 -0.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-16 58P ΔOI +3,582 占该期限总 OI 21.9%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 58.73 → 收盘 58.12（-1.0%） ｜ 今日高 58.96 ｜ 低 57.88 ｜ 昨收 57.50 → 收盘 58.12（+1.1%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-09-18，窗口结束前不做对错判定）

Options: P/C成交量 0.91 | OI比 0.64 | ATM IV 50.3% | Skew -73.4pp | Term 0.80 | ExpMove ±1.8%（近端） | Rank 83%
量化视角： IV 历史高位（Rank 83%，期权偏贵）｜期限结构倒挂（Term 0.80，近月 IV 高于远月）｜Put 保护异常便宜（Skew -73.4pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.64）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.91×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.64×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-14（3D）±1.8% ｜ 09-16（5D）±3.2% ｜ 09-18（7D）±4.2% ｜ 09-21（10D）±4.6%
   ⇒ IV–VIX Spread: +34.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 50,387,491 | GEX Change vs 上次快照 -24,479,775 | Flip: Primary Flip: 56.13（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 898 / LOW 204 / INVALID 358
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 56.13（全链重定价，覆盖 94%）
最近结构参考: Flip 56（现价高于该位 3.5%）
量化视角： 正 Gamma（5039万，无历史分位）｜正 Gamma 减弱（2448万）｜现价位于 Flip 上方 3.54%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 59（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 56（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 64.0C — Vol 12,371 | 最新价 $1.21 | OI 32244→44281 (ΔOI +12037张) | ΔOI/Volume 97.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12037张（+37.3% vs前日OI），连续性待观察（方向未知）
09-30 53.0P — Vol 37 | 最新价 $0.40 | OI 1316→11129 (ΔOI +9813张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9813张（+745.7% vs前日OI），连续性待观察（方向未知）
10-02 50.0P — Vol 15 | 最新价 $0.20 | OI 619→7090 (ΔOI +6471张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6471张（+1045.4% vs前日OI），连续性待观察（方向未知）
09-16 58.0P — Vol 1,451 | 最新价 $0.87 | OI 341→3923 (ΔOI +3582张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3582张（+1050.4% vs前日OI），连续性待观察（方向未知）
09-30 50.0P — Vol 251 | 最新价 $0.16 | OI 3418→6788 (ΔOI +3370张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3370张（+98.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 35,273 张（Put 23,236 / Call 12,037），跨 4 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-14  C +5.9k / P +3.0k ｜ Activity HIGH ｜ 3D
09-16  C +1.4k / P +5.1k ｜ Activity HIGH ｜ 5D
09-18  C -5.4k / P -2.1k ｜ Activity MEDIUM △ ｜ 7D
09-21  C +0.4k / P +0.8k ｜ Activity HIGH ｜ 10D

📆 09-14 Forward Structure
存量OI:      C 16.5k / P 7.9k
今日变化ΔOI: C +5.9k / P +3.0k
平值价格ATM:  C 0.58 / P 0.46
隐含波动率 ATM IV:  25.1%
净 delta 敞口变化 ΔOI Δ Exposure*: 7k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 58 ｜ +1,578 ｜ $0.46 ｜ 名义 $72.6k* ｜ -0.2%
C 63 ｜ +1,257 ｜ $0.02 ｜ 名义 $2.5k* ｜ +8.4%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：63（+8.4%） / 58（-0.2%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 59（结算参考） ｜ Put Wall 58（-0.2%）（OI 2.5k）
量化解读： 存量 Call 重｜ATM IV 25.1%｜历史 Rank 83%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 7,200 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-16 Forward Structure
存量OI:      C 7.5k / P 8.8k
今日变化ΔOI: C +1.4k / P +5.1k
平值价格ATM:  C 1.01 / P 0.87
隐含波动率 ATM IV:  34.2%
净 delta 敞口变化 ΔOI Δ Exposure*: -140k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 58 ｜ +3,582 ｜ $0.87 ｜ 名义 $311.6k* ｜ -0.2%
P 57 ｜ +524 ｜ $0.47 ｜ 名义 $24.6k* ｜ -1.9%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：58（-0.2%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 60（结算参考） ｜ Put Wall 58（-0.2%）（OI 3.9k）
量化解读： 存量两侧均衡｜ATM IV 34.2%｜历史 Rank 83%（近端代理）｜净 delta 敞口 负 140,221 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（MEDIUM △）Top ΔOI: 63C -10,084 ｜ 80P -3,877
09-18（MEDIUM △）仓位参考: Max Pain 60（结算参考）

📆 09-21 Forward Structure
存量OI:      C 1.3k / P 1.2k
今日变化ΔOI: C +0.4k / P +0.8k
平值价格ATM:  C 1.42 / P 1.26
隐含波动率 ATM IV:  34.9%
净 delta 敞口变化 ΔOI Δ Exposure*: -28k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 59 ｜ +298 ｜ $1.84 ｜ 名义 $54.8k* ｜ +1.5%
P 57 ｜ +219 ｜ $0.83 ｜ 名义 $18.2k* ｜ -1.9%
C 60 ｜ +97 ｜ $0.69 ｜ 名义 $6.7k* ｜ +3.2%
结构参考：59（+1.5%） / 57（-1.9%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 59（结算参考） ｜ Put Wall 59（+1.5%，弱）（OI 0.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 34.9%｜历史 Rank 83%（近端代理）｜净 delta 敞口 负 27,710 股（方向不可观测）——方向不可观测，观察点，非方向信号

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-11/SLV_evening.json