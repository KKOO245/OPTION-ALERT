# 期权晚报 2026-11-19（快照 16:40 ET）

📊 市场环境

SPY $715.87 ｜ QQQ $nan
VIX 28.44 ↑15.8%（5D +52.1%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 18.7（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🔴 **Vol Regime 升档**: ELEVATED → STRESS（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 152.92 → 收盘 145.98（-4.5%） ｜ 今日高 158.13 ｜ 低 145.71 ｜ 昨收 150.96 → 收盘 145.98（-3.3%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-24，窗口结束前不做对错判定）

Options: P/C成交量 0.99 | OI比 0.55 | ATM IV 83.1% | Skew 7.3pp | Term 0.65 | ExpMove ±3.5%（近端） | Rank 93%
量化视角： IV 历史高位（Rank 93%，期权偏贵）｜期限结构倒挂（Term 0.65，近月 IV 高于远月）｜保护溢价显著（Skew 7.3pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.55）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.99×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.55×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（1D）±3.5% ｜ 11-23（4D）±5.3% ｜ 11-25（6D）±6.5% ｜ 11-27（8D）±6.9%
   ⇒ IV–VIX Spread: +54.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -145,609,252 | GEX Change vs 上次快照 -182,532,329 | Flip: Primary Flip: 152.58（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1045 / LOW 293 / INVALID 618
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 152.58（全链重定价，覆盖 100%）
Put Wall 160（弱结构｜现价低于该位 8.8%）
最近结构参考: Flip 153（现价低于该位 4.3%）
量化视角： 负 Gamma（1.46亿，无历史分位）｜由正转负（1.83亿）｜现价位于 Flip 下方 4.32%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 160（Put Wall，弱结构） / 170（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 153（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C +26.9k / P -126.7k ｜ Activity HIGH ｜ 1D
11-23  C +18.6k / P +7.7k ｜ Activity HIGH ｜ 4D
11-25  C +12.0k / P +7.5k ｜ Activity HIGH ｜ 6D
11-27  C +71.5k / P +9.9k ｜ Activity HIGH ｜ 8D

📆 11-20 Forward Structure
存量OI: C 1599.0k / P 885.4k，今日变化ΔOI: C +26.9k / P -126.7k，平值价格ATM: C $2.62 / P $2.53 ｜ ATM IV 83.1%，净 delta 敞口 15.3M shares
Top ΔOI: P 200 -31,483 ｜ P 190 -30,800
仓位参考: Max Pain 170 ｜ Call Wall 160（+9.6%，弱）（OI 48.9k） ｜ Put Wall 150（+2.8%，弱）（OI 47.6k）
量化解读： 存量 Call 重｜ATM IV 83.1%｜历史 Rank 93%（近端代理）｜IV/RV 1.68×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 15,298,226 股

📆 11-23 Forward Structure
存量OI: C 73.8k / P 42.3k，今日变化ΔOI: C +18.6k / P +7.7k，平值价格ATM: C $4.40 / P $3.30 ｜ ATM IV 62.7%，净 delta 敞口 -153k shares
Top ΔOI: C 160 +5,803 ｜ C 155 +2,390
仓位参考: Max Pain 155 ｜ Call Wall 160（+9.6%）（OI 10.1k） ｜ Put Wall 150（+2.8%，弱）（OI 6.1k）
量化解读： 存量 Call 重｜ATM IV 62.7%｜历史 Rank 93%（近端代理）｜IV/RV 1.26×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 153,021 股

📆 11-25 Forward Structure
存量OI: C 43.7k / P 19.8k，今日变化ΔOI: C +12.0k / P +7.5k，平值价格ATM: C $4.85 / P $4.70 ｜ ATM IV 64.3%，净 delta 敞口 -88k shares
Top ΔOI: P 125 +2,856 ｜ C 165 +2,451 ｜ C 160 +1,513
仓位参考: Max Pain 155 ｜ Call Wall 160（+9.6%，弱）（OI 2.9k） ｜ Put Wall 140（-4.1%，弱）（OI 2.4k）
量化解读： 存量 Call 重｜ATM IV 64.3%｜历史 Rank 93%（近端代理）｜IV/RV 1.30×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 87,732 股

📆 11-27 Forward Structure
存量OI: C 296.8k / P 173.7k，今日变化ΔOI: C +71.5k / P +9.9k，平值价格ATM: C $5.15 / P $4.95 ｜ ATM IV 58.7%，净 delta 敞口 1.6M shares
Top ΔOI: C 165 +18,880 ｜ C 157 +16,160
仓位参考: Max Pain 165 ｜ Call Wall 157.5（+7.9%，弱）（OI 17.7k） ｜ Put Wall 145（-0.7%，弱）（OI 12.5k）
量化解读： 存量 Call 重｜ATM IV 58.7%｜历史 Rank 93%（近端代理）｜IV/RV 1.18×（近似）｜净 delta 敞口 正 1,639,028 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-19/NVDA_evening.json