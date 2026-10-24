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


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 702.10 → 收盘 704.40（+0.3%） ｜ 今日高 709.30 ｜ 低 701.16 ｜ 昨收 704.47 → 收盘 704.40（-0.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.06 | OI比 1.93 | ATM IV 19.2% | Skew 4.0pp | Term 1.30 | ExpMove ±1.4%（近端） | Rank 55%
量化视角： IV 中性（Rank 55%）｜期限结构正常偏陡（Term 1.30）｜保护溢价中性（Skew 4.0pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.06×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.93×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 8% ｜ P/C OI(近端) 73%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 8%）｜近端持仓结构中性（P/C OI 分位 73%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-26（3D）±1.4% ｜ 10-27（4D）±1.9% ｜ 10-28（5D）±2.4% ｜ 10-29（6D）±2.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -892,697,791 | GEX Change vs 上次快照 96,407,930 | Flip: Primary Flip: 730.51（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 2933 / LOW 213 / INVALID 1214
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 730.51（全链重定价，覆盖 99%）
Put Wall 690（弱结构｜现价高于该位 2.1%）
最近结构参考: Put Wall 690（现价高于该位 2.1%）
量化视角： 负 Gamma（8.93亿，历史分位偏负区，比 92% 的交易日更负）｜负 Gamma 缓解（+9641万）｜现价位于 Flip 下方 3.57%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 690（Put Wall，弱结构）；上方 721（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 731（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-26  C +0 / P +0 ｜ Activity LOW ｜ 3D
10-27  C +0 / P +0 ｜ Activity LOW ｜ 4D
10-28  C +0 / P +0 ｜ Activity LOW ｜ 5D
10-29  C +0 / P +0 ｜ Activity LOW ｜ 6D

📆 10-26 Forward Structure
存量OI: C 69.0k / P 133.5k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $5.62 / P $4.27 ｜ ATM IV 19.2%，净 delta 敞口 0 shares
仓位参考: Max Pain 721 ｜ Call Wall 720（+2.2%，弱）（OI 2.1k） ｜ Put Wall 722（+2.5%，弱）（OI 12.6k）
量化解读： 存量 Put 重｜ATM IV 19.2%｜历史 Rank 55%（近端代理）｜IV/RV 1.05×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

10-27（Activity LOW）仓位参考: Max Pain 720

10-28（Activity LOW）仓位参考: Max Pain 720 ｜ Call Wall 720（+2.2%，弱）（OI 1.2k） ｜ Put Wall 720（+2.2%，弱）（OI 2.8k）

10-29（Activity LOW）仓位参考: Max Pain 719 ｜ Call Wall 720（+2.2%，弱）（OI 0.5k） ｜ Put Wall 700（-0.6%，弱）（OI 1.8k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-23/QQQ_evening.json