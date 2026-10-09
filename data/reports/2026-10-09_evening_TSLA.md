# 期权晚报 2026-10-09（快照 16:40 ET）

📊 市场环境

SPY $778.57 ｜ QQQ $751.27
VIX 14.84 ↓3.7%（5D -3.1%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 45.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-09

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 46.3 ｜ 前值 48.1　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-12 370P ΔOI +1,744（距现价 -3.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 382.38 → 收盘 382.70（+0.1%） ｜ 今日高 388.56 ｜ 低 379.71 ｜ 昨收 375.00 → 收盘 382.70（+2.1%）
Target 等待验证: 3D_mdd >= 0.03（3D） — PENDING（评估日 ≈ 2026-10-14，窗口结束前不做对错判定）

Options: P/C成交量 0.61 | OI比 1.16 | ATM IV 19.6% | Skew -1.5pp | Term 2.20 | ExpMove ±1.6%（近端） | Rank 20%
量化视角： IV 历史低位（Rank 20%，期权偏便宜）｜期限结构正常偏陡（Term 2.20）｜Put 保护异常便宜（Skew -1.5pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.61×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.16×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-12（3D）±1.6% ｜ 10-14（5D）±2.9% ｜ 10-16（7D）±4.1% ｜ 10-19（10D）±4.5%
   ⇒ IV–VIX Spread: +4.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 183,312,333 | GEX Change vs 上次快照 -2,936,218 | Flip: Primary Flip: 361.21（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 87%（带内） ｜ IV 有效性: VALID 1044 / LOW 126 / INVALID 554
结构观察区: Primary Flip 361.21（全链重定价，覆盖 87%）
Call Wall 400（现价低于该位 4.3%）
最近结构参考: Call Wall 400（现价低于该位 4.3%）
量化视角： 正 Gamma（1.83亿，无历史分位）｜正 Gamma 减弱（294万）｜现价位于 Flip 上方 5.95%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 370（MaxPain，仅结算参考）；上方 400（Call Wall）。
• Gamma 区域：切换参考 361（全链重定价，覆盖 87%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-12  C +8.8k / P +5.3k ｜ Activity HIGH ｜ 3D
10-14  C +3.3k / P +3.1k ｜ Activity HIGH ｜ 5D
10-16  C +20.6k / P +4.4k ｜ Activity HIGH ｜ 7D
10-19  C +1.9k / P +1.2k ｜ Activity HIGH ｜ 10D

📆 10-12 Forward Structure
存量OI: C 31.7k / P 28.0k，今日变化ΔOI: C +8.8k / P +5.3k，平值价格ATM: C $3.25 / P $3.05 ｜ ATM IV 23.1%，净 delta 敞口 369k shares
Top ΔOI: P 370 +1,744 ｜ C 397 +1,640 ｜ C 372 +1,521
仓位参考: Max Pain 370 ｜ Call Wall 400（+4.5%，弱）（OI 3.1k） ｜ Put Wall 370（-3.3%，弱）（OI 3.1k）
量化解读： 存量两侧均衡｜ATM IV 23.1%｜历史 Rank 20%（近端代理）｜IV/RV 0.81×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 368,565 股

📆 10-14 Forward Structure
存量OI: C 11.6k / P 9.8k，今日变化ΔOI: C +3.3k / P +3.1k，平值价格ATM: C $5.70 / P $5.40 ｜ ATM IV 31.0%，净 delta 敞口 145k shares
Top ΔOI: C 375 +1,082 ｜ P 360 +472 ｜ P 350 +447
仓位参考: Max Pain 370 ｜ Call Wall 400（+4.5%，弱）（OI 1.7k） ｜ Put Wall 360（-5.9%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 31.0%｜历史 Rank 20%（近端代理）｜IV/RV 1.08×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 145,305 股

📆 10-16 Forward Structure
存量OI: C 336.4k / P 294.5k，今日变化ΔOI: C +20.6k / P +4.4k，平值价格ATM: C $8.15 / P $7.65 ｜ ATM IV 37.3%，净 delta 敞口 676k shares
Top ΔOI: C 400 +7,984 ｜ C 377 +3,292 ｜ C 390 +2,980
仓位参考: Max Pain 370 ｜ Call Wall 400（+4.5%）（OI 31.3k） ｜ Put Wall 380（-0.7%，弱）（OI 14.6k）
量化解读： 存量两侧均衡｜ATM IV 37.3%｜历史 Rank 20%（近端代理）｜IV/RV 1.30×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 675,634 股

📆 10-19 Forward Structure
存量OI: C 6.7k / P 3.1k，今日变化ΔOI: C +1.9k / P +1.2k，平值价格ATM: C $8.95 / P $8.30 ｜ ATM IV 34.3%，净 delta 敞口 62k shares
Top ΔOI: P 360 +266 ｜ C 375 +252 ｜ C 372 +219
仓位参考: Max Pain 375 ｜ Call Wall 400（+4.5%）（OI 1.7k） ｜ Put Wall 360（-5.9%）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 34.3%｜历史 Rank 20%（近端代理）｜IV/RV 1.20×（近似）｜净 delta 敞口 正 62,350 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-09/TSLA_evening.json