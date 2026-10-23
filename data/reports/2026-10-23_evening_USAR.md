# 期权晚报 2026-10-23（快照 16:40 ET）

📊 市场环境

SPY $759.97 ｜ QQQ $704.40
VIX 19.45 ↑2.2%（5D -2.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 21.0（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-23

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-30 9P ΔOI +2,966（距现价 -3.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-30 9P ΔOI +2,966 占该期限总 OI 10.5%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 9.54 → 收盘 9.33（-2.2%） ｜ 今日高 9.58 ｜ 低 9.26 ｜ 昨收 9.63 → 收盘 9.33（-3.1%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-28，窗口结束前不做对错判定）

Options: P/C成交量 0.54 | OI比 0.18 | ATM IV 98.9% | Skew 47.7pp | Term 0.91 | ExpMove ±8.5%（近端） | Rank 29%
量化视角： IV 中性（Rank 29%）｜期限结构正常（Term 0.91）｜保护溢价显著（Skew 47.7pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.18）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.54×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.18×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（7D）±8.5% ｜ 11-06（14D）±13.7% ｜ 11-13（21D）±17.7% ｜ 11-20（28D）±19.5%
   ⇒ IV–VIX Spread: +79.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,831,309 | GEX Change vs 上次快照 -2,375,413 | Flip: Primary Flip: 9.92（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 201 / LOW 66 / INVALID 173
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 9.92（全链重定价，覆盖 91%）
Put Wall 10（现价低于该位 6.7%）
最近结构参考: Flip 10（现价低于该位 6.0%）
量化视角： 负 Gamma（183万，无历史分位）｜由正转负（238万）｜现价位于 Flip 下方 5.99%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 10（Put Wall） / 10（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 10（全链重定价，覆盖 91%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-30  C +0.5k / P -0.2k ｜ Activity MEDIUM △ ｜ 7D
11-06  C +0.3k / P -99 ｜ Activity HIGH ｜ 14D
11-13  C +0.2k / P -0.8k ｜ Activity HIGH ｜ 21D
11-20  C +0.6k / P +0.9k ｜ Activity HIGH ｜ 28D

📆 10-30 Forward Structure
存量OI: C 19.4k / P 8.8k，今日变化ΔOI: C +0.5k / P -0.2k，平值价格ATM: C $0.38 / P $0.41 ｜ ATM IV 76.5%，净 delta 敞口 256k shares
Top ΔOI: P 9 +2,966 ｜ P 14 -2,090 ｜ P 13 -523
仓位参考: Max Pain 11 ｜ Call Wall 10（+7.2%，弱）（OI 0.9k） ｜ Put Wall 9（-3.5%）（OI 3.6k）
量化解读： 存量 Call 重｜ATM IV 76.5%｜历史 Rank 29%（近端代理）｜IV/RV 1.34×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 255,705 股

📆 11-06 Forward Structure
存量OI: C 5.2k / P 4.3k，今日变化ΔOI: C +0.3k / P -99，平值价格ATM: C $0.59 / P $0.69 ｜ ATM IV 86.8%，净 delta 敞口 26k shares
Top ΔOI: C 10 +104 ｜ P 15 -98 ｜ C 9 +52
仓位参考: Max Pain 12 ｜ Put Wall 9（-3.5%）（OI 1.5k）
量化解读： 存量 Call 重｜ATM IV 86.8%｜历史 Rank 29%（近端代理）｜IV/RV 1.52×（近似）｜净 delta 敞口 正 25,937 股

📆 11-13 Forward Structure
存量OI: C 2.7k / P 2.6k，今日变化ΔOI: C +0.2k / P -0.8k，平值价格ATM: C $0.76 / P $0.89 ｜ ATM IV 89.1%，净 delta 敞口 87k shares
Top ΔOI: P 16 -505 ｜ P 17 -296
仓位参考: Max Pain 12 ｜ Call Wall 10（+7.2%，弱）（OI 94） ｜ Put Wall 10（+7.2%，弱）（OI 0.1k）
量化解读： 存量两侧均衡｜ATM IV 89.1%｜历史 Rank 29%（近端代理）｜IV/RV 1.56×（近似）｜净 delta 敞口 正 86,822 股

📆 11-20 Forward Structure
存量OI: C 24.0k / P 26.4k，今日变化ΔOI: C +0.6k / P +0.9k，平值价格ATM: C $0.89 / P $0.93 ｜ ATM IV 89.9%，净 delta 敞口 -9k shares
Top ΔOI: P 10 +451
仓位参考: Max Pain 14 ｜ Put Wall 10（+7.2%，弱）（OI 8.2k）
量化解读： 存量两侧均衡｜ATM IV 89.9%｜历史 Rank 29%（近端代理）｜IV/RV 1.58×（近似）｜净 delta 敞口 负 9,181 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=61 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=61）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-23/USAR_evening.json