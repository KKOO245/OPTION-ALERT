# 期权晚报 2026-09-04（快照 17:18 ET）

📊 市场环境

SPY $770.19 ｜ QQQ $718.96
VIX 14.53 ↑1.5%（5D +0.7%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 41.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 56 ｜ 实际 162 ｜ 前值 21　✅ 今日已公布
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 4.1 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览
🔵 **Flip 状态**: CONDITIONAL（Candidates: 16.8）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 17.75 → 收盘 17.72（-0.2%） ｜ 今日高 18.01 ｜ 低 17.20 ｜ 昨收 17.65 → 收盘 17.72（+0.4%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-09-11，窗口结束前不做对错判定）

Options: P/C成交量 0.34 | OI比 0.59 | ATM IV 145.9% | Skew -26.2pp | Term 0.50 | ExpMove ±7.6%（近端） | Rank 83%
量化视角： IV 历史高位（Rank 83%，期权偏贵）｜期限结构倒挂（Term 0.50，近月 IV 高于远月）｜Put 保护异常便宜（Skew -26.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.59）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.34×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.59×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（7D）±7.6% ｜ 09-18（14D）±12.7% ｜ 09-25（21D）±13.1% ｜ 10-02（28D）±16.4%
   ⇒ IV–VIX Spread: +131.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 911,039 | GEX Change vs 上次快照 565,620 | Flip: Candidates 16.80 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 78%（带内） ｜ IV 有效性: VALID 155 / LOW 88 / INVALID 223
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: ≈17（全链重定价，覆盖 78%，CONDITIONAL）
Put Wall 16（弱结构｜现价高于该位 10.7%）
最近结构参考: Flip 17（现价高于该位 5.5%）
量化视角： 正 Gamma（91万，无历史分位）｜正 Gamma 增强（+57万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 16（Put Wall，弱结构） / 18（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 17（全链重定价，覆盖 78%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 18.5C — Vol 15 | 最新价 $0.05 | OI 164→287 (ΔOI +123张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增123张（+75.0% vs前日OI），值得跟踪（方向未知）
10-02 18.5P — Vol 85（Yahoo补） | 最新价 $1.95 | OI 15→100 (ΔOI +85张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增85张（+566.7% vs前日OI），连续性待观察（方向未知）
09-18 20.0C — Vol 1 | 最新价 $0.25 | OI 556→617 (ΔOI +61张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增61张（+11.0% vs前日OI），值得跟踪（方向未知）
09-11 16.0P — Vol 272 | 最新价 $0.15 | OI 401→460 (ΔOI +59张) | ΔOI/Volume 21.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增59张（+14.7% vs前日OI），连续性待观察（方向未知）
10-02 19.0P — Vol 57（Yahoo补） | 最新价 $2.20 | OI 8→65 (ΔOI +57张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增57张（+712.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 385 张（Put 201 / Call 184），跨 4 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +0 / P +0 ｜ Activity LOW ｜ 7D
09-18  C +0 / P +0 ｜ Activity LOW ｜ 14D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 21D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 28D

📆 09-11 Forward Structure
存量OI:      C 2.7k / P 2.2k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 0.75 / P 0.60
隐含波动率 ATM IV:  60.8%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 20（结算参考） ｜ Put Wall 16（-9.7%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 60.8%｜历史 Rank 83%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（Activity LOW）仓位参考: Max Pain 19（结算参考） ｜ Put Wall 18（+1.6%）（OI 0.7k）

09-25（Activity LOW）仓位参考: Max Pain 19（结算参考）

10-02（Activity LOW）仓位参考: Max Pain 19（结算参考） ｜ Put Wall 17（-4.1%，弱）（OI 0.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-04/NNE_evening.json