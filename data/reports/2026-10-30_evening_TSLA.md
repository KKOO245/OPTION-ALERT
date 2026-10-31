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


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 393.04 → 收盘 399.81（+1.7%） ｜ 今日高 404.20 ｜ 低 387.52 ｜ 昨收 403.30 → 收盘 399.81（-0.9%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.97 | OI比 0.46 | ATM IV 32.6% | Skew 2.6pp | Term 1.27 | ExpMove ±2.4%（近端） | Rank 5%
量化视角： IV 历史低位（Rank 5%，期权偏便宜）｜期限结构正常偏陡（Term 1.27）｜保护溢价中性（Skew 2.6pp）｜存量 Call 偏重（OI比 0.46）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.97×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.46×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-02（3D）±2.4% ｜ 11-04（5D）±4.3% ｜ 11-06（7D）±5.3% ｜ 11-09（10D）±5.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 48,300,001 | GEX Change vs 上次快照 -41,048,384 | Flip: Primary Flip: 382.74（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1218 / LOW 51 / INVALID 765
结构观察区: Primary Flip 382.74（全链重定价，覆盖 100%）
Call Wall 400（弱结构｜现价低于该位 0.0%）
最近结构参考: Call Wall 400（现价低于该位 0.0%）
量化视角： 正 Gamma（4830万，无历史分位）｜正 Gamma 减弱（4105万）｜现价位于 Flip 上方 4.46%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 395（MaxPain，仅结算参考）；上方 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 383（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-02  C +0 / P +0 ｜ Activity LOW ｜ 3D
11-04  C +0 / P +0 ｜ Activity LOW ｜ 5D
11-06  C +0 / P +0 ｜ Activity LOW ｜ 7D
11-09  C +0 / P +0 ｜ Activity LOW ｜ 10D

📆 11-02 Forward Structure
存量OI: C 60.4k / P 27.5k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $4.70 / P $4.77 ｜ ATM IV 32.6%，净 delta 敞口 0 shares
仓位参考: Max Pain 395 ｜ Call Wall 410（+2.5%，弱）（OI 3.3k） ｜ Put Wall 400（+0.0%，弱）（OI 1.8k）
量化解读： 存量 Call 重｜ATM IV 32.6%｜历史 Rank 5%（近端代理）｜IV/RV 0.98×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

11-04（Activity LOW）仓位参考: Max Pain 400 ｜ Call Wall 410（+2.5%，弱）（OI 1.6k） ｜ Put Wall 400（+0.0%，弱）（OI 1.6k）

11-06（Activity LOW）仓位参考: Max Pain 390 ｜ Call Wall 425（+6.3%，弱）（OI 7.2k） ｜ Put Wall 400（+0.0%，弱）（OI 4.3k）

11-09（Activity LOW）仓位参考: Max Pain 400 ｜ Call Wall 420（+5.0%）（OI 0.8k） ｜ Put Wall 380（-5.0%）（OI 1.0k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-30/TSLA_evening.json