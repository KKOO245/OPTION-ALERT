# 期权晨报 2026-09-30（快照 10:20 ET）

📊 市场环境

SPY $769.13 ｜ QQQ $743.60
VIX 15.68 ↓2.2%（5D +3.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-30

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.2 ｜ 前值 0.1　✅ 今日已公布
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 0.9 ｜ 前值 0.1　✅ 今日已公布
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 2.2 ｜ 前值 2.5　✅ 今日已公布
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **事件差分**: 10-02（2D）ATM IV 48.9% vs 10-09 33.1%（差 +15.9pp），覆盖 PCE 物价 Price Index MoM、Personal Spending MoM 等
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 10-16 407P ΔOI +41（距现价 -0.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-23 425C ΔOI +451 占该期限总 OI 17.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 412.18 → 今开 410.45（-0.4%） | 较昨收变动（含盘初走势） ｜ 今日高 410.74 ｜ 低 405.93

Options: P/C成交量 0.07 | OI比 1.57 | ATM IV 48.9% | Skew -1.5pp | Term 0.89 | ExpMove ±2.8%（近端） | Rank 80%
量化视角： IV 历史高位（Rank 80%，期权偏贵）｜期限结构倒挂（Term 0.89，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.5pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.07×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.57×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-02（2D）±2.8% ｜ 10-09（9D）±4.9% ｜ 10-16（16D）±5.5% ｜ 10-23（23D）±9.1%
   ⇒ IV–VIX Spread: +33.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 3,159,884 | GEX Change vs 上次快照 -707,765 | Flip: Primary Flip: 389.35（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 300 / LOW 161 / INVALID 401
结构观察区: Primary Flip 389.35（全链重定价，覆盖 97%）
Call Wall 420（弱结构｜现价低于该位 2.5%）
最近结构参考: Call Wall 420（现价低于该位 2.5%）
量化视角： 正 Gamma（316万，无历史分位）｜正 Gamma 减弱（71万）｜现价位于 Flip 上方 5.15%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 392（MaxPain，仅结算参考）；上方 420（Call Wall，弱结构）。
• Gamma 区域：切换参考 389（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 360.0P — Vol 1,000 | 最新价 $0.49 | OI 419→1349 (ΔOI +930张) | ΔOI/Volume 93.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增930张（+222.0% vs前日OI），连续性待观察（方向未知）
10-23 425.0C — Vol 530 | 最新价 $13.11 | OI 21→472 (ΔOI +451张) | ΔOI/Volume 85.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增451张（+2147.6% vs前日OI），连续性待观察（方向未知）
10-23 415.0P — Vol 439 | 最新价 $20.90 | OI 34→450 (ΔOI +416张) | ΔOI/Volume 94.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增416张（+1223.5% vs前日OI），连续性待观察（方向未知）
10-02 425.0C — Vol 211 | 最新价 $1.54 | OI 98→178 (ΔOI +80张) | ΔOI/Volume 37.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增80张（+81.6% vs前日OI），连续性待观察（方向未知）
10-16 407.5P — Vol 41 | 最新价 $8.90 | OI 1→42 (ΔOI +41张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增41张（+4100.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,918 张（Put 1,387 / Call 531），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +60 / P +67 ｜ Activity MEDIUM △ ｜ 2D
10-09  C +43 / P +14 ｜ Activity MEDIUM △ ｜ 9D
10-16  C +47 / P +1.1k ｜ Activity MEDIUM △ ｜ 16D
10-23  C +0.5k / P +0.4k ｜ Activity MEDIUM △ ｜ 23D

📆 10-02 Forward Structure
存量OI: C 2.2k / P 3.5k，今日变化ΔOI: C +60 / P +67，平值价格ATM: C $4.72 / P $6.67 ｜ ATM IV 48.9%，净 delta 敞口 -1k shares
Top ΔOI: C 425 +80 ｜ C 405 +25 ｜ P 400 +24
仓位参考: Max Pain 392 ｜ Call Wall 410（+0.1%，弱）（OI 0.3k）
量化解读： 存量 Put 重｜ATM IV 48.9%｜历史 Rank 80%（近端代理）｜IV/RV 1.86×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,441 股

10-09（MEDIUM △）Top ΔOI: 405C +27 ｜ 400C +7
10-09（MEDIUM △）仓位参考: Max Pain 375 ｜ Call Wall 420（+2.6%，弱）（OI 0.1k） ｜ Put Wall 370（-9.6%，弱）（OI 17）

10-16（MEDIUM △）Top ΔOI: 360P +930 ｜ 407P +41
10-16（MEDIUM △）仓位参考: Max Pain 390 ｜ Call Wall 400（-2.3%，弱）（OI 0.9k） ｜ Put Wall 380（-7.2%，弱）（OI 0.6k）

10-23（MEDIUM △）Top ΔOI: 425C +451 ｜ 415P +416
10-23（MEDIUM △）仓位参考: Max Pain 415 ｜ Call Wall 425（+3.8%）（OI 0.5k） ｜ Put Wall 415（+1.4%）（OI 0.5k）

📅 事件差分（观察，非因果）: 10-02（2D）ATM IV 48.9% vs 10-09 33.1%（差 +15.9pp）——覆盖 PCE 物价 Price Index MoM、Personal Spending MoM 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-30/ISRG_morning.json