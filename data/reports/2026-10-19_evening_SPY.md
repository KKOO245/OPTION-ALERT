# 期权晚报 2026-10-19（快照 21:00 ET）

📊 市场环境

SPY $766.48 ｜ QQQ $718.36
VIX 18.44 ↓7.8%（5D +21.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 23.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.4 ｜ 实际 待公布 ｜ 前值 1.403
- 周二 10-20 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.275

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 767.23 → 收盘 766.48（-0.1%） ｜ 今日高 770.46 ｜ 低 765.82 ｜ 昨收 763.25 → 收盘 766.48（+0.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.10 | OI比 1.90 | ATM IV 13.4% | Skew 2.7pp | Term 1.06 | ExpMove ±0.6%（近端） | Rank 55%
量化视角： IV 中性（Rank 55%）｜期限结构正常（Term 1.06）｜保护溢价中性（Skew 2.7pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.10×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.90×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 32% ｜ P/C OI(近端) 55%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 32%）｜近端持仓结构中性（P/C OI 分位 55%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-20（1D）±0.6% ｜ 10-21（2D）±0.8% ｜ 10-22（3D）±1.0% ｜ 10-23（4D）±1.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,064,534,252 | GEX Change vs 上次快照 48,461,666 | Flip: Primary Flip: 773.34（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 2719 / LOW 232 / INVALID 1483
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 773.34（全链重定价，覆盖 98%）
最近结构参考: Flip 773（现价低于该位 0.9%）
量化视角： 负 Gamma（10.65亿，历史分位 32%，中性区）｜负 Gamma 缓解（+4846万）｜现价位于 Flip 下方 0.89%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 770（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 773（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-20  C +0 / P +0 ｜ Activity LOW ｜ 1D
10-21  C +0 / P +0 ｜ Activity LOW ｜ 2D
10-22  C +0 / P +0 ｜ Activity LOW ｜ 3D
10-23  C +0 / P +0 ｜ Activity LOW ｜ 4D

📆 10-20 Forward Structure
存量OI: C 98.9k / P 187.7k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $2.70 / P $1.68 ｜ ATM IV 13.4%，净 delta 敞口 0 shares
仓位参考: Max Pain 770 ｜ Call Wall 775（+1.1%，弱）（OI 6.1k） ｜ Put Wall 751（-2.0%，弱）（OI 12.3k）
量化解读： 存量 Put 重｜ATM IV 13.4%｜历史 Rank 55%（近端代理）｜IV/RV 1.56×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

10-21（Activity LOW）仓位参考: Max Pain 769 ｜ Call Wall 773（+0.9%，弱）（OI 3.2k） ｜ Put Wall 746（-2.7%，弱）（OI 10.6k）

10-22（Activity LOW）仓位参考: Max Pain 771 ｜ Call Wall 780（+1.8%，弱）（OI 6.2k） ｜ Put Wall 745（-2.8%，弱）（OI 4.2k）

10-23（Activity LOW）仓位参考: Max Pain 770 ｜ Call Wall 780（+1.8%，弱）（OI 24.1k） ｜ Put Wall 745（-2.8%，弱）（OI 38.8k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-19/SPY_evening.json