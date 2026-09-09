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

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **单日价格波动**: -2.5%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 55.11 → 收盘 54.30（-1.5%） ｜ 今日高 56.33 ｜ 低 54.21 ｜ 昨收 55.37 → 收盘 54.30（-1.9%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-09-14，窗口结束前不做对错判定）

Options: P/C成交量 1.05 | OI比 0.74 | ATM IV 77.3% | Skew -4.0pp | Term 0.94 | ExpMove ±4.0%（近端） | Rank 66%
量化视角： IV 中性（Rank 66%）｜期限结构正常（Term 0.94）｜Put 保护异常便宜（Skew -4.0pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.74）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.05×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.74×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（2D）±4.0% ｜ 09-18（9D）±8.6% ｜ 09-25（16D）±10.8% ｜ 10-02（23D）±14.8%
   ⇒ IV–VIX Spread: +60.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -29,050 | GEX Change vs 上次快照 -2,110,287 | Flip: Primary Flip: 54.32（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 270 / LOW 61 / INVALID 79
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 54.32（全链重定价，覆盖 99%）
最近结构参考: Flip 54（现价低于该位 0.0%）
量化视角： 负 Gamma（3万，无历史分位）｜由正转负（211万）｜现价位于 Flip 下方 0.03%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 55（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 54（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 54.0P — Vol 457 | 最新价 $0.80 | OI 315→957 (ΔOI +642张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增642张（+203.8% vs前日OI），连续性待观察（方向未知）
09-11 60.0C — Vol 461 | 最新价 $0.15 | OI 1021→1597 (ΔOI +576张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增576张（+56.4% vs前日OI），连续性待观察（方向未知）
09-18 55.0C — Vol 300 | 最新价 $2.00 | OI 3487→3945 (ΔOI +458张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增458张（+13.1% vs前日OI），值得跟踪（方向未知）
09-11 58.0C — Vol 82 | 最新价 $0.25 | OI 384→742 (ΔOI +358张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增358张（+93.2% vs前日OI），值得跟踪（方向未知）
09-18 60.0C — Vol 420 | 最新价 $0.73 | OI 6347→6703 (ΔOI +356张) | ΔOI/Volume 84.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增356张（+5.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,390 张（Put 642 / Call 1,748），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-18  C +0 / P +0 ｜ Activity LOW ｜ 9D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 16D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 23D

📆 09-11 Forward Structure
存量OI:      C 9.6k / P 7.1k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 1.37 / P 0.80
隐含波动率 ATM IV:  77.3%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 55（结算参考）
量化解读： 存量 Call 重｜ATM IV 77.3%｜历史 Rank 66%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（Activity LOW）仓位参考: Max Pain 55（结算参考） ｜ Put Wall 55（+1.3%，弱）（OI 9.1k）

09-25（Activity LOW）仓位参考: Max Pain 52（结算参考）

10-02（Activity LOW）仓位参考: Max Pain 59（结算参考） ｜ Put Wall 50（-7.9%）（OI 1.2k）

📅 事件差分（观察，非因果）: 09-11（2D）ATM IV 77.3% vs 09-18 70.4%（差 +6.9pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=14 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=14）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-09/MP_evening.json