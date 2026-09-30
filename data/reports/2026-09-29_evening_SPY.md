# 期权晚报 2026-09-29（快照 21:00 ET）

📊 市场环境

SPY $764.20 ｜ QQQ $nan
VIX 16.04 ↓0.2%（5D +12.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-29

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-29 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.23 ｜ 实际 7.079 ｜ 前值 7.335　✅ 今日已公布
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 待公布 ｜ 前值 2.1
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 766.83 → 收盘 764.20（-0.3%） ｜ 今日高 766.95 ｜ 低 762.35 ｜ 昨收 765.61 → 收盘 764.20（-0.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.93 | OI比 2.87 | ATM IV 13.5% | Skew 1.7pp | Term 1.00 | ExpMove ±0.6%（近端） | Rank 55%
量化视角： IV 中性（Rank 55%）｜期限结构正常（Term 1.00）｜保护溢价薄（Skew 1.7pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.93×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 2.87×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 31% ｜ P/C OI(近端) 94%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 31%）｜近端 Put 显著偏重（P/C OI 分位 94%，历史高位区）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-30（1D）±0.6% ｜ 10-01（2D）±0.8% ｜ 10-02（3D）±1.1% ｜ 10-05（6D）±1.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,103,448,114 | GEX Change vs 上次快照 -292,863,787 | Flip: Primary Flip: 769.46（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 2630 / LOW 410 / INVALID 1794
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 769.46（全链重定价，覆盖 92%）
Call Wall 785（现价低于该位 2.6%）
最近结构参考: Flip 769（现价低于该位 0.7%）
量化视角： 负 Gamma（11.03亿，历史分位 31%，中性区）｜负 Gamma 加深（2.93亿）｜现价位于 Flip 下方 0.68%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 761（MaxPain，仅结算参考）；上方 785（Call Wall）。
• Gamma 区域：切换参考 769（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-30  C +0 / P +0 ｜ Activity LOW ｜ 1D
10-01  C +0 / P +0 ｜ Activity LOW ｜ 2D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 3D
10-05  C +0 / P +0 ｜ Activity LOW ｜ 6D

📆 09-30 Forward Structure
存量OI: C 647.1k / P 1857.7k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $2.58 / P $1.82 ｜ ATM IV 13.5%，净 delta 敞口 0 shares
仓位参考: Max Pain 761 ｜ Call Wall 786（+2.9%，弱）（OI 23.8k）
量化解读： 存量 Put 重｜ATM IV 13.5%｜历史 Rank 55%（近端代理）｜IV/RV 1.37×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-01（Activity LOW）仓位参考: Max Pain 765 ｜ Call Wall 782（+2.3%）（OI 13.6k） ｜ Put Wall 764（-0.0%，弱）（OI 4.7k）

10-02（Activity LOW）仓位参考: Max Pain 765 ｜ Call Wall 785（+2.7%）（OI 61.9k） ｜ Put Wall 745（-2.5%，弱）（OI 67.9k）

10-05（Activity LOW）仓位参考: Max Pain 767 ｜ Call Wall 775（+1.4%，弱）（OI 1.7k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-29/SPY_evening.json