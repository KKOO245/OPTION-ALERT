# 期权晚报 2026-11-13（快照 16:40 ET）

📊 市场环境

SPY $754.37 ｜ QQQ $679.89
VIX 19.30 ↑3.2%（5D -24.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-13

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 0.3 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🔵 **期限 OI 集中**: 11-18 130P ΔOI +7,149 占该期限总 OI 18.9%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## SPCX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPCX: 今开 140.17 → 收盘 139.11（-0.8%） ｜ 今日高 142.24 ｜ 低 136.64 ｜ 昨收 139.94 → 收盘 139.11（-0.6%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-20，窗口结束前不做对错判定）

Options: P/C成交量 0.58 | OI比 0.77 | ATM IV 89.4% | Skew 10.8pp | Term 0.66 | ExpMove ±4.9%（近端） | Rank 93%
量化视角： IV 历史高位（Rank 93%，期权偏贵）｜期限结构倒挂（Term 0.66，近月 IV 高于远月）｜保护溢价显著（Skew 10.8pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.77）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.58×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.77×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-16（3D）±4.9% ｜ 11-18（5D）±6.9% ｜ 11-20（7D）±8.3% ｜ 11-23（10D）±8.7%
   ⇒ IV–VIX Spread: +70.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 14,337,971 | GEX Change vs 上次快照 -2,578,512 | Flip: Primary Flip: 137.42（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 779 / LOW 245 / INVALID 580
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 137.42（全链重定价，覆盖 91%）
Put Wall 130（弱结构｜现价高于该位 7.0%）
最近结构参考: Flip 137（现价高于该位 1.2%）
量化视角： 正 Gamma（1434万，无历史分位）｜正 Gamma 减弱（258万）｜现价位于 Flip 上方 1.23%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 130（Put Wall，弱结构）；上方 140（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 137（全链重定价，覆盖 91%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-16  C +8.3k / P +3.3k ｜ Activity HIGH ｜ 3D
11-18  C +3.1k / P +8.6k ｜ Activity HIGH ｜ 5D
11-20  C +33.9k / P +10.1k ｜ Activity HIGH ｜ 7D
11-23  C +0.3k / P +0.9k ｜ Activity HIGH ｜ 10D

📆 11-16 Forward Structure
存量OI: C 51.2k / P 12.2k，今日变化ΔOI: C +8.3k / P +3.3k，平值价格ATM: C $3.45 / P $3.35 ｜ ATM IV 67.8%，净 delta 敞口 17k shares
Top ΔOI: C 150 +1,564
仓位参考: Max Pain 140 ｜ Call Wall 150（+7.8%，弱）（OI 6.7k） ｜ Put Wall 140（+0.6%）（OI 1.2k）
量化解读： 存量 Call 重｜ATM IV 67.8%｜历史 Rank 93%（近端代理）｜IV/RV 0.90×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 16,516 股

📆 11-18 Forward Structure
存量OI: C 14.0k / P 23.9k，今日变化ΔOI: C +3.1k / P +8.6k，平值价格ATM: C $4.87 / P $4.71 ｜ ATM IV 73.8%，净 delta 敞口 -187k shares
Top ΔOI: P 130 +7,149 ｜ C 150 +601
仓位参考: Max Pain 141 ｜ Call Wall 150（+7.8%，弱）（OI 1.6k） ｜ Put Wall 135（-3.0%，弱）（OI 9.9k）
量化解读： 存量 Put 重｜ATM IV 73.8%｜历史 Rank 93%（近端代理）｜IV/RV 0.98×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 186,532 股

📆 11-20 Forward Structure
存量OI: C 473.5k / P 379.2k，今日变化ΔOI: C +33.9k / P +10.1k，平值价格ATM: C $5.86 / P $5.76 ｜ ATM IV 75.2%，净 delta 敞口 1k shares
Top ΔOI: C 170 +15,392 ｜ C 175 +7,990 ｜ C 160 +5,616
仓位参考: Max Pain 145 ｜ Call Wall 145（+4.2%，弱）（OI 38.5k） ｜ Put Wall 130（-6.5%，弱）（OI 34.9k）
量化解读： 存量 Call 重｜ATM IV 75.2%｜历史 Rank 93%（近端代理）｜IV/RV 1.00×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,008 股

📆 11-23 Forward Structure
存量OI: C 3.6k / P 1.7k，今日变化ΔOI: C +0.3k / P +0.9k，平值价格ATM: C $6.35 / P $5.72 ｜ ATM IV 67.3%，净 delta 敞口 -28k shares
Top ΔOI: P 140 +244 ｜ P 138 +163
仓位参考: Max Pain 141 ｜ Call Wall 150（+7.8%）（OI 1.1k） ｜ Put Wall 140（+0.6%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 67.3%｜历史 Rank 93%（近端代理）｜IV/RV 0.89×（近似）｜净 delta 敞口 负 27,761 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-13/SPCX_evening.json