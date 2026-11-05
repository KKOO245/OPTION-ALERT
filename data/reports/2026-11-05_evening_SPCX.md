# 期权晚报 2026-11-05（快照 16:40 ET）

📊 市场环境

SPY $733.00 ｜ QQQ $647.05
VIX 28.18 ↑69.7%（5D +63.8%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 19.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-05

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🔴 **事件差分**: 11-06（1D）ATM IV 118.8% vs 11-09 82.4%（差 +36.4pp），覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Vol Regime 升档**: ELEVATED → STRESS（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-09 120P ΔOI +7,880（距现价 -2.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPCX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPCX: 今开 131.34 → 收盘 123.62（-5.9%） ｜ 今日高 131.87 ｜ 低 120.42 ｜ 昨收 135.92 → 收盘 123.62（-9.0%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-10，窗口结束前不做对错判定）

Options: P/C成交量 1.09 | OI比 0.71 | ATM IV 118.9% | Skew 18.3pp | Term 0.56 | ExpMove ±5.0%（近端） | Rank 96%
量化视角： IV 历史高位（Rank 96%，期权偏贵）｜期限结构倒挂（Term 0.56，近月 IV 高于远月）｜保护溢价显著（Skew 18.3pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.71）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.09×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.71×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（1D）±5.0% ｜ 11-09（4D）±7.0% ｜ 11-11（6D）±9.0% ｜ 11-13（8D）±10.1%
   ⇒ IV–VIX Spread: +90.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -74,527,794 | GEX Change vs 上次快照 8,858,279 | Flip: Primary Flip: 137.30（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 682 / LOW 171 / INVALID 601
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 137.30（全链重定价，覆盖 95%）
Put Wall 135（弱结构｜现价低于该位 8.4%）
最近结构参考: Put Wall 135（现价低于该位 8.4%）
量化视角： 负 Gamma（7453万，无历史分位）｜负 Gamma 缓解（+886万）｜现价位于 Flip 下方 9.96%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 135（Put Wall，弱结构） / 142（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 137（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-06  C +7.9k / P -1.6k ｜ Activity MEDIUM △ ｜ 1D
11-09  C +3.8k / P +19.6k ｜ Activity HIGH ｜ 4D
11-11  C +3.2k / P +2.1k ｜ Activity HIGH ｜ 6D
11-13  C +10.3k / P +11.8k ｜ Activity HIGH ｜ 8D

📆 11-06 Forward Structure
存量OI: C 257.3k / P 181.6k，今日变化ΔOI: C +7.9k / P -1.6k，平值价格ATM: C $2.89 / P $3.33 ｜ ATM IV 118.8%，净 delta 敞口 718k shares
Top ΔOI: P 135 -6,650
仓位参考: Max Pain 142 ｜ Put Wall 135（+9.2%，弱）（OI 15.7k）
量化解读： 存量 Call 重｜ATM IV 118.8%｜历史 Rank 96%（近端代理）｜IV/RV 2.05×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 718,364 股

📆 11-09 Forward Structure
存量OI: C 13.4k / P 27.2k，今日变化ΔOI: C +3.8k / P +19.6k，平值价格ATM: C $4.02 / P $4.68 ｜ ATM IV 82.4%，净 delta 敞口 -881k shares
Top ΔOI: P 120 +7,880 ｜ P 130 +3,647 ｜ P 115 +2,625
仓位参考: Max Pain 140 ｜ Put Wall 120（-2.9%）（OI 8.0k）
量化解读： 存量 Put 重｜ATM IV 82.4%｜历史 Rank 96%（近端代理）｜IV/RV 1.42×（近似）｜净 delta 敞口 负 880,800 股

📆 11-11 Forward Structure
存量OI: C 6.7k / P 5.3k，今日变化ΔOI: C +3.2k / P +2.1k，平值价格ATM: C $5.35 / P $5.80 ｜ ATM IV 85.1%，净 delta 敞口 -74k shares
Top ΔOI: C 140 +896 ｜ P 125 +512
仓位参考: Max Pain 139 ｜ Put Wall 125（+1.1%，弱）（OI 0.9k）
量化解读： 存量 Call 重｜ATM IV 85.1%｜历史 Rank 96%（近端代理）｜IV/RV 1.47×（近似）｜净 delta 敞口 负 73,536 股

📆 11-13 Forward Structure
存量OI: C 82.6k / P 71.6k，今日变化ΔOI: C +10.3k / P +11.8k，平值价格ATM: C $6.00 / P $6.48 ｜ ATM IV 85.5%，净 delta 敞口 -370k shares
Top ΔOI: P 118 +2,831 ｜ P 117 +2,029 ｜ P 124 +1,958
仓位参考: Max Pain 145 ｜ Put Wall 135（+9.2%，弱）（OI 5.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 85.5%｜历史 Rank 96%（近端代理）｜IV/RV 1.48×（近似）｜净 delta 敞口 负 370,102 股

📅 事件差分（观察，非因果）: 11-06（1D）ATM IV 118.8% vs 11-09 82.4%（差 +36.4pp）——覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=85 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=85）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-05/SPCX_evening.json