# 期权晨报 2026-09-11（快照 10:20 ET）

📊 市场环境

SPY $766.00 ｜ QQQ $716.23
VIX 15.94 ↓10.7%（5D +9.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.5（fear）
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
🟡 **单日价格波动**: +2.2%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-14 58P ΔOI +1,578（距现价 -1.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-16 58P ΔOI +3,582 占该期限总 OI 21.9%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 57.50 → 今开 58.73（+2.1%） | 较昨收变动（含盘初走势） ｜ 今日高 58.96 ｜ 低 58.45

Options: P/C成交量 0.74 | OI比 0.64 | ATM IV 51.9% | Skew -1.1pp | Term 0.82 | ExpMove ±2.4%（近端） | Rank 85%
量化视角： IV 历史高位（Rank 85%，期权偏贵）｜期限结构倒挂（Term 0.82，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.1pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.64）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.74×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.64×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-14（3D）±2.4% ｜ 09-16（5D）±4.0% ｜ 09-18（7D）±4.8% ｜ 09-21（10D）±5.4%
   ⇒ IV–VIX Spread: +36.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 72,000,429 | GEX Change vs 上次快照 35,764,644 | Flip: Primary Flip: 56.89（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 940 / LOW 229 / INVALID 291
结构观察区: Primary Flip 56.89（全链重定价，覆盖 98%）
最近结构参考: Flip 57（现价高于该位 3.3%）
量化视角： 正 Gamma（7200万，无历史分位）｜正 Gamma 增强（+3576万）｜现价位于 Flip 上方 3.32%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 59（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 57（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 64.0C — Vol 12,411 | 最新价 $1.27 | OI 32244→44281 (ΔOI +12037张) | ΔOI/Volume 97.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12037张（+37.3% vs前日OI），连续性待观察（方向未知）
09-30 53.0P — Vol 11,128 | 最新价 $0.69 | OI 1316→11129 (ΔOI +9813张) | ΔOI/Volume 88.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9813张（+745.7% vs前日OI），连续性待观察（方向未知）
10-02 50.0P — Vol 6,887 | 最新价 $0.32 | OI 619→7090 (ΔOI +6471张) | ΔOI/Volume 94.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6471张（+1045.4% vs前日OI），连续性待观察（方向未知）
09-16 58.0P — Vol 3,776 | 最新价 $1.69 | OI 341→3923 (ΔOI +3582张) | ΔOI/Volume 94.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3582张（+1050.4% vs前日OI），连续性待观察（方向未知）
09-30 50.0P — Vol 3,845 | 最新价 $0.30 | OI 3418→6788 (ΔOI +3370张) | ΔOI/Volume 87.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3370张（+98.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 35,273 张（Put 23,236 / Call 12,037），跨 4 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-14  C +5.9k / P +3.0k ｜ Activity HIGH ｜ 3D
09-16  C +1.4k / P +5.1k ｜ Activity HIGH ｜ 5D
09-18  C -5.4k / P -2.1k ｜ Activity HIGH ｜ 7D
09-21  C +0.4k / P +0.8k ｜ Activity HIGH ｜ 10D

📆 09-14 Forward Structure
存量OI:      C 16.5k / P 7.9k
今日变化ΔOI: C +5.9k / P +3.0k
平值价格ATM:  C 0.51 / P 0.90
隐含波动率 ATM IV:  30.6%
净 delta 敞口变化 ΔOI Δ Exposure*: 52k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 58 ｜ +1,578 ｜ $0.38 ｜ 名义 $60.0k* ｜ -1.3%
C 63 ｜ +1,257 ｜ $0.03 ｜ 名义 $3.8k* ｜ +7.2%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：63（+7.2%） / 58（-1.3%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 59（结算参考） ｜ Put Wall 58（-1.3%）（OI 2.5k）
量化解读： 存量 Call 重｜ATM IV 30.6%｜历史 Rank 85%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 51,504 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-16 Forward Structure
存量OI:      C 7.5k / P 8.8k
今日变化ΔOI: C +1.4k / P +5.1k
平值价格ATM:  C 1.06 / P 1.30
隐含波动率 ATM IV:  40.6%
净 delta 敞口变化 ΔOI Δ Exposure*: -106k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 58 ｜ +3,582 ｜ $0.83 ｜ 名义 $297.3k* ｜ -1.3%
P 57 ｜ +524 ｜ $0.46 ｜ 名义 $24.1k* ｜ -3.0%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：58（-1.3%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 60（结算参考） ｜ Call Wall 64（+8.9%）（OI 1.8k） ｜ Put Wall 58（-1.3%）（OI 3.9k）
量化解读： 存量两侧均衡｜ATM IV 40.6%｜历史 Rank 85%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 105,935 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 962.1k / P 461.2k
今日变化ΔOI: C -5.4k / P -2.1k
平值价格ATM:  C 1.20 / P 1.60
隐含波动率 ATM IV:  42.5%
净 delta 敞口变化 ΔOI Δ Exposure*: 707k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 63 ｜ -10,084 ｜ $0.30 ｜ 名义 $-302.5k* ｜ +7.2%
P 80 ｜ -3,877 ｜ $21.88 ｜ 名义 $-8.48M* ｜ +36.1%
C 60 ｜ +2,999 ｜ $0.87 ｜ 名义 $260.9k* ｜ +2.1%
结构参考：60（+2.1%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 60（结算参考）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 42.5%｜历史 Rank 85%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 707,469 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-21 Forward Structure
存量OI:      C 1.3k / P 1.2k
今日变化ΔOI: C +0.4k / P +0.8k
平值价格ATM:  C 1.41 / P 1.78
隐含波动率 ATM IV:  39.5%
净 delta 敞口变化 ΔOI Δ Exposure*: -22k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 59 ｜ +298 ｜ $1.78 ｜ 名义 $53.0k* ｜ +0.4%
P 57 ｜ +219 ｜ $0.82 ｜ 名义 $18.0k* ｜ -3.0%
C 60 ｜ +97 ｜ $0.99 ｜ 名义 $9.6k* ｜ +2.1%
结构参考：59（+0.4%） / 57（-3.0%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 59（结算参考） ｜ Put Wall 59（+0.4%，弱）（OI 0.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 39.5%｜历史 Rank 85%（近端代理）｜净 delta 敞口 负 21,786 股（方向不可观测）——方向不可观测，观察点，非方向信号

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-11/SLV_morning.json