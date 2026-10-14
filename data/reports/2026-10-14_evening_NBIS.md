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
🔴 **事件差分**: 10-16（2D）ATM IV 106.3% vs 10-23 84.0%（差 +22.3pp），覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY、Inflation Rate YoY、Inflation Rate MoM、PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 10-16 195P ΔOI +2,122（距现价 +4.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 195.00 → 收盘 186.01（-4.6%） ｜ 今日高 198.60 ｜ 低 183.13 ｜ 昨收 206.86 → 收盘 186.01（-10.1%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-19，窗口结束前不做对错判定）

Options: P/C成交量 0.72 | OI比 0.92 | ATM IV 106.3% | Skew 5.6pp | Term 0.83 | ExpMove ±6.3%（近端） | Rank 57%
量化视角： IV 中性（Rank 57%）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜保护溢价中性（Skew 5.6pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.72×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.92×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（2D）±6.3% ｜ 10-23（9D）±10.3% ｜ 10-30（16D）±13.7% ｜ 11-06（23D）±16.1%
   ⇒ IV–VIX Spread: +89.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -21,556,571 | GEX Change vs 上次快照 -1,576,652 | Flip: Primary Flip: 209.77（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 528 / LOW 50 / INVALID 118
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 209.77（全链重定价，覆盖 100%）
Put Wall 200（弱结构｜现价低于该位 7.0%）
最近结构参考: Put Wall 200（现价低于该位 7.0%）
量化视角： 负 Gamma（2156万，无历史分位）｜负 Gamma 加深（158万）｜现价位于 Flip 下方 11.33%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 200（Put Wall，弱结构） / 220（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 210（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +7.0k / P +1.8k ｜ Activity HIGH ｜ 2D
10-23  C +6.5k / P +2.3k ｜ Activity HIGH ｜ 9D
10-30  C +3.4k / P +1.4k ｜ Activity HIGH ｜ 16D
11-06  C +3.5k / P +0.4k ｜ Activity HIGH ｜ 23D

📆 10-16 Forward Structure
存量OI: C 133.5k / P 123.3k，今日变化ΔOI: C +7.0k / P +1.8k，平值价格ATM: C $6.45 / P $5.30 ｜ ATM IV 106.3%，净 delta 敞口 113k shares
Top ΔOI: C 230 +5,257 ｜ P 195 +2,122
仓位参考: Max Pain 220 ｜ Call Wall 200（+7.5%，弱）（OI 3.4k） ｜ Put Wall 190（+2.1%，弱）（OI 7.3k）
量化解读： 存量两侧均衡｜ATM IV 106.3%｜历史 Rank 57%（近端代理）｜IV/RV 1.72×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 113,063 股

📆 10-23 Forward Structure
存量OI: C 30.9k / P 21.2k，今日变化ΔOI: C +6.5k / P +2.3k，平值价格ATM: C $10.15 / P $9.04 ｜ ATM IV 84.0%，净 delta 敞口 -53k shares
Top ΔOI: P 190 +684
仓位参考: Max Pain 215 ｜ Put Wall 200（+7.5%，弱）（OI 2.8k）
量化解读： 存量 Call 重｜ATM IV 84.0%｜历史 Rank 57%（近端代理）｜IV/RV 1.36×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 52,831 股

📆 10-30 Forward Structure
存量OI: C 26.0k / P 19.0k，今日变化ΔOI: C +3.4k / P +1.4k，平值价格ATM: C $13.50 / P $12.00 ｜ ATM IV 82.3%，净 delta 敞口 -37k shares
Top ΔOI: C 240 +470
仓位参考: Max Pain 220 ｜ Put Wall 200（+7.5%）（OI 2.6k）
量化解读： 存量 Call 重｜ATM IV 82.3%｜历史 Rank 57%（近端代理）｜IV/RV 1.33×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 36,921 股

📆 11-06 Forward Structure
存量OI: C 11.3k / P 13.4k，今日变化ΔOI: C +3.5k / P +0.4k，平值价格ATM: C $15.40 / P $14.60 ｜ ATM IV 80.5%，净 delta 敞口 79k shares
Top ΔOI: C 220 +1,974 ｜ C 225 +889 ｜ C 210 +165
仓位参考: Max Pain 220 ｜ Put Wall 200（+7.5%）（OI 3.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 80.5%｜历史 Rank 57%（近端代理）｜IV/RV 1.30×（近似）｜净 delta 敞口 正 78,744 股

📅 事件差分（观察，非因果）: 10-16（2D）ATM IV 106.3% vs 10-23 84.0%（差 +22.3pp）——覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY、Inflation Rate YoY、Inflation Rate MoM、PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-14/NBIS_evening.json