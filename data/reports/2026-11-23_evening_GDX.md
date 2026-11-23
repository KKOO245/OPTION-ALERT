# 期权晚报 2026-11-23（快照 16:40 ET）

📊 市场环境

SPY $722.29 ｜ QQQ $651.03
VIX 26.62 ↓25.8%（5D +16.2%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 17.0（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-23

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-25 08:30　【高】Personal Spending MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.5
- 周三 11-25 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 11-25 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 11-25 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 3.4 ｜ 实际 待公布 ｜ 前值 1.5
- 周三 11-25 08:30　【高】耐用品订单 Orders MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.8

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-25 75C ΔOI +217（距现价 +3.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-27 71C ΔOI +15,034 占该期限总 OI 14.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 73.85 → 收盘 72.80（-1.4%） ｜ 今日高 74.47 ｜ 低 72.08 ｜ 昨收 68.40 → 收盘 72.80（+6.4%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-30，窗口结束前不做对错判定）

Options: P/C成交量 0.73 | OI比 0.54 | ATM IV 117.5% | Skew -26.2pp | Term 0.42 | ExpMove ±3.6%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.42，近月 IV 高于远月）｜Put 保护异常便宜（Skew -26.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.54）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.73×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.54×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-25（2D）±3.6% ｜ 11-27（4D）±4.5% ｜ 11-30（7D）±5.4% ｜ 12-02（9D）±6.5%
   ⇒ IV–VIX Spread: +90.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 1,458,056 | GEX Change vs 上次快照 -1,845,317 | Flip: Primary Flip: 72.62（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 504 / LOW 205 / INVALID 585
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 72.62（全链重定价，覆盖 98%）
Put Wall 75（弱结构｜现价低于该位 2.9%）
最近结构参考: Flip 73（现价高于该位 0.3%）
量化视角： 正 Gamma（146万，无历史分位）｜正 Gamma 减弱（185万）｜现价位于 Flip 上方 0.25%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 72（MaxPain，仅结算参考）；上方 75（Put Wall，弱结构）。
• Gamma 区域：切换参考 73（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 71.0C — Vol 803 | 最新价 $2.85 | OI 0→15034 (ΔOI +15034张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增15034张（前日OI缺失），值得跟踪（方向未知）
11-27 74.0C — Vol 1,019 | 最新价 $0.88 | OI 435→15240 (ΔOI +14805张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14805张（+3403.4% vs前日OI），连续性待观察（方向未知）
12-18 62.0P — Vol 102 | 最新价 $0.67 | OI 2678→7025 (ΔOI +4347张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4347张（+162.3% vs前日OI），连续性待观察（方向未知）
12-11 60.0P — Vol 10 | 最新价 $0.40 | OI 26→3846 (ΔOI +3820张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3820张（+14692.3% vs前日OI），连续性待观察（方向未知）
11-27 72.0C — Vol 54 | 最新价 $2.10 | OI 41→1891 (ΔOI +1850张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1850张（+4512.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 39,856 张（Put 8,167 / Call 31,689），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-25  C +0.4k / P +8 ｜ Activity HIGH ｜ 2D
11-27  C +36.5k / P +4.1k ｜ Activity HIGH ｜ 4D
11-30  C +0.4k / P +0.9k ｜ Activity HIGH ｜ 7D
12-02  C +0.2k / P +18 ｜ Activity HIGH ｜ 9D

📆 11-25 Forward Structure
存量OI: C 2.1k / P 1.1k，今日变化ΔOI: C +0.4k / P +8，平值价格ATM: C $1.31 / P $1.34 ｜ ATM IV 61.0%，净 delta 敞口 19k shares
Top ΔOI: C 75 +217 ｜ P 72 -139 ｜ C 74 +63
仓位参考: Max Pain 73 ｜ Call Wall 75（+3.0%，弱）（OI 0.4k） ｜ Put Wall 69（-5.2%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 61.0%｜历史 Rank 100%（近端代理）｜IV/RV 0.98×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 19,169 股

📆 11-27 Forward Structure
存量OI: C 89.7k / P 12.2k，今日变化ΔOI: C +36.5k / P +4.1k，平值价格ATM: C $1.70 / P $1.58 ｜ ATM IV 52.4%，净 delta 敞口 2.0M shares
Top ΔOI: C 71 +15,034 ｜ C 74 +14,805 ｜ C 72 +1,850
仓位参考: Max Pain 71 ｜ Call Wall 74（+1.6%，弱）（OI 15.2k） ｜ Put Wall 70（-3.8%，弱）（OI 2.0k）
量化解读： 存量 Call 重｜ATM IV 52.4%｜历史 Rank 100%（近端代理）｜IV/RV 0.84×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,970,265 股

📆 11-30 Forward Structure
存量OI: C 1.2k / P 1.5k，今日变化ΔOI: C +0.4k / P +0.9k，平值价格ATM: C $2.02 / P $1.91 ｜ ATM IV 48.4%，净 delta 敞口 6k shares
Top ΔOI: C 75 +219 ｜ C 73 +50
仓位参考: Max Pain 75 ｜ Call Wall 75（+3.0%，弱）（OI 0.2k） ｜ Put Wall 70（-3.8%，弱）（OI 0.3k）
量化解读： 存量 Put 重｜ATM IV 48.4%｜历史 Rank 100%（近端代理）｜IV/RV 0.78×（近似）｜净 delta 敞口 正 6,173 股

📆 12-02 Forward Structure
存量OI: C 0.7k / P 0.1k，今日变化ΔOI: C +0.2k / P +18，平值价格ATM: C $2.38 / P $2.35 ｜ ATM IV 50.6%，净 delta 敞口 8k shares
Top ΔOI: C 73 +106 ｜ C 71 +16 ｜ C 75 +16
仓位参考: Max Pain 73 ｜ Call Wall 75（+3.0%，弱）（OI 0.2k） ｜ Put Wall 74（+1.6%）（OI 55）
量化解读： 存量 Call 重｜ATM IV 50.6%｜历史 Rank 100%（近端代理）｜IV/RV 0.81×（近似）｜净 delta 敞口 正 7,549 股

📅 事件差分（观察，非因果）: 11-25（2D）ATM IV 61.0% vs 11-27 52.4%（差 +8.5pp）——覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-23/GDX_evening.json