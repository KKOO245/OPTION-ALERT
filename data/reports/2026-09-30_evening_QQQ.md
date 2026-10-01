# 期权晚报 2026-09-30（快照 21:00 ET）

📊 市场环境

SPY $762.63 ｜ QQQ $nan
VIX 16.34 ↑1.9%（5D +7.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 30.8（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-30

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.2 ｜ 前值 0.1　✅ 今日已公布
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 2.2 ｜ 前值 2.5　✅ 今日已公布
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 0.9 ｜ 前值 0.1　✅ 今日已公布
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 740.19 → 收盘 739.77（-0.1%） ｜ 今日高 745.08 ｜ 低 739.46 ｜ 昨收 737.93 → 收盘 739.77（+0.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.14 | OI比 1.05 | ATM IV 20.7% | Skew 2.5pp | Term 0.95 | ExpMove ±0.9%（近端） | Rank 64%
量化视角： IV 中性（Rank 64%）｜期限结构正常（Term 0.95）｜保护溢价中性（Skew 2.5pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.14×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.05×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 64% ｜ P/C OI(近端) 7%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 64%）｜近端持仓极端 Call 重（P/C OI 分位 7%，历史极低区）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-01（1D）±0.9% ｜ 10-02（2D）±1.2% ｜ 10-05（5D）±1.6% ｜ 10-06（6D）±1.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 123,882,274 | GEX Change vs 上次快照 -192,787,238 | Flip: Primary Flip: 738.03（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 2609 / LOW 347 / INVALID 1698
结构观察区: Primary Flip 738.03（全链重定价，覆盖 98%）
Call Wall 760（现价低于该位 2.7%）
最近结构参考: Flip 738（现价高于该位 0.2%）
量化视角： 正 Gamma（1.24亿，历史分位 64%，中性区）｜正 Gamma 减弱（1.93亿）｜现价位于 Flip 上方 0.24%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 738（MaxPain，仅结算参考）；上方 760（Call Wall）。
• Gamma 区域：切换参考 738（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-01  C +0 / P +0 ｜ Activity LOW ｜ 1D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 2D
10-05  C +0 / P +0 ｜ Activity LOW ｜ 5D
10-06  C +0 / P +0 ｜ Activity LOW ｜ 6D

📆 10-01 Forward Structure
存量OI: C 80.7k / P 84.7k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $3.50 / P $3.02 ｜ ATM IV 20.7%，净 delta 敞口 0 shares
仓位参考: Max Pain 738 ｜ Call Wall 740（+0.0%，弱）（OI 7.6k） ｜ Put Wall 740（+0.0%，弱）（OI 5.1k）
量化解读： 存量两侧均衡｜ATM IV 20.7%｜历史 Rank 64%（近端代理）｜IV/RV 1.41×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-02（Activity LOW）仓位参考: Max Pain 730 ｜ Call Wall 725（-2.0%）（OI 35.2k） ｜ Put Wall 730（-1.3%，弱）（OI 49.9k）

10-05（Activity LOW）仓位参考: Max Pain 739 ｜ Call Wall 755（+2.1%）（OI 8.0k）

10-06（Activity LOW）仓位参考: Max Pain 738 ｜ Call Wall 740（+0.0%，弱）（OI 1.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-30/QQQ_evening.json