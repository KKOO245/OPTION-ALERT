# 期权晚报 2026-11-05（快照 16:40 ET）

📊 市场环境

SPY $733.00 ｜ QQQ $647.05
VIX 28.18 ↑69.7%（5D +63.8%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 19.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-05

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🔴 **Vol Regime 升档**: ELEVATED → STRESS（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **事件差分**: 11-06 ATM IV 36.0% vs 11-09 25.6%（差 +10.4pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-06 760P ΔOI +11,457（距现价 +3.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 765.47 → 收盘 733.00（-4.2%） ｜ 今日高 765.97 ｜ 低 732.71 ｜ 昨收 766.81 → 收盘 733.00（-4.4%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-10，窗口结束前不做对错判定）

Options: P/C成交量 1.38 | OI比 1.74 | ATM IV 39.6% | Skew -3.2pp | Term 0.55 | ExpMove ±1.5%（近端） | Rank 99%
量化视角： IV 历史高位（Rank 99%，期权偏贵）｜期限结构倒挂（Term 0.55，近月 IV 高于远月）｜Put 保护异常便宜（Skew -3.2pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 1.38）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.38×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.74×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 21% ｜ P/C OI(近端) 42%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 21%）｜近端持仓结构中性（P/C OI 分位 42%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-06（1D）±1.5% ｜ 11-09（4D）±2.2% ｜ 11-10（5D）±2.5% ｜ 11-11（6D）±2.8%
   ⇒ IV–VIX Spread: +11.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,677,681,405 | GEX Change vs 上次快照 11,822,850 | Flip: Primary Flip: 767.11（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 2934 / LOW 258 / INVALID 1944
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 767.11（全链重定价，覆盖 90%）
最近结构参考: Flip 767（现价低于该位 4.4%）
量化视角： 负 Gamma（16.78亿，历史分位偏负区，比 79% 的交易日更负）｜负 Gamma 缓解（+1182万）｜现价位于 Flip 下方 4.45%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 766（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 767（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-06  C +22.3k / P +44.9k ｜ Activity MEDIUM △ ｜ 1D
11-09  C +15.5k / P +40.4k ｜ Activity HIGH ｜ 4D
11-10  C +25.2k / P +38.3k ｜ Activity HIGH ｜ 5D
11-11  C +10.1k / P +29.1k ｜ Activity HIGH ｜ 6D

📆 11-06 Forward Structure
存量OI: C 260.5k / P 495.7k，今日变化ΔOI: C +22.3k / P +44.9k，平值价格ATM: C $5.40 / P $5.59 ｜ ATM IV 36.0%，净 delta 敞口 -4.0M shares
Top ΔOI: P 760 +11,457 ｜ P 767 +8,310 ｜ P 765 +6,220
仓位参考: Max Pain 765 ｜ Put Wall 750（+2.3%）（OI 38.6k）
量化解读： 存量 Put 重｜ATM IV 36.0%｜历史 Rank 99%（近端代理）｜IV/RV 2.89×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 3,994,695 股

📆 11-09 Forward Structure
存量OI: C 50.1k / P 97.2k，今日变化ΔOI: C +15.5k / P +40.4k，平值价格ATM: C $7.80 / P $8.04 ｜ ATM IV 25.6%，净 delta 敞口 -2.0M shares
Top ΔOI: P 680 +11,213 ｜ P 755 +6,070 ｜ P 660 +4,665
仓位参考: Max Pain 764 ｜ Put Wall 745（+1.6%，弱）（OI 5.6k）
量化解读： 存量 Put 重｜ATM IV 25.6%｜历史 Rank 99%（近端代理）｜IV/RV 2.05×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 1,950,483 股

📆 11-10 Forward Structure
存量OI: C 54.0k / P 65.4k，今日变化ΔOI: C +25.2k / P +38.3k，平值价格ATM: C $9.17 / P $9.20 ｜ ATM IV 26.8%，净 delta 敞口 -3.3M shares
Top ΔOI: P 764 +5,797 ｜ P 772 +5,637 ｜ P 758 +5,085
仓位参考: Max Pain 770 ｜ Put Wall 745（+1.6%，弱）（OI 2.0k）
量化解读： 存量 Put 重｜ATM IV 26.8%｜历史 Rank 99%（近端代理）｜IV/RV 2.15×（近似）｜净 delta 敞口 负 3,319,655 股

📆 11-11 Forward Structure
存量OI: C 25.4k / P 53.2k，今日变化ΔOI: C +10.1k / P +29.1k，平值价格ATM: C $10.12 / P $10.13 ｜ ATM IV 26.9%，净 delta 敞口 -1.4M shares
Top ΔOI: P 750 +3,093 ｜ P 720 +2,820 ｜ P 763 +2,214
仓位参考: Max Pain 767 ｜ Put Wall 720（-1.8%，弱）（OI 6.4k）
量化解读： 存量 Put 重｜ATM IV 26.9%｜历史 Rank 99%（近端代理）｜IV/RV 2.16×（近似）｜净 delta 敞口 负 1,420,601 股

📅 事件差分（观察，非因果）: 11-06（1D）ATM IV 36.0% vs 11-09 25.6%（差 +10.4pp）——覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=85 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=85）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-05/SPY_evening.json