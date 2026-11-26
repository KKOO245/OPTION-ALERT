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


## XBI

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
XBI: 今开 154.54 → 收盘 156.60（+1.3%） ｜ 今日高 157.02 ｜ 低 151.38 ｜ 昨收 156.82 → 收盘 156.60（-0.1%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-12-02，窗口结束前不做对错判定）

Options: P/C成交量 5.27 | OI比 1.98 | ATM IV 44.9% | Skew 15.1pp | Term 0.82 | ExpMove ±2.4%（近端） | Rank 91%
量化视角： IV 历史高位（Rank 91%，期权偏贵）｜期限结构倒挂（Term 0.82，近月 IV 高于远月）｜保护溢价显著（Skew 15.1pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 5.27）——观察点，非方向信号
   ⇒ Put/Call Volume: 5.27×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.98×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-27（2D）±2.4% ｜ 12-04（9D）±4.8% ｜ 12-11（16D）±3.0% ｜ 12-18（23D）±8.8%
   ⇒ IV–VIX Spread: +16.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 9,726,703 | GEX Change vs 上次快照 12,995,260 | Flip: Primary Flip: 154.47（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 386 / LOW 143 / INVALID 383
结构观察区: Primary Flip 154.47（全链重定价，覆盖 96%）
最近结构参考: Flip 154（现价高于该位 1.4%）
量化视角： 正 Gamma（973万，无历史分位）｜由负转正（+1300万）｜现价位于 Flip 上方 1.38%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 152（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 154（全链重定价，覆盖 96%）。
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
存量OI: C 7.1k / P 14.2k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $1.20 / P $2.60 ｜ ATM IV 44.9%，净 delta 敞口 0 shares
仓位参考: Max Pain 152 ｜ Call Wall 152（-2.9%，弱）（OI 0.6k） ｜ Put Wall 153（-2.3%，弱）（OI 2.9k）
量化解读： 存量 Put 重｜ATM IV 44.9%｜历史 Rank 91%（近端代理）｜IV/RV 0.95×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

12-04（Activity LOW）仓位参考: Max Pain 154 ｜ Call Wall 157.5（+0.6%，弱）（OI 0.2k） ｜ Put Wall 147（-6.1%，弱）（OI 2.0k）

12-11（Activity LOW）仓位参考: Max Pain 150 ｜ Call Wall 147（-6.1%，弱）（OI 1.0k） ｜ Put Wall 150（-4.2%，弱）（OI 2.0k）

12-18（Activity LOW）仓位参考: Max Pain 140

📅 事件差分（观察，非因果）: 11-27（2D）ATM IV 44.9% vs 12-04 37.7%（差 +7.2pp）——覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-25/XBI_evening.json