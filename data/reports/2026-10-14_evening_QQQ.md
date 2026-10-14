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
🟡 **近现价集中开仓**: 10-15 750C ΔOI +4,241（距现价 +2.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 738.00 → 收盘 728.95（-1.2%） ｜ 今日高 740.53 ｜ 低 726.43 ｜ 昨收 743.57 → 收盘 728.95（-2.0%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-19，窗口结束前不做对错判定）

Options: P/C成交量 0.80 | OI比 2.12 | ATM IV 46.5% | Skew 2.7pp | Term 0.43 | ExpMove ±1.1%（近端） | Rank 99%
量化视角： IV 历史高位（Rank 99%，期权偏贵）｜期限结构倒挂（Term 0.43，近月 IV 高于远月）｜保护溢价中性（Skew 2.7pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.80×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 2.12×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 6% ｜ P/C OI(近端) 82%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 6%）｜近端持仓结构中性（P/C OI 分位 82%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-15（1D）±1.1% ｜ 10-16（2D）±1.4% ｜ 10-19（5D）±1.6% ｜ 10-20（6D）±1.9%
   ⇒ IV–VIX Spread: +29.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,023,474,891 | GEX Change vs 上次快照 -260,374,795 | Flip: Primary Flip: 744.63（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 2922 / LOW 384 / INVALID 1680
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 744.63（全链重定价，覆盖 97%）
最近结构参考: Flip 745（现价低于该位 2.1%）
量化视角： 负 Gamma（10.23亿，历史分位偏负区，比 94% 的交易日更负）｜负 Gamma 加深（2.60亿）｜现价位于 Flip 下方 2.11%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 745（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 745（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-15  C +23.0k / P +21.6k ｜ Activity HIGH ｜ 1D
10-16  C +13.7k / P +48.0k ｜ Activity MEDIUM △ ｜ 2D
10-19  C +9.7k / P +25.4k ｜ Activity HIGH ｜ 5D
10-20  C +7.9k / P +10.5k ｜ Activity HIGH ｜ 6D

📆 10-15 Forward Structure
存量OI: C 60.6k / P 97.4k，今日变化ΔOI: C +23.0k / P +21.6k，平值价格ATM: C $3.34 / P $4.36 ｜ ATM IV 25.1%，净 delta 敞口 -1.3M shares
Top ΔOI: C 750 +4,241 ｜ C 743 +3,343 ｜ P 730 +2,743
仓位参考: Max Pain 744 ｜ Call Wall 750（+2.9%，弱）（OI 5.8k） ｜ Put Wall 730（+0.1%，弱）（OI 4.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 25.1%｜历史 Rank 99%（近端代理）｜IV/RV 2.50×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,276,473 股

10-16（MEDIUM △）Top ΔOI: 707P +11,583 ｜ 724P +5,639
10-16（MEDIUM △）仓位参考: Max Pain 735 ｜ Call Wall 750（+2.9%，弱）（OI 37.2k） ｜ Put Wall 740（+1.5%，弱）（OI 30.9k）

📆 10-19 Forward Structure
存量OI: C 36.4k / P 74.5k，今日变化ΔOI: C +9.7k / P +25.4k，平值价格ATM: C $5.80 / P $5.86 ｜ ATM IV 17.8%，净 delta 敞口 -659k shares
Top ΔOI: P 740 +4,683 ｜ P 710 +2,800
仓位参考: Max Pain 750 ｜ Call Wall 750（+2.9%，弱）（OI 1.8k） ｜ Put Wall 740（+1.5%，弱）（OI 5.8k）
量化解读： 存量 Put 重｜ATM IV 17.8%｜历史 Rank 99%（近端代理）｜IV/RV 1.77×（近似）｜净 delta 敞口 负 659,304 股

📆 10-20 Forward Structure
存量OI: C 27.1k / P 37.3k，今日变化ΔOI: C +7.9k / P +10.5k，平值价格ATM: C $6.94 / P $7.14 ｜ ATM IV 18.4%，净 delta 敞口 -221k shares
Top ΔOI: C 749 +3,044 ｜ P 721 +582
仓位参考: Max Pain 747 ｜ Call Wall 749（+2.8%）（OI 9.1k） ｜ Put Wall 726（-0.4%，弱）（OI 2.4k）
量化解读： 存量 Put 重｜ATM IV 18.4%｜历史 Rank 99%（近端代理）｜IV/RV 1.83×（近似）｜净 delta 敞口 负 220,802 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-14/QQQ_evening.json