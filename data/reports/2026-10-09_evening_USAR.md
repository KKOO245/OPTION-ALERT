# 期权晚报 2026-10-09（快照 21:00 ET）

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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 12.67 → 收盘 12.56（-0.9%） ｜ 今日高 12.79 ｜ 低 12.40 ｜ 昨收 12.63 → 收盘 12.56（-0.6%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-14，窗口结束前不做对错判定）

Options: P/C成交量 0.76 | OI比 0.32 | ATM IV 58.2% | Skew -4.7pp | Term 1.20 | ExpMove ±6.8%（近端） | Rank 50%
量化视角： IV 中性（Rank 50%）｜期限结构正常偏陡（Term 1.20）｜Put 保护异常便宜（Skew -4.7pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.32）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.76×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.32×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（7D）±6.8% ｜ 10-23（14D）±9.5% ｜ 10-30（21D）±12.3% ｜ 11-06（28D）±15.3%
   ⇒ IV–VIX Spread: +43.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,991,186 | GEX Change vs 上次快照 -3,992,178 | Flip: Primary Flip: 13.97（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 160 / LOW 59 / INVALID 103
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 13.97（全链重定价，覆盖 100%）
最近结构参考: Flip 14（现价低于该位 10.1%）
量化视角： 负 Gamma（199万，无历史分位）｜由正转负（399万）｜现价位于 Flip 下方 10.12%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 15（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 14（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +0 / P +0 ｜ Activity LOW ｜ 7D
10-23  C +0 / P +0 ｜ Activity LOW ｜ 14D
10-30  C +0 / P +0 ｜ Activity LOW ｜ 21D
11-06  C +0 / P +0 ｜ Activity LOW ｜ 28D

📆 10-16 Forward Structure
存量OI: C 51.1k / P 16.3k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $0.47 / P $0.38 ｜ ATM IV 58.2%，净 delta 敞口 0 shares
仓位参考: Max Pain 15 ｜ Put Wall 13（+3.5%，弱）（OI 1.7k）
量化解读： 存量 Call 重｜ATM IV 58.2%｜历史 Rank 50%（近端代理）｜IV/RV 1.10×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

10-23（Activity LOW）仓位参考: Max Pain 15 ｜ Put Wall 13.5（+7.5%，弱）（OI 0.5k）

10-30（Activity LOW）仓位参考: Max Pain 16 ｜ Call Wall 13.5（+7.5%，弱）（OI 0.2k） ｜ Put Wall 12.5（-0.5%，弱）（OI 1.2k）

11-06（Activity LOW）仓位参考: Max Pain 16 ｜ Call Wall 13.5（+7.5%，弱）（OI 0.2k） ｜ Put Wall 13（+3.5%，弱）（OI 0.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=43 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=43）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-09/USAR_evening.json