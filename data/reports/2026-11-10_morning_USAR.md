# 期权晨报 2026-11-10（快照 10:20 ET）

📊 市场环境

SPY $751.28 ｜ QQQ $676.43
VIX 19.85 ↓0.3%（5D -4.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.6（fear）
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
🔴 **事件差分**: 11-13（3D）ATM IV 134.4% vs 11-20 118.6%（差 +15.8pp），覆盖 Core Inflation Rate MoM、Inflation Rate MoM 等
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔵 **期限 OI 集中**: 11-13 9C ΔOI +3,453 占该期限总 OI 10.4%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 8.76 → 今开 8.27（-5.6%） | 较昨收变动（含盘初走势） ｜ 今日高 8.60 ｜ 低 7.89

Options: P/C成交量 0.18 | OI比 0.20 | ATM IV 134.4% | Skew -5.1pp | Term 0.78 | ExpMove ±10.3%（近端） | Rank 74%
量化视角： IV 中性（Rank 74%）｜期限结构倒挂（Term 0.78，近月 IV 高于远月）｜Put 保护异常便宜（Skew -5.1pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.20）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.18×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.20×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（3D）±10.3% ｜ 11-20（10D）±13.8% ｜ 11-27（17D）±20.0% ｜ 12-04（24D）±22.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,325,119 | GEX Change vs 上次快照 -414,760 | Flip: Primary Flip: 7.84（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 237 / LOW 93 / INVALID 94
结构观察区: Primary Flip 7.84（全链重定价，覆盖 100%）
Put Wall 9（弱结构｜现价低于该位 8.7%） | Call Wall 9（现价低于该位 8.7%）
最近结构参考: Flip 8（现价高于该位 4.8%）
量化视角： 正 Gamma（133万，无历史分位）｜正 Gamma 减弱（41万）｜现价位于 Flip 上方 4.81%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 8（MaxPain，仅结算参考）；上方 9（Put Wall，弱结构） / 9（Call Wall）。
• Gamma 区域：切换参考 8（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 9.5C — Vol 4,420 | 最新价 $0.27 | OI 1858→5311 (ΔOI +3453张) | ΔOI/Volume 78.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3453张（+185.8% vs前日OI），连续性待观察（方向未知）
11-13 10.0C — Vol 2,717 | 最新价 $0.16 | OI 1370→3250 (ΔOI +1880张) | ΔOI/Volume 69.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1880张（+137.2% vs前日OI），连续性待观察（方向未知）
11-20 15.0C — Vol 1,212 | 最新价 $0.02 | OI 4870→5692 (ΔOI +822张) | ΔOI/Volume 67.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增822张（+16.9% vs前日OI），连续性待观察（方向未知）
11-13 10.5C — Vol 1,359 | 最新价 $0.10 | OI 585→1388 (ΔOI +803张) | ΔOI/Volume 59.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增803张（+137.3% vs前日OI），连续性待观察（方向未知）
11-13 9.0C — Vol 2,832 | 最新价 $0.43 | OI 2974→3611 (ΔOI +637张) | ΔOI/Volume 22.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增637张（+21.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 7,595 张（Put 0 / Call 7,595），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +8.0k / P +1.3k ｜ Activity HIGH ｜ 3D
11-20  C +2.2k / P -0.1k ｜ Activity MEDIUM △ ｜ 10D
11-27  C +0.6k / P +0.2k ｜ Activity MEDIUM △ ｜ 17D
12-04  C +0.4k / P +0.1k ｜ Activity MEDIUM △ ｜ 24D

📆 11-13 Forward Structure
存量OI: C 27.6k / P 5.6k，今日变化ΔOI: C +8.0k / P +1.3k，平值价格ATM: C $0.56 / P $0.29 ｜ ATM IV 134.4%，净 delta 敞口 48k shares
仓位参考: Max Pain 8 ｜ Call Wall 9（+9.6%，弱）（OI 3.6k） ｜ Put Wall 8（-2.6%，弱）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 134.4%｜历史 Rank 74%（近端代理）｜IV/RV 1.35×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 48,431 股

11-20（MEDIUM △）Top ΔOI: 11P -318
11-20（MEDIUM △）仓位参考: Max Pain 10 ｜ Call Wall 9（+9.6%，弱）（OI 4.1k） ｜ Put Wall 8（-2.6%，弱）（OI 7.0k）

11-27（MEDIUM △）仓位参考: Max Pain 9 ｜ Call Wall 8.5（+3.5%，弱）（OI 1.1k） ｜ Put Wall 9（+9.6%，弱）（OI 0.5k）

12-04（MEDIUM △）Top ΔOI: 8P +101
12-04（MEDIUM △）仓位参考: Max Pain 10 ｜ Call Wall 9（+9.6%，弱）（OI 0.1k） ｜ Put Wall 8.5（+3.5%）（OI 0.2k）

📅 事件差分（观察，非因果）: 11-13（3D）ATM IV 134.4% vs 11-20 118.6%（差 +15.8pp）——覆盖 Core Inflation Rate MoM、Inflation Rate MoM 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-10/USAR_morning.json