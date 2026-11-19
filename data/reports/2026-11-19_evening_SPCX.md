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
🟡 **近现价集中开仓**: 11-20 145P ΔOI +5,839（距现价 +4.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPCX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPCX: 今开 144.91 → 收盘 138.43（-4.5%） ｜ 今日高 147.29 ｜ 低 135.50 ｜ 昨收 143.50 → 收盘 138.43（-3.5%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-24，窗口结束前不做对错判定）

Options: P/C成交量 0.68 | OI比 0.79 | ATM IV 81.3% | Skew 10.7pp | Term 0.70 | ExpMove ±3.6%（近端） | Rank 90%
量化视角： IV 历史高位（Rank 90%，期权偏贵）｜期限结构倒挂（Term 0.70，近月 IV 高于远月）｜保护溢价显著（Skew 10.7pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.79）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.68×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.79×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（1D）±3.6% ｜ 11-23（4D）±5.0% ｜ 11-25（6D）±6.4% ｜ 11-27（8D）±6.9%
   ⇒ IV–VIX Spread: +52.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -45,474,734 | GEX Change vs 上次快照 -120,585,829 | Flip: Primary Flip: 140.60（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 715 / LOW 221 / INVALID 464
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 140.60（全链重定价，覆盖 98%）
Put Wall 140（弱结构｜现价低于该位 1.1%）
最近结构参考: Put Wall 140（现价低于该位 1.1%）
量化视角： 负 Gamma（4547万，无历史分位）｜由正转负（1.21亿）｜现价位于 Flip 下方 1.54%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 140（Put Wall，弱结构） / 144（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 141（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C +18.5k / P -1.5k ｜ Activity MEDIUM △ ｜ 1D
11-23  C +2.3k / P +2.2k ｜ Activity HIGH ｜ 4D
11-25  C +1.9k / P +1.1k ｜ Activity HIGH ｜ 6D
11-27  C +2.7k / P +5.1k ｜ Activity HIGH ｜ 8D

📆 11-20 Forward Structure
存量OI: C 552.8k / P 437.9k，今日变化ΔOI: C +18.5k / P -1.5k，平值价格ATM: C $2.84 / P $2.19 ｜ ATM IV 81.3%，净 delta 敞口 284k shares
Top ΔOI: P 145 +5,839 ｜ P 165 -4,016 ｜ C 150 +3,807
仓位参考: Max Pain 144 ｜ Call Wall 150（+8.4%，弱）（OI 51.7k） ｜ Put Wall 135（-2.5%，弱）（OI 42.8k）
量化解读： 存量 Call 重｜ATM IV 81.3%｜历史 Rank 90%（近端代理）｜IV/RV 1.31×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 283,684 股

📆 11-23 Forward Structure
存量OI: C 13.1k / P 9.7k，今日变化ΔOI: C +2.3k / P +2.2k，平值价格ATM: C $3.85 / P $3.05 ｜ ATM IV 58.5%，净 delta 敞口 -80k shares
Top ΔOI: P 135 +392
仓位参考: Max Pain 142 ｜ Call Wall 150（+8.4%）（OI 2.7k） ｜ Put Wall 126（-9.0%，弱）（OI 1.8k）
量化解读： 存量 Call 重｜ATM IV 58.5%｜历史 Rank 90%（近端代理）｜IV/RV 0.94×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 80,033 股

📆 11-25 Forward Structure
存量OI: C 5.7k / P 4.0k，今日变化ΔOI: C +1.9k / P +1.1k，平值价格ATM: C $4.53 / P $4.30 ｜ ATM IV 63.2%，净 delta 敞口 -5k shares
Top ΔOI: C 143 +221
仓位参考: Max Pain 140 ｜ Call Wall 150（+8.4%，弱）（OI 0.9k） ｜ Put Wall 130（-6.1%）（OI 1.4k）
量化解读： 存量 Call 重｜ATM IV 63.2%｜历史 Rank 90%（近端代理）｜IV/RV 1.02×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 5,392 股

📆 11-27 Forward Structure
存量OI: C 130.5k / P 62.5k，今日变化ΔOI: C +2.7k / P +5.1k，平值价格ATM: C $5.30 / P $4.30 ｜ ATM IV 58.2%，净 delta 敞口 -156k shares
Top ΔOI: P 134 +508
仓位参考: Max Pain 142 ｜ Call Wall 150（+8.4%，弱）（OI 9.8k） ｜ Put Wall 135（-2.5%，弱）（OI 3.8k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 58.2%｜历史 Rank 90%（近端代理）｜IV/RV 0.94×（近似）｜净 delta 敞口 负 155,713 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-19/SPCX_evening.json