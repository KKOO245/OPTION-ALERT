# 期权晚报 2026-10-29（快照 16:40 ET）

📊 市场环境

SPY $769.36 ｜ QQQ $715.34
VIX 17.20 ↑1.7%（5D -9.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-29

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 3.4 ｜ 前值 2.2　✅ 今日已公布
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 0.5 ｜ 前值 0.9　✅ 今日已公布
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-30 690P ΔOI -6,665（距现价 -3.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 716.57 → 收盘 715.34（-0.2%） ｜ 今日高 718.07 ｜ 低 711.62 ｜ 昨收 725.61 → 收盘 715.34（-1.4%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-05，窗口结束前不做对错判定）

Options: P/C成交量 1.09 | OI比 1.94 | ATM IV 110.9% | Skew -1.7pp | Term 0.19 | ExpMove ±1.5%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.19，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.7pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.09×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.94×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 15% ｜ P/C OI(近端) 73%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 15%）｜近端持仓结构中性（P/C OI 分位 73%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-30（1D）±1.5% ｜ 11-02（4D）±1.9% ｜ 11-03（5D）±2.3% ｜ 11-04（6D）±2.5%
   ⇒ IV–VIX Spread: +93.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -649,034,975 | GEX Change vs 上次快照 33,654,148 | Flip: Primary Flip: 725.83（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 2594 / LOW 445 / INVALID 987
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 725.83（全链重定价，覆盖 94%）
最近结构参考: Flip 726（现价低于该位 1.4%）
量化视角： 负 Gamma（6.49亿，历史分位偏负区，比 85% 的交易日更负）｜负 Gamma 缓解（+3365万）｜现价位于 Flip 下方 1.45%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 722（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 726（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-30  C +7.8k / P +9.7k ｜ Activity MEDIUM △ ｜ 1D
11-02  C +6.3k / P +15.1k ｜ Activity HIGH ｜ 4D
11-03  C +2.5k / P +14.9k ｜ Activity HIGH ｜ 5D
11-04  C +3.0k / P +6.2k ｜ Activity HIGH ｜ 6D

📆 10-30 Forward Structure
存量OI: C 396.3k / P 809.4k，今日变化ΔOI: C +7.8k / P +9.7k，平值价格ATM: C $1.09 / P $9.53 ｜ ATM IV 26.9%，净 delta 敞口 -791k shares
Top ΔOI: P 690 -6,665 ｜ P 700 -5,828
仓位参考: Max Pain 723 ｜ Call Wall 730（+2.0%，弱）（OI 19.8k） ｜ Put Wall 700（-2.1%，弱）（OI 42.1k）
量化解读： 存量 Put 重｜ATM IV 26.9%｜历史 Rank 100%（近端代理）｜IV/RV 1.45×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 790,566 股

📆 11-02 Forward Structure
存量OI: C 47.8k / P 65.6k，今日变化ΔOI: C +6.3k / P +15.1k，平值价格ATM: C $2.38 / P $10.88 ｜ ATM IV 19.0%，净 delta 敞口 -619k shares
Top ΔOI: P 703 +5,113 ｜ P 670 -2,673 ｜ P 715 +2,022
仓位参考: Max Pain 719 ｜ Call Wall 725（+1.4%，弱）（OI 8.3k） ｜ Put Wall 695（-2.8%，弱）（OI 7.0k）
量化解读： 存量 Put 重｜ATM IV 19.0%｜历史 Rank 100%（近端代理）｜IV/RV 1.02×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 618,798 股

📆 11-03 Forward Structure
存量OI: C 23.1k / P 52.5k，今日变化ΔOI: C +2.5k / P +14.9k，平值价格ATM: C $3.37 / P $12.78 ｜ ATM IV 20.2%，净 delta 敞口 -130k shares
Top ΔOI: P 635 +5,785 ｜ P 640 +5,237 ｜ P 675 +1,364
仓位参考: Max Pain 714 ｜ Call Wall 710（-0.7%）（OI 2.7k）
量化解读： 存量 Put 重｜ATM IV 20.2%｜历史 Rank 100%（近端代理）｜IV/RV 1.09×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 130,126 股

📆 11-04 Forward Structure
存量OI: C 16.7k / P 29.3k，今日变化ΔOI: C +3.0k / P +6.2k，平值价格ATM: C $4.68 / P $13.55 ｜ ATM IV 22.1%，净 delta 敞口 -280k shares
Top ΔOI: P 700 +970 ｜ P 722 +502 ｜ P 665 +447
仓位参考: Max Pain 720 ｜ Call Wall 730（+2.0%，弱）（OI 0.9k） ｜ Put Wall 715（-0.0%，弱）（OI 3.7k）
量化解读： 存量 Put 重｜ATM IV 22.1%｜历史 Rank 100%（近端代理）｜IV/RV 1.19×（近似）｜净 delta 敞口 负 279,558 股

📅 事件差分（观察，非因果）: 10-30（1D）ATM IV 26.9% vs 11-02 19.0%（差 +7.9pp）——覆盖 GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM、PCE 物价 Price Index MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-29/QQQ_evening.json