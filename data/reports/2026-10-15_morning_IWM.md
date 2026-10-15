# 期权晨报 2026-10-15（快照 10:20 ET）

📊 市场环境

SPY $767.19 ｜ QQQ $720.69
VIX 17.51 ↑3.8%（5D +13.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 24.6（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 1.3 ｜ 前值 0.5　✅ 今日已公布
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 0.8 ｜ 前值 1.3　✅ 今日已公布
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布　⏰ 今日

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## IWM

Options: P/C成交量 0.81 | OI比 1.64 | ATM IV 25.4% | Skew 1.7pp | Term 0.78 | ExpMove ±1.1%（近端） | Rank — (历史不足)
量化视角： 期限结构倒挂（Term 0.78，近月 IV 高于远月）｜保护溢价薄（Skew 1.7pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.81×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.64×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-16（1D）±1.1% ｜ 10-19（4D）±1.4% ｜ 10-20（5D）±1.7% ｜ 10-21（6D）±2.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,968,306,702 | GEX Change N/A | Flip: Primary Flip: 282.02（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 1282 / LOW 202 / INVALID 1414
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 282.02（全链重定价，覆盖 96%）
Put Wall 270（弱结构｜现价高于该位 0.8%） | Call Wall 285（弱结构｜现价低于该位 4.5%）
最近结构参考: Put Wall 270（现价高于该位 0.8%）
量化视角： 负 Gamma（19.68亿，无历史分位）｜现价位于 Flip 下方 3.46%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 270（Put Wall，弱结构） / 272（MaxPain，仅结算参考）；上方 285（Call Wall，弱结构）。
• Gamma 区域：切换参考 282（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
🎯 今日到期（0DTE）
存量OI: C 35.6k / P 58.4k，今日成交量: C 90.4k / P 73.7k，平值价格ATM: C $1.00 / P $0.54 ｜ ATM IV 25.4%，预期波动 ±0.6%，Max Pain 272

📆 Forward Expiration Structure

10-16  C N/A / P N/A ｜ Activity LOW ｜ 1D（新上架）
10-19  C N/A / P N/A ｜ Activity LOW ｜ 4D（新上架）
10-20  C N/A / P N/A ｜ Activity LOW ｜ 5D（新上架）
10-21  C N/A / P N/A ｜ Activity LOW ｜ 6D（新上架）

📆 10-16 Forward Structure
存量OI: C 668.1k / P 1034.6k，今日变化ΔOI: C N/A / P N/A，平值价格ATM: C $1.73 / P $1.16 ｜ ATM IV 22.2%
仓位参考: Max Pain 280 ｜ Call Wall 289（+6.1%，弱）（OI 48.5k） ｜ Put Wall 275（+1.0%，弱）（OI 79.1k）
量化解读： 存量 Put 重｜ATM IV 22.2%｜期限倒挂（近端 IV > 远月）

10-19（Activity LOW）仓位参考: Max Pain 276 ｜ Call Wall 285（+4.7%）（OI 2.6k） ｜ Put Wall 273（+0.3%，弱）（OI 2.1k）

10-20（Activity LOW）仓位参考: Max Pain 275 ｜ Call Wall 277（+1.7%，弱）（OI 1.5k） ｜ Put Wall 263（-3.4%，弱）（OI 1.4k）

10-21（Activity LOW）仓位参考: Max Pain 276 ｜ Call Wall 285（+4.7%，弱）（OI 1.0k） ｜ Put Wall 260（-4.5%）（OI 1.2k）

📅 事件差分（观察，非因果）: 10-16（1D）ATM IV 22.2% vs 10-19 15.9%（差 +6.3pp）——覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 C ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-15/IWM_morning.json