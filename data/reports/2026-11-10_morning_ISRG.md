# 期权晨报 2026-11-10（快照 10:20 ET）

📊 市场环境

SPY $750.86 ｜ QQQ $674.76
VIX 19.85 ↓0.3%（5D -4.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-10

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-10 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周二 11-10 08:30　【高】Inflation Rate MoM　预测 0.3 ｜ 实际 0.4 ｜ 前值 0.6　✅ 今日已公布
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **事件差分**: 11-13 ATM IV 49.9% vs 11-20 36.9%（差 +13.0pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-13 467C ΔOI +68（距现价 +2.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 460.56 → 今开 458.00（-0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 458.80 ｜ 低 450.82

Options: P/C成交量 0.27 | OI比 0.96 | ATM IV 49.9% | Skew 7.0pp | Term 0.68 | ExpMove ±3.6%（近端） | Rank 83%
量化视角： IV 历史高位（Rank 83%，期权偏贵）｜期限结构倒挂（Term 0.68，近月 IV 高于远月）｜保护溢价显著（Skew 7.0pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.27×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.96×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-13（3D）±3.6% ｜ 11-20（10D）±4.9% ｜ 11-27（17D）±4.3% ｜ 12-04（24D）±8.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 3,225,768 | GEX Change vs 上次快照 -367,351 | Flip: Primary Flip: 415.97（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 335 / LOW 176 / INVALID 493
结构观察区: Primary Flip 415.97（全链重定价，覆盖 96%）
Call Wall 480（弱结构｜现价低于该位 5.4%）
最近结构参考: Call Wall 480（现价低于该位 5.4%）
量化视角： 正 Gamma（323万，无历史分位）｜正 Gamma 减弱（37万）｜现价位于 Flip 上方 9.20%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 440（MaxPain，仅结算参考）；上方 480（Call Wall，弱结构）。
• Gamma 区域：切换参考 416（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 480.0C — Vol 171 | 最新价 $1.75 | OI 41→176 (ΔOI +135张) | ΔOI/Volume 79.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增135张（+329.3% vs前日OI），连续性待观察（方向未知）
11-13 467.5C — Vol 68 | 最新价 $5.00 | OI 50→118 (ΔOI +68张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增68张（+136.0% vs前日OI），连续性待观察（方向未知）
11-20 447.5P — Vol 24 | 最新价 $5.80 | OI 36→59 (ΔOI +23张) | ΔOI/Volume 95.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增23张（+63.9% vs前日OI），连续性待观察（方向未知）
11-20 410.0P — Vol 96 | 最新价 $0.57 | OI 449→472 (ΔOI +23张) | ΔOI/Volume 24.0% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增23张（+5.1% vs前日OI），值得跟踪（方向未知）
11-13 470.0C — Vol 18 | 最新价 $3.30 | OI 37→54 (ΔOI +17张) | ΔOI/Volume 94.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17张（+46.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 266 张（Put 46 / Call 220），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +0.3k / P +56 ｜ Activity MEDIUM △ ｜ 3D
11-20  C +1 / P +52 ｜ Activity MEDIUM △ ｜ 10D
11-27  C +6 / P +12 ｜ Activity LOW ｜ 17D
12-04  C -8 / P +28 ｜ Activity MEDIUM △ ｜ 24D

📆 11-13 Forward Structure
存量OI: C 1.5k / P 1.5k，今日变化ΔOI: C +0.3k / P +56，平值价格ATM: C $11.22 / P $5.26 ｜ ATM IV 49.9%，净 delta 敞口 3k shares
Top ΔOI: C 480 +135 ｜ C 467 +68 ｜ C 470 +17
仓位参考: Max Pain 440 ｜ Call Wall 480（+5.7%，弱）（OI 0.2k） ｜ Put Wall 462.5（+1.8%，弱）（OI 0.1k）
量化解读： 存量两侧均衡｜ATM IV 49.9%｜历史 Rank 83%（近端代理）｜IV/RV 1.14×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 3,473 股

11-20（MEDIUM △）Top ΔOI: 450C -24 ｜ 410P +23
11-20（MEDIUM △）仓位参考: Max Pain 410 ｜ Call Wall 420（-7.5%，弱）（OI 0.8k） ｜ Put Wall 410（-9.7%，弱）（OI 0.5k）

11-27（Activity LOW）仓位参考: Max Pain 430 ｜ Call Wall 430（-5.3%，弱）（OI 64） ｜ Put Wall 410（-9.7%，弱）（OI 42）

12-04（MEDIUM △）Top ΔOI: 460P +10 ｜ 475C -10
12-04（MEDIUM △）仓位参考: Max Pain 450 ｜ Call Wall 475（+4.6%，弱）（OI 82） ｜ Put Wall 410（-9.7%，弱）（OI 20）

📅 事件差分（观察，非因果）: 11-13（3D）ATM IV 49.9% vs 11-20 36.9%（差 +13.0pp）——覆盖 Core Inflation Rate MoM、Inflation Rate MoM 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-10/ISRG_morning.json