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
🔴 **事件差分**: 11-13（3D）ATM IV 121.1% vs 11-20 106.0%（差 +15.1pp），覆盖 Core Inflation Rate MoM、Inflation Rate MoM 等
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 11-13 900C ΔOI +961（距现价 -1.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 886.51 → 今开 861.34（-2.8%） | 较昨收变动（含盘初走势） ｜ 今日高 914.82 ｜ 低 839.41

Options: P/C成交量 0.51 | OI比 0.62 | ATM IV 121.1% | Skew 5.1pp | Term 0.74 | ExpMove ±8.9%（近端） | Rank 79%
量化视角： IV 历史高位（Rank 79%，期权偏贵）｜期限结构倒挂（Term 0.74，近月 IV 高于远月）｜保护溢价中性（Skew 5.1pp）｜存量 Call 偏重（OI比 0.62）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.51×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.62×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（3D）±8.9% ｜ 11-20（10D）±18.1% ｜ 11-27（17D）±20.4% ｜ 12-04（24D）±16.9%
   ⇒ IV–VIX Spread: +101.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 541,564 | GEX Change vs 上次快照 3,307,193 | Flip: Primary Flip: 905.00（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1911 / LOW 828 / INVALID 1271
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 905.00（全链重定价，覆盖 100%）
最近结构参考: Flip 905（现价高于该位 1.0%）
量化视角： 正 Gamma（54万，无历史分位）｜由负转正（+331万）｜现价位于 Flip 上方 1.00%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 900（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 905（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 1100.0C — Vol 3,873 | 最新价 $2.60 | OI 1156→2184 (ΔOI +1028张) | ΔOI/Volume 26.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1028张（+88.9% vs前日OI），连续性待观察（方向未知）
11-13 900.0C — Vol 4,976 | 最新价 $38.73 | OI 702→1663 (ΔOI +961张) | ΔOI/Volume 19.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增961张（+136.9% vs前日OI），连续性待观察（方向未知）
11-13 1000.0C — Vol 5,364 | 最新价 $10.40 | OI 1713→2416 (ΔOI +703张) | ΔOI/Volume 13.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增703张（+41.0% vs前日OI），连续性待观察（方向未知）
11-13 950.0C — Vol 3,161 | 最新价 $20.80 | OI 1042→1736 (ΔOI +694张) | ΔOI/Volume 22.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增694张（+66.6% vs前日OI），连续性待观察（方向未知）
11-20 900.0C — Vol 1,479 | 最新价 $60.70 | OI 932→1465 (ΔOI +533张) | ΔOI/Volume 36.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增533张（+57.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,919 张（Put 0 / Call 3,919），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +8.8k / P +3.3k ｜ Activity HIGH ｜ 3D
11-20  C +3.2k / P +0.5k ｜ Activity HIGH ｜ 10D
11-27  C +0.6k / P +0.2k ｜ Activity MEDIUM △ ｜ 17D
12-04  C +0.5k / P +0.4k ｜ Activity MEDIUM △ ｜ 24D

📆 11-13 Forward Structure
存量OI: C 45.0k / P 28.0k，今日变化ΔOI: C +8.8k / P +3.3k，平值价格ATM: C $35.46 / P $45.89 ｜ ATM IV 121.1%，净 delta 敞口 231k shares
Top ΔOI: C 1100 +1,028 ｜ C 900 +961 ｜ C 1000 +703
仓位参考: Max Pain 900 ｜ Call Wall 1000（+9.4%，弱）（OI 2.4k） ｜ Put Wall 900（-1.5%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 121.1%｜历史 Rank 79%（近端代理）｜IV/RV 0.97×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 231,062 股

📆 11-20 Forward Structure
存量OI: C 72.0k / P 52.6k，今日变化ΔOI: C +3.2k / P +0.5k，平值价格ATM: C $64.90 / P $101.00 ｜ ATM IV 106.0%，净 delta 敞口 134k shares
Top ΔOI: C 900 +533 ｜ C 1000 +451 ｜ C 925 +315
仓位参考: Max Pain 1,130 ｜ Call Wall 1000（+9.4%，弱）（OI 2.0k） ｜ Put Wall 870（-4.8%，弱）（OI 2.3k）
量化解读： 存量 Call 重｜ATM IV 106.0%｜历史 Rank 79%（近端代理）｜IV/RV 0.85×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 134,313 股

11-27（MEDIUM △）Top ΔOI: 1200C -71
11-27（MEDIUM △）仓位参考: Max Pain 1,150 ｜ Put Wall 930（+1.7%，弱）（OI 0.2k）

12-04（MEDIUM △）Top ΔOI: 980C +102 ｜ 770P +100
12-04（MEDIUM △）仓位参考: Max Pain 1,010 ｜ Call Wall 950（+3.9%，弱）（OI 0.2k） ｜ Put Wall 830（-9.2%，弱）（OI 0.2k）

📅 事件差分（观察，非因果）: 11-13（3D）ATM IV 121.1% vs 11-20 106.0%（差 +15.1pp）——覆盖 Core Inflation Rate MoM、Inflation Rate MoM 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-10/SNDK_morning.json