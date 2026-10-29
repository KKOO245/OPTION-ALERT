# 期权晨报 2026-10-29（快照 10:20 ET）

📊 市场环境

SPY $769.48 ｜ QQQ $716.11
VIX 16.74 ↓1.0%（5D -12.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.6（fear）
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
🟡 **事件差分**: 10-30 ATM IV 57.6% vs 11-06 44.2%（差 +13.4pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-30 535C ΔOI +1,742（距现价 +4.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-06 550C ΔOI +7,514 占该期限总 OI 15.6%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 521.94 → 今开 512.03（-1.9%） | 较昨收变动（含盘初走势） ｜ 今日高 514.99 ｜ 低 506.62

Options: P/C成交量 9.21 | OI比 6.19 | ATM IV 57.6% | Skew 10.8pp | Term 0.71 | ExpMove ±2.6%（近端） | Rank 92%
量化视角： IV 历史高位（Rank 92%，期权偏贵）｜期限结构倒挂（Term 0.71，近月 IV 高于远月）｜保护溢价显著（Skew 10.8pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 9.21）——观察点，非方向信号
   ⇒ Put/Call Volume: 9.21×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 6.19×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-30（1D）±2.6% ｜ 11-06（8D）±4.9% ｜ 11-13（15D）±6.8% ｜ 11-20（22D）±13.5%
   ⇒ IV–VIX Spread: +40.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 7,328,746 | GEX Change vs 上次快照 -7,247,600 | Flip: Primary Flip: 509.44（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 610 / LOW 277 / INVALID 705
结构观察区: Primary Flip 509.44（全链重定价，覆盖 96%）
最近结构参考: Flip 509（现价高于该位 0.6%）
量化视角： 正 Gamma（733万，无历史分位）｜正 Gamma 减弱（725万）｜现价位于 Flip 上方 0.61%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 515（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 509（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 480.0P — Vol 11,699 | 最新价 $0.41 | OI 8289→17886 (ΔOI +9597张) | ΔOI/Volume 82.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9597张（+115.8% vs前日OI），连续性待观察（方向未知）
10-30 470.0P — Vol 10,190 | 最新价 $0.40 | OI 5697→14709 (ΔOI +9012张) | ΔOI/Volume 88.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9012张（+158.2% vs前日OI），连续性待观察（方向未知）
11-06 550.0C — Vol 7,619 | 最新价 $4.38 | OI 8970→16484 (ΔOI +7514张) | ΔOI/Volume 98.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7514张（+83.8% vs前日OI），连续性待观察（方向未知）
11-06 540.0C — Vol 7,618 | 最新价 $6.45 | OI 6619→14094 (ΔOI +7475张) | ΔOI/Volume 98.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7475张（+112.9% vs前日OI），连续性待观察（方向未知）
10-30 535.0C — Vol 2,212 | 最新价 $3.10 | OI 376→2118 (ΔOI +1742张) | ΔOI/Volume 78.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1742张（+463.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 35,340 张（Put 18,609 / Call 16,731），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +2.8k / P +17.0k ｜ Activity HIGH ｜ 1D
11-06  C +15.0k / P +1.6k ｜ Activity HIGH ｜ 8D
11-13  C -0.6k / P +36 ｜ Activity MEDIUM △ ｜ 15D
11-20  C -1.0k / P -1.5k ｜ Activity HIGH ｜ 22D

📆 10-30 Forward Structure
存量OI: C 31.0k / P 191.8k，今日变化ΔOI: C +2.8k / P +17.0k，平值价格ATM: C $5.20 / P $8.40 ｜ ATM IV 57.6%，净 delta 敞口 -3k shares
Top ΔOI: P 480 +9,597 ｜ P 470 +9,012 ｜ C 535 +1,742
仓位参考: Max Pain 515 ｜ Call Wall 500（-2.5%，弱）（OI 2.8k） ｜ Put Wall 480（-6.4%，弱）（OI 17.9k）
量化解读： 存量 Put 重｜ATM IV 57.6%｜历史 Rank 92%（近端代理）｜IV/RV 1.37×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 3,468 股

📆 11-06 Forward Structure
存量OI: C 37.9k / P 10.2k，今日变化ΔOI: C +15.0k / P +1.6k，平值价格ATM: C $13.00 / P $12.10 ｜ ATM IV 44.2%，净 delta 敞口 239k shares
Top ΔOI: C 550 +7,514 ｜ C 540 +7,475 ｜ P 497 +802
仓位参考: Max Pain 505 ｜ Call Wall 540（+5.4%，弱）（OI 14.1k） ｜ Put Wall 500（-2.5%，弱）（OI 1.0k）
量化解读： 存量 Call 重｜ATM IV 44.2%｜历史 Rank 92%（近端代理）｜IV/RV 1.05×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 239,009 股

11-13（MEDIUM △）Top ΔOI: 520C -360 ｜ 500C -85
11-13（MEDIUM △）仓位参考: Max Pain 510 ｜ Call Wall 510（-0.5%，弱）（OI 9.6k）

📆 11-20 Forward Structure
存量OI: C 39.4k / P 63.1k，今日变化ΔOI: C -1.0k / P -1.5k，平值价格ATM: C $27.14 / P $42.00 ｜ ATM IV 43.0%，净 delta 敞口 -25k shares
Top ΔOI: P 430 -1,107 ｜ C 555 -629 ｜ P 475 +609
仓位参考: Max Pain 535 ｜ Call Wall 505（-1.5%，弱）（OI 2.7k） ｜ Put Wall 490（-4.4%，弱）（OI 3.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 43.0%｜历史 Rank 92%（近端代理）｜IV/RV 1.02×（近似）｜净 delta 敞口 负 24,809 股

📅 事件差分（观察，非因果）: 10-30（1D）ATM IV 57.6% vs 11-06 44.2%（差 +13.4pp）——覆盖 GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM、PCE 物价 Price Index MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-29/SOXX_morning.json