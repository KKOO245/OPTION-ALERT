# 期权晚报 2026-10-28（快照 21:00 ET）

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
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.9

🔍 重点速览
🔴 **事件差分**: 10-30（2D）ATM IV 106.5% vs 11-06 81.1%（差 +25.3pp），覆盖 美联储议息会议 Statement、美联储利率决议 Decision、Fed Press Conference、PCE 物价 Price Index MoM、GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 139.57 → 收盘 145.16（+4.0%） ｜ 今日高 145.30 ｜ 低 138.66 ｜ 昨收 141.40 → 收盘 145.16（+2.7%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-04，窗口结束前不做对错判定）

Options: P/C成交量 0.40 | OI比 0.73 | ATM IV 106.5% | Skew -0.3pp | Term 0.66 | ExpMove ±6.4%（近端） | Rank 85%
量化视角： IV 历史高位（Rank 85%，期权偏贵）｜期限结构倒挂（Term 0.66，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.3pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.73）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.40×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.73×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（2D）±6.4% ｜ 11-06（9D）±10.5% ｜ 11-13（16D）±12.5% ｜ 11-20（23D）±14.8%
   ⇒ IV–VIX Spread: +89.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 45,321,546 | GEX Change vs 上次快照 17,850,089 | Flip: Primary Flip: 137.72（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 538 / LOW 90 / INVALID 288
结构观察区: Primary Flip 137.72（全链重定价，覆盖 100%）
Call Wall 135（弱结构｜现价高于该位 7.5%）
最近结构参考: Flip 138（现价高于该位 5.4%）
量化视角： 正 Gamma（4532万，无历史分位）｜正 Gamma 增强（+1785万）｜现价位于 Flip 上方 5.40%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 142（MaxPain，仅结算参考） / 135（Call Wall，弱结构）。
• Gamma 区域：切换参考 138（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-30  C +0 / P +0 ｜ Activity LOW ｜ 2D
11-06  C +0 / P +0 ｜ Activity LOW ｜ 9D
11-13  C +0 / P +0 ｜ Activity LOW ｜ 16D
11-20  C +0 / P +0 ｜ Activity LOW ｜ 23D

📆 10-30 Forward Structure
存量OI: C 233.7k / P 171.4k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $4.70 / P $4.53 ｜ ATM IV 106.5%，净 delta 敞口 0 shares
仓位参考: Max Pain 142 ｜ Call Wall 152.5（+5.1%，弱）（OI 37.8k）
量化解读： 存量 Call 重｜ATM IV 106.5%｜历史 Rank 85%（近端代理）｜IV/RV 1.62×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-06（Activity LOW）仓位参考: Max Pain 155 ｜ Call Wall 150（+3.3%，弱）（OI 1.4k） ｜ Put Wall 155（+6.8%，弱）（OI 3.6k）

11-13（Activity LOW）仓位参考: Max Pain 160 ｜ Put Wall 155（+6.8%，弱）（OI 2.4k）

11-20（Activity LOW）仓位参考: Max Pain 135 ｜ Call Wall 135（-7.0%）（OI 42.4k） ｜ Put Wall 145（-0.1%，弱）（OI 4.2k）

📅 事件差分（观察，非因果）: 10-30（2D）ATM IV 106.5% vs 11-06 81.1%（差 +25.3pp）——覆盖 美联储议息会议 Statement、美联储利率决议 Decision、Fed Press Conference、PCE 物价 Price Index MoM、GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-28/MSTR_evening.json