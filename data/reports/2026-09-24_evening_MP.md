# 期权晚报 2026-09-24（快照 16:40 ET）

📊 市场环境

SPY $767.18 ｜ QQQ $741.10
VIX 15.67 ↑3.2%（5D -11.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 36.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-24

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **事件差分**: 09-25 ATM IV 65.4% vs 10-02 54.9%（差 +10.5pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 09-25 47P ΔOI +650（距现价 -3.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 48.37 → 收盘 49.30（+1.9%） ｜ 今日高 49.89 ｜ 低 47.60 ｜ 昨收 48.89 → 收盘 49.30（+0.8%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-09-29，窗口结束前不做对错判定）

Options: P/C成交量 0.44 | OI比 0.80 | ATM IV 65.4% | Skew 1.7pp | Term 0.84 | ExpMove ±2.9%（近端） | Rank 46%
量化视角： IV 中性（Rank 46%）｜期限结构倒挂（Term 0.84，近月 IV 高于远月）｜保护溢价薄（Skew 1.7pp）｜存量 Call 偏重（OI比 0.80）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.44×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.80×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-25（1D）±2.9% ｜ 10-02（8D）±6.7% ｜ 10-09（15D）±9.8% ｜ 10-16（22D）±11.4%
   ⇒ IV–VIX Spread: +49.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -228,537 | GEX Change vs 上次快照 -3,982,985 | Flip: Primary Flip: 49.36（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 316 / LOW 64 / INVALID 104
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 49.36（全链重定价，覆盖 96%）
Put Wall 50（弱结构｜现价低于该位 1.4%）
最近结构参考: Flip 49（现价低于该位 0.1%）
量化视角： 负 Gamma（23万，无历史分位）｜由正转负（398万）｜现价位于 Flip 下方 0.13%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 50（Put Wall，弱结构） / 50（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 49（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +1.3k / P +1.4k ｜ Activity HIGH ｜ 1D
10-02  C +0.3k / P +1.0k ｜ Activity HIGH ｜ 8D
10-09  C +0.6k / P +76 ｜ Activity MEDIUM △ ｜ 15D
10-16  C +1.4k / P +1.9k ｜ Activity HIGH ｜ 22D

📆 09-25 Forward Structure
存量OI: C 15.2k / P 12.2k，今日变化ΔOI: C +1.3k / P +1.4k，平值价格ATM: C $0.56 / P $0.88 ｜ ATM IV 65.4%，净 delta 敞口 37k shares
Top ΔOI: P 47 +650 ｜ C 49 +348 ｜ P 48 +345
仓位参考: Max Pain 50 ｜ Call Wall 52（+5.5%，弱）（OI 1.7k） ｜ Put Wall 47（-4.7%，弱）（OI 1.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 65.4%｜历史 Rank 46%（近端代理）｜IV/RV 1.56×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 36,623 股

📆 10-02 Forward Structure
存量OI: C 8.1k / P 5.2k，今日变化ΔOI: C +0.3k / P +1.0k，平值价格ATM: C $1.55 / P $1.76 ｜ ATM IV 54.9%，净 delta 敞口 -26k shares
Top ΔOI: P 50 +231 ｜ C 52 +156 ｜ P 54 +91
仓位参考: Max Pain 50 ｜ Call Wall 49（-0.6%，弱）（OI 1.1k） ｜ Put Wall 50（+1.4%）（OI 1.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 54.9%｜历史 Rank 46%（近端代理）｜IV/RV 1.31×（近似）｜净 delta 敞口 负 26,469 股

10-09（MEDIUM △）仓位参考: Max Pain 52 ｜ Put Wall 47（-4.7%）（OI 1.1k）

📆 10-16 Forward Structure
存量OI: C 15.4k / P 13.1k，今日变化ΔOI: C +1.4k / P +1.9k，平值价格ATM: C $2.69 / P $2.93 ｜ ATM IV 56.1%，净 delta 敞口 -32k shares
Top ΔOI: P 50 +783 ｜ C 52 +430 ｜ P 49 +326
仓位参考: Max Pain 55 ｜ Call Wall 50（+1.4%，弱）（OI 3.0k） ｜ Put Wall 50（+1.4%，弱）（OI 3.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 56.1%｜历史 Rank 46%（近端代理）｜IV/RV 1.34×（近似）｜净 delta 敞口 负 31,805 股

📅 事件差分（观察，非因果）: 09-25（1D）ATM IV 65.4% vs 10-02 54.9%（差 +10.5pp）——覆盖 耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=28 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=28）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-24/MP_evening.json