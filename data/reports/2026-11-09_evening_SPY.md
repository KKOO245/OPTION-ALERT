# 期权晚报 2026-11-09（快照 21:00 ET）

📊 市场环境

SPY $752.69 ｜ QQQ $679.35
VIX 19.92 ↓22.3%（5D -5.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-09

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-10 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周二 11-10 08:30　【高】Core Inflation Rate YoY　预测 2.8 ｜ 实际 待公布 ｜ 前值 2.6
- 周二 11-10 08:30　【高】Inflation Rate MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.6
- 周二 11-10 08:30　【高】Inflation Rate YoY　预测 3.9 ｜ 实际 待公布 ｜ 前值 3.7
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 741.95 → 收盘 752.69（+1.4%） ｜ 今日高 755.42 ｜ 低 741.09 ｜ 昨收 735.29 → 收盘 752.69（+2.4%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-16，窗口结束前不做对错判定）

Options: P/C成交量 1.24 | OI比 0.69 | ATM IV 19.2% | Skew 4.0pp | Term 0.83 | ExpMove ±0.8%（近端） | Rank 82%
量化视角： IV 历史高位（Rank 82%，期权偏贵）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜保护溢价中性（Skew 4.0pp）｜⚠️ 重点观察：存量 Call 重（OI比 0.69）+ 当日成交偏 Put（P/C量 1.24）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.24×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.69×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 39% ｜ P/C OI(近端) 0%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 39%）｜近端持仓极端 Call 重（P/C OI 分位 0%，历史极低区）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-10（1D）±0.8% ｜ 11-11（2D）±1.1% ｜ 11-12（3D）±1.3% ｜ 11-13（4D）±1.5%
   ⇒ IV–VIX Spread: -0.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -741,283,309 | GEX Change vs 上次快照 175,291,254 | Flip: Primary Flip: 760.71（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 3245 / LOW 196 / INVALID 1445
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 760.71（全链重定价，覆盖 99%）
最近结构参考: Flip 761（现价低于该位 1.1%）
量化视角： 负 Gamma（7.41亿，历史分位 39%，中性区）｜负 Gamma 缓解（+1.75亿）｜现价位于 Flip 下方 1.05%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 740（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 761（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-10  C +0 / P +0 ｜ Activity LOW ｜ 1D
11-11  C +0 / P +0 ｜ Activity LOW ｜ 2D
11-12  C +0 / P +0 ｜ Activity LOW ｜ 3D
11-13  C +0 / P +0 ｜ Activity LOW ｜ 4D

📆 11-10 Forward Structure
存量OI: C 139.6k / P 96.3k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $3.14 / P $2.94 ｜ ATM IV 19.2%，净 delta 敞口 0 shares
仓位参考: Max Pain 740 ｜ Call Wall 740（-1.7%，弱）（OI 12.4k） ｜ Put Wall 734（-2.5%）（OI 10.0k）
量化解读： 存量 Call 重｜ATM IV 19.2%｜历史 Rank 82%（近端代理）｜IV/RV 0.88×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-11（Activity LOW）仓位参考: Max Pain 746 ｜ Call Wall 770（+2.3%）（OI 6.7k） ｜ Put Wall 750（-0.4%，弱）（OI 3.5k）

11-12（Activity LOW）仓位参考: Max Pain 748 ｜ Call Wall 775（+3.0%）（OI 6.7k） ｜ Put Wall 735（-2.4%，弱）（OI 2.5k）

11-13（Activity LOW）仓位参考: Max Pain 750 ｜ Call Wall 750（-0.4%，弱）（OI 11.2k） ｜ Put Wall 745（-1.0%，弱）（OI 28.8k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-09/SPY_evening.json