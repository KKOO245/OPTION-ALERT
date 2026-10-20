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


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 719.61 → 收盘 718.36（-0.2%） ｜ 今日高 724.55 ｜ 低 716.57 ｜ 昨收 709.80 → 收盘 718.36（+1.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.08 | OI比 1.07 | ATM IV 22.3% | Skew 4.6pp | Term 0.97 | ExpMove ±0.9%（近端） | Rank 71%
量化视角： IV 中性（Rank 71%）｜期限结构正常（Term 0.97）｜保护溢价中性（Skew 4.6pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.08×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.07×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 14% ｜ P/C OI(近端) 8%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 14%）｜近端持仓极端 Call 重（P/C OI 分位 8%，历史极低区）｜⚠️ 需重点观察：持仓极端 + Gamma 异常侧组合——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-20（1D）±0.9% ｜ 10-21（2D）±1.4% ｜ 10-22（3D）±1.7% ｜ 10-23（4D）±2.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -683,193,064 | GEX Change vs 上次快照 8,011,909 | Flip: Primary Flip: 731.90（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 2804 / LOW 282 / INVALID 1646
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 731.90（全链重定价，覆盖 99%）
Put Wall 700（弱结构｜现价高于该位 2.6%）
最近结构参考: Flip 732（现价低于该位 1.9%）
量化视角： 负 Gamma（6.83亿，历史分位偏负区，比 86% 的交易日更负）｜负 Gamma 缓解（+801万）｜现价位于 Flip 下方 1.85%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 700（Put Wall，弱结构）；上方 719（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 732（全链重定价，覆盖 99%）。
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
存量OI: C 99.2k / P 106.5k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $3.81 / P $2.98 ｜ ATM IV 22.3%，净 delta 敞口 0 shares
仓位参考: Max Pain 719 ｜ Call Wall 733（+2.0%，弱）（OI 7.4k） ｜ Put Wall 705（-1.9%，弱）（OI 10.8k）
量化解读： 存量两侧均衡｜ATM IV 22.3%｜历史 Rank 71%（近端代理）｜IV/RV 1.46×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

10-21（Activity LOW）仓位参考: Max Pain 720 ｜ Call Wall 730（+1.6%，弱）（OI 2.1k） ｜ Put Wall 700（-2.6%）（OI 5.8k）

10-22（Activity LOW）仓位参考: Max Pain 724 ｜ Call Wall 730（+1.6%，弱）（OI 1.3k）

10-23（Activity LOW）仓位参考: Max Pain 727 ｜ Call Wall 735（+2.3%，弱）（OI 22.4k） ｜ Put Wall 711（-1.0%，弱）（OI 40.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-19/QQQ_evening.json