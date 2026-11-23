# 期权晨报 2026-11-23（快照 10:20 ET）

📊 市场环境

SPY $723.32 ｜ QQQ $651.03
VIX 27.37 ↓23.7%（5D +19.5%） ｜ Vol Regime: STRESS
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
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-27 74C ΔOI +14,805（距现价 +1.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-27 71C ΔOI +15,034 占该期限总 OI 14.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 68.40 → 今开 73.85（+8.0%） | 较昨收变动（含盘初走势） ｜ 今日高 74.47 ｜ 低 72.08

Options: P/C成交量 0.26 | OI比 0.54 | ATM IV 86.8% | Skew 14.0pp | Term 0.59 | ExpMove ±4.2%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.59，近月 IV 高于远月）｜保护溢价显著（Skew 14.0pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.54）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.26×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.54×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-25（2D）±4.2% ｜ 11-27（4D）±4.9% ｜ 11-30（7D）±5.3% ｜ 12-02（9D）±5.5%
   ⇒ IV–VIX Spread: +59.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 3,303,373 | GEX Change vs 上次快照 39,198,112 | Flip: Primary Flip: 72.45（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 576 / LOW 210 / INVALID 508
结构观察区: Primary Flip 72.45（全链重定价，覆盖 99%）
Put Wall 75（弱结构｜现价低于该位 2.8%）
最近结构参考: Flip 72（现价高于该位 0.6%）
量化视角： 正 Gamma（330万，无历史分位）｜由负转正（+3920万）｜现价位于 Flip 上方 0.61%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 72（MaxPain，仅结算参考）；上方 75（Put Wall，弱结构）。
• Gamma 区域：切换参考 72（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 71.0C — Vol 15,555 | 最新价 $1.14 | OI 0→15034 (ΔOI +15034张) | ΔOI/Volume 96.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15034张（前日OI缺失），连续性待观察（方向未知）
11-27 74.0C — Vol 15,145 | 最新价 $0.40 | OI 435→15240 (ΔOI +14805张) | ΔOI/Volume 97.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14805张（+3403.4% vs前日OI），连续性待观察（方向未知）
12-18 62.0P — Vol 7,469 | 最新价 $1.95 | OI 2678→7025 (ΔOI +4347张) | ΔOI/Volume 58.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4347张（+162.3% vs前日OI），连续性待观察（方向未知）
12-11 60.0P — Vol 3,832 | 最新价 $1.12 | OI 26→3846 (ΔOI +3820张) | ΔOI/Volume 99.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3820张（+14692.3% vs前日OI），连续性待观察（方向未知）
11-27 72.0C — Vol 1,910 | 最新价 $0.86 | OI 41→1891 (ΔOI +1850张) | ΔOI/Volume 96.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1850张（+4512.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 39,856 张（Put 8,167 / Call 31,689），跨 3 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 5.4k / P 2.9k，今日成交量: C 2.0k / P 0.5k，平值价格ATM: C $0.70 / P $0.68 ｜ ATM IV 86.8%，预期波动 ±1.9%，Max Pain 72
Top ΔOI: C 72 +667 ｜ P 65 +230 ｜ C 73 +216

📆 Forward Expiration Structure

11-25  C +0.4k / P +8 ｜ Activity MEDIUM △ ｜ 2D
11-27  C +36.5k / P +4.1k ｜ Activity HIGH ｜ 4D
11-30  C +0.4k / P +0.9k ｜ Activity HIGH ｜ 7D
12-02  C +0.2k / P +18 ｜ Activity MEDIUM △ ｜ 9D

📆 11-25 Forward Structure
存量OI: C 2.1k / P 1.1k，今日变化ΔOI: C +0.4k / P +8，平值价格ATM: C $1.40 / P $1.70 ｜ ATM IV 66.4%，净 delta 敞口 21k shares
Top ΔOI: C 75 +217 ｜ P 72 -139 ｜ C 74 +63
仓位参考: Max Pain 73 ｜ Call Wall 75（+2.9%，弱）（OI 0.4k） ｜ Put Wall 69（-5.3%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 66.4%｜历史 Rank 100%（近端代理）｜IV/RV 1.06×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 20,929 股

📆 11-27 Forward Structure
存量OI: C 89.7k / P 12.2k，今日变化ΔOI: C +36.5k / P +4.1k，平值价格ATM: C $1.55 / P $2.01 ｜ ATM IV 58.8%，净 delta 敞口 2.0M shares
Top ΔOI: C 71 +15,034 ｜ C 74 +14,805 ｜ C 72 +1,850
仓位参考: Max Pain 71 ｜ Call Wall 74（+1.5%，弱）（OI 15.2k） ｜ Put Wall 70（-4.0%，弱）（OI 2.0k）
量化解读： 存量 Call 重｜ATM IV 58.8%｜历史 Rank 100%（近端代理）｜IV/RV 0.94×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,030,372 股

📆 11-30 Forward Structure
存量OI: C 1.2k / P 1.5k，今日变化ΔOI: C +0.4k / P +0.9k，平值价格ATM: C $1.58 / P $2.26 ｜ ATM IV 54.8%，净 delta 敞口 6k shares
Top ΔOI: C 75 +219 ｜ C 73 +50
仓位参考: Max Pain 75 ｜ Call Wall 75（+2.9%，弱）（OI 0.2k） ｜ Put Wall 70（-4.0%，弱）（OI 0.3k）
量化解读： 存量 Put 重｜ATM IV 54.8%｜历史 Rank 100%（近端代理）｜IV/RV 0.88×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 6,023 股

12-02（MEDIUM △）Top ΔOI: 73C +106 ｜ 71C +16
12-02（MEDIUM △）仓位参考: Max Pain 73 ｜ Call Wall 75（+2.9%，弱）（OI 0.2k） ｜ Put Wall 74（+1.5%）（OI 55）

📅 事件差分（观察，非因果）: 11-25（2D）ATM IV 66.4% vs 11-27 58.8%（差 +7.6pp）——覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-23/GDX_morning.json