# 期权晨报 2026-09-11（快照 10:20 ET）

📊 市场环境

SPY $766.00 ｜ QQQ $716.42
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
🟡 **近现价集中开仓**: 09-18 517P ΔOI +341（距现价 -1.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 517.43 → 今开 525.23（+1.5%） | 较昨收变动（含盘初走势） ｜ 今日高 529.14 ｜ 低 521.14

Options: P/C成交量 1.39 | OI比 1.56 | ATM IV 42.5% | Skew 9.9pp | Term 0.90 | ExpMove ±4.6%（近端） | Rank 76%
量化视角： IV 历史高位（Rank 76%，期权偏贵）｜期限结构倒挂（Term 0.90，近月 IV 高于远月）｜保护溢价显著（Skew 9.9pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 1.39）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.39×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.56×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-18（7D）±4.6% ｜ 09-25（14D）±6.7% ｜ 10-02（21D）±6.9% ｜ 10-09（28D）±9.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 5,630,976 | GEX Change vs 上次快照 19,539,972 | Flip: Primary Flip: 524.27（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 582 / LOW 379 / INVALID 699
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 524.27（全链重定价，覆盖 98%）
Call Wall 575（弱结构｜现价低于该位 8.4%）
最近结构参考: Flip 524（现价高于该位 0.5%）
量化视角： 正 Gamma（563万，无历史分位）｜由负转正（+1954万）｜现价位于 Flip 上方 0.46%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 518（MaxPain，仅结算参考）；上方 575（Call Wall，弱结构）。
• Gamma 区域：切换参考 524（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 510.0P — Vol 2,424 | 最新价 $3.00 | OI 1316→3569 (ΔOI +2253张) | ΔOI/Volume 93.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2253张（+171.2% vs前日OI），连续性待观察（方向未知）
09-11 525.0C — Vol 2,289 | 最新价 $2.25 | OI 56→2180 (ΔOI +2124张) | ΔOI/Volume 92.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2124张（+3792.9% vs前日OI），连续性待观察（方向未知）
10-16 470.0P — Vol 2,285 | 最新价 $8.04 | OI 531→2648 (ΔOI +2117张) | ΔOI/Volume 92.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2117张（+398.7% vs前日OI），连续性待观察（方向未知）
10-16 485.0P — Vol 1,415 | 最新价 $11.97 | OI 2872→4277 (ΔOI +1405张) | ΔOI/Volume 99.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1405张（+48.9% vs前日OI），连续性待观察（方向未知）
09-11 507.5P — Vol 1,337 | 最新价 $2.14 | OI 253→1253 (ΔOI +1000张) | ΔOI/Volume 74.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1000张（+395.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 8,899 张（Put 6,775 / Call 2,124），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $4M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C -0.1k / P +0.7k ｜ Activity MEDIUM △ ｜ 7D
09-25  C +23 / P +0.2k ｜ Activity MEDIUM △ ｜ 14D
10-02  C +31 / P +0.7k ｜ Activity HIGH ｜ 21D
10-09  C +0.3k / P +0.2k ｜ Activity HIGH ｜ 28D

📆 09-18 Forward Structure
存量OI:      C 99.3k / P 92.3k
今日变化ΔOI: C -0.1k / P +0.7k
平值价格ATM:  C 8.82 / P 15.58
隐含波动率 ATM IV:  38.3%
净 delta 敞口变化 ΔOI Δ Exposure*: -23k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 470 ｜ -439 ｜ $1.25 ｜ 名义 $-54.9k* ｜ -10.8%
P 517 ｜ +341 ｜ $10.50 ｜ 名义 $358.1k* ｜ -1.7%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：517（-1.7%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 530（结算参考） ｜ Call Wall 575（+9.2%，弱）（OI 15.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 38.3%｜历史 Rank 76%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 23,197 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-25（MEDIUM △）Top ΔOI: 495P +30
09-25（MEDIUM △）仓位参考: Max Pain 530（结算参考） ｜ Put Wall 480（-8.9%，弱）（OI 1.9k）

📆 10-02 Forward Structure
存量OI:      C 10.4k / P 9.4k
今日变化ΔOI: C +31 / P +0.7k
平值价格ATM:  C 16.35 / P 20.10
隐含波动率 ATM IV:  38.5%
净 delta 敞口变化 ΔOI Δ Exposure*: -1k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 420 ｜ +630 ｜ $1.00 ｜ 名义 $63.0k* ｜ -20.3%
C 570 ｜ +20 ｜ $4.60 ｜ 名义 $9.2k* ｜ +8.2%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：570（+8.2%） / 420（-20.3%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 525（结算参考） ｜ Call Wall 542.5（+3.0%，弱）（OI 2.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 38.5%｜历史 Rank 76%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,352 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 10-09 Forward Structure
存量OI:      C 3.0k / P 1.4k
今日变化ΔOI: C +0.3k / P +0.2k
平值价格ATM:  C 27.99 / P 23.13
隐含波动率 ATM IV:  38.1%
净 delta 敞口变化 ΔOI Δ Exposure*: 10k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 520 ｜ +128 ｜ $22.82 ｜ 名义 $292.1k* ｜ -1.3%
C 525 ｜ +101 ｜ $20.37 ｜ 名义 $205.7k* ｜ -0.3%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：520（-1.3%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 510（结算参考） ｜ Call Wall 525（-0.3%）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 38.1%｜历史 Rank 76%（近端代理）｜净 delta 敞口 正 9,808 股（方向不可观测）——方向不可观测，观察点，非方向信号

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-11/SOXX_morning.json