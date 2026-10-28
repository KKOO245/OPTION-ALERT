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
🔴 **事件差分**: 10-30（2D）ATM IV 136.2% vs 11-06 89.2%（差 +47.0pp），覆盖 美联储议息会议 Statement、美联储利率决议 Decision、Fed Press Conference、GDP 增速 Rate QoQ Adv、PCE 物价 Price Index MoM、Personal Income MoM、Personal Spending MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 11-20 1400C ΔOI -301（距现价 -0.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 1,356.60 → 收盘 1,404.77（+3.6%） ｜ 今日高 1408.45 ｜ 低 1343.85 ｜ 昨收 1,304.84 → 收盘 1,404.77（+7.7%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-04，窗口结束前不做对错判定）

Options: P/C成交量 0.67 | OI比 0.77 | ATM IV 136.2% | Skew 2.0pp | Term 0.53 | ExpMove ±8.1%（近端） | Rank 88%
量化视角： IV 历史高位（Rank 88%，期权偏贵）｜期限结构倒挂（Term 0.53，近月 IV 高于远月）｜保护溢价薄（Skew 2.0pp）｜存量 Call 偏重（OI比 0.77）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.67×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.77×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（2D）±8.1% ｜ 11-06（9D）±11.5% ｜ 11-13（16D）±14.6% ｜ 11-20（23D）±15.4%
   ⇒ IV–VIX Spread: +119.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 3,510,516 | GEX Change vs 上次快照 1,783,173 | Flip: Primary Flip: 1328.74（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 2016 / LOW 394 / INVALID 984
结构观察区: Primary Flip 1328.74（全链重定价，覆盖 100%）
Call Wall 1,500（弱结构｜现价低于该位 6.3%）
最近结构参考: Flip 1329（现价高于该位 5.7%）
量化视角： 正 Gamma（351万，无历史分位）｜正 Gamma 增强（+178万）｜现价位于 Flip 上方 5.72%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 1,350（MaxPain，仅结算参考）；上方 1,500（Call Wall，弱结构）。
• Gamma 区域：切换参考 1329（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-30  C +4.2k / P +2.9k ｜ Activity HIGH ｜ 2D
11-06  C +2.5k / P +1.3k ｜ Activity HIGH ｜ 9D
11-13  C +0.3k / P +0.8k ｜ Activity HIGH ｜ 16D
11-20  C -0.6k / P +0.5k ｜ Activity MEDIUM △ ｜ 23D

📆 10-30 Forward Structure
存量OI: C 48.8k / P 37.6k，今日变化ΔOI: C +4.2k / P +2.9k，平值价格ATM: C $57.63 / P $56.05 ｜ ATM IV 136.2%，净 delta 敞口 121k shares
Top ΔOI: C 1670 +661 ｜ C 1610 +547 ｜ C 1300 +404
仓位参考: Max Pain 1,350 ｜ Call Wall 1500（+6.8%，弱）（OI 2.6k） ｜ Put Wall 1350（-3.9%，弱）（OI 1.1k）
量化解读： 存量 Call 重｜ATM IV 136.2%｜历史 Rank 88%（近端代理）｜IV/RV 2.33×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 121,283 股

📆 11-06 Forward Structure
存量OI: C 17.0k / P 12.3k，今日变化ΔOI: C +2.5k / P +1.3k，平值价格ATM: C $78.00 / P $83.50 ｜ ATM IV 89.2%，净 delta 敞口 30k shares
Top ΔOI: C 1650 +672 ｜ C 1600 +288
仓位参考: Max Pain 1,400 ｜ Call Wall 1400（-0.3%，弱）（OI 0.8k） ｜ Put Wall 1400（-0.3%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 89.2%｜历史 Rank 88%（近端代理）｜IV/RV 1.53×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 30,471 股

📆 11-13 Forward Structure
存量OI: C 5.8k / P 6.3k，今日变化ΔOI: C +0.3k / P +0.8k，平值价格ATM: C $95.45 / P $110.18 ｜ ATM IV 79.5%，净 delta 敞口 4k shares
Top ΔOI: C 1600 +51
仓位参考: Max Pain 1,480 ｜ Call Wall 1480（+5.4%，弱）（OI 0.2k） ｜ Put Wall 1300（-7.5%，弱）（OI 0.2k）
量化解读： 存量两侧均衡｜ATM IV 79.5%｜历史 Rank 88%（近端代理）｜IV/RV 1.36×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 3,559 股

11-20（MEDIUM △）Top ΔOI: 1500C -570 ｜ 1400C -301
11-20（MEDIUM △）仓位参考: Max Pain 1,490 ｜ Call Wall 1500（+6.8%，弱）（OI 2.1k） ｜ Put Wall 1450（+3.2%，弱）（OI 1.2k）

📅 事件差分（观察，非因果）: 10-30（2D）ATM IV 136.2% vs 11-06 89.2%（差 +47.0pp）——覆盖 美联储议息会议 Statement、美联储利率决议 Decision、Fed Press Conference、GDP 增速 Rate QoQ Adv、PCE 物价 Price Index MoM、Personal Income MoM、Personal Spending MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-28/SNDK_evening.json