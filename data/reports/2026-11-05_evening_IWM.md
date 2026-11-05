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
🟡 **事件差分**: 11-06 ATM IV 41.6% vs 11-09 28.5%（差 +13.2pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-09 283P ΔOI +10,229（距现价 +4.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## IWM

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
IWM: 今开 283.75 → 收盘 270.98（-4.5%） ｜ 今日高 284.70 ｜ 低 270.52 ｜ 昨收 284.02 → 收盘 270.98（-4.6%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-10，窗口结束前不做对错判定）

Options: P/C成交量 1.59 | OI比 0.87 | ATM IV 29.2% | Skew 7.0pp | Term 0.86 | ExpMove ±1.8%（近端） | Rank 70%
量化视角： IV 中性（Rank 70%）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜保护溢价显著（Skew 7.0pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 1.59）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.59×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.87×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-06（1D）±1.8% ｜ 11-09（4D）±2.4% ｜ 11-10（5D）±2.7% ｜ 11-11（6D）±2.9%
   ⇒ IV–VIX Spread: +1.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,070,174,565 | GEX Change vs 上次快照 -521,647,470 | Flip: Primary Flip: 285.61（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 1216 / LOW 195 / INVALID 1201
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 285.61（全链重定价，覆盖 95%）
Put Wall 270（弱结构｜现价高于该位 0.4%） | Call Wall 290（弱结构｜现价低于该位 6.6%）
最近结构参考: Put Wall 270（现价高于该位 0.4%）
量化视角： 负 Gamma（10.70亿，无历史分位）｜负 Gamma 加深（5.22亿）｜现价位于 Flip 下方 5.12%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 270（Put Wall，弱结构）；上方 283（MaxPain，仅结算参考） / 290（Call Wall，弱结构）。
• Gamma 区域：切换参考 286（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-06  C +35.2k / P +2.7k ｜ Activity HIGH ｜ 1D
11-09  C +4.5k / P +12.5k ｜ Activity HIGH ｜ 4D
11-10  C +13.6k / P +9.9k ｜ Activity HIGH ｜ 5D
11-11  C +2.8k / P +4.7k ｜ Activity HIGH ｜ 6D

📆 11-06 Forward Structure
存量OI: C 167.9k / P 298.8k，今日变化ΔOI: C +35.2k / P +2.7k，平值价格ATM: C $2.17 / P $2.58 ｜ ATM IV 41.6%，净 delta 敞口 -213k shares
Top ΔOI: C 290 +15,289 ｜ C 288 +5,819 ｜ C 287 +3,241
仓位参考: Max Pain 280 ｜ Call Wall 290（+7.0%）（OI 25.3k） ｜ Put Wall 277（+2.2%，弱）（OI 30.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 41.6%｜历史 Rank 70%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 213,246 股

📆 11-09 Forward Structure
存量OI: C 23.4k / P 35.9k，今日变化ΔOI: C +4.5k / P +12.5k，平值价格ATM: C $3.05 / P $3.31 ｜ ATM IV 28.5%，净 delta 敞口 -1.1M shares
Top ΔOI: P 283 +10,229 ｜ P 266 +1,011 ｜ C 293 +677
仓位参考: Max Pain 283 ｜ Call Wall 285（+5.2%）（OI 7.6k） ｜ Put Wall 283（+4.4%）（OI 10.5k）
量化解读： 存量 Put 重｜ATM IV 28.5%｜历史 Rank 70%（近端代理）｜净 delta 敞口 负 1,109,201 股

📆 11-10 Forward Structure
存量OI: C 19.4k / P 20.1k，今日变化ΔOI: C +13.6k / P +9.9k，平值价格ATM: C $3.61 / P $3.77 ｜ ATM IV 29.8%，净 delta 敞口 -681k shares
Top ΔOI: C 292 +3,987 ｜ C 290 +3,758 ｜ P 282 +1,945
仓位参考: Max Pain 282 ｜ Call Wall 290（+7.0%，弱）（OI 4.2k） ｜ Put Wall 280（+3.3%）（OI 3.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 29.8%｜历史 Rank 70%（近端代理）｜净 delta 敞口 负 680,673 股

📆 11-11 Forward Structure
存量OI: C 10.1k / P 12.4k，今日变化ΔOI: C +2.8k / P +4.7k，平值价格ATM: C $4.12 / P $3.77 ｜ ATM IV 29.9%，净 delta 敞口 -338k shares
Top ΔOI: P 277 +2,332 ｜ C 298 +903 ｜ P 282 +521
仓位参考: Max Pain 282 ｜ Call Wall 286（+5.5%）（OI 3.1k） ｜ Put Wall 277（+2.2%）（OI 3.0k）
量化解读： 存量 Put 重｜ATM IV 29.9%｜历史 Rank 70%（近端代理）｜净 delta 敞口 负 337,651 股

📅 事件差分（观察，非因果）: 11-06（1D）ATM IV 41.6% vs 11-09 28.5%（差 +13.2pp）——覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=85 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=85）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-05/IWM_evening.json