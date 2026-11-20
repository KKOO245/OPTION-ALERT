# 期权晚报 2026-11-19（快照 16:40 ET）

📊 市场环境

SPY $715.87 ｜ QQQ $nan
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
🟡 **近现价集中开仓**: 11-20 625P ΔOI +13,786（距现价 -3.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 671.05 → 收盘 645.04（-3.9%） ｜ 今日高 676.46 ｜ 低 644.34 ｜ 昨收 659.51 → 收盘 645.04（-2.2%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-24，窗口结束前不做对错判定）

Options: P/C成交量 1.00 | OI比 1.01 | ATM IV 59.4% | Skew -3.2pp | Term 0.55 | ExpMove ±2.1%（近端） | Rank 99%
量化视角： IV 历史高位（Rank 99%，期权偏贵）｜期限结构倒挂（Term 0.55，近月 IV 高于远月）｜Put 保护异常便宜（Skew -3.2pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.00×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.01×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 16% ｜ P/C OI(近端) 6%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 16%）｜近端持仓极端 Call 重（P/C OI 分位 6%，历史极低区）｜⚠️ 需重点观察：持仓极端 + Gamma 异常侧组合——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-20（1D）±2.1% ｜ 11-23（4D）±3.1% ｜ 11-24（5D）±3.7% ｜ 11-25（6D）±4.0%
   ⇒ IV–VIX Spread: +31.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -605,768,077 | GEX Change vs 上次快照 -645,131,130 | Flip: Primary Flip: 666.87（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 3251 / LOW 480 / INVALID 1451
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 666.87（全链重定价，覆盖 95%）
最近结构参考: Flip 667（现价低于该位 3.3%）
量化视角： 负 Gamma（6.06亿，历史分位偏负区，比 84% 的交易日更负）｜由正转负（6.45亿）｜现价位于 Flip 下方 3.27%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 661（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 667（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C +33.4k / P -15.9k ｜ Activity MEDIUM △ ｜ 1D
11-23  C +9.3k / P +5.8k ｜ Activity HIGH ｜ 4D
11-24  C +4.2k / P +16.2k ｜ Activity HIGH ｜ 5D
11-25  C +18.8k / P +8.7k ｜ Activity HIGH ｜ 6D

📆 11-20 Forward Structure
存量OI: C 1248.1k / P 1088.0k，今日变化ΔOI: C +33.4k / P -15.9k，平值价格ATM: C $7.04 / P $6.65 ｜ ATM IV 50.5%，净 delta 敞口 4.3M shares
Top ΔOI: C 678 +14,930 ｜ P 625 +13,786 ｜ P 680 -10,925
仓位参考: Max Pain 680 ｜ Call Wall 660（+2.3%，弱）（OI 12.1k） ｜ Put Wall 640（-0.8%，弱）（OI 48.4k）
量化解读： 存量两侧均衡｜ATM IV 50.5%｜历史 Rank 99%（近端代理）｜IV/RV 1.45×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 4,313,981 股

📆 11-23 Forward Structure
存量OI: C 52.8k / P 42.6k，今日变化ΔOI: C +9.3k / P +5.8k，平值价格ATM: C $10.36 / P $9.80 ｜ ATM IV 37.1%，净 delta 敞口 -123k shares
Top ΔOI: P 630 +1,363 ｜ C 690 +1,280 ｜ C 687 +1,253
仓位参考: Max Pain 665 ｜ Put Wall 645（-0.0%）（OI 5.8k）
量化解读： 存量 Call 重｜ATM IV 37.1%｜历史 Rank 99%（近端代理）｜IV/RV 1.07×（近似）｜净 delta 敞口 负 123,100 股

📆 11-24 Forward Structure
存量OI: C 32.9k / P 44.6k，今日变化ΔOI: C +4.2k / P +16.2k，平值价格ATM: C $12.10 / P $11.80 ｜ ATM IV 38.6%，净 delta 敞口 -125k shares
Top ΔOI: P 570 +6,343 ｜ P 555 +5,681 ｜ C 689 +1,125
仓位参考: Max Pain 666 ｜ Put Wall 660（+2.3%，弱）（OI 4.9k）
量化解读： 存量 Put 重｜ATM IV 38.6%｜历史 Rank 99%（近端代理）｜IV/RV 1.11×（近似）｜净 delta 敞口 负 125,169 股

📆 11-25 Forward Structure
存量OI: C 41.7k / P 23.7k，今日变化ΔOI: C +18.8k / P +8.7k，平值价格ATM: C $13.35 / P $12.72 ｜ ATM IV 39.0%，净 delta 敞口 -151k shares
Top ΔOI: P 655 +1,892 ｜ C 690 +1,826
仓位参考: Max Pain 666 ｜ Put Wall 655（+1.5%，弱）（OI 2.2k）
量化解读： 存量 Call 重｜ATM IV 39.0%｜历史 Rank 99%（近端代理）｜IV/RV 1.12×（近似）｜净 delta 敞口 负 150,992 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-19/QQQ_evening.json