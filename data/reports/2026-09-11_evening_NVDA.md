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
🟡 **近现价集中开仓**: 09-14 225C ΔOI +5,527（距现价 +3.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-21 65P ΔOI +10,705 占该期限总 OI 36.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 221.25 → 收盘 218.29（-1.3%） ｜ 今日高 222.00 ｜ 低 218.15 ｜ 昨收 218.36 → 收盘 218.29（-0.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.51 | OI比 0.70 | ATM IV 33.3% | Skew -13.0pp | Term 0.93 | ExpMove ±1.5%（近端） | Rank 13%
量化视角： IV 历史低位（Rank 13%，期权偏便宜）｜期限结构正常（Term 0.93）｜Put 保护异常便宜（Skew -13.0pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.70）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.51×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.70×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-14（3D）±1.5% ｜ 09-16（5D）±2.7% ｜ 09-18（7D）±3.4% ｜ 09-21（10D）±3.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 254,557,438 | GEX Change vs 上次快照 -222,663,064 | Flip: Primary Flip: 209.64（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 88%（带内） ｜ IV 有效性: VALID 622 / LOW 215 / INVALID 651
结构观察区: Primary Flip 209.64（全链重定价，覆盖 88%）
Put Wall 200（弱结构｜现价高于该位 9.1%）
最近结构参考: Flip 210（现价高于该位 4.1%）
量化视角： 正 Gamma（2.55亿，无历史分位）｜正 Gamma 减弱（2.23亿）｜现价位于 Flip 上方 4.13%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall，弱结构）；上方 220（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 210（全链重定价，覆盖 88%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 222.5C — Vol 16,223 | 最新价 $1.91 | OI 6334→46519 (ΔOI +40185张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增40185张（+634.4% vs前日OI），连续性待观察（方向未知）
09-18 230.0C — Vol 38,585 | 最新价 $0.46 | OI 59663→93452 (ΔOI +33789张) | ΔOI/Volume 87.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增33789张（+56.6% vs前日OI），连续性待观察（方向未知）
09-11 220.0C — Vol 439,564 | 最新价 $0.01 | OI 10557→41789 (ΔOI +31232张) | ΔOI/Volume 7.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增31232张（+295.8% vs前日OI），连续性待观察（方向未知）
09-11 225.0C — Vol 124,295 | 最新价 $0.01 | OI 26127→40635 (ΔOI +14508张) | ΔOI/Volume 11.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14508张（+55.5% vs前日OI），连续性待观察（方向未知）
09-11 222.5C — Vol 326,270 | 最新价 $0.01 | OI 3995→17935 (ΔOI +13940张) | ΔOI/Volume 4.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13940张（+348.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 133,654 张（Put 0 / Call 133,654），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-14  C +21.5k / P +21.0k ｜ Activity HIGH ｜ 3D
09-16  C +8.0k / P +9.2k ｜ Activity HIGH ｜ 5D
09-18  C +79.6k / P +9.4k ｜ Activity HIGH ｜ 7D
09-21  C +11.2k / P +13.4k ｜ Activity HIGH ｜ 10D

📆 09-14 Forward Structure
存量OI:      C 70.1k / P 44.9k
今日变化ΔOI: C +21.5k / P +21.0k
平值价格ATM:  C 2.05 / P 1.31
隐含波动率 ATM IV:  20.8%
净 delta 敞口变化 ΔOI Δ Exposure*: 229k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 225 ｜ +5,527 ｜ $0.12 ｜ 名义 $66.3k* ｜ +3.1%
C 227 ｜ +5,244 ｜ $0.06 ｜ 名义 $31.5k* ｜ +4.2%
C 220 ｜ +4,642 ｜ $0.86 ｜ 名义 $399.2k* ｜ +0.8%
结构参考：225（+3.1%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 220（结算参考） ｜ Call Wall 230（+5.4%，弱）（OI 14.7k）
量化解读： 存量 Call 重｜ATM IV 20.8%｜历史 Rank 13%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 229,282 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-16 Forward Structure
存量OI:      C 41.4k / P 21.0k
今日变化ΔOI: C +8.0k / P +9.2k
平值价格ATM:  C 3.35 / P 2.55
隐含波动率 ATM IV:  28.5%
净 delta 敞口变化 ΔOI Δ Exposure*: 75k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 202 ｜ +2,074 ｜ $0.19 ｜ 名义 $39.4k* ｜ -7.2%
C 220 ｜ +1,699 ｜ $2.08 ｜ 名义 $353.4k* ｜ +0.8%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：220（+0.8%） / 202（-7.2%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 220（结算参考） ｜ Call Wall 235（+7.7%）（OI 14.5k） ｜ Put Wall 215（-1.5%，弱）（OI 3.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 28.5%｜历史 Rank 13%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 74,924 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 1207.2k / P 1027.7k
今日变化ΔOI: C +79.6k / P +9.4k
平值价格ATM:  C 4.13 / P 3.20
隐含波动率 ATM IV:  30.1%
净 delta 敞口变化 ΔOI Δ Exposure*: 2.2M shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 222 ｜ +40,185 ｜ $1.91 ｜ 名义 $7.68M* ｜ +1.9%
C 230 ｜ +33,789 ｜ $0.46 ｜ 名义 $1.55M* ｜ +5.4%
P 250 ｜ -3,255 ｜ $31.35 ｜ 名义 $-10.20M* ｜ +14.5%
结构参考：222（+1.9%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 202（结算参考） ｜ Call Wall 230（+5.4%，弱）（OI 93.5k）
量化解读： 存量两侧均衡｜ATM IV 30.1%｜历史 Rank 13%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,244,741 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-21 Forward Structure
存量OI:      C 13.8k / P 15.9k
今日变化ΔOI: C +11.2k / P +13.4k
平值价格ATM:  C 4.72 / P 3.45
隐含波动率 ATM IV:  28.1%
净 delta 敞口变化 ΔOI Δ Exposure*: 123k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 240 ｜ +4,256 ｜ $0.12 ｜ 名义 $51.1k* ｜ +9.9%
C 230 ｜ +2,200 ｜ $0.65 ｜ 名义 $143.0k* ｜ +5.4%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：240（+9.9%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 218（结算参考） ｜ Call Wall 240（+9.9%）（OI 4.8k）
量化解读： 存量两侧均衡｜ATM IV 28.1%｜历史 Rank 13%（近端代理）｜净 delta 敞口 正 123,088 股（方向不可观测）——方向不可观测，观察点，非方向信号

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-11/NVDA_evening.json