# 期权晨报 2026-11-09（快照 10:20 ET）

📊 市场环境

SPY $748.41 ｜ QQQ $674.66
VIX 21.34 ↓16.8%（5D +0.9%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 31.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-09

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-10 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周二 11-10 08:30　【高】Core Inflation Rate YoY　预测 2.8 ｜ 实际 待公布 ｜ 前值 2.6
- 周二 11-10 08:30　【高】Inflation Rate MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.6
- 周二 11-10 08:30　【高】Inflation Rate YoY　预测 3.9 ｜ 实际 待公布 ｜ 前值 3.7
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-13 450P ΔOI +66（距现价 -1.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 452.80 → 今开 456.02（+0.7%） | 较昨收变动（含盘初走势） ｜ 今日高 458.99 ｜ 低 454.04

Options: P/C成交量 0.18 | OI比 1.15 | ATM IV 45.8% | Skew 0.7pp | Term 0.79 | ExpMove ±7.9%（近端） | Rank 77%
量化视角： IV 历史高位（Rank 77%，期权偏贵）｜期限结构倒挂（Term 0.79，近月 IV 高于远月）｜保护溢价薄（Skew 0.7pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.18×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.15×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-13（4D）±7.9% ｜ 11-20（11D）±0.0% ｜ 11-27（18D）±0.0% ｜ 12-04（25D）±8.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 3,142,369 | GEX Change vs 上次快照 1,096,354 | Flip: Primary Flip: 414.59（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 359 / LOW 161 / INVALID 484
结构观察区: Primary Flip 414.59（全链重定价，覆盖 97%）
Call Wall 500（弱结构｜现价低于该位 8.7%）
最近结构参考: Call Wall 500（现价低于该位 8.7%）
量化视角： 正 Gamma（314万，无历史分位）｜正 Gamma 增强（+110万）｜现价位于 Flip 上方 10.11%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 440（MaxPain，仅结算参考）；上方 500（Call Wall，弱结构）。
• Gamma 区域：切换参考 415（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 450.0P — Vol 70 | 最新价 $7.81 | OI 19→85 (ΔOI +66张) | ΔOI/Volume 94.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增66张（+347.4% vs前日OI），连续性待观察（方向未知）
12-11 505.0C — Vol 46 | 最新价 $4.05 | OI 7→51 (ΔOI +44张) | ΔOI/Volume 95.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增44张（+628.6% vs前日OI），连续性待观察（方向未知）
11-13 450.0C — Vol 38 | 最新价 $11.50 | OI 27→59 (ΔOI +32张) | ΔOI/Volume 84.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增32张（+118.5% vs前日OI），连续性待观察（方向未知）
12-04 460.0C — Vol 35 | 最新价 $14.67 | OI 9→40 (ΔOI +31张) | ΔOI/Volume 88.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增31张（+344.4% vs前日OI），连续性待观察（方向未知）
11-20 412.5P — Vol 24 | 最新价 $1.90 | OI 10→34 (ΔOI +24张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增24张（+240.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 197 张（Put 90 / Call 107），跨 4 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +0.1k / P +93 ｜ Activity HIGH ｜ 4D
11-20  C +0 / P +36 ｜ Activity LOW ｜ 11D
11-27  C +2 / P +2 ｜ Activity MEDIUM △ ｜ 18D
12-04  C +60 / P +14 ｜ Activity MEDIUM △ ｜ 25D

📆 11-13 Forward Structure
存量OI: C 1.2k / P 1.4k，今日变化ΔOI: C +0.1k / P +93，平值价格ATM: C $27.56 / P $8.45 ｜ ATM IV 45.8%，净 delta 敞口 2k shares
Top ΔOI: P 450 +66 ｜ C 450 +32 ｜ C 485 +13
仓位参考: Max Pain 440 ｜ Call Wall 440（-3.6%，弱）（OI 0.1k） ｜ Put Wall 462.5（+1.3%，弱）（OI 0.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 45.8%｜历史 Rank 77%（近端代理）｜IV/RV 1.05×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,808 股

11-20（Activity LOW）仓位参考: Max Pain 405 ｜ Call Wall 420（-8.0%，弱）（OI 0.8k） ｜ Put Wall 427.5（-6.4%，弱）（OI 0.4k）

11-27（MEDIUM △）Top ΔOI: 435C -3 ｜ 420C +1
11-27（MEDIUM △）仓位参考: Max Pain 430 ｜ Call Wall 430（-5.8%，弱）（OI 64）

12-04（MEDIUM △）Top ΔOI: 460C +31 ｜ 465C +20
12-04（MEDIUM △）仓位参考: Max Pain 440 ｜ Call Wall 475（+4.1%）（OI 92） ｜ Put Wall 420（-8.0%，弱）（OI 17）

📅 事件差分（观察，非因果）: 11-13（4D）ATM IV 45.8% vs 11-20 39.9%（差 +5.9pp）——覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-09/ISRG_morning.json