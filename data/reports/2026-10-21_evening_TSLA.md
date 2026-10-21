# 期权晚报 2026-10-21（快照 16:40 ET）

📊 市场环境

SPY $773.09 ｜ QQQ $725.20
VIX 16.68 ↓3.6%（5D -1.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.4（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 381.51 → 收盘 386.47（+1.3%） ｜ 今日高 388.84 ｜ 低 380.51 ｜ 昨收 373.71 → 收盘 386.47（+3.4%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-28，窗口结束前不做对错判定）

Options: P/C成交量 0.71 | OI比 0.95 | ATM IV 93.6% | Skew 1.6pp | Term 0.46 | ExpMove ±5.6%（近端） | Rank 95%
量化视角： IV 历史高位（Rank 95%，期权偏贵）｜期限结构倒挂（Term 0.46，近月 IV 高于远月）｜保护溢价薄（Skew 1.6pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.71×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.95×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（2D）±5.6% ｜ 10-26（5D）±5.9% ｜ 10-28（7D）±6.5% ｜ 10-30（9D）±6.9%
   ⇒ IV–VIX Spread: +76.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 96,527,963 | GEX Change vs 上次快照 3,246,629 | Flip: Primary Flip: 354.24（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1245 / LOW 125 / INVALID 720
结构观察区: Primary Flip 354.24（全链重定价，覆盖 100%）
Call Wall 400（现价低于该位 3.4%）
最近结构参考: Call Wall 400（现价低于该位 3.4%）
量化视角： 正 Gamma（9653万，无历史分位）｜正 Gamma 增强（+325万）｜现价位于 Flip 上方 9.10%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 365（MaxPain，仅结算参考）；上方 400（Call Wall）。
• Gamma 区域：切换参考 354（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +26.9k / P +36.2k ｜ Activity HIGH ｜ 2D
10-26  C +12.7k / P +6.1k ｜ Activity HIGH ｜ 5D
10-28  C +1.4k / P +1.7k ｜ Activity HIGH ｜ 7D
10-30  C +4.7k / P +10.1k ｜ Activity HIGH ｜ 9D

📆 10-23 Forward Structure
存量OI: C 237.0k / P 225.7k，今日变化ΔOI: C +26.9k / P +36.2k，平值价格ATM: C $10.25 / P $11.26 ｜ ATM IV 93.6%，净 delta 敞口 431k shares
Top ΔOI: C 410 +5,028
仓位参考: Max Pain 365 ｜ Call Wall 400（+3.5%，弱）（OI 16.1k） ｜ Put Wall 350（-9.4%，弱）（OI 6.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 93.6%｜历史 Rank 95%（近端代理）｜IV/RV 3.29×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 431,485 股

📆 10-26 Forward Structure
存量OI: C 34.4k / P 18.6k，今日变化ΔOI: C +12.7k / P +6.1k，平值价格ATM: C $11.20 / P $11.75 ｜ ATM IV 63.1%，净 delta 敞口 154k shares
Top ΔOI: C 455 +4,111 ｜ P 350 +1,340
仓位参考: Max Pain 368 ｜ Put Wall 350（-9.4%）（OI 2.2k）
量化解读： 存量 Call 重｜ATM IV 63.1%｜历史 Rank 95%（近端代理）｜IV/RV 2.22×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 153,993 股

📆 10-28 Forward Structure
存量OI: C 7.6k / P 8.0k，今日变化ΔOI: C +1.4k / P +1.7k，平值价格ATM: C $12.02 / P $12.90 ｜ ATM IV 57.9%，净 delta 敞口 38k shares
Top ΔOI: P 350 +157
仓位参考: Max Pain 368 ｜ Call Wall 420（+8.7%，弱）（OI 1.1k） ｜ Put Wall 350（-9.4%）（OI 1.6k）
量化解读： 存量两侧均衡｜ATM IV 57.9%｜历史 Rank 95%（近端代理）｜IV/RV 2.03×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 37,793 股

📆 10-30 Forward Structure
存量OI: C 78.6k / P 75.1k，今日变化ΔOI: C +4.7k / P +10.1k，平值价格ATM: C $13.00 / P $13.50 ｜ ATM IV 54.3%，净 delta 敞口 123k shares
Top ΔOI: C 420 +1,564
仓位参考: Max Pain 370 ｜ Call Wall 400（+3.5%）（OI 9.7k） ｜ Put Wall 350（-9.4%，弱）（OI 3.5k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 54.3%｜历史 Rank 95%（近端代理）｜IV/RV 1.91×（近似）｜净 delta 敞口 正 123,007 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-21/TSLA_evening.json