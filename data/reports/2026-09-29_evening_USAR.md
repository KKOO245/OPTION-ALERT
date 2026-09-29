# 期权晚报 2026-09-29（快照 16:40 ET）

📊 市场环境

SPY $764.20 ｜ QQQ $737.93
VIX 16.04 ↓0.2%（5D +12.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-29

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-29 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.23 ｜ 实际 7.079 ｜ 前值 7.335　✅ 今日已公布
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 待公布 ｜ 前值 2.1
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 14.58 → 收盘 14.07（-3.5%） ｜ 今日高 14.58 ｜ 低 13.96 ｜ 昨收 14.41 → 收盘 14.07（-2.4%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-02，窗口结束前不做对错判定）

Options: P/C成交量 0.51 | OI比 0.50 | ATM IV 69.8% | Skew -8.2pp | Term 0.98 | ExpMove ±5.1%（近端） | Rank 3%
量化视角： IV 历史低位（Rank 3%，期权偏便宜）｜期限结构正常（Term 0.98）｜Put 保护异常便宜（Skew -8.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.50）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.51×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.50×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（3D）±5.1% ｜ 10-09（10D）±9.1% ｜ 10-16（17D）±11.5% ｜ 10-23（24D）±13.9%
   ⇒ IV–VIX Spread: +53.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -3,497,634 | GEX Change vs 上次快照 -567,362 | Flip: Primary Flip: 15.35（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 204 / LOW 68 / INVALID 132
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 15.35（全链重定价，覆盖 100%）
Put Wall 15（弱结构｜现价低于该位 6.2%）
最近结构参考: Put Wall 15（现价低于该位 6.2%）
量化视角： 负 Gamma（350万，无历史分位）｜负 Gamma 加深（57万）｜现价位于 Flip 下方 8.33%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 15（Put Wall，弱结构） / 16（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 15（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C +2.8k / P -1.5k ｜ Activity HIGH ｜ 3D
10-09  C +1.2k / P +1.8k ｜ Activity HIGH ｜ 10D
10-16  C +2.0k / P +1.4k ｜ Activity HIGH ｜ 17D
10-23  C +0.9k / P +0.3k ｜ Activity HIGH ｜ 24D

📆 10-02 Forward Structure
存量OI: C 24.1k / P 12.0k，今日变化ΔOI: C +2.8k / P -1.5k，平值价格ATM: C $0.41 / P $0.31 ｜ ATM IV 69.8%，净 delta 敞口 257k shares
Top ΔOI: P 17 -879 ｜ P 15 -827
仓位参考: Max Pain 16 ｜ Put Wall 15（+6.6%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 69.8%｜历史 Rank 3%（近端代理）｜IV/RV 1.27×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 257,458 股

📆 10-09 Forward Structure
存量OI: C 7.8k / P 6.3k，今日变化ΔOI: C +1.2k / P +1.8k，平值价格ATM: C $0.67 / P $0.61 ｜ ATM IV 66.2%，净 delta 敞口 -125k shares
Top ΔOI: P 15 +853 ｜ P 16 +563
仓位参考: Max Pain 16 ｜ Put Wall 15（+6.6%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 66.2%｜历史 Rank 3%（近端代理）｜IV/RV 1.21×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 125,241 股

📆 10-16 Forward Structure
存量OI: C 40.9k / P 15.3k，今日变化ΔOI: C +2.0k / P +1.4k，平值价格ATM: C $0.87 / P $0.75 ｜ ATM IV 66.3%，净 delta 敞口 -79k shares
Top ΔOI: P 17 +642
仓位参考: Max Pain 17 ｜ Put Wall 15（+6.6%）（OI 5.7k）
量化解读： 存量 Call 重｜ATM IV 66.3%｜历史 Rank 3%（近端代理）｜IV/RV 1.21×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 79,468 股

📆 10-23 Forward Structure
存量OI: C 9.2k / P 3.1k，今日变化ΔOI: C +0.9k / P +0.3k，平值价格ATM: C $1.03 / P $0.93 ｜ ATM IV 66.1%，净 delta 敞口 -10k shares
Top ΔOI: P 17 +212
仓位参考: Max Pain 18 ｜ Put Wall 15（+6.6%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 66.1%｜历史 Rank 3%（近端代理）｜IV/RV 1.20×（近似）｜净 delta 敞口 负 9,626 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=35 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=35）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-29/USAR_evening.json