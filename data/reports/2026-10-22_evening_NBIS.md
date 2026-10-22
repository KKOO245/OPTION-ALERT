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
🟡 **近现价集中开仓**: 10-23 162P ΔOI +1,092（距现价 +2.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 164.89 → 收盘 159.17（-3.5%） ｜ 今日高 167.50 ｜ 低 155.73 ｜ 昨收 171.57 → 收盘 159.17（-7.2%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-27，窗口结束前不做对错判定）

Options: P/C成交量 0.97 | OI比 0.59 | ATM IV 117.7% | Skew 0.5pp | Term 0.87 | ExpMove ±5.0%（近端） | Rank 70%
量化视角： IV 中性（Rank 70%）｜期限结构倒挂（Term 0.87，近月 IV 高于远月）｜保护溢价薄（Skew 0.5pp）｜存量 Call 偏重（OI比 0.59）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.97×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.59×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（1D）±5.0% ｜ 10-30（8D）±11.9% ｜ 11-06（15D）±16.3% ｜ 11-13（22D）±21.5%
   ⇒ IV–VIX Spread: +98.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -17,556,112 | GEX Change vs 上次快照 -1,416,901 | Flip: Primary Flip: 172.78（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 592 / LOW 73 / INVALID 147
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 172.78（全链重定价，覆盖 100%）
Put Wall 150（弱结构｜现价高于该位 6.1%）
最近结构参考: Put Wall 150（现价高于该位 6.1%）
量化视角： 负 Gamma（1756万，无历史分位）｜负 Gamma 加深（142万）｜现价位于 Flip 下方 7.88%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（Put Wall，弱结构）；上方 180（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 173（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +2.1k / P -2.2k ｜ Activity MEDIUM △ ｜ 1D
10-30  C +5.0k / P +3.1k ｜ Activity HIGH ｜ 8D
11-06  C +1.5k / P +0.4k ｜ Activity HIGH ｜ 15D
11-13  C +1.0k / P +0.8k ｜ Activity HIGH ｜ 22D

📆 10-23 Forward Structure
存量OI: C 107.6k / P 63.0k，今日变化ΔOI: C +2.1k / P -2.2k，平值价格ATM: C $3.63 / P $4.25 ｜ ATM IV 117.7%，净 delta 敞口 384k shares
Top ΔOI: P 225 -1,942 ｜ P 162 +1,092 ｜ P 220 -992
仓位参考: Max Pain 180 ｜ Call Wall 175（+9.9%，弱）（OI 2.9k） ｜ Put Wall 165（+3.7%，弱）（OI 4.8k）
量化解读： 存量 Call 重｜ATM IV 117.7%｜历史 Rank 70%（近端代理）｜IV/RV 1.51×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 384,056 股

📆 10-30 Forward Structure
存量OI: C 54.8k / P 42.2k，今日变化ΔOI: C +5.0k / P +3.1k，平值价格ATM: C $9.18 / P $9.72 ｜ ATM IV 100.5%，净 delta 敞口 -50k shares
Top ΔOI: C 190 +1,494 ｜ P 150 +565
仓位参考: Max Pain 200 ｜ Call Wall 175（+9.9%，弱）（OI 1.5k） ｜ Put Wall 165（+3.7%，弱）（OI 2.2k）
量化解读： 存量 Call 重｜ATM IV 100.5%｜历史 Rank 70%（近端代理）｜IV/RV 1.29×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 49,959 股

📆 11-06 Forward Structure
存量OI: C 32.7k / P 17.6k，今日变化ΔOI: C +1.5k / P +0.4k，平值价格ATM: C $12.55 / P $13.40 ｜ ATM IV 98.6%，净 delta 敞口 7k shares
Top ΔOI: C 175 +146
仓位参考: Max Pain 205 ｜ Put Wall 170（+6.8%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 98.6%｜历史 Rank 70%（近端代理）｜IV/RV 1.26×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 6,595 股

📆 11-13 Forward Structure
存量OI: C 13.3k / P 16.5k，今日变化ΔOI: C +1.0k / P +0.8k，平值价格ATM: C $16.54 / P $17.65 ｜ ATM IV 106.4%，净 delta 敞口 16k shares
Top ΔOI: P 175 +236 ｜ P 215 -157
仓位参考: Max Pain 200 ｜ Call Wall 170（+6.8%，弱）（OI 0.4k） ｜ Put Wall 165（+3.7%，弱）（OI 1.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 106.4%｜历史 Rank 70%（近端代理）｜IV/RV 1.36×（近似）｜净 delta 敞口 正 15,658 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=61 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=61）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-22/NBIS_evening.json