# 期权晨报 2026-10-13（快照 10:20 ET）

📊 市场环境

SPY $777.81 ｜ QQQ $743.57
VIX 15.31 ↑0.7%（5D +2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 44.7（fear）
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
🟡 **近现价集中开仓**: 10-16 160C ΔOI +1,475（距现价 +3.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 152.68 → 今开 153.01（+0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 156.13 ｜ 低 152.32

Options: P/C成交量 0.59 | OI比 0.67 | ATM IV 72.6% | Skew -5.1pp | Term 0.90 | ExpMove ±5.5%（近端） | Rank 34%
量化视角： IV 中性（Rank 34%）｜期限结构倒挂（Term 0.90，近月 IV 高于远月）｜Put 保护异常便宜（Skew -5.1pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.67）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.59×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.67×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（3D）±5.5% ｜ 10-23（10D）±8.6% ｜ 10-30（17D）±11.2% ｜ 11-06（24D）±13.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 68,085,655 | GEX Change vs 上次快照 6,004,691 | Flip: Primary Flip: 143.88（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 572 / LOW 91 / INVALID 217
结构观察区: Primary Flip 143.88（全链重定价，覆盖 99%）
Call Wall 165（弱结构｜现价低于该位 6.6%）
最近结构参考: Call Wall 165（现价低于该位 6.6%）
量化视角： 正 Gamma（6809万，无历史分位）｜正 Gamma 增强（+600万）｜现价位于 Flip 上方 7.08%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 141（MaxPain，仅结算参考）；上方 165（Call Wall，弱结构）。
• Gamma 区域：切换参考 144（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 125.0P — Vol 6,878 | 最新价 $0.93 | OI 4800→11254 (ΔOI +6454张) | ΔOI/Volume 93.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6454张（+134.5% vs前日OI），连续性待观察（方向未知）
10-16 160.0C — Vol 9,084 | 最新价 $1.86 | OI 31951→33426 (ΔOI +1475张) | ΔOI/Volume 16.2% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增1475张（+4.6% vs前日OI），值得跟踪（方向未知）
10-16 155.0P — Vol 5,574 | 最新价 $5.60 | OI 4569→5916 (ΔOI +1347张) | ΔOI/Volume 24.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1347张（+29.5% vs前日OI），连续性待观察（方向未知）
10-23 145.0P — Vol 1,745 | 最新价 $3.30 | OI 1267→2584 (ΔOI +1317张) | ΔOI/Volume 75.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1317张（+104.0% vs前日OI），连续性待观察（方向未知）
10-16 157.5C — Vol 5,079 | 最新价 $2.55 | OI 39504→40646 (ΔOI +1142张) | ΔOI/Volume 22.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1142张（+2.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 11,735 张（Put 9,118 / Call 2,617），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +3.6k / P +1.3k ｜ Activity HIGH ｜ 3D
10-23  C +3.2k / P +5.5k ｜ Activity HIGH ｜ 10D
10-30  C +0.2k / P +8.5k ｜ Activity HIGH ｜ 17D
11-06  C +1.0k / P +2.1k ｜ Activity MEDIUM △ ｜ 24D

📆 10-16 Forward Structure
存量OI: C 348.8k / P 234.1k，今日变化ΔOI: C +3.6k / P +1.3k，平值价格ATM: C $3.96 / P $4.50 ｜ ATM IV 72.6%，净 delta 敞口 38k shares
Top ΔOI: C 160 +1,475 ｜ P 155 +1,347
仓位参考: Max Pain 141 ｜ Call Wall 165（+7.1%，弱）（OI 45.8k） ｜ Put Wall 142（-7.8%，弱）（OI 7.1k）
量化解读： 存量 Call 重｜ATM IV 72.6%｜历史 Rank 34%（近端代理）｜IV/RV 1.46×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 37,511 股

📆 10-23 Forward Structure
存量OI: C 44.0k / P 89.3k，今日变化ΔOI: C +3.2k / P +5.5k，平值价格ATM: C $6.40 / P $6.87 ｜ ATM IV 63.8%，净 delta 敞口 31k shares
Top ΔOI: P 145 +1,317 ｜ C 160 +822 ｜ C 175 -629
仓位参考: Max Pain 158 ｜ Call Wall 165（+7.1%，弱）（OI 3.1k） ｜ Put Wall 160（+3.9%，弱）（OI 6.3k）
量化解读： 存量 Put 重｜ATM IV 63.8%｜历史 Rank 34%（近端代理）｜IV/RV 1.29×（近似）｜净 delta 敞口 正 31,419 股

📆 10-30 Forward Structure
存量OI: C 33.3k / P 50.7k，今日变化ΔOI: C +0.2k / P +8.5k，平值价格ATM: C $8.35 / P $8.93 ｜ ATM IV 65.8%，净 delta 敞口 -43k shares
Top ΔOI: P 125 +6,454
仓位参考: Max Pain 160 ｜ Call Wall 160（+3.9%，弱）（OI 3.8k） ｜ Put Wall 160（+3.9%，弱）（OI 3.4k）
量化解读： 存量 Put 重｜ATM IV 65.8%｜历史 Rank 34%（近端代理）｜IV/RV 1.33×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 42,662 股

11-06（MEDIUM △）Top ΔOI: 160C +631
11-06（MEDIUM △）仓位参考: Max Pain 160 ｜ Call Wall 160（+3.9%）（OI 1.8k） ｜ Put Wall 160（+3.9%，弱）（OI 2.8k）

📅 事件差分（观察，非因果）: 10-16（3D）ATM IV 72.6% vs 10-23 63.8%（差 +8.8pp）——覆盖 成屋销售、Core Inflation Rate MoM 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-13/MSTR_morning.json