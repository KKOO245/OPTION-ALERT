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
🟡 **近现价集中开仓**: 09-25 152P ΔOI +7,438（距现价 +3.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPCX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPCX: 今开 148.22 → 收盘 148.03（-0.1%） ｜ 今日高 149.00 ｜ 低 145.88 ｜ 昨收 148.36 → 收盘 148.03（-0.2%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-09-29，窗口结束前不做对错判定）

Options: P/C成交量 0.68 | OI比 0.87 | ATM IV 48.3% | Skew -2.8pp | Term 0.94 | ExpMove ±2.0%（近端） | Rank 16%
量化视角： IV 历史低位（Rank 16%，期权偏便宜）｜期限结构正常（Term 0.94）｜Put 保护异常便宜（Skew -2.8pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.68×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.87×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-25（1D）±2.0% ｜ 10-02（8D）±5.5% ｜ 10-09（15D）±7.5% ｜ 10-16（22D）±9.0%
   ⇒ IV–VIX Spread: +32.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -41,743,414 | GEX Change vs 上次快照 -83,645,992 | Flip: Primary Flip: 150.02（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 530 / LOW 137 / INVALID 323
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 150.02（全链重定价，覆盖 100%）
Call Wall 160（弱结构｜现价低于该位 7.5%）
最近结构参考: Flip 150（现价低于该位 1.3%）
量化视角： 负 Gamma（4174万，无历史分位）｜由正转负（8365万）｜现价位于 Flip 下方 1.33%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 150（MaxPain，仅结算参考） / 160（Call Wall，弱结构）。
• Gamma 区域：切换参考 150（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +29.0k / P +22.4k ｜ Activity HIGH ｜ 1D
10-02  C +26.2k / P +19.5k ｜ Activity HIGH ｜ 8D
10-09  C +4.2k / P +5.2k ｜ Activity HIGH ｜ 15D
10-16  C +6.4k / P -62.9k ｜ Activity HIGH ｜ 22D

📆 09-25 Forward Structure
存量OI: C 250.8k / P 217.6k，今日变化ΔOI: C +29.0k / P +22.4k，平值价格ATM: C $1.56 / P $1.46 ｜ ATM IV 48.3%，净 delta 敞口 -603k shares
Top ΔOI: P 152 +7,438 ｜ C 155 +6,045 ｜ C 157 +5,209
仓位参考: Max Pain 150 ｜ Call Wall 160（+8.1%，弱）（OI 30.9k） ｜ Put Wall 150（+1.3%，弱）（OI 20.2k）
量化解读： 存量两侧均衡｜ATM IV 48.3%｜历史 Rank 16%（近端代理）｜IV/RV 1.06×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 603,132 股

📆 10-02 Forward Structure
存量OI: C 91.8k / P 96.9k，今日变化ΔOI: C +26.2k / P +19.5k，平值价格ATM: C $4.20 / P $3.95 ｜ ATM IV 46.6%，净 delta 敞口 -83k shares
Top ΔOI: C 157 +3,075 ｜ C 150 +2,925 ｜ C 155 +2,853
仓位参考: Max Pain 150 ｜ Call Wall 155（+4.7%，弱）（OI 7.6k） ｜ Put Wall 150（+1.3%，弱）（OI 5.7k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 46.6%｜历史 Rank 16%（近端代理）｜IV/RV 1.03×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 82,948 股

📆 10-09 Forward Structure
存量OI: C 28.3k / P 32.0k，今日变化ΔOI: C +4.2k / P +5.2k，平值价格ATM: C $5.70 / P $5.39 ｜ ATM IV 46.0%，净 delta 敞口 -81k shares
Top ΔOI: P 135 +918 ｜ P 155 +858 ｜ C 155 +854
仓位参考: Max Pain 150 ｜ Call Wall 160（+8.1%，弱）（OI 2.5k） ｜ Put Wall 135（-8.8%）（OI 4.6k）
量化解读： 存量两侧均衡｜ATM IV 46.0%｜历史 Rank 16%（近端代理）｜IV/RV 1.01×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 81,250 股

📆 10-16 Forward Structure
存量OI: C 321.2k / P 335.2k，今日变化ΔOI: C +6.4k / P -62.9k，平值价格ATM: C $6.85 / P $6.45 ｜ ATM IV 45.6%，净 delta 敞口 3.0M shares
Top ΔOI: P 155 -37,864 ｜ P 135 -35,680 ｜ P 145 +5,638
仓位参考: Max Pain 140 ｜ Call Wall 160（+8.1%，弱）（OI 34.1k） ｜ Put Wall 135（-8.8%，弱）（OI 28.7k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 45.6%｜历史 Rank 16%（近端代理）｜IV/RV 1.00×（近似）｜净 delta 敞口 正 2,991,944 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=28 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=28）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-24/SPCX_evening.json