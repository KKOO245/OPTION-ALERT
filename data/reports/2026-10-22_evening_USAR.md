# 期权晚报 2026-10-22（快照 16:40 ET）

📊 市场环境

SPY $763.96 ｜ QQQ $704.47
VIX 19.03 ↑14.1%（5D +15.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 19.8（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-23 10C ΔOI +1,617（距现价 +3.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 9.75 → 收盘 9.63（-1.2%） ｜ 今日高 10.06 ｜ 低 9.41 ｜ 昨收 10.23 → 收盘 9.63（-5.9%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-27，窗口结束前不做对错判定）

Options: P/C成交量 0.32 | OI比 0.24 | ATM IV 85.3% | Skew -7.4pp | Term 1.04 | ExpMove ±4.7%（近端） | Rank 17%
量化视角： IV 历史低位（Rank 17%，期权偏便宜）｜期限结构正常（Term 1.04）｜Put 保护异常便宜（Skew -7.4pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.24）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.32×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.24×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（1D）±4.7% ｜ 10-30（8D）±9.2% ｜ 11-06（15D）±14.0% ｜ 11-13（22D）±17.3%
   ⇒ IV–VIX Spread: +66.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -872,350 | GEX Change vs 上次快照 -1,713,658 | Flip: Primary Flip: 9.76（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 212 / LOW 81 / INVALID 143
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 9.76（全链重定价，覆盖 95%）
Put Wall 10（弱结构｜现价低于该位 3.7%）
最近结构参考: Flip 10（现价低于该位 1.3%）
量化视角： 负 Gamma（87万，无历史分位）｜由正转负（171万）｜现价位于 Flip 下方 1.34%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 10（Put Wall，弱结构） / 10（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 10（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +2.6k / P +0.8k ｜ Activity HIGH ｜ 1D
10-30  C +0.4k / P +0.1k ｜ Activity MEDIUM △ ｜ 8D
11-06  C +0.6k / P -56 ｜ Activity HIGH ｜ 15D
11-13  C +0.2k / P -3 ｜ Activity HIGH ｜ 22D

📆 10-23 Forward Structure
存量OI: C 26.3k / P 6.4k，今日变化ΔOI: C +2.6k / P +0.8k，平值价格ATM: C $0.27 / P $0.18 ｜ ATM IV 85.3%，净 delta 敞口 -20k shares
Top ΔOI: C 10 +1,617 ｜ P 10 +1,032
仓位参考: Max Pain 10 ｜ Call Wall 10.5（+9.0%，弱）（OI 2.5k） ｜ Put Wall 10（+3.8%，弱）（OI 1.8k）
量化解读： 存量 Call 重｜ATM IV 85.3%｜历史 Rank 17%（近端代理）｜IV/RV 1.55×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 20,163 股

10-30（MEDIUM △）Top ΔOI: 9P +87
10-30（MEDIUM △）仓位参考: Max Pain 12 ｜ Call Wall 10（+3.8%，弱）（OI 0.8k） ｜ Put Wall 9（-6.5%，弱）（OI 0.7k）

📆 11-06 Forward Structure
存量OI: C 4.9k / P 4.4k，今日变化ΔOI: C +0.6k / P -56，平值价格ATM: C $0.72 / P $0.63 ｜ ATM IV 85.5%，净 delta 敞口 11k shares
仓位参考: Max Pain 12 ｜ Put Wall 9（-6.5%）（OI 1.5k）
量化解读： 存量两侧均衡｜ATM IV 85.5%｜历史 Rank 17%（近端代理）｜IV/RV 1.56×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 11,421 股

📆 11-13 Forward Structure
存量OI: C 2.5k / P 3.4k，今日变化ΔOI: C +0.2k / P -3，平值价格ATM: C $0.87 / P $0.80 ｜ ATM IV 84.3%，净 delta 敞口 5k shares
仓位参考: Max Pain 14 ｜ Call Wall 10.5（+9.0%，弱）（OI 0.3k） ｜ Put Wall 10.5（+9.0%，弱）（OI 0.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 84.3%｜历史 Rank 17%（近端代理）｜IV/RV 1.53×（近似）｜净 delta 敞口 正 4,893 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=61 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=61）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-22/USAR_evening.json