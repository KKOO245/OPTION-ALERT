# 期权晚报 2026-11-10（快照 16:40 ET）

📊 市场环境

SPY $749.92 ｜ QQQ $674.76
VIX 19.46 ↓2.3%（5D -6.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-10

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-10 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周二 11-10 08:30　【高】Inflation Rate MoM　预测 0.3 ｜ 实际 0.4 ｜ 前值 0.6　✅ 今日已公布
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🔵 **期限 OI 集中**: 11-11 96C ΔOI +2,704 占该期限总 OI 20.5%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 88.02 → 收盘 86.49（-1.7%） ｜ 今日高 88.99 ｜ 低 85.96 ｜ 昨收 91.46 → 收盘 86.49（-5.4%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-17，窗口结束前不做对错判定）

Options: P/C成交量 1.47 | OI比 0.37 | ATM IV 51.7% | Skew -2.7pp | Term 0.87 | ExpMove ±2.6%（近端） | Rank 84%
量化视角： IV 历史高位（Rank 84%，期权偏贵）｜期限结构倒挂（Term 0.87，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.7pp，Put IV < Call IV）｜⚠️ 重点观察：存量 Call 重（OI比 0.37）+ 当日成交偏 Put（P/C量 1.47）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.47×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.37×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-11（1D）±2.6% ｜ 11-13（3D）±4.1% ｜ 11-16（6D）±4.7% ｜ 11-18（8D）±8.7%
   ⇒ IV–VIX Spread: +32.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 40,323,639 | GEX Change vs 上次快照 -21,807,532 | Flip: Primary Flip: 84.05（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 683 / LOW 182 / INVALID 447
结构观察区: Primary Flip 84.05（全链重定价，覆盖 99%）
最近结构参考: Flip 84（现价高于该位 2.9%）
量化视角： 正 Gamma（4032万，无历史分位）｜正 Gamma 减弱（2181万）｜现价位于 Flip 上方 2.90%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 85（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 84（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-11  C +4.3k / P +1.9k ｜ Activity HIGH ｜ 1D
11-13  C +1.1k / P +1.4k ｜ Activity HIGH ｜ 3D
11-16  C +1.1k / P +0.1k ｜ Activity HIGH ｜ 6D
11-18  C +0.2k / P +22 ｜ Activity MEDIUM △ ｜ 8D

📆 11-11 Forward Structure
存量OI: C 9.6k / P 3.6k，今日变化ΔOI: C +4.3k / P +1.9k，平值价格ATM: C $1.61 / P $0.65 ｜ ATM IV 51.7%，净 delta 敞口 -121k shares
Top ΔOI: C 93 +433 ｜ P 89 +425
仓位参考: Max Pain 85 ｜ Call Wall 85（-1.7%，弱）（OI 2.2k） ｜ Put Wall 89（+2.9%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 51.7%｜历史 Rank 84%（近端代理）｜IV/RV 1.00×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 121,058 股

📆 11-13 Forward Structure
存量OI: C 81.9k / P 34.8k，今日变化ΔOI: C +1.1k / P +1.4k，平值价格ATM: C $2.00 / P $1.57 ｜ ATM IV 50.6%，净 delta 敞口 -98k shares
Top ΔOI: C 95 +654 ｜ P 87 +355 ｜ P 89 +297
仓位参考: Max Pain 84 ｜ Call Wall 88（+1.7%，弱）（OI 13.3k） ｜ Put Wall 82（-5.2%，弱）（OI 4.9k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 50.6%｜历史 Rank 84%（近端代理）｜IV/RV 0.98×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 97,949 股

📆 11-16 Forward Structure
存量OI: C 1.8k / P 0.7k，今日变化ΔOI: C +1.1k / P +0.1k，平值价格ATM: C $2.50 / P $1.53 ｜ ATM IV 42.0%，净 delta 敞口 4k shares
Top ΔOI: C 94 +839 ｜ C 91 +40
仓位参考: Max Pain 85 ｜ Call Wall 88（+1.7%，弱）（OI 0.2k） ｜ Put Wall 81（-6.3%，弱）（OI 0.1k）
量化解读： 存量 Call 重｜ATM IV 42.0%｜历史 Rank 84%（近端代理）｜IV/RV 0.82×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 4,316 股

11-18（MEDIUM △）Top ΔOI: 92C +50 ｜ 95C +32
11-18（MEDIUM △）仓位参考: Max Pain 85 ｜ Call Wall 87（+0.6%）（OI 97） ｜ Put Wall 84（-2.9%）（OI 0.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-10/GDX_evening.json