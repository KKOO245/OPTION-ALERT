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
🟡 **近现价集中开仓**: 10-16 420C ΔOI -59（距现价 -0.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 416.39 → 收盘 423.96（+1.8%） ｜ 今日高 427.53 ｜ 低 415.86 ｜ 昨收 415.41 → 收盘 423.96（+2.1%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-16，窗口结束前不做对错判定）

Options: P/C成交量 0.17 | OI比 0.51 | ATM IV 114.3% | Skew -5.8pp | Term 0.41 | ExpMove ±3.4%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.41，近月 IV 高于远月）｜Put 保护异常便宜（Skew -5.8pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.51）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.17×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.51×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（7D）±3.4% ｜ 10-23（14D）±8.6% ｜ 10-30（21D）±9.5% ｜ 11-06（28D）±10.5%
   ⇒ IV–VIX Spread: +99.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 3,290,873 | GEX Change vs 上次快照 -868,113 | Flip: Primary Flip: 394.56（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 83%（带内） ｜ IV 有效性: VALID 260 / LOW 132 / INVALID 472
结构观察区: Primary Flip 394.56（全链重定价，覆盖 83%）
Call Wall 420（弱结构｜现价高于该位 0.9%）
最近结构参考: Call Wall 420（现价高于该位 0.9%）
量化视角： 正 Gamma（329万，无历史分位）｜正 Gamma 减弱（87万）｜现价位于 Flip 上方 7.45%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 395（MaxPain，仅结算参考） / 420（Call Wall，弱结构）。
• Gamma 区域：切换参考 395（全链重定价，覆盖 83%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +60 / P +33 ｜ Activity LOW ｜ 7D
10-23  C +25 / P +12 ｜ Activity LOW ｜ 14D
10-30  C +18 / P +51 ｜ Activity HIGH ｜ 21D
11-06  C +4 / P +3 ｜ Activity LOW ｜ 28D

📆 10-16 Forward Structure
存量OI: C 10.8k / P 10.6k，今日变化ΔOI: C +60 / P +33，平值价格ATM: C $7.23 / P $7.30 ｜ ATM IV 29.7%，净 delta 敞口 -1k shares
Top ΔOI: C 420 -59 ｜ C 435 +44
仓位参考: Max Pain 390 ｜ Call Wall 400（-5.7%，弱）（OI 0.9k） ｜ Put Wall 400（-5.7%，弱）（OI 0.5k）
量化解读： 存量两侧均衡｜ATM IV 29.7%｜历史 Rank 100%（近端代理）｜IV/RV 1.22×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 1,471 股

10-23（Activity LOW）仓位参考: Max Pain 415 ｜ Call Wall 425（+0.2%）（OI 0.5k） ｜ Put Wall 415（-2.1%）（OI 0.5k）

📆 10-30 Forward Structure
存量OI: C 0.8k / P 0.6k，今日变化ΔOI: C +18 / P +51，平值价格ATM: C $20.56 / P $19.70 ｜ ATM IV 48.6%，净 delta 敞口 178 shares
仓位参考: Max Pain 395 ｜ Call Wall 460（+8.5%，弱）（OI 94） ｜ Put Wall 400（-5.7%，弱）（OI 45）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 48.6%｜历史 Rank 100%（近端代理）｜IV/RV 2.00×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 178 股

11-06（Activity LOW）仓位参考: Max Pain 400 ｜ Call Wall 455（+7.3%，弱）（OI 49） ｜ Put Wall 400（-5.7%，弱）（OI 35）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-09/ISRG_evening.json