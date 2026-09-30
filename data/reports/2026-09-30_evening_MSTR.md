# 期权晚报 2026-09-30（快照 16:40 ET）

📊 市场环境

SPY $762.63 ｜ QQQ $739.77
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

🔍 重点速览
🟡 **事件差分**: 10-02 ATM IV 72.3% vs 10-09 62.1%（差 +10.2pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-09 160C ΔOI +746（距现价 +4.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 160.82 → 收盘 153.09（-4.8%） ｜ 今日高 163.53 ｜ 低 152.02 ｜ 昨收 154.67 → 收盘 153.09（-1.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.36 | OI比 0.81 | ATM IV 72.3% | Skew -7.1pp | Term 0.90 | ExpMove ±4.2%（近端） | Rank 32%
量化视角： IV 中性（Rank 32%）｜期限结构正常（Term 0.90）｜Put 保护异常便宜（Skew -7.1pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.81）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.36×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.81×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-02（2D）±4.2% ｜ 10-09（9D）±7.7% ｜ 10-16（16D）±10.3% ｜ 10-23（23D）±12.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 29,148,078 | GEX Change vs 上次快照 -25,160,277 | Flip: Primary Flip: 147.73（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 770 / LOW 91 / INVALID 181
结构观察区: Primary Flip 147.73（全链重定价，覆盖 100%）
最近结构参考: Flip 148（现价高于该位 3.6%）
量化视角： 正 Gamma（2915万，无历史分位）｜正 Gamma 减弱（2516万）｜现价位于 Flip 上方 3.63%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 155（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 148（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C +1.2k / P -1.1k ｜ Activity MEDIUM △ ｜ 2D
10-09  C +4.8k / P +4.6k ｜ Activity HIGH ｜ 9D
10-16  C -17 / P +1.7k ｜ Activity MEDIUM △ ｜ 16D
10-23  C +6.8k / P +1.9k ｜ Activity HIGH ｜ 23D

📆 10-02 Forward Structure
存量OI: C 240.6k / P 194.3k，今日变化ΔOI: C +1.2k / P -1.1k，平值价格ATM: C $3.55 / P $2.85 ｜ ATM IV 72.3%，净 delta 敞口 258k shares
Top ΔOI: C 170 -3,839 ｜ C 167 +2,805 ｜ P 162 -2,712
仓位参考: Max Pain 155 ｜ Call Wall 165（+7.8%，弱）（OI 32.2k） ｜ Put Wall 150（-2.0%，弱）（OI 10.8k）
量化解读： 存量 Call 重｜ATM IV 72.3%｜历史 Rank 32%（近端代理）｜IV/RV 0.94×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 257,841 股

📆 10-09 Forward Structure
存量OI: C 43.1k / P 58.7k，今日变化ΔOI: C +4.8k / P +4.6k，平值价格ATM: C $6.40 / P $5.45 ｜ ATM IV 62.1%，净 delta 敞口 -24k shares
Top ΔOI: C 160 +746
仓位参考: Max Pain 150 ｜ Call Wall 165（+7.8%，弱）（OI 5.2k） ｜ Put Wall 155（+1.2%，弱）（OI 2.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 62.1%｜历史 Rank 32%（近端代理）｜IV/RV 0.81×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 24,101 股

10-16（MEDIUM △）Top ΔOI: 190C -1,133 ｜ 175C -488
10-16（MEDIUM △）仓位参考: Max Pain 120 ｜ Call Wall 155（+1.2%，弱）（OI 10.4k） ｜ Put Wall 140（-8.6%，弱）（OI 5.3k）

📆 10-23 Forward Structure
存量OI: C 22.6k / P 25.1k，今日变化ΔOI: C +6.8k / P +1.9k，平值价格ATM: C $10.70 / P $8.70 ｜ ATM IV 62.0%，净 delta 敞口 180k shares
Top ΔOI: C 165 +4,103 ｜ C 162 +1,124 ｜ C 167 +501
仓位参考: Max Pain 160 ｜ Call Wall 165（+7.8%）（OI 5.1k） ｜ Put Wall 155（+1.2%，弱）（OI 2.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 62.0%｜历史 Rank 32%（近端代理）｜IV/RV 0.81×（近似）｜净 delta 敞口 正 180,034 股

📅 事件差分（观察，非因果）: 10-02（2D）ATM IV 72.3% vs 10-09 62.1%（差 +10.2pp）——覆盖 PCE 物价 Price Index MoM、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-30/MSTR_evening.json