# 期权晨报 2026-11-11（快照 10:20 ET）

📊 市场环境

SPY $759.90 ｜ QQQ $690.38
VIX 18.31 ↓5.9%（5D +10.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 37.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-11

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **事件差分**: 11-13 ATM IV 75.6% vs 11-16 65.6%（差 +10.0pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-13 145C ΔOI +2,870（距现价 +3.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-16 145C ΔOI +2,538 占该期限总 OI 11.1%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 143.09 → 今开 143.40（+0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 145.16 ｜ 低 138.62

Options: P/C成交量 0.65 | OI比 0.88 | ATM IV 91.8% | Skew 3.1pp | Term 0.63 | ExpMove ±4.8%（近端） | Rank 93%
量化视角： IV 历史高位（Rank 93%，期权偏贵）｜期限结构倒挂（Term 0.63，近月 IV 高于远月）｜保护溢价中性（Skew 3.1pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.65×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.88×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-13（2D）±4.8% ｜ 11-16（5D）±6.5% ｜ 11-18（7D）±7.7% ｜ 11-20（9D）±8.6%
   ⇒ IV–VIX Spread: +73.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 27,714,262 | GEX Change vs 上次快照 -30,601,777 | Flip: Primary Flip: 137.98（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 907 / LOW 231 / INVALID 610
结构观察区: Primary Flip 137.98（全链重定价，覆盖 99%）
Put Wall 135（弱结构｜现价高于该位 3.8%）
最近结构参考: Flip 138（现价高于该位 1.5%）
量化视角： 正 Gamma（2771万，无历史分位）｜正 Gamma 减弱（3060万）｜现价位于 Flip 上方 1.54%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 135（Put Wall，弱结构） / 140（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 138（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-18 135.0P — Vol 8,979 | 最新价 $2.75 | OI 109→8861 (ΔOI +8752张) | ΔOI/Volume 97.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8752张（+8029.4% vs前日OI），连续性待观察（方向未知）
11-27 155.0C — Vol 6,106 | 最新价 $3.05 | OI 1463→6413 (ΔOI +4950张) | ΔOI/Volume 81.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4950张（+338.4% vs前日OI），连续性待观察（方向未知）
11-27 165.0C — Vol 4,074 | 最新价 $1.19 | OI 3039→6140 (ΔOI +3101张) | ΔOI/Volume 76.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3101张（+102.0% vs前日OI），连续性待观察（方向未知）
11-27 128.0P — Vol 3,126 | 最新价 $2.41 | OI 17→3025 (ΔOI +3008张) | ΔOI/Volume 96.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3008张（+17694.1% vs前日OI），连续性待观察（方向未知）
11-27 160.0C — Vol 4,403 | 最新价 $1.89 | OI 5351→8350 (ΔOI +2999张) | ΔOI/Volume 68.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2999张（+56.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 22,810 张（Put 11,760 / Call 11,050），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $3M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 53.4k / P 47.0k，今日成交量: C 69.7k / P 45.1k，平值价格ATM: C $1.79 / P $1.06 ｜ ATM IV 91.8%，预期波动 ±2.0%，Max Pain 140
Top ΔOI: P 140 +2,802 ｜ P 127 +1,809 ｜ C 145 +1,730

📆 Forward Expiration Structure

11-13  C +9.7k / P +9.2k ｜ Activity HIGH ｜ 2D
11-16  C +9.0k / P +1.1k ｜ Activity HIGH ｜ 5D
11-18  C +2.5k / P +10.1k ｜ Activity HIGH ｜ 7D
11-20  C +7.0k / P +4.8k ｜ Activity HIGH ｜ 9D

📆 11-13 Forward Structure
存量OI: C 194.7k / P 144.1k，今日变化ΔOI: C +9.7k / P +9.2k，平值价格ATM: C $3.73 / P $3.01 ｜ ATM IV 75.6%，净 delta 敞口 -87k shares
Top ΔOI: C 145 +2,870 ｜ P 141 +2,681 ｜ P 135 +1,783
仓位参考: Max Pain 140 ｜ Call Wall 150（+7.1%，弱）（OI 17.2k） ｜ Put Wall 135（-3.6%，弱）（OI 8.8k）
量化解读： 存量 Call 重｜ATM IV 75.6%｜历史 Rank 93%（近端代理）｜IV/RV 1.01×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 87,079 股

📆 11-16 Forward Structure
存量OI: C 17.9k / P 4.9k，今日变化ΔOI: C +9.0k / P +1.1k，平值价格ATM: C $4.85 / P $4.25 ｜ ATM IV 65.6%，净 delta 敞口 219k shares
Top ΔOI: C 145 +2,538 ｜ C 150 +1,029 ｜ C 140 +809
仓位参考: Max Pain 137 ｜ Call Wall 150（+7.1%，弱）（OI 3.3k） ｜ Put Wall 135（-3.6%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 65.6%｜历史 Rank 93%（近端代理）｜IV/RV 0.88×（近似）｜净 delta 敞口 正 219,185 股

📆 11-18 Forward Structure
存量OI: C 7.7k / P 12.3k，今日变化ΔOI: C +2.5k / P +10.1k，平值价格ATM: C $5.45 / P $5.35 ｜ ATM IV 67.1%，净 delta 敞口 -233k shares
Top ΔOI: P 135 +8,752
仓位参考: Max Pain 135 ｜ Call Wall 145（+3.5%，弱）（OI 0.9k） ｜ Put Wall 135（-3.6%）（OI 8.9k）
量化解读： 存量 Put 重｜ATM IV 67.1%｜历史 Rank 93%（近端代理）｜IV/RV 0.90×（近似）｜净 delta 敞口 负 233,455 股

📆 11-20 Forward Structure
存量OI: C 455.4k / P 368.0k，今日变化ΔOI: C +7.0k / P +4.8k，平值价格ATM: C $6.25 / P $5.76 ｜ ATM IV 68.7%，净 delta 敞口 34k shares
Top ΔOI: C 145 +1,921 ｜ P 142 +1,427
仓位参考: Max Pain 145 ｜ Call Wall 145（+3.5%，弱）（OI 40.2k） ｜ Put Wall 130（-7.2%，弱）（OI 33.9k）
量化解读： 存量 Call 重｜ATM IV 68.7%｜历史 Rank 93%（近端代理）｜IV/RV 0.92×（近似）｜净 delta 敞口 正 34,016 股

📅 事件差分（观察，非因果）: 11-13（2D）ATM IV 75.6% vs 11-16 65.6%（差 +10.0pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-11/SPCX_morning.json