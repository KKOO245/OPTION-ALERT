# 期权晚报 2026-10-28（快照 16:40 ET）

📊 市场环境

SPY $772.31 ｜ QQQ $725.61
VIX 16.91 ↓3.5%（5D +1.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-28

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布　✅ 今日已公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 4 ｜ 前值 4　✅ 今日已公布
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布　✅ 今日已公布
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.9

🔍 重点速览
🟡 **近现价集中开仓**: 10-30 222C ΔOI +2,305（距现价 +3.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 219.88 → 收盘 215.38（-2.0%） ｜ 今日高 219.99 ｜ 低 214.47 ｜ 昨收 217.94 → 收盘 215.38（-1.2%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-04，窗口结束前不做对错判定）

Options: P/C成交量 0.65 | OI比 0.93 | ATM IV 86.4% | Skew 5.6pp | Term 0.47 | ExpMove ±2.6%（近端） | Rank 94%
量化视角： IV 历史高位（Rank 94%，期权偏贵）｜期限结构倒挂（Term 0.47，近月 IV 高于远月）｜保护溢价中性（Skew 5.6pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.65×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.93×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-30（2D）±2.6% ｜ 11-02（5D）±3.2% ｜ 11-04（7D）±4.0% ｜ 11-06（9D）±4.7%
   ⇒ IV–VIX Spread: +69.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 201,361,064 | GEX Change vs 上次快照 -109,526,172 | Flip: Primary Flip: 209.60（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 641 / LOW 232 / INVALID 587
结构观察区: Primary Flip 209.60（全链重定价，覆盖 96%）
Put Wall 200（弱结构｜现价高于该位 7.7%） | Call Wall 230（现价低于该位 6.4%）
最近结构参考: Flip 210（现价高于该位 2.8%）
量化视角： 正 Gamma（2.01亿，无历史分位）｜正 Gamma 减弱（1.10亿）｜现价位于 Flip 上方 2.76%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall，弱结构） / 215（MaxPain，仅结算参考）；上方 230（Call Wall）。
• Gamma 区域：切换参考 210（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-30  C +11.0k / P +5.9k ｜ Activity MEDIUM △ ｜ 2D
11-02  C +6.0k / P +7.8k ｜ Activity HIGH ｜ 5D
11-04  C +3.5k / P +2.0k ｜ Activity HIGH ｜ 7D
11-06  C +5.3k / P +5.5k ｜ Activity HIGH ｜ 9D

📆 10-30 Forward Structure
存量OI: C 482.8k / P 304.3k，今日变化ΔOI: C +11.0k / P +5.9k，平值价格ATM: C $2.98 / P $2.53 ｜ ATM IV 42.7%，净 delta 敞口 91k shares
Top ΔOI: C 230 +2,807 ｜ C 232 +2,586 ｜ C 222 +2,305
仓位参考: Max Pain 215 ｜ Call Wall 225（+4.5%，弱）（OI 59.2k） ｜ Put Wall 210（-2.5%，弱）（OI 23.5k）
量化解读： 存量 Call 重｜ATM IV 42.7%｜历史 Rank 94%（近端代理）｜IV/RV 1.56×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 90,934 股

📆 11-02 Forward Structure
存量OI: C 20.2k / P 20.2k，今日变化ΔOI: C +6.0k / P +7.8k，平值价格ATM: C $3.57 / P $3.31 ｜ ATM IV 33.1%，净 delta 敞口 -135k shares
Top ΔOI: P 215 +2,409 ｜ C 225 +1,633
仓位参考: Max Pain 215 ｜ Call Wall 230（+6.8%，弱）（OI 3.3k） ｜ Put Wall 215（-0.2%，弱）（OI 2.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 33.1%｜历史 Rank 94%（近端代理）｜IV/RV 1.21×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 135,025 股

📆 11-04 Forward Structure
存量OI: C 12.0k / P 8.0k，今日变化ΔOI: C +3.5k / P +2.0k，平值价格ATM: C $4.55 / P $4.00 ｜ ATM IV 35.8%，净 delta 敞口 31k shares
Top ΔOI: C 225 +745 ｜ C 217 +490 ｜ P 205 +468
仓位参考: Max Pain 215 ｜ Call Wall 225（+4.5%）（OI 3.7k） ｜ Put Wall 205（-4.8%，弱）（OI 1.0k）
量化解读： 存量 Call 重｜ATM IV 35.8%｜历史 Rank 94%（近端代理）｜IV/RV 1.31×（近似）｜净 delta 敞口 正 31,119 股

📆 11-06 Forward Structure
存量OI: C 109.4k / P 152.1k，今日变化ΔOI: C +5.3k / P +5.5k，平值价格ATM: C $5.25 / P $4.80 ｜ ATM IV 36.5%，净 delta 敞口 7k shares
Top ΔOI: C 217 +1,688 ｜ C 230 +1,639
仓位参考: Max Pain 225 ｜ Call Wall 230（+6.8%，弱）（OI 12.3k） ｜ Put Wall 200（-7.1%，弱）（OI 11.7k）
量化解读： 存量 Put 重｜ATM IV 36.5%｜历史 Rank 94%（近端代理）｜IV/RV 1.33×（近似）｜净 delta 敞口 正 6,512 股

📅 事件差分（观察，非因果）: 10-30（2D）ATM IV 42.7% vs 11-02 33.1%（差 +9.7pp）——覆盖 美联储议息会议 Statement、美联储利率决议 Decision、Fed Press Conference、GDP 增速 Rate QoQ Adv、PCE 物价 Price Index MoM、Personal Income MoM、Personal Spending MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-28/NVDA_evening.json