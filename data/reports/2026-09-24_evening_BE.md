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
🟡 **近现价集中开仓**: 09-25 275P ΔOI +745（距现价 +3.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 256.00 → 收盘 266.65（+4.2%） ｜ 今日高 269.34 ｜ 低 251.30 ｜ 昨收 275.19 → 收盘 266.65（-3.1%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-09-29，窗口结束前不做对错判定）

Options: P/C成交量 0.57 | OI比 1.24 | ATM IV 85.0% | Skew -0.5pp | Term 0.89 | ExpMove ±3.6%（近端） | Rank 45%
量化视角： IV 中性（Rank 45%）｜期限结构倒挂（Term 0.89，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.5pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.57×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.24×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-25（1D）±3.6% ｜ 10-02（8D）±9.2% ｜ 10-09（15D）±12.2% ｜ 10-16（22D）±14.6%
   ⇒ IV–VIX Spread: +69.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -162,359 | GEX Change vs 上次快照 -13,492,536 | Flip: Primary Flip: 266.78（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 576 / LOW 117 / INVALID 241
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 266.78（全链重定价，覆盖 98%）
Put Wall 240（弱结构｜现价高于该位 11.1%）
最近结构参考: Flip 267（现价低于该位 0.0%）
量化视角： 负 Gamma（16万，无历史分位）｜由正转负（1349万）｜现价位于 Flip 下方 0.05%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 240（Put Wall，弱结构）；上方 268（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 267（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +4.3k / P +5.9k ｜ Activity HIGH ｜ 1D
10-02  C +2.2k / P +3.7k ｜ Activity HIGH ｜ 8D（新行权价 C 2）
10-09  C +0.6k / P +1.4k ｜ Activity HIGH ｜ 15D
10-16  C +3.1k / P +1.4k ｜ Activity HIGH ｜ 22D

📆 09-25 Forward Structure
存量OI: C 41.4k / P 51.4k，今日变化ΔOI: C +4.3k / P +5.9k，平值价格ATM: C $4.15 / P $5.39 ｜ ATM IV 85.0%，净 delta 敞口 -304k shares
Top ΔOI: P 240 +772 ｜ P 275 +745
仓位参考: Max Pain 268 ｜ Call Wall 280（+5.0%，弱）（OI 3.2k） ｜ Put Wall 250（-6.2%，弱）（OI 4.0k）
量化解读： 存量 Put 重｜ATM IV 85.0%｜历史 Rank 45%（近端代理）｜IV/RV 1.21×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 303,760 股

📆 10-02 Forward Structure
存量OI: C 21.7k / P 21.3k，今日变化ΔOI: C +2.2k / P +3.7k（新行权价 C 2），平值价格ATM: C $11.70 / P $12.82 ｜ ATM IV 77.7%，净 delta 敞口 -150k shares
Top ΔOI: C 270 -2,503 ｜ C 320 +1,061 ｜ P 250 +838
仓位参考: Max Pain 255 ｜ Call Wall 270（+1.3%，弱）（OI 3.0k） ｜ Put Wall 245（-8.1%，弱）（OI 2.0k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 77.7%｜历史 Rank 45%（近端代理）｜IV/RV 1.10×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 150,156 股

📆 10-09 Forward Structure
存量OI: C 4.9k / P 9.1k，今日变化ΔOI: C +0.6k / P +1.4k，平值价格ATM: C $15.95 / P $16.70 ｜ ATM IV 75.7%，净 delta 敞口 -13k shares
Top ΔOI: P 245 +451
仓位参考: Max Pain 260 ｜ Call Wall 275（+3.1%，弱）（OI 0.3k） ｜ Put Wall 240（-10.0%）（OI 1.6k）
量化解读： 存量 Put 重｜ATM IV 75.7%｜历史 Rank 45%（近端代理）｜IV/RV 1.08×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 13,277 股

📆 10-16 Forward Structure
存量OI: C 67.9k / P 71.5k，今日变化ΔOI: C +3.1k / P +1.4k，平值价格ATM: C $18.87 / P $20.00 ｜ ATM IV 75.1%，净 delta 敞口 18k shares
Top ΔOI: C 320 +854 ｜ P 200 -410 ｜ C 300 +384
仓位参考: Max Pain 255 ｜ Call Wall 280（+5.0%，弱）（OI 8.2k） ｜ Put Wall 240（-10.0%，弱）（OI 3.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 75.1%｜历史 Rank 45%（近端代理）｜IV/RV 1.07×（近似）｜净 delta 敞口 正 18,060 股

📅 事件差分（观察，非因果）: 09-25（1D）ATM IV 85.0% vs 10-02 77.7%（差 +7.3pp）——覆盖 耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=28 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=28）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-24/BE_evening.json