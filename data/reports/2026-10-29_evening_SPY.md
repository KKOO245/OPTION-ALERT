# 期权晚报 2026-10-29（快照 16:40 ET）

📊 市场环境

SPY $769.36 ｜ QQQ $715.34
VIX 17.20 ↑1.7%（5D -9.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-29

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 3.4 ｜ 前值 2.2　✅ 今日已公布
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 0.5 ｜ 前值 0.9　✅ 今日已公布
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-30 765P ΔOI +13,462（距现价 -0.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-03 660P ΔOI +11,337 占该期限总 OI 15.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 768.79 → 收盘 769.36（+0.1%） ｜ 今日高 770.76 ｜ 低 766.62 ｜ 昨收 772.31 → 收盘 769.36（-0.4%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-05，窗口结束前不做对错判定）

Options: P/C成交量 1.01 | OI比 1.64 | ATM IV 29.1% | Skew -0.6pp | Term 0.46 | ExpMove ±0.7%（近端） | Rank 97%
量化视角： IV 历史高位（Rank 97%，期权偏贵）｜期限结构倒挂（Term 0.46，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.6pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.01×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.64×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 40% ｜ P/C OI(近端) 34%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 40%）｜近端持仓结构中性（P/C OI 分位 34%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-30（1D）±0.7% ｜ 11-02（4D）±0.9% ｜ 11-03（5D）±1.1% ｜ 11-04（6D）±1.3%
   ⇒ IV–VIX Spread: +11.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -703,938,924 | GEX Change vs 上次快照 84,553,141 | Flip: Primary Flip: 773.43（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 89%（带内） ｜ IV 有效性: VALID 2682 / LOW 483 / INVALID 1151
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 773.43（全链重定价，覆盖 89%）
最近结构参考: Flip 773（现价低于该位 0.5%）
量化视角： 负 Gamma（7.04亿，历史分位 40%，中性区）｜负 Gamma 缓解（+8455万）｜现价位于 Flip 下方 0.53%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 770（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 773（全链重定价，覆盖 89%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-30  C +6.3k / P +29.6k ｜ Activity MEDIUM △ ｜ 1D
11-02  C +8.2k / P +25.0k ｜ Activity HIGH ｜ 4D
11-03  C +9.3k / P +18.5k ｜ Activity HIGH ｜ 5D
11-04  C +5.6k / P +29.6k ｜ Activity HIGH ｜ 6D

📆 10-30 Forward Structure
存量OI: C 674.7k / P 1666.2k，今日变化ΔOI: C +6.3k / P +29.6k，平值价格ATM: C $1.14 / P $4.22 ｜ ATM IV 14.5%，净 delta 敞口 -1.4M shares
Top ΔOI: P 765 +13,462 ｜ P 748 -5,984 ｜ C 764 +4,036
仓位参考: Max Pain 765 ｜ Call Wall 780（+1.4%，弱）（OI 27.9k） ｜ Put Wall 750（-2.5%，弱）（OI 67.1k）
量化解读： 存量 Put 重｜ATM IV 14.5%｜历史 Rank 97%（近端代理）｜IV/RV 1.58×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,419,487 股

📆 11-02 Forward Structure
存量OI: C 38.5k / P 76.6k，今日变化ΔOI: C +8.2k / P +25.0k，平值价格ATM: C $2.09 / P $5.05 ｜ ATM IV 10.4%，净 delta 敞口 -749k shares
Top ΔOI: P 775 +5,790 ｜ P 760 +3,071 ｜ P 705 +1,702
仓位参考: Max Pain 770 ｜ Call Wall 770（+0.1%，弱）（OI 2.1k） ｜ Put Wall 750（-2.5%，弱）（OI 8.9k）
量化解读： 存量 Put 重｜ATM IV 10.4%｜历史 Rank 97%（近端代理）｜IV/RV 1.14×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 749,219 股

📆 11-03 Forward Structure
存量OI: C 26.4k / P 49.0k，今日变化ΔOI: C +9.3k / P +18.5k，平值价格ATM: C $2.68 / P $5.78 ｜ ATM IV 11.1%，净 delta 敞口 -171k shares
Top ΔOI: C 780 +2,524 ｜ P 759 +2,441
仓位参考: Max Pain 770 ｜ Call Wall 780（+1.4%，弱）（OI 3.3k） ｜ Put Wall 755（-1.9%，弱）（OI 2.9k）
量化解读： 存量 Put 重｜ATM IV 11.1%｜历史 Rank 97%（近端代理）｜IV/RV 1.21×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 171,484 股

📆 11-04 Forward Structure
存量OI: C 16.7k / P 66.7k，今日变化ΔOI: C +5.6k / P +29.6k，平值价格ATM: C $3.69 / P $6.37 ｜ ATM IV 12.4%，净 delta 敞口 -1.2M shares
Top ΔOI: P 767 +18,239 ｜ P 758 +3,548 ｜ P 760 +822
仓位参考: Max Pain 769 ｜ Call Wall 771（+0.2%，弱）（OI 1.3k） ｜ Put Wall 767（-0.3%）（OI 29.8k）
量化解读： 存量 Put 重｜ATM IV 12.4%｜历史 Rank 97%（近端代理）｜IV/RV 1.35×（近似）｜净 delta 敞口 负 1,199,058 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-29/SPY_evening.json