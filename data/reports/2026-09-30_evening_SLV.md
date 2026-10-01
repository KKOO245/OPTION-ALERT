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


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 55.11 → 收盘 54.51（-1.1%） ｜ 今日高 55.24 ｜ 低 54.22 ｜ 昨收 55.48 → 收盘 54.51（-1.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.37 | OI比 0.51 | ATM IV 40.1% | Skew 2.1pp | Term 0.86 | ExpMove ±2.4%（近端） | Rank 66%
量化视角： IV 中性（Rank 66%）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜保护溢价中性（Skew 2.1pp）｜存量 Call 偏重（OI比 0.51）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.37×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.51×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（2D）±2.4% ｜ 10-05（5D）±2.9% ｜ 10-07（7D）±3.5% ｜ 10-09（9D）±4.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) -4,756,629 | GEX Change vs 上次快照 -14,964,382 | Flip: Primary Flip: 54.75（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 670 / LOW 88 / INVALID 452
结构观察区: Primary Flip 54.75（全链重定价，覆盖 98%）
最近结构参考: Flip 55（现价低于该位 0.4%）
量化视角： 负 Gamma（476万，无历史分位）｜由正转负（1496万）｜现价位于 Flip 下方 0.44%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 58（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 55（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C +0 / P +0 ｜ Activity LOW ｜ 2D
10-05  C +0 / P +0 ｜ Activity LOW ｜ 5D
10-07  C +0 / P +0 ｜ Activity LOW ｜ 7D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 9D

📆 10-02 Forward Structure
存量OI: C 90.1k / P 46.2k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $0.67 / P $0.64 ｜ ATM IV 40.1%，净 delta 敞口 0 shares
仓位参考: Max Pain 58 ｜ Call Wall 59（+8.2%，弱）（OI 6.6k） ｜ Put Wall 50（-8.3%）（OI 7.4k）
量化解读： 存量 Call 重｜ATM IV 40.1%｜历史 Rank 66%（近端代理）｜IV/RV 1.04×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-05（Activity LOW）仓位参考: Max Pain 57 ｜ Call Wall 55.5（+1.8%，弱）（OI 0.6k） ｜ Put Wall 52（-4.6%）（OI 1.3k）

10-07（Activity LOW）仓位参考: Max Pain 57 ｜ Call Wall 59（+8.2%，弱）（OI 0.8k） ｜ Put Wall 57（+4.6%）（OI 1.7k）

10-09（Activity LOW）仓位参考: Max Pain 57 ｜ Put Wall 55（+0.9%，弱）（OI 2.7k）

📅 事件差分（观察，非因果）: 10-02（2D）ATM IV 40.1% vs 10-05 30.4%（差 +9.7pp）——覆盖 PCE 物价 Price Index MoM、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-30/SLV_evening.json