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
🟡 **单日价格波动**: -3.5%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向


## SPCX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPCX: 今开 151.98 → 收盘 147.55（-2.9%） ｜ 今日高 153.00 ｜ 低 145.55 ｜ 昨收 153.47 → 收盘 147.55（-3.9%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-09-14，窗口结束前不做对错判定）

Options: P/C成交量 0.83 | OI比 1.69 | ATM IV 59.3% | Skew 0.5pp | Term 0.88 | ExpMove ±3.5%（近端） | Rank 48%
量化视角： IV 中性（Rank 48%）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜保护溢价薄（Skew 0.5pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.83×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.69×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-11（2D）±3.5% ｜ 09-18（9D）±6.9% ｜ 09-25（16D）±8.8% ｜ 10-02（23D）±10.4%
   ⇒ IV–VIX Spread: +42.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -14,639,448 | GEX Change vs 上次快照 -32,269,389 | Flip: Primary Flip: 148.68（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 651 / LOW 147 / INVALID 296
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 148.68（全链重定价，覆盖 100%）
Call Wall 160（弱结构｜现价低于该位 7.8%）
最近结构参考: Flip 149（现价低于该位 0.8%）
量化视角： 负 Gamma（1464万，无历史分位）｜由正转负（3227万）｜现价位于 Flip 下方 0.76%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 149（MaxPain，仅结算参考） / 160（Call Wall，弱结构）。
• Gamma 区域：切换参考 149（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 152.5P — Vol 17,325 | 最新价 $5.52 | OI 902→15903 (ΔOI +15001张) | ΔOI/Volume 86.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15001张（+1663.1% vs前日OI），连续性待观察（方向未知）
09-11 160.0C — Vol 22,232 | 最新价 $0.15 | OI 11130→24399 (ΔOI +13269张) | ΔOI/Volume 59.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13269张（+119.2% vs前日OI），连续性待观察（方向未知）
09-11 139.0P — Vol 3,139 | 最新价 $0.33 | OI 2862→11774 (ΔOI +8912张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8912张（+311.4% vs前日OI），连续性待观察（方向未知）
09-11 145.0P — Vol 30,276 | 最新价 $1.50 | OI 9781→18082 (ΔOI +8301张) | ΔOI/Volume 27.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8301张（+84.9% vs前日OI），连续性待观察（方向未知）
09-11 162.5C — Vol 3,280 | 最新价 $0.09 | OI 2184→10000 (ΔOI +7816张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7816张（+357.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 53,299 张（Put 32,214 / Call 21,085），跨 1 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $10M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-18  C +0 / P +0 ｜ Activity LOW ｜ 9D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 16D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 23D

📆 09-11 Forward Structure
存量OI:      C 146.5k / P 247.0k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 2.39 / P 2.81
隐含波动率 ATM IV:  59.3%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 149（结算参考） ｜ Call Wall 160（+8.4%）（OI 24.4k） ｜ Put Wall 140（-5.1%）（OI 31.0k）
量化解读： 存量 Put 重｜ATM IV 59.3%｜历史 Rank 48%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（Activity LOW）仓位参考: Max Pain 145（结算参考） ｜ Call Wall 150（+1.7%，弱）（OI 44.3k） ｜ Put Wall 150（+1.7%，弱）（OI 45.8k）

09-25（Activity LOW）仓位参考: Max Pain 143（结算参考）

10-02（Activity LOW）仓位参考: Max Pain 144（结算参考） ｜ Call Wall 150（+1.7%，弱）（OI 2.6k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=14 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=14）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-09/SPCX_evening.json