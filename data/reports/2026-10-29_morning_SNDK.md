# 期权晨报 2026-10-29（快照 10:20 ET）

📊 市场环境

SPY $769.48 ｜ QQQ $715.61
VIX 16.74 ↓1.0%（5D -12.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-29

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 3.4 ｜ 前值 2.2　✅ 今日已公布
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 0.5 ｜ 前值 0.9　✅ 今日已公布
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布

🔍 重点速览
🔴 **事件差分**: 10-30（1D）ATM IV 166.1% vs 11-06 91.4%（差 +74.7pp），覆盖 GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM、PCE 物价 Price Index MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 1,404.77 → 今开 1,381.49（-1.7%） | 较昨收变动（含盘初走势） ｜ 今日高 1385.80 ｜ 低 1347.70

Options: P/C成交量 0.75 | OI比 0.80 | ATM IV 166.1% | Skew 2.3pp | Term 0.44 | ExpMove ±7.8%（近端） | Rank 96%
量化视角： IV 历史高位（Rank 96%，期权偏贵）｜期限结构倒挂（Term 0.44，近月 IV 高于远月）｜保护溢价中性（Skew 2.3pp）｜存量 Call 偏重（OI比 0.80）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.75×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.80×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-30（1D）±7.8% ｜ 11-06（8D）±5.5% ｜ 11-13（15D）±6.2% ｜ 11-20（22D）±15.6%
   ⇒ IV–VIX Spread: +149.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,427,350 | GEX Change vs 上次快照 -2,487,112 | Flip: Primary Flip: 1344.29（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 2039 / LOW 428 / INVALID 939
结构观察区: Primary Flip 1344.29（全链重定价，覆盖 100%）
Call Wall 1,500（弱结构｜现价低于该位 8.8%）
最近结构参考: Flip 1344（现价高于该位 1.8%）
量化视角： 正 Gamma（143万，无历史分位）｜正 Gamma 减弱（249万）｜现价位于 Flip 上方 1.75%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 1,370（MaxPain，仅结算参考） / 1,500（Call Wall，弱结构）。
• Gamma 区域：切换参考 1344（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 1610.0C — Vol 635 | 最新价 $5.92 | OI 683→1191 (ΔOI +508张) | ΔOI/Volume 80.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增508张（+74.4% vs前日OI），连续性待观察（方向未知）
10-30 670.0P — Vol 500 | 最新价 $0.05 | OI 442→942 (ΔOI +500张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增500张（+113.1% vs前日OI），连续性待观察（方向未知）
10-30 1720.0C — Vol 556 | 最新价 $1.23 | OI 169→612 (ΔOI +443张) | ΔOI/Volume 79.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增443张（+262.1% vs前日OI），连续性待观察（方向未知）
10-30 1650.0C — Vol 860 | 最新价 $3.63 | OI 671→1084 (ΔOI +413张) | ΔOI/Volume 48.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增413张（+61.5% vs前日OI），连续性待观察（方向未知）
10-30 1100.0P — Vol 1,296 | 最新价 $0.85 | OI 930→1305 (ΔOI +375张) | ΔOI/Volume 28.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增375张（+40.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,239 张（Put 875 / Call 1,364），跨 1 个期限｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +4.1k / P +5.0k ｜ Activity HIGH ｜ 1D
11-06  C +1.3k / P +1.3k ｜ Activity HIGH ｜ 8D
11-13  C +0.4k / P +0.4k ｜ Activity MEDIUM △ ｜ 15D
11-20  C +0.5k / P +0.7k ｜ Activity HIGH ｜ 22D

📆 10-30 Forward Structure
存量OI: C 52.9k / P 42.6k，今日变化ΔOI: C +4.1k / P +5.0k，平值价格ATM: C $53.60 / P $53.30 ｜ ATM IV 166.1%，净 delta 敞口 -57k shares
Top ΔOI: C 1610 +508
仓位参考: Max Pain 1,370 ｜ Call Wall 1500（+9.7%，弱）（OI 2.4k） ｜ Put Wall 1350（-1.3%，弱）（OI 1.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 166.1%｜历史 Rank 96%（近端代理）｜IV/RV 2.52×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 57,248 股

📆 11-06 Forward Structure
存量OI: C 18.3k / P 13.5k，今日变化ΔOI: C +1.3k / P +1.3k，平值价格ATM: C $75.69 / P $0.00 ｜ ATM IV 91.4%，净 delta 敞口 -11k shares
Top ΔOI: P 1200 -315 ｜ C 1400 -233 ｜ P 1170 +220
仓位参考: Max Pain 1,400 ｜ Call Wall 1300（-5.0%，弱）（OI 0.6k） ｜ Put Wall 1400（+2.3%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 91.4%｜历史 Rank 96%（近端代理）｜IV/RV 1.39×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 10,869 股

11-13（MEDIUM △）Top ΔOI: 1475P +41
11-13（MEDIUM △）仓位参考: Max Pain 1,480 ｜ Call Wall 1500（+9.7%，弱）（OI 0.2k） ｜ Put Wall 1300（-5.0%，弱）（OI 0.2k）

📆 11-20 Forward Structure
存量OI: C 44.6k / P 51.3k，今日变化ΔOI: C +0.5k / P +0.7k，平值价格ATM: C $105.96 / P $107.12 ｜ ATM IV 76.8%，净 delta 敞口 -7k shares
Top ΔOI: C 1630 +373 ｜ C 1400 -331
仓位参考: Max Pain 1,500 ｜ Call Wall 1500（+9.7%，弱）（OI 2.0k） ｜ Put Wall 1450（+6.0%，弱）（OI 1.2k）
量化解读： 存量两侧均衡｜ATM IV 76.8%｜历史 Rank 96%（近端代理）｜IV/RV 1.16×（近似）｜净 delta 敞口 负 6,987 股

📅 事件差分（观察，非因果）: 10-30（1D）ATM IV 166.1% vs 11-06 91.4%（差 +74.7pp）——覆盖 GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM、PCE 物价 Price Index MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-29/SNDK_morning.json