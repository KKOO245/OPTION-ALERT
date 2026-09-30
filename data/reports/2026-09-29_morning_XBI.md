# 期权晨报 2026-09-29（快照 10:20 ET）

📊 市场环境

SPY $764.20 ｜ QQQ $nan
VIX 15.96 ↓0.7%（5D +12.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-29

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-29 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.23 ｜ 实际 7.079 ｜ 前值 7.335　✅ 今日已公布
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 待公布 ｜ 前值 2.1
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-02 150P ΔOI +1,397（距现价 -3.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-02 169C ΔOI +4,874 占该期限总 OI 11.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 156.61 → 今开 156.13（-0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 157.80 ｜ 低 155.19

Options: P/C成交量 0.26 | OI比 2.63 | ATM IV 41.1% | Skew -6.5pp | Term 0.78 | ExpMove ±3.1%（近端） | Rank 87%
量化视角： IV 历史高位（Rank 87%，期权偏贵）｜期限结构倒挂（Term 0.78，近月 IV 高于远月）｜Put 保护异常便宜（Skew -6.5pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.26×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 2.63×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-02（3D）±3.1% ｜ 10-09（10D）±5.0% ｜ 10-16（17D）±6.2% ｜ 10-23（24D）±7.3%
   ⇒ IV–VIX Spread: +25.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -39,653,429 | GEX Change vs 上次快照 -5,889,114 | Flip: Primary Flip: 164.55（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 343 / LOW 66 / INVALID 353
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 164.55（全链重定价，覆盖 99%）
Put Wall 150（现价高于该位 3.9%）
最近结构参考: Put Wall 150（现价高于该位 3.9%）
量化视角： 负 Gamma（3965万，无历史分位）｜负 Gamma 加深（589万）｜现价位于 Flip 下方 5.29%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（Put Wall） / 155（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 165（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 169.0C — Vol 5,005 | 最新价 $0.13 | OI 101→4975 (ΔOI +4874张) | ΔOI/Volume 97.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4874张（+4825.7% vs前日OI），连续性待观察（方向未知）
10-02 150.0P — Vol 2,211 | 最新价 $0.50 | OI 1215→2612 (ΔOI +1397张) | ΔOI/Volume 63.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1397张（+115.0% vs前日OI），连续性待观察（方向未知）
10-02 155.0P — Vol 1,297 | 最新价 $1.72 | OI 3249→4479 (ΔOI +1230张) | ΔOI/Volume 94.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1230张（+37.9% vs前日OI），连续性待观察（方向未知）
10-30 152.0P — Vol 1,247 | 最新价 $3.88 | OI 118→1286 (ΔOI +1168张) | ΔOI/Volume 93.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1168张（+989.8% vs前日OI），连续性待观察（方向未知）
10-30 140.0P — Vol 627 | 最新价 $1.43 | OI 88→712 (ΔOI +624张) | ΔOI/Volume 99.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增624张（+709.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 9,293 张（Put 4,419 / Call 4,874），跨 2 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +5.6k / P -0.1k ｜ Activity HIGH ｜ 3D
10-09  C +0.2k / P +82 ｜ Activity MEDIUM △ ｜ 10D
10-16  C +0.3k / P +0.2k ｜ Activity MEDIUM △ ｜ 17D
10-23  C +0 / P +10 ｜ Activity LOW ｜ 24D

📆 10-02 Forward Structure
存量OI: C 12.2k / P 32.1k，今日变化ΔOI: C +5.6k / P -0.1k，平值价格ATM: C $2.27 / P $2.56 ｜ ATM IV 41.1%，净 delta 敞口 -28k shares
Top ΔOI: C 169 +4,874 ｜ P 148 -2,110 ｜ P 150 +1,397
仓位参考: Max Pain 155 ｜ Call Wall 162（+3.9%，弱）（OI 1.6k） ｜ Put Wall 148（-5.0%）（OI 9.9k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 41.1%｜历史 Rank 87%（近端代理）｜IV/RV 1.68×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 27,506 股

10-09（MEDIUM △）Top ΔOI: 156C +96 ｜ 166C +32
10-09（MEDIUM △）仓位参考: Max Pain 156 ｜ Call Wall 158（+1.4%，弱）（OI 0.2k） ｜ Put Wall 150（-3.8%，弱）（OI 0.5k）

10-16（MEDIUM △）Top ΔOI: 150P +271 ｜ 163C +220
10-16（MEDIUM △）仓位参考: Max Pain 162 ｜ Call Wall 165（+5.9%，弱）（OI 2.9k） ｜ Put Wall 150（-3.8%）（OI 22.6k）

10-23（Activity LOW）仓位参考: Max Pain 159 ｜ Call Wall 154（-1.2%，弱）（OI 75） ｜ Put Wall 153（-1.8%）（OI 0.4k）

📅 事件差分（观察，非因果）: 10-02（3D）ATM IV 41.1% vs 10-09 33.2%（差 +7.8pp）——覆盖 职位空缺(JOLTS) Job Openings、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-29/XBI_morning.json