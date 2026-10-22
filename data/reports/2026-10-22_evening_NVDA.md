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

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-23 222C ΔOI +6,209（距现价 +4.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 217.23 → 收盘 212.21（-2.3%） ｜ 今日高 218.88 ｜ 低 211.26 ｜ 昨收 221.97 → 收盘 212.21（-4.4%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-27，窗口结束前不做对错判定）

Options: P/C成交量 0.58 | OI比 0.80 | ATM IV 45.7% | Skew 4.6pp | Term 0.94 | ExpMove ±1.9%（近端） | Rank 61%
量化视角： IV 中性（Rank 61%）｜期限结构正常（Term 0.94）｜保护溢价中性（Skew 4.6pp）｜存量 Call 偏重（OI比 0.80）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.58×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.80×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（1D）±1.9% ｜ 10-26（4D）±3.0% ｜ 10-28（6D）±4.0% ｜ 10-30（8D）±4.7%
   ⇒ IV–VIX Spread: +26.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -50,509,741 | GEX Change vs 上次快照 -165,809,733 | Flip: Primary Flip: 213.57（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 717 / LOW 213 / INVALID 528
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 213.57（全链重定价，覆盖 97%）
Call Wall 230（弱结构｜现价低于该位 7.7%）
最近结构参考: Flip 214（现价低于该位 0.6%）
量化视角： 负 Gamma（5051万，无历史分位）｜由正转负（1.66亿）｜现价位于 Flip 下方 0.64%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 220（MaxPain，仅结算参考） / 230（Call Wall，弱结构）。
• Gamma 区域：切换参考 214（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +33.4k / P +23.7k ｜ Activity HIGH ｜ 1D
10-26  C +2.8k / P +5.3k ｜ Activity HIGH ｜ 4D
10-28  C +5.4k / P +4.7k ｜ Activity HIGH ｜ 6D
10-30  C +14.5k / P +24.1k ｜ Activity HIGH ｜ 8D

📆 10-23 Forward Structure
存量OI: C 475.1k / P 379.1k，今日变化ΔOI: C +33.4k / P +23.7k，平值价格ATM: C $2.01 / P $2.12 ｜ ATM IV 45.7%，净 delta 敞口 -449k shares
Top ΔOI: C 222 +6,209 ｜ C 227 +5,638
仓位参考: Max Pain 220 ｜ Call Wall 230（+8.4%，弱）（OI 58.5k） ｜ Put Wall 210（-1.0%，弱）（OI 18.2k）
量化解读： 存量 Call 重｜ATM IV 45.7%｜历史 Rank 61%（近端代理）｜IV/RV 1.89×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 449,340 股

📆 10-26 Forward Structure
存量OI: C 42.5k / P 37.3k，今日变化ΔOI: C +2.8k / P +5.3k，平值价格ATM: C $3.05 / P $3.25 ｜ ATM IV 34.7%，净 delta 敞口 -107k shares
Top ΔOI: C 225 +1,255
仓位参考: Max Pain 218 ｜ Call Wall 230（+8.4%，弱）（OI 5.6k） ｜ Put Wall 200（-5.8%）（OI 8.0k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 34.7%｜历史 Rank 61%（近端代理）｜IV/RV 1.43×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 107,370 股

📆 10-28 Forward Structure
存量OI: C 18.9k / P 17.1k，今日变化ΔOI: C +5.4k / P +4.7k，平值价格ATM: C $4.15 / P $4.24 ｜ ATM IV 38.7%，净 delta 敞口 -169k shares
Top ΔOI: P 215 +1,576 ｜ C 232 +985
仓位参考: Max Pain 218 ｜ Call Wall 230（+8.4%）（OI 5.5k） ｜ Put Wall 215（+1.3%）（OI 3.4k）
量化解读： 存量两侧均衡｜ATM IV 38.7%｜历史 Rank 61%（近端代理）｜IV/RV 1.60×（近似）｜净 delta 敞口 负 168,778 股

📆 10-30 Forward Structure
存量OI: C 209.3k / P 193.5k，今日变化ΔOI: C +14.5k / P +24.1k，平值价格ATM: C $5.00 / P $5.05 ｜ ATM IV 39.9%，净 delta 敞口 -553k shares
Top ΔOI: P 210 +5,680 ｜ P 197 +5,342
仓位参考: Max Pain 222 ｜ Call Wall 230（+8.4%，弱）（OI 18.7k） ｜ Put Wall 210（-1.0%，弱）（OI 16.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 39.9%｜历史 Rank 61%（近端代理）｜IV/RV 1.65×（近似）｜净 delta 敞口 负 553,289 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=61 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=61）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-22/NVDA_evening.json