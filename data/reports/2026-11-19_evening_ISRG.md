# 期权晚报 2026-11-19（快照 16:40 ET）

📊 市场环境

SPY $715.87 ｜ QQQ $nan
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


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 420.95 → 收盘 407.24（-3.3%） ｜ 今日高 425.08 ｜ 低 404.85 ｜ 昨收 420.95 → 收盘 407.24（-3.3%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-24，窗口结束前不做对错判定）

Options: P/C成交量 2.17 | OI比 0.98 | ATM IV 58.7% | Skew -5.8pp | Term 0.58 | ExpMove ±2.3%（近端） | Rank 91%
量化视角： IV 历史高位（Rank 91%，期权偏贵）｜期限结构倒挂（Term 0.58，近月 IV 高于远月）｜Put 保护异常便宜（Skew -5.8pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 2.17）——观察点，非方向信号
   ⇒ Put/Call Volume: 2.17×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.98×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-20（1D）±2.3% ｜ 11-27（8D）±2.0% ｜ 12-04（15D）±2.9% ｜ 12-11（22D）±0.9%
   ⇒ IV–VIX Spread: +30.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -752,664 | GEX Change vs 上次快照 -1,667,586 | Flip: Primary Flip: 411.30（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 82%（带内） ｜ IV 有效性: VALID 260 / LOW 224 / INVALID 498
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 411.30（全链重定价，覆盖 82%）
最近结构参考: Flip 411（现价低于该位 1.0%）
量化视角： 负 Gamma（75万，无历史分位）｜由正转负（167万）｜现价位于 Flip 下方 0.99%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 405（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 411（全链重定价，覆盖 82%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C +67 / P -0.4k ｜ Activity MEDIUM △ ｜ 1D
11-27  C +70 / P +31 ｜ Activity HIGH ｜ 8D
12-04  C +24 / P +18 ｜ Activity MEDIUM △ ｜ 15D
12-11  C -1 / P +2 ｜ Activity LOW ｜ 22D

📆 11-20 Forward Structure
存量OI: C 10.6k / P 10.4k，今日变化ΔOI: C +67 / P -0.4k，平值价格ATM: C $5.80 / P $3.61 ｜ ATM IV 58.7%，净 delta 敞口 34k shares
Top ΔOI: P 470 -105 ｜ P 460 -89 ｜ P 475 -71
仓位参考: Max Pain 405 ｜ Call Wall 420（+3.1%，弱）（OI 0.8k） ｜ Put Wall 380（-6.7%，弱）（OI 0.6k）
量化解读： 存量两侧均衡｜ATM IV 58.7%｜历史 Rank 91%（近端代理）｜IV/RV 1.36×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 34,433 股

📆 11-27 Forward Structure
存量OI: C 0.8k / P 0.7k，今日变化ΔOI: C +70 / P +31，平值价格ATM: C $0.00 / P $8.32 ｜ ATM IV 33.5%，净 delta 敞口 -387 shares
Top ΔOI: C 432 +46 ｜ P 410 +13
仓位参考: Max Pain 430 ｜ Call Wall 430（+5.6%，弱）（OI 65） ｜ Put Wall 395（-3.0%，弱）（OI 0.2k）
量化解读： 存量两侧均衡｜ATM IV 33.5%｜历史 Rank 91%（近端代理）｜IV/RV 0.78×（近似）｜净 delta 敞口 负 387 股

12-04（MEDIUM △）Top ΔOI: 425C +12 ｜ 430C +6
12-04（MEDIUM △）仓位参考: Max Pain 450 ｜ Call Wall 440（+8.0%，弱）（OI 17） ｜ Put Wall 405（-0.6%，弱）（OI 24）

12-11（Activity LOW）仓位参考: Max Pain 440 ｜ Call Wall 445（+9.3%，弱）（OI 50） ｜ Put Wall 435（+6.8%）（OI 36）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-19/ISRG_evening.json