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

🔍 重点速览
🟡 **近现价集中开仓**: 10-02 45P ΔOI +1,030（距现价 -0.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 46.88 → 收盘 45.43（-3.1%） ｜ 今日高 46.63 ｜ 低 44.75 ｜ 昨收 46.45 → 收盘 45.43（-2.2%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-02，窗口结束前不做对错判定）

Options: P/C成交量 0.85 | OI比 0.80 | ATM IV 59.1% | Skew -2.1pp | Term 0.90 | ExpMove ±4.5%（近端） | Rank 35%
量化视角： IV 中性（Rank 35%）｜期限结构正常（Term 0.90）｜Put 保护异常便宜（Skew -2.1pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.80）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.85×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.80×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（3D）±4.5% ｜ 10-09（10D）±7.5% ｜ 10-16（17D）±9.7% ｜ 10-23（24D）±11.3%
   ⇒ IV–VIX Spread: +43.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -4,219,069 | GEX Change vs 上次快照 -343,464 | Flip: Primary Flip: 48.77（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 309 / LOW 54 / INVALID 83
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 48.77（全链重定价，覆盖 100%）
最近结构参考: Flip 49（现价低于该位 6.8%）
量化视角： 负 Gamma（422万，无历史分位）｜负 Gamma 加深（34万）｜现价位于 Flip 下方 6.85%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 50（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 49（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C +1.0k / P +2.4k ｜ Activity HIGH ｜ 3D
10-09  C +0.4k / P +0.4k ｜ Activity HIGH ｜ 10D
10-16  C +1.2k / P +0.7k ｜ Activity HIGH ｜ 17D
10-23  C +19 / P +0.1k ｜ Activity HIGH ｜ 24D

📆 10-02 Forward Structure
存量OI: C 11.6k / P 9.3k，今日变化ΔOI: C +1.0k / P +2.4k，平值价格ATM: C $0.99 / P $1.05 ｜ ATM IV 59.2%，净 delta 敞口 -54k shares
Top ΔOI: P 45 +1,030 ｜ P 45 +898 ｜ P 46 +377
仓位参考: Max Pain 50 ｜ Call Wall 49（+7.9%，弱）（OI 1.3k） ｜ Put Wall 45（-0.9%，弱）（OI 1.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 59.2%｜历史 Rank 35%（近端代理）｜IV/RV 1.36×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 53,996 股

📆 10-09 Forward Structure
存量OI: C 4.7k / P 3.4k，今日变化ΔOI: C +0.4k / P +0.4k，平值价格ATM: C $1.67 / P $1.74 ｜ ATM IV 57.7%，净 delta 敞口 -7k shares
Top ΔOI: P 42 +149 ｜ P 46 +107
仓位参考: Max Pain 51 ｜ Put Wall 47（+3.5%）（OI 1.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 57.7%｜历史 Rank 35%（近端代理）｜IV/RV 1.33×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 7,056 股

📆 10-16 Forward Structure
存量OI: C 17.1k / P 14.6k，今日变化ΔOI: C +1.2k / P +0.7k，平值价格ATM: C $2.24 / P $2.17 ｜ ATM IV 54.6%，净 delta 敞口 5k shares
Top ΔOI: C 49 +975 ｜ C 47 +285 ｜ P 54 +238
仓位参考: Max Pain 50 ｜ Call Wall 49（+7.9%，弱）（OI 1.1k） ｜ Put Wall 45（-0.9%，弱）（OI 3.3k）
量化解读： 存量两侧均衡｜ATM IV 54.6%｜历史 Rank 35%（近端代理）｜IV/RV 1.26×（近似）｜净 delta 敞口 正 5,313 股

📆 10-23 Forward Structure
存量OI: C 1.7k / P 1.3k，今日变化ΔOI: C +19 / P +0.1k，平值价格ATM: C $2.59 / P $2.56 ｜ ATM IV 55.0%，净 delta 敞口 -6k shares
Top ΔOI: P 46 +30
仓位参考: Max Pain 52 ｜ Put Wall 45（-0.9%，弱）（OI 0.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 55.0%｜历史 Rank 35%（近端代理）｜IV/RV 1.27×（近似）｜净 delta 敞口 负 6,105 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=35 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=35）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-29/MP_evening.json