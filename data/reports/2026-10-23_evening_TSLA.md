# 期权晚报 2026-10-23（快照 21:00 ET）

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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 373.14 → 收盘 372.22（-0.2%） ｜ 今日高 377.30 ｜ 低 365.27 ｜ 昨收 374.58 → 收盘 372.22（-0.6%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.92 | OI比 0.53 | ATM IV 29.1% | Skew 1.4pp | Term 1.36 | ExpMove ±2.1%（近端） | Rank 3%
量化视角： IV 历史低位（Rank 3%，期权偏便宜）｜期限结构正常偏陡（Term 1.36）｜保护溢价薄（Skew 1.4pp）｜存量 Call 偏重（OI比 0.53）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.92×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.53×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-26（3D）±2.1% ｜ 10-28（5D）±3.4% ｜ 10-30（7D）±4.4% ｜ 11-02（10D）±4.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 15,558,835 | GEX Change vs 上次快照 -203,482 | Flip: Primary Flip: 368.20（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1232 / LOW 98 / INVALID 554
结构观察区: Primary Flip 368.20（全链重定价，覆盖 99%）
Call Wall 400（弱结构｜现价低于该位 6.9%）
最近结构参考: Flip 368（现价高于该位 1.1%）
量化视角： 正 Gamma（1556万，无历史分位）｜正 Gamma 减弱（20万）｜现价位于 Flip 上方 1.09%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 375（MaxPain，仅结算参考） / 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 368（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-26  C +0 / P +0 ｜ Activity LOW ｜ 3D
10-28  C +0 / P +0 ｜ Activity LOW ｜ 5D
10-30  C +0 / P +0 ｜ Activity LOW ｜ 7D
11-02  C +0 / P +0 ｜ Activity LOW ｜ 10D

📆 10-26 Forward Structure
存量OI: C 68.9k / P 36.5k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $3.81 / P $4.03 ｜ ATM IV 29.1%，净 delta 敞口 0 shares
仓位参考: Max Pain 375 ｜ Put Wall 365（-1.9%，弱）（OI 2.6k）
量化解读： 存量 Call 重｜ATM IV 29.1%｜历史 Rank 3%（近端代理）｜IV/RV 0.90×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

10-28（Activity LOW）仓位参考: Max Pain 380 ｜ Call Wall 400（+7.5%，弱）（OI 1.4k） ｜ Put Wall 350（-6.0%，弱）（OI 1.8k）

10-30（Activity LOW）仓位参考: Max Pain 372 ｜ Call Wall 400（+7.5%，弱）（OI 10.4k） ｜ Put Wall 340（-8.7%，弱）（OI 4.3k）

11-02（Activity LOW）仓位参考: Max Pain 380 ｜ Put Wall 380（+2.1%，弱）（OI 0.6k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-23/TSLA_evening.json