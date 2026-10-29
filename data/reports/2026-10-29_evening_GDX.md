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
🟡 **事件差分**: 10-30 ATM IV 48.5% vs 11-02 34.5%（差 +13.9pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-30 85C ΔOI +1,621（距现价 +4.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 81.82 → 收盘 81.33（-0.6%） ｜ 今日高 82.08 ｜ 低 80.71 ｜ 昨收 83.95 → 收盘 81.33（-3.1%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-05，窗口结束前不做对错判定）

Options: P/C成交量 0.84 | OI比 0.25 | ATM IV 48.5% | Skew 8.1pp | Term 0.82 | ExpMove ±2.1%（近端） | Rank 79%
量化视角： IV 历史高位（Rank 79%，期权偏贵）｜期限结构倒挂（Term 0.82，近月 IV 高于远月）｜保护溢价显著（Skew 8.1pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.25）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.84×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.25×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（1D）±2.1% ｜ 11-02（4D）±3.0% ｜ 11-04（6D）±4.1% ｜ 11-06（8D）±5.2%
   ⇒ IV–VIX Spread: +31.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 50,573,269 | GEX Change vs 上次快照 -4,086,991 | Flip: Primary Flip: 79.72（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 516 / LOW 142 / INVALID 462
结构观察区: Primary Flip 79.72（全链重定价，覆盖 91%）
Put Wall 80（弱结构｜现价高于该位 1.7%） | Call Wall 85（弱结构｜现价低于该位 4.3%）
最近结构参考: Put Wall 80（现价高于该位 1.7%）
量化视角： 正 Gamma（5057万，无历史分位）｜正 Gamma 减弱（409万）｜现价位于 Flip 上方 2.02%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 80（Put Wall，弱结构） / 81（MaxPain，仅结算参考）；上方 85（Call Wall，弱结构）。
• Gamma 区域：切换参考 80（全链重定价，覆盖 91%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-30  C +1.6k / P +0.2k ｜ Activity HIGH ｜ 1D
11-02  C +0.1k / P +0.4k ｜ Activity HIGH ｜ 4D
11-04  C +17 / P +12 ｜ Activity MEDIUM △ ｜ 6D
11-06  C +0.2k / P -22 ｜ Activity MEDIUM △ ｜ 8D

📆 10-30 Forward Structure
存量OI: C 136.8k / P 33.9k，今日变化ΔOI: C +1.6k / P +0.2k，平值价格ATM: C $1.01 / P $0.72 ｜ ATM IV 48.5%，净 delta 敞口 9k shares
Top ΔOI: C 85 +1,621 ｜ C 87 -538 ｜ P 80 +270
仓位参考: Max Pain 81 ｜ Call Wall 85（+4.5%）（OI 29.8k） ｜ Put Wall 79（-2.9%，弱）（OI 3.7k）
量化解读： 存量 Call 重｜ATM IV 48.5%｜历史 Rank 79%（近端代理）｜IV/RV 1.24×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 8,525 股

📆 11-02 Forward Structure
存量OI: C 1.7k / P 2.0k，今日变化ΔOI: C +0.1k / P +0.4k，平值价格ATM: C $1.35 / P $1.08 ｜ ATM IV 34.5%，净 delta 敞口 -7k shares
Top ΔOI: P 76 +150 ｜ P 80 +56
仓位参考: Max Pain 84 ｜ Call Wall 86（+5.7%）（OI 0.8k） ｜ Put Wall 81（-0.4%，弱）（OI 0.3k）
量化解读： 存量 Put 重｜ATM IV 34.5%｜历史 Rank 79%（近端代理）｜IV/RV 0.89×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 6,842 股

11-04（MEDIUM △）Top ΔOI: 85C +8 ｜ 80P +5
11-04（MEDIUM △）仓位参考: Max Pain 82 ｜ Call Wall 83（+2.1%，弱）（OI 0.2k） ｜ Put Wall 79（-2.9%）（OI 57）

11-06（MEDIUM △）Top ΔOI: 85C -798 ｜ 82P -98
11-06（MEDIUM △）仓位参考: Max Pain 85 ｜ Call Wall 85（+4.5%）（OI 2.4k） ｜ Put Wall 80（-1.6%，弱）（OI 2.3k）

📅 事件差分（观察，非因果）: 10-30（1D）ATM IV 48.5% vs 11-02 34.5%（差 +13.9pp）——覆盖 GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM、PCE 物价 Price Index MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-29/GDX_evening.json