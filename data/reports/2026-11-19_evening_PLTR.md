# 期权晚报 2026-11-19（快照 16:40 ET）

📊 市场环境

SPY $715.87 ｜ QQQ $645.04
VIX 28.44 ↑15.8%（5D +52.1%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 18.7（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🔴 **Vol Regime 升档**: ELEVATED → STRESS（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 160.94 → 收盘 153.68（-4.5%） ｜ 今日高 167.13 ｜ 低 153.20 ｜ 昨收 156.67 → 收盘 153.68（-1.9%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-24，窗口结束前不做对错判定）

Options: P/C成交量 0.75 | OI比 0.82 | ATM IV 91.9% | Skew 11.5pp | Term 0.63 | ExpMove ±3.9%（近端） | Rank 94%
量化视角： IV 历史高位（Rank 94%，期权偏贵）｜期限结构倒挂（Term 0.63，近月 IV 高于远月）｜保护溢价显著（Skew 11.5pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.82）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.75×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.82×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-20（1D）±3.9% ｜ 11-27（8D）±7.3% ｜ 12-04（15D）±11.6% ｜ 12-11（22D）±11.5%
   ⇒ IV–VIX Spread: +63.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -21,104,261 | GEX Change vs 上次快照 -46,163,007 | Flip: Primary Flip: 157.98（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 420 / LOW 177 / INVALID 221
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 157.98（全链重定价，覆盖 96%）
Put Wall 140（弱结构｜现价高于该位 9.8%）
最近结构参考: Flip 158（现价低于该位 2.7%）
量化视角： 负 Gamma（2110万，无历史分位）｜由正转负（4616万）｜现价位于 Flip 下方 2.72%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 140（Put Wall，弱结构）；上方 165（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 158（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C -7.7k / P -12.9k ｜ Activity HIGH ｜ 1D
11-27  C +15.8k / P +1.3k ｜ Activity HIGH ｜ 8D
12-04  C +1.3k / P +0.3k ｜ Activity HIGH ｜ 15D
12-11  C +0.2k / P +95 ｜ Activity MEDIUM △ ｜ 22D

📆 11-20 Forward Structure
存量OI: C 235.4k / P 192.0k，今日变化ΔOI: C -7.7k / P -12.9k，平值价格ATM: C $3.62 / P $2.36 ｜ ATM IV 91.9%，净 delta 敞口 1.5M shares
Top ΔOI: P 185 -7,476 ｜ P 190 -3,803
仓位参考: Max Pain 165 ｜ Call Wall 165（+7.4%，弱）（OI 12.5k） ｜ Put Wall 140（-8.9%，弱）（OI 10.0k）
量化解读： 存量 Call 重｜ATM IV 91.9%｜历史 Rank 94%（近端代理）｜IV/RV 1.73×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,542,110 股

📆 11-27 Forward Structure
存量OI: C 43.8k / P 39.0k，今日变化ΔOI: C +15.8k / P +1.3k，平值价格ATM: C $6.20 / P $4.97 ｜ ATM IV 62.5%，净 delta 敞口 396k shares
Top ΔOI: C 167 +5,108 ｜ C 162 +4,282 ｜ C 170 +3,447
仓位参考: Max Pain 160 ｜ Call Wall 167.5（+9.0%）（OI 6.8k） ｜ Put Wall 150（-2.4%，弱）（OI 4.6k）
量化解读： 存量两侧均衡｜ATM IV 62.5%｜历史 Rank 94%（近端代理）｜IV/RV 1.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 395,613 股

📆 12-04 Forward Structure
存量OI: C 19.5k / P 14.5k，今日变化ΔOI: C +1.3k / P +0.3k，平值价格ATM: C $11.15 / P $6.69 ｜ ATM IV 61.2%，净 delta 敞口 37k shares
Top ΔOI: C 160 +276 ｜ C 162 +240
仓位参考: Max Pain 168 ｜ Call Wall 160（+4.1%，弱）（OI 0.8k） ｜ Put Wall 155（+0.9%）（OI 2.8k）
量化解读： 存量 Call 重｜ATM IV 61.2%｜历史 Rank 94%（近端代理）｜IV/RV 1.15×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 37,190 股

12-11（MEDIUM △）Top ΔOI: 145P +111
12-11（MEDIUM △）仓位参考: Max Pain 170 ｜ Put Wall 150（-2.4%，弱）（OI 1.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-19/PLTR_evening.json