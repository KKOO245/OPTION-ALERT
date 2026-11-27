# 期权晨报 2026-11-27（快照 10:20 ET）

📊 市场环境

SPY $722.09 ｜ QQQ $642.13
VIX 27.52 ↑2.7%（5D -23.3%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 22.6（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-27

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 156.60 → 今开 157.92（+0.8%） | 较昨收变动（含盘初走势） ｜ 今日高 157.92 ｜ 低 155.38

Options: P/C成交量 5.27 | OI比 1.98 | ATM IV 34.1% | Skew 15.1pp | Term 1.11 | ExpMove ±5.0%（近端） | Rank 52%
量化视角： IV 中性（Rank 52%）｜期限结构正常（Term 1.11）｜保护溢价显著（Skew 15.1pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 5.27）——观察点，非方向信号
   ⇒ Put/Call Volume: 5.27×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.98×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 12-04（7D）±5.0% ｜ 12-11（14D）±3.4% ｜ 12-18（21D）±8.7% ｜ 12-24（27D）±4.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 6,306,461 | GEX Change vs 上次快照 -3,345,593 | Flip: Primary Flip: 154.55（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 386 / LOW 143 / INVALID 383
结构观察区: Primary Flip 154.55（全链重定价，覆盖 97%）
最近结构参考: Flip 155（现价高于该位 0.9%）
量化视角： 正 Gamma（631万，无历史分位）｜正 Gamma 减弱（335万）｜现价位于 Flip 上方 0.87%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 152（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 155（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
🎯 今日到期（0DTE）
存量OI: C 7.1k / P 14.2k，今日成交量: C 0.8k / P 4.3k，平值价格ATM: C $1.81 / P $1.30 ｜ ATM IV 34.1%，预期波动 ±2.0%，Max Pain 152

📆 Forward Expiration Structure

12-04  C +0 / P +0 ｜ Activity LOW ｜ 7D
12-11  C +0 / P +0 ｜ Activity LOW ｜ 14D
12-18  C +0 / P +0 ｜ Activity LOW ｜ 21D
12-24  C +0 / P +0 ｜ Activity LOW ｜ 27D

📆 12-04 Forward Structure
存量OI: C 1.7k / P 17.7k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $4.36 / P $3.50 ｜ ATM IV 40.3%，净 delta 敞口 0 shares
仓位参考: Max Pain 154 ｜ Call Wall 157.5（+1.0%，弱）（OI 0.2k） ｜ Put Wall 146（-6.3%，弱）（OI 2.0k）
量化解读： 存量 Put 重｜ATM IV 40.3%｜历史 Rank 52%（近端代理）｜IV/RV 0.86×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

12-11（Activity LOW）仓位参考: Max Pain 150 ｜ Call Wall 147（-5.7%，弱）（OI 1.0k） ｜ Put Wall 150（-3.8%，弱）（OI 2.0k）

12-18（Activity LOW）仓位参考: Max Pain 140

12-24（Activity LOW）仓位参考: Max Pain 154 ｜ Call Wall 155（-0.6%）（OI 0.3k） ｜ Put Wall 160（+2.6%，弱）（OI 0.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-27/XBI_morning.json