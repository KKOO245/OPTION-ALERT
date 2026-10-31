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


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 203.48 → 收盘 203.17（-0.1%） ｜ 今日高 215.45 ｜ 低 194.15 ｜ 昨收 222.30 → 收盘 203.17（-8.6%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.71 | OI比 1.03 | ATM IV 91.4% | Skew 6.8pp | Term 0.91 | ExpMove ±10.3%（近端） | Rank 53%
量化视角： IV 中性（Rank 53%）｜期限结构正常（Term 0.91）｜保护溢价显著（Skew 6.8pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.71×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.03×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-06（7D）±10.3% ｜ 11-13（14D）±13.6% ｜ 11-20（21D）±16.8% ｜ 11-27（28D）±17.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -5,982,646 | GEX Change vs 上次快照 -3,481,599 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 490 / LOW 91 / INVALID 171
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: NO_CROSS
Put Wall 200（现价高于该位 1.6%）
最近结构参考: Put Wall 200（现价高于该位 1.6%）
量化视角： 负 Gamma（598万，无历史分位）｜负 Gamma 加深（348万）｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall）；上方 230（MaxPain，仅结算参考）。
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
存量OI: C 20.6k / P 21.2k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $10.71 / P $10.20 ｜ ATM IV 91.4%，净 delta 敞口 0 shares
仓位参考: Max Pain 230 ｜ Call Wall 200（-1.6%，弱）（OI 1.3k） ｜ Put Wall 200（-1.6%，弱）（OI 1.1k）
量化解读： 存量两侧均衡｜ATM IV 91.4%｜历史 Rank 53%（近端代理）｜IV/RV 1.06×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-13（Activity LOW）仓位参考: Max Pain 240 ｜ Call Wall 220（+8.3%，弱）（OI 0.3k） ｜ Put Wall 200（-1.6%，弱）（OI 0.6k）

11-20（Activity LOW）仓位参考: Max Pain 230 ｜ Call Wall 220（+8.3%，弱）（OI 1.8k） ｜ Put Wall 200（-1.6%，弱）（OI 5.5k）

11-27（Activity LOW）仓位参考: Max Pain 230 ｜ Call Wall 215（+5.8%，弱）（OI 0.1k） ｜ Put Wall 190（-6.5%，弱）（OI 1.9k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-30/BE_evening.json