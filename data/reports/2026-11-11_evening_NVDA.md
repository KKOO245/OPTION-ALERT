# 期权晚报 2026-11-11（快照 16:40 ET）

📊 市场环境

SPY $759.81 ｜ QQQ $nan
VIX 17.49 ↓10.1%（5D +5.3%） ｜ Vol Regime: NORMAL
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
🟡 **事件差分**: 11-13 ATM IV 62.4% vs 11-16 50.4%（差 +12.0pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-16 182C ΔOI +6,524（距现价 +5.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 172.72 → 收盘 173.73（+0.6%） ｜ 今日高 177.54 ｜ 低 170.77 ｜ 昨收 168.89 → 收盘 173.73（+2.9%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-18，窗口结束前不做对错判定）

Options: P/C成交量 0.70 | OI比 0.59 | ATM IV 73.7% | Skew 5.9pp | Term 0.75 | ExpMove ±3.7%（近端） | Rank 91%
量化视角： IV 历史高位（Rank 91%，期权偏贵）｜期限结构倒挂（Term 0.75，近月 IV 高于远月）｜保护溢价中性（Skew 5.9pp）｜存量 Call 偏重（OI比 0.59）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.70×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.59×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（2D）±3.7% ｜ 11-16（5D）±4.8% ｜ 11-18（7D）±9.3% ｜ 11-20（9D）±9.8%
   ⇒ IV–VIX Spread: +56.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 54,227,563 | GEX Change vs 上次快照 -9,366,637 | Flip: Primary Flip: 170.95（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 1206 / LOW 259 / INVALID 801
结构观察区: Primary Flip 170.95（全链重定价，覆盖 94%）
Call Wall 185（弱结构｜现价低于该位 6.1%）
最近结构参考: Flip 171（现价高于该位 1.6%）
量化视角： 正 Gamma（5423万，无历史分位）｜正 Gamma 减弱（937万）｜现价位于 Flip 上方 1.63%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 170（MaxPain，仅结算参考）；上方 185（Call Wall，弱结构）。
• Gamma 区域：切换参考 171（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +49.0k / P +48.3k ｜ Activity HIGH ｜ 2D
11-16  C +47.0k / P +17.1k ｜ Activity HIGH ｜ 5D
11-18  C +22.6k / P +14.9k ｜ Activity HIGH ｜ 7D
11-20  C +66.6k / P +31.1k ｜ Activity HIGH ｜ 9D

📆 11-13 Forward Structure
存量OI: C 515.7k / P 404.3k，今日变化ΔOI: C +49.0k / P +48.3k，平值价格ATM: C $3.95 / P $2.53 ｜ ATM IV 62.4%，净 delta 敞口 3.5M shares
Top ΔOI: P 162 +16,974 ｜ C 200 -15,614
仓位参考: Max Pain 180 ｜ Call Wall 190（+9.4%，弱）（OI 40.5k） ｜ Put Wall 160（-7.9%，弱）（OI 24.1k）
量化解读： 存量 Call 重｜ATM IV 62.4%｜历史 Rank 91%（近端代理）｜IV/RV 1.25×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 3,475,082 股

📆 11-16 Forward Structure
存量OI: C 101.2k / P 43.4k，今日变化ΔOI: C +47.0k / P +17.1k，平值价格ATM: C $4.85 / P $3.41 ｜ ATM IV 50.4%，净 delta 敞口 1.1M shares
Top ΔOI: C 182 +6,524 ｜ C 190 +5,913 ｜ C 170 +3,923
仓位参考: Max Pain 172 ｜ Call Wall 190（+9.4%，弱）（OI 9.3k） ｜ Put Wall 160（-7.9%，弱）（OI 4.8k）
量化解读： 存量 Call 重｜ATM IV 50.4%｜历史 Rank 91%（近端代理）｜IV/RV 1.01×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 1,124,950 股

📆 11-18 Forward Structure
存量OI: C 72.7k / P 39.0k，今日变化ΔOI: C +22.6k / P +14.9k，平值价格ATM: C $8.80 / P $7.30 ｜ ATM IV 84.1%，净 delta 敞口 507k shares
Top ΔOI: C 200 +3,902 ｜ C 170 +2,873 ｜ C 180 +2,721
仓位参考: Max Pain 175 ｜ Call Wall 190（+9.4%，弱）（OI 5.7k） ｜ Put Wall 160（-7.9%，弱）（OI 3.8k）
量化解读： 存量 Call 重｜ATM IV 84.1%｜历史 Rank 91%（近端代理）｜IV/RV 1.68×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 507,033 股

📆 11-20 Forward Structure
存量OI: C 1132.8k / P 744.5k，今日变化ΔOI: C +66.6k / P +31.1k，平值价格ATM: C $9.30 / P $7.80 ｜ ATM IV 79.0%，净 delta 敞口 3.4M shares
Top ΔOI: C 185 +18,910 ｜ C 200 -13,412 ｜ C 170 +12,291
仓位参考: Max Pain 200 ｜ Call Wall 185（+6.5%，弱）（OI 29.0k） ｜ Put Wall 190（+9.4%）（OI 89.8k）
量化解读： 存量 Call 重｜ATM IV 79.0%｜历史 Rank 91%（近端代理）｜IV/RV 1.58×（近似）｜净 delta 敞口 正 3,443,090 股

📅 事件差分（观察，非因果）: 11-13（2D）ATM IV 62.4% vs 11-16 50.4%（差 +12.0pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-11/NVDA_evening.json