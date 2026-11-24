# 期权晚报 2026-11-24（快照 16:40 ET）

📊 市场环境

SPY $718.78 ｜ QQQ $638.10
VIX 26.36 ↓1.0%（5D +3.5%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 17.4（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-24

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-25 08:30　【高】Personal Spending MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.5
- 周三 11-25 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 11-25 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 11-25 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 3.5 ｜ 实际 待公布 ｜ 前值 1.5
- 周三 11-25 08:30　【高】耐用品订单 Orders MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 1.8

🔍 重点速览
🟡 **近现价集中开仓**: 11-25 619P ΔOI +4,655（距现价 -3.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 640.02 → 收盘 638.10（-0.3%） ｜ 今日高 643.47 ｜ 低 631.15 ｜ 昨收 651.03 → 收盘 638.10（-2.0%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-12-01，窗口结束前不做对错判定）

Options: P/C成交量 1.12 | OI比 1.55 | ATM IV 46.9% | Skew 4.0pp | Term 0.68 | ExpMove ±1.8%（近端） | Rank 97%
量化视角： IV 历史高位（Rank 97%，期权偏贵）｜期限结构倒挂（Term 0.68，近月 IV 高于远月）｜保护溢价中性（Skew 4.0pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.12×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.55×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 24% ｜ P/C OI(近端) 43%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 24%）｜近端持仓结构中性（P/C OI 分位 43%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-25（1D）±1.8% ｜ 11-27（3D）±2.4% ｜ 11-30（6D）±3.2% ｜ 12-01（7D）±3.6%
   ⇒ IV–VIX Spread: +20.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -413,637,650 | GEX Change vs 上次快照 -106,176,945 | Flip: Primary Flip: 657.25（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 3172 / LOW 681 / INVALID 1793
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 657.25（全链重定价，覆盖 95%）
最近结构参考: Flip 657（现价低于该位 2.9%）
量化视角： 负 Gamma（4.14亿，历史分位偏负区，比 76% 的交易日更负）｜负 Gamma 加深（1.06亿）｜现价位于 Flip 下方 2.91%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 650（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 657（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-25  C +8.7k / P +46.5k ｜ Activity HIGH ｜ 1D
11-27  C +32.2k / P +80.8k ｜ Activity HIGH ｜ 3D
11-30  C +37.5k / P +39.8k ｜ Activity HIGH ｜ 6D
12-01  C +1.9k / P +5.3k ｜ Activity HIGH ｜ 7D

📆 11-25 Forward Structure
存量OI: C 101.4k / P 101.0k，今日变化ΔOI: C +8.7k / P +46.5k，平值价格ATM: C $5.01 / P $6.19 ｜ ATM IV 41.4%，净 delta 敞口 -939k shares
Top ΔOI: P 605 +15,315 ｜ P 619 +4,655
仓位参考: Max Pain 642 ｜ Call Wall 650（+1.9%，弱）（OI 5.6k） ｜ Put Wall 619（-3.0%，弱）（OI 4.7k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 41.4%｜历史 Rank 97%（近端代理）｜IV/RV 0.90×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 939,154 股

📆 11-27 Forward Structure
存量OI: C 266.9k / P 257.1k，今日变化ΔOI: C +32.2k / P +80.8k，平值价格ATM: C $7.30 / P $8.27 ｜ ATM IV 34.1%，净 delta 敞口 -1.7M shares
Top ΔOI: P 550 +27,701 ｜ C 700 +15,529
仓位参考: Max Pain 654 ｜ Put Wall 640（+0.3%，弱）（OI 15.7k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 34.1%｜历史 Rank 97%（近端代理）｜IV/RV 0.74×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,692,147 股

📆 11-30 Forward Structure
存量OI: C 335.9k / P 346.0k，今日变化ΔOI: C +37.5k / P +39.8k，平值价格ATM: C $9.78 / P $10.71 ｜ ATM IV 31.2%，净 delta 敞口 -457k shares
Top ΔOI: P 540 +11,169 ｜ P 500 +11,167
仓位参考: Max Pain 670 ｜ Call Wall 650（+1.9%，弱）（OI 13.8k） ｜ Put Wall 650（+1.9%，弱）（OI 21.3k）
量化解读： 存量两侧均衡｜ATM IV 31.2%｜历史 Rank 97%（近端代理）｜IV/RV 0.68×（近似）｜净 delta 敞口 负 456,870 股

📆 12-01 Forward Structure
存量OI: C 20.8k / P 41.1k，今日变化ΔOI: C +1.9k / P +5.3k，平值价格ATM: C $11.20 / P $11.98 ｜ ATM IV 32.7%，净 delta 敞口 -182k shares
Top ΔOI: C 630 -1,140 ｜ P 575 +435 ｜ C 650 +420
仓位参考: Max Pain 642 ｜ Call Wall 630（-1.3%，弱）（OI 1.0k）
量化解读： 存量 Put 重｜ATM IV 32.7%｜历史 Rank 97%（近端代理）｜IV/RV 0.71×（近似）｜净 delta 敞口 负 182,418 股

📅 事件差分（观察，非因果）: 11-25（1D）ATM IV 41.4% vs 11-27 34.1%（差 +7.3pp）——覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-24/QQQ_evening.json