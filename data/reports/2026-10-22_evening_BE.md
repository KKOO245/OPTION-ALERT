# 期权晚报 2026-10-22（快照 16:40 ET）

📊 市场环境

SPY $763.96 ｜ QQQ $704.47
VIX 19.03 ↑14.1%（5D +15.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 19.8（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 228.15 → 收盘 217.77（-4.5%） ｜ 今日高 229.91 ｜ 低 210.74 ｜ 昨收 238.53 → 收盘 217.77（-8.7%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-27，窗口结束前不做对错判定）

Options: P/C成交量 0.80 | OI比 0.83 | ATM IV 226.6% | Skew 19.8pp | Term 0.40 | ExpMove ±9.3%（近端） | Rank 99%
量化视角： IV 历史高位（Rank 99%，期权偏贵）｜期限结构倒挂（Term 0.40，近月 IV 高于远月）｜保护溢价显著（Skew 19.8pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.83）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.80×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.83×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（1D）±9.3% ｜ 10-30（8D）±14.5% ｜ 11-06（15D）±17.1% ｜ 11-13（22D）±19.3%
   ⇒ IV–VIX Spread: +207.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -8,764,159 | GEX Change vs 上次快照 -3,063,344 | Flip: Primary Flip: 240.50（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 671 / LOW 73 / INVALID 116
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 240.50（全链重定价，覆盖 100%）
Put Wall 200（弱结构｜现价高于该位 8.9%）
最近结构参考: Put Wall 200（现价高于该位 8.9%）
量化视角： 负 Gamma（876万，无历史分位）｜负 Gamma 加深（306万）｜现价位于 Flip 下方 9.45%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall，弱结构）；上方 240（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 240（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +4.6k / P +2.8k ｜ Activity HIGH ｜ 1D
10-30  C +1.1k / P +1.9k ｜ Activity HIGH ｜ 8D
11-06  C +0.7k / P +0.1k ｜ Activity HIGH ｜ 15D
11-13  C +0.3k / P +0.3k ｜ Activity MEDIUM △ ｜ 22D

📆 10-23 Forward Structure
存量OI: C 57.2k / P 47.3k，今日变化ΔOI: C +4.6k / P +2.8k，平值价格ATM: C $10.09 / P $10.20 ｜ ATM IV 226.6%，净 delta 敞口 -86k shares
Top ΔOI: C 265 +1,143 ｜ C 235 +517 ｜ P 235 +445
仓位参考: Max Pain 240 ｜ Call Wall 230（+5.6%，弱）（OI 1.6k） ｜ Put Wall 200（-8.2%，弱）（OI 3.5k）
量化解读： 存量 Call 重｜ATM IV 226.6%｜历史 Rank 99%（近端代理）｜IV/RV 2.96×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 86,430 股

📆 10-30 Forward Structure
存量OI: C 21.4k / P 27.9k，今日变化ΔOI: C +1.1k / P +1.9k，平值价格ATM: C $14.62 / P $17.05 ｜ ATM IV 118.3%，净 delta 敞口 -29k shares
Top ΔOI: P 205 +269
仓位参考: Max Pain 250 ｜ Call Wall 230（+5.6%，弱）（OI 0.7k） ｜ Put Wall 205（-5.9%，弱）（OI 1.6k）
量化解读： 存量 Put 重｜ATM IV 118.3%｜历史 Rank 99%（近端代理）｜IV/RV 1.54×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 28,667 股

📆 11-06 Forward Structure
存量OI: C 8.7k / P 11.7k，今日变化ΔOI: C +0.7k / P +0.1k，平值价格ATM: C $17.50 / P $19.73 ｜ ATM IV 101.6%，净 delta 敞口 662 shares
仓位参考: Max Pain 250 ｜ Call Wall 225（+3.3%，弱）（OI 1.0k） ｜ Put Wall 235（+7.9%，弱）（OI 1.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 101.6%｜历史 Rank 99%（近端代理）｜IV/RV 1.33×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 662 股

11-13（MEDIUM △）Top ΔOI: 205P +142 ｜ 200P +60
11-13（MEDIUM △）仓位参考: Max Pain 250 ｜ Call Wall 220（+1.0%，弱）（OI 0.2k） ｜ Put Wall 230（+5.6%）（OI 2.7k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=61 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=61）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-22/BE_evening.json