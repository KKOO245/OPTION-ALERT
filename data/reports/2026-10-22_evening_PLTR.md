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
🟡 **近现价集中开仓**: 10-23 195P ΔOI +2,011（距现价 -0.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 200.98 → 收盘 196.19（-2.4%） ｜ 今日高 202.63 ｜ 低 194.54 ｜ 昨收 201.72 → 收盘 196.19（-2.7%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-29，窗口结束前不做对错判定）

Options: P/C成交量 0.97 | OI比 1.01 | ATM IV 63.3% | Skew 5.4pp | Term 1.04 | ExpMove ±2.7%（近端） | Rank 95%
量化视角： IV 历史高位（Rank 95%，期权偏贵）｜期限结构正常（Term 1.04）｜保护溢价中性（Skew 5.4pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.97×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.01×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（1D）±2.7% ｜ 10-30（8D）±6.3% ｜ 11-06（15D）±13.0% ｜ 11-13（22D）±13.6%
   ⇒ IV–VIX Spread: +44.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 47,537,072 | GEX Change vs 上次快照 -29,225,577 | Flip: Primary Flip: 188.89（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 643 / LOW 91 / INVALID 182
结构观察区: Primary Flip 188.89（全链重定价，覆盖 100%）
Put Wall 190（弱结构｜现价高于该位 3.3%） | Call Wall 200（弱结构｜现价低于该位 1.9%）
最近结构参考: Call Wall 200（现价低于该位 1.9%）
量化视角： 正 Gamma（4754万，无历史分位）｜正 Gamma 减弱（2923万）｜现价位于 Flip 上方 3.87%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 190（Put Wall，弱结构） / 190（MaxPain，仅结算参考）；上方 200（Call Wall，弱结构）。
• Gamma 区域：切换参考 189（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +0.8k / P +9.5k ｜ Activity HIGH ｜ 1D
10-30  C +6.3k / P -0.4k ｜ Activity HIGH ｜ 8D
11-06  C +3.0k / P +2.1k ｜ Activity HIGH ｜ 15D
11-13  C +1.1k / P +0.9k ｜ Activity HIGH ｜ 22D

📆 10-23 Forward Structure
存量OI: C 132.5k / P 134.2k，今日变化ΔOI: C +0.8k / P +9.5k，平值价格ATM: C $3.30 / P $2.00 ｜ ATM IV 63.3%，净 delta 敞口 -183k shares
Top ΔOI: P 195 +2,011 ｜ P 177 -1,582 ｜ C 202 +1,403
仓位参考: Max Pain 190 ｜ Call Wall 205（+4.5%，弱）（OI 17.0k） ｜ Put Wall 190（-3.2%，弱）（OI 8.7k）
量化解读： 存量两侧均衡｜ATM IV 63.3%｜历史 Rank 95%（近端代理）｜IV/RV 1.44×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 183,032 股

📆 10-30 Forward Structure
存量OI: C 56.8k / P 80.0k，今日变化ΔOI: C +6.3k / P -0.4k，平值价格ATM: C $6.81 / P $5.55 ｜ ATM IV 52.6%，净 delta 敞口 -36k shares
Top ΔOI: P 162 -2,586 ｜ P 165 -2,116
仓位参考: Max Pain 190 ｜ Call Wall 210（+7.0%，弱）（OI 4.4k） ｜ Put Wall 190（-3.2%，弱）（OI 6.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 52.6%｜历史 Rank 95%（近端代理）｜IV/RV 1.20×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 35,549 股

📆 11-06 Forward Structure
存量OI: C 29.4k / P 29.7k，今日变化ΔOI: C +3.0k / P +2.1k，平值价格ATM: C $13.40 / P $12.10 ｜ ATM IV 79.4%，净 delta 敞口 45k shares
Top ΔOI: P 150 +628 ｜ C 215 +414
仓位参考: Max Pain 190 ｜ Call Wall 215（+9.6%，弱）（OI 2.1k） ｜ Put Wall 190（-3.2%，弱）（OI 3.0k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 79.4%｜历史 Rank 95%（近端代理）｜IV/RV 1.81×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 44,580 股

📆 11-13 Forward Structure
存量OI: C 11.6k / P 14.6k，今日变化ΔOI: C +1.1k / P +0.9k，平值价格ATM: C $13.50 / P $13.10 ｜ ATM IV 71.1%，净 delta 敞口 5k shares
Top ΔOI: C 192 +143
仓位参考: Max Pain 192 ｜ Call Wall 210（+7.0%，弱）（OI 1.2k） ｜ Put Wall 180（-8.3%，弱）（OI 1.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 71.1%｜历史 Rank 95%（近端代理）｜IV/RV 1.62×（近似）｜净 delta 敞口 正 4,910 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-22/PLTR_evening.json