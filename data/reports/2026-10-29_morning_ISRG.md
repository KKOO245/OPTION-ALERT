# 期权晨报 2026-10-29（快照 10:20 ET）

📊 市场环境

SPY $765.72 ｜ QQQ $715.34
VIX 16.74 ↓1.0%（5D -12.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.6（fear）
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
🟡 **事件差分**: 10-30 ATM IV 52.6% vs 11-06 39.1%（差 +13.5pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-13 470C ΔOI +2（距现价 +5.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 444.18 → 今开 447.85（+0.8%） | 较昨收变动（含盘初走势） ｜ 今日高 448.45 ｜ 低 443.65

Options: P/C成交量 0.58 | OI比 0.90 | ATM IV 52.6% | Skew 10.5pp | Term 0.61 | ExpMove ±2.9%（近端） | Rank 84%
量化视角： IV 历史高位（Rank 84%，期权偏贵）｜期限结构倒挂（Term 0.61，近月 IV 高于远月）｜保护溢价显著（Skew 10.5pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.58×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.90×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-30（1D）±2.9% ｜ 11-06（8D）±5.0% ｜ 11-13（15D）±2.6% ｜ 11-20（22D）±6.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,354,655 | GEX Change vs 上次快照 494,071 | Flip: Primary Flip: 424.25（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 265 / LOW 169 / INVALID 558
结构观察区: Primary Flip 424.25（全链重定价，覆盖 92%）
Call Wall 420（弱结构｜现价高于该位 6.6%）
最近结构参考: Flip 424（现价高于该位 5.5%）
量化视角： 正 Gamma（235万，无历史分位）｜正 Gamma 增强（+49万）｜现价位于 Flip 上方 5.54%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 435（MaxPain，仅结算参考） / 420（Call Wall，弱结构）。
• Gamma 区域：切换参考 424（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 470.0C — Vol 69 | 最新价 $1.95 | OI 25→84 (ΔOI +59张) | ΔOI/Volume 85.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增59张（+236.0% vs前日OI），连续性待观察（方向未知）
11-06 502.5C — Vol 37 | 最新价 $0.40 | OI 49→86 (ΔOI +37张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增37张（+75.5% vs前日OI），连续性待观察（方向未知）
11-06 500.0C — Vol 39 | 最新价 $0.35 | OI 6→42 (ΔOI +36张) | ΔOI/Volume 92.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增36张（+600.0% vs前日OI），连续性待观察（方向未知）
11-20 480.0C — Vol 27 | 最新价 $3.60 | OI 413→431 (ΔOI +18张) | ΔOI/Volume 66.7% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增18张（+4.4% vs前日OI），值得跟踪（方向未知）
10-30 455.0C — Vol 27 | 最新价 $2.04 | OI 133→148 (ΔOI +15张) | ΔOI/Volume 55.6% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增15张（+11.3% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 165 张（Put 0 / Call 165），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +15 / P +12 ｜ Activity MEDIUM △ ｜ 1D
11-06  C +0.1k / P +20 ｜ Activity MEDIUM △ ｜ 8D
11-13  C +6 / P -7 ｜ Activity MEDIUM △ ｜ 15D
11-20  C +22 / P +17 ｜ Activity MEDIUM △ ｜ 22D

📆 10-30 Forward Structure
存量OI: C 2.4k / P 2.2k，今日变化ΔOI: C +15 / P +12，平值价格ATM: C $6.10 / P $6.65 ｜ ATM IV 52.6%，净 delta 敞口 -1k shares
Top ΔOI: C 455 +15 ｜ C 460 +11 ｜ P 450 +10
仓位参考: Max Pain 435 ｜ Call Wall 455（+1.6%，弱）（OI 0.1k） ｜ Put Wall 455（+1.6%）（OI 0.2k）
量化解读： 存量两侧均衡｜ATM IV 52.6%｜历史 Rank 84%（近端代理）｜IV/RV 2.31×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,084 股

11-06（MEDIUM △）Top ΔOI: 470C +59
11-06（MEDIUM △）仓位参考: Max Pain 428 ｜ Call Wall 430（-4.0%，弱）（OI 0.1k） ｜ Put Wall 420（-6.2%，弱）（OI 0.2k）

11-13（MEDIUM △）Top ΔOI: 460P -10 ｜ 470C +2
11-13（MEDIUM △）仓位参考: Max Pain 425 ｜ Call Wall 440（-1.7%，弱）（OI 0.1k） ｜ Put Wall 420（-6.2%，弱）（OI 81）

11-20（MEDIUM △）Top ΔOI: 480C +18 ｜ 447P +10
11-20（MEDIUM △）仓位参考: Max Pain 400 ｜ Call Wall 420（-6.2%，弱）（OI 0.8k） ｜ Put Wall 410（-8.4%，弱）（OI 0.4k）

📅 事件差分（观察，非因果）: 10-30（1D）ATM IV 52.6% vs 11-06 39.1%（差 +13.5pp）——覆盖 GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM、PCE 物价 Price Index MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-29/ISRG_morning.json