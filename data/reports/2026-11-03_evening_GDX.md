# 期权晚报 2026-11-03（快照 16:41 ET）

📊 市场环境

SPY $754.35 ｜ QQQ $685.28
VIX 20.83 ↓1.5%（5D +18.9%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 19.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-03

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-03 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.1 ｜ 实际 7.523 ｜ 前值 7.19　✅ 今日已公布
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 待公布 ｜ 前值 54.9
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-04 77P ΔOI +5,353（距现价 -0.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-04 77P ΔOI +5,353 占该期限总 OI 33.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 78.94 → 收盘 77.60（-1.7%） ｜ 今日高 79.05 ｜ 低 77.30 ｜ 昨收 79.15 → 收盘 77.60（-2.0%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-10，窗口结束前不做对错判定）

Options: P/C成交量 1.87 | OI比 0.80 | ATM IV 57.0% | Skew 2.0pp | Term 0.74 | ExpMove ±2.5%（近端） | Rank 91%
量化视角： IV 历史高位（Rank 91%，期权偏贵）｜期限结构倒挂（Term 0.74，近月 IV 高于远月）｜保护溢价中性（Skew 2.0pp）｜⚠️ 重点观察：存量 Call 重（OI比 0.80）+ 当日成交偏 Put（P/C量 1.87）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.87×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.80×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-04（1D）±2.5% ｜ 11-06（3D）±4.0% ｜ 11-09（6D）±4.5% ｜ 11-11（8D）±4.5%
   ⇒ IV–VIX Spread: +36.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 10,914,213 | GEX Change vs 上次快照 -3,920,111 | Flip: Primary Flip: 76.83（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 505 / LOW 111 / INVALID 538
结构观察区: Primary Flip 76.83（全链重定价，覆盖 99%）
Call Wall 81（弱结构｜现价低于该位 4.2%）
最近结构参考: Flip 77（现价高于该位 1.0%）
量化视角： 正 Gamma（1091万，无历史分位）｜正 Gamma 减弱（392万）｜现价位于 Flip 上方 1.00%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 78（MaxPain，仅结算参考） / 81（Call Wall，弱结构）。
• Gamma 区域：切换参考 77（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-04  C +3.4k / P +6.2k ｜ Activity HIGH ｜ 1D
11-06  C +3.6k / P +1.3k ｜ Activity HIGH ｜ 3D
11-09  C +0.4k / P +0.2k ｜ Activity HIGH ｜ 6D
11-11  C +1.9k / P -12 ｜ Activity HIGH ｜ 8D

📆 11-04 Forward Structure
存量OI: C 9.0k / P 7.2k，今日变化ΔOI: C +3.4k / P +6.2k，平值价格ATM: C $0.83 / P $1.15 ｜ ATM IV 57.0%，净 delta 敞口 -245k shares
Top ΔOI: P 77 +5,353 ｜ C 84 +2,456 ｜ P 78 +518
仓位参考: Max Pain 78 ｜ Call Wall 81（+4.4%，弱）（OI 2.7k） ｜ Put Wall 77（-0.8%）（OI 5.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 57.0%｜历史 Rank 91%（近端代理）｜IV/RV 1.36×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 245,001 股

📆 11-06 Forward Structure
存量OI: C 93.7k / P 30.3k，今日变化ΔOI: C +3.6k / P +1.3k，平值价格ATM: C $1.58 / P $1.51 ｜ ATM IV 53.6%，净 delta 敞口 -1k shares
Top ΔOI: C 80 +1,209 ｜ P 78 +1,077 ｜ C 81 +787
仓位参考: Max Pain 78 ｜ Call Wall 81（+4.4%，弱）（OI 22.8k） ｜ Put Wall 75（-3.4%，弱）（OI 4.3k）
量化解读： 存量 Call 重｜ATM IV 53.6%｜历史 Rank 91%（近端代理）｜IV/RV 1.28×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,257 股

📆 11-09 Forward Structure
存量OI: C 0.8k / P 0.5k，今日变化ΔOI: C +0.4k / P +0.2k，平值价格ATM: C $1.57 / P $1.93 ｜ ATM IV 43.8%，净 delta 敞口 -7k shares
Top ΔOI: C 84 +141 ｜ C 85 +123 ｜ P 79 +55
仓位参考: Max Pain 78 ｜ Call Wall 78（+0.5%，弱）（OI 0.1k） ｜ Put Wall 73（-5.9%，弱）（OI 0.1k）
量化解读： 存量 Call 重｜ATM IV 43.8%｜历史 Rank 91%（近端代理）｜IV/RV 1.05×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 7,138 股

📆 11-11 Forward Structure
存量OI: C 2.5k / P 1.3k，今日变化ΔOI: C +1.9k / P -12，平值价格ATM: C $2.43 / P $1.03 ｜ ATM IV 46.5%，净 delta 敞口 24k shares
Top ΔOI: C 85 +1,868 ｜ C 77 +26 ｜ P 82 -19
仓位参考: Max Pain 78 ｜ Put Wall 77（-0.8%）（OI 1.0k）
量化解读： 存量 Call 重｜ATM IV 46.5%｜历史 Rank 91%（近端代理）｜IV/RV 1.11×（近似）｜净 delta 敞口 正 24,261 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-03/GDX_evening.json