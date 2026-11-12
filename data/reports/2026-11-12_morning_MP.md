# 期权晨报 2026-11-12（快照 10:20 ET）

📊 市场环境

SPY $756.94 ｜ QQQ $685.64
VIX 18.45 ↑5.5%（5D -34.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 41.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-12

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 3.75 ｜ 前值 3.97　✅ 今日已公布
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🔴 **事件差分**: 11-13（1D）ATM IV 100.8% vs 11-20 69.3%（差 +31.6pp），覆盖 成屋销售、PPI 生产者物价 MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 36.73 → 今开 37.81（+2.9%） | 较昨收变动（含盘初走势） ｜ 今日高 37.81 ｜ 低 35.93

Options: P/C成交量 0.56 | OI比 0.34 | ATM IV 100.8% | Skew -8.0pp | Term 0.67 | ExpMove ±5.4%（近端） | Rank 93%
量化视角： IV 历史高位（Rank 93%，期权偏贵）｜期限结构倒挂（Term 0.67，近月 IV 高于远月）｜Put 保护异常便宜（Skew -8.0pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.34）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.56×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.34×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（1D）±5.4% ｜ 11-20（8D）±10.0% ｜ 11-27（15D）±10.2% ｜ 12-04（22D）±14.4%
   ⇒ IV–VIX Spread: +82.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,632,755 | GEX Change vs 上次快照 -775,382 | Flip: Primary Flip: 35.14（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 232 / LOW 89 / INVALID 171
结构观察区: Primary Flip 35.14（全链重定价，覆盖 97%）
Put Wall 35（现价高于该位 2.9%）
最近结构参考: Flip 35（现价高于该位 2.5%）
量化视角： 正 Gamma（263万，无历史分位）｜正 Gamma 减弱（78万）｜现价位于 Flip 上方 2.49%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 35（Put Wall）；上方 37（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 35（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 34.0P — Vol 918 | 最新价 $0.51 | OI 464→1269 (ΔOI +805张) | ΔOI/Volume 87.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增805张（+173.5% vs前日OI），连续性待观察（方向未知）
11-20 39.5C — Vol 721 | 最新价 $0.65 | OI 1479→2176 (ΔOI +697张) | ΔOI/Volume 96.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增697张（+47.1% vs前日OI），连续性待观察（方向未知）
11-13 39.0C — Vol 503 | 最新价 $0.15 | OI 919→1242 (ΔOI +323张) | ΔOI/Volume 64.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增323张（+35.1% vs前日OI），连续性待观察（方向未知）
11-20 35.0P — Vol 246 | 最新价 $0.75 | OI 3761→3912 (ΔOI +151张) | ΔOI/Volume 61.4% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增151张（+4.0% vs前日OI），值得跟踪（方向未知）
11-13 35.0P — Vol 434 | 最新价 $0.17 | OI 606→733 (ΔOI +127张) | ΔOI/Volume 29.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增127张（+21.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,103 张（Put 1,083 / Call 1,020），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +0.5k / P +15 ｜ Activity MEDIUM △ ｜ 1D
11-20  C +0.7k / P +0.8k ｜ Activity HIGH ｜ 8D
11-27  C +0.1k / P +0.1k ｜ Activity MEDIUM △ ｜ 15D
12-04  C +86 / P +13 ｜ Activity LOW ｜ 22D

📆 11-13 Forward Structure
存量OI: C 15.1k / P 5.1k，今日变化ΔOI: C +0.5k / P +15，平值价格ATM: C $1.30 / P $0.64 ｜ ATM IV 100.8%，净 delta 敞口 5k shares
Top ΔOI: C 39 +323 ｜ P 34 -272 ｜ P 35 +127
仓位参考: Max Pain 37 ｜ Call Wall 37（+2.7%，弱）（OI 1.7k） ｜ Put Wall 34（-5.6%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 100.8%｜历史 Rank 93%（近端代理）｜IV/RV 1.69×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 4,616 股

📆 11-20 Forward Structure
存量OI: C 25.7k / P 13.2k，今日变化ΔOI: C +0.7k / P +0.8k，平值价格ATM: C $2.20 / P $1.40 ｜ ATM IV 69.3%，净 delta 敞口 5k shares
Top ΔOI: P 34 +805 ｜ C 39 +697 ｜ P 35 +151
仓位参考: Max Pain 40 ｜ Call Wall 39.5（+9.7%，弱）（OI 2.2k） ｜ Put Wall 35（-2.8%）（OI 3.9k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 69.3%｜历史 Rank 93%（近端代理）｜IV/RV 1.16×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 4,551 股

11-27（MEDIUM △）Top ΔOI: 35P +37
11-27（MEDIUM △）仓位参考: Max Pain 42 ｜ Put Wall 38（+5.5%，弱）（OI 82）

12-04（Activity LOW）仓位参考: Max Pain 35 ｜ Call Wall 35（-2.8%）（OI 0.5k） ｜ Put Wall 34（-5.6%）（OI 0.2k）

📅 事件差分（观察，非因果）: 11-13（1D）ATM IV 100.8% vs 11-20 69.3%（差 +31.6pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-12/MP_morning.json