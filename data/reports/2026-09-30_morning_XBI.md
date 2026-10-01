# 期权晨报 2026-09-30（快照 10:20 ET）

📊 市场环境

SPY $762.63 ｜ QQQ $nan
VIX 15.68 ↓2.2%（5D +3.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 30.8（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-30

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.2 ｜ 前值 0.1　✅ 今日已公布
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 2.2 ｜ 前值 2.5　✅ 今日已公布
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 0.9 ｜ 前值 0.1　✅ 今日已公布
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **事件差分**: 10-02 ATM IV 44.5% vs 10-09 32.4%（差 +12.1pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-02 152P ΔOI +1,306（距现价 -2.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 156.81 → 今开 157.84（+0.7%） | 较昨收变动（含盘初走势） ｜ 今日高 158.10 ｜ 低 156.48

Options: P/C成交量 0.09 | OI比 2.72 | ATM IV 44.5% | Skew -4.1pp | Term 0.72 | ExpMove ±2.4%（近端） | Rank 93%
量化视角： IV 历史高位（Rank 93%，期权偏贵）｜期限结构倒挂（Term 0.72，近月 IV 高于远月）｜Put 保护异常便宜（Skew -4.1pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.09×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 2.72×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-02（2D）±2.4% ｜ 10-09（9D）±4.1% ｜ 10-16（16D）±5.3% ｜ 10-23（23D）±7.2%
   ⇒ IV–VIX Spread: +28.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -37,993,555 | GEX Change vs 上次快照 -4,727,925 | Flip: Primary Flip: 163.85（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 372 / LOW 76 / INVALID 314
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 163.85（全链重定价，覆盖 99%）
Put Wall 150（现价高于该位 4.5%）
最近结构参考: Flip 164（现价低于该位 4.4%）
量化视角： 负 Gamma（3799万，无历史分位）｜负 Gamma 加深（473万）｜现价位于 Flip 下方 4.35%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（Put Wall） / 156（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 164（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 152.5P — Vol 2,483 | 最新价 $0.67 | OI 2590→3896 (ΔOI +1306张) | ΔOI/Volume 52.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1306张（+50.4% vs前日OI），连续性待观察（方向未知）
10-02 156.0P — Vol 517 | 最新价 $2.52 | OI 218→720 (ΔOI +502张) | ΔOI/Volume 97.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增502张（+230.3% vs前日OI），连续性待观察（方向未知）
10-02 148.0P — Vol 624 | 最新价 $0.14 | OI 9890→10355 (ΔOI +465张) | ΔOI/Volume 74.5% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增465张（+4.7% vs前日OI），值得跟踪（方向未知）
10-16 162.0C — Vol 518 | 最新价 $2.20 | OI 1248→1633 (ΔOI +385张) | ΔOI/Volume 74.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增385张（+30.9% vs前日OI），连续性待观察（方向未知）
10-16 152.0P — Vol 509 | 最新价 $2.23 | OI 238→602 (ΔOI +364张) | ΔOI/Volume 71.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增364张（+152.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,022 张（Put 2,637 / Call 385），跨 2 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +0.1k / P +1.4k ｜ Activity HIGH ｜ 2D
10-09  C +0.1k / P +0.8k ｜ Activity HIGH ｜ 9D
10-16  C +0.5k / P +0.3k ｜ Activity MEDIUM △ ｜ 16D
10-23  C +0.2k / P -8 ｜ Activity MEDIUM △ ｜ 23D

📆 10-02 Forward Structure
存量OI: C 12.3k / P 33.5k，今日变化ΔOI: C +0.1k / P +1.4k，平值价格ATM: C $2.00 / P $1.80 ｜ ATM IV 44.5%，净 delta 敞口 -19k shares
Top ΔOI: P 152 +1,306 ｜ P 155 -805 ｜ P 156 +502
仓位参考: Max Pain 156 ｜ Call Wall 162（+3.4%，弱）（OI 1.6k） ｜ Put Wall 148（-5.6%）（OI 10.4k）
量化解读： 存量 Put 重｜ATM IV 44.5%｜历史 Rank 93%（近端代理）｜IV/RV 1.82×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 18,971 股

📆 10-09 Forward Structure
存量OI: C 1.0k / P 3.9k，今日变化ΔOI: C +0.1k / P +0.8k，平值价格ATM: C $3.02 / P $3.47 ｜ ATM IV 32.4%，净 delta 敞口 -14k shares
Top ΔOI: P 155 +307 ｜ P 154 +99 ｜ P 152 +88
仓位参考: Max Pain 156 ｜ Call Wall 158（+0.8%，弱）（OI 0.2k） ｜ Put Wall 150（-4.3%，弱）（OI 0.6k）
量化解读： 存量 Put 重｜ATM IV 32.4%｜历史 Rank 93%（近端代理）｜IV/RV 1.33×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 14,064 股

10-16（MEDIUM △）Top ΔOI: 162C +385 ｜ 152P +364
10-16（MEDIUM △）仓位参考: Max Pain 162 ｜ Call Wall 165（+5.3%，弱）（OI 2.9k） ｜ Put Wall 150（-4.3%）（OI 22.5k）

10-23（MEDIUM △）Top ΔOI: 155C +73 ｜ 145P -33
10-23（MEDIUM △）仓位参考: Max Pain 156 ｜ Call Wall 155（-1.1%，弱）（OI 78） ｜ Put Wall 153（-2.4%）（OI 0.4k）

📅 事件差分（观察，非因果）: 10-02（2D）ATM IV 44.5% vs 10-09 32.4%（差 +12.1pp）——覆盖 PCE 物价 Price Index MoM、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-30/XBI_morning.json