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
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **单日价格波动**: -2.3%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-11 167P ΔOI +2,114（距现价 +1.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 167.36 → 收盘 165.86（-0.9%） ｜ 今日高 169.00 ｜ 低 164.55 ｜ 昨收 169.53 → 收盘 165.86（-2.2%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-09-15，窗口结束前不做对错判定）

Options: P/C成交量 0.76 | OI比 0.74 | ATM IV 53.8% | Skew 1.2pp | Term 0.88 | ExpMove ±2.3%（近端） | Rank — (历史不足)
量化视角： 期限结构倒挂（Term 0.88，近月 IV 高于远月）｜保护溢价薄（Skew 1.2pp）｜存量 Call 偏重（OI比 0.74）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.76×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.74×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（1D）±2.3% ｜ 09-18（8D）±5.8% ｜ 09-25（15D）±7.6% ｜ 10-02（22D）±9.3%
   ⇒ IV–VIX Spread: +36.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -3,630,105 | GEX Change vs 上次快照 -14,917,252 | Flip: Primary Flip: 166.24（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 581 / LOW 121 / INVALID 176
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 166.24（全链重定价，覆盖 99%）
Put Wall 170（弱结构｜现价低于该位 2.4%） | Call Wall 180（弱结构｜现价低于该位 7.9%）
最近结构参考: Flip 166（现价低于该位 0.2%）
量化视角： 负 Gamma（363万，无历史分位）｜由正转负（1492万）｜现价位于 Flip 下方 0.23%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 170（Put Wall，弱结构） / 170（MaxPain，仅结算参考） / 180（Call Wall，弱结构）。
• Gamma 区域：切换参考 166（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 180.0C — Vol 6,095 | 最新价 $0.04 | OI 15238→18621 (ΔOI +3383张) | ΔOI/Volume 55.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3383张（+22.2% vs前日OI），连续性待观察（方向未知）
09-11 175.0C — Vol 15,885 | 最新价 $0.12 | OI 12306→14893 (ΔOI +2587张) | ΔOI/Volume 16.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2587张（+21.0% vs前日OI），连续性待观察（方向未知）
09-18 177.5C — Vol 11,627 | 最新价 $1.14 | OI 890→3306 (ΔOI +2416张) | ΔOI/Volume 20.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2416张（+271.5% vs前日OI），连续性待观察（方向未知）
09-18 180.0C — Vol 6,429 | 最新价 $0.83 | OI 13666→16041 (ΔOI +2375张) | ΔOI/Volume 36.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2375张（+17.4% vs前日OI），连续性待观察（方向未知）
09-11 167.5P — Vol 6,454 | 最新价 $2.79 | OI 3640→5754 (ΔOI +2114张) | ΔOI/Volume 32.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2114张（+58.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 12,875 张（Put 2,114 / Call 10,761），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +3.9k / P +4.5k ｜ Activity MEDIUM △ ｜ 1D
09-18  C +4.6k / P +1.7k ｜ Activity MEDIUM △ ｜ 8D
09-25  C +1.6k / P +2.2k ｜ Activity HIGH ｜ 15D
10-02  C +0.4k / P +0.4k ｜ Activity MEDIUM △ ｜ 22D

📆 09-11 Forward Structure
存量OI:      C 151.5k / P 111.4k
今日变化ΔOI: C +3.9k / P +4.5k
平值价格ATM:  C 2.36 / P 1.45
隐含波动率 ATM IV:  53.8%
净 delta 敞口变化 ΔOI Δ Exposure*: -123k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 180 ｜ +3,383 ｜ $0.04 ｜ 名义 $13.5k* ｜ +8.5%
C 175 ｜ +2,587 ｜ $0.12 ｜ 名义 $31.0k* ｜ +5.5%
P 167 ｜ +2,114 ｜ $2.79 ｜ 名义 $589.8k* ｜ +1.0%
结构参考：180（+8.5%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 170（结算参考） ｜ Call Wall 180（+8.5%，弱）（OI 18.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 53.8%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 123,237 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（MEDIUM △）Top ΔOI: 135C -5,651 ｜ 177C +2,416
09-18（MEDIUM △）仓位参考: Max Pain 150（结算参考）

📆 09-25 Forward Structure
存量OI:      C 22.6k / P 33.3k
今日变化ΔOI: C +1.6k / P +2.2k
平值价格ATM:  C 6.89 / P 5.70
隐含波动率 ATM IV:  47.0%
净 delta 敞口变化 ΔOI Δ Exposure*: -18k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 155 ｜ +1,447 ｜ $2.23 ｜ 名义 $322.7k* ｜ -6.5%
P 152 ｜ +594 ｜ $1.71 ｜ 名义 $101.6k* ｜ -8.1%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：155（-6.5%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 175（结算参考） ｜ Put Wall 170（+2.5%）（OI 7.3k）
量化解读： 存量 Put 重｜ATM IV 47.0%｜净 delta 敞口 负 18,010 股（方向不可观测）——方向不可观测，观察点，非方向信号

10-02（MEDIUM △）Top ΔOI: 155P +180 ｜ 150C +102
10-02（MEDIUM △）仓位参考: Max Pain 175（结算参考） ｜ Call Wall 180（+8.5%，弱）（OI 2.5k） ｜ Put Wall 160（-3.5%，弱）（OI 2.7k）

📅 事件差分（观察，非因果）: 09-11（1D）ATM IV 53.8% vs 09-18 47.9%（差 +5.9pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=14 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=14）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-10/PLTR_evening.json