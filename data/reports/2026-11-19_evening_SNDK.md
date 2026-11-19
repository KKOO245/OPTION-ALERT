# 期权晚报 2026-11-19（快照 16:40 ET）

📊 市场环境

SPY $715.87 ｜ QQQ $645.04
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


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 811.47 → 收盘 755.16（-6.9%） ｜ 今日高 846.76 ｜ 低 753.34 ｜ 昨收 776.22 → 收盘 755.16（-2.7%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-24，窗口结束前不做对错判定）

Options: P/C成交量 1.16 | OI比 0.58 | ATM IV 136.9% | Skew 15.5pp | Term 0.74 | ExpMove ±5.8%（近端） | Rank 87%
量化视角： IV 历史高位（Rank 87%，期权偏贵）｜期限结构倒挂（Term 0.74，近月 IV 高于远月）｜保护溢价显著（Skew 15.5pp，Put 明显贵于 Call）｜⚠️ 重点观察：存量 Call 重（OI比 0.58）+ 当日成交偏 Put（P/C量 1.16）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.16×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.58×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（1D）±5.8% ｜ 11-27（8D）±12.1% ｜ 12-04（15D）±17.8% ｜ 12-11（22D）±11.2%
   ⇒ IV–VIX Spread: +108.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -5,298,803 | GEX Change vs 上次快照 -5,215,285 | Flip: Primary Flip: 800.84（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1513 / LOW 741 / INVALID 1278
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 800.84（全链重定价，覆盖 100%）
最近结构参考: Flip 801（现价低于该位 5.7%）
量化视角： 负 Gamma（530万，无历史分位）｜负 Gamma 加深（522万）｜现价位于 Flip 下方 5.70%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 870（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 801（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C +2.6k / P -1.0k ｜ Activity MEDIUM △ ｜ 1D
11-27  C +4.3k / P +0.4k ｜ Activity HIGH ｜ 8D
12-04  C +1.6k / P +0.1k ｜ Activity HIGH ｜ 15D
12-11  C +0.5k / P +0.4k ｜ Activity HIGH ｜ 22D

📆 11-20 Forward Structure
存量OI: C 102.8k / P 59.9k，今日变化ΔOI: C +2.6k / P -1.0k，平值价格ATM: C $21.92 / P $22.25 ｜ ATM IV 136.8%，净 delta 敞口 536k shares
Top ΔOI: C 800 +1,082 ｜ P 1100 -820
仓位参考: Max Pain 870 ｜ Call Wall 800（+5.9%，弱）（OI 2.9k） ｜ Put Wall 700（-7.3%，弱）（OI 1.9k）
量化解读： 存量 Call 重｜ATM IV 136.8%｜历史 Rank 87%（近端代理）｜IV/RV 1.03×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 536,342 股

📆 11-27 Forward Structure
存量OI: C 27.9k / P 13.7k，今日变化ΔOI: C +4.3k / P +0.4k，平值价格ATM: C $47.20 / P $43.96 ｜ ATM IV 107.0%，净 delta 敞口 183k shares
Top ΔOI: C 800 +1,883 ｜ C 825 +303 ｜ P 850 +239
仓位参考: Max Pain 850 ｜ Call Wall 800（+5.9%，弱）（OI 2.1k） ｜ Put Wall 800（+5.9%，弱）（OI 1.1k）
量化解读： 存量 Call 重｜ATM IV 107.0%｜历史 Rank 87%（近端代理）｜IV/RV 0.81×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 182,877 股

📆 12-04 Forward Structure
存量OI: C 13.2k / P 7.1k，今日变化ΔOI: C +1.6k / P +0.1k，平值价格ATM: C $74.23 / P $60.50 ｜ ATM IV 105.3%，净 delta 敞口 47k shares
Top ΔOI: C 800 +232
仓位参考: Max Pain 880 ｜ Call Wall 800（+5.9%，弱）（OI 0.3k） ｜ Put Wall 820（+8.6%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 105.3%｜历史 Rank 87%（近端代理）｜IV/RV 0.79×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 46,558 股

📆 12-11 Forward Structure
存量OI: C 6.5k / P 4.0k，今日变化ΔOI: C +0.5k / P +0.4k，平值价格ATM: C $84.90 / P $0.00 ｜ ATM IV 105.2%，净 delta 敞口 6k shares
Top ΔOI: C 780 +90 ｜ P 770 +76 ｜ C 1015 +76
仓位参考: Max Pain 870 ｜ Call Wall 780（+3.3%，弱）（OI 97） ｜ Put Wall 830（+9.9%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 105.2%｜历史 Rank 87%（近端代理）｜IV/RV 0.79×（近似）｜净 delta 敞口 正 6,150 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-19/SNDK_evening.json