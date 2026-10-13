# 期权晨报 2026-10-12（快照 10:20 ET）

📊 市场环境

SPY $778.10 ｜ QQQ $746.04
VIX 15.29 ↑3.0%（5D -1.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 45.7（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-12

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-13 10:00　【高】成屋销售　预测 3.96 ｜ 实际 待公布 ｜ 前值 3.98
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.7 ｜ 实际 待公布 ｜ 前值 3.4
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 待公布 ｜ 前值 2.4
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览
🔴 **Vol Regime 升档**: LOW → NORMAL（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 10-14 162C ΔOI +2,643（距现价 -1.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 162.57 → 今开 164.70（+1.3%） | 较昨收变动（含盘初走势） ｜ 今日高 167.07 ｜ 低 160.85

Options: P/C成交量 0.33 | OI比 0.48 | ATM IV 68.3% | Skew -2.4pp | Term 0.75 | ExpMove ±3.3%（近端） | Rank 87%
量化视角： IV 历史高位（Rank 87%，期权偏贵）｜期限结构倒挂（Term 0.75，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.4pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.48）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.33×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.48×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-14（2D）±3.3% ｜ 10-16（4D）±4.4% ｜ 10-19（7D）±5.0% ｜ 10-21（9D）±5.8%
   ⇒ IV–VIX Spread: +53.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 110,539,686 | GEX Change vs 上次快照 57,016,150 | Flip: Primary Flip: 155.39（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 743 / LOW 186 / INVALID 467
结构观察区: Primary Flip 155.39（全链重定价，覆盖 99%）
Call Wall 180（弱结构｜现价低于该位 8.3%）
最近结构参考: Flip 155（现价高于该位 6.2%）
量化视角： 正 Gamma（1.11亿，无历史分位）｜正 Gamma 增强（+5702万）｜现价位于 Flip 上方 6.20%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 162（MaxPain，仅结算参考）；上方 180（Call Wall，弱结构）。
• Gamma 区域：切换参考 155（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 165.0C — Vol 20,200 | 最新价 $2.82 | OI 14143→17606 (ΔOI +3463张) | ΔOI/Volume 17.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3463张（+24.5% vs前日OI），连续性待观察（方向未知）
10-16 175.0C — Vol 13,952 | 最新价 $0.69 | OI 15750→19201 (ΔOI +3451张) | ΔOI/Volume 24.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3451张（+21.9% vs前日OI），连续性待观察（方向未知）
10-12 165.0C — Vol 47,785 | 最新价 $0.87 | OI 4193→7533 (ΔOI +3340张) | ΔOI/Volume 7.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3340张（+79.7% vs前日OI），连续性待观察（方向未知）
10-16 162.5C — Vol 8,391 | 最新价 $3.95 | OI 6510→9688 (ΔOI +3178张) | ΔOI/Volume 37.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3178张（+48.8% vs前日OI），连续性待观察（方向未知）
10-16 167.5C — Vol 14,979 | 最新价 $2.03 | OI 4757→7917 (ΔOI +3160张) | ΔOI/Volume 21.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3160张（+66.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 16,592 张（Put 0 / Call 16,592），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 61.2k / P 29.5k，今日成交量: C 98.6k / P 32.9k，平值价格ATM: C $1.35 / P $1.02 ｜ ATM IV 68.3%，预期波动 ±1.4%，Max Pain 162
Top ΔOI: C 165 +3,340 ｜ C 167 +3,085 ｜ C 160 +3,059

📆 Forward Expiration Structure

10-14  C +7.7k / P +3.6k ｜ Activity HIGH ｜ 2D
10-16  C +20.6k / P +19.6k ｜ Activity HIGH ｜ 4D
10-19  C +2.1k / P +0.7k ｜ Activity HIGH ｜ 7D
10-21  C +1.2k / P +0.7k ｜ Activity HIGH ｜ 9D

📆 10-14 Forward Structure
存量OI: C 18.9k / P 10.2k，今日变化ΔOI: C +7.7k / P +3.6k，平值价格ATM: C $2.89 / P $2.55 ｜ ATM IV 53.3%，净 delta 敞口 351k shares
Top ΔOI: C 162 +2,643 ｜ C 165 +1,185 ｜ P 160 +964
仓位参考: Max Pain 162 ｜ Call Wall 162.5（-1.5%，弱）（OI 3.1k） ｜ Put Wall 160（-3.0%，弱）（OI 1.7k）
量化解读： 存量 Call 重｜ATM IV 53.3%｜历史 Rank 87%（近端代理）｜IV/RV 1.12×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 350,735 股

📆 10-16 Forward Structure
存量OI: C 378.7k / P 407.7k，今日变化ΔOI: C +20.6k / P +19.6k，平值价格ATM: C $3.80 / P $3.52 ｜ ATM IV 50.5%，净 delta 敞口 436k shares
Top ΔOI: C 165 +3,463 ｜ C 175 +3,451 ｜ C 162 +3,178
仓位参考: Max Pain 150 ｜ Call Wall 170（+3.0%，弱）（OI 31.0k） ｜ Put Wall 150（-9.1%，弱）（OI 25.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 50.5%｜历史 Rank 87%（近端代理）｜IV/RV 1.06×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 435,592 股

📆 10-19 Forward Structure
存量OI: C 9.1k / P 4.7k，今日变化ΔOI: C +2.1k / P +0.7k，平值价格ATM: C $4.20 / P $3.97 ｜ ATM IV 43.7%，净 delta 敞口 81k shares
Top ΔOI: C 167 +615 ｜ C 170 +444 ｜ C 160 +347
仓位参考: Max Pain 165 ｜ Call Wall 180（+9.1%，弱）（OI 1.2k） ｜ Put Wall 165（-0.0%）（OI 1.0k）
量化解读： 存量 Call 重｜ATM IV 43.7%｜历史 Rank 87%（近端代理）｜IV/RV 0.92×（近似）｜净 delta 敞口 正 81,357 股

📆 10-21 Forward Structure
存量OI: C 3.9k / P 2.1k，今日变化ΔOI: C +1.2k / P +0.7k，平值价格ATM: C $5.00 / P $4.60 ｜ ATM IV 45.0%，净 delta 敞口 34k shares
Top ΔOI: C 170 +461 ｜ C 165 +154
仓位参考: Max Pain 162 ｜ Call Wall 170（+3.0%）（OI 0.7k） ｜ Put Wall 162.5（-1.5%）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 45.0%｜历史 Rank 87%（近端代理）｜IV/RV 0.95×（近似）｜净 delta 敞口 正 34,423 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-12/SPCX_morning.json