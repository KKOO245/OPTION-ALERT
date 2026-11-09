# 期权晨报 2026-11-09（快照 10:20 ET）

📊 市场环境

SPY $748.63 ｜ QQQ $674.69
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
🟡 **事件差分**: 11-13 ATM IV 119.6% vs 11-20 107.9%（差 +11.8pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 835.06 → 今开 856.96（+2.6%） | 较昨收变动（含盘初走势） ｜ 今日高 891.00 ｜ 低 830.64

Options: P/C成交量 0.50 | OI比 0.68 | ATM IV 119.6% | Skew 9.5pp | Term 0.79 | ExpMove ±10.3%（近端） | Rank 78%
量化视角： IV 历史高位（Rank 78%，期权偏贵）｜期限结构倒挂（Term 0.79，近月 IV 高于远月）｜保护溢价显著（Skew 9.5pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.68）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.50×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.68×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（4D）±10.3% ｜ 11-20（11D）±15.4% ｜ 11-27（18D）±17.7% ｜ 12-04（25D）±24.0%
   ⇒ IV–VIX Spread: +98.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -2,257,372 | GEX Change vs 上次快照 429,897 | Flip: Primary Flip: 931.96（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 2003 / LOW 696 / INVALID 1175
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 931.96（全链重定价，覆盖 100%）
最近结构参考: Flip 932（现价低于该位 5.5%）
量化视角： 负 Gamma（226万，无历史分位）｜负 Gamma 缓解（+43万）｜现价位于 Flip 下方 5.49%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 940（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 932（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 1000.0C — Vol 2,905 | 最新价 $8.00 | OI 566→1713 (ΔOI +1147张) | ΔOI/Volume 39.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1147张（+202.7% vs前日OI），连续性待观察（方向未知）
11-13 410.0P — Vol 1,295 | 最新价 $0.28 | OI 0→1038 (ΔOI +1038张) | ΔOI/Volume 80.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1038张（前日OI缺失），连续性待观察（方向未知）
11-13 500.0P — Vol 759 | 最新价 $0.93 | OI 0→660 (ΔOI +660张) | ΔOI/Volume 87.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增660张（前日OI缺失），连续性待观察（方向未知）
11-13 940.0C — Vol 864 | 最新价 $16.85 | OI 40→648 (ΔOI +608张) | ΔOI/Volume 70.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增608张（+1520.0% vs前日OI），连续性待观察（方向未知）
11-13 1100.0C — Vol 1,574 | 最新价 $2.53 | OI 611→1156 (ΔOI +545张) | ΔOI/Volume 34.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增545张（+89.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,998 张（Put 1,698 / Call 2,300），跨 1 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +7.6k / P +8.1k ｜ Activity HIGH ｜ 4D
11-20  C +1.9k / P +0.7k ｜ Activity HIGH ｜ 11D
11-27  C +0.9k / P +84 ｜ Activity MEDIUM △ ｜ 18D
12-04  C +0.4k / P +0.7k ｜ Activity HIGH ｜ 25D

📆 11-13 Forward Structure
存量OI: C 36.2k / P 24.7k，今日变化ΔOI: C +7.6k / P +8.1k，平值价格ATM: C $42.70 / P $48.40 ｜ ATM IV 119.6%，净 delta 敞口 120k shares
Top ΔOI: C 1000 +1,147
仓位参考: Max Pain 940 ｜ Call Wall 950（+7.9%，弱）（OI 1.0k） ｜ Put Wall 820（-6.9%，弱）（OI 0.9k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 119.6%｜历史 Rank 78%（近端代理）｜IV/RV 0.98×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 120,455 股

📆 11-20 Forward Structure
存量OI: C 68.8k / P 52.1k，今日变化ΔOI: C +1.9k / P +0.7k，平值价格ATM: C $65.90 / P $69.60 ｜ ATM IV 107.9%，净 delta 敞口 64k shares
Top ΔOI: C 800 -1,181 ｜ P 680 +508 ｜ P 730 +258
仓位参考: Max Pain 1,150 ｜ Call Wall 800（-9.2%，弱）（OI 1.1k） ｜ Put Wall 870（-1.2%，弱）（OI 2.1k）
量化解读： 存量 Call 重｜ATM IV 107.9%｜历史 Rank 78%（近端代理）｜IV/RV 0.88×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 64,263 股

11-27（MEDIUM △）Top ΔOI: 910C +139 ｜ 1000C +134
11-27（MEDIUM △）仓位参考: Max Pain 1,170 ｜ Put Wall 930（+5.6%，弱）（OI 0.2k）

📆 12-04 Forward Structure
存量OI: C 6.6k / P 5.0k，今日变化ΔOI: C +0.4k / P +0.7k，平值价格ATM: C $90.60 / P $121.11 ｜ ATM IV 96.0%，净 delta 敞口 9k shares
Top ΔOI: P 410 +124 ｜ C 950 +120
仓位参考: Max Pain 1,060 ｜ Call Wall 950（+7.9%，弱）（OI 0.2k） ｜ Put Wall 820（-6.9%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 96.0%｜历史 Rank 78%（近端代理）｜IV/RV 0.78×（近似）｜净 delta 敞口 正 9,328 股

📅 事件差分（观察，非因果）: 11-13（4D）ATM IV 119.6% vs 11-20 107.9%（差 +11.8pp）——覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-09/SNDK_morning.json