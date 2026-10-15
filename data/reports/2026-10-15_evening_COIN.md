# 期权晚报 2026-10-15（快照 16:40 ET）

📊 市场环境

SPY $771.79 ｜ QQQ $728.00
VIX 16.46 ↓2.4%（5D +6.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-15

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 1.3 ｜ 前值 0.5　✅ 今日已公布
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 0.8 ｜ 前值 1.3　✅ 今日已公布
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布　⏰ 今日

🔍 重点速览
🔴 **事件差分**: 10-16（1D）ATM IV 78.8% vs 10-23 63.0%（差 +15.8pp），覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-16 190C ΔOI +2,364（距现价 +3.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 167.84 → 收盘 183.81（+9.5%） ｜ 今日高 185.49 ｜ 低 165.80 ｜ 昨收 172.89 → 收盘 183.81（+6.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.57 | OI比 0.79 | ATM IV 78.8% | Skew -0.2pp | Term 0.89 | ExpMove ±3.2%（近端） | Rank 59%
量化视角： IV 中性（Rank 59%）｜期限结构倒挂（Term 0.89，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.79）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.57×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.79×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（1D）±3.2% ｜ 10-23（8D）±7.5% ｜ 10-30（15D）±11.8% ｜ 11-06（22D）±14.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 38,264,588 | GEX Change vs 上次快照 49,910,462 | Flip: Primary Flip: 173.02（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 471 / LOW 134 / INVALID 217
结构观察区: Primary Flip 173.02（全链重定价，覆盖 100%）
Call Wall 200（弱结构｜现价低于该位 8.1%）
最近结构参考: Flip 173（现价高于该位 6.2%）
量化视角： 正 Gamma（3826万，无历史分位）｜由负转正（+4991万）｜现价位于 Flip 上方 6.24%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 178（MaxPain，仅结算参考）；上方 200（Call Wall，弱结构）。
• Gamma 区域：切换参考 173（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C -96 / P -2.7k ｜ Activity MEDIUM △ ｜ 1D
10-23  C +1.8k / P +1.5k ｜ Activity HIGH ｜ 8D
10-30  C +1.1k / P +0.7k ｜ Activity HIGH ｜ 15D
11-06  C +0.7k / P +0.5k ｜ Activity HIGH ｜ 22D

📆 10-16 Forward Structure
存量OI: C 139.3k / P 110.3k，今日变化ΔOI: C -96 / P -2.7k，平值价格ATM: C $2.42 / P $3.55 ｜ ATM IV 78.8%，净 delta 敞口 155k shares
Top ΔOI: C 190 +2,364 ｜ C 195 -1,681
仓位参考: Max Pain 178 ｜ Call Wall 185（+0.6%，弱）（OI 10.7k） ｜ Put Wall 170（-7.5%，弱）（OI 6.8k）
量化解读： 存量 Call 重｜ATM IV 78.8%｜历史 Rank 59%（近端代理）｜IV/RV 2.17×（近似）｜净 delta 敞口 正 154,823 股

📆 10-23 Forward Structure
存量OI: C 15.4k / P 20.8k，今日变化ΔOI: C +1.8k / P +1.5k，平值价格ATM: C $6.40 / P $7.30 ｜ ATM IV 63.0%，净 delta 敞口 61k shares
Top ΔOI: C 180 +360
仓位参考: Max Pain 182 ｜ Call Wall 190（+3.4%，弱）（OI 1.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 63.0%｜历史 Rank 59%（近端代理）｜IV/RV 1.73×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 60,993 股

📆 10-30 Forward Structure
存量OI: C 13.4k / P 11.9k，今日变化ΔOI: C +1.1k / P +0.7k，平值价格ATM: C $10.88 / P $10.90 ｜ ATM IV 72.2%，净 delta 敞口 56k shares
Top ΔOI: C 180 +262 ｜ C 200 +247
仓位参考: Max Pain 185 ｜ Call Wall 200（+8.8%）（OI 2.1k） ｜ Put Wall 180（-2.1%，弱）（OI 0.8k）
量化解读： 存量两侧均衡｜ATM IV 72.2%｜历史 Rank 59%（近端代理）｜IV/RV 1.98×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 56,109 股

📆 11-06 Forward Structure
存量OI: C 4.6k / P 7.4k，今日变化ΔOI: C +0.7k / P +0.5k，平值价格ATM: C $13.45 / P $13.34 ｜ ATM IV 79.2%，净 delta 敞口 33k shares
Top ΔOI: C 160 +205 ｜ C 175 +177
仓位参考: Max Pain 175 ｜ Call Wall 200（+8.8%）（OI 0.7k） ｜ Put Wall 170（-7.5%，弱）（OI 0.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 79.2%｜历史 Rank 59%（近端代理）｜IV/RV 2.18×（近似）｜净 delta 敞口 正 32,505 股

📅 事件差分（观察，非因果）: 10-16（1D）ATM IV 78.8% vs 10-23 63.0%（差 +15.8pp）——覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-15/COIN_evening.json