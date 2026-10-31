# 期权晚报 2026-10-30（快照 21:00 ET）

📊 市场环境

SPY $755.72 ｜ QQQ $690.49
VIX 19.42 ↑12.9%（5D -0.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 26.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-30

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 39.26 → 收盘 39.57（+0.8%） ｜ 今日高 40.34 ｜ 低 38.49 ｜ 昨收 41.64 → 收盘 39.57（-5.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.03 | OI比 0.48 | ATM IV 79.7% | Skew 0.7pp | Term 0.85 | ExpMove ±9.2%（近端） | Rank 72%
量化视角： IV 中性（Rank 72%）｜期限结构倒挂（Term 0.85，近月 IV 高于远月）｜保护溢价薄（Skew 0.7pp）｜存量 Call 偏重（OI比 0.48）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.03×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.48×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（7D）±9.2% ｜ 11-13（14D）±8.4% ｜ 11-20（21D）±17.7% ｜ 11-27（28D）±11.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,914,589 | GEX Change vs 上次快照 -1,447,012 | Flip: Primary Flip: 36.25（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 307 / LOW 24 / INVALID 79
结构观察区: Primary Flip 36.25（全链重定价，覆盖 100%）
最近结构参考: Flip 36（现价高于该位 9.2%）
量化视角： 正 Gamma（191万，无历史分位）｜正 Gamma 减弱（145万）｜现价位于 Flip 上方 9.15%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 42（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 36（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-06  C +0 / P +0 ｜ Activity LOW ｜ 7D
11-13  C +0 / P +0 ｜ Activity LOW ｜ 14D
11-20  C +0 / P +0 ｜ Activity LOW ｜ 21D
11-27  C +0 / P +0 ｜ Activity LOW ｜ 28D

📆 11-06 Forward Structure
存量OI: C 9.9k / P 4.7k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $1.53 / P $2.10 ｜ ATM IV 79.7%，净 delta 敞口 0 shares
仓位参考: Max Pain 42 ｜ Call Wall 43（+8.7%，弱）（OI 1.0k） ｜ Put Wall 38（-4.0%）（OI 0.9k）
量化解读： 存量 Call 重｜ATM IV 79.7%｜历史 Rank 72%（近端代理）｜IV/RV 1.48×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-13（Activity LOW）仓位参考: Max Pain 40 ｜ Call Wall 40（+1.1%，弱）（OI 0.8k） ｜ Put Wall 39（-1.4%）（OI 0.5k）

11-20（Activity LOW）仓位参考: Max Pain 45 ｜ Call Wall 40（+1.1%，弱）（OI 0.9k） ｜ Put Wall 40（+1.1%，弱）（OI 1.5k）

11-27（Activity LOW）仓位参考: Max Pain 44 ｜ Put Wall 38（-4.0%，弱）（OI 68）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-30/MP_evening.json