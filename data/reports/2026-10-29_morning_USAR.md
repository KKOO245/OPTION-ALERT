# 期权晨报 2026-10-29（快照 10:20 ET）

📊 市场环境

SPY $769.48 ｜ QQQ $715.89
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
🔴 **事件差分**: 10-30（1D）ATM IV 120.3% vs 11-06 94.6%（差 +25.7pp），覆盖 GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM、PCE 物价 Price Index MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 10-30 10C ΔOI +318（距现价 +0.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 10.48 → 今开 10.15（-3.1%） | 较昨收变动（含盘初走势） ｜ 今日高 10.53 ｜ 低 10.08

Options: P/C成交量 0.19 | OI比 0.35 | ATM IV 120.3% | Skew 17.1pp | Term 0.77 | ExpMove ±5.7%（近端） | Rank 58%
量化视角： IV 中性（Rank 58%）｜期限结构倒挂（Term 0.77，近月 IV 高于远月）｜保护溢价显著（Skew 17.1pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.35）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.19×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.35×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（1D）±5.7% ｜ 11-06（8D）±12.4% ｜ 11-13（15D）±16.5% ｜ 11-20（22D）±20.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 6,105,585 | GEX Change vs 上次快照 277,193 | Flip: Primary Flip: 9.52（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 216 / LOW 74 / INVALID 130
结构观察区: Primary Flip 9.52（全链重定价，覆盖 94%）
Put Wall 10（弱结构｜现价高于该位 4.5%） | Call Wall 11（弱结构｜现价低于该位 5.0%）
最近结构参考: Put Wall 10（现价高于该位 4.5%）
量化视角： 正 Gamma（611万，无历史分位）｜正 Gamma 增强（+28万）｜现价位于 Flip 上方 9.79%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 10（Put Wall，弱结构） / 10（MaxPain，仅结算参考）；上方 11（Call Wall，弱结构）。
• Gamma 区域：切换参考 10（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 9.5P — Vol 1,271 | 最新价 $0.19 | OI 90→1141 (ΔOI +1051张) | ΔOI/Volume 82.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1051张（+1167.8% vs前日OI），连续性待观察（方向未知）
10-30 10.5C — Vol 1,495 | 最新价 $0.21 | OI 1714→2032 (ΔOI +318张) | ΔOI/Volume 21.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增318张（+18.6% vs前日OI），连续性待观察（方向未知）
11-13 11.0C — Vol 456 | 最新价 $0.62 | OI 841→1052 (ΔOI +211张) | ΔOI/Volume 46.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增211张（+25.1% vs前日OI），连续性待观察（方向未知）
10-30 11.0C — Vol 1,161 | 最新价 $0.11 | OI 4748→4950 (ΔOI +202张) | ΔOI/Volume 17.4% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增202张（+4.2% vs前日OI），值得跟踪（方向未知）
11-20 11.0C — Vol 429 | 最新价 $0.70 | OI 1797→1989 (ΔOI +192张) | ΔOI/Volume 44.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增192张（+10.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,974 张（Put 1,051 / Call 923），跨 4 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +0.2k / P -0.5k ｜ Activity MEDIUM △ ｜ 1D
11-06  C +0.4k / P +1.0k ｜ Activity HIGH ｜ 8D
11-13  C +0.4k / P +12 ｜ Activity MEDIUM △ ｜ 15D
11-20  C +0.5k / P -0.1k ｜ Activity MEDIUM △ ｜ 22D

📆 10-30 Forward Structure
存量OI: C 29.3k / P 10.4k，今日变化ΔOI: C +0.2k / P -0.5k，平值价格ATM: C $0.29 / P $0.30 ｜ ATM IV 120.3%，净 delta 敞口 11k shares
Top ΔOI: P 10 -324 ｜ C 10 +318 ｜ C 11 +202
仓位参考: Max Pain 10 ｜ Call Wall 10（-4.3%，弱）（OI 5.1k） ｜ Put Wall 10（-4.3%，弱）（OI 1.7k）
量化解读： 存量 Call 重｜ATM IV 120.3%｜历史 Rank 58%（近端代理）｜IV/RV 1.41×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 11,408 股

📆 11-06 Forward Structure
存量OI: C 8.5k / P 5.3k，今日变化ΔOI: C +0.4k / P +1.0k，平值价格ATM: C $0.60 / P $0.70 ｜ ATM IV 94.6%，净 delta 敞口 -9k shares
Top ΔOI: P 9 +1,051 ｜ C 11 +118
仓位参考: Max Pain 10 ｜ Call Wall 11（+5.3%，弱）（OI 1.0k） ｜ Put Wall 9.5（-9.1%，弱）（OI 1.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 94.6%｜历史 Rank 58%（近端代理）｜IV/RV 1.11×（近似）｜净 delta 敞口 负 9,287 股

11-13（MEDIUM △）Top ΔOI: 11C +211 ｜ 10C +106
11-13（MEDIUM △）仓位参考: Max Pain 10 ｜ Call Wall 11（+5.3%）（OI 1.1k） ｜ Put Wall 11（+5.3%，弱）（OI 0.4k）

11-20（MEDIUM △）Top ΔOI: 11C +192 ｜ 10C +163
11-20（MEDIUM △）仓位参考: Max Pain 13 ｜ Call Wall 11（+5.3%，弱）（OI 2.0k） ｜ Put Wall 10（-4.3%，弱）（OI 6.3k）

📅 事件差分（观察，非因果）: 10-30（1D）ATM IV 120.3% vs 11-06 94.6%（差 +25.7pp）——覆盖 GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM、PCE 物价 Price Index MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-29/USAR_morning.json