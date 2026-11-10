# 期权晨报 2026-11-09（快照 10:20 ET）

📊 市场环境

SPY $752.69 ｜ QQQ $679.35
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
🟡 **近现价集中开仓**: 11-11 90C ΔOI +555（距现价 -0.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 87.60 → 今开 90.12（+2.9%） | 较昨收变动（含盘初走势） ｜ 今日高 91.48 ｜ 低 89.90

Options: P/C成交量 0.57 | OI比 0.73 | ATM IV 58.6% | Skew 4.0pp | Term 0.77 | ExpMove ±3.6%（近端） | Rank 93%
量化视角： IV 历史高位（Rank 93%，期权偏贵）｜期限结构倒挂（Term 0.77，近月 IV 高于远月）｜保护溢价中性（Skew 4.0pp）｜存量 Call 偏重（OI比 0.73）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.57×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.73×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-11（2D）±3.6% ｜ 11-13（4D）±5.1% ｜ 11-16（7D）±5.3% ｜ 11-18（9D）±3.3%
   ⇒ IV–VIX Spread: +37.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 74,468,344 | GEX Change vs 上次快照 58,600,754 | Flip: Primary Flip: 83.94（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 707 / LOW 164 / INVALID 447
结构观察区: Primary Flip 83.94（全链重定价，覆盖 100%）
最近结构参考: Flip 84（现价高于该位 7.7%）
量化视角： 正 Gamma（7447万，无历史分位）｜正 Gamma 增强（+5860万）｜现价位于 Flip 上方 7.67%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 86（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 84（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 88.0C — Vol 10,464 | 最新价 $1.86 | OI 3270→13318 (ΔOI +10048张) | ΔOI/Volume 96.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10048张（+307.3% vs前日OI），连续性待观察（方向未知）
11-13 91.0C — Vol 10,060 | 最新价 $0.80 | OI 2623→12649 (ΔOI +10026张) | ΔOI/Volume 99.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10026张（+382.2% vs前日OI），连续性待观察（方向未知）
11-13 92.5C — Vol 8,327 | 最新价 $0.58 | OI 84→8365 (ΔOI +8281张) | ΔOI/Volume 99.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8281张（+9858.3% vs前日OI），连续性待观察（方向未知）
11-13 89.5C — Vol 8,266 | 最新价 $1.19 | OI 328→8578 (ΔOI +8250张) | ΔOI/Volume 99.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8250张（+2515.2% vs前日OI），连续性待观察（方向未知）
11-13 92.0C — Vol 7,195 | 最新价 $0.70 | OI 5239→12350 (ΔOI +7111张) | ΔOI/Volume 98.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7111张（+135.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 43,716 张（Put 0 / Call 43,716），跨 1 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 6.0k / P 4.4k，今日成交量: C 3.0k / P 1.7k，平值价格ATM: C $0.77 / P $0.41 ｜ ATM IV 58.6%，预期波动 ±1.3%，Max Pain 86
Top ΔOI: C 92 +1,284 ｜ P 86 +1,228 ｜ C 91 +721

📆 Forward Expiration Structure

11-11  C +1.3k / P +0.3k ｜ Activity HIGH ｜ 2D
11-13  C +51.8k / P +9.2k ｜ Activity HIGH ｜ 4D
11-16  C +81 / P +49 ｜ Activity MEDIUM △ ｜ 7D
11-18  C +42 / P +0.1k ｜ Activity MEDIUM △ ｜ 9D

📆 11-11 Forward Structure
存量OI: C 5.4k / P 1.7k，今日变化ΔOI: C +1.3k / P +0.3k，平值价格ATM: C $1.80 / P $1.45 ｜ ATM IV 55.0%，净 delta 敞口 59k shares
Top ΔOI: C 90 +555 ｜ C 93 +532 ｜ P 83 +96
仓位参考: Max Pain 79 ｜ Call Wall 85（-6.0%）（OI 2.2k）
量化解读： 存量 Call 重｜ATM IV 55.0%｜历史 Rank 93%（近端代理）｜IV/RV 1.09×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 58,594 股

📆 11-13 Forward Structure
存量OI: C 80.8k / P 33.4k，今日变化ΔOI: C +51.8k / P +9.2k，平值价格ATM: C $2.19 / P $2.38 ｜ ATM IV 54.7%，净 delta 敞口 2.7M shares
Top ΔOI: C 88 +10,048 ｜ C 91 +10,026 ｜ C 92 +8,281
仓位参考: Max Pain 83 ｜ Call Wall 88（-2.6%，弱）（OI 13.3k）
量化解读： 存量 Call 重｜ATM IV 54.7%｜历史 Rank 93%（近端代理）｜IV/RV 1.09×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,683,557 股

11-16（MEDIUM △）Top ΔOI: 90C +45 ｜ 86P +25
11-16（MEDIUM △）仓位参考: Max Pain 82 ｜ Call Wall 88（-2.6%，弱）（OI 0.2k） ｜ Put Wall 86（-4.8%，弱）（OI 76）

11-18（MEDIUM △）Top ΔOI: 88P +31 ｜ 85C +30
11-18（MEDIUM △）仓位参考: Max Pain 85 ｜ Call Wall 87（-3.7%）（OI 98）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-09/GDX_morning.json