# 期权晚报 2026-10-16（快照 21:00 ET）

📊 市场环境

SPY $763.25 ｜ QQQ $nan
VIX 19.99 ↑21.4%（5D +34.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 17.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 231.28 → 收盘 221.31（-4.3%） ｜ 今日高 233.59 ｜ 低 219.17 ｜ 昨收 236.30 → 收盘 221.31（-6.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.03 | OI比 0.91 | ATM IV 110.6% | Skew 8.8pp | Term 0.82 | ExpMove ±12.4%（近端） | Rank 70%
量化视角： IV 中性（Rank 70%）｜期限结构倒挂（Term 0.82，近月 IV 高于远月）｜保护溢价显著（Skew 8.8pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.03×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.91×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（7D）±12.4% ｜ 10-30（14D）±15.8% ｜ 11-06（21D）±19.3% ｜ 11-13（28D）±20.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -7,952,179 | GEX Change vs 上次快照 -2,020,046 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 540 / LOW 30 / INVALID 96
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: NO_CROSS
Put Wall 240（弱结构｜现价低于该位 7.8%）
最近结构参考: Put Wall 240（现价低于该位 7.8%）
量化视角： 负 Gamma（795万，无历史分位）｜负 Gamma 加深（202万）｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 240（Put Wall，弱结构） / 255（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +0 / P +0 ｜ Activity LOW ｜ 7D
10-30  C +0 / P +0 ｜ Activity LOW ｜ 14D
11-06  C +0 / P +0 ｜ Activity LOW ｜ 21D
11-13  C +0 / P +0 ｜ Activity LOW ｜ 28D

📆 10-23 Forward Structure
存量OI: C 33.1k / P 30.1k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $13.25 / P $14.15 ｜ ATM IV 110.6%，净 delta 敞口 0 shares
仓位参考: Max Pain 255 ｜ Call Wall 230（+3.9%，弱）（OI 1.4k） ｜ Put Wall 230（+3.9%，弱）（OI 2.3k）
量化解读： 存量两侧均衡｜ATM IV 110.6%｜历史 Rank 70%（近端代理）｜IV/RV 1.36×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-30（Activity LOW）仓位参考: Max Pain 260 ｜ Call Wall 240（+8.4%，弱）（OI 1.3k） ｜ Put Wall 230（+3.9%）（OI 3.5k）

11-06（Activity LOW）仓位参考: Max Pain 260 ｜ Call Wall 240（+8.4%，弱）（OI 0.3k） ｜ Put Wall 235（+6.2%）（OI 2.7k）

11-13（Activity LOW）仓位参考: Max Pain 270 ｜ Call Wall 240（+8.4%，弱）（OI 0.3k） ｜ Put Wall 230（+3.9%）（OI 2.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-16/BE_evening.json