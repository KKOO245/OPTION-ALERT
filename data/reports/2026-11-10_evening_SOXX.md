# 期权晚报 2026-11-10（快照 16:40 ET）

📊 市场环境

SPY $749.92 ｜ QQQ $674.76
VIX 19.46 ↓2.3%（5D -6.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-10

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-10 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周二 11-10 08:30　【高】Inflation Rate MoM　预测 0.3 ｜ 实际 0.4 ｜ 前值 0.6　✅ 今日已公布
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-20 140P ΔOI +14,908（距现价 -4.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SOXX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SOXX: 今开 144.18 → 收盘 146.59（+1.7%） ｜ 今日高 149.74 ｜ 低 143.13 ｜ 昨收 146.76 → 收盘 146.59（-0.1%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-17，窗口结束前不做对错判定）

Options: P/C成交量 1.27 | OI比 2.16 | ATM IV 69.1% | Skew 11.1pp | Term 0.79 | ExpMove ±5.3%（近端） | Rank 96%
量化视角： IV 历史高位（Rank 96%，期权偏贵）｜期限结构倒挂（Term 0.79，近月 IV 高于远月）｜保护溢价显著（Skew 11.1pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 1.27）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.27×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 2.16×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-13（3D）±5.3% ｜ 11-20（10D）±8.5% ｜ 11-27（17D）±7.9% ｜ 12-04（24D）±11.1%
   ⇒ IV–VIX Spread: +49.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -50,259,407 | GEX Change vs 上次快照 -9,905,367 | Flip: Primary Flip: 154.31（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 585 / LOW 441 / INVALID 778
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 154.31（全链重定价，覆盖 96%）
最近结构参考: Flip 154（现价低于该位 5.0%）
量化视角： 负 Gamma（5026万，无历史分位）｜负 Gamma 加深（991万）｜现价位于 Flip 下方 5.01%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 153（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 154（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +3.5k / P +22.5k ｜ Activity HIGH ｜ 3D
11-20  C +10.4k / P +2.0k ｜ Activity HIGH ｜ 10D
11-27  C +0.5k / P +1.1k ｜ Activity MEDIUM △ ｜ 17D
12-04  C +1.3k / P +51 ｜ Activity HIGH ｜ 24D

📆 11-13 Forward Structure
存量OI: C 110.1k / P 238.0k，今日变化ΔOI: C +3.5k / P +22.5k，平值价格ATM: C $3.56 / P $4.20 ｜ ATM IV 69.1%，净 delta 敞口 132k shares
Top ΔOI: P 105 +29,721 ｜ P 138 -4,054
仓位参考: Max Pain 153
量化解读： 存量 Put 重｜ATM IV 69.1%｜历史 Rank 96%（近端代理）｜IV/RV 0.16×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 131,520 股

📆 11-20 Forward Structure
存量OI: C 199.5k / P 313.6k，今日变化ΔOI: C +10.4k / P +2.0k，平值价格ATM: C $6.00 / P $6.40 ｜ ATM IV 62.7%，净 delta 敞口 -92k shares
Top ΔOI: P 140 +14,908 ｜ P 105 -12,672 ｜ P 120 -11,783
仓位参考: Max Pain 162 ｜ Call Wall 153.33（+4.6%，弱）（OI 7.8k） ｜ Put Wall 150（+2.3%，弱）（OI 21.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 62.7%｜历史 Rank 96%（近端代理）｜IV/RV 0.14×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 91,743 股

11-27（MEDIUM △）Top ΔOI: 127P +400 ｜ 142P +200
11-27（MEDIUM △）仓位参考: Max Pain 162 ｜ Put Wall 146.67（+0.1%，弱）（OI 3.2k）

📆 12-04 Forward Structure
存量OI: C 5.9k / P 7.9k，今日变化ΔOI: C +1.3k / P +51，平值价格ATM: C $7.37 / P $8.90 ｜ ATM IV 54.8%，净 delta 敞口 35k shares
Top ΔOI: C 160 +748 ｜ C 148 +227
仓位参考: Max Pain 160 ｜ Call Wall 153.33（+4.6%，弱）（OI 0.3k） ｜ Put Wall 148.33（+1.2%，弱）（OI 0.9k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 54.8%｜历史 Rank 96%（近端代理）｜IV/RV 0.12×（近似）｜净 delta 敞口 正 34,889 股

📅 事件差分（观察，非因果）: 11-13（3D）ATM IV 69.1% vs 11-20 62.7%（差 +6.3pp）——覆盖 Core Inflation Rate MoM、Inflation Rate MoM 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-10/SOXX_evening.json