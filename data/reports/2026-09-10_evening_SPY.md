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
🟡 **近现价集中开仓**: 09-11 770C ΔOI +15,584（距现价 +1.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-15 760P ΔOI +20,623 占该期限总 OI 25.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 758.03 → 收盘 757.83（-0.0%） ｜ 今日高 760.09 ｜ 低 756.64 ｜ 昨收 762.40 → 收盘 757.83（-0.6%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-09-15，窗口结束前不做对错判定）

Options: P/C成交量 1.15 | OI比 1.76 | ATM IV 19.1% | Skew 2.1pp | Term 0.75 | ExpMove ±0.8%（近端） | Rank 82%
量化视角： IV 历史高位（Rank 82%，期权偏贵）｜期限结构倒挂（Term 0.75，近月 IV 高于远月）｜保护溢价中性（Skew 2.1pp）｜当日成交偏 Put（P/C量 1.15）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.15×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.76×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 20% ｜ P/C OI(近端) 44%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 20%）｜近端持仓结构中性（P/C OI 分位 44%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-11（1D）±0.8% ｜ 09-14（4D）±1.1% ｜ 09-15（5D）±1.3% ｜ 09-16（6D）±1.5%
   ⇒ IV–VIX Spread: +1.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,724,542,501 | GEX Change vs 上次快照 -78,913,288 | Flip: Primary Flip: 770.29（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 2393 / LOW 325 / INVALID 2980
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 770.29（全链重定价，覆盖 96%）
Call Wall 800（弱结构｜现价低于该位 5.3%）
最近结构参考: Flip 770（现价低于该位 1.6%）
量化视角： 负 Gamma（17.25亿，历史分位偏负区，比 80% 的交易日更负）｜负 Gamma 加深（7891万）｜现价位于 Flip 下方 1.62%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 763（MaxPain，仅结算参考） / 800（Call Wall，弱结构）。
• Gamma 区域：切换参考 770（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-10 737.0P — Vol 1,125 | 最新价 $0.01 | OI 440→21393 (ΔOI +20953张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20953张（+4762.1% vs前日OI），连续性待观察（方向未知）
09-10 735.0P — Vol 3,237 | 最新价 $0.01 | OI 146→20770 (ΔOI +20624张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20624张（+14126.0% vs前日OI），连续性待观察（方向未知）
09-15 760.0P — Vol 7,057 | 最新价 $5.15 | OI 3965→24588 (ΔOI +20623张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20623张（+520.1% vs前日OI），连续性待观察（方向未知）
09-18 823.0C — Vol 1,000 | 最新价 $0.03 | OI 1354→19933 (ΔOI +18579张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18579张（+1372.2% vs前日OI），连续性待观察（方向未知）
09-11 770.0C — Vol 26,702 | 最新价 $0.13 | OI 8421→24005 (ΔOI +15584张) | ΔOI/Volume 58.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15584张（+185.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 96,363 张（Put 62,200 / Call 34,163），跨 4 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $11M，买/卖方向不可观测）｜彩票/名义 2 档（价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +35.8k / P +7.5k ｜ Activity HIGH ｜ 1D
09-14  C +9.6k / P +11.9k ｜ Activity HIGH ｜ 4D
09-15  C +4.6k / P +18.3k ｜ Activity HIGH ｜ 5D
09-16  C +5.0k / P +8.2k ｜ Activity HIGH ｜ 6D

📆 09-11 Forward Structure
存量OI:      C 276.2k / P 424.7k
今日变化ΔOI: C +35.8k / P +7.5k
平值价格ATM:  C 3.57 / P 2.70
隐含波动率 ATM IV:  19.5%
净 delta 敞口变化 ΔOI Δ Exposure*: 1.4M shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 770 ｜ +15,584 ｜ $0.13 ｜ 名义 $202.6k* ｜ +1.6%
P 760 ｜ -6,650 ｜ $3.60 ｜ 名义 $-2.39M* ｜ +0.3%
C 763 ｜ +4,513 ｜ $1.23 ｜ 名义 $555.1k* ｜ +0.7%
结构参考：770（+1.6%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 765（结算参考） ｜ Call Wall 770（+1.6%，弱）（OI 24.0k） ｜ Put Wall 760（+0.3%，弱）（OI 45.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 19.5%｜历史 Rank 82%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,444,351 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-14 Forward Structure
存量OI:      C 43.6k / P 50.6k
今日变化ΔOI: C +9.6k / P +11.9k
平值价格ATM:  C 4.56 / P 3.66
隐含波动率 ATM IV:  12.9%
净 delta 敞口变化 ΔOI Δ Exposure*: 121k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 700 ｜ +7,745 ｜ $0.09 ｜ 名义 $69.7k* ｜ -7.6%
C 765 ｜ +2,739 ｜ $1.36 ｜ 名义 $372.5k* ｜ +0.9%
C 785 ｜ +2,416 ｜ $0.02 ｜ 名义 $4.8k* ｜ +3.6%
结构参考：765（+0.9%） / 700（-7.6%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 765（结算参考） ｜ Call Wall 785（+3.6%，弱）（OI 7.3k） ｜ Put Wall 700（-7.6%）（OI 24.1k）
量化解读： 存量两侧均衡｜ATM IV 12.9%｜历史 Rank 82%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 120,974 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-15 Forward Structure
存量OI:      C 17.2k / P 62.7k
今日变化ΔOI: C +4.6k / P +18.3k
平值价格ATM:  C 5.28 / P 4.33
隐含波动率 ATM IV:  13.4%
净 delta 敞口变化 ΔOI Δ Exposure*: -580k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 760 ｜ +20,623 ｜ $5.15 ｜ 名义 $10.62M* ｜ +0.3%
P 755 ｜ -12,121 ｜ $3.25 ｜ 名义 $-3.94M* ｜ -0.4%
P 700 ｜ +4,028 ｜ $0.14 ｜ 名义 $56.4k* ｜ -7.6%
结构参考：760（+0.3%） / 700（-7.6%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 765（结算参考） ｜ Call Wall 770（+1.6%，弱）（OI 3.7k） ｜ Put Wall 760（+0.3%）（OI 24.6k）
量化解读： 存量 Put 重｜ATM IV 13.4%｜历史 Rank 82%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 负 579,658 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-16 Forward Structure
存量OI:      C 13.5k / P 18.2k
今日变化ΔOI: C +5.0k / P +8.2k
平值价格ATM:  C 6.03 / P 5.32
隐含波动率 ATM IV:  14.9%
净 delta 敞口变化 ΔOI Δ Exposure*: -19k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 700 ｜ +1,940 ｜ $0.22 ｜ 名义 $42.7k* ｜ -7.6%
P 735 ｜ +1,883 ｜ $1.02 ｜ 名义 $192.1k* ｜ -3.0%
C 765 ｜ +1,156 ｜ $2.81 ｜ 名义 $324.8k* ｜ +0.9%
结构参考：765（+0.9%） / 700（-7.6%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 765（结算参考） ｜ Call Wall 770（+1.6%，弱）（OI 2.7k） ｜ Put Wall 735（-3.0%，弱）（OI 2.5k）
量化解读： 存量 Put 重｜ATM IV 14.9%｜历史 Rank 82%（近端代理）｜净 delta 敞口 负 19,353 股（方向不可观测）——方向不可观测，观察点，非方向信号

📅 事件差分（观察，非因果）: 09-11（1D）ATM IV 19.5% vs 09-14 12.9%（差 +6.7pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=14 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=14）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-10/SPY_evening.json