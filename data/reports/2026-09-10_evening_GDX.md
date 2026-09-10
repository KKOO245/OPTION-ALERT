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
🔴 **事件差分**: 09-11（1D）ATM IV 64.9% vs 09-18 49.6%（差 +15.3pp），覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **单日价格波动**: -3.5%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-11 96P ΔOI +7,037（距现价 -0.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 96.53 → 收盘 96.03（-0.5%） ｜ 今日高 97.44 ｜ 低 95.62 ｜ 昨收 99.47 → 收盘 96.03（-3.5%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-09-15，窗口结束前不做对错判定）

Options: P/C成交量 0.45 | OI比 0.65 | ATM IV 64.9% | Skew 1.6pp | Term 0.71 | ExpMove ±2.9%（近端） | Rank 96%
量化视角： IV 历史高位（Rank 96%，期权偏贵）｜期限结构倒挂（Term 0.71，近月 IV 高于远月）｜保护溢价薄（Skew 1.6pp）｜存量 Call 偏重（OI比 0.65）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.45×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.65×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（1D）±2.9% ｜ 09-18（8D）±6.0% ｜ 09-25（15D）±7.8% ｜ 10-02（22D）±9.0%
   ⇒ IV–VIX Spread: +47.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -27,600,159 | GEX Change vs 上次快照 -12,017,503 | Flip: Primary Flip: 97.18（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 582 / LOW 170 / INVALID 198
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 97.18（全链重定价，覆盖 96%）
Call Wall 100（弱结构｜现价低于该位 4.0%）
最近结构参考: Flip 97（现价低于该位 1.2%）
量化视角： 负 Gamma（2760万，无历史分位）｜负 Gamma 加深（1202万）｜现价位于 Flip 下方 1.18%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 98（MaxPain，仅结算参考） / 100（Call Wall，弱结构）。
• Gamma 区域：切换参考 97（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 96.0P — Vol 8,991 | 最新价 $1.37 | OI 843→7880 (ΔOI +7037张) | ΔOI/Volume 78.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7037张（+834.8% vs前日OI），连续性待观察（方向未知）
09-11 103.0C — Vol 432 | 最新价 $0.05 | OI 6081→10310 (ΔOI +4229张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4229张（+69.5% vs前日OI），连续性待观察（方向未知）
09-11 97.0P — Vol 614 | 最新价 $1.86 | OI 565→4517 (ΔOI +3952张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3952张（+699.5% vs前日OI），连续性待观察（方向未知）
09-18 108.0C — Vol 37 | 最新价 $0.25 | OI 5663→9444 (ΔOI +3781张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3781张（+66.8% vs前日OI），连续性待观察（方向未知）
09-18 105.0C — Vol 308 | 最新价 $0.46 | OI 7871→10882 (ΔOI +3011张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3011张（+38.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 22,010 张（Put 10,989 / Call 11,021），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $2M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +8.3k / P +16.5k ｜ Activity HIGH ｜ 1D
09-18  C +7.3k / P -2.0k ｜ Activity HIGH ｜ 8D
09-25  C +74 / P -11 ｜ Activity MEDIUM △ ｜ 15D
10-02  C +0.3k / P +0.2k ｜ Activity MEDIUM △ ｜ 22D

📆 09-11 Forward Structure
存量OI:      C 113.7k / P 74.0k
今日变化ΔOI: C +8.3k / P +16.5k
平值价格ATM:  C 1.41 / P 1.37
隐含波动率 ATM IV:  64.9%
净 delta 敞口变化 ΔOI Δ Exposure*: -714k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 96 ｜ +7,037 ｜ $1.37 ｜ 名义 $964.1k* ｜ -0.0%
C 103 ｜ +4,229 ｜ $0.05 ｜ 名义 $21.1k* ｜ +7.3%
P 97 ｜ +3,952 ｜ $1.86 ｜ 名义 $735.1k* ｜ +1.0%
结构参考：103（+7.3%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 98（结算参考） ｜ Call Wall 104（+8.3%，弱）（OI 18.2k） ｜ Put Wall 90（-6.3%，弱）（OI 11.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 64.9%｜历史 Rank 96%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 713,819 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 255.1k / P 416.7k
今日变化ΔOI: C +7.3k / P -2.0k
平值价格ATM:  C 2.91 / P 2.84
隐含波动率 ATM IV:  49.6%
净 delta 敞口变化 ΔOI Δ Exposure*: 107k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 108 ｜ +3,781 ｜ $0.25 ｜ 名义 $94.5k* ｜ +12.5%
C 105 ｜ +3,011 ｜ $0.46 ｜ 名义 $138.5k* ｜ +9.3%
P 95 ｜ -1,370 ｜ $2.32 ｜ 名义 $-317.8k* ｜ -1.1%
结构参考：108（+12.5%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 90（结算参考） ｜ Call Wall 100（+4.1%，弱）（OI 23.7k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 49.6%｜历史 Rank 96%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 107,057 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-25（MEDIUM △）Top ΔOI: 89P +39 ｜ 99P -33
09-25（MEDIUM △）仓位参考: Max Pain 96（结算参考） ｜ Call Wall 105（+9.3%）（OI 1.0k）

10-02（MEDIUM △）Top ΔOI: 90P +149 ｜ 100C -41
10-02（MEDIUM △）仓位参考: Max Pain 99（结算参考） ｜ Put Wall 97（+1.0%）（OI 15.1k）

📅 事件差分（观察，非因果）: 09-11（1D）ATM IV 64.9% vs 09-18 49.6%（差 +15.3pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=14 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=14）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-10/GDX_evening.json