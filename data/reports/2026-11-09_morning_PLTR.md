# 期权晨报 2026-11-09（快照 10:20 ET）

📊 市场环境

SPY $752.91 ｜ QQQ $679.35
VIX 21.34 ↓16.8%（5D +0.9%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 31.7（fear）
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
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-13 170C ΔOI +9,136（距现价 +1.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 160.38 → 今开 161.27（+0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 168.16 ｜ 低 161.05

Options: P/C成交量 0.42 | OI比 0.73 | ATM IV 64.4% | Skew 6.6pp | Term 0.84 | ExpMove ±5.6%（近端） | Rank 85%
量化视角： IV 历史高位（Rank 85%，期权偏贵）｜期限结构倒挂（Term 0.84，近月 IV 高于远月）｜保护溢价显著（Skew 6.6pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.73）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.42×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.73×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（4D）±5.6% ｜ 11-20（11D）±8.3% ｜ 11-27（18D）±9.8% ｜ 12-04（25D）±11.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 25,289,214 | GEX Change vs 上次快照 27,704,717 | Flip: Primary Flip: 158.43（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 555 / LOW 136 / INVALID 243
结构观察区: Primary Flip 158.43（全链重定价，覆盖 100%）
最近结构参考: Flip 158（现价高于该位 5.8%）
量化视角： 正 Gamma（2529万，无历史分位）｜由负转正（+2770万）｜现价位于 Flip 上方 5.81%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 162（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 158（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 90.0P — Vol 14,750 | 最新价 $0.05 | OI 340→12667 (ΔOI +12327张) | ΔOI/Volume 83.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12327张（+3625.6% vs前日OI），连续性待观察（方向未知）
11-13 170.0C — Vol 13,603 | 最新价 $1.81 | OI 2642→11778 (ΔOI +9136张) | ΔOI/Volume 67.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9136张（+345.8% vs前日OI），连续性待观察（方向未知）
11-13 172.5C — Vol 12,301 | 最新价 $1.23 | OI 1678→8628 (ΔOI +6950张) | ΔOI/Volume 56.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6950张（+414.2% vs前日OI），连续性待观察（方向未知）
11-13 167.5C — Vol 9,054 | 最新价 $2.59 | OI 1196→7510 (ΔOI +6314张) | ΔOI/Volume 69.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6314张（+527.9% vs前日OI），连续性待观察（方向未知）
11-13 165.0C — Vol 13,331 | 最新价 $3.43 | OI 7991→14187 (ΔOI +6196张) | ΔOI/Volume 46.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6196张（+77.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 40,923 张（Put 12,327 / Call 28,596），跨 1 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +35.6k / P +33.8k ｜ Activity HIGH ｜ 4D
11-20  C +3.7k / P +0.7k ｜ Activity HIGH ｜ 11D
11-27  C +0.4k / P +3.2k ｜ Activity MEDIUM △ ｜ 18D
12-04  C +0.7k / P +0.2k ｜ Activity HIGH ｜ 25D

📆 11-13 Forward Structure
存量OI: C 105.8k / P 77.0k，今日变化ΔOI: C +35.6k / P +33.8k，平值价格ATM: C $4.60 / P $4.85 ｜ ATM IV 64.4%，净 delta 敞口 1.5M shares
Top ΔOI: C 170 +9,136 ｜ C 172 +6,950
仓位参考: Max Pain 162 ｜ Call Wall 165（-1.6%，弱）（OI 14.2k） ｜ Put Wall 155（-7.5%，弱）（OI 2.8k）
量化解读： 存量 Call 重｜ATM IV 64.4%｜历史 Rank 85%（近端代理）｜IV/RV 1.10×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,518,295 股

📆 11-20 Forward Structure
存量OI: C 184.6k / P 181.5k，今日变化ΔOI: C +3.7k / P +0.7k，平值价格ATM: C $7.05 / P $6.85 ｜ ATM IV 58.0%，净 delta 敞口 219k shares
Top ΔOI: C 180 +3,429
仓位参考: Max Pain 175 ｜ Call Wall 165（-1.6%，弱）（OI 12.5k） ｜ Put Wall 180（+7.4%，弱）（OI 9.9k）
量化解读： 存量两侧均衡｜ATM IV 58.0%｜历史 Rank 85%（近端代理）｜IV/RV 0.99×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 218,658 股

11-27（MEDIUM △）Top ΔOI: 150P +1,692
11-27（MEDIUM △）仓位参考: Max Pain 175 ｜ Call Wall 180（+7.4%，弱）（OI 0.8k） ｜ Put Wall 170（+1.4%，弱）（OI 1.3k）

📆 12-04 Forward Structure
存量OI: C 14.4k / P 8.7k，今日变化ΔOI: C +0.7k / P +0.2k，平值价格ATM: C $8.40 / P $11.55 ｜ ATM IV 52.3%，净 delta 敞口 2k shares
Top ΔOI: C 195 +366 ｜ P 160 +146
仓位参考: Max Pain 175 ｜ Call Wall 175（+4.4%，弱）（OI 0.8k） ｜ Put Wall 160（-4.6%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 52.3%｜历史 Rank 85%（近端代理）｜IV/RV 0.89×（近似）｜净 delta 敞口 正 2,431 股

📅 事件差分（观察，非因果）: 11-13（4D）ATM IV 64.4% vs 11-20 58.0%（差 +6.3pp）——覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-09/PLTR_morning.json