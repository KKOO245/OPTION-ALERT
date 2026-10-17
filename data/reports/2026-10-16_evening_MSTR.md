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


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 146.14 → 收盘 136.83（-6.4%） ｜ 今日高 146.83 ｜ 低 134.11 ｜ 昨收 151.29 → 收盘 136.83（-9.6%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.52 | OI比 1.30 | ATM IV 71.5% | Skew 9.3pp | Term 1.00 | ExpMove ±8.0%（近端） | Rank 32%
量化视角： IV 中性（Rank 32%）｜期限结构正常（Term 1.00）｜保护溢价显著（Skew 9.3pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.52×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.30×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-23（7D）±8.0% ｜ 10-30（14D）±11.8% ｜ 11-06（21D）±14.4% ｜ 11-13（28D）±16.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -13,173,755 | GEX Change vs 上次快照 -23,583,511 | Flip: Primary Flip: 144.47（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 538 / LOW 62 / INVALID 130
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 144.47（全链重定价，覆盖 100%）
Call Wall 135（现价高于该位 1.4%）
最近结构参考: Call Wall 135（现价高于该位 1.4%）
量化视角： 负 Gamma（1317万，无历史分位）｜由正转负（2358万）｜现价位于 Flip 下方 5.29%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 135（Call Wall）；上方 152（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 144（全链重定价，覆盖 100%）。
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
存量OI: C 95.0k / P 123.5k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $5.42 / P $5.50 ｜ ATM IV 71.5%，净 delta 敞口 0 shares
仓位参考: Max Pain 152 ｜ Put Wall 150（+9.6%，弱）（OI 5.7k）
量化解读： 存量 Put 重｜ATM IV 71.5%｜历史 Rank 32%（近端代理）｜IV/RV 1.53×（近似）｜净 delta 敞口 正 0 股

10-30（Activity LOW）仓位参考: Max Pain 158 ｜ Put Wall 125（-8.6%）（OI 11.7k）

11-06（Activity LOW）仓位参考: Max Pain 160 ｜ Put Wall 150（+9.6%，弱）（OI 2.2k）

11-13（Activity LOW）仓位参考: Max Pain 165 ｜ Put Wall 150（+9.6%，弱）（OI 1.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-16/MSTR_evening.json