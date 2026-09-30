# 期权晚报 2026-09-30（快照 16:40 ET）

📊 市场环境

SPY $762.63 ｜ QQQ $739.77
VIX 16.34 ↑1.9%（5D +7.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 30.8（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-30

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.2 ｜ 前值 0.1　✅ 今日已公布
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 2.2 ｜ 前值 2.5　✅ 今日已公布
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 0.9 ｜ 前值 0.1　✅ 今日已公布
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-02 52P ΔOI +1,500（距现价 -4.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 55.11 → 收盘 54.51（-1.1%） ｜ 今日高 55.24 ｜ 低 54.22 ｜ 昨收 55.48 → 收盘 54.51（-1.7%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-05，窗口结束前不做对错判定）

Options: P/C成交量 0.94 | OI比 0.39 | ATM IV 42.8% | Skew -0.5pp | Term 0.80 | ExpMove ±2.4%（近端） | Rank 71%
量化视角： IV 中性（Rank 71%）｜期限结构倒挂（Term 0.80，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.5pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.39）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.94×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.39×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（2D）±2.4% ｜ 10-05（5D）±2.9% ｜ 10-07（7D）±3.5% ｜ 10-09（9D）±4.2%
   ⇒ IV–VIX Spread: +26.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -4,689,051 | GEX Change vs 上次快照 -14,896,805 | Flip: Primary Flip: 54.72（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 85%（带内） ｜ IV 有效性: VALID 679 / LOW 112 / INVALID 707
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 54.72（全链重定价，覆盖 85%）
Put Wall 50（弱结构｜现价高于该位 9.0%）
最近结构参考: Flip 55（现价低于该位 0.4%）
量化视角： 负 Gamma（469万，无历史分位）｜由正转负（1490万）｜现价位于 Flip 下方 0.39%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 50（Put Wall，弱结构） / 54（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 55（全链重定价，覆盖 85%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C +4.2k / P +2.6k ｜ Activity HIGH ｜ 2D
10-05  C +2.3k / P +1.7k ｜ Activity HIGH ｜ 5D
10-07  C +1.0k / P +1.3k ｜ Activity HIGH ｜ 7D
10-09  C +2.4k / P +0.6k ｜ Activity HIGH ｜ 9D

📆 10-02 Forward Structure
存量OI: C 90.1k / P 46.2k，今日变化ΔOI: C +4.2k / P +2.6k，平值价格ATM: C $0.67 / P $0.64 ｜ ATM IV 40.1%，净 delta 敞口 175k shares
Top ΔOI: P 52 +1,500 ｜ C 55 +823 ｜ C 56 +798
仓位参考: Max Pain 58 ｜ Call Wall 59（+8.2%，弱）（OI 6.6k） ｜ Put Wall 50（-8.3%）（OI 7.4k）
量化解读： 存量 Call 重｜ATM IV 40.1%｜历史 Rank 71%（近端代理）｜IV/RV 1.04×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 175,423 股

📆 10-05 Forward Structure
存量OI: C 7.0k / P 6.0k，今日变化ΔOI: C +2.3k / P +1.7k，平值价格ATM: C $0.79 / P $0.80 ｜ ATM IV 30.4%，净 delta 敞口 -9k shares
Top ΔOI: P 52 +976 ｜ C 55 +359
仓位参考: Max Pain 57 ｜ Call Wall 55.5（+1.8%，弱）（OI 0.6k） ｜ Put Wall 52（-4.6%）（OI 1.3k）
量化解读： 存量两侧均衡｜ATM IV 30.4%｜历史 Rank 71%（近端代理）｜IV/RV 0.79×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 9,457 股

📆 10-07 Forward Structure
存量OI: C 5.1k / P 5.1k，今日变化ΔOI: C +1.0k / P +1.3k，平值价格ATM: C $0.96 / P $0.97 ｜ ATM IV 32.1%，净 delta 敞口 -14k shares
Top ΔOI: P 53 +353 ｜ C 55 +300 ｜ P 51 +240
仓位参考: Max Pain 57 ｜ Call Wall 59（+8.2%，弱）（OI 0.8k） ｜ Put Wall 57（+4.6%）（OI 1.7k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 32.1%｜历史 Rank 71%（近端代理）｜IV/RV 0.84×（近似）｜净 delta 敞口 负 13,918 股

📆 10-09 Forward Structure
存量OI: C 62.3k / P 16.8k，今日变化ΔOI: C +2.4k / P +0.6k，平值价格ATM: C $1.15 / P $1.11 ｜ ATM IV 33.0%，净 delta 敞口 17k shares
Top ΔOI: P 52 -409 ｜ C 56 +318 ｜ P 54 +312
仓位参考: Max Pain 57 ｜ Put Wall 55（+0.9%，弱）（OI 2.7k）
量化解读： 存量 Call 重｜ATM IV 33.0%｜历史 Rank 71%（近端代理）｜IV/RV 0.86×（近似）｜净 delta 敞口 正 17,111 股

📅 事件差分（观察，非因果）: 10-02（2D）ATM IV 40.1% vs 10-05 30.4%（差 +9.7pp）——覆盖 PCE 物价 Price Index MoM、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=35 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=35）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-30/SLV_evening.json