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


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 1,215.09 → 收盘 1,150.89（-5.3%） ｜ 今日高 1239.00 ｜ 低 1115.23 ｜ 昨收 1,330.05 → 收盘 1,150.89（-13.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.95 | OI比 0.74 | ATM IV 83.7% | Skew 8.8pp | Term 0.91 | ExpMove ±9.3%（近端） | Rank 41%
量化视角： IV 中性（Rank 41%）｜期限结构正常（Term 0.91）｜保护溢价显著（Skew 8.8pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.74）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.95×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.74×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（7D）±9.3% ｜ 11-13（14D）±12.5% ｜ 11-20（21D）±15.2% ｜ 11-27（28D）±16.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -5,165,964 | GEX Change vs 上次快照 806,591 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1609 / LOW 377 / INVALID 782
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: NO_CROSS
量化视角： 负 Gamma（517万，无历史分位）｜负 Gamma 缓解（+81万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 1,380（MaxPain，仅结算参考）。
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
存量OI: C 21.4k / P 15.9k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $55.20 / P $52.29 ｜ ATM IV 83.7%，净 delta 敞口 0 shares
仓位参考: Max Pain 1,380 ｜ Call Wall 1250（+8.6%，弱）（OI 0.2k） ｜ Put Wall 1200（+4.3%，弱）（OI 0.9k）
量化解读： 存量 Call 重｜ATM IV 83.7%｜历史 Rank 41%（近端代理）｜IV/RV 1.24×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-13（Activity LOW）仓位参考: Max Pain 1,480

11-20（Activity LOW）仓位参考: Max Pain 1,480 ｜ Put Wall 1200（+4.3%，弱）（OI 1.4k）

11-27（Activity LOW）仓位参考: Max Pain 1,390 ｜ Call Wall 1150（-0.1%，弱）（OI 0.2k） ｜ Put Wall 1150（-0.1%）（OI 1.0k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-30/SNDK_evening.json