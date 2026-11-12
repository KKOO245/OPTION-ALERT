# 期权晨报 2026-11-11（快照 10:20 ET）

📊 市场环境

SPY $759.81 ｜ QQQ $nan
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
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **事件差分**: 11-13 ATM IV 64.4% vs 11-16 51.0%（差 +13.4pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-16 170C ΔOI +3,923（距现价 -1.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 168.89 → 今开 172.72（+2.3%） | 较昨收变动（含盘初走势） ｜ 今日高 175.13 ｜ 低 170.77

Options: P/C成交量 0.60 | OI比 0.59 | ATM IV 73.6% | Skew 1.6pp | Term 0.77 | ExpMove ±4.1%（近端） | Rank 91%
量化视角： IV 历史高位（Rank 91%，期权偏贵）｜期限结构倒挂（Term 0.77，近月 IV 高于远月）｜保护溢价薄（Skew 1.6pp）｜存量 Call 偏重（OI比 0.59）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.60×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.59×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（2D）±4.1% ｜ 11-16（5D）±4.9% ｜ 11-18（7D）±9.5% ｜ 11-20（9D）±10.1%
   ⇒ IV–VIX Spread: +55.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 63,594,200 | GEX Change vs 上次快照 206,685,555 | Flip: Primary Flip: 170.39（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 1189 / LOW 241 / INVALID 836
结构观察区: Primary Flip 170.39（全链重定价，覆盖 98%）
Call Wall 185（弱结构｜现价低于该位 6.5%）
最近结构参考: Flip 170（现价高于该位 1.5%）
量化视角： 正 Gamma（6359万，无历史分位）｜由负转正（+2.07亿）｜现价位于 Flip 上方 1.52%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 170（MaxPain，仅结算参考）；上方 185（Call Wall，弱结构）。
• Gamma 区域：切换参考 170（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-11 170.0C — Vol 184,867 | 最新价 $2.35 | OI 1586→23757 (ΔOI +22171张) | ΔOI/Volume 12.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增22171张（+1397.9% vs前日OI），连续性待观察（方向未知）
11-11 175.0C — Vol 203,862 | 最新价 $0.82 | OI 3333→22439 (ΔOI +19106张) | ΔOI/Volume 9.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增19106张（+573.2% vs前日OI），连续性待观察（方向未知）
11-20 185.0C — Vol 36,594 | 最新价 $3.35 | OI 10083→28993 (ΔOI +18910张) | ΔOI/Volume 51.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18910张（+187.5% vs前日OI），连续性待观察（方向未知）
11-13 162.5P — Vol 31,686 | 最新价 $2.12 | OI 3607→20581 (ΔOI +16974张) | ΔOI/Volume 53.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16974张（+470.6% vs前日OI），连续性待观察（方向未知）
11-11 165.0P — Vol 184,139 | 最新价 $1.45 | OI 5460→21641 (ΔOI +16181张) | ΔOI/Volume 8.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16181张（+296.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 93,342 张（Put 33,155 / Call 60,187），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $6M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 265.2k / P 155.3k，今日成交量: C 260.8k / P 156.4k，平值价格ATM: C $1.85 / P $0.98 ｜ ATM IV 73.6%，预期波动 ±1.6%，Max Pain 170
Top ΔOI: C 170 +22,171 ｜ C 175 +19,106 ｜ P 165 +16,181

📆 Forward Expiration Structure

11-13  C +49.0k / P +48.3k ｜ Activity HIGH ｜ 2D
11-16  C +47.0k / P +17.1k ｜ Activity HIGH ｜ 5D
11-18  C +22.6k / P +14.9k ｜ Activity HIGH ｜ 7D
11-20  C +66.6k / P +31.1k ｜ Activity HIGH ｜ 9D

📆 11-13 Forward Structure
存量OI: C 515.7k / P 404.3k，今日变化ΔOI: C +49.0k / P +48.3k，平值价格ATM: C $4.00 / P $3.02 ｜ ATM IV 64.4%，净 delta 敞口 3.3M shares
Top ΔOI: C 207 -19,766 ｜ P 162 +16,974 ｜ C 200 -15,614
仓位参考: Max Pain 180 ｜ Call Wall 190（+9.8%，弱）（OI 40.5k） ｜ Put Wall 160（-7.5%，弱）（OI 24.1k）
量化解读： 存量 Call 重｜ATM IV 64.4%｜历史 Rank 91%（近端代理）｜IV/RV 1.29×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 3,285,171 股

📆 11-16 Forward Structure
存量OI: C 101.2k / P 43.4k，今日变化ΔOI: C +47.0k / P +17.1k，平值价格ATM: C $4.75 / P $3.75 ｜ ATM IV 51.0%，净 delta 敞口 1.1M shares
Top ΔOI: C 182 +6,524 ｜ C 190 +5,913 ｜ C 170 +3,923
仓位参考: Max Pain 172 ｜ Call Wall 190（+9.8%，弱）（OI 9.3k） ｜ Put Wall 160（-7.5%，弱）（OI 4.8k）
量化解读： 存量 Call 重｜ATM IV 51.0%｜历史 Rank 91%（近端代理）｜IV/RV 1.02×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 1,088,545 股

📆 11-18 Forward Structure
存量OI: C 72.7k / P 39.0k，今日变化ΔOI: C +22.6k / P +14.9k，平值价格ATM: C $8.70 / P $7.80 ｜ ATM IV 83.8%，净 delta 敞口 485k shares
Top ΔOI: C 200 +3,902 ｜ C 170 +2,873 ｜ C 180 +2,721
仓位参考: Max Pain 175 ｜ Call Wall 190（+9.8%，弱）（OI 5.7k） ｜ Put Wall 160（-7.5%，弱）（OI 3.8k）
量化解读： 存量 Call 重｜ATM IV 83.8%｜历史 Rank 91%（近端代理）｜IV/RV 1.67×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 485,094 股

📆 11-20 Forward Structure
存量OI: C 1132.8k / P 744.5k，今日变化ΔOI: C +66.6k / P +31.1k，平值价格ATM: C $9.25 / P $8.20 ｜ ATM IV 79.5%，净 delta 敞口 3.4M shares
Top ΔOI: C 185 +18,910 ｜ C 200 -13,412 ｜ C 170 +12,291
仓位参考: Max Pain 200 ｜ Call Wall 185（+7.0%，弱）（OI 29.0k） ｜ Put Wall 190（+9.8%）（OI 89.8k）
量化解读： 存量 Call 重｜ATM IV 79.5%｜历史 Rank 91%（近端代理）｜IV/RV 1.59×（近似）｜净 delta 敞口 正 3,368,389 股

📅 事件差分（观察，非因果）: 11-13（2D）ATM IV 64.4% vs 11-16 51.0%（差 +13.4pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-11/NVDA_morning.json