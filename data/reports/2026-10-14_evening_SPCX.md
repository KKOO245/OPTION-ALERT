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
🟡 **事件差分**: 10-16 ATM IV 56.3% vs 10-19 44.0%（差 +12.3pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-16 157C ΔOI +4,473（距现价 +3.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-21 162C ΔOI +1,686 占该期限总 OI 10.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SPCX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPCX: 今开 154.96 → 收盘 152.16（-1.8%） ｜ 今日高 155.44 ｜ 低 151.10 ｜ 昨收 156.54 → 收盘 152.16（-2.8%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-19，窗口结束前不做对错判定）

Options: P/C成交量 0.95 | OI比 0.47 | ATM IV 51.8% | Skew 8.2pp | Term 1.04 | ExpMove ±3.3%（近端） | Rank 41%
量化视角： IV 中性（Rank 41%）｜期限结构正常（Term 1.04）｜保护溢价显著（Skew 8.2pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.47）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.95×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.47×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（2D）±3.3% ｜ 10-19（5D）±4.2% ｜ 10-21（7D）±5.2% ｜ 10-23（9D）±6.1%
   ⇒ IV–VIX Spread: +34.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -9,930,223 | GEX Change vs 上次快照 -16,665,277 | Flip: Primary Flip: 153.07（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 716 / LOW 182 / INVALID 578
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 153.07（全链重定价，覆盖 97%）
最近结构参考: Flip 153（现价低于该位 0.6%）
量化视角： 负 Gamma（993万，无历史分位）｜由正转负（1667万）｜现价位于 Flip 下方 0.60%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 160（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 153（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +11.5k / P -0.3k ｜ Activity MEDIUM △ ｜ 2D
10-19  C +10.9k / P +3.3k ｜ Activity HIGH ｜ 5D
10-21  C +5.8k / P +2.9k ｜ Activity HIGH ｜ 7D
10-23  C +9.5k / P +5.4k ｜ Activity HIGH ｜ 9D

📆 10-16 Forward Structure
存量OI: C 409.3k / P 414.6k，今日变化ΔOI: C +11.5k / P -0.3k，平值价格ATM: C $2.46 / P $2.62 ｜ ATM IV 56.3%，净 delta 敞口 441k shares
Top ΔOI: C 165 +10,378 ｜ C 157 +4,473
仓位参考: Max Pain 150 ｜ Call Wall 165（+8.4%，弱）（OI 33.1k） ｜ Put Wall 150（-1.4%，弱）（OI 25.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 56.3%｜历史 Rank 41%（近端代理）｜IV/RV 1.13×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 440,713 股

📆 10-19 Forward Structure
存量OI: C 26.3k / P 9.2k，今日变化ΔOI: C +10.9k / P +3.3k，平值价格ATM: C $3.03 / P $3.31 ｜ ATM IV 44.0%，净 delta 敞口 -29k shares
Top ΔOI: C 157 +2,552 ｜ C 162 +2,296
仓位参考: Max Pain 160 ｜ Call Wall 157.5（+3.5%，弱）（OI 2.6k） ｜ Put Wall 162.5（+6.8%，弱）（OI 1.8k）
量化解读： 存量 Call 重｜ATM IV 44.0%｜历史 Rank 41%（近端代理）｜IV/RV 0.88×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 29,312 股

📆 10-21 Forward Structure
存量OI: C 10.2k / P 5.5k，今日变化ΔOI: C +5.8k / P +2.9k，平值价格ATM: C $3.80 / P $4.10 ｜ ATM IV 46.5%，净 delta 敞口 -15k shares
Top ΔOI: C 162 +1,686 ｜ P 147 +1,416
仓位参考: Max Pain 160 ｜ Call Wall 162.5（+6.8%，弱）（OI 1.8k） ｜ Put Wall 147（-3.4%）（OI 1.4k）
量化解读： 存量 Call 重｜ATM IV 46.5%｜历史 Rank 41%（近端代理）｜IV/RV 0.94×（近似）｜净 delta 敞口 负 14,912 股

📆 10-23 Forward Structure
存量OI: C 56.6k / P 65.7k，今日变化ΔOI: C +9.5k / P +5.4k，平值价格ATM: C $4.55 / P $4.75 ｜ ATM IV 48.2%，净 delta 敞口 -86k shares
Top ΔOI: C 160 +2,377 ｜ C 165 +1,736 ｜ P 200 +1,575
仓位参考: Max Pain 158 ｜ Call Wall 165（+8.4%，弱）（OI 5.3k） ｜ Put Wall 140（-8.0%，弱）（OI 6.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 48.2%｜历史 Rank 41%（近端代理）｜IV/RV 0.97×（近似）｜净 delta 敞口 负 85,733 股

📅 事件差分（观察，非因果）: 10-16（2D）ATM IV 56.3% vs 10-19 44.0%（差 +12.3pp）——覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY、Inflation Rate YoY、Inflation Rate MoM、PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-14/SPCX_evening.json