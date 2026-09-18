# 期权晚报 2026-09-17（快照 21:08 ET）

📊 市场环境

SPY $762.60 ｜ QQQ $nan
VIX 15.44 ↓12.8%（5D -13.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-17

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 1.275 ｜ 前值 1.309　✅ 今日已公布
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 1.394 ｜ 前值 1.433　✅ 今日已公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 763.15 → 收盘 762.60（-0.1%） ｜ 今日高 763.57 ｜ 低 759.96 ｜ 昨收 754.05 → 收盘 762.60（+1.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.80 | OI比 2.98 | ATM IV 11.8% | Skew 2.0pp | Term 1.04 | ExpMove ±0.6%（近端） | Rank 41%
量化视角： IV 中性（Rank 41%）｜期限结构正常（Term 1.04）｜保护溢价薄（Skew 2.0pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.80×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 2.98×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 39% ｜ P/C OI(近端) 95%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 39%）｜近端 Put 显著偏重（P/C OI 分位 95%，历史高位区）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-18（1D）±0.6% ｜ 09-21（4D）±0.8% ｜ 09-22（5D）±0.9% ｜ 09-23（6D）±1.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -769,724,135 | GEX Change vs 上次快照 146,714,620 | Flip: Primary Flip: 765.43（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 3137 / LOW 404 / INVALID 1469
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 765.43（全链重定价，覆盖 91%）
Call Wall 800（弱结构｜现价低于该位 4.7%）
最近结构参考: Flip 765（现价低于该位 0.4%）
量化视角： 负 Gamma（7.70亿，历史分位 39%，中性区）｜负 Gamma 缓解（+1.47亿）｜现价位于 Flip 下方 0.37%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 755（MaxPain，仅结算参考）；上方 800（Call Wall，弱结构）。
• Gamma 区域：切换参考 765（全链重定价，覆盖 91%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-18  C +0 / P +0 ｜ Activity LOW ｜ 1D
09-21  C +0 / P +0 ｜ Activity LOW ｜ 4D
09-22  C +0 / P +0 ｜ Activity LOW ｜ 5D
09-23  C +0 / P +0 ｜ Activity LOW ｜ 6D

📆 09-18 Forward Structure
存量OI: C 1320.6k / P 3938.7k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $1.15 / P $3.37 ｜ ATM IV 11.8%，净 delta 敞口 0 shares
仓位参考: Max Pain 755 ｜ Call Wall 790（+3.6%，弱）（OI 58.5k） ｜ Put Wall 740（-3.0%，弱）（OI 97.2k）
量化解读： 存量 Put 重｜ATM IV 11.8%｜历史 Rank 41%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-21（Activity LOW）仓位参考: Max Pain 756 ｜ Call Wall 789（+3.5%，弱）（OI 6.9k） ｜ Put Wall 755（-1.0%）（OI 11.5k）

09-22（Activity LOW）仓位参考: Max Pain 759 ｜ Call Wall 804（+5.4%，弱）（OI 3.1k） ｜ Put Wall 733（-3.9%，弱）（OI 6.0k）

09-23（Activity LOW）仓位参考: Max Pain 757 ｜ Call Wall 807（+5.8%，弱）（OI 5.4k） ｜ Put Wall 725（-4.9%，弱）（OI 2.5k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-17/SPY_evening.json