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


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 158.76 → 收盘 158.74（-0.0%） ｜ 今日高 162.99 ｜ 低 155.86 ｜ 昨收 159.17 → 收盘 158.74（-0.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.51 | OI比 0.66 | ATM IV 94.7% | Skew 3.7pp | Term 1.06 | ExpMove ±10.5%（近端） | Rank 36%
量化视角： IV 中性（Rank 36%）｜期限结构正常（Term 1.06）｜保护溢价中性（Skew 3.7pp）｜存量 Call 偏重（OI比 0.66）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.51×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.66×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（7D）±10.5% ｜ 11-06（14D）±15.2% ｜ 11-13（21D）±20.4% ｜ 11-20（28D）±22.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -7,259,331 | GEX Change vs 上次快照 -1,838,267 | Flip: Primary Flip: 176.27（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 512 / LOW 23 / INVALID 165
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 176.27（全链重定价，覆盖 100%）
Put Wall 150（弱结构｜现价高于该位 5.8%）
最近结构参考: Put Wall 150（现价高于该位 5.8%）
量化视角： 负 Gamma（726万，无历史分位）｜负 Gamma 加深（184万）｜现价位于 Flip 下方 9.95%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（Put Wall，弱结构）；上方 198（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 176（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-30  C +0 / P +0 ｜ Activity LOW ｜ 7D
11-06  C +0 / P +0 ｜ Activity LOW ｜ 14D
11-13  C +0 / P +0 ｜ Activity LOW ｜ 21D
11-20  C +0 / P +0 ｜ Activity LOW ｜ 28D

📆 10-30 Forward Structure
存量OI: C 66.6k / P 44.0k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $9.05 / P $7.64 ｜ ATM IV 94.7%，净 delta 敞口 0 shares
仓位参考: Max Pain 198 ｜ Call Wall 170（+7.1%，弱）（OI 1.7k） ｜ Put Wall 150（-5.5%，弱）（OI 2.3k）
量化解读： 存量 Call 重｜ATM IV 94.7%｜历史 Rank 36%（近端代理）｜IV/RV 1.19×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

11-06（Activity LOW）仓位参考: Max Pain 200 ｜ Put Wall 170（+7.1%，弱）（OI 1.6k）

11-13（Activity LOW）仓位参考: Max Pain 195 ｜ Call Wall 170（+7.1%，弱）（OI 0.6k） ｜ Put Wall 165（+3.9%，弱）（OI 1.4k）

11-20（Activity LOW）仓位参考: Max Pain 195 ｜ Call Wall 170（+7.1%，弱）（OI 2.8k） ｜ Put Wall 150（-5.5%，弱）（OI 8.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-23/NBIS_evening.json