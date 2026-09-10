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
🟡 **单日价格波动**: -5.5%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **事件差分**: 09-11 ATM IV 69.8% vs 09-18 59.2%（差 +10.6pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 09-18 52P ΔOI +66（距现价 +1.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 53.33 → 收盘 51.32（-3.8%） ｜ 今日高 53.73 ｜ 低 51.12 ｜ 昨收 54.30 → 收盘 51.32（-5.5%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-09-15，窗口结束前不做对错判定）

Options: P/C成交量 0.62 | OI比 0.82 | ATM IV 69.8% | Skew -12.2pp | Term 0.93 | ExpMove ±3.3%（近端） | Rank 53%
量化视角： IV 中性（Rank 53%）｜期限结构正常（Term 0.93）｜Put 保护异常便宜（Skew -12.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.82）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.62×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.82×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-11（1D）±3.3% ｜ 09-18（8D）±7.6% ｜ 09-25（15D）±10.6% ｜ 10-02（22D）±12.5%
   ⇒ IV–VIX Spread: +51.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -5,413,417 | GEX Change vs 上次快照 -1,292,009 | Flip: Primary Flip: 54.41（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 257 / LOW 59 / INVALID 116
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 54.41（全链重定价，覆盖 99%）
最近结构参考: Flip 54（现价低于该位 5.7%）
量化视角： 负 Gamma（541万，无历史分位）｜负 Gamma 加深（129万）｜现价位于 Flip 下方 5.67%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 55（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 54（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 53.0P — Vol 210 | 最新价 $2.07 | OI 697→974 (ΔOI +277张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增277张（+39.7% vs前日OI），值得跟踪（方向未知）
09-11 54.0P — Vol 251 | 最新价 $2.78 | OI 957→1182 (ΔOI +225张) | ΔOI/Volume 89.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增225张（+23.5% vs前日OI），连续性待观察（方向未知）
09-25 50.0P — Vol 18 | 最新价 $2.06 | OI 291→450 (ΔOI +159张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增159张（+54.6% vs前日OI），值得跟踪（方向未知）
10-09 50.0P — Vol 30 | 最新价 $3.00 | OI 37→195 (ΔOI +158张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增158张（+427.0% vs前日OI），值得跟踪（方向未知）
09-11 38.0P — Vol 116（Yahoo补） | 最新价 $0.02 | OI 9→125 (ΔOI +116张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增116张（+1288.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 935 张（Put 935 / Call 0），跨 3 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +0.2k / P +0.8k ｜ Activity HIGH ｜ 1D
09-18  C -0.7k / P +0.1k ｜ Activity MEDIUM △ ｜ 8D
09-25  C +0.1k / P +0.2k ｜ Activity MEDIUM △ ｜ 15D
10-02  C +34 / P +27 ｜ Activity LOW ｜ 22D

📆 09-11 Forward Structure
存量OI:      C 9.8k / P 8.0k
今日变化ΔOI: C +0.2k / P +0.8k
平值价格ATM:  C 1.00 / P 0.70
隐含波动率 ATM IV:  69.8%
净 delta 敞口变化 ΔOI Δ Exposure*: -44k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 53 ｜ +277 ｜ $2.07 ｜ 名义 $57.3k* ｜ +3.3%
P 54 ｜ +225 ｜ $2.78 ｜ 名义 $62.5k* ｜ +5.2%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：53（+3.3%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 55（结算参考）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 69.8%｜历史 Rank 53%（近端代理）｜净 delta 敞口 负 44,426 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（MEDIUM △）Top ΔOI: 56C -533 ｜ 52P +66
09-18（MEDIUM △）仓位参考: Max Pain 55（结算参考） ｜ Put Wall 55（+7.2%，弱）（OI 9.1k）

09-25（MEDIUM △）Top ΔOI: 50P +159 ｜ 53P +39
09-25（MEDIUM △）仓位参考: Max Pain 52（结算参考）

10-02（Activity LOW）仓位参考: Max Pain 59（结算参考） ｜ Put Wall 50（-2.6%）（OI 1.2k）

📅 事件差分（观察，非因果）: 09-11（1D）ATM IV 69.8% vs 09-18 59.2%（差 +10.6pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=14 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=14）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-10/MP_evening.json