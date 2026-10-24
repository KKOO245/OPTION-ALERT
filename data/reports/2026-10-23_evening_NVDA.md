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

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 210.94 → 收盘 210.96（+0.0%） ｜ 今日高 213.85 ｜ 低 210.18 ｜ 昨收 212.21 → 收盘 210.96（-0.6%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.70 | OI比 0.74 | ATM IV 29.2% | Skew 3.5pp | Term 1.50 | ExpMove ±2.2%（近端） | Rank 7%
量化视角： IV 历史低位（Rank 7%，期权偏便宜）｜期限结构正常偏陡（Term 1.50）｜保护溢价中性（Skew 3.5pp）｜存量 Call 偏重（OI比 0.74）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.70×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.74×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-26（3D）±2.2% ｜ 10-28（5D）±3.5% ｜ 10-30（7D）±4.3% ｜ 11-02（10D）±4.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -6,137,547 | GEX Change vs 上次快照 -120,877,676 | Flip: Primary Flip: 211.26（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 686 / LOW 179 / INVALID 415
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 211.26（全链重定价，覆盖 99%）
Put Wall 200（弱结构｜现价高于该位 5.5%） | Call Wall 230（弱结构｜现价低于该位 8.3%）
最近结构参考: Flip 211（现价低于该位 0.1%）
量化视角： 负 Gamma（614万，无历史分位）｜由正转负（1.21亿）｜现价位于 Flip 下方 0.14%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall，弱结构）；上方 215（MaxPain，仅结算参考） / 230（Call Wall，弱结构）。
• Gamma 区域：切换参考 211（全链重定价，覆盖 99%）。
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
存量OI: C 61.5k / P 45.6k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $2.79 / P $1.77 ｜ ATM IV 29.2%，净 delta 敞口 0 shares
仓位参考: Max Pain 215 ｜ Call Wall 225（+6.7%，弱）（OI 7.0k） ｜ Put Wall 200（-5.2%）（OI 10.1k）
量化解读： 存量 Call 重｜ATM IV 29.2%｜历史 Rank 7%（近端代理）｜IV/RV 1.02×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

10-28（Activity LOW）仓位参考: Max Pain 215 ｜ Call Wall 230（+9.0%，弱）（OI 5.9k） ｜ Put Wall 215（+1.9%）（OI 3.5k）

10-30（Activity LOW）仓位参考: Max Pain 218 ｜ Call Wall 225（+6.7%，弱）（OI 32.3k） ｜ Put Wall 210（-0.5%，弱）（OI 19.1k）

11-02（Activity LOW）仓位参考: Max Pain 212 ｜ Call Wall 230（+9.0%，弱）（OI 2.0k） ｜ Put Wall 200（-5.2%，弱）（OI 0.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-23/NVDA_evening.json