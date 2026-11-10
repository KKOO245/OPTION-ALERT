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
🟡 **近现价集中开仓**: 11-20 150P ΔOI +1,786（距现价 -4.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 156.90 → 今开 155.22（-1.1%） | 较昨收变动（含盘初走势） ｜ 今日高 157.85 ｜ 低 154.85

Options: P/C成交量 38.00 | OI比 1.32 | ATM IV 43.4% | Skew 18.0pp | Term 0.79 | ExpMove ±3.2%（近端） | Rank 90%
量化视角： IV 历史高位（Rank 90%，期权偏贵）｜期限结构倒挂（Term 0.79，近月 IV 高于远月）｜保护溢价显著（Skew 18.0pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 38.00）——观察点，非方向信号
   ⇒ Put/Call Volume: 38.00×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.32×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-13（3D）±3.2% ｜ 11-20（10D）±5.0% ｜ 11-27（17D）±7.3% ｜ 12-04（24D）±3.7%
   ⇒ IV–VIX Spread: +23.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 15,453,502 | GEX Change vs 上次快照 42,449 | Flip: Primary Flip: 152.57（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 402 / LOW 138 / INVALID 382
结构观察区: Primary Flip 152.57（全链重定价，覆盖 98%）
最近结构参考: Flip 153（现价高于该位 2.9%）
量化视角： 正 Gamma（1545万，无历史分位）｜正 Gamma 增强（+4万）｜现价位于 Flip 上方 2.94%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 153（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 150.0P — Vol 2,173 | 最新价 $1.51 | OI 1701→3487 (ΔOI +1786张) | ΔOI/Volume 82.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1786张（+105.0% vs前日OI），连续性待观察（方向未知）
11-20 152.0P — Vol 1,004 | 最新价 $2.07 | OI 483→1425 (ΔOI +942张) | ΔOI/Volume 93.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增942张（+195.0% vs前日OI），连续性待观察（方向未知）
11-20 157.0P — Vol 846 | 最新价 $3.96 | OI 107→743 (ΔOI +636张) | ΔOI/Volume 75.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增636张（+594.4% vs前日OI），连续性待观察（方向未知）
11-20 160.0C — Vol 586 | 最新价 $2.35 | OI 2224→2612 (ΔOI +388张) | ΔOI/Volume 66.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增388张（+17.4% vs前日OI），连续性待观察（方向未知）
11-13 160.0C — Vol 352 | 最新价 $1.35 | OI 775→1071 (ΔOI +296张) | ΔOI/Volume 84.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增296张（+38.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,048 张（Put 3,364 / Call 684），跨 2 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +0.8k / P +1.3k ｜ Activity HIGH ｜ 3D
11-20  C +0.5k / P +2.5k ｜ Activity MEDIUM △ ｜ 10D
11-27  C +14 / P +0.1k ｜ Activity MEDIUM △ ｜ 17D
12-04  C +4 / P +0.3k ｜ Activity MEDIUM △ ｜ 24D

📆 11-13 Forward Structure
存量OI: C 5.8k / P 7.7k，今日变化ΔOI: C +0.8k / P +1.3k，平值价格ATM: C $1.87 / P $3.20 ｜ ATM IV 43.4%，净 delta 敞口 11k shares
Top ΔOI: C 160 +296 ｜ P 147 +252 ｜ P 146 +213
仓位参考: Max Pain 150 ｜ Call Wall 160（+1.9%，弱）（OI 1.1k） ｜ Put Wall 147（-6.4%）（OI 2.0k）
量化解读： 存量 Put 重｜ATM IV 43.4%｜历史 Rank 90%（近端代理）｜IV/RV 1.13×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 10,626 股

11-20（MEDIUM △）Top ΔOI: 150P +1,786 ｜ 152P +942
11-20（MEDIUM △）仓位参考: Max Pain 154 ｜ Call Wall 165（+5.1%）（OI 5.5k） ｜ Put Wall 147（-6.4%，弱）（OI 5.6k）

11-27（MEDIUM △）Top ΔOI: 142P +128 ｜ 143P +18
11-27（MEDIUM △）仓位参考: Max Pain 158 ｜ Call Wall 152.5（-2.9%，弱）（OI 0.1k） ｜ Put Wall 156（-0.7%）（OI 0.2k）

12-04（MEDIUM △）Top ΔOI: 159P +80 ｜ 156P +45
12-04（MEDIUM △）仓位参考: Max Pain 162 ｜ Call Wall 162（+3.1%，弱）（OI 44） ｜ Put Wall 159（+1.2%，弱）（OI 80）

📅 事件差分（观察，非因果）: 11-13（3D）ATM IV 43.4% vs 11-20 38.3%（差 +5.1pp）——覆盖 Core Inflation Rate MoM、Inflation Rate MoM 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-10/XBI_morning.json