# 期权晨报 2026-10-13（快照 10:20 ET）

📊 市场环境

SPY $777.22 ｜ QQQ $743.48
VIX 15.31 ↑0.7%（5D +2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 46.0（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-13

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-13 10:00　【高】成屋销售　预测 3.95 ｜ 实际 3.99 ｜ 前值 3.93　✅ 今日已公布
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.6 ｜ 实际 待公布 ｜ 前值 3.4
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 待公布 ｜ 前值 2.4
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-14 390C ΔOI +3,250（距现价 +4.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 378.03 → 今开 372.17（-1.5%） | 较昨收变动（含盘初走势） ｜ 今日高 375.39 ｜ 低 371.30

Options: P/C成交量 0.74 | OI比 0.76 | ATM IV 39.9% | Skew -0.3pp | Term 1.07 | ExpMove ±1.9%（近端） | Rank 10%
量化视角： IV 历史低位（Rank 10%，期权偏便宜）｜期限结构正常（Term 1.07）｜Put 保护异常便宜（Skew -0.3pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.76）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.74×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.76×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-14（1D）±1.9% ｜ 10-16（3D）±3.5% ｜ 10-19（6D）±3.9% ｜ 10-23（10D）±7.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 39,159,275 | GEX Change vs 上次快照 -16,658,494 | Flip: Primary Flip: 368.08（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1157 / LOW 126 / INVALID 565
结构观察区: Primary Flip 368.08（全链重定价，覆盖 99%）
Call Wall 400（现价低于该位 6.6%）
最近结构参考: Flip 368（现价高于该位 1.5%）
量化视角： 正 Gamma（3916万，无历史分位）｜正 Gamma 减弱（1666万）｜现价位于 Flip 上方 1.54%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 378（MaxPain，仅结算参考） / 400（Call Wall）。
• Gamma 区域：切换参考 368（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-14 400.0C — Vol 9,194 | 最新价 $0.15 | OI 3144→7396 (ΔOI +4252张) | ΔOI/Volume 46.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4252张（+135.2% vs前日OI），连续性待观察（方向未知）
10-14 390.0C — Vol 9,051 | 最新价 $0.72 | OI 2088→5338 (ΔOI +3250张) | ΔOI/Volume 35.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3250张（+155.7% vs前日OI），连续性待观察（方向未知）
10-14 425.0C — Vol 5,330 | 最新价 $0.03 | OI 203→3072 (ΔOI +2869张) | ΔOI/Volume 53.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2869张（+1413.3% vs前日OI），连续性待观察（方向未知）
10-14 380.0C — Vol 23,183 | 最新价 $3.20 | OI 790→3618 (ΔOI +2828张) | ΔOI/Volume 12.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2828张（+358.0% vs前日OI），连续性待观察（方向未知）
10-16 382.5C — Vol 5,526 | 最新价 $4.94 | OI 2872→5452 (ΔOI +2580张) | ΔOI/Volume 46.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2580张（+89.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 15,779 张（Put 0 / Call 15,779），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-14  C +33.3k / P +20.2k ｜ Activity HIGH ｜ 1D
10-16  C +25.9k / P +14.3k ｜ Activity HIGH ｜ 3D
10-19  C +8.1k / P +3.4k ｜ Activity HIGH ｜ 6D
10-23  C +4.7k / P +2.9k ｜ Activity HIGH ｜ 10D

📆 10-14 Forward Structure
存量OI: C 53.2k / P 40.7k，今日变化ΔOI: C +33.3k / P +20.2k，平值价格ATM: C $2.93 / P $4.11 ｜ ATM IV 39.9%，净 delta 敞口 -107k shares
Top ΔOI: C 400 +4,252 ｜ C 390 +3,250
仓位参考: Max Pain 378 ｜ Call Wall 400（+7.0%，弱）（OI 7.4k） ｜ Put Wall 370（-1.0%，弱）（OI 2.8k）
量化解读： 存量 Call 重｜ATM IV 39.9%｜历史 Rank 10%（近端代理）｜IV/RV 1.39×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 107,341 股

📆 10-16 Forward Structure
存量OI: C 395.1k / P 392.5k，今日变化ΔOI: C +25.9k / P +14.3k，平值价格ATM: C $6.10 / P $7.14 ｜ ATM IV 46.4%，净 delta 敞口 53k shares
Top ΔOI: C 382 +2,580 ｜ C 380 +2,310
仓位参考: Max Pain 372 ｜ Call Wall 400（+7.0%，弱）（OI 24.4k） ｜ Put Wall 380（+1.7%，弱）（OI 15.4k）
量化解读： 存量两侧均衡｜ATM IV 46.4%｜历史 Rank 10%（近端代理）｜IV/RV 1.61×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 53,005 股

📆 10-19 Forward Structure
存量OI: C 22.4k / P 8.1k，今日变化ΔOI: C +8.1k / P +3.4k，平值价格ATM: C $6.79 / P $7.80 ｜ ATM IV 37.0%，净 delta 敞口 48k shares
Top ΔOI: C 400 +916
仓位参考: Max Pain 378 ｜ Call Wall 400（+7.0%，弱）（OI 2.7k） ｜ Put Wall 360（-3.7%，弱）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 37.0%｜历史 Rank 10%（近端代理）｜IV/RV 1.28×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 48,014 股

📆 10-23 Forward Structure
存量OI: C 67.3k / P 45.7k，今日变化ΔOI: C +4.7k / P +2.9k，平值价格ATM: C $13.17 / P $13.93 ｜ ATM IV 54.0%，净 delta 敞口 46k shares
Top ΔOI: C 390 +448
仓位参考: Max Pain 370 ｜ Call Wall 400（+7.0%，弱）（OI 5.7k） ｜ Put Wall 360（-3.7%，弱）（OI 2.7k）
量化解读： 存量 Call 重｜ATM IV 54.0%｜历史 Rank 10%（近端代理）｜IV/RV 1.87×（近似）｜净 delta 敞口 正 46,243 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-13/TSLA_morning.json