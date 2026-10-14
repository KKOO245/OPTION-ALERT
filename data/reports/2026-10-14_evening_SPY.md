# 期权晚报 2026-10-14（快照 16:42 ET）

📊 市场环境

SPY $769.60 ｜ QQQ $728.95
VIX 16.87 ↑10.5%（5D +11.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 32.4（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-14

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 2.6 ｜ 前值 2.4　✅ 今日已公布
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.6 ｜ 实际 3.7 ｜ 前值 3.4　✅ 今日已公布
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 0.6 ｜ 前值 0.4　✅ 今日已公布
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-15 795C ΔOI +15,813（距现价 +3.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 774.92 → 收盘 769.60（-0.7%） ｜ 今日高 776.30 ｜ 低 766.71 ｜ 昨收 778.01 → 收盘 769.60（-1.1%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-19，窗口结束前不做对错判定）

Options: P/C成交量 1.07 | OI比 1.82 | ATM IV 34.9% | Skew -3.2pp | Term 0.38 | ExpMove ±0.6%（近端） | Rank 98%
量化视角： IV 历史高位（Rank 98%，期权偏贵）｜期限结构倒挂（Term 0.38，近月 IV 高于远月）｜Put 保护异常便宜（Skew -3.2pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.07×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.82×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 23% ｜ P/C OI(近端) 49%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 23%）｜近端持仓结构中性（P/C OI 分位 49%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-15（1D）±0.6% ｜ 10-16（2D）±0.8% ｜ 10-19（5D）±1.0% ｜ 10-20（6D）±1.1%
   ⇒ IV–VIX Spread: +18.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,529,433,361 | GEX Change vs 上次快照 -568,033,083 | Flip: Primary Flip: 777.51（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 2857 / LOW 284 / INVALID 1731
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 777.51（全链重定价，覆盖 95%）
最近结构参考: Flip 778（现价低于该位 1.0%）
量化视角： 负 Gamma（15.29亿，历史分位偏负区，比 77% 的交易日更负）｜负 Gamma 加深（5.68亿）｜现价位于 Flip 下方 1.02%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 777（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 778（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-15  C +32.3k / P +28.8k ｜ Activity HIGH ｜ 1D
10-16  C +16.6k / P +56.0k ｜ Activity MEDIUM △ ｜ 2D
10-19  C +6.2k / P +13.3k ｜ Activity HIGH ｜ 5D
10-20  C +6.7k / P +9.7k ｜ Activity HIGH ｜ 6D

📆 10-15 Forward Structure
存量OI: C 70.2k / P 191.1k，今日变化ΔOI: C +32.3k / P +28.8k，平值价格ATM: C $1.98 / P $2.86 ｜ ATM IV 14.8%，净 delta 敞口 -877k shares
Top ΔOI: C 795 +15,813 ｜ P 766 +3,779 ｜ P 759 +2,799
仓位参考: Max Pain 777 ｜ Call Wall 780（+1.4%，弱）（OI 3.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 14.8%｜历史 Rank 98%（近端代理）｜IV/RV 2.21×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 877,166 股

10-16（MEDIUM △）Top ΔOI: 773P +20,790 ｜ 782C +7,204
10-16（MEDIUM △）仓位参考: Max Pain 772 ｜ Call Wall 785（+2.0%）（OI 59.3k） ｜ Put Wall 750（-2.5%，弱）（OI 66.8k）

📆 10-19 Forward Structure
存量OI: C 41.3k / P 80.4k，今日变化ΔOI: C +6.2k / P +13.3k，平值价格ATM: C $3.68 / P $4.07 ｜ ATM IV 10.8%，净 delta 敞口 -400k shares
Top ΔOI: P 750 +4,517 ｜ P 777 +1,610 ｜ C 777 +1,602
仓位参考: Max Pain 777 ｜ Call Wall 790（+2.7%，弱）（OI 4.5k） ｜ Put Wall 747（-2.9%）（OI 15.0k）
量化解读： 存量 Put 重｜ATM IV 10.8%｜历史 Rank 98%（近端代理）｜IV/RV 1.61×（近似）｜净 delta 敞口 负 400,460 股

📆 10-20 Forward Structure
存量OI: C 18.3k / P 28.0k，今日变化ΔOI: C +6.7k / P +9.7k，平值价格ATM: C $4.25 / P $4.49 ｜ ATM IV 11.1%，净 delta 敞口 -193k shares
Top ΔOI: C 778 +1,117 ｜ P 735 +962 ｜ P 757 +886
仓位参考: Max Pain 777 ｜ Call Wall 778（+1.1%，弱）（OI 1.5k） ｜ Put Wall 759（-1.4%，弱）（OI 1.4k）
量化解读： 存量 Put 重｜ATM IV 11.1%｜历史 Rank 98%（近端代理）｜IV/RV 1.65×（近似）｜净 delta 敞口 负 193,449 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-14/SPY_evening.json