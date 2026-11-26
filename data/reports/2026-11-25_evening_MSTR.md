# 期权晚报 2026-11-25（快照 21:00 ET）

📊 市场环境

SPY $716.70 ｜ QQQ $633.93
VIX 28.29 ↑7.3%（5D +15.2%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 15.2（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-25

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-25 08:30　【高】Personal Spending MoM　预测 0.4 ｜ 实际 0.3 ｜ 前值 0.6　✅ 今日已公布
- 周三 11-25 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周三 11-25 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 0.7 ｜ 前值 0.3　✅ 今日已公布
- 周三 11-25 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 3.5 ｜ 实际 4.3 ｜ 前值 1.5　✅ 今日已公布
- 周三 11-25 08:30　【高】耐用品订单 Orders MoM　预测 0.6 ｜ 实际 0.2 ｜ 前值 1.8　✅ 今日已公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 74.24 → 收盘 79.96（+7.7%） ｜ 今日高 81.02 ｜ 低 70.37 ｜ 昨收 77.55 → 收盘 79.96（+3.1%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-12-02，窗口结束前不做对错判定）

Options: P/C成交量 0.94 | OI比 0.56 | ATM IV 110.9% | Skew 4.7pp | Term 0.95 | ExpMove ±6.4%（近端） | Rank 86%
量化视角： IV 历史高位（Rank 86%，期权偏贵）｜期限结构正常（Term 0.95）｜保护溢价中性（Skew 4.7pp）｜存量 Call 偏重（OI比 0.56）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.94×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.56×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（2D）±6.4% ｜ 12-04（9D）±14.6% ｜ 12-11（16D）±18.5% ｜ 12-18（23D）±21.7%
   ⇒ IV–VIX Spread: +82.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -9,271,459 | GEX Change vs 上次快照 10,908,539 | Flip: Primary Flip: 81.19（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 559 / LOW 229 / INVALID 244
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 81.19（全链重定价，覆盖 100%）
Put Wall 80（弱结构｜现价低于该位 0.1%）
最近结构参考: Put Wall 80（现价低于该位 0.1%）
量化视角： 负 Gamma（927万，无历史分位）｜负 Gamma 缓解（+1091万）｜现价位于 Flip 下方 1.51%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 80（Put Wall，弱结构） / 85（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 81（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-27  C +0 / P +0 ｜ Activity LOW ｜ 2D
12-04  C +0 / P +0 ｜ Activity LOW ｜ 9D
12-11  C +0 / P +0 ｜ Activity LOW ｜ 16D
12-18  C +0 / P +0 ｜ Activity LOW ｜ 23D

📆 11-27 Forward Structure
存量OI: C 262.3k / P 145.7k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $2.60 / P $2.55 ｜ ATM IV 110.9%，净 delta 敞口 0 shares
仓位参考: Max Pain 85 ｜ Call Wall 85（+6.3%，弱）（OI 28.5k） ｜ Put Wall 80（+0.1%，弱）（OI 7.9k）
量化解读： 存量 Call 重｜ATM IV 110.9%｜历史 Rank 86%（近端代理）｜IV/RV 1.38×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

12-04（Activity LOW）仓位参考: Max Pain 86 ｜ Call Wall 80（+0.1%，弱）（OI 7.2k） ｜ Put Wall 80（+0.1%，弱）（OI 8.8k）

12-11（Activity LOW）仓位参考: Max Pain 100 ｜ Put Wall 80（+0.1%，弱）（OI 3.8k）

12-18（Activity LOW）仓位参考: Max Pain 115 ｜ Call Wall 85（+6.3%，弱）（OI 9.6k） ｜ Put Wall 80（+0.1%，弱）（OI 9.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-25/MSTR_evening.json