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
🟡 **近现价集中开仓**: 10-26 385C ΔOI +2,560（距现价 +3.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-02 455C ΔOI +7,079 占该期限总 OI 36.5%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 373.14 → 收盘 372.22（-0.2%） ｜ 今日高 377.28 ｜ 低 365.27 ｜ 昨收 374.58 → 收盘 372.22（-0.6%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.06 | OI比 1.02 | ATM IV 34.0% | Skew 0.1pp | Term 1.16 | ExpMove ±2.1%（近端） | Rank 6%
量化视角： IV 历史低位（Rank 6%，期权偏便宜）｜期限结构正常偏陡（Term 1.16）｜保护溢价薄（Skew 0.1pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.06×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.02×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-26（3D）±2.1% ｜ 10-28（5D）±3.4% ｜ 10-30（7D）±4.4% ｜ 11-02（10D）±4.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 52,464,559 | GEX Change vs 上次快照 36,702,242 | Flip: Primary Flip: 359.31（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 80%（带内） ｜ IV 有效性: VALID 1252 / LOW 157 / INVALID 773
结构观察区: Primary Flip 359.31（全链重定价，覆盖 80%）
Call Wall 400（现价低于该位 6.9%）
最近结构参考: Flip 359（现价高于该位 3.6%）
量化视角： 正 Gamma（5246万，无历史分位）｜正 Gamma 增强（+3670万）｜现价位于 Flip 上方 3.59%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 370（MaxPain，仅结算参考）；上方 400（Call Wall）。
• Gamma 区域：切换参考 359（全链重定价，覆盖 80%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-26  C +18.9k / P +6.9k ｜ Activity HIGH ｜ 3D
10-28  C +5.4k / P +5.6k ｜ Activity HIGH ｜ 5D
10-30  C +24.8k / P +17.5k ｜ Activity HIGH ｜ 7D
11-02  C +10.0k / P +1.6k ｜ Activity HIGH ｜ 10D

📆 10-26 Forward Structure
存量OI: C 68.9k / P 36.5k，今日变化ΔOI: C +18.9k / P +6.9k，平值价格ATM: C $3.81 / P $4.03 ｜ ATM IV 29.1%，净 delta 敞口 -152k shares
Top ΔOI: C 385 +2,560
仓位参考: Max Pain 375 ｜ Put Wall 365（-1.9%，弱）（OI 2.6k）
量化解读： 存量 Call 重｜ATM IV 29.1%｜历史 Rank 6%（近端代理）｜IV/RV 0.90×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 152,466 股

📆 10-28 Forward Structure
存量OI: C 14.8k / P 16.2k，今日变化ΔOI: C +5.4k / P +5.6k，平值价格ATM: C $6.25 / P $6.40 ｜ ATM IV 37.0%，净 delta 敞口 -153k shares
Top ΔOI: P 385 +1,160 ｜ C 387 +906 ｜ P 382 +611
仓位参考: Max Pain 380 ｜ Call Wall 400（+7.5%，弱）（OI 1.4k） ｜ Put Wall 350（-6.0%，弱）（OI 1.8k）
量化解读： 存量两侧均衡｜ATM IV 37.0%｜历史 Rank 6%（近端代理）｜IV/RV 1.14×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 153,002 股

📆 10-30 Forward Structure
存量OI: C 107.5k / P 113.1k，今日变化ΔOI: C +24.8k / P +17.5k，平值价格ATM: C $8.10 / P $8.15 ｜ ATM IV 39.5%，净 delta 敞口 64k shares
Top ΔOI: C 420 +5,004 ｜ C 395 +3,491
仓位参考: Max Pain 372 ｜ Call Wall 400（+7.5%，弱）（OI 10.4k） ｜ Put Wall 340（-8.7%，弱）（OI 4.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 39.5%｜历史 Rank 6%（近端代理）｜IV/RV 1.22×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 63,964 股

📆 11-02 Forward Structure
存量OI: C 13.2k / P 6.1k，今日变化ΔOI: C +10.0k / P +1.6k，平值价格ATM: C $9.15 / P $8.90 ｜ ATM IV 36.8%，净 delta 敞口 -32k shares
Top ΔOI: C 455 +7,079 ｜ P 380 +493
仓位参考: Max Pain 380 ｜ Put Wall 380（+2.1%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 36.8%｜历史 Rank 6%（近端代理）｜IV/RV 1.13×（近似）｜净 delta 敞口 负 31,700 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-23/TSLA_evening.json